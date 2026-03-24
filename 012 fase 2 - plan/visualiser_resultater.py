
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Opprett figurer-mappe hvis den ikke finnes
os.makedirs('014 fase 4 - report/figurer', exist_ok=True)

# 2. Last inn de nyeste analyse-resultatene
df = pd.read_csv('004 data/analyse_resultater_stram.csv', parse_dates=['dato'])
df = df.sort_values('dato')

# Sett stil
sns.set_theme(style="whitegrid")
plt.figure(figsize=(14, 10))

# --- FIGUR 3: SAMMENLIGNING AV MODELLER (TESTSETT) ---
plt.subplot(2, 1, 1)
plt.plot(df['dato'], df['faktisk_ettersporsel'], label='Faktisk etterspørsel', color='black', linewidth=2, marker='o', markersize=4)
plt.plot(df['dato'], df['pred_naive'], label='Baseline (Seasonal Naive)', linestyle='--', alpha=0.7, color='red')
plt.plot(df['dato'], df['pred_rf'], label='Random Forest (m/ Kampanjer)', linewidth=2, color='green', alpha=0.8)

# Marker Crazy Days i uke 5 2026
cd_dates = df[df['is_crazy_days'] == 1]['dato']
if not cd_dates.empty:
    plt.axvspan(cd_dates.min(), cd_dates.max(), color='blue', alpha=0.1, label='Crazy Days Periode')

plt.title('Figur 3: Faktisk etterspørsel vs. Prediksjoner (Januar - Februar 2026)', fontsize=14)
plt.ylabel('Antall enheter', fontsize=12)
plt.legend(loc='upper left')

# --- FIGUR 4: FEILMARGINER (MAE) PER DAG ---
plt.subplot(2, 1, 2)
df['error_naive'] = abs(df['faktisk_ettersporsel'] - df['pred_naive'])
df['error_rf'] = abs(df['faktisk_ettersporsel'] - df['pred_rf'])

plt.fill_between(df['dato'], df['error_naive'], label='Feil: Baseline (MAE)', alpha=0.3, color='red')
plt.fill_between(df['dato'], df['error_rf'], label='Feil: Random Forest (MAE)', alpha=0.3, color='green')

plt.title('Figur 4: Absolutt feil (MAE) per dag', fontsize=14)
plt.xlabel('Dato', fontsize=12)
plt.ylabel('Absolutt feil (Enheter)', fontsize=12)
plt.legend(loc='upper left')

plt.tight_layout()
plt.savefig('014 fase 4 - report/figurer/fig3_4_modellsammenligning.png')

# --- FIGUR 5: FORKLARING AV KAMPANJEEFFEKT (CRAZY DAYS) ---
plt.figure(figsize=(10, 6))
sns.boxplot(x='is_crazy_days', y='faktisk_ettersporsel', data=df)
plt.title('Figur 5: Etterspørselsfordeling med og uten "Crazy Days"', fontsize=14)
plt.xlabel('Er Crazy Day? (0 = Nei, 1 = Ja)', fontsize=12)
plt.ylabel('Antall enheter (dpak)', fontsize=12)
plt.xticks([0, 1], ['Normal drift', 'Crazy Days'])

plt.tight_layout()
plt.savefig('014 fase 4 - report/figurer/fig5_kampanjeeffekt.png')

print("Visualisering fullført! Figurer er lagret i '014 fase 4 - report/figurer/'.")
