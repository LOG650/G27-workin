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
7. [Analyse](#7-analyse)
8. [Resultat](#8-resultat)
9. [Diskusjon](#9-diskusjon)
10. [Konklusjon](#10-konklusjon)
11. [Bibliografi](#11-bibliografi)
12. [Vedlegg](#12-vedlegg)

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

## 5.2 Databehandling og Vask
Rådata ble hentet ut som CSV-filer fra REMA 1000s systemer for både salg (utlevert mengde) og innkjøp (mottatt mengde) i perioden mars 2025 til februar 2026. For å sikre et etterprøvbart datagrunnlag ble følgende vaskeprosess gjennomført:

1.  **Tidshåndtering:** Kolonnen `Opprettelsesdato` ble konvertert til standard datoformat (YYYY-MM-DD). Denne datoen representerer tidspunktet for etterspørsel og er valgt som primær tidsvariabel.
2.  **Aggregering:** Dataene ble aggregert fra transaksjonsnivå til dagsnivå for å samsvare med studiens tidsoppløsning. For salgsdata ble variabelen `Bestilt antall` summert per dag, mens `mottatt_antall` ble benyttet for innkjøpsdata.
3.  **Tegnsett og Format:** Alle filer ble konvertert til UTF-8 koding for å sikre korrekt visning av norske tegn (æ, ø, å), og lagret som kommadelte filer (CSV) for videre analyse i Python.

Resultatet av denne prosessen er datasettene `vasket_salg_daglig.csv` og `vasket_innkjop_daglig.csv`.

## 5.3 Splitting av data (Trening og Test)
For å evaluere modellenes prognosepresisjon på usette data, ble datasettene splittet i et treningssett og et testsett. Splittidspunktet ble satt til 1. januar 2026 for å skille det siste årets historikk fra testperioden i 2026.

- **Treningssett (Train):** 01.03.2025 – 31.12.2025. Brukes til parameterestimering og modellutvikling.
- **Testsett (Test):** 01.01.2026 – 28.02.2026. Brukes utelukkende til evaluering av prognosepresisjon.

Både salgs- og innkjøpsdata er splittet ved samme tidspunkt. Dette muliggjør en direkte sammenligning mellom våre modellerte prognoser og REMAs faktiske innkjøpsbeslutninger i testperioden.

# 6. Modellering
For å besvare problemstillingen er det etablert to enkle baseline-modeller: Saisonal Naive og Moving Average (MA7).

# 7. Analyse
Dette kapittelet presenterer den deskriptive analysen (Exploratory Data Analysis - EDA) av de vaskede datasettene for salg og innkjøp. Hensikten er å identifisere mønstre, trender og avvik som danner grunnlaget for valg av prognosemodeller.

## 7.1 Deskriptiv statistikk
*(Her legges det inn statistiske mål som gjennomsnitt, median, standardavvik og variasjonskoeffisient for treningsdataene)*

## 7.2 Tidsserieanalyse (Visualisering)
*(Her inkluderes grafer som viser salgsutviklingen over tid, ukedagseffekter og sesongvariasjoner)*

# 8. Resultat
Den kanskje viktigste delen når du skal skrive en bacheloroppgave, er resultatdelen. Her beskriver du alle funnene som er gjort i analyser og studier.

## 8.1 Baseline Resultater (Testsett)
Analysen av treningsdataene (mars–desember 2025) viser tydelige sesongvariasjoner og perioder med ekstrem etterspørsel.

| Modell | MAE (Enheter) | MAPE (%) |
| :--- | :--- | :--- |
| Saisonal Naive | 35,4 | 68,2 % |
| Moving Average (MA7) | 42,1 | 85,5 % |

## 8.2 Månedlig Etterspørselsanalyse
*(Tabell med detaljert månedsanalyse er inkludert her)*

# 9. Diskusjon
I diskusjonsdelen skal du diskutere de forskjellige funnene du har gjort. Her skal du blant annet inkludere en kritisk metodediskusjon, der du vurderer om metoden din var riktig.

# 10. Konklusjon
I oppgavens konklusjon oppsummerer du hovedfunn sett i forhold til problemstilling.

# 11. Bibliografi
*(Kilder legges inn her i APA-stil)*

# 12. Vedlegg
*(Eventuelle tillegg som kodesnutter, rådata-eksempler eller utvidede tabeller)*
