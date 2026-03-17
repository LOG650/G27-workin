# Prosjektrapport: Prognosepresisjon ved REMA 1000 Distribusjon Trondheim (LOG650)

**Forfattere:** Line Lyngsnes Johansen og Amanda Arnesen Almaas  
**Studium:** Logistikk (Nettbasert), Høgskolen i Molde  
**Dato:** 17. mars 2026  
**Sted:** Trondheim  

---

**Obligatorisk egenerklæring / gruppeerklæring**  
*(Innhold fra mal legges inn her ved endelig innlevering)*

**Personvern og Publiseringsavtale**  
*(Innhold fra mal legges inn her ved endelig innlevering)*

---

## Sammendrag
Denne rapporten undersøker prognosepresisjon for daglig etterspørsel ved REMA 1000 Distribusjon Trondheim. Formålet er å evaluere i hvilken grad tidsserie-baserte modeller kan predikere etterspørselen for produktet "Lasagne Familiepakning", og hvordan faktorer som kampanjer påvirker nøyaktigheten. Ved bruk av historiske salgsdata og feilmålene MAE og MAPE, sammenlignes ulike modeller for å identifisere de mest effektive tilnærmingene.

## Abstract
This report investigates the forecast accuracy of daily demand at REMA 1000 Distribution Trondheim. The objective of the study is to evaluate the extent to which time-series-based models can predict the demand for "Lasagne Familiepakning", and how factors such as promotions influence the accuracy of these forecasts. Using historical sales data and statistical error measures like MAE and MAPE, various models are compared to identify the most effective approaches for the distribution stage.

---

# Innhold
1. [Innledning](#1-innledning)
2. [Litteratur](#2-litteratur)
3. [Teori](#3-teori)
4. [Casebeskrivelse](#4-casebeskrivelse)
5. [Metode og data](#5-metode-og-data)
6. [Modellering](#6-modellering)
7. [Resultat](#7-resultat)
8. [Diskusjon](#8-diskusjon)
9. [Konklusjon](#9-konklusjon)
10. [Bibliografi](#10-bibliografi)

---

# 1. Innledning
Dette prosjektet undersøker hvordan tidsserie-baserte metoder kan anvendes for å predikere daglig etterspørsel i distribusjonssystemer, med særlig fokus på REMA 1000 Distribusjon Trondheim. Prognosepresisjon er kritisk for effektiv lagerstyring og redusert matsvinn.

## 1.1 Problemstilling
Problemstillingen for dette prosjektet er:
> **I hvilken grad kan tidsserie-baserte prognosemetoder predikere daglig etterspørsel for utvalgte produkter ved REMA 1000 Distribusjon Trondheim, målt ved prognosepresisjon (forecast accuracy)?**

## 1.2 Avgrensinger
- **Geografisk:** REMA 1000 Distribusjon Trondheim.
- **Produkt:** Lasagne Familiepakning.
- **Tidsoppløsning:** Daglige observasjoner fra mars 2025 til februar 2026.

## 1.3 Antagelser
- **Datatilgang:** Vi antar tilgang til minimum ett års historiske, anonymiserte data på dagsnivå fra REMA 1000 Distribusjon Trondheim.
- **Datakvalitet:** Vi forutsetter at dataene inkluderer faktisk plukket volum og at disse er tilstrekkelig nøyaktige for statistisk modellering.

# 2. Litteratur
Dette kapittelet diskuterer sentrale bidrag innen retail forecasting og etterspørselsplanlegging. Vi baserer oss på nyere forskning som belyser gapet mellom teori og praksis i varehandelen (Fildes et al., 2022) og utfordringer med kampanjer (Trapero et al., 2015). En detaljert gjennomgang av de 7 utvalgte kjerneartiklene vil bli presentert her.

# 3. Teori
Dette kapittelet presenterer de sentrale logistikkfaglige teoriene som ligger til grunn for analysen av prognosepresisjon.

## 3.1 Etterspørselsmønstre i Distribusjonsleddet
Etterspørselen i dagligvaremarkedet karakteriseres ofte som volatil og påvirket av flere komponenter: Trend, Sesong, Kampanjer og Tilfeldig variasjon (støy).

## 3.2 Prognosemetoder for Tidsserier
Dette prosjektet fokuserer på kvantitative metoder som Naive modeller, Moving Average (MA) og Exponential Smoothing.

## 3.3 Måling av Prognosepresisjon
For å evaluere modellenes evne til å predikere etterspørsel, benyttes statistiske feilmål som MAE (Mean Absolute Error) og MAPE (Mean Absolute Percentage Error).

# 4. Casebeskrivelse
REMA 1000 Distribusjon Trondheim fungerer som et sentralt knutepunkt for vareforsyning i regionen. En av de største utfordringene er å balansere lagernivåer mot kundeservicegrad under høy volatilitet.

## 4.1 Identifiserte etterspørselsmønstre
Gjennom en deskriptiv analyse av salgsdataene for "Lasagne Familiepakning" er følgende mønstre identifisert:
1.  **Ukedagseffekt:** Mandager har systematisk høyere etterspørsel enn øvrige dager.
2.  **Kampanjeperioder:** En massiv salgstopp ble observert i uke 44 (oktober 2025), der etterspørselen lå stabilt på 115 enheter per dag.
3.  **Sesongvariasjon:** Det ble observert lavere aktivitet i juli og august.

# 5. Metode og data
Dette kapittelet beskriver den kvantitative tilnærmingen og databehandlingen.

## 5.1 Metode
Studien følger et kvantitativt forskningsdesign basert på en case-studie. Vi benytter statistiske metoder for tidsserieanalyse for å utvikle og evaluere prognosemodeller.

## 5.2 Data
Rådata ble hentet ut som CSV-filer for salg og innkjøp. Datavasken inkluderte konvertering av tidsstempler, aggregering til dagsnivå og håndtering av tegnsett.

## 5.3 Splitting av data (Train/Test)
Datasettet er delt i to:
- **Treningssett:** 01.03.2025 – 31.12.2025.
- **Testsett:** 01.01.2026 – 20.02.2026.

# 6. Modellering
For å besvare problemstillingen er det etablert to enkle baseline-modeller: Saisonal Naive og Moving Average (MA7).

# 7. Resultat
Analysen av treningsdataene (mars–desember 2025) viser tydelige sesongvariasjoner og perioder med ekstrem etterspørsel.

## 7.1 Baseline Resultater (Testsett)
| Modell | MAE (Enheter) | MAPE (%) |
| :--- | :--- | :--- |
| Saisonal Naive | 35,4 | 68,2 % |
| Moving Average (MA7) | 42,1 | 85,5 % |

## 7.2 Månedlig Etterspørselsanalyse
*(Tabell med detaljert månedsanalyse er flyttet hit fra kapittel 5 i forrige utkast)*

# 8. Diskusjon
I diskusjonsdelen skal vi drøfte resultatene opp mot problemstillingen, inkludert betydningen for lagerstyring (Syntetos et al., 2009) og effekten av menneskelige justeringer (Fildes et al., 2008).

# 9. Konklusjon
Konklusjonen vil oppsummere hovedfunn sett i forhold til problemstillingen om prognosepresisjon ved REMA 1000 Distribusjon Trondheim.

# 10. Bibliografi
*(Kilder legges inn her i APA-stil)*
