"""
Hovedanalyse: estimerer seks modeller for daglig etterspørsel av Lasagne
Familiepakning ved RD Trondheim:

  1. Seasonal Naive (baseline, samme ukedag forrige uke)
  2. SARIMA (exog, grid-valgt parametere)
  3. Random Forest (full feature-sett)
  4. Random Forest uten lag_1 (fanger mønster i stedet for å speile i går)
  5. Gradient Boosting (kryssvalidert tunet)
  6. Hybrid (SARIMA rutine + RF-u-lag_1 kampanje)

Datagrunnlag: `vasket_salg_daglig.csv` (260 virkedager fra RELEX-eksport).
Virkedagssyklus s=5. Kampanjer leses fra `kampanjekalender.csv`.
"""

import warnings
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

from metrics import all_metrics
from modeller import (
    SESONGLENGDE, bygg_features, sarima_grid_search, tune_gbm,
    hybrid_prediksjon, hybrid_terskelbasert, holt_winters_prediksjon,
    ljung_box_test, adf_test,
)

warnings.filterwarnings('ignore', category=UserWarning)

DATA_STI = Path('004 data/vasket_salg_daglig.csv')
ACF_STI = Path('014 fase 4 - report/figurer/fig6_residual_acf.png')
RESULTAT_STI = Path('004 data/analyse_resultater_stram.csv')
GRID_STI = Path('004 data/sarima_diagnostikk.csv')
GBM_GRID_STI = Path('004 data/gbm_tuning.csv')
FI_STI = Path('004 data/rf_feature_importance.csv')
SAMMENDRAG_STI = Path('004 data/modell_sammendrag.csv')
DIAGNOSTIKK_STI = Path('004 data/residual_diagnostikk.csv')
ADF_STI_CSV = Path('004 data/adf_test.csv')

SPLITT_DATO = '2026-01-01'
KVANTIL_TOPP = 0.90
RF_SEED = 42
RF_ESTIMATORS = 100


def last_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_STI, parse_dates=['dato'])
    return df.sort_values('dato').set_index('dato')


def main() -> None:
    df = bygg_features(last_data())
    df_clean = df.dropna().copy()

    train = df_clean[df_clean.index < SPLITT_DATO]
    test = df_clean[df_clean.index >= SPLITT_DATO].copy()
    # P90 beregnes på det fulle treningssettet (218 virkedager), ikke det
    # padding-reduserte ML-settet (208 dager), slik at terskelen er felles for
    # alle modeller og uavhengig av hvilke features ML-modellene krever.
    threshold_top = df[df.index < SPLITT_DATO]['faktisk_ettersporsel'].quantile(KVANTIL_TOPP)

    exog_cols = ['is_crazy_days', 'is_event']
    rf_features = (
        ['lag_1', 'lag_5', 'lag_10', 'rolling_mean_5',
         'is_monday', 'month', 'week_of_month', 'days_since_last_order',
         'is_crazy_days', 'is_event']
        + [c for c in df_clean.columns if c.startswith('day_')]
    )
    rf_uten_lag1 = [f for f in rf_features if f != 'lag_1']

    # ---- A: SARIMA grid-search ----
    print('SARIMA grid-search (144 kombinasjoner)...')
    grid, (sarima_order, sarima_seas) = sarima_grid_search(
        train['faktisk_ettersporsel'], exog=train[exog_cols]
    )
    GRID_STI.parent.mkdir(parents=True, exist_ok=True)
    grid.to_csv(GRID_STI, index=False)
    print(f'  Beste: order={sarima_order}, seasonal={sarima_seas}, AIC={grid.iloc[0]["aic"]:.2f}')

    # ---- ADF-test på trening (stasjonaritet) ----
    adf_rå = adf_test(train['faktisk_ettersporsel'])
    adf_diff = adf_test(train['faktisk_ettersporsel'].diff().dropna())
    adf_sesong = adf_test(train['faktisk_ettersporsel'].diff(SESONGLENGDE).dropna())
    adf_df = pd.DataFrame([
        {'serie': 'rå', **adf_rå},
        {'serie': 'differensiert (1. ordens)', **adf_diff},
        {'serie': 'sesongdifferensiert (s=5)', **adf_sesong},
    ])
    adf_df.to_csv(ADF_STI_CSV, index=False)
    print(f'ADF rå: p={adf_rå["p_verdi"]:.4f} '
          f'({"stasjonær" if adf_rå["stasjonaer"] else "ikke stasjonær"})')

    # ---- Seasonal Naive ----
    full_series = pd.concat([train['faktisk_ettersporsel'], test['faktisk_ettersporsel']])
    test['pred_naive'] = full_series.shift(SESONGLENGDE).loc[test.index]

    # ---- Holt-Winters (tredje klassisk baseline) ----
    test['pred_hw'] = holt_winters_prediksjon(train['faktisk_ettersporsel'], test['faktisk_ettersporsel'])

    # ---- SARIMA ----
    sarima_mod = sm.tsa.statespace.SARIMAX(
        train['faktisk_ettersporsel'], exog=train[exog_cols],
        order=sarima_order, seasonal_order=sarima_seas,
        enforce_stationarity=False, enforce_invertibility=False,
    )
    sarima_res = sarima_mod.fit(disp=False)
    test['pred_sarima'] = sarima_res.predict(
        start=test.index[0], end=test.index[-1], exog=test[exog_cols]
    )

    # ---- Random Forest (full) ----
    rf = RandomForestRegressor(n_estimators=RF_ESTIMATORS, random_state=RF_SEED)
    rf.fit(train[rf_features], train['faktisk_ettersporsel'])
    test['pred_rf'] = rf.predict(test[rf_features])

    # ---- Random Forest uten lag_1 ----
    rf_d = RandomForestRegressor(n_estimators=RF_ESTIMATORS, random_state=RF_SEED)
    rf_d.fit(train[rf_uten_lag1], train['faktisk_ettersporsel'])
    test['pred_rf_uten_lag1'] = rf_d.predict(test[rf_uten_lag1])

    # ---- C: Gradient Boosting (tunet) ----
    print('GBM tuning (16 kombinasjoner × 3-fold TimeSeriesSplit)...')
    gbm, gbm_beste, gbm_grid = tune_gbm(train[rf_features], train['faktisk_ettersporsel'], seed=RF_SEED)
    gbm_grid.to_csv(GBM_GRID_STI, index=False)
    print(f'  Beste GBM-params: {gbm_beste}')
    test['pred_gbm'] = gbm.predict(test[rf_features])

    # ---- Hybrid (kampanjebasert) og terskelbasert hybrid ----
    test['pred_hybrid_kamp'] = hybrid_prediksjon(test, 'pred_sarima', 'pred_rf_uten_lag1')
    test['pred_hybrid_terskel'] = hybrid_terskelbasert(
        test, 'pred_sarima', 'pred_rf_uten_lag1', terskel=threshold_top,
    )

    # ---- Feature importance ----
    fi = pd.DataFrame({
        'feature': rf_features,
        'rf_importance': rf.feature_importances_,
        'gbm_importance': gbm.feature_importances_,
        'rf_uten_lag1_importance': [
            rf_d.feature_importances_[rf_uten_lag1.index(f)] if f in rf_uten_lag1 else np.nan
            for f in rf_features
        ],
    }).sort_values('rf_importance', ascending=False)
    fi.to_csv(FI_STI, index=False)

    # ---- Residualer ----
    pred_cols = ['pred_naive', 'pred_hw', 'pred_sarima', 'pred_rf', 'pred_rf_uten_lag1',
                 'pred_gbm', 'pred_hybrid_kamp', 'pred_hybrid_terskel']
    for col in pred_cols:
        test[f'res_{col.replace("pred_","")}'] = test['faktisk_ettersporsel'] - test[col]

    # ---- Ljung-Box på residualer ----
    diagnostikk = []
    for col in pred_cols:
        res_col = f'res_{col.replace("pred_","")}'
        lb = ljung_box_test(test[res_col], lags=10)
        diagnostikk.append({'modell': col.replace('pred_', ''), **lb})
    pd.DataFrame(diagnostikk).to_csv(DIAGNOSTIKK_STI, index=False)

    # ---- Evaluering ----
    modeller = [
        ('Seasonal Naive', 'pred_naive'),
        ('Holt-Winters', 'pred_hw'),
        ('SARIMA (exog)', 'pred_sarima'),
        ('Random Forest', 'pred_rf'),
        ('RF uten lag_1', 'pred_rf_uten_lag1'),
        ('Gradient Boosting', 'pred_gbm'),
        ('Hybrid (kampanje)', 'pred_hybrid_kamp'),
        ('Hybrid (terskel)', 'pred_hybrid_terskel'),
    ]

    def evaluate_segment(df_seg: pd.DataFrame, segment_navn: str) -> list[dict]:
        rader = []
        for navn, pred_col in modeller:
            df_eval = df_seg.dropna(subset=[pred_col])
            m = all_metrics(df_eval['faktisk_ettersporsel'], df_eval[pred_col])
            rader.append({'Modell': navn, 'Segment': segment_navn, **m})
        return rader

    test_normal = test[test['faktisk_ettersporsel'] <= threshold_top].copy()
    test_top = test[test['faktisk_ettersporsel'] > threshold_top].copy()
    sammendrag = (
        evaluate_segment(test, 'Alle testdager')
        + evaluate_segment(test_normal, 'Normale dager')
        + evaluate_segment(test_top, 'Toppdager')
    )
    sammendrag_df = pd.DataFrame(sammendrag)
    sammendrag_df.to_csv(SAMMENDRAG_STI, index=False)

    # ---- ACF-plot ----
    ACF_STI.parent.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(5, 1, figsize=(10, 16))
    for ax, col, tittel in [
        (axes[0], 'res_naive', 'Seasonal Naive'),
        (axes[1], 'res_hw', 'Holt-Winters'),
        (axes[2], 'res_sarima', 'SARIMA (grid)'),
        (axes[3], 'res_rf_uten_lag1', 'RF uten lag_1'),
        (axes[4], 'res_hybrid_terskel', 'Hybrid (terskel)'),
    ]:
        plot_acf(test[col].dropna(), ax=ax, lags=14, title=f'ACF – {tittel} residualer')
    plt.tight_layout()
    plt.savefig(ACF_STI)
    plt.close()

    # ---- Utskrift ----
    print(f'\nTreningssett: {len(train)} virkedager')
    print(f'Testsett: {len(test)} ({len(test_normal)} normale, {len(test_top)} topp)')
    print(f'Terskel (90. persentil): {threshold_top:.1f}')
    print(f'SARIMA AIC/BIC: {sarima_res.aic:.2f} / {sarima_res.bic:.2f}')

    for seg in ['Alle testdager', 'Normale dager', 'Toppdager']:
        print(f'\n--- {seg} ---')
        print(sammendrag_df[sammendrag_df['Segment'] == seg]
              .drop(columns='Segment').round(2).to_string(index=False))

    print('\n--- Feature importance (topp 10) ---')
    print(fi.head(10).round(4).to_string(index=False))

    print('\n--- Ljung-Box residualtest (10 lags) ---')
    diag_df = pd.DataFrame(diagnostikk)
    print(diag_df.round(4).to_string(index=False))

    print('\n--- ADF-test på trening ---')
    print(adf_df[['serie', 'adf_stat', 'p_verdi', 'stasjonaer']].round(4).to_string(index=False))

    test.to_csv(RESULTAT_STI)
    print(f'\nLagret: {RESULTAT_STI}, {SAMMENDRAG_STI}, {FI_STI}, {GRID_STI}, {GBM_GRID_STI}, {DIAGNOSTIKK_STI}, {ADF_STI_CSV}')


if __name__ == '__main__':
    main()
