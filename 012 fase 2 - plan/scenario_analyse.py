
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import statsmodels.api as sm
import matplotlib.pyplot as plt

# 1. Last inn og klargjør data
df = pd.read_csv('004 data/vasket_salg_daglig.csv', parse_dates=['dato'])
df = df.sort_values('dato')
df.set_index('dato', inplace=True)
df = df.asfreq('D').fillna(0)

# 2. Feature Engineering
iso = df.index.isocalendar()
df['is_crazy_days'] = 0
df.loc[(iso.year == 2025) & (iso.week == 45), 'is_crazy_days'] = 1
df.loc[(iso.year == 2026) & (iso.week == 5), 'is_crazy_days'] = 1

df['is_event'] = 0
df.loc[(iso.year == 2025) & (iso.week == 16), 'is_event'] = 1  # Påske
df.loc[(iso.year == 2025) & (iso.week == 33), 'is_event'] = 1  # Skolestart
df.loc[(iso.year == 2025) & (iso.week == 51), 'is_event'] = 1  # Jul

df['lag_1'] = df['faktisk_ettersporsel'].shift(1)
df['lag_7'] = df['faktisk_ettersporsel'].shift(7)
df['lag_14'] = df['faktisk_ettersporsel'].shift(14)
df['rolling_mean_7'] = df['faktisk_ettersporsel'].shift(1).rolling(window=7).mean()

df['ukedag'] = df.index.dayofweek
df = pd.concat([df, pd.get_dummies(df['ukedag'], prefix='day')], axis=1)
df_clean = df.dropna().copy()

# Splitt Trening/Test
train = df_clean[df_clean.index <= '2025-12-31']
test = df_clean[df_clean.index >= '2026-01-01'].copy()
threshold_top = train['faktisk_ettersporsel'].quantile(0.90)

def get_metrics(actual, pred):
    actual, pred = np.array(actual), np.array(pred)
    mae = mean_absolute_error(actual, pred)
    mask = (actual != 0)
    mape = np.mean(np.abs((actual[mask] - pred[mask]) / actual[mask])) * 100 if any(mask) else 0
    bias = np.mean(pred - actual)
    return mae, mape, bias

results = []

# --- SCENARIO 1: KUN HISTORIKK ---
# 1. Seasonal Naive
full_series = pd.concat([train['faktisk_ettersporsel'], test['faktisk_ettersporsel']])
test['s1_naive'] = full_series.shift(7).loc[test.index]

# 2. SARIMA (Ingen exog)
s1_sarima_mod = sm.tsa.statespace.SARIMAX(train['faktisk_ettersporsel'], order=(1,1,1), seasonal_order=(1,1,1,7))
s1_sarima_res = s1_sarima_mod.fit(disp=False)
test['s1_sarima'] = s1_sarima_res.predict(start=test.index[0], end=test.index[-1])

# 3. Random Forest (Ingen kampanje-features)
s1_rf_feats = ['lag_1', 'lag_7', 'lag_14', 'rolling_mean_7'] + [f'day_{i}' for i in range(7)]
rf1 = RandomForestRegressor(n_estimators=100, random_state=42)
rf1.fit(train[s1_rf_feats], train['faktisk_ettersporsel'])
test['s1_rf'] = rf1.predict(test[s1_rf_feats])

# --- SCENARIO 2: HISTORIKK + KAMPANJER ---
exog_cols = ['is_crazy_days', 'is_event']
# 1. Seasonal Naive (Identisk i S2)
test['s2_naive'] = test['s1_naive']

# 2. SARIMAX (Med exog)
s2_sarima_mod = sm.tsa.statespace.SARIMAX(train['faktisk_ettersporsel'], exog=train[exog_cols], order=(1,1,1), seasonal_order=(1,1,1,7))
s2_sarima_res = s2_sarima_mod.fit(disp=False)
test['s2_sarima'] = s2_sarima_res.predict(start=test.index[0], end=test.index[-1], exog=test[exog_cols])

# 3. Random Forest (Med kampanje-features)
s2_rf_feats = s1_rf_feats + exog_cols
rf2 = RandomForestRegressor(n_estimators=100, random_state=42)
rf2.fit(train[s2_rf_feats], train['faktisk_ettersporsel'])
test['s2_rf'] = rf2.predict(test[s2_rf_feats])

# --- EVALUERING ---
def collect_res(df_seg, segment_name):
    rows = []
    for scen in [1, 2]:
        for mod in ['naive', 'sarima', 'rf']:
            col = f's{scen}_{mod}'
            mae, mape, bias = get_metrics(df_seg['faktisk_ettersporsel'], df_seg[col])
            rows.append({'Scenario': f'Scenario {scen}', 'Modell': mod.upper(), 'Segment': segment_name, 'MAE': mae, 'MAPE': mape, 'Bias': bias})
    return rows

test_normal = test[test['faktisk_ettersporsel'] <= threshold_top]
test_top = test[test['faktisk_ettersporsel'] > threshold_top]

final_results = collect_res(test_normal, 'Normal') + collect_res(test_top, 'Toppdager')
res_df = pd.DataFrame(final_results)

# --- VISUALISERING ---
plt.figure(figsize=(12, 6))
plt.plot(test.index, test['faktisk_ettersporsel'], label='Faktisk', color='black', linewidth=2)
plt.plot(test.index, test['s1_rf'], label='RF Scenario 1 (Blind)', linestyle='--', color='red', alpha=0.7)
plt.plot(test.index, test['s2_rf'], label='RF Scenario 2 (Info)', color='green', alpha=0.8)
plt.axvline(pd.Timestamp('2026-01-26'), color='blue', linestyle=':', alpha=0.3, label='Kampanjestart')
plt.title('Sammenligning Scenario 1 vs Scenario 2 (Fokus på Toppdager)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('014 fase 4 - report/figurer/fig_scenario_sammenligning.png')

# Print tabeller
print("\n--- SAMMENLIGNINGSTABELL: NORMALE DAGER ---")
print(res_df[res_df['Segment'] == 'Normal'].drop(columns='Segment').to_string(index=False))

print("\n--- SAMMENLIGNINGSTABELL: TOPPDAGER ---")
print(res_df[res_df['Segment'] == 'Toppdager'].drop(columns='Segment').to_string(index=False))

# Lagre data
test.to_csv('004 data/scenario_resultater.csv')
