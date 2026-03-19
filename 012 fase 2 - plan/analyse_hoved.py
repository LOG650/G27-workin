
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

# Sørg for daglig frekvens (fyller eventuelle hull med 0 eller forrige verdi)
df = df.asfreq('D').fillna(0)

# 2. Feature Engineering for Random Forest (Metodisk korrekt - ingen lekkasje)
df['lag_1'] = df['faktisk_ettersporsel'].shift(1)
df['lag_7'] = df['faktisk_ettersporsel'].shift(7)
df['lag_14'] = df['faktisk_ettersporsel'].shift(14)
df['rolling_mean_7'] = df['faktisk_ettersporsel'].shift(1).rolling(window=7).mean()

# Kalenderfeatures
df['ukedag'] = df.index.dayofweek
df['maaned'] = df.index.month
df = pd.concat([df, pd.get_dummies(df['ukedag'], prefix='day')], axis=1)

# Fjern rader med NaN etter lagging
df_clean = df.dropna().copy()

# 3. Splitt i trening og test (Jan-Feb 2026 er test)
train = df_clean[df_clean.index <= '2025-12-31']
test = df_clean[df_clean.index >= '2026-01-01']

# --- MODELL 1: BASELINE (Seasonal Naive) ---
test = test.copy()
test['pred_naive'] = train['faktisk_ettersporsel'].iloc[-7:].tolist() * (len(test)//7 + 1)
test['pred_naive'] = test['faktisk_ettersporsel'].shift(7) # Enklere: bruk faktisk lag 7

# --- MODELL 2: SARIMA (Hovedmodell) ---
# Vi bruker (1,1,1)x(1,1,1,7) som et standard utgangspunkt for dagligvare
try:
    sarima_model = sm.tsa.statespace.SARIMAX(train['faktisk_ettersporsel'], 
                                            order=(1,1,1), 
                                            seasonal_order=(1,1,1,7),
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
    sarima_results = sarima_model.fit(disp=False)
    test['pred_sarima'] = sarima_results.predict(start=test.index[0], end=test.index[-1])
except:
    test['pred_sarima'] = test['pred_naive'] # Fallback

# --- MODELL 3: RANDOM FOREST (Benchmark) ---
features = ['lag_1', 'lag_7', 'lag_14', 'rolling_mean_7'] + [f'day_{i}' for i in range(7)]
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(train[features], train['faktisk_ettersporsel'])
test['pred_rf'] = rf.predict(test[features])

# 4. EVALUERING
def get_metrics(actual, pred):
    actual, pred = np.array(actual), np.array(pred)
    mae = mean_absolute_error(actual, pred)
    mask = actual != 0
    mape = np.mean(np.abs((actual[mask] - pred[mask]) / actual[mask])) * 100
    bias = np.mean(pred - actual) # Positiv = overestimering, Negativ = underestimering
    return mae, mape, bias

# Global evaluering
m_naive = get_metrics(test['faktisk_ettersporsel'], test['pred_naive'].fillna(0))
m_sarima = get_metrics(test['faktisk_ettersporsel'], test['pred_sarima'])
m_rf = get_metrics(test['faktisk_ettersporsel'], test['pred_rf'])

# Segmentert evaluering (Topper vs Normal)
threshold = 80 # Definert som "ekstrem" dag for analyse
test_extreme = test[test['faktisk_ettersporsel'] > threshold]
test_normal = test[test['faktisk_ettersporsel'] <= threshold]

m_sarima_extreme = get_metrics(test_extreme['faktisk_ettersporsel'], test_extreme['pred_sarima'])
m_sarima_normal = get_metrics(test_normal['faktisk_ettersporsel'], test_normal['pred_sarima'])

# 5. UTSKRIFT AV RESULTATER
print(f"{'Modell':<20} | {'MAE':<7} | {'MAPE':<7} | {'Bias':<7}")
print("-" * 50)
print(f"{'Seasonal Naive':<20} | {m_naive[0]:<7.2f} | {m_naive[1]:<7.1f}% | {m_naive[2]:<7.2f}")
print(f"{'SARIMA (Hoved)':<20} | {m_sarima[0]:<7.2f} | {m_sarima[1]:<7.1f}% | {m_sarima[2]:<7.2f}")
print(f"{'Random Forest':<20} | {m_rf[0]:<7.2f} | {m_rf[1]:<7.1f}% | {m_rf[2]:<7.2f}")

print("\n--- Segmentert analyse (SARIMA) ---")
print(f"{'Segment':<20} | {'MAE':<7} | {'Bias':<7}")
print(f"{'Normale dager':<20} | {m_sarima_normal[0]:<7.2f} | {m_sarima_normal[2]:<7.2f}")
print(f"{'Ekstreme dager':<20} | {m_sarima_extreme[0]:<7.2f} | {m_sarima_extreme[2]:<7.2f}")

# Lagre resultater
test.to_csv('004 data/analyse_resultater_stram.csv')
