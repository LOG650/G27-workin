# Prosjektinstrukser: Prognosepresisjon REMA 1000 (LOG650)

Dette dokumentet inneholder de fundamentale føringene for hvordan vi jobber i dette prosjektet. Alle fremtidige handlinger og forslag skal samsvare med disse reglene.

## 1. Språk og Format
- **Språk:** All dokumentasjon, kodekommentarer og rapporttekst skal skrives på norsk (inkludert særnorske tegn som æ, ø og å).
- **Tone i rapporten:** Bruk et saklig, konsist og profesjonelt fagspråk (akademisk standard for LOG650). Unngå overforklaringer av grunnleggende begreper i selve rapportteksten med mindre det er strengt nødvendig for analysen.
- **Tone i chat (Pedagogisk veiledning):** I dialogen med brukeren skal jeg være pedagogisk, forklare logistikkmessige og metodiske valg underveis, og fungere som en mentor/peer-programmerer for å fremme læring.
- **Format:** Alle tekstfiler skal lagres i UTF-8. Markdown benyttes for all løpende dokumentasjon.
- **Krav og Maler:** Følg detaljerte tips og krav i `000 templates\Mal prosjekt LOG650 v2.docx`.
- **Referanser:** Bruk APA 7. utgave som beskrevet i `000 templates\Referansestiler\APA 7th norsk v1.12.pdf`.

## 2. Retningslinjer for Rapportskriving
- **Kontinuerlig skriving:** Rapporten skal skrives fortløpende parallelt med analyse og databehandling. Ikke utsett skriving til slutten av prosjektet.
- **Kobling til teori:** Metodiske valg skal begrunnes med henvisning til relevant pensum/litteratur med en gang de tas.

## 3. Rapportstruktur
Rapporten skal følge denne overordnede strukturen:
1.  **Innledning:** Problemstilling, bakgrunn og avgrensning.
2.  **Metode:** Datagrunnlag, modellvalg og evalueringskriterier.
3.  **Analyse:** Deskriptiv statistikk, databehandling og resultatpresentasjon.
4.  **Diskusjon:** Tolkning av resultater, feilkilder og praktisk relevans.
5.  **Konklusjon:** Oppsummering av funn knyttet til problemstillingen.

## 4. Analyse og Modellering
- **Datavask:** Alle steg i datarensingen skal dokumenteres slik at prosessen er etterprøvbar.
- **Modellvalg:** Ingen spesifikke modeller skal forhåndsvelges. Valg av modell skal baseres på datamønstre identifisert i analysen.
- **Evaluering:** Prognosepresisjon skal alltid måles og dokumenteres ved bruk av **MAE** (Mean Absolute Error) og/eller **MAPE** (Mean Absolute Percentage Error).
- **Dokumentasjon:** All kode (Python/R) skal ha forklarende kommentarer på norsk.

## 5. Praktiske Arbeidsregler
- **Statusoppdatering:** Filen `012 fase 2 - plan/status.md` skal oppdateres etter hver arbeidsøkt eller ved vesentlig fremdrift.
- **Fakta vs. Antagelser:** Skill tydelig mellom observerte data (fakta) og tolkninger eller antagelser i all dokumentasjon.
- **Kritisk linje:** Aktiviteter på den kritiske linjen (datavask, modellering) skal alltid prioriteres ved tidsnød.

## 6. Tydelig Skille i Innhold
- **Casebeskrivelse:** Beskrivende data om REMA 1000 og produktene. Her legges faktagrunnlaget.
- **Metode:** Beskrivelse av *hvordan* vi analyserer (f.eks. valg av statistiske tester eller modeller).
- **Analyse/Resultater:** Presentasjon av faktiske funn og observasjoner uten omfattende tolkning.

## 7. Figurer og Tabeller
- **Aktiv bruk:** Figurer skal brukes aktivt for å visualisere mønstre, trender og avvik i analysen.
- **Figurtekster:** Skal være korte, nøkterne og forklare hva figuren viser.
- **Introduksjon:** Alle tabeller og figurer skal introduseres og forklares i teksten *før* de vises.

## 8. Stegvis Analysearbeid
- **Prosess:** Arbeidet skal følge rekkefølgen: Datavask → Deskriptiv analyse (EDA) → Modellering → Evaluering.
- **Dokumentasjon:** Resultater skal dokumenteres fortløpende for å unngå tap av innsikt underveis.
- **Forståelse:** Gå aldri rett til modellering uten en grundig forståelse av dataenes egenskaper.

## 9. Kvalitet og Etterprøvbarhet
- **Begrunnelse:** Alle metodiske og analytiske valg skal begrunnes faglig.
- **Etterprøvbarhet:** Analysen skal utføres slik at en annen person kan gjenskape resultatene basert på dokumentasjonen.
- **Rød tråd:** Det skal være en tydelig sammenheng mellom problemstilling, valgt metode og de endelige resultatene. Husk alltid problemstillingen spesifisert i `011 fase 1 - proposal\proposal.md`.

## 10. Samarbeid og Fremdrift
- **Arbeidsfordeling:** Oppgaver skal fordeles tydelig slik at begge parter bidrar til kjerneleveransene.
- **Jevn fremdrift:** Arbeidet skal utføres i et jevnt tempo gjennom hele prosjektperioden.
- **Unngå skippertak:** Ingen kritiske deler av rapporten eller analysen skal utsettes til de siste to ukene.

## 11. Spesifikke Krav til Kapittelstruktur (Lærerens føringer)

### Kapittel 4: Casebeskrivelse (Kontekst for analysen)
*   **Hensikt:** Gi kontekst ved å beskrive problem, data og modellbehov slik at leseren forstår utfordringene før modellering starter.
*   **Kjerneinnhold:**
    *   **Beslutningssituasjon:** Hva virksomheten prøver å ta beslutninger om, og hvorfor det er vanskelig uten analyse.
    *   **Data:** Type data (tidsserie), periode, representasjon og visualisering (grafer over tid).
    *   **Mønstre:** Sesongvariasjon, spredning og enkle tabeller med beskrivende statistikk.
    *   **Konsekvenser:** Hva skjer ved manglende analyse (behov for modell).

### Kapittel 5: Metode og data (Gjennomføring og transparens)
*   **Hensikt:** Dokumentere hvordan analysen gjennomføres for å sikre transparens og etterprøvbarhet.
*   **Kjerneinnhold:**
    *   **Metodevalg:** Type analyse og stegvis struktur.
    *   **Analyseprosess:** Detaljert beskrivelse (Dataklargjøring → Modellering → Validering → Prognose).
    *   **Datakvalitet:** Antagelser, begrensninger og reliabilitet.
    *   **Oppdeling:** Begrunnelse for splitting i trening- og testsett.
    *   **Oppsummering:** Tabell med tekniske nøkkeltall (min, maks, gjennomsnitt).

### Kapittel 6 & 7: Modellering og Analyse (Prosessfokus)
*   **Hensikt:** Beskrive *hvordan* arbeidet er gjort, ikke resultatene.
*   **Kjerneinnhold:**
    *   **Begrunnelse:** Hvilke modeller som ble vurdert/forkastet (f.eks. Moving Average).
    *   **Parametrisering:** Hvordan parameterkombinasjoner (tuning) er testet.
    *   **Validering:** Hvordan modellvalget er gjort og validert (residualanalyse).

### Kapittel 8: Resultater (Funn)
*   **Hensikt:** Presentere faktiske funn.
*   **Kjerneinnhold:** Tabeller med MAE, MAPE og Bias (gjerne segmentert).
