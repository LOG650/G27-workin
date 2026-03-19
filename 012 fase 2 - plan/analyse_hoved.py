
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

# 1. Last inn og klargjør data
df = pd.read_csv('004 data/vasket_salg_daglig.csv', parse_dates=['dato'])
df = df.sort_values('dato')
df.set_index('dato', inplace=True)

# Sørg for daglig frekvens
df = df.asfreq('D').fillna(0)

# 2. Feature Engineering
df['lag_1'] = df['faktisk_ettersporsel'].shift(1)
df['lag_7'] = df['faktisk_ettersporsel'].shift(7)
df['lag_14'] = df['faktisk_ettersporsel'].shift(14)
df['rolling_mean_7'] = df['faktisk_ettersporsel'].shift(1).rolling(window=7).mean()

df['ukedag'] = df.index.dayofweek
df = pd.concat([df, pd.get_dummies(df['ukedag'], prefix='day')], axis=1)

df_clean = df.dropna().copy()

# 3. Splitt i trening og test
train = df_clean[df_clean.index <= '2025-12-31']
test = df_clean[df_clean.index >= '2026-01-01'].copy()

# --- MODELLERING ---
# 1. Seasonal Naive
full_series = pd.concat([train['faktisk_ettersporsel'], test['faktisk_ettersporsel']])
test['pred_naive'] = full_series.shift(7).loc[test.index]

# 2. SARIMA
sarima_model = sm.tsa.statespace.SARIMAX(train['faktisk_ettersporsel'], 
                                        order=(1,1,1), 
                                        seasonal_order=(1,1,1,7),
                                        enforce_stationarity=False,
                                        enforce_invertibility=False)
sarima_results = sarima_model.fit(disp=False)
test['pred_sarima'] = sarima_results.predict(start=test.index[0], end=test.index[-1])

# 3. Random Forest
features = ['lag_1', 'lag_7', 'lag_14', 'rolling_mean_7'] + [f'day_{i}' for i in range(7)]
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(train[features], train['faktisk_ettersporsel'])
test['pred_rf'] = rf.predict(test[features])

# --- EVALUERING ---
def get_metrics(actual, pred):
    actual, pred = np.array(actual), np.array(pred)
    mae = mean_absolute_error(actual, pred)
    mask = actual != 0
    mape = np.mean(np.abs((actual[mask] - pred[mask]) / actual[mask])) * 100
    bias = np.mean(pred - actual)
    return mae, mape, bias

# Residualer
test['res_naive'] = test['faktisk_ettersporsel'] - test['pred_naive'].fillna(0)
test['res_sarima'] = test['faktisk_ettersporsel'] - test['pred_sarima']
test['res_rf'] = test['faktisk_ettersporsel'] - test['pred_rf']

# Segmentering
threshold_top = train['faktisk_ettersporsel'].quantile(0.90)
test_normal = test[test['faktisk_ettersporsel'] <= threshold_top].copy()
test_top = test[test['faktisk_ettersporsel'] > threshold_top].copy()

def evaluate_segments(df_segment):
    res = []
    for m_name, p_col in [('Seasonal Naive', 'pred_naive'), ('SARIMA', 'pred_sarima'), ('Random Forest', 'pred_rf')]:
        df_eval = df_segment.dropna(subset=[p_col])
        mae, mape, bias = get_metrics(df_eval['faktisk_ettersporsel'], df_eval[p_col])
        res.append({'Modell': m_name, 'MAE': mae, 'MAPE': mape, 'Bias': bias})
    return pd.DataFrame(res)

results_normal = evaluate_segments(test_normal)
results_top = evaluate_segments(test_top)

# --- ACF PLOTTING ---
fig, axes = plt.subplots(3, 1, figsize=(10, 12))
plot_acf(test['res_naive'].dropna(), ax=axes[0], lags=14, title='ACF - Seasonal Naive Residualer')
plot_acf(test['res_sarima'].dropna(), ax=axes[1], lags=14, title='ACF - SARIMA Residualer')
plot_acf(test['res_rf'].dropna(), ax=axes[2], lags=14, title='ACF - Random Forest Residualer')
plt.tight_layout()
plt.savefig('014 fase 4 - report/figurer/fig6_residual_acf.png')

# --- UTSKRIFT ---
print(f"Terskelverdi: {threshold_top:.2f}")
print("\n--- NORMALE DAGER ---")
print(results_normal.to_string(index=False))
print("\n--- TOPPDAGER ---")
print(results_top.to_string(index=False))

test.to_csv('004 data/analyse_resultater_stram.csv')
