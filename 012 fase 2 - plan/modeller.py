"""
Felles modellbygger og grid-search for hoved- og scenarioanalyse.

Eksporterer:
- bygg_features(df): legger på lags, rolling mean, ukedag-dummier, kalenderfeatures
- last_kampanjeflag(indeks): leser kampanjekalender og returnerer binære flagg
- sarima_grid_search(train_y, exog): grid over (p,d,q)(P,D,Q)_s
- tune_gbm(X_train, y_train): kryss-validert søk over GBM-hyperparametere
- hybrid_prediksjon(df): kombinerer SARIMA (normale) og RF-u-lag_1 (topp)
"""

from __future__ import annotations
import warnings
from pathlib import Path
import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import TimeSeriesSplit, GridSearchCV

warnings.filterwarnings('ignore', category=UserWarning)

SESONGLENGDE = 5
KAMPANJE_STI = Path('004 data/kampanjekalender.csv')


def last_kampanjeflag(indeks: pd.DatetimeIndex) -> pd.DataFrame:
    kamp = pd.read_csv(KAMPANJE_STI, parse_dates=['startdato', 'sluttdato'])
    flag = pd.DataFrame(index=indeks)
    flag['is_crazy_days'] = 0
    flag['is_event'] = 0
    for _, rad in kamp.iterrows():
        maske = (flag.index >= rad['startdato']) & (flag.index <= rad['sluttdato'])
        if rad['type'] == 'crazy_days':
            flag.loc[maske, 'is_crazy_days'] = 1
        elif rad['type'] == 'event':
            flag.loc[maske, 'is_event'] = 1
    return flag


def bygg_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.join(last_kampanjeflag(df.index))
    df['lag_1'] = df['faktisk_ettersporsel'].shift(1)
    df['lag_5'] = df['faktisk_ettersporsel'].shift(SESONGLENGDE)
    df['lag_10'] = df['faktisk_ettersporsel'].shift(2 * SESONGLENGDE)
    df['rolling_mean_5'] = df['faktisk_ettersporsel'].shift(1).rolling(window=SESONGLENGDE).mean()
    df['ukedag'] = df.index.dayofweek
    df['is_monday'] = (df['ukedag'] == 0).astype(int)
    df['month'] = df.index.month
    df['week_of_month'] = ((df.index.day - 1) // 7) + 1
    df['days_since_last_order'] = df.index.to_series().diff().dt.days.fillna(1).astype(int)
    df = pd.concat([df, pd.get_dummies(df['ukedag'], prefix='day')], axis=1)
    return df


def sarima_grid_search(
    train_y: pd.Series,
    exog: pd.DataFrame | None = None,
    p_max: int = 2, d_max: int = 1, q_max: int = 2,
    P_max: int = 1, D_max: int = 1, Q_max: int = 1,
) -> tuple[pd.DataFrame, tuple]:
    """Grid over (p,d,q)(P,D,Q)_s. Returnerer grid-DataFrame og beste (order, seasonal_order)."""
    resultater = []
    for p in range(p_max + 1):
        for d in range(d_max + 1):
            for q in range(q_max + 1):
                for P in range(P_max + 1):
                    for D in range(D_max + 1):
                        for Q in range(Q_max + 1):
                            order = (p, d, q)
                            seas = (P, D, Q, SESONGLENGDE)
                            try:
                                mod = sm.tsa.statespace.SARIMAX(
                                    train_y, exog=exog, order=order, seasonal_order=seas,
                                    enforce_stationarity=False, enforce_invertibility=False,
                                )
                                res = mod.fit(disp=False, maxiter=50)
                                resultater.append({
                                    'order': str(order), 'seasonal_order': str(seas),
                                    'aic': res.aic, 'bic': res.bic,
                                    'konvergerte': res.mle_retvals.get('converged', False),
                                })
                            except Exception as e:
                                resultater.append({
                                    'order': str(order), 'seasonal_order': str(seas),
                                    'aic': np.nan, 'bic': np.nan, 'konvergerte': False,
                                    'feil': str(e)[:60],
                                })
    grid = pd.DataFrame(resultater).sort_values('aic').reset_index(drop=True)
    konv = grid[grid['konvergerte'] & grid['aic'].notna()]
    beste = konv.iloc[0] if len(konv) > 0 else grid.iloc[0]
    return grid, (eval(beste['order']), eval(beste['seasonal_order']))


def tune_gbm(
    X_train: pd.DataFrame, y_train: pd.Series, seed: int = 42,
) -> tuple[GradientBoostingRegressor, dict, pd.DataFrame]:
    """Kryssvalidert søk over GBM-hyperparametere med TimeSeriesSplit."""
    param_grid = {
        'learning_rate': [0.05, 0.1],
        'max_depth': [2, 3],
        'n_estimators': [100, 200],
        'subsample': [0.8, 1.0],
    }
    tscv = TimeSeriesSplit(n_splits=3)
    base = GradientBoostingRegressor(random_state=seed)
    # scoring='neg_mean_absolute_error' minimerer MAE
    søk = GridSearchCV(
        base, param_grid, cv=tscv, scoring='neg_mean_absolute_error', n_jobs=1,
    )
    søk.fit(X_train, y_train)
    cv_resultater = pd.DataFrame(søk.cv_results_)[
        ['params', 'mean_test_score', 'std_test_score']
    ].copy()
    cv_resultater['mae_cv'] = -cv_resultater['mean_test_score']
    cv_resultater = cv_resultater.sort_values('mae_cv').reset_index(drop=True)
    return søk.best_estimator_, søk.best_params_, cv_resultater


def hybrid_prediksjon(
    test: pd.DataFrame,
    pred_sarima_col: str,
    pred_rf_uten_lag1_col: str,
) -> pd.Series:
    """
    Kampanjebasert hybrid: kampanjedager (is_crazy_days=1 eller is_event=1) →
    RF uten lag_1. Ellers → SARIMA. Enkel regelbasert routing.
    """
    er_kampanje = (test['is_crazy_days'] == 1) | (test['is_event'] == 1)
    hybrid = test[pred_sarima_col].copy()
    hybrid.loc[er_kampanje] = test.loc[er_kampanje, pred_rf_uten_lag1_col]
    return hybrid


def hybrid_terskelbasert(
    test: pd.DataFrame,
    pred_sarima_col: str,
    pred_rf_uten_lag1_col: str,
    terskel: float,
) -> pd.Series:
    """
    Terskelbasert hybrid: rute etter RF-u-lag_1s egen prediksjon. Hvis RF mener
    at dagen blir > terskel (90. persentil fra trening) → bruk RF-u-lag_1.
    Ellers → SARIMA.

    Merk: Vi ruter etter RF's prediksjon, ikke SARIMA's, fordi SARIMA
    systematisk underpredikerer toppdager (bias << 0) og derfor aldri selv
    melder "her kommer en topp". RF-u-lag_1 er mer balansert og fanger opp
    toppdager uavhengig av kampanjeflagg.
    """
    er_topp = test[pred_rf_uten_lag1_col] > terskel
    hybrid = test[pred_sarima_col].copy()
    hybrid.loc[er_topp] = test.loc[er_topp, pred_rf_uten_lag1_col]
    return hybrid


def holt_winters_prediksjon(
    train_y: pd.Series, test_y: pd.Series,
) -> pd.Series:
    """
    Holt-Winters eksponensiell utjevning med additiv sesong (s=5 virkedager).
    Brukes som klassisk tredje baseline ved siden av Seasonal Naive og SARIMA.
    """
    from statsmodels.tsa.holtwinters import ExponentialSmoothing
    # initialization_method='estimated' lar modellen finne start-nivå/-trend fra data
    modell = ExponentialSmoothing(
        train_y.values,
        trend='add',
        seasonal='add',
        seasonal_periods=SESONGLENGDE,
        initialization_method='estimated',
    )
    res = modell.fit(optimized=True)
    pred = res.forecast(len(test_y))
    return pd.Series(pred, index=test_y.index)


def ljung_box_test(residualer: pd.Series, lags: int = 10) -> dict:
    """
    Ljung-Box Q-test for autokorrelasjon i residualer. Nullhypotesen er at
    residualene er uavhengige. p-verdi < 0.05 → avvises (residualer har mønster).
    """
    from statsmodels.stats.diagnostic import acorr_ljungbox
    res = residualer.dropna()
    if len(res) < lags + 2:
        return {'lags': lags, 'q_stat': np.nan, 'p_verdi': np.nan, 'avvist_H0': None}
    lb = acorr_ljungbox(res, lags=[lags], return_df=True)
    return {
        'lags': lags,
        'q_stat': float(lb['lb_stat'].iloc[0]),
        'p_verdi': float(lb['lb_pvalue'].iloc[0]),
        'avvist_H0': bool(lb['lb_pvalue'].iloc[0] < 0.05),
    }


def adf_test(serie: pd.Series) -> dict:
    """
    Augmented Dickey-Fuller-test for stasjonaritet. Nullhypotesen er at serien
    har en enhetsrot (ikke-stasjonær). p-verdi < 0.05 → avvises (stasjonær).
    """
    from statsmodels.tsa.stattools import adfuller
    s = serie.dropna()
    adf = adfuller(s, autolag='AIC')
    return {
        'adf_stat': float(adf[0]),
        'p_verdi': float(adf[1]),
        'brukte_lags': int(adf[2]),
        'n_obs': int(adf[3]),
        'kritisk_1pct': float(adf[4]['1%']),
        'kritisk_5pct': float(adf[4]['5%']),
        'stasjonaer': bool(adf[1] < 0.05),
    }
