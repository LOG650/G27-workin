

























******************Prognosepresisjon ved REMA 1000 Distribusjon Trondheim******



Line Lyngsnes Johansen og Amanda Arnesen Almaas



Totalt antall sider inkludert forsiden:      



Molde, 27. februar 2026





**Obligatorisk egenerklæring****/gruppeerklæring**** **



Den enkelte student er selv ansvarlig for å sette seg inn i hva som er lovlige hjelpemidler, retningslinjer for bruk av disse og regler om kildebruk. Erklæringen skal bevisstgjøre studentene på deres ansvar og hvilke konsekvenser fusk kan medføre. Manglende erklæring fritar ikke studentene fra sitt ansvar.











**Personvern**



**Personopplysningsloven**

Forskningsprosjekt som innebærer behandling av personopplysninger iht. Personopplysningsloven skal meldes til Norsk senter for forskningsdata, NSD, for vurdering.



**Har oppgaven vært vurdert av NSD?****	****	****	****	****	****ja****	 ************************nei**

- Hvis ja: 

**Referansenummer:**** ******************** **** **** **** **** ******

- Hvis nei: 

**Jeg/vi erklærer at oppgaven ikke**** omfattes av Personopplysningsloven: ****	**



**Helseforskningsloven**

Dersom prosjektet faller inn under Helseforskningsloven, skal det også søkes om forhåndsgodkjenning fra Regionale komiteer for medisinsk og helsefaglig forskningsetikk, REK, i din region.



**Har oppga****ven vært til behandling hos REK?****	****	****	****	****ja****	 ************************nei**

- Hvis ja: 

**Referansenummer:**** ******************** **** **** **** **** ******







**Publiseringsavtale**



**Studiepoeng: ******************** **** **** **** **** ********	****	****	**

**Veileder: ******************** **** **** **** **** ******



**Fullmakt til elektronisk publisering av oppgaven**

Forfatter(ne) har opphavsrett til oppgaven. Det betyr blant annet enerett til å gjøre verket tilgjengelig for allmennheten (Åndsverkloven. §2).

Alle oppgaver som fyller kriteriene vil bli registrert og publisert i Brage HiM med forfatter(ne)s godkjennelse.

Oppgaver som er unntatt offentlighet eller båndlagt vil ikke bli publisert.



**Jeg/vi gir herved Høgskolen i Molde en vederlagsfri rett til å **

**gjøre oppgaven tilgjengelig for elektronisk publisering: ****	****	****ja****	 ************************nei**



**Er oppgaven båndlagt (konfidensiell)?****	****	****	****	****	************************ja****	 ************************nei**

**(**Båndleggingsavtale må fylles ut)

- Hvis ja: 

**Kan oppgaven publiseres når båndleggingsperioden er over?****	****	************************ja****	 ************************nei**



**Dato: ******************** **** **** **** **** ******





**Antall ord: **Marker denne setningen, og skriv inn antall ord dersom det er et krav at antall ord skal oppgis. Hvis det ikke er et krav at antall ord skal oppgis slettes hele dette avsnittet, og i begge tilfeller slettes denne setning. 



**Forfattererklæring**: Marker denne setningen, og skriv inn forfattererklæring dersom det er et krav til oppgaven. Hvis det ikke er krav om forfattererklæring slettes hele dette avsnitt, og i begge tilfeller slettes denne setning. 









**Sammendrag**

Denne rapporten undersøker prognosepresisjon for daglig etterspørsel ved REMA 1000 Distribusjon Trondheim. Formålet med studien er å evaluere i hvilken grad tidsserie-baserte modeller kan predikere etterspørselen for utvalgte produkter, og hvordan faktorer som kampanjer og pris påvirker nøyaktigheten i disse prognosene. Ved bruk av historiske salgsdata og statistiske feilmål som MAE og MAPE, sammenlignes ulike modeller for å identifisere de mest effektive tilnærmingene for distribusjonsleddet. Foreløpige planer innebærer analyse av sammenhengen mellom planlagte kampanjer og faktiske salgstopper for å forbedre beslutningsgrunnlaget for lagerstyring og logistikkplanlegging.

**Abstract**

This report investigates the forecast accuracy of daily demand at REMA 1000 Distribution Trondheim. The objective of the study is to evaluate the extent to which time-series-based models can predict the demand for selected products, and how factors such as promotions and pricing influence the accuracy of these forecasts. Using historical sales data and statistical error measures like MAE and MAPE, various models are compared to identify the most effective approaches for the distribution stage. Preliminary plans include analyzing the correlation between planned promotions and actual sales peaks to enhance the decision-making basis for inventory management and logistics planning.







Innhold







































# Innledning

Dette prosjektet undersøker hvordan tidsserie-baserte metoder kan anvendes for å predikere daglig etterspørsel i distribusjonssystemer, med særlig fokus på REMA 1000 Distribusjon Trondheim. Prognosepresisjon er en kritisk faktor i supply chain management, da nøyaktige prognoser legger grunnlaget for effektiv lagerstyring, transportplanlegging og redusert matsvinn.

I dagens marked påvirkes etterspørselen av en rekke faktorer, herunder kampanjeaktiviteter og prisendringer. Ved å analysere historiske salgsdata, søker denne rapporten å avdekke i hvilken grad standardiserte tidsseriemodeller kan fange opp disse variasjonene og gi pålitelige estimater for fremtidig behov.

## Problemstilling

Problemstillingen for dette prosjektet er:

**I hvilken grad kan tidsserie-baserte prognosemetoder predikere daglig etterspørsel for utvalgte produkter ved REMA 1000 Distribusjon Trondheim, målt ved prognosepresisjon (forecast accuracy)?**

For å besvare hovedproblemstillingen vil vi også undersøke hvordan forklaringsvariabler som kampanje og pris påvirker modellens nøyaktighet.

## Delproblemer (valgfri)

## Avgrensinger

Prosjektet er avgrenset på følgende måte for å sikre en gjennomførbar og presis analyse:

- **Geografisk avgrensing:** Studien begrenses til ett distribusjonssenter, REMA 1000 Distribusjon Trondheim.
- **Produktutvalg:** Analysen gjennomføres på ett eller et begrenset antall utvalgte produkter, for å muliggjøre en dypere dykk i datakvalitet og modellering.
- **Tidsoppløsning:** Analysen utføres på daglig nivå.
- **Omfang:** Det utvikles ikke et fullstendig kommersielt prognosesystem, og prosjektet omfatter ikke optimalisering av lagerbeholdning eller transportruter utover selve prognosearbeidet.

## Antagelser

Følgende antagelser ligger til grunn for analysen:

- **Datatilgang:** Vi antar tilgang til minimum ett års historiske, anonymiserte data på dagsnivå fra REMA 1000 Distribusjon Trondheim.
- **Datakvalitet:** Vi forutsetter at dataene inkluderer faktisk plukket volum, kampanjeindikatorer og prisdata, og at disse er tilstrekkelig nøyaktige for statistisk modellering.
- **Konsistens:** Vi antar at historiske mønstre i etterspørselen har en viss grad av overførbarhet til fremtidige perioder under like forutsetninger.



# Litteratur

Diskuter de viktigste bidragene de 5 siste årene innen temaet du har valgt. Prøv å trekk tråder til din problemstilling og beskriv hvor og hvordan din rapport forholder seg til disse. Pass på at referanser blir korrekte. 

Det er ikke alltid nødvendig å ha et eget kapittel for litteratur, det viktigste av alt er at man aldri, *aldri* siterer noen eller kommer med fakta eller påstander, uten at det refereres til hvor du har denne påstanden ifra.  Dette kaller vi synsing, og synsing trekker ned karakteren kraftig.

Det kan ofte skje at man henviser til samme rapport flere ganger i teksten. Unngå da å repetere funnene i rapporten, men ha med selve referansen.

Husk en referanse har to hensikter:

Kreditere resultatet til de som fant det.

Gi leseren en mulighet til å sjekke opp en påstand eller fakta som du bygger rapporten din på.

# Teori

Når du skal skrive en bacheloroppgave, er det også viktig å inkludere en teoridel. Her skal du beskrive teoretisk perspektiv, tidligere litteratur som beskriver samme tema og hva forskere eventuelt er uenige om.



Du kan også nevne hvorvidt tidligere forskning kan ha oversett noen faktorer, og plassere egen problemstilling i lys av tidligere litteratur på fagfeltet. 

Pass på at du får frem hva problemstillingen din belyser, som ikke tidligere forskning allerede har gjennomgått.



Teoridelen din skal rett og slett beskrive grunnlaget for studiet ditt, og danner utgangspunktet for videre metodevalg.



# Casebeskrivelse

Dette prosjektet tar for seg logistikkutfordringene ved REMA 1000 Distribusjon Trondheim, som er et sentralt knutepunkt for vareforsyning til REMA 1000-butikker i regionen. En av de største utfordringene i distribusjonsleddet er å balansere lagernivåer mot kundeservicegrad, noe som krever svært presise etterspørselsprognoser.

### REMA 1000 Distribusjon Trondheim
Som en stor aktør innen dagligvarelogistikk håndterer distribusjonssenteret i Trondheim et enormt volum av varer med varierende holdbarhet og etterspørselsmønstre. For ferskvarer og andre kritiske varegrupper kan selv små avvik i prognosene føre til enten tomt lager (stock-out) eller unødvendig høyt svinn.

### Utfordringer med dagens prognoser
Etterspørselen i dagligvaremarkedet er preget av høy volatilitet. Spesielt to faktorer kompliserer prognosearbeidet:
1.  **Kampanjeaktivitet:** Planlagte prisreduksjoner og markedsføringstiltak skaper kraftige topper i etterspørselen som standard tidsseriemodeller ofte har problemer med å fange opp uten tilleggsdata.
2.  **Prisendringer:** Endringer i utsalgspris påvirker kundenes kjøpsmønster og kan føre til vedvarende endringer i etterspørselsnivået.

### Datagrunnlag i caset
For å analysere disse utfordringene har vi fått tilgang til anonymiserte historiske data som inkluderer:
- Daglig plukket volum (faktisk etterspørsel).
- Kampanjekalender med start- og sluttdatoer.
- Historiske prisdata for de utvalgte produktene.
- Informasjon om eventuelle leveringsavvik eller lagerbrudd.

Gjennom dette caset ønsker vi å teste ut ulike matematiske modeller for å se om vi kan oppnå en høyere prognosepresisjon enn ved bruk av enklere gjennomsnittsmodeller.



# Metode og data

Dette kapittelet beskriver den vitenskapelige tilnærmingen og datagrunnlaget som er benyttet for å besvare problemstillingen.

## Metode

Studien følger et kvantitativt forskningsdesign basert på en case-studie av REMA 1000 Distribusjon Trondheim. Vi benytter statistiske metoder for tidsserieanalyse for å utvikle og evaluere prognosemodeller.

### Forskningsdesign og modellering
Vi har valgt å teste ut ulike tidsseriemodeller, fra enkle modeller som glidende gjennomsnitt og eksponensiell utjevning, til mer komplekse modeller som tar hensyn til trend og sesongvariasjoner. I tillegg inkluderer vi regresjonskomponenter for å evaluere effekten av forklaringsvariabler (kampanje og pris).

### Evaluering av prognosepresisjon
For å måle hvor nøyaktige modellene er, benytter vi følgende standardiserte feilmål:
- **MAE (Mean Absolute Error):** Gir et uttrykk for det gjennomsnittlige absolutte avviket mellom prognose og faktisk etterspørsel i fysiske enheter.
- **MAPE (Mean Absolute Percentage Error):** Angir det prosentvise avviket, noe som gjør det enklere å sammenligne presisjon på tvers av produkter med ulikt volum.
- **Prognosebias:** Vi analyserer også om modellene har en systematisk tendens til å over- eller underestimere etterspørselen.

## Data

Datamaterialet består av historiske transaksjonsdata fra REMA 1000 Distribusjon Trondheim.

### Datainnsamling og behandling
Dataene er hentet ut fra bedriftens ERP-system og dekker en periode på minimum ett år. Prosessen for databehandling inkluderer:
1.  **Datavask:** Identifisering og håndtering av manglende verdier eller åpenbare feilregistreringer.
2.  **Strukturering:** Aggregering av data til dagsnivå og kobling mellom salgsvolum, pris og kampanjedata.
3.  **Anonymisering:** Alle produkt-ID-er er anonymisert for å ivareta bedriftsinterne hensyn.

### Variabler
- **Uavhengige variabler:** Dato, kampanjeindikator (binær), pris.
- **Avhengig variabel:** Daglig utlevert volum (etterspørsel).

# Modellering

I dette kapittelet presenteres de matematiske og statistiske modellene som er valgt for å predikere etterspørselen. Modelleringen er delt inn i to hovedfaser:

1.  **Baseline-modeller:** Bruk av rene tidsseriemodeller (f.eks. Naive, Moving Average, og Exponential Smoothing) for å etablere et sammenligningsgrunnlag.
2.  **Utvidede modeller:** Inkludering av forklaringsvariabler (regresjonsanalyse) for å fange opp effekten av kampanjer og prisendringer.

Detaljerte formler og parameterinnstillinger for de valgte modellene vil bli beskrevet i de påfølgende underavsnittene etter hvert som analysen gjennomføres.

Hvordan skrive bacheloroppgave etter at metodedelen er laget? Jo, du lager en analyse!

Dette er siste bit før du kan presentere selve resultatene av studiene. Du kan velge mellom forskjellige metoder, nemlig:



Kvalitativ metode (intervju eller lignende)

Kvantitativ metode

Dokumentanalyse



Prat gjerne med veilederen din om du er usikker på hvilken metode som er best for akkurat din problemstilling.



# Resultat

Den kanskje viktigste delen når du skal skrive en bacheloroppgave, er resultatdelen. Her beskriver du alle funnene som er gjort i analyser og studier.



Det er viktig at du presenterer resultatene på en klar og tydelig måte – gjerne ved bruk av tabeller og figurer.

Noen viktige punkter:



Dersom dette er et eget kapittel så skal dere her kun presentere resultatene i form av tabeller og/eller figurer.

Tabeller: Oppsummerte resultater

Resultatene er direkte linket til forskningsspørsmålet!

Dersom det ikke er det så er det to alternativer:

Kjør analysene på nytt i henhold til forskningsspørsmålet

Endre forskningsspørsmålet slik at det er samsvar med analysene

NB: En forklarende tekst for hver tabell og hver figur!

Som regel kommer teksten før tabellen/figuren, men noen ganger etter og noen ganger litt tekst først og litt etter tabellen/figuren.

Dere vil synes at det er overflødig med forklarende tekst, men det må gjøres og kun det som dere ser: en objektiv presentasjon.





# Diskusjon

I diskusjonsdelen skal du diskutere de forskjellige funnene du har gjort. Her skal du blant annet inkludere en kritisk metodediskusjon, der du vurderer om metoden din var riktig.

Diskuter hvor pålitelige funnene dine er, om de er generaliserbare og eventuelle svakheter. Forklar også hvorvidt studiet har gitt ny teoretisk innsikt, og om hypoteser kan avkreftes.



Noen viktige punkter:



Her skal resultatene diskuteres

Studenter blander ofte sammen diskusjon og resultater...

Her skal dere kommentere de resultatene som dere har funnet

Er dette som forventet?

Uventede funn? Hvis ja hvordan kan dere forklare dette

Stemmer deres resultater med forskningslitteraturen?

Hvis ikke, hvorfor ikke? Og det kan være bra! 

Hvis ja, kan dere henvise til forskningslitteraturen for å understøtte deres resultater

Resultatene diskuteres opp mot problemstillingen!•Har dere fått svar på forskningsspørsmålet?

Hvilken betydning for næringslivet?

Anbefales som eget punkt i diskusjonen (dette er et viktig punkt i oppgaven)

Hva medfører deres resultater for næringslivet/bedriften?

Hvilke endringer bør bedriften/næringslivet gjøre?

Mulig å generalisere?

Ta med begrensinger/svakheter i oppgaven

Ikke overfokuser på dette punktet men vær ærlige



# Konklusjon



I oppgavens konklusjon oppsummerer du hovedfunn sett i forhold til problemstilling.

Avslutt gjerne med spørsmål til videre forskning, og del personlige refleksjoner du eventuelt måtte ha.



Hva er det viktigste dere har funnet?

Konkludere i henhold til oppgavens problemstilling. Ofte begynner en konklusjon med å gjenta forskningsspørsmålet:

«I denne oppgaven har analysert/redegjort for...».

«Hovedfunnene i oppgaven viser at ....»

«På tross av de svakhetene som oppgaven har er det indikasjoner om at ...»

I konklusjonen blir det ofte litt gjentagelse fra diskusjon/resultat men det er helt greit. Her skal dere dra frem de viktigste funnene og hvilken betydning det har for deres case.





# Bibliografi

# Vedlegg

