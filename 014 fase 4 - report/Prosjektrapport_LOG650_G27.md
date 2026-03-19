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
Dette prosjektet fokuserer på kvantitativ logistikk og supply chain management, med særlig vekt på etterspørselsprognoser og prognosepresisjon i distribusjonssystemer. Studien undersøker hvordan tidsserie-baserte metoder kan anvendes for å predikere daglig etterspørsel ved REMA 1000 Distribusjon Trondheim.

Prognosearbeid er en kritisk suksessfaktor i dagligvarebransjen. Nøyaktige estimater for fremtidig etterspørsel er avgjørende for å balansere lagerbeholdninger, sikre høy kundeservicegrad og minimere matsvinn i distribusjonsleddet. Ved å analysere historiske data og evaluere ulike prediksjonsmodeller, søker dette prosjektet å identifisere metoder som kan forbedre beslutningsgrunnlaget for innkjøp og kapasitetsplanlegging.

## 1.1 Problemstilling
Basert på behovet for økt presisjon i planleggingen, er følgende problemstilling formulert for prosjektet:

> **I hvilken grad kan tidsserie-baserte prognosemetoder predikere daglig etterspørsel for utvalgte produkter ved REMA 1000 Distribusjon Trondheim, målt ved prognosepresisjon (forecast accuracy)?**

For å besvare denne problemstillingen vil vi utvikle og evaluere modeller basert på historisk volum (plukket/utlevert mengde), samt undersøke i hvilken grad inkludering av forklaringsvariabler som kampanjeindikatorer og pris bidrar til forbedret nøyaktighet.

## 1.2 Delproblemer
For å strukturere analysen har vi definert følgende deloppgaver:
1. Hvordan karakteriseres de historiske etterspørselsmønstrene for det valgte produktet?
2. Hvilke tidsserie-baserte modeller gir lavest feilrate (målt ved MAE og MAPE)?
3. I hvilken grad påvirker kampanjeaktiviteter modellens evne til å predikere etterspørsel?

## 1.3 Avgrensinger
For å sikre dybde i analysen er prosjektet avgrenset på følgende måte:
- **Geografisk:** Analysen er begrenset til REMA 1000 Distribusjon Trondheim.
- **Produkt:** Studien fokuserer på ett utvalgt produkt, "Lasagne Familiepakning", som anses som representativt for kategorien tørrvarer med stabil etterspørsel og periodevis kampanjeaktivitet.
- **Tidsoppløsning:** Analysen gjennomføres på dagsnivå.
- **Omfang:** Prosjektet omfatter ikke full optimalisering av transport eller lagerstyring, men fokuserer isolert på prediksjonsleddet.

## 1.4 Antagelser
I arbeidet legges følgende antagelser til grunn:
- **Datakvalitet:** Vi antar at de historiske dataene fra REMAs ERP-systemer gir et representativt bilde av den faktiske etterspørselen, og at eventuelle avvik i registrering (f.eks. ved systemfeil) er minimale.
- **Stabilitet:** Vi forutsetter at grunnleggende markedsforhold for det valgte produktet er relativt stabile gjennom hele analyseperioden, bortsett fra de variablene vi eksplisitt modellerer (pris og kampanje).

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
Dette kapittelet gir en beskrivelse av den operative konteksten for studien, med fokus på REMA 1000 Distribusjon Trondheim (RDT) og det utvalgte produktet, "Lasagne Familiepakning".

## 4.1 REMA 1000 Distribusjon Trondheim
REMA 1000 Distribusjon Trondheim fungerer som et sentralt logistikknutepunkt for vareforsyning til REMA 1000-butikker i Midt-Norge. Distribusjonssenterets primære oppgave er å sikre effektiv vareflyt fra produsenter til utsalgssteder. En av de største utfordringene i dette leddet er å balansere hensynet til høy kundeservicegrad (unngå "out-of-stock" i butikk) mot målet om lavest mulig kapitalbinding og effektiv lagerdrift.

Prognosepresisjon ved distribusjonssenteret er kritisk fordi feilmarginer her kan forsterkes gjennom forsyningskjeden (Bullwhip-effekten). Dersom senteret overestimerer etterspørselen, øker lagerkostnadene og risikoen for ukurans. Ved underestimering risikerer man leveringssvikt til butikkene, noe som direkte påvirker sluttkundens opplevelse og bedriftens omdømme.

## 4.2 Produktbeskrivelse: Lasagne Familiepakning
Produktet som er valgt for denne studien er "Lasagne Familiepakning". Dette er en tørrvare med lang holdbarhet, noe som i utgangspunktet reduserer risikoen for fysisk matsvinn sammenlignet med ferskvarer. Likevel er produktet preget av en dynamisk etterspørsel som gjør det velegnet for prognosemodellering:

- **Etterspørselsstabilitet:** I normale uker har produktet en relativt stabil og forutsigbar etterspørsel basert på faste leveringsrutiner til butikkene.
- **Kampanjefølsomhet:** Produktet inngår ofte i nasjonale kampanjer, som for eksempel "Crazy Days", noe som skaper kraftige salgstoppar (spikes) som er utfordrende å predikere nøyaktig.
- **Strategisk betydning:** Som et volumprodukt i tørrvarekategorien representerer nøyaktige prognoser for denne varen et betydelig potensial for forbedret transport- og lagerplanlegging.

## 4.3 Identifiserte etterspørselsmønstre
Gjennom en foreløpig deskriptiv analyse av de vaskede salgsdataene er følgende mønstre identifisert for analyseperioden:

1.  **Ukedagseffekt:** Det er observert systematiske variasjoner gjennom uken, der mandager ofte har den høyeste utleverte mengden. Dette skyldes trolig butikkenes behov for å fylle opp hyllene etter storhandelen i helgen.
2.  **Kampanjeperioder (Crazy Days):** Det er identifisert to markante salgstoppar i løpet av perioden som sammenfaller med "Crazy Days"-kampanjer. Den mest omfattende toppen ble observert i oktober 2025 (uke 44), der etterspørselen lå stabilt på et nivå betydelig over normalen.
3.  **Sesongvariasjon:** Dataene indikerer lavere utlevert volum i fellesferien (juli/august), noe som kan knyttes til endrede handlevaner i sommerferien og redusert aktivitet i regionen.

# 5. Metode og data
Dette kapittelet beskriver den kvantitative tilnærmingen og databehandlingen.

# 5. Metode og data
Dette kapittelet beskriver studiens metodiske fundament, datagrunnlaget og prosessene som er benyttet for å transformere rådata til et beslutningsgrunnlag for prognosemodellering.

## 5.1 Forskningsdesign: Kvantitativ Case-studie
Studien benytter et kvantitativt forskningsdesign basert på en case-studie av REMA 1000 Distribusjon Trondheim. Valget av kvantitativ metode er begrunnet i studiens behov for å analysere historiske transaksjonsdata for å identifisere mønstre og evaluere numerisk nøyaktighet i prognoser. Case-studiedesignet muliggjør en dypere forståelse av hvordan spesifikke faktorer, som "Crazy Days"-kampanjer, påvirker etterspørselen i en reell logistisk kontekst.

## 5.2 Datainnsamling og Kildekritikk
Primærdataene består av historiske uttrekk fra REMAs ERP-systemer (Enterprise Resource Planning). 

- **Datakilde:** Sekundærdata i form av historiske salgs- og innkjøpstransaksjoner for perioden mars 2025 til februar 2026.
- **Kildekritikk:** Dataene anses som svært pålitelige da de representerer faktiske fysiske bevegelser (plukk og mottak) ved distribusjonssenteret. En potensiell feilkilde er eventuelle systemfeil eller manuelle korrigeringer i ERP-systemet som ikke reflekterer fysisk etterspørsel, men slike avvik antas å være statistisk insignifikante i det store datamaterialet.

## 5.3 Databehandling og Vaskeprosess
For å klargjøre dataene for tidsserieanalyse, ble det gjennomført en omfattende vaskeprosess ved bruk av programmeringsspråket Python og biblioteket Pandas. Dette er et kritisk steg for å sikre etterprøvbarhet:

1.  **Valg av tidsvariabel:** Vi har valgt `Opprettelsesdato` som den primære tidsvariabelen. I logistikksammenheng representerer dette tidspunktet butikken legger inn ordren, noe som gir det mest presise bildet av etterspørselen sammenlignet med `Plukkdato`.
2.  **Aggregering til dagsnivå:** Rådataene inneholder hver enkelt ordrelinje (transaksjonsnivå). Ved å summere alle bestillinger per dag, skaper vi en sammenhengende tidsserie som er nødvendig for de valgte prognosemodellene.
3.  **Tegnsett og Format:** Alle filer ble konvertert til UTF-8 koding for å sikre korrekt visning av norske tegn (æ, ø, å).

Resultatet av denne prosessen er datasettene `vasket_salg_daglig.csv` og `vasket_innkjop_daglig.csv`.

## 5.4 Analysemetoder og Evaluering
For å evaluere hvor gode prognosemodellene er, benytter vi to anerkjente statistiske feilmål:

- **MAE (Mean Absolute Error):** Måler det gjennomsnittlige avviket i faktiske enheter. Dette er lett å tolke for logistikkplanleggere (f.eks. "vi bommer i snitt med 10 kasser").
- **MAPE (Mean Absolute Percentage Error):** Måler det prosentvise avviket. Dette gjør det mulig å sammenligne prognosepresisjon på tvers av ulike produkter med ulikt salgsvolum.

## 5.5 Splitting av data (Trening og Test)
Datasettet er delt i et treningssett og et testsett (Out-of-sample test). Dette simulerer en reell situasjon der man skal forutsi fremtiden basert på fortiden.

- **Treningssett (Train):** 01.03.2025 – 31.12.2025. Brukes til parameterestimering og modellutvikling.
- **Testsett (Test):** 01.01.2026 – 28.02.2026. Brukes utelukkende til evaluering av prognosepresisjon.

# 6. Modellering
For å besvare problemstillingen er det etablert to enkle baseline-modeller: Saisonal Naive og Moving Average (MA7).

# 7. Analyse
Dette kapittelet presenterer den deskriptive analysen (Exploratory Data Analysis - EDA) av de vaskede datasettene for salg og innkjøp. Hensikten er å identifisere mønstre, trender og avvik som danner grunnlaget for valg av prognosemodeller.

## 7.1 Deskriptiv statistikk
For å forstå de grunnleggende egenskapene til etterspørselen etter "Lasagne Familiepakning", er det gjennomført en deskriptiv statistisk analyse av treningsdatasettet (mars–desember 2025). Resultatene er oppsummert i tabell 1 nedenfor.

**Tabell 1: Deskriptiv statistikk for daglig etterspørsel (Treningssett)**

| Statistisk mål | Verdi (Antall enheter) |
| :--- | :--- |
| Antall observasjoner (dager) | 228 |
| Gjennomsnitt (Mean) | 24,52 |
| Median (50%) | 10,00 |
| Standardavvik (Std) | 36,53 |
| Minimum | 1,00 |
| Maksimum | 171,00 |
| **Variasjonskoeffisient (CV)** | **1,49** |

Analysen av treningsdataene avdekker flere kritiske forhold:
1.  **Høy volatilitet:** En variasjonskoeffisient (CV) på 1,49 indikerer en svært volatil etterspørsel. I logistikklitteraturen regnes verdier over 1,0 som "uforutsigbare" (lumpy demand), noe som gjør tradisjonelle prognosemetoder utfordrende å anvende.
2.  **Skjevfordeling:** Det er et betydelig gap mellom gjennomsnittet (24,52) og medianen (10,00). Dette indikerer at datasettet er positivt skjevt; de fleste dagene har et relativt lavt salgsvolum, mens noen få dager med ekstremt høy etterspørsel (opptil 171 enheter) drar gjennomsnittet opp.
3.  **Ekstremverdier:** Maksimumsverdien er over sju ganger høyere enn gjennomsnittet, noe som underbygger behovet for å identifisere spesifikke hendelser, som "Crazy Days"-kampanjer, for å forbedre prognosepresisjonen.

## 7.2 Tidsserieanalyse (Visualisering)
For å identifisere de underliggende mønstrene i etterspørselen, er treningsdataene visualisert gjennom et tidsseriediagram (Figur 1) og en ukedagsanalyse (Figur 2).

**Figur 1: Daglig etterspørsel for Lasagne Familiepakning (Mars–Desember 2025)**
*(Referanse til bildefil: figurer/fig1_tidsserie.png)*

Visualiseringen i Figur 1 bekrefter tilstedeværelsen av ekstreme etterspørselsstopper (spikes) som sammenfaller med "Crazy Days"-kampanjer. Den mest omfattende toppen ble registrert i oktober 2025, med en daglig etterspørsel på 171 enheter. Utenom disse kampanjeperiodene fremstår grunnplan etterspørselen som relativt stabil, men med betydelig daglig variasjon (støy). Det er ingen tydelig langsiktig trend (økning eller reduksjon) i det utleverte volumet gjennom 2025.

**Figur 2: Gjennomsnittlig daglig etterspørsel fordelt på ukedager**
*(Referanse til bildefil: figurer/fig2_ukedag.png)*

Figur 2 avdekker en signifikant ukedagseffekt som er kritisk for logistikkplanleggingen:
1.  **Mandagseffekten:** Mandager har en gjennomsnittlig etterspørsel på 50,89 enheter, noe som er mer enn dobbelt så høyt som det totale gjennomsnittet (24,52). Dette mønsteret indikerer at butikkenes påfyllingsbehov er størst rett etter helgehandelen.
2.  **Lavpunkt:** Etterspørselen avtar gradvis gjennom uken og når sitt laveste punkt på fredager (12,39 enheter i snitt).
3.  **Søndagsetterslep:** Det registreres også en viss aktivitet på søndager (19,00 enheter), noe som kan knyttes til forhåndsbestillinger fra butikker som klargjøres for utlevering tidlig mandag morgen.

Denne systematiske variasjonen mellom ukedagene betyr at en sesongbasert naive modell (Seasonal Naive) sannsynligvis vil prestere bedre enn en enkel gjennomsnittsmodell (Moving Average), da den fanger opp de faste ukentlige svingningene.

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
