
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Opprett figurer-mappe hvis den ikke finnes
os.makedirs('014 fase 4 - report/figurer', exist_ok=True)

# 2. Last inn prediksjonsdataene vi genererte
df = pd.read_csv('004 data/prediksjoner_avansert.csv', parse_dates=['dato'])
df = df.sort_values('dato')

# Sett stil
sns.set_theme(style="whitegrid")
plt.figure(figsize=(14, 8))

# --- FIGUR 3: SAMMENLIGNING AV MODELLER (TESTSETT) ---
plt.subplot(2, 1, 1)
plt.plot(df['dato'], df['faktisk_ettersporsel'], label='Faktisk etterspørsel', color='black', linewidth=2, marker='o', markersize=4)
plt.plot(df['dato'], df['pred_sn'], label='Baseline (Seasonal Naive)', linestyle='--', alpha=0.7, color='red')
plt.plot(df['dato'], df['pred_reg'], label='Ny Modell (Regresjon + CD)', linewidth=2, color='green')

plt.title('Figur 3: Faktisk etterspørsel vs. Prediksjoner (Januar - Februar 2026)', fontsize=14)
plt.ylabel('Antall enheter', fontsize=12)
plt.legend()

# --- FIGUR 4: FEILMARGINER (MAE) PER DAG ---
plt.subplot(2, 1, 2)
df['error_sn'] = abs(df['faktisk_ettersporsel'] - df['pred_sn'])
df['error_reg'] = abs(df['faktisk_ettersporsel'] - df['pred_reg'])

plt.fill_between(df['dato'], df['error_sn'], label='Feil: Baseline (MAE)', alpha=0.3, color='red')
plt.fill_between(df['dato'], df['error_reg'], label='Feil: Ny Modell (MAE)', alpha=0.3, color='green')

plt.title('Figur 4: Absolutt feil (MAE) per dag', fontsize=14)
plt.xlabel('Dato', fontsize=12)
plt.ylabel('Absolutt feil (Enheter)', fontsize=12)
plt.legend()

plt.tight_layout()
plt.savefig('014 fase 4 - report/figurer/fig3_4_modellsammenligning.png')

# --- FIGUR 5: FORKLARING AV KAMPANJEEFFEKT (CRAZY DAYS) ---
plt.figure(figsize=(10, 6))
sns.boxplot(x='is_crazy_day', y='faktisk_ettersporsel', data=df)
plt.title('Figur 5: Etterspørselsfordeling med og uten "Crazy Days"', fontsize=14)
plt.xlabel('Er Crazy Day? (0 = Nei, 1 = Ja)', fontsize=12)
plt.ylabel('Antall enheter', fontsize=12)
plt.xticks([0, 1], ['Normal drift', 'Crazy Days'])

plt.tight_layout()
plt.savefig('014 fase 4 - report/figurer/fig5_kampanjeeffekt.png')

print("Visualisering fullført! Figurer er lagret i '014 fase 4 - report/figurer/'.")
