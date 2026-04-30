# Prosjektinstrukser: Prognosepresisjon REMA 1000 (LOG650)

Dette dokumentet inneholder de fundamentale føringene for hvordan vi jobber i dette prosjektet. Alle fremtidige handlinger og forslag skal samsvare med disse reglene.

## Prosjektinfo

- **Kurs:** LOG650, Høgskolen i Molde
- **Tema:** Etterspørselsprognoser og prognosenøyaktighet i forsyningskjeden
- **Produkt:** Lasagne Familiepakning, REMA 1000 Distribusjon Trondheim
- **Team:** Line Lyngsnes Johansen og Amanda Arnesen Almaas
- **Problemstilling:** Se `011 fase 1 - proposal/proposal.md`

## Prosjektstruktur

```
G27-workin/
├── 000 templates/           Maler og referanseformat
├── 001 info/                Prosjektinformasjon
├── 002 meetings/            Møtenotater
├── 003 references/          Litteraturdatabase
├── 004 data/                Rå og behandlede datafiler
├── 011 fase 1 - proposal/   Godkjent proposal
├── 012 fase 2 - plan/       Prosjektplan og Python-skript
├── 013 fase 3 - review/     Peer review
├── 014 fase 4 - report/     Rapport (hovedutkast)
└── GEMINI.md                Tilsvarende instrukser for Gemini
```

### Nøkkelfiler

- **Rapport:** `014 fase 4 - report/Prosjektrapport_LOG650_G27.md`
- **Analyseskript:** `012 fase 2 - plan/scenario_analyse.py`
- **Hovedanalyse:** `012 fase 2 - plan/analyse_hoved.py`
- **Datavask:** `012 fase 2 - plan/vask_data.py`
- **Resultater:** `004 data/scenario_resultater.csv`
- **Figurer:** `014 fase 4 - report/figurer/`
- **Status:** `012 fase 2 - plan/status.md`
- **Maler:** `000 templates/Mal prosjekt LOG650 v2.docx`
- **Referansestil:** `000 templates/Referansestiler/APA 7th norsk v1.12.pdf`

## 1. Språk og Format

- **Språk:** All dokumentasjon, kodekommentarer og rapporttekst skal skrives på norsk (inkludert æ, ø og å).
- **Tone i rapporten:** Saklig, konsist og profesjonelt fagspråk (akademisk standard for LOG650). Unngå overforklaringer av grunnleggende begreper med mindre det er strengt nødvendig for analysen.
- **Tone i chat:** Vær pedagogisk, forklar logistikkmessige og metodiske valg underveis, og fungér som mentor/peer-programmerer for å fremme læring.
- **Format:** Alle tekstfiler i UTF-8. Markdown for all løpende dokumentasjon.
- **Typografi (rapporttekst):** Ikke bruk fet skrift inne i løpende tekst. Fet skrift er forbeholdt overskrifter, og kan unntaksvis brukes som etikett i tabeller eller liste-elementer der det er nødvendig for struktur.
- **Setningsoppdeling:** Ikke bruk bindestrek eller tankestrek til å dele opp setninger. Bruk i stedet komma, punktum, kolon eller eksplisitte konjunksjoner (og, men, fordi, slik at, osv.).
- **Referanser:** APA 7. utgave.

## 2. Retningslinjer for Rapportskriving

- **Kontinuerlig skriving:** Rapporten skrives fortløpende parallelt med analyse og databehandling.
- **Kobling til teori:** Metodiske valg skal begrunnes med henvisning til relevant pensum/litteratur med en gang de tas.

## 3. Rapportstruktur

1. **Innledning:** Problemstilling, bakgrunn og avgrensning.
2. **Metode:** Datagrunnlag, modellvalg og evalueringskriterier.
3. **Analyse:** Deskriptiv statistikk, databehandling og resultatpresentasjon.
4. **Diskusjon:** Tolkning av resultater, feilkilder og praktisk relevans.
5. **Konklusjon:** Oppsummering av funn knyttet til problemstillingen.

## 4. Analyse og Modellering

- **Datavask:** Alle steg i datarensingen skal dokumenteres slik at prosessen er etterprøvbar.
- **Modellvalg:** Ingen spesifikke modeller skal forhåndsvelges. Valg av modell skal baseres på datamønstre identifisert i analysen.
- **Evaluering:** Prognosepresisjon skal alltid måles og dokumenteres ved bruk av **MAE** og/eller **MAPE**.
- **Dokumentasjon:** All Python-kode skal ha forklarende kommentarer på norsk.

## 5. Praktiske Arbeidsregler

- **Statusoppdatering:** Filen `012 fase 2 - plan/status.md` skal oppdateres etter hver arbeidsøkt eller ved vesentlig fremdrift.
- **Fakta vs. Antagelser:** Skill tydelig mellom observerte data (fakta) og tolkninger eller antagelser.
- **Kritisk linje:** Aktiviteter på den kritiske linjen (datavask, modellering) skal alltid prioriteres ved tidsnød.

## 6. Tydelig Skille i Innhold

- **Casebeskrivelse:** Beskrivende data om REMA 1000 og produktene. Her legges faktagrunnlaget.
- **Metode:** Beskrivelse av *hvordan* vi analyserer (f.eks. valg av statistiske tester eller modeller).
- **Analyse/Resultater:** Presentasjon av faktiske funn og observasjoner uten omfattende tolkning.

## 7. Figurer og Tabeller

- **Aktiv bruk:** Figurer skal brukes aktivt for å visualisere mønstre, trender og avvik.
- **Figurtekster:** Korte, nøkterne og forklare hva figuren viser.
- **Introduksjon:** Alle tabeller og figurer skal introduseres og forklares i teksten *før* de vises.
- **Plassering:** Tabeller og figurer skal midtstilles i dokumentet.
- **Bildetekst og tabelltekst:** Skal settes i kursiv og med mindre skriftstørrelse enn brødteksten.

## 8. Stegvis Analysearbeid

- **Prosess:** Datavask → Deskriptiv analyse (EDA) → Modellering → Evaluering.
- **Dokumentasjon:** Resultater dokumenteres fortløpende for å unngå tap av innsikt.
- **Forståelse:** Gå aldri rett til modellering uten grundig forståelse av dataenes egenskaper.

## 9. Kvalitet og Etterprøvbarhet

- **Begrunnelse:** Alle metodiske og analytiske valg skal begrunnes faglig.
- **Etterprøvbarhet:** Analysen skal utføres slik at en annen person kan gjenskape resultatene.
- **Rød tråd:** Tydelig sammenheng mellom problemstilling, valgt metode og endelige resultater.

## 10. Samarbeid og Fremdrift

- **Jevn fremdrift:** Arbeidet utføres i et jevnt tempo gjennom hele prosjektperioden.
- **Unngå skippertak:** Ingen kritiske deler skal utsettes til de siste to ukene.

## 11. Spesifikke Krav til Kapittelstruktur (Lærerens føringer)

### Kapittel 4: Casebeskrivelse (Kontekst for analysen)

- **Hensikt:** Gi kontekst ved å beskrive problem, data og modellbehov slik at leseren forstår utfordringene før modellering starter.
- **Kjerneinnhold:**
  - **Beslutningssituasjon:** Hva virksomheten prøver å ta beslutninger om, og hvorfor det er vanskelig uten analyse.
  - **Data:** Type data (tidsserie), periode, representasjon og visualisering (grafer over tid).
  - **Mønstre:** Sesongvariasjon, spredning og enkle tabeller med beskrivende statistikk.
  - **Konsekvenser:** Hva skjer ved manglende analyse (behov for modell).

### Kapittel 5: Metode og data (Gjennomføring og transparens)

- **Hensikt:** Dokumentere hvordan analysen gjennomføres for å sikre transparens og etterprøvbarhet.
- **Kjerneinnhold:**
  - **Metodevalg:** Type analyse og stegvis struktur.
  - **Analyseprosess:** Detaljert beskrivelse (Dataklargjøring → Modellering → Validering → Prognose).
  - **Datakvalitet:** Antagelser, begrensninger og reliabilitet.
  - **Oppdeling:** Begrunnelse for splitting i trening- og testsett.
  - **Oppsummering:** Tabell med tekniske nøkkeltall (min, maks, gjennomsnitt).

### Kapittel 6 & 7: Modellering og Analyse (Prosessfokus)

- **Hensikt:** Beskrive *hvordan* arbeidet er gjort, ikke resultatene.
- **Kjerneinnhold:**
  - **Begrunnelse:** Hvilke modeller som ble vurdert/forkastet (f.eks. Moving Average).
  - **Parametrisering:** Hvordan parameterkombinasjoner (tuning) er testet.
  - **Validering:** Hvordan modellvalget er gjort og validert (residualanalyse).

### Kapittel 8: Resultater (Funn)

- **Hensikt:** Presentere faktiske funn.
- **Kjerneinnhold:** Tabeller med MAE, MAPE og Bias (gjerne segmentert).
