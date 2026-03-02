Prosjektstyringsplan
for
REMA 1000 Distribusjon Trondheim

**2026-03-02**

Utarbeidet av:
Line Lyngsnes Johansen og Amanda Arnesen Almaas
Logistikk (nettbasert), Høgskolen i Molde

Prosjektleder:
Amanda Almaas Arnesen

Autorisert av:
[Sponsor]

**Innhold**

# 1. Sammendrag

Dette dokumentet utgjør prosjektstyringsplanen for REMA 1000-prosjektet. Det dokumenterer planbaselines for omfang, fremdrift og risiko, og gir tilleggsinformasjon for å støtte prosjektleder og team i vellykket gjennomføring.

Dette prosjektet støtter målet om å forbedre prognosepresisjon i distribusjonssystemet ved REMA 1000 Distribusjon Trondheim.

Dette er et levende dokument, og skal oppdateres av prosjektleder ved behov gjennom prosjektets løpetid.

## 1.1 Behov
Dette prosjektet svarer på behovet for bedre prognosepresisjon i distribusjonskjeden. Problemstillingen er: I hvilken grad kan tidsserie-baserte prognosemetoder predikere daglig etterspørsel for utvalgte produkter ved REMA 1000 Distribusjon Trondheim, målt ved prognosepresisjon (forecast accuracy)?

## 1.2 Sponsor
[Sponsor] er sponsor for dette prosjektet og myndighet for godkjenning av denne prosjektplanen og eventuelle endringer under gjennomføringen.

## 1.3 Kunde
[Kunde] representerer sluttbrukerne av prosjektet, har deltatt i definisjon av prosjektomfanget og vil være ansvarlig for godkjenning av kravene og aksept av de endelige leveransene.

## 1.4 Forretningscase
Forretningscase-analysen indikerer at prosjektet er begrunnet fordi det vil gi innsikt i faktorer som skaper variasjon i etterspørsel, noe som er av høy interesse for både REMA 1000 og faglærere for senere bruk.

### 1.4.1 Vurdering av alternativer
Prosjektgruppen vurderte to hovedalternativer for oppgaven:
- **Alternativ 1:** Hvilke faktorer påvirker avviket mellom prognose og faktisk etterspørsel (mindre teknisk vanskelig).
- **Alternativ 2:** Hvordan historiske bestillingsdata kan brukes til å predikere ukentlig etterspørsel.

Etter diskusjoner med faglærer (møte 17.02.2026) ble det besluttet å gå for en variant av alternativ 2, men spisset mot **daglig etterspørsel** og inkludering av forklaringsvariabler som kampanjer og pris, da vi skal bygge en modell.

# 2. Omfang

Denne seksjonen beskriver prosjektomfanget, inkludert prosjektmål, forutsetninger, begrensninger, krav og arbeidsnedbrytningsstruktur (WBS) som definerer alle leveranser.

## 2.1 Mål
Prosjektmålet er å undersøke i hvilken grad tidsserie-baserte prognosemetoder kan predikere daglig etterspørsel for utvalgte produkter ved REMA 1000 Distribusjon Trondheim, med særlig fokus på:
- Kampanjebaserte produkter (f.eks. Toro familiepakning lasagne).
- Inkludering av prisingdata, kampanjeindikatorer og reklameeffekter.
- Analyse av både utgående varestrøm til butikk og inngående varestrøm til senteret (lagerkapasitet).

## 2.2 Krav
Prosjektkravene beskriver hva prosjektet må oppfylle for å nå målet. Dette inkluderer tilgang til anonymiserte data, identifikasjon av variasjonsårsaker og evaluering av modellene ved bruk av MAE og MAPE.

En fullstendig kravliste finnes i vedlegg A, sammen med kravets eier og foreløpig kobling (traceability) til leveranser og testtilfeller.

## 2.3 Løsning
Løsningen som skal utvikles er tidsserie-baserte prognosemodeller. Viktige leveranser inkluderer deskriptiv analyse, implementerte modeller og en analyse av prognosebias og effekt av forklaringsvariabler.

## 2.4 Arbeidsnedbrytningsstruktur (WBS)
Dette prosjektets WBS utgjør den formelle baselinen for hele prosjektets omfang.

```text
Prognoseprosjekt
│
├── 1.1 Prosjektgrunnlag
│   ├── 1.1.1 Prosjektoppstart og gruppedannelse
│   ├── 1.1.2 Valgt prosjektområde
│   ├── 1.1.3 Samarbeidsavklaring med REMA
│   ├── 1.1.4 Utarbeidet proposal
│   └── 1.1.5 Godkjent proposal (milepæl)
│
├── 1.2 Prosjektplanlegging
│   ├── 1.2.1 Litteraturgrunnlag
│   ├── 1.2.2 Definert metode og analyseopplegg
│   ├── 1.2.3 Arbeidsnedbrytningsstruktur (WBS)
│   ├── 1.2.4 Gantt-plan
│   └── 1.2.5 Godkjent prosjektplan (milepæl)
│
├── 1.3 Datagrunnlag
│   ├── 1.3.1 Mottatt rådata fra REMA
│   ├── 1.3.2 Datavask og strukturering
│   ├── 1.3.3 Ferdig analyseklar database
│   └── 1.3.4 Dokumentert datasett
│
├── 1.4 Analyse og modellering
│   ├── 1.4.1 Beregning av prognoseavvik
│   ├── 1.4.2 Forecast accuracy-målinger
│   ├── 1.4.3 Identifiserte mønstre og variasjoner
│   ├── 1.4.4 Robusthets- og sensitivitetsanalyse
│   └── 1.4.5 Ferdig analysegjennomføring (milepæl)
│
├── 1.5 Forskningsrapport
│   ├── 1.5.1 Metodekapittel
│   ├── 1.5.2 Resultatkapittel
│   ├── 1.5.3 Diskusjon
│   ├── 1.5.4 Konklusjon
│   ├── 1.5.5 Hovedutkast ferdig (milepæl)
│   └── 1.5.6 Ferdig kvalitetssikret rapport (milepæl)
│
└── 1.6 Presentasjon
    ├── 1.6.1 Utarbeidet presentasjonsmateriell
    └── 1.6.2 Gjennomført muntlig eksamen (milepæl)
```

Mer informasjon finnes også i WBS-ordlisten i vedlegg B, som gir beskrivelse, eier og kostnadskonto for hver leveranse.

## 2.5 Forutsetninger og begrensninger
- **Data:** Vi har fått data fra REMA for perioden 1. mars 2025 til og med 28. februar 2026. Dette er begrenset til ett år på grunn av skifte av ERP-system hos REMA.
- **Omfang:** Analysen utføres på daglig nivå for utvalgte kampanjeprodukter ved distribusjonssenteret.

## 2.6 Omfangsverifikasjon
Alt arbeid skal verifiseres av prosjektteamet og gjennom kvalitetssikring (QA) for å sikre at leveransene oppfyller kravene. Verifikasjoner kan gjennomføres gjennom inspeksjoner, demonstrasjoner, analyser eller tester, avhengig av hva som er hensiktsmessig.

# 3. Fremdrift

Denne seksjonen dokumenterer fremdrifts-baselinen for prosjektet.

## 3.1 Detaljert Fremdriftsplan

Prosjektets tidsplan og fremdrift styres etter det detaljerte Gantt-diagrammet: **'Prosjektplan gant2mars.pdf'**. Nedenfor er en oppsummering av aktivitetene og tidslinjen:

| Fase / Aktivitet | Varighet | Start | Slutt |
| :--- | :--- | :--- | :--- |
| **Fase 1 – Initiering** | **31 dager** | **12.01.26** | **23.02.26** |
| Prosjektoppstart | 6 dager | 12.01.26 | 19.01.26 |
| Utarbeidelse av proposal | 31 dager | 12.01.26 | 23.02.26 |
| *Godkjent proposal (milepæl)* | 0 dager | 23.02.26 | 23.02.26 |
| **Fase 2 – Planlegging** | **10 dager** | **24.02.26** | **09.03.26** |
| Litteraturgjennomgang | 15 dager | 24.02.26 | 16.03.26 |
| Metode og analyseopplegg | 10 dager | 24.02.26 | 09.03.26 |
| Arbeidsnedbrytningsstruktur (WBS) | 10 dager | 24.02.26 | 09.03.26 |
| Gantt-plan | 10 dager | 24.02.26 | 09.03.26 |
| Datainnhenting | 24 dager | 16.02.26 | 19.03.26 |
| *Godkjent prosjektplan (milepæl)* | 0 dager | 09.03.26 | 09.03.26 |
| **Fase 3 – Analyse og modeller** | **35 dager** | **10.03.26** | **27.04.26** |
| Datavask og strukturering | 21 dager | 16.02.26 | 16.03.26 |
| Analyse og modellering | 21 dager | 16.03.26 | 13.04.26 |
| Skriving av diskusjon og metodekapittel | 35 dager | 10.03.26 | 27.04.26 |
| *Ferdig analyse (milepæl)* | 0 dager | 27.04.26 | 27.04.26 |
| Peer to peer-review | 5 dager | 27.04.26 | 01.05.26 |
| **Fase 4 – Rapport og levering** | **47 dager** | **28.04.26** | **01.07.26** |
| Skriving av konklusjon | 4 dager | 11.05.26 | 14.05.26 |
| Utarbeidelse av presentasjon | 10 dager | 18.05.26 | 29.05.26 |
| *Hovedutkast ferdig (milepæl)* | 0 dager | 18.05.26 | 18.05.26 |
| *Ferdig kvalitetssikret rapport (milepæl)* | 0 dager | 31.05.26 | 31.05.26 |
| *Gjennomført muntlig eksamen (milepæl)* | 5 dager | 01.06.26 | 05.06.26 |

## 3.2 Kritisk linje
Den kritiske linjen drives av datavask, modellutvikling og ferdigstilling av forskningsrapporten. Enhver forsinkelse her vil påvirke sluttdatoen for innlevering.

## 3.3 Milepæler
Viktige milepæler inkluderer godkjent prosjektplan, ferdig analyseklar database, ferdig analysegjennomføring og endelig rapport.

# 4. Risiko

Denne seksjonen beskriver risikostyringsprosessen og gir en kopi av risikoregisteret som baseline.

## 4.1 Prosess for risikostyring
Risikoer ble identifisert gjennom sjekklister og konsultasjon med veiledere. Risikoregisteret skal gjennomgås ved slutten av hver mandagsmøte. Tiltak skal iverksettes proaktivt. Sannsynlighet og tidsestimater for risikoene ble utviklet av prosjektgruppen basert på tidligere erfaring.

## 4.2 Risikoregister
[Risikoregisteret viser kjente risikoer som datakvalitet, tidsnød og tekniske utfordringer med modellering.] Det fullstendige risikoregisteret finnes også i vedlagt dokument.

# 5. Saker
Nødvendige ressurser og fremdrift for å håndtere alle forventede prosjektsaker er bygget inn i baselineplanen. Kjente problemer inkluderer endelig avklaring av variabler med REMA-kontakt.

# 6. Interessenter
Denne seksjonen beskriver de viktigste interessentene for prosjektet. De viktigste interessentene inkluderer:
- Studentene (Line og Amanda)
- Faglærere og hjelpelærer ved Høgskolen i Molde
- Kontaktperson ved REMA 1000 Distribusjon Trondheim

# 7. Ressurser

## 7.1 Prosjektteam
Prosjektet gjennomføres av to studenter i tett samarbeid.

| Navn | Rolle | Ansvar |
| --- | --- | --- |
| Amanda Almaas Arnesen | Prosjektleder / Student | Overordnet ansvar, koordinering og planlegging. |
| Line Lyngsnes Johansen | Student | Analyse, modellering og rapportskriving. |
| Faglærere (2 stk) | Veiledere | Faglig støtte og vurdering. |
| Hjelpelærer | Assistent | Teknisk støtte. |
| Kontakt REMA 1000 | Ekstern kontakt | Tilgang til data og domenekunnskap. |

## 7.2 Ressursbelastning
Studentene er allokert på fulltid til prosjektet. Samarbeidet foregår kontinuerlig gjennom uka.

# 8. Kommunikasjon

Denne seksjonen beskriver planlagt formell kommunikasjon etter hvert som prosjektet gjennomføres.

## 8.1 Møter mellom studentene
- **Ukentlige møter:** Hver mandag kl. 09:00 for planlegging og status.
- **Tett samarbeid:** Løpende kontakt gjennom hele uka.
- **Månedlig gjennomgang:** Gjennomgang av hele prosjektet for å vurdere status mot frister.

## 8.2 Møter med veiledere og REMA
- Veiledningsmøter skjer etter behov.
- Faglærer har uttrykt interesse for å delta i møte med sjefen hos REMA for å spisse problemstillingen ytterligere.

## 8.3 Møter i endringskontrollstyret
Formålet med møter i endringskontrollstyret (CCB) er å gjennomgå alle endringer i omfang, fremdriftsplan eller tidligere baselinede og godkjente leveranser for å sikre at alle mulige konsekvenser identifiseres.

# 9. Kvalitet

Denne seksjonen beskriver tilnærmingen til kvalitetsstyring gjennom hele prosjektet.

## 9.1 Kvalitetsprinsipper
Kvalitet bygges inn i arbeidet gjennom kontinuerlig fagfellevurdering mellom studentene og regelmessig tilbakemelding fra veiledere. De fire kvalitetsprinsippene (Planlegging, Gevinst, Kontinuerlig forbedring, Egnet for formålet) ligger til grunn.

## 9.2 Fagfellevurderinger
Fagfellevurderinger er en av de mest effektive prosessene for å sikre at leveranser har høy kvalitet. Det skal brukes både uformelle og formelle fagfellevurderinger.

### 9.2.1 Uformelle fagfellevurderinger
Eier av hver leveranse skal sikre at leveransen har vært gjennom en fagfellevurdering før den ferdigstilles. En fagfellevurdering bør inkludere to eller tre fagfeller.

### 9.2.2 Formelle fagfellevurderinger
Formelle fagfellevurderinger er påkrevd for alle leveranser som har juridiske eller akademiske krav. QA-organisasjonen skal administrere prosessen.

## 9.3 Brukerreviews
Brukerreviews er inkludert for å sikre at prosjektresultatet er egnet for formålet. Kunden representeres av REMA-kontakten og faglærere.

# 10. Anskaffelser
Prosjektet krever for øyeblikket ingen eksterne anskaffelser utover eksisterende programvare (Python/R, Excel) og data fra REMA.

# 11. Endringskontrollprosess

Når denne prosjektplanen er godkjent, skal alle endringer i omfang eller fremdriftsplan gå gjennom den formelle endringskontrollprosessen. En endring må dokumenteres formelt i et endringsforespørselsskjema (vedlegg F).

# Vedlegg

## Vedlegg A - Kravliste
Dette vedlegget gir en oversikt over prosjektkravene, inkludert unik identifikator, type, eier og sporbarhet til leveranser.

## Vedlegg B - WBS-ordliste
Dette vedlegget gir en WBS-ordliste med mer informasjon om leveransene dokumentert i seksjon 2.4.

## Vedlegg C - Format for saksliste
Dette vedlegget gir malen for prosjektets saksliste som brukes til koordinering av det ukentlige saksstatusmøtet.

## Vedlegg D - Format for månedlig prosjektrapport
Dette vedlegget gir formatet for én-sides rapporten som skal brukes i de månedlige prosjektgjennomgangene.

## Vedlegg E - Mal for brukerreview
Dette vedlegget gir malen som brukes i brukerreview-prosessen.

## Vedlegg F - Skjema for endringsforespørsel
Dette vedlegget gir det formelle skjemaet som brukes for endringsforespørsler.
