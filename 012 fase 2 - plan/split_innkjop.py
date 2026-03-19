import pandas as pd
import os

def split_innkjop_data(file_path):
    print(f"Leser vaskede data fra: {file_path}")
    
    # Leser filen
    df = pd.read_csv(file_path)
    df['dato'] = pd.to_datetime(df['dato'])
    
    # Definerer splitt-dato (samsvarer med salgsdataene)
    # Alt før 2026-01-01 er trening, fra og med er test.
    split_date = '2026-01-01'
    
    train_df = df[df['dato'] < split_date].copy()
    test_df = df[df['dato'] >= split_date].copy()
    
    # Lagre som CSV
    train_path = '004 data/train_innkjop.csv'
    test_path = '004 data/test_innkjop.csv'
    
    train_df.to_csv(train_path, index=False)
    test_df.to_csv(test_path, index=False)
    
    print(f"Splitting fullført!")
    print(f"Trening: {len(train_df)} rader (lagret til {train_path})")
    print(f"Test: {len(test_df)} rader (lagret til {test_path})")

if __name__ == "__main__":
    file_path = '004 data/vasket_innkjop_daglig.csv'
    if os.path.exists(file_path):
        split_innkjop_data(file_path)
    else:
        print(f"Fant ikke filen: {file_path}")
