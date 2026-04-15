"""
Bygger vasket daglig salgstidsserie fra RELEX-eksport (Nytt fra rema (in).csv).

RELEX-CSV-en er et bredt format: én rad per lokasjon/produkt med 365 dagskolonner
tvers gjennom perioden 1.3.2025-28.2.2026. Denne modulen henter ut Totalt-raden for
RD Trondheim + Lasagne Familiepakning, pivoterer til langt format og filtrerer til
kun virkedager (distribusjonssenteret er stengt i helg).

Utdata erstatter det tidligere `vasket_salg_daglig.csv` (som var generert fra et
utdatert rådatauttrekk og undertelte reell etterspørsel med ~70 %).
"""

import pandas as pd
from pathlib import Path

# Stier — skriptet forventes kjørt fra prosjektroten (C:/Users/lj_77/G27-workin)
RELEX_PATH = Path('Nytt fra rema (in).csv')
OUTPUT_PATH = Path('004 data/vasket_salg_daglig.csv')

# Strukturkonstanter for RELEX-eksporten
ANTALL_METADATAKOLONNER = 12  # Totalt, Lokasjonsnavn, ..., Pallestørrelse
KOLONNE_TOTALSUM = 12          # Kolonne "Salg (stk)" totalt for perioden
FORSTE_DAGSKOLONNE = 13        # Kolonne 1.3.2025 Lør starter her


def vask_relex(file_path: Path) -> pd.DataFrame:
    """Leser RELEX-eksport og returnerer daglig salg på virkedager."""
    # Hopp over de to første radene (kildekommentar og periodeinfo)
    df = pd.read_csv(file_path, sep=';', encoding='latin-1', header=None, skiprows=2)

    datorad = df.iloc[0]      # "1.3.2025 Lør", "2.3.2025 Søn", ...
    total_rad = df.iloc[2]    # Første datarad = Totalt for RD Trondheim + Lasagne

    datoer, verdier = [], []
    for i in range(FORSTE_DAGSKOLONNE, len(datorad)):
        dato_tekst = datorad[i]
        if not isinstance(dato_tekst, str):
            continue
        # Formatet er "D.M.ÅÅÅÅ Ukedag" — vi bruker kun datodelen
        dato_del = dato_tekst.split(' ')[0]
        try:
            dato = pd.to_datetime(dato_del, dayfirst=True)
        except (ValueError, TypeError):
            continue

        raa_verdi = total_rad[i]
        # Blanke celler i RELEX representerer 0 salg (typisk helg)
        verdi = 0 if pd.isna(raa_verdi) else int(float(raa_verdi))

        datoer.append(dato)
        verdier.append(verdi)

    df_daglig = (
        pd.DataFrame({'dato': datoer, 'faktisk_ettersporsel': verdier})
        .sort_values('dato')
        .reset_index(drop=True)
    )

    # Kun virkedager (mandag=0 til fredag=4). Helger er systematisk null i RELEX
    # fordi RD Trondheim ikke ekspederer i helg — å ta dem med forurenser SARIMA
    # og lag-features med kunstige nuller.
    df_virkedag = df_daglig[df_daglig['dato'].dt.weekday < 5].copy()
    return df_virkedag


if __name__ == '__main__':
    if not RELEX_PATH.exists():
        raise SystemExit(f'Fant ikke RELEX-fil: {RELEX_PATH}')

    vasket = vask_relex(RELEX_PATH)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    vasket.to_csv(OUTPUT_PATH, index=False, encoding='utf-8')

    sum_total = vasket['faktisk_ettersporsel'].sum()
    print(f'Vasket fra: {RELEX_PATH}')
    print(f'Skrevet til: {OUTPUT_PATH}')
    print(f'Antall virkedager: {len(vasket)}')
    print(f'Sum etterspørsel: {sum_total}')
    print(f'Periode: {vasket["dato"].min().date()} til {vasket["dato"].max().date()}')
