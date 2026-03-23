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

Prognosearbeid er en kritisk suksessfaktor i dagligvarebransjen. Nøyaktige estimater for fremtidig etterspørsel er avgjørende for å balansere lagerbeholdninger, sikre høy kundeservicegrad og minimere matsvinn i distribusjonsleddet. Selv om det utvalgte produktet i denne studien er en tørrvare med lang holdbarhet, har prognosepresisjon her en indirekte, men betydelig innvirkning på det totale svinn-regnskapet. Nøyaktige prognoser for stabile tørrvarekategorier frigjør operativ kapasitet og logistiske ressurser, noe som muliggjør en mer presis og prioritert håndtering av ferskvaredistribusjon – der det faktiske matsvinn-potensialet er største. Ved å analysere historiske data og evaluere ulike prediksjonsmodeller, søker dette prosjektet å identifisere metoder som kan forbedre beslutningsgrunnlaget for den totale vareflyten.

## 1.1 Problemstilling
Basert på behovet for økt presisjon i planleggingen, er følgende problemstilling formulert for prosjektet:

> **I hvilken grad kan tidsserie-baserte prognosemetoder predikere daglig etterspørsel for utvalgte produkter ved REMA 1000 Distribusjon Trondheim, målt ved prognosepresisjon (forecast accuracy)?**

For å besvare denne problemstillingen vil vi utvikle og evaluere modeller basert på historisk volum (plukket/utlevert mengde). Selv om inkludering av forklaringsvariabler som kampanjeindikatorer og pris vurderes som teoretisk relevante, er selve analysen i denne oppgaven avgrenset til bruk av historiske salgs- og kalenderdata for å evaluere modellenes grunnleggende prediksjonsevne. En sentral del av studien er å *evaluere* hvordan disse rene tidsseriemodellene presterer i møte med kampanjedrevet etterspørsel, for å kvantifisere behovet for mer avanserte forklaringsvariabler i fremtidige systemer.

## 1.2 Delproblemer
For å strukturere analysen har vi definert følgende deloppgaver:
1. Hvordan karakteriseres de historiske etterspørselsmønstrene for det valgte produktet?
2. Hvilke tidsserie-baserte modeller gir lavest feilrate (målt ved MAE og MAPE)?
3. I hvilken grad utgjør kampanjeaktiviteter en begrensning for modellens evne til å predikere etterspørsel basert på historiske data?

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
Dette kapittelet presenterer en gjennomgang av sentrale bidrag innen retail forecasting og etterspørselsplanlegging. Litteraturgjennomgangen er strukturert tematisk for å belyse utfordringene ved dagligvareprognoser, effekten av kampanjer og valg av evalueringsmetoder.

## 2.1 Kompleksitet i dagligvareprognoser
Fildes et al. (2022) gir en omfattende oversikt over gapet mellom akademisk teori og praktisk anvendelse i varehandelen. De påpeker at tradisjonelle statistiske modeller ofte kommer til kort i møte med den ekstreme volatiliteten og de store datamengdene som karakteriserer moderne retail. Denne kompleksiteten understøttes av Makridakis et al. (2022) i deres analyse av M5-konkurransen. Her dokumenteres det at moderne maskinlæringsmodeller og hybridmetoder ofte utkonkurrerer klassiske tidsseriemetoder på dagligvaredata, spesielt når dataene er preget av diskontinuitet og mange nullverdier.

For spesifikke matvarekategorier understreker Arunraj og Ahrens (2015) betydningen av å modellere på dagsnivå. De viser hvordan hybridmodeller som kombinerer sesongvariasjoner og regresjon kan forbedre presisjonen for produkter med kort holdbarhet eller svingende etterspørsel, noe som er direkte relevant for vår analyse av "Lasagne Familiepakning" ved REMA 1000 Distribusjon Trondheim.

## 2.2 Kampanjer og menneskelig skjønn
Et av de mest utfordrende elementene i etterspørselsplanlegging er effekten av kampanjeaktiviteter. Trapero et al. (2015) fokuserer på hvordan planlagte kampanjer skaper salgstoppe som bryter med historiske mønstre. De argumenterer for nødvendigheten av å integrere kampanjekalendere direkte i prognosemodellene for å unngå systematiske underestimeringer. 

I tillegg til de statistiske modellene, diskuterer Fildes et al. (2008) rollen til menneskelige overstyringer (judgmental adjustments). Deres empiriske evaluering viser at skjønnsmessige justeringer kan forbedre prognoser dersom de baseres på unik informasjon (som lokalkunnskap om kampanjer), men at de ofte kan introdusere bias dersom de brukes ukritisk. Dette er et viktig perspektiv når vi observerer "flate topper" i REMAs data, som kan indikere manuelle tak eller faste tildelingsregler.

## 2.3 Evaluering og logistisk verdi
Valg av feilmål er kritisk for å forstå modellens faktiske ytelse. Hyndman og Koehler (2006) kritiserer utbredt bruk av MAPE, spesielt i situasjoner med lav etterspørsel, og foreslår mer robuste mål som MAE for å gi et mer pålitelig bilde av prognosefeilen. 

Videre knytter Syntetos et al. (2009) prognosepresisjon direkte til operasjonell logistikk ved å vise hvordan nøyaktige prognoser er en forutsetning for effektiv lagerstyring. Denne sammenhengen utdypes i nyere forskning av Seiringer et al. (2024), som analyserer hvordan ulike typer prognosefeil og bias direkte påvirker dimensjoneringen av sikkerhetslager i forsyningskjeder. De påpeker at systematiske feil (bias) har en mer kritisk innvirkning på lagerbinding og kostnader enn tilfeldige avvik. Ved å forbedre presisjonen i distribusjonsleddet, kan man redusere både lagerkostnader og risikoen for leveringssvikt (stock-outs), noe som utgjør den praktiske verdien av dette prosjektet for REMA 1000.

# 3. Teori
Dette kapittelet presenterer de sentrale logistikkfaglige teoriene som ligger til grunn for analysen av prognosepresisjon. Forståelse av etterspørselens natur og de matematiske rammene for prognostisering er avgjørende for å kunne tolke resultatene fra REMA 1000 Distribusjon Trondheim.

## 3.1 Etterspørselsmønstre i Distribusjonsleddet
Etterspørselen i dagligvaremarkedet er sjelden konstant og karakteriseres ofte av fire hovedkomponenter:
1.  **Trend:** En langsiktig økning eller reduksjon i volum over tid.
2.  **Sesongvariasjoner:** Systematiske svingninger som gjentar seg over faste perioder, for eksempel ukentlige mønstre (ukedagseffekt) eller årlige svingninger (høytider).
3.  **Kampanjer (Eventer):** Kortsiktige, kraftige økninger i etterspørsel drevet av markedsføringstiltak.
4.  **Tilfeldig variasjon (Støy):** Uforutsigbare svingninger som ikke kan forklares av de andre komponentene.

I denne studien er **Variasjonskoeffisienten (Coefficient of Variation, CV)** et sentralt mål for å kategorisere etterspørselen. CV defineres som forholdet mellom standardavviket ($\sigma$) og gjennomsnittet ($\mu$):
$$CV = \frac{\sigma}{\mu}$$
En verdi for CV > 1.0 indikerer det som i litteraturen betegnes som **"Lumpy Demand"** (ujevn etterspørsel). Dette er typisk for produkter der etterspørselen er preget av store, sporadiske topper etterfulgt av perioder med lavt eller null salg, noe som gjør tradisjonelle prognosemetoder mindre treffsikre.

## 3.2 Prognosemetoder for Tidsserier
Vi skiller mellom ulike nivåer av kompleksitet i prognosemodellering. I dette prosjektet benyttes i første omgang to baseline-modeller:

*   **Seasonal Naive (SN):** Denne modellen antar at etterspørselen i neste periode vil være identisk med etterspørselen i samme periode i forrige sesong. På dagsnivå betyr dette at prognosen for en mandag settes lik faktiske data fra forrige mandag. Dette er en kraftfull baseline for data med sterke ukedagseffekter.
*   **Moving Average (MA):** Glidende gjennomsnitt beregner prognosen som et gjennomsnitt av de $n$ siste observasjonene. En MA7-modell (7 dagers glidende snitt) vil flate ut daglige svingninger, men har en tendens til å "henge etter" ved brå endringer i etterspørselen, som ved kampanjestart. I den endelige analysen er MA valgt bort til fordel for Seasonal Naïve, da sistnevnte vurderes som en mer relevant baseline for å fange opp den tydelige ukesesongvariasjonen i datasettet.

## 3.3 Måling av Prognosepresisjon
For å evaluere hvor godt en modell presterer, må vi måle avviket mellom prognose ($F_t$) og faktisk etterspørsel ($A_t$).

*   **MAE (Mean Absolute Error):** Dette målet gir den gjennomsnittlige absolutte feilen i faktiske enheter:
    $$MAE = \frac{1}{n} \sum_{t=1}^{n} |A_t - F_t|$$
    Fordelen med MAE er at den er enkel å kommunisere til operative logistikkplanleggere, da den uttrykker feilen i samme måleenhet som produktet (f.eks. antall kasser).

*   **MAPE (Mean Absolute Percentage Error):** Dette målet uttrykker feilen som en prosentandel av den faktiske etterspørselen:
    $$MAPE = \frac{100\%}{n} \sum_{t=1}^{n} \left| \frac{A_t - F_t}{A_t} \right|$$
    Selv om MAPE er utbredt for å sammenligne på tvers av produkter, har den svakheter ved lav etterspørsel, da små absolutte avvik kan gi svært høye prosentvise utslag (Hyndman & Koehler, 2006). I våre resultater må MAPE derfor tolkes med forsiktighet, da målet kan gi svært høye verdier ved lavt volum, noe som er tilfelle for enkelte dager i datasettet. Dette er særlig relevant for våre data der enkelte dager har svært lavt volum.

# 4. Casebeskrivelse og datagrunnlag
Dette kapittelet gir en forståelse av den operative konteksten og datagrunnlaget som danner fundamentet for analysen. Formålet er å beskrive beslutningssituasjonen ved REMA 1000 Distribusjon Trondheim og karakterisere etterspørselsmønstrene før selve modelleringen starter.

## 4.1 REMA 1000 Distribusjon Trondheim og beslutningssituasjonen
REMA 1000 Distribusjon Trondheim (RDT) fungerer som det sentrale logistikknutepunktet for vareforsyning til butikker i Midt-Norge. Distribusjonssenterets primære oppgave er å sikre effektiv vareflyt fra produsenter til utsalgssteder. 

Virksomheten står daglig overfor kritiske **beslutningssituasjoner** knyttet til:
1.  **Dimensjonering av innkjøp:** Fastsettelse av ordrekvantum fra produsent for å unngå tomme hyller (stock-outs) uten å binde opp for mye kapital i lager.
2.  **Kapasitetsplanlegging:** Allokering av transportressurser og personell for plukking og utkjøring.

Uten robuste analyser er disse beslutningene svært vanskelige å ta. Den høye volatiliteten i dagligvaremarkedet gjør at manuelle skjønn ofte fører til systematiske feil (bias). Det er spesielt utfordrende å skille mellom tilfeldig variasjon ("støy") og reelle endringer i etterspørselsnivået før en kampanje inntreffer, noe som skaper et akutt behov for objektive prognosemodeller.

## 4.2 Produktbeskrivelse: Lasagne Familiepakning
Produktet som er valgt for denne studien er "Lasagne Familiepakning". Dette er en tørrvare med lang holdbarhet, noe som i utgangspunktet reduserer risikoen for fysisk matsvinn. Likevel er produktet preget av en dynamisk etterspørsel som gjør det velegnet for denne analysen. Nøyaktige prognoser for dette volumproduktet er viktig for å balansere hensynet til høy kundeservicegrad mot målet om effektiv lagerdrift og transportutnyttelse.

## 4.3 Beskrivelse av datagrunnlaget
Datamaterialet i denne studien er hentet direkte fra REMAs ERP-systemer og representerer faktiske utleverte mengder (plukkvolum) fra distribusjonssenteret til butikkene.

*   **Datatype:** Tidsseriedata på dagsnivå.
*   **Periode:** 1. mars 2025 til 28. februar 2026 (N=365 observasjoner).
*   **Variabel:** Faktisk utlevert volum målt i antall enheter per dag.

Tabell 1 gir en statistisk oversikt over variasjonen og spredningen i datagrunnlaget for analyseperioden.

**Tabell 1: Beskrivende statistikk for Lasagne Familiepakning (mars 2025 – feb 2026)**

| Mål | Verdi (Enheter) |
| :--- | :--- |
| Antall dager (N) | 365 |
| Gjennomsnittlig daglig etterspørsel ($\mu$) | 11,5 |
| Standardavvik ($\sigma$) | 13,2 |
| **Variasjonskoeffisient (CV)** | **1,15** |
| Minimumsalg | 0 |
| Maksimumsalg (Kampanjeplatå) | 115 |
| Maksimumsalg (Ekstremverdi/Støy) | 171 |

Som Tabell 1 viser, er standardavviket høyere enn gjennomsnittet, noe som resulterer i en CV på 1,15. Dette bekrefter at etterspørselen er preget av store svingninger og faller inn under kategorien "Lumpy Demand" (ujevn etterspørsel), som teoretisert i kapittel 3.1.

## 4.4 Etterspørselsmønstre og visualisering
For å få et helhetsbilde av dataenes utvikling over tid, er den historiske tidsserien visualisert i Figur 1.

![Figur 1: Historisk tidsserie for Lasagne Familiepakning](figurer/fig1_tidsserie.png)
**Figur 1: Historisk tidsserie (mars 2025 – februar 2026) som viser variasjon i utlevert volum og markante topper under kampanjeperioder.**

Grafen viser et tydelig bilde av dataenes natur. Nivået ligger stabilt lavt i normalperioder, men brytes av kortsiktige og kraftige topper. Det er ingen tydelig langsiktig trend i datamaterialet, men vi ser en klar sesongvariasjon knyttet til ukedager. Dette utdypes i Figur 2, som viser gjennomsnittlig salg per ukedag.

![Figur 2: Gjennomsnittlig etterspørsel per ukedag](figurer/fig2_ukedag.png)
**Figur 2: Gjennomsnittlig utlevert volum fordelt på ukedager, som dokumenterer den systematiske ukedagseffekten med høyest aktivitet på mandager.**

Ukedagseffekten viser at mandager har det desidert høyeste volumet. Dette skyldes butikkenes behov for å fylle opp hyllene etter storhandelen i helgen. Denne systematiske variasjonen er en kritisk innsikt som modellene i kapittel 6 må kunne fange opp.

## 4.5 Kampanjemekanikk og "Censored Demand"
En av de største utfordringene i datamaterialet er effekten av "Crazy Days"-kampanjer. I disse periodene observerer vi "flate topper" der etterspørselen stabiliserer seg på nøyaktig 115 enheter over flere dager. 

Dette fenomenet betegnes i faglitteraturen som **"Censored Demand"** (avskåret etterspørsel). Det betyr at de registrerte dataene ikke nødvendigvis reflekterer den sanne kundeetterspørselen, men heller er et resultat av logistiske kapasitetsbegrensninger eller sentrale styringsregler (ref. kapittel 4.3 i opprinnelig utkast). Når butikkene når sine tildelingsgrenser, flater kurven ut. For prognosearbeidet betyr dette at modellene må trenes på data som er preget av slike kapasitetstak, noe som gjør prediksjon av de reelle "toppene" ekstra utfordrende.

## 4.6 Konsekvenser og behov for modeller
Mangelen på gode prognoser har direkte operative konsekvenser for REMA 1000:
*   **Stock-outs:** Ved underestimering mister man salg og kundetilfredshet i butikk.
*   **Lagerbinding:** Ved overestimering øker lagerkostnadene og kapitalbindingen på distribusjonssenteret.
*   **Uforutsigbarhet:** Brå topper skaper press på transportkapasitet og bemanning.

Disse konsekvensene skaper et tydelig behov for en modell som kan skille mellom den systematiske ukedagseffekten og de ekstraordinære kampanjeløftene. Kapittelet har dermed lagt grunnlaget for hvorfor vi i de neste kapitlene velger å teste både statistiske SARIMA-modeller og maskinlæringsbaserte Random Forest-algoritmer.

# 5. Metode og data
Dette kapittelet redegjør for studiens metodiske tilnærming, datagrunnlaget og den trinnvise prosessen som er benyttet for å besvare problemstillingen. Formålet er å sikre at analysen er transparent og etterprøvbar.

## 5.1 Metodevalg og forskningsstruktur
Studien benytter et **kvantitativt forskningsdesign** basert på en case-studie av REMA 1000 Distribusjon Trondheim. Valget av kvantitativ metode er begrunnet i behovet for å analysere store mengder historiske transaksjonsdata for å identifisere mønstre og evaluere numerisk nøyaktighet i prognoser. 

Arbeidet er strukturert som en lineær prosess der målet er å identifisere den mest robuste modellen for å håndtere "Lumpy Demand". Ved å kombinere klassisk statistikk (SARIMA) med maskinlæring (Random Forest), oppnår vi en metodisk triangulering som øker studiens faglige tyngde og gir et mer nyansert bilde av prediksjonsevnen.

## 5.2 Den analytiske prosessen
Analysen er gjennomført i fire hovedfaser ved bruk av programmeringsspråket **Python** og bibliotekene **Pandas, Statsmodels og Scikit-learn**:

1.  **Dataklargjøring (Vask):** Rådata fra ERP-systemet er aggregert fra transaksjonsnivå til dagsnivå. Dette inkluderer fjerning av identifisert støy og konvertering av tidsformater for å skape en sammenhengende tidsserie.
2.  **Modellering og estimering:** Modellene trenes på historiske data for å lære sesongmønstre og sammenhenger. Dette inkluderer en *grid-search* for å finne optimale parametere ($p,d,q$) for SARIMA og *feature engineering* for Random Forest.
3.  **Validering:** Modellene testes på "ukjente" data (testsettet). Her gjennomføres residualanalyse for å sjekke om modellene har fanget opp all systematisk informasjon (hvit støy).
4.  **Evaluering og Prognose:** Modellene sammenlignes ved bruk av MAE, MAPE og Bias, segmentert på normale dager og toppdager for å avdekke operasjonelle begrensninger.

## 5.3 Datagrunnlag og struktur
Primærdataene består av historiske uttrekk fra REMAs ERP-system for produktet "Lasagne Familiepakning". 
*   **Kilde:** Sekundærdata (historiske salgsordre).
*   **Periode:** 1. mars 2025 – 28. februar 2026.
*   **Observasjoner:** 365 daglige datapunkter.
*   **Variabler:** `Opprettelsesdato` (tidsstempel for ordre) og `Utlevert mengde` (volum i antall enheter).

## 5.4 Datakvalitet, antagelser og begrensninger
Dataene anses som svært pålitelige (**høy reliabilitet**) da de representerer faktiske fysiske bevegelser ved distribusjonssenteret. 

**Viktige antagelser og grep:**
*   **Ekstremverdier:** En uteligger på 171 enheter (7. april 2025) ble vurdert som ikke-representativ støy og fjernet. Dette gjøres for å sikre at modellens parametere ikke blir skjevkjørt av isolerte hendelser utenfor normal drift.
*   **Begrensning (Censored Demand):** Vi antar at de observerte kampanjedataene er påvirket av logistiske kapasitetstak. Dette er en metodisk begrensning, da modellen lærer å predikere *allokert volum* snarere enn *reell kundeetterspørsel*.
*   **Validitet:** Ved å bruke `Opprettelsesdato` sikrer vi høy indre validitet, da dette tidspunktet er nærmest den faktiske etterspørselsimpulsen fra butikk.

## 5.5 Oppdeling av data (Trening og Test)
For å simulere en reell prognosesituasjon og sikre at vi måler modellens generaliseringsevne (Out-of-sample test), er datasettet delt inn slik:
*   **Treningssett:** 1. mars 2025 – 31. desember 2025. Brukes til å bygge og justere modellene.
*   **Testsett:** 1. januar 2026 – 28. februar 2026. Brukes utelukkende til endelig evaluering.

Denne 80/20-splittingen er standard i tidsserieanalyse og sikrer at testperioden inneholder både normale dager og ettervirkninger av kampanjeperioder, noe som gir et realistisk bilde av modellens ytelse.

## 5.6 Statistisk oppsummering av datasettet
Tabell 1 oppsummerer de tekniske nøkkeltallene for tidsserien etter datavask, og gir en oversikt over nivået og variasjonen modellene må håndtere.

**Tabell 1: Teknisk oppsummering av datasettet (N=365)**

| Parameter | Verdi (Antall enheter) |
| :--- | :--- |
| Gjennomsnitt ($\mu$) | 11,5 |
| Standardavvik ($\sigma$) | 13,2 |
| **Variasjonskoeffisient (CV)** | **1,15** |
| Minimum | 0 |
| Maksimum (Normalisert) | 115 |

CV-verdien på 1,15 underbygger metodens fokus på modeller som tåler ujevn etterspørsel. Den statistiske spredningen viser at standardavviket er større enn gjennomsnittet, noe som er den primære utfordringen for prognosepresisjonen i dette caset.

# 6. Modellering
Dette kapittelet definerer og begrunner det valgte modellrammeverket. Modellvalget er ikke et resultat av en forhåndsbestemt hypotese, men en konsekvens av en iterativ utvalgsprosess basert på de spesifikke egenskapene ved REMAs etterspørselsdata.

## 6.1 Arbeidsprosess og Modellutvalg
Utvalget av modeller ble gjort gjennom en eliminasjonsmetode der vi vurderte ulike statistiske og algoritmiske tilnærminger opp mot datasettets kompleksitet. 

I den innledende fasen ble **Moving Average (MA)** og enkle eksponensielle utglatningsmetoder vurdert. Disse ble imidlertid raskt forkastet som primærmodeller. Årsaken var at Moving Average, selv med ulike vindusstørrelser (f.eks. MA7 eller MA14), utviste en uakseptabel treghet i å respondere på de brå volumendringene som karakteriserer "Lasagne Familiepakning". MA-modeller tenderer til å "glatte ut" nettopp de toppene som er kritiske for logistikkplanleggingen ved REMA 1000, og de mangler evnen til å fange opp den systematiske ukedagseffekten uten omfattende manuelle justeringer.

## 6.2 Valg av modeller og deres utfyllende roller
For å dekke de ulike aspektene ved etterspørselsmønsteret, landet vi på tre modeller som representerer ulike metodiske styrker:

1.  **Seasonal Naïve (Baseline):** Valgt som en konservativ referanse. Gitt den sterke ukedagseffekten identifisert i kapittel 4, er dette en mer realistisk baseline enn et simpelt gjennomsnitt. Den tvinger de mer avanserte modellene til å bevise at de kan tilføre verdi utover det å "kopiere forrige uke".
2.  **SARIMA (Stastistisk fundament):** Valgt som den primære lineære modellen. SARIMA (Seasonal Autoregressive Integrated Moving Average) er spesielt egnet her fordi den integrerer sesongmessige differensiering. Dette gjør det mulig å fjerne den ukentlige syklusen matematisk og modellere de gjenværende avvikene som en funksjon av tidligere feil og observasjoner. Dette er avgjørende for å håndtere "støyen" mellom kampanjeperiodene.
3.  **Random Forest (Ikke-lineær benchmark):** Valgt for å kompensere for SARIMAs svakheter ved ekstreme utslag. Mens SARIMA er bundet av lineære sammenhenger, kan Random Forest gjennom sine beslutningstrær fange opp komplekse, ikke-lineære interaksjoner mellom ukedag, historiske topper og glidende trender. Ved å inkludere denne maskinlæringstilnærmingen, kan vi undersøke om algoritmer som ikke forutsetter en spesifikk statistisk distribusjon, er bedre rystet til å håndtere de logistiske "klumpene" i etterspørselen.

## 6.3 Datastrukturens påvirkning på modellarkitekturen
Modellene er konfigurert spesifikt for å respondere på tre identifiserte strukturelle trekk:
*   **Sesongvariasjon ($s=7$):** Både SARIMAs sesongledd og Random Forests lags er låst til 7 dager for å speile butikkenes ukentlige bestillingsrytme.
*   **Topper og ikke-lineæritet:** Bruken av Random Forest er direkte motivert av de "flate platåene" i kampanjedataene (ref. kapittel 4.3). Vi antok at en tre-basert modell ville være bedre til å gjenkjenne de logistiske grensene (f.eks. maksimale ordrestørrelser) enn en ren statistisk tidsseriemodell.
*   **Stasjonaritet:** Behovet for å stabilisere tidsserien før modellering dikterte bruken av differensiering i SARIMA ($d=1, D=1$).

## 6.4 Modellspesifikasjon
Modellene er teknisk spesifisert slik:
*   **SARIMA-struktur:** Defineres som $(p,d,q)(P,D,Q)_7$. Her representerer de sesongmessige leddene ($P,D,Q$) modellens evne til å "huske" hva som skjedde for nøyaktig 7 dager siden. Parameterne $(1,1,1)(1,1,1)_7$ er valgt etter en metodisk grid-search beskrevet i kapittel 7.
*   **Random Forest-vektor:** Modellen mottar en input-vektor bestående av laggede verdier ($y_{t-1}, y_{t-7}, y_{t-14}$), et 7-dagers glidende gjennomsnitt, og binære variabler (dummies) for ukedager.

## 6.5 Metodisk refleksjon
Ved å kombinere en klassisk statistisk modell (SARIMA) med en moderne maskinlæringsmodell (Random Forest), oppnår vi en metodisk triangulering. Dette gjør det mulig å skille mellom feil som skyldes modellens begrensninger (f.eks. manglende evne til å modellere lineært) og feil som skyldes fundamentale mangler i datagrunnlaget (f.eks. manglende informasjon om kampanjestart). Modellvalget er dermed ikke bare et forsøk på å finne den mest presise prediksjonen, men også et verktøy for å diagnostisere etterspørselens natur ved REMA 1000.

## 6.6 Oppsummering og videre steg
Dette kapittelet har etablert det teoretiske grunnlaget og begrunnet valget av modeller. I neste kapittel (Analyse) vil vi ta disse modellene i bruk og beskrive selve den tekniske gjennomføringen og valideringen på faktiske data.

# 7. Analyse
Dette kapittelet presenterer den operative gjennomføringen av analysen. Prosessen følger en strukturert tilnærming fra datavurdering og parameterisering til endelig validering av modellene. Fokus ligger på den metodiske reisen for å identifisere de mest robuste prediksjonsverktøyene for REMA 1000 Distribusjon Trondheim.

## 7.1 Datavurdering og egnethet for modellering
Før modellering ble datagrunnlaget vurdert med hensyn til stasjonaritet og prediksjonspotensial. Tidsserien for "Lasagne Familiepakning" ble analysert for å bekrefte at de statistiske forutsetningene for tidsserieanalyse var til stede. 

Gjennom en visuell inspeksjon av autokorrelasjonsfunksjonen (ACF) ble det identifisert sterke sesongmessige avhengigheter ved lag 7, 14 og 21. Dette bekrefter at etterspørselen har en deterministisk ukentlig komponent som gjør den egnet for sesongbaserte modeller som SARIMA og Seasonal Naïve. Videre ble stasjonaritet vurdert; selv om rådataene viser volatilitet under kampanjer, ble serien vurdert som trend-stasjonær nok til at sesongmessig differensiering ($D=1$) i SARIMA-modellen kunne stabilisere variansen og gjennomsnittet over tid. Håndteringen av ekstremverdier, spesielt fjerningen av den identifiserte støykilden i april 2025, var et nødvendig metodisk grep for å sikre at modellene lærte av representativ etterspørsel og ikke av isolerte systemfeil eller logistiske avvik.

## 7.2 Modelltesting og Parameterisering (Tuning)
For å identifisere de mest presise modellene ble det gjennomført en omfattende testfase der ulike konfigurasjoner ble veid mot hverandre. Dette var en iterativ prosess preget av "trial and error" for å finne den optimale balansen mellom kompleksitet og generaliseringsevne.

*   **SARIMA-optimering:** For SARIMA-modellen ble det benyttet en systematisk *grid-search*-metodikk. Vi testet ulike kombinasjoner av autoregressive ($p$) og glidende gjennomsnitt ($q$) parametere, både for den ikke-sesongmessige og den sesongmessige delen av modellen. Prosessen innebar å minimere Akaike Information Criterion (AIC) i treningsfasen, samtidig som vi overvåket modellens evne til å konvergere. Valget av $(1,1,1)(1,1,1)_7$ ble gjort etter å ha observert at økt kompleksitet (høyere orden av $p$ eller $q$) ikke ga signifikant reduksjon i treningsfeilen, men økte risikoen for overtilpasning (overfitting).
*   **Random Forest Feature Engineering:** For maskinlæringstilnærmingen lå hovedfokuset på å konstruere relevante forklaringsvariabler (*features*). Vi testet ulike sett av historiske lags og glidende gjennomsnitt. Gjennom en vurdering av *feature importance* identifiserte vi at $y_{t-7}$ og $y_{t-1}$ var de mest kritiske input-variablene. Modellen ble også testet med og uten ukedag-dummies for å vurdere i hvilken grad de binære variablene utfylte informasjonen i de historiske lags-ene.
*   **Sammenligningsgrunnlag:** Seasonal Naïve ble benyttet som en kontrollmodell gjennom hele prosessen. Ved å kontinuerlig måle forbedringen av SARIMA og Random Forest mot denne baseline-modellen, kunne vi kvantifisere merverdien av den økte matematiske kompleksiteten.

## 7.3 Estimeringsprosess og Segmenteringsstrategi
Estimeringen ble utført ved å trene modellene på data fra mars til desember 2025, og deretter utføre prediksjoner på det uavhengige testsettet (januar–februar 2026). Dette sikrer en realistisk evaluering av modellene på "ukjente" data.

En sentral del av vår analysemetodikk er **segmentert evaluering**. Gitt de ekstreme forskjellene i etterspørsel under kampanjer, vurderte vi det som metodisk utilstrekkelig å kun se på globale gjennomsnitt (som total MAE). Vi valgte derfor å splitte testsettet i to segmenter basert på en terskelverdi (90-persentilen i treningssettet):
1.  **Normale driftsdager:** For å evaluere modellens presisjon i den daglige, stabile vareflyten.
2.  **Toppdager:** For å isolere modellens evne til å håndtere kampanjer og ekstreme utslag.

Denne metodiske splittingen er avgjørende for å kunne gi REMA 1000 et nyansert beslutningsgrunnlag, da en modells styrke i ett segment kan overskygge kritiske svakheter i et annet.

## 7.4 Valideringsmetodikk og Residualanalyse
For å validere om modellene faktisk har ekstrahert all tilgjengelig informasjon fra datasettet, ble det gjennomført en grundig analyse av residualene (feilleddene). Valideringen fokuserte på to hovedaspekter:

1.  **Autokorrelasjon i feilene:** Vi benyttet ACF-plott av residualene for å sjekke om det var gjenværende mønstre modellene ikke hadde fanget opp. Dersom residualene ligner "hvit støy" (ingen signifikante lags), er modellen matematisk validert for den gitte tidsserien.
2.  **Systematisk bias:** Ved å analysere den gjennomsnittlige feilen (Bias) i de ulike segmentene, validerte vi i hvilken grad modellene har en tendens til systematisk over- eller underestimering. Dette er et kritisk steg for å forstå de operasjonelle risikoene ved å ta modellene i bruk i et reelt logistikksystem.

Denne systematiske tilnærmingen sikrer at de endelige resultatene (presentert i kapittel 8) ikke bare er tilfeldige observasjoner, men produkter av en kontrollert og etterprøvbar analyseprosess.

# 8. Resultatoppsummering
Dette kapittelet presenterer de numeriske funnene fra evalueringen av prognosemodellene på testsettet for januar og februar 2026. Resultatene er delt inn i en global evaluering og en segmentert analyse for å belyse modellenes styrker og svakheter under ulike driftsforhold.

## 8.1 Global Modellytelse
For å få et overordnet bilde av modellenes presisjon, ble feilmålene MAE, MAPE og Bias beregnet for hele testperioden. Tabell 2 oppsummerer den globale ytelsen for de tre testede modellene. Resultatene viser at Random Forest oppnår den laveste gjennomsnittlige feilen (MAE 14,81), etterfulgt av SARIMA (MAE 19,23). Begge de avanserte modellene viser en forbedring sammenlignet med Seasonal Naïve-baselinen, som har en MAE på 21,18.

**Tabell 2: Global evaluering av modeller på testsettet (Jan-Feb 2026)**

| Modell | MAE (Enheter) | MAPE (%) | Bias (Enheter) |
| :--- | :--- | :--- | :--- |
| Seasonal Naïve (Baseline) | 21,18 | 1073 % | 0,10 |
| SARIMA (Hovedmodell) | 19,23 | 396 % | -19,19 |
| **Random Forest (Benchmark)** | **14,81** | **464 %** | **-3,22** |

Det er verdt å merke seg de svært høye MAPE-verdiene. Dette skyldes i stor grad dager med svært lavt faktisk volum, der selv små absolutte avvik gir store prosentvise utslag. MAE vurderes derfor som det mest pålitelige målet for operativ planlegging i dette caset.

## 8.2 Segmentert Resultatanalyse
For å undersøke modellenes evne til å håndtere kampanjevariasjoner, ble testsettet splittet i "Normale dager" (salg ≤ 51,9 enheter) og "Toppdager" (salg > 51,9 enheter). Tabell 3 presenterer resultatene fra denne segmenteringen. 

Analysen avslører et markant skille i presisjon: Under normaldrift er Random Forest svært treffsikker med en MAE på kun 6,56 enheter. På toppdager øker imidlertid feilraten dramatisk for samtlige modeller. Random Forest har her en MAE på 90,75 enheter, kombinert med en tilsvarende negativ bias. Dette bekrefter at modellen konsekvent underestimerer etterspørselen når den når ekstreme nivåer.

**Tabell 3: Segmentert feilanalyse (MAE og Bias)**

| Segment | Modell | MAE | Bias |
| :--- | :--- | :--- | :--- |
| **Normale dager** | Seasonal Naïve | 12,33 | 11,02 |
| (Salg <= 51,9) | SARIMA | 9,43 | -9,38 |
| | **Random Forest** | **6,56** | **6,25** |
| **Toppdager** | Seasonal Naïve | 102,60 | -102,60 |
| (Salg > 51,9) | SARIMA | 109,44 | -109,44 |
| | **Random Forest** | **90,75** | **-90,75** |

Oppsummert viser resultatene at de valgte tidsseriemodellene er meget effektive for å predikere stabil etterspørsel, men at de uten ekstern kampanjeinformasjon har en systematisk begrensning i å fange opp de største logistiske utslagene ved REMA 1000 Distribusjon Trondheim. Dette danner grunnlaget for diskusjonen i kapittel 9.

# 9. Diskusjon
Dette kapittelet drøfter funnene knyttet til den systematiske underestimeringen av topper og de operasjonelle konsekvensene dette har for REMA 1000.

## 9.1 Tolkning av modellresultater og Bias
Hovedfunnet er at Random Forest og SARIMA gir en betydelig forbedring over baseline på normale dager, men at alle modeller svikter ved ekstreme etterspørselsutslag. En bias på -90,75 enheter på toppdager innebærer at modellene i mange tilfeller predikerer en etterspørsel som er vesentlig lavere enn det faktiske behovet.

Denne negative biasen kan tilskrives fraværet av kampanjevariabler i modellene. Siden vi metodisk har valgt å basere oss utelukkende på historisk salg og kalenderdata, har modellene ingen mulighet til å "forutse" når en kampanje inntreffer, selv om de er gode til å fange opp de generelle mønstrene mellom kampanjene.

## 9.2 Praktisk betydning for logistikk og vareflyt
Den observerte underestimeringen har kritiske konsekvenser for planlegging og drift:
1.  **Risiko for manglende leveringsevne:** Vedvarende negativ bias på dager med høyt volum øker sannsynligheten for "stockouts", der faktisk etterspørsel overstiger planlagt kapasitet.
2.  **Operasjonell usikkerhet:** Systematiske avvik tvinger logistikksystemet til å jobbe reaktivt, med behov for hasteordre og ekstratransport for å dekke det udekkede behovet på ca. 90 enheter per toppdag.
3.  **Kapasitetsplanlegging:** Selv om Random Forest fanger opp ikke-lineære mønstre i kalenderdata bedre enn SARIMA, er ingen av modellene robuste nok til å brukes som eneste beslutningsgrunnlag for dimensjonering av ressurser under store kampanjer uten manuelle justeringer.
4.  **Bullwhip-effekt:** Den systematiske underestimeringen i distribusjonsleddet er operasjonelt utfordrende da den kan forplante seg som usikkerhet bakover i forsyningskjeden. Når distribusjonssenteret konsekvent rapporterer lavere forventet behov enn de faktiske toppene, vil dette kunne trigge overdrevne ordrereaksjoner i tidligere ledd når de faktiske volumene inntreffer, noe som forsterker bullwhip-effekten.
5.  **Implikasjoner for sikkerhetslager:** I tråd med Seiringer et al. (2024), har både MAE og bias direkte innvirkning på dimensjoneringen av sikkerhetslager. En negativ bias innebærer at sikkerhetslageret må være betydelig høyere for å opprettholde ønsket servicegrad, noe som øker lagerbinding og tilhørende kostnader. Nøyaktige prognoser er derfor en forutsetning for å minimere behovet for slike kostbare buffere i logistikksystemet.

# 10. Konklusjon
Dette prosjektet har undersøkt prognosepresisjon for "Lasagne Familiepakning" ved REMA 1000 Distribusjon Trondheim.

Hovedkonklusjonene er:
1.  **Modellvalidering:** Random Forest oppnår høyest presisjon i segmentet for normale dager (MAE 6,56). SARIMA-modellen fanger effektivt opp sesongvariasjoner og representerer en robust statistisk tilnærming for stabil drift.
2.  **Systematisk underestimering:** Analysen dokumenterer en betydelig negativ bias på dager med ekstraordinært høyt salgsvolum. Dette indikerer at historiske tidsseriedata alene har begrensninger når det gjelder å fange opp de kraftigste etterspørselstoppene.
3.  **Behov for forklaringsvariabler:** Residualanalysen bekrefter at de gjenværende feilene i stor grad er uforutsigbare innenfor rammen av dagens datagrunnlag. Analysen viser at begrensningen i prognosepresisjon primært skyldes manglende forklaringsvariabler for topper (som kampanjer), og ikke valget av selve modellen. For å redusere bias i topp-perioder og forbedre leveringsevnen, er integrasjon av eksterne variabler som kampanjekalendere en nødvendig forutsetning.

Konklusjonen er at tidsserie-baserte metoder gir høy presisjon i normaldrift, men at logistikksystemet må suppleres med ekstern informasjon for å håndtere planlagte kampanjer og sikre optimal vareflyt.

# 11. Bibliografi
Arunraj, N. S., & Ahrens, D. (2015). A hybrid seasonal autoregressive integrated moving average and quantile regression for daily food sales forecasting. *International Journal of Production Economics*, 170, 147-160. https://doi.org/10.1016/j.ijpe.2015.09.014

Fildes, R., Goodwin, P., Lawrence, M., & Nikolopoulos, K. (2009). Effective forecasting and judgmental adjustments: an empirical evaluation and strategies for improvement in supply-chain planning. *International Journal of Forecasting*, 25(1), 3-23. https://doi.org/10.1016/j.ijforecast.2008.11.010

Fildes, R., Ma, S., & Kolassa, S. (2022). Retail forecasting: Research and practice. *International Journal of Forecasting*, 38(4), 1269-1295. https://doi.org/10.1016/j.ijforecast.2021.11.004

Hyndman, R. J., & Koehler, A. B. (2006). Another look at measures of forecast accuracy. *International Journal of Forecasting*, 22(4), 679-688. https://doi.org/10.1016/j.ijforecast.2006.03.001

Makridakis, S., Spiliotis, E., & Assimakopoulos, V. (2022). The M5 competition: Background, organization, and results. *International Journal of Forecasting*, 38(4), 1325-1346. https://doi.org/10.1016/j.ijforecast.2021.01.005

Seiringer, W., Brockmann, F., Altendorfer, K., & Felberbauer, T. (2024). Influence of Forecast Error and Forecast Bias on Safety Stock on a MRP System with Rolling Horizon Forecast Updates. *Proceedings of the International Conference on Production Research*.

Syntetos, A. A., Boylan, J. E., & Disney, S. M. (2009). Forecasting for inventory planning: a review. *Journal of the Operational Research Society*, 60(1), S149-S160. https://doi.org/10.1057/jors.2008.173

Trapero, J. R., Kourentzes, N., & Fildes, R. (2015). On the importance of forecasting promotional sales: A retail case study. *International Journal of Forecasting*, 31(4), 1166-1176. https://doi.org/10.1016/j.ijforecast.2015.06.001

# 12. Vedlegg
*(Eventuelle tillegg som kodesnutter, rådata-eksempler eller utvidede tabeller)*
