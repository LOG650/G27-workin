
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# 1. Last inn data
df = pd.read_csv('004 data/vasket_salg_daglig.csv', parse_dates=['dato'])
df['dato'] = pd.to_datetime(df['dato'])
df = df.sort_values('dato')

# 2. Lag features (Ukedag og Crazy Days)
df['ukedag'] = df['dato'].dt.dayofweek
df['is_crazy_day'] = (df['faktisk_ettersporsel'] > 100).astype(int)

# One-hot encoding for ukedag (0=Mandag, 6=Søndag)
df = pd.concat([df, pd.get_dummies(df['ukedag'], prefix='day')], axis=1)

# 3. Splitt i trening og test (slik det er definert i kapittel 5.5)
train = df[df['dato'] <= '2025-12-31'].copy()
test = df[df['dato'] >= '2026-01-01'].copy()

# 4. Modellering: Regresjon med ukedag og Crazy Days
features = [f'day_{i}' for i in range(7)] + ['is_crazy_day']
X_train = train[features]
y_train = train['faktisk_ettersporsel']
X_test = test[features]
y_test = test['faktisk_ettersporsel']

model = LinearRegression()
model.fit(X_train, y_train)

# 5. Prediksjon
test['pred_reg'] = model.predict(X_test)

# 6. Baseline: Seasonal Naive (SN) - bruker verdi fra nøyaktig 7 dager siden
# Vi må koble på historiske verdier for testsettet
df_all = df.copy()
df_all['pred_sn'] = df_all['faktisk_ettersporsel'].shift(7)
test = test.merge(df_all[['dato', 'pred_sn']], on='dato', how='left')

# 7. Evaluering (MAE)
mae_reg = mean_absolute_error(test['faktisk_ettersporsel'], test['pred_reg'])
mae_sn = mean_absolute_error(test['faktisk_ettersporsel'], test['pred_sn'].fillna(0))

# 8. Beregn MAPE (håndterer 0-verdier ved å ekskludere dem)
def calculate_mape(actual, forecast):
    actual, forecast = np.array(actual), np.array(forecast)
    mask = actual != 0
    return np.mean(np.abs((actual[mask] - forecast[mask]) / actual[mask])) * 100

mape_reg = calculate_mape(test['faktisk_ettersporsel'], test['pred_reg'])
mape_sn = calculate_mape(test['faktisk_ettersporsel'], test['pred_sn'].fillna(0))

print(f"--- Evaluering på Testsett (Jan-Feb 2026) ---")
print(f"Baseline (Seasonal Naive): MAE = {mae_sn:.2f}, MAPE = {mape_sn:.2f}%")
print(f"Ny Modell (Regresjon + CrazyDays): MAE = {mae_reg:.2f}, MAPE = {mape_reg:.2f}%")

# Lagre resultater for rapporten
test.to_csv('004 data/prediksjoner_avansert.csv', index=False)
