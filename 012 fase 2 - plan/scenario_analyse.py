"""
Scenarioanalyse: sammenligner Scenario 1 (blind prognose) mot Scenario 2
(med kampanje-/hendelsesinfo) for Lasagne Familiepakning, RD Trondheim.

Begge scenarier kjøres med seks modeller:
  1. Seasonal Naive, 2. SARIMA (grid), 3. Random Forest, 4. RF uten lag_1,
  5. Gradient Boosting (tunet), 6. Hybrid (SARIMA rutine + RF-u-lag_1 kampanje).

Scenario 2 legger til `is_crazy_days` og `is_event` som eksogene/feature-
variabler. Hybrid er kun definert i Scenario 2 (krever kampanjeflagg for routing).
"""

import warnings
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import statsmodels.api as sm
import matplotlib.pyplot as plt

from metrics import all_metrics
from modeller import (
    SESONGLENGDE, bygg_features, sarima_grid_search, tune_gbm,
    hybrid_prediksjon, hybrid_terskelbasert, holt_winters_prediksjon,
)

warnings.filterwarnings('ignore', category=UserWarning)

DATA_STI = Path('004 data/vasket_salg_daglig.csv')
FIGUR_STI = Path('014 fase 4 - report/figurer/fig_scenario_sammenligning.png')
RESULTAT_STI = Path('004 data/scenario_resultater.csv')
SAMMENDRAG_STI = Path('004 data/scenario_sammendrag.csv')

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
    threshold_top = train['faktisk_ettersporsel'].quantile(KVANTIL_TOPP)

    rf_base = (
        ['lag_1', 'lag_5', 'lag_10', 'rolling_mean_5',
         'is_monday', 'month', 'week_of_month', 'days_since_last_order']
        + [c for c in df_clean.columns if c.startswith('day_')]
    )
    exog_cols = ['is_crazy_days', 'is_event']
    rf_ext = rf_base + exog_cols
    rf_ext_uten_lag1 = [f for f in rf_ext if f != 'lag_1']

    # ---- SARIMA grid for Scenario 1 (uten exog) og Scenario 2 (med exog) ----
    print('Grid-search SARIMA, Scenario 1 (uten exog)...')
    _, (s1_order, s1_seas) = sarima_grid_search(train['faktisk_ettersporsel'], exog=None)
    print(f'  S1 beste: {s1_order} × {s1_seas}')
    print('Grid-search SARIMA, Scenario 2 (med exog)...')
    _, (s2_order, s2_seas) = sarima_grid_search(train['faktisk_ettersporsel'], exog=train[exog_cols])
    print(f'  S2 beste: {s2_order} × {s2_seas}')

    # ---- Seasonal Naive (lik i begge scenarier) ----
    full_series = pd.concat([train['faktisk_ettersporsel'], test['faktisk_ettersporsel']])
    test['s1_naive'] = full_series.shift(SESONGLENGDE).loc[test.index]
    test['s2_naive'] = test['s1_naive']

    # ---- Holt-Winters (lik i begge scenarier, ingen exog) ----
    hw_pred = holt_winters_prediksjon(train['faktisk_ettersporsel'], test['faktisk_ettersporsel'])
    test['s1_hw'] = hw_pred
    test['s2_hw'] = hw_pred

    # ---- Scenario 1: blind prognose ----
    # SARIMA
    s1_mod = sm.tsa.statespace.SARIMAX(
        train['faktisk_ettersporsel'], order=s1_order, seasonal_order=s1_seas,
        enforce_stationarity=False, enforce_invertibility=False,
    )
    s1_res = s1_mod.fit(disp=False)
    test['s1_sarima'] = s1_res.predict(start=test.index[0], end=test.index[-1])

    # RF og RF uten lag_1
    s1_rf = RandomForestRegressor(n_estimators=RF_ESTIMATORS, random_state=RF_SEED)
    s1_rf.fit(train[rf_base], train['faktisk_ettersporsel'])
    test['s1_rf'] = s1_rf.predict(test[rf_base])

    s1_rf_d = RandomForestRegressor(n_estimators=RF_ESTIMATORS, random_state=RF_SEED)
    s1_rf_d.fit(train[[f for f in rf_base if f != 'lag_1']], train['faktisk_ettersporsel'])
    test['s1_rf_uten_lag1'] = s1_rf_d.predict(test[[f for f in rf_base if f != 'lag_1']])

    # GBM tunet
    print('GBM tuning Scenario 1...')
    s1_gbm, _, _ = tune_gbm(train[rf_base], train['faktisk_ettersporsel'], seed=RF_SEED)
    test['s1_gbm'] = s1_gbm.predict(test[rf_base])

    # ---- Scenario 2: historikk + kampanjer ----
    s2_mod = sm.tsa.statespace.SARIMAX(
        train['faktisk_ettersporsel'], exog=train[exog_cols],
        order=s2_order, seasonal_order=s2_seas,
        enforce_stationarity=False, enforce_invertibility=False,
    )
    s2_res = s2_mod.fit(disp=False)
    test['s2_sarima'] = s2_res.predict(
        start=test.index[0], end=test.index[-1], exog=test[exog_cols]
    )

    s2_rf = RandomForestRegressor(n_estimators=RF_ESTIMATORS, random_state=RF_SEED)
    s2_rf.fit(train[rf_ext], train['faktisk_ettersporsel'])
    test['s2_rf'] = s2_rf.predict(test[rf_ext])

    s2_rf_d = RandomForestRegressor(n_estimators=RF_ESTIMATORS, random_state=RF_SEED)
    s2_rf_d.fit(train[rf_ext_uten_lag1], train['faktisk_ettersporsel'])
    test['s2_rf_uten_lag1'] = s2_rf_d.predict(test[rf_ext_uten_lag1])

    print('GBM tuning Scenario 2...')
    s2_gbm, _, _ = tune_gbm(train[rf_ext], train['faktisk_ettersporsel'], seed=RF_SEED)
    test['s2_gbm'] = s2_gbm.predict(test[rf_ext])

    # Hybridmodeller kun i Scenario 2
    test['s2_hybrid_kamp'] = hybrid_prediksjon(test, 's2_sarima', 's2_rf_uten_lag1')
    test['s2_hybrid_terskel'] = hybrid_terskelbasert(
        test, 's2_sarima', 's2_rf_uten_lag1', terskel=threshold_top,
    )

    # ---- Evaluering ----
    def collect_res(df_seg: pd.DataFrame, segment_navn: str) -> list[dict]:
        rader = []
        for scen in [1, 2]:
            modeller = ['naive', 'hw', 'sarima', 'rf', 'rf_uten_lag1', 'gbm']
            if scen == 2:
                modeller.extend(['hybrid_kamp', 'hybrid_terskel'])
            for mod in modeller:
                col = f's{scen}_{mod}'
                df_eval = df_seg.dropna(subset=[col])
                m = all_metrics(df_eval['faktisk_ettersporsel'], df_eval[col])
                rader.append({
                    'Scenario': f'Scenario {scen}', 'Modell': mod.upper(),
                    'Segment': segment_navn, **m,
                })
        return rader

    test_normal = test[test['faktisk_ettersporsel'] <= threshold_top]
    test_top = test[test['faktisk_ettersporsel'] > threshold_top]
    res_rader = (
        collect_res(test, 'Alle testdager')
        + collect_res(test_normal, 'Normale dager')
        + collect_res(test_top, 'Toppdager')
    )
    res_df = pd.DataFrame(res_rader)
    res_df.to_csv(SAMMENDRAG_STI, index=False)

    # ---- Visualisering: hybrid og to RF-varianter mot faktisk ----
    FIGUR_STI.parent.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(13, 6))
    plt.plot(test.index, test['faktisk_ettersporsel'], label='Faktisk', color='black', linewidth=2)
    plt.plot(test.index, test['s1_rf'], label='RF S1 (blind)', linestyle='--', color='red', alpha=0.7)
    plt.plot(test.index, test['s2_rf_uten_lag1'], label='RF u/lag_1 S2', color='orange', alpha=0.8)
    plt.plot(test.index, test['s2_hybrid_terskel'], label='Hybrid terskel S2', color='green', linewidth=2, alpha=0.9)
    kampanjedager = test[test['is_crazy_days'] == 1]
    if not kampanjedager.empty:
        plt.axvspan(kampanjedager.index.min(), kampanjedager.index.max(),
                    color='blue', alpha=0.1, label='Crazy Days')
    plt.title('Scenario 1 vs Scenario 2 — RF, RF u/lag_1 og Hybrid (virkedagsdata, s=5)')
    plt.xlabel('Dato')
    plt.ylabel('Etterspørsel (stk)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(FIGUR_STI)
    plt.close()

    # ---- Utskrift ----
    print(f'\nTreningssett: {len(train)}, Testsett: {len(test)} ({len(test_normal)}n + {len(test_top)}t)')
    print(f'Terskel 90. persentil: {threshold_top:.1f}')
    for seg in ['Alle testdager', 'Normale dager', 'Toppdager']:
        print(f'\n--- {seg} ---')
        print(res_df[res_df['Segment'] == seg]
              .drop(columns='Segment').round(2).to_string(index=False))

    test.to_csv(RESULTAT_STI)
    print(f'\nLagret: {RESULTAT_STI}, {SAMMENDRAG_STI}')


if __name__ == '__main__':
    main()
