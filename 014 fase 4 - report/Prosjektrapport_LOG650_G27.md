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

For å besvare denne problemstillingen vil vi utvikle og evaluere modeller basert på historisk volum (plukket/utlevert mengde). Selv om inkludering av forklaringsvariabler som kampanjeindikatorer og pris vurderes som teoretisk relevante, er selve analysen i denne oppgaven avgrenset til bruk av historiske salgs- og kalenderdata for å evaluere modellenes grunnleggende prediksjonsevne.

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

# 4. Casebeskrivelse
Dette kapittelet gir en beskrivelse av den operative konteksten for studien, med fokus på REMA 1000 Distribusjon Trondheim (RDT) og det utvalgte produktet, "Lasagne Familiepakning".

## 4.1 REMA 1000 Distribusjon Trondheim
REMA 1000 Distribusjon Trondheim fungerer som et sentralt logistikknutepunkt for vareforsyning til REMA 1000-butikker i Midt-Norge. Distribusjonssenterets primære oppgave er å sikre effektiv vareflyt fra produsenter til utsalgssteder. En av de største utfordringene i dette leddet er å balansere hensynet til høy kundeservicegrad (unngå "stockouts" i butikk) mot målet om lavest mulig kapitalbinding og effektiv lagerdrift.

Prognosepresisjon ved distribusjonssenteret er kritisk fordi feilmarginer her kan forsterkes gjennom forsyningskjeden (Bullwhip-effekten). Dersom senteret overestimerer etterspørselen, øker lagerkostnadene og risikoen for ukurans. Ved underestimering risikerer man leveringssvikt til butikkene, noe som direkte påvirker sluttkundens opplevelse og bedriftens omdømme.

## 4.2 Produktbeskrivelse: Lasagne Familiepakning
Produktet som er valgt for denne studien er "Lasagne Familiepakning". Dette er en tørrvare med lang holdbarhet, noe som i utgangspunktet reduserer risikoen for fysisk matsvinn sammenlignet med ferskvarer. Likevel er produktet preget av en dynamisk etterspørsel som gjør det velegnet for prognosemodellering:

- **Etterspørselsstabilitet:** I normale uker har produktet en relativt stabil og forutsigbar etterspørsel basert på faste leveringsrutiner til butikkene.
- **Kampanjefølsomhet:** Produktet inngår ofte i nasjonale kampanjer, som for eksempel "Crazy Days", noe som skaper kraftige salgstopper (spikes) som er utfordrende å predikere nøyaktig.
- **Strategisk betydning:** Som et volumprodukt i tørrvarekategorien representerer nøyaktige prognoser for denne varen et betydelig potensial for forbedret transport- og lagerplanlegging.

## 4.3 Kampanjemekanikk og volumstyring
For å forstå etterspørselsdataene for "Lasagne Familiepakning", er det nødvendig å skille mellom normale driftsperioder og kampanjeperioder som "Crazy Days".

I normale uker fungerer vareforsyningen etter et **pull-prinsipp**, der de enkelte REMA 1000-butikkene selvstendig bestiller varer fra distribusjonssenteret basert på lokalt behov. Under "Crazy Days"-kampanjer endres imidlertid denne dynamikken til en mer sentralt styrt prosess:

1.  **Sentral allokering:** Hovedkontoret velger ut kampanjevarer og fastsetter aggressive priser. Butikkene har i disse periodene begrenset handlingsrom for fri bestilling. Volumene blir ofte forhåndsallokert til butikkene basert på historisk salg, butikkstørrelse og sentrale prognoser.
2.  **Volumstyring og tak:** For å sikre en rettferdig fordeling av varer og unngå kritiske "stockouts"-situasjoner tidlig i kampanjeperioden, opereres det ofte med anbefalte volumer eller maksimale bestillingsgrenser per butikk. 
3.  **Standardiserte kollistørrelser:** Varene distribueres ofte i faste, store kolli (pakkestørrelser). Dette medfører at bestillingene skjer i "trinn" (f.eks. multipler av 96 eller 120 enheter), noe som skaper tydelige "klumper" i etterspørselsmønsteret.

Disse mekanismene forklarer de observerte "platåene" i datasettet, der etterspørselen stabiliserer seg på spesifikke nivåer (som de identifiserte 115-enhets-toppene). Dette er ikke nødvendigvis et uttrykk for en mettet kundeetterspørsel, men snarere et resultat av logistiske begrensninger og sentrale styringsregler. For prognosearbeidet betyr dette at modeller må ta hensyn til at kampanjedataene er preget av slike kapasitetsbegrensninger (censored demand).

## 4.4 Identifiserte etterspørselsmønstre
Gjennom en foreløpig deskriptiv analyse av de vaskede salgsdataene er følgende mønstre identifisert for analyseperioden:

1.  **Ukedagseffekt:** Det er observert systematiske variasjoner gjennom uken, der mandager ofte har den høyeste utleverte mengden. Dette skyldes trolig butikkenes behov for å fylle opp hyllene etter storhandelen i helgen. Som vist i Figur 2, bekrefter analysen en tydelig sesongvariasjon innenfor uken, noe som er karakteristisk for dagligvarelogistikk (Arunraj & Ahrens, 2015).
2.  **Kampanjeperioder (Crazy Days):** Det er identifisert to markante salgstopper i løpet av perioden som sammenfaller med "Crazy Days"-kampanjer. Den mest omfattende toppen ble observert i oktober 2025 (uke 44), der etterspørselen lå stabilt på et nivå betydelig over normalen. Figur 1 illustrerer den historiske tidsserien og de markante avvikene fra normal etterspørsel.
3.  **Sesongvariasjon:** Dataene indikerer lavere utlevert volum i fellesferien (juli/august), noe som kan knyttes til endrede handlevaner i sommerferien og redusert aktivitet i regionen.

![Figur 1: Historisk tidsserie for Lasagne Familiepakning](figurer/fig1_tidsserie.png)
**Figur 1: Historisk tidsserie (mars 2025 – februar 2026) som viser variasjon i utlevert volum og markante topper under kampanjeperioder.**

![Figur 2: Gjennomsnittlig etterspørsel per ukedag](figurer/fig2_ukedag.png)
**Figur 2: Gjennomsnittlig utlevert volum fordelt på ukedager, som dokumenterer den systematiske ukedagseffekten med høyest aktivitet på mandager.**

# 5. Metode og data
Dette kapittelet beskriver studiens metodiske fundament, datagrunnlaget og prosessene som er benyttet for å transformere rådata til et beslutningsgrunnlag for prognosemodellering.

## 5.1 Forskningsdesign: Kvantitativ Case-studie
Studien benytter et kvantitativt forskningsdesign basert på en case-studie av REMA 1000 Distribusjon Trondheim. Valget av kvantitativ metode er begrunnet i studiens behov for å analysere historiske transaksjonsdata for å identifisere mønstre og evaluere numerisk nøyaktighet i prognoser. Case-studiedesignet muliggjør en dypere forståelse av hvordan spesifikke faktorer, som "Crazy Days"-kampanjer, påvirker etterspørselen i en reell logistisk kontekst.

## 5.2 Datainnsamling og Kildekritikk
Primærdataene består av historiske uttrekk fra REMAs ERP-systemer (Enterprise Resource Planning). 

- **Datakilde:** Sekundærdata i form av historiske salgs- og innkjøpstransaksjoner for perioden mars 2025 til februar 2026.
- **Kildekritikk:** Dataene anses som svært pålitelige da de representerer faktiske fysiske bevegelser (plukk og mottak) ved distribusjonssenteret. En potensiell feilkilde er eventuelle systemfeil eller manuelle korrigeringer i ERP-systemet som ikke reflekterer fysisk etterspørsel, men slike avvik antas å være statistisk insignifikante i det store datamaterialet.

## 5.3 Databehandling og Vaskeprosess
For å klargjøre dataene for tidsserieanalyse, ble det gjennomført en omfattende vaskeprosess ved bruk av programmeringsspråket **Python (versjon 3.x)** og biblioteket **Pandas** for datamanipulering. Dette er et kritisk steg for å sikre etterprøvbarhet:

1.  **Valg av tidsvariabel:** Vi har valgt `Opprettelsesdato` som den primære tidsvariabelen. I logistikksammenheng representerer dette tidspunktet butikken legger inn ordren, noe som gir det mest presise bildet av etterspørselen sammenlignet med `Plukkdato`.
2.  **Aggregering til dagsnivå:** Rådataene inneholder hver enkelt ordrelinje (transaksjonsnivå). Ved å summere alle bestillinger per dag ved hjelp av `groupby`-funksjonalitet, skaper vi en sammenhengende tidsserie som er nødvendig for de valgte prognosemodellene.
3.  **Tegnsett og Format:** Alle filer ble konvertert til UTF-8 koding for å sikre korrekt visning av norske tegn (æ, ø, å).
4.  **Håndtering av ekstremverdier (Outliers):** Gjennom vaskeprosessen ble det identifisert en ekstremverdi på 171 enheter den 7. april 2025. Da denne verdien er mer enn sju ganger høyere enn gjennomsnittet og ikke sammenfaller med kjente nasjonale kampanjer, er den vurdert som en ikke-representativ engangshendelse (eksempelvis nyåpning av butikk eller feilbestilling). For å unngå at denne verdien skjevkjører (bias) prognosemodellene, er den dokumentert som en støykilde i datamaterialet.

Resultatet av denne prosessen er datasettene `vasket_salg_daglig.csv` og `vasket_innkjop_daglig.csv`. Analysen og visualiseringen er utført med bibliotekene **NumPy** for numeriske operasjoner og **Matplotlib/Seaborn** for grafisk fremstilling.

## 5.4 Analysemetoder og Evaluering
For å evaluere hvor gode prognosemodellene er, benytter vi to anerkjente statistiske feilmål:

- **MAE (Mean Absolute Error):** Måler det gjennomsnittlige avviket i faktiske enheter. Dette er lett å tolke for logistikkplanleggere (f.eks. "vi bommer i snitt med 10 kasser"). MAE er vårt primære evalueringsmål for dager med svært lav eller null etterspørsel.
- **MAPE (Mean Absolute Percentage Error):** Måler det prosentvise avviket. Dette gjør det mulig å sammenligne prognosepresisjon på tvers av ulike produkter med ulikt salgsvolum. Vi er imidlertid oppmerksomme på at MAPE har matematiske begrensninger ved null-etterspørsel ($A_t = 0$), da formelen involverer divisjon med faktisk verdi. I slike tilfeller vil MAPE enten ekskludere disse observasjonene eller gi urealistisk høye feilprosenter. For å sikre en robust evaluering, kombineres derfor alltid MAPE med MAE for å gi et balansert bilde av modellenes nøyaktighet.

## 5.5 Splitting av data (Trening og Test)
Datasettet er delt i et treningssett og et testsett (Out-of-sample test). Dette simulerer en reell situasjon der man skal forutsi fremtiden basert på fortiden.

- **Treningssett (Train):** 01.03.2025 – 31.12.2025. Brukes til parameterestimering og modellutvikling.
- **Testsett (Test):** 01.01.2026 – 28.02.2026. Brukes utelukkende til evaluering av prognosepresisjon.

# 6. Modellering
For å besvare problemstillingen er det etablert to enkle baseline-modeller, samt en maskinlæringsmodell som benytter tilgjengelige kalender- og historiske data.

## 6.1 Baseline-modeller
Som referansepunkt for evalueringen benyttes to standardmetoder:
1.  **Seasonal Naive (SN):** Denne modellen antar at etterspørselen for en gitt ukedag er identisk med samme ukedag forrige uke. Dette fanger opp den sterke "mandagseffekten" identifisert i EDA-en.
2.  **SARIMA (Hovedmodell):** En avansert statistisk tidsseriemodell som kombinerer autoregresjon (AR), differensiering (I) og glidende gjennomsnitt (MA), tilpasset både trend og sesongvariasjoner i datasettet.

## 6.2 Random Forest (Benchmark)
Som en mer avansert sammenligningsmodell benyttes en Random Forest-regressor. Denne maskinlæringsmetoden er valgt for sin evne til å fange opp ikke-lineære mønstre uten å kreve antagelser om dataenes fordeling. Modellen er spesifisert med følgende uavhengige variabler for å unngå data leakage:
- **Laggede variabler:** Historisk etterspørsel fra t-1, t-7 og t-14 dager tilbake.
- **Glidende gjennomsnitt:** Et 7-dagers glidende snitt av historisk salg.
- **Kalenderdata:** One-hot encoding av ukedag for å fange opp systematiske ukentlige svingninger.

Ved å utelate kampanjevariabler eksplisitt, evalueres modellens evne til å predikere etterspørsel utelukkende basert på mønstre i den historiske tidsrekken. Det ble vurdert å inkludere en proxy for kampanjer basert på etterspørselsmønstre, men dette ble forkastet på grunn av risiko for *data leakage*. Bruk av indirekte eller fremtidig informasjon i modelleringen er metodisk problematisk da det kan gi et urealistisk bilde av prognoseevnen i sanntid. Modellen benytter derfor kun historisk salg og kalenderdata.

# 7. Analyse
Dette kapittelet presenterer den statistiske evalueringen av modellene, med fokus på segmentert feilanalyse og residualanalyse for å identifisere systematiske avvik.

Analysen er strukturert i tre trinn for å gi en helhetlig vurdering av prognosepresisjon. Først evalueres den samlede nøyaktigheten for testperioden. Deretter gjennomføres en segmentert analyse der vi skiller mellom normale dager og toppdager for å avdekke modellenes begrensninger ved ekstreme volumutslag. Til slutt benyttes residualanalyse for å vurdere i hvilken grad modellene har evnet å fange opp den systematiske strukturen i dataene.

# 8. Resultat
Dette kapittelet presenterer resultatene fra evalueringen av de tre prognosemodellene i testperioden januar–februar 2026. Modellene er evaluert uten bruk av kampanjevariabler for å sikre metodisk validitet og unngå "data leakage".

## 8.1 Sammenligning av prognosepresisjon
Evalueringen indikerer at Random Forest oppnår den laveste gjennomsnittlige feilraten i testperioden, med særlig styrke i segmentet for normale dager. SARIMA fremstår som en robust statistisk hovedmodell, mens Seasonal Naïve benyttes som baseline for å fange opp gjentakende ukentlige sesongmønstre. Figur 3 og 4 gir en visuell sammenligning av modellene mot de faktiske salgsdataene i testperioden.

![Figur 3 & 4: Sammenligning av modeller i testperioden](figurer/fig3_4_modellsammenligning.png)
**Figur 3 & 4: Visualisering av prediksjoner fra SARIMA og Random Forest mot faktiske salgsdata. Modellene følger grunnleggende sesongvariasjoner godt, men viser tydelige avvik ved brå endringer.**

**Tabell 2: Global evaluering av modeller på testsettet (Jan-Feb 2026)**

... (tabell innhold) ...

## 8.2 Segmentert feilanalyse og Bias
For å forstå modellenes begrensninger i perioder med høy etterspørsel, ble testsettet delt inn i "normale dager" og "toppdager". Terskelverdien for en toppdag er beregnet til **51,90 enheter**, tilsvarende 90-persentilen i treningssettet. Som illustrert i Figur 5, skaper kampanjeaktivitet etterspørselstopper som ligger langt over modellens prediksjonsnivå.

![Figur 5: Kampanjeeffekt og modellavvik](figurer/fig5_campaign_impact.png)
**Figur 5: Detaljvisning av kampanjeeffekt der faktiske salgstopper (spikes) sammenlignes med modellenes prognoser, noe som tydeliggjør den systematiske underestimeringen (negative bias).**

**Tabell 3: Segmentert feilanalyse (MAE og Bias)**

| Segment | Modell | MAE | Bias |
| :--- | :--- | :--- | :--- |
| **Normale dager** | Seasonal Naïve | 12,33 | 11,02 |
| (Salg <= 51,9) | SARIMA | 9,43 | -9,38 |
| | **Random Forest** | **6,56** | **6,25** |
| **Toppdager** | Seasonal Naïve | 102,60 | -102,60 |
| (Salg > 51,9) | SARIMA | 109,44 | -109,44 |
| | **Random Forest** | **90,75** | **-90,75** |

Resultatene viser en tydelig **negativ bias** for alle modeller på toppdager. Denne systematiske underestimeringen av topper er i tråd med funn fra Trapero et al. (2015), som understreker utfordringene ved å fange opp kampanjedrevet etterspørsel uten eksplisitte forklaringsvariabler. Selv om Random Forest er den mest presise modellen på dager med normalt volum, underestimerer den etterspørselen med i gjennomsnitt 90,75 enheter på dager der salget overstiger 90-persentilen.

## 8.3 Residualanalyse
Residualanalyse gjennomføres for å kontrollere om all systematisk struktur i dataene er fanget opp av modellen. Residualanalysen (ACF-plott) av feilene viser at SARIMA og Random Forest har eliminert det meste av autokorrelasjonen i tidsserien. 

![Figur 6: ACF-plott av residualer](figurer/fig6_residual_acf.png)

**Figur 6: Autokorrelasjonsfunksjon (ACF) for residualene til de tre testede modellene.**

Som vist i Figur 6, fremstår de gjenværende feilene for SARIMA og Random Forest i stor grad som uforutsigbar variasjon (støy), da de fleste laggene ligger innenfor konfidensintervallet. Dette indikerer at modellene utnytter de tilgjengelige historiske dataene og kalenderdataene effektivt. Den systematiske underestimeringen på toppdager (identifisert i bias-analysen) bekrefter imidlertid at informasjonen som kreves for å predikere disse toppene ikke ligger latent i selve salgshistorikken.

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
