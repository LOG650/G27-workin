import pandas as pd
import os

# Definer stier (bruker relative stier for portabilitet)
raw_data_path = '004 data/Salg 20250301-20260228.csv'
output_path = '004 data/vasket_salg_daglig.csv'

def vask_salgsdata(file_path):
    print(f"Leser rådata fra: {file_path}")
    
    # Leser filen med latin-1 koding pga norske tegn og semikolon som separator
    # Skipper de første linjene som ser ut til å være metadata (;;;...)
    try:
        df = pd.read_csv(file_path, sep=';', encoding='latin-1', skiprows=1)
    except Exception as e:
        print(f"Feil ved innlesing: {e}")
        return

    # 1. Konverter datoer
    # Bruker 'Opprettelsesdato' for å se når ordren kom inn, 
    # eller 'Plukkdato' for når varen faktisk ble sendt.
    # I LOG650 er ofte 'Opprettelsesdato' (etterspørselstidspunkt) mest relevant.
    df['Dato'] = pd.to_datetime(df['Opprettelsesdato'], dayfirst=True).dt.date
    
    # 2. Velg relevante kolonner
    # Vi fokuserer på 'Bestilt antall' som representerer den faktiske etterspørselen
    kolonner_inn = ['Dato', 'Bestilt antall']
    df_clean = df[kolonner_inn].copy()
    
    # 3. Aggreger til dagsnivå
    # Summerer alt salg for 'Lasagne Familiepakning' per dag
    df_daglig = df_clean.groupby('Dato')['Bestilt antall'].sum().reset_index()
    
    # 4. Gi kolonnen et tydelig navn (som vi diskuterte)
    df_daglig.columns = ['dato', 'faktisk_ettersporsel']
    
    # Sorter etter dato
    df_daglig = df_daglig.sort_values('dato')
    
    print(f"Vask fullført. Antall dager med salg: {len(df_daglig)}")
    return df_daglig

if __name__ == "__main__":
    if os.path.exists(raw_data_path):
        vasket_df = vask_salgsdata(raw_data_path)
        if vasket_df is not None:
            vasket_df.to_csv(output_path, index=False, encoding='utf-8')
            print(f"Vasket data lagret til: {output_path}")
    else:
        print(f"Fant ikke filen: {raw_data_path}")
