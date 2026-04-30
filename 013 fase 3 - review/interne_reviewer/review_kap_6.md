# Intern review av Prosjektrapport_LOG650_G27 — kap. 6 (Modellering)

**Dato:** 2026-04-30
**Reviewer:** Intern gjennomgang (Claude Code-assistert)
**Rapportfil:** `014 fase 4 - report/Prosjektrapport_LOG650_G27.md` (kap. 6, opprinnelig l. 353–404)
**Formål:** Strukturert kvalitetsvurdering av kap. 6 (Modellering) før peer review (M-05, 2026-05-01).

---

## Sammendrag og status

| Punkt | Status |
|---|---|
| Kap. 6 vurdert | Ja |
| Tiltak besluttet | Alle 15 tiltak (prioritet 1–3) gjennomført 2026-04-30 |
| Strukturendring | Delkap. 6.6 (redundant oppsummering) fjernet 2026-04-30; kap. 6 består nå av 6.1–6.5 |
| Oppfølgingssak | Vedlegg A1 (l. 709) har samme «d=1 konservativt valgt»-formulering som ble rettet i 6.3 — bør rettes ved neste anledning |

**Hovedfunn:** Kapittelet var godt strukturert og faglig dekkende, men hadde tre kritiske svakheter: (1) en faktisk selvmotsigelse om SARIMA-differensiering mellom kap. 6.3 og 7.2/9.6, (2) **manglende in-tekst-sitater** for kjernemodellene (Box & Jenkins, Breiman, Friedman, Hyndman & Athanasopoulos), og (3) **uskarp evalueringsprotokoll** i 6.4 som feilaktig framstilte alle modeller som én-steg-frem-prognoser. Verifikasjon mot `analyse_hoved.py` og `modeller.py` viste at SARIMA og Holt-Winters i realiteten produserer 42-stegs multi-step-prognoser, mens Seasonal Naïve, RF, RF uten lag_1 og GBM bruker faktiske observerte lag — altså en blandet protokoll.

---

## 1. Språkvurdering

**Styrker (i opprinnelig versjon)**
- Konsistent bruk av æ/ø/å og generelt godt akademisk fagspråk.
- God praksis med å oversette engelske fagtermer i parentes første gang de brukes (f.eks. «feature-sett (variabelsett)», «Regelbasert routing (ruting mellom modeller basert på regler)»).
- Fagterminologien (lag, sesongledd, eksogene regressorer, residual, persentil) brukt korrekt og konsekvent.

**Svakheter (rettet i revisjonen)**
- **Apostrof-feil (l. 385):** «SARIMA's differensiering» — engelsk genitiv-apostrof i norsk tekst. Rettet til «SARIMAs».
- **Inkonsistent fagterm (l. 366):** «Holt-Winters (ETS)» likestilte to ulike begreper. Holt-Winters er én konkret klasse innen ETS-rammeverket (Hyndman & Athanasopoulos, 2021), ikke et synonym. Rettet ved å droppe «(ETS)»-parentesen og heller knytte modellen til ETS-familien i Tabell 4.
- **Stikkordpreget setning (l. 357):** «MA (MA5, MA10, MA21) ble forkastet …» — parantesen leste som ren oppramsing. Utvidet til «MA5, MA10 og MA21, det vil si glidende gjennomsnitt over henholdsvis fem, ti og 21 virkedager».
- **Tunge setninger i 6.4 (l. 392):** Blandet beskrivelse, begrunnelse og forbehold i én lang setning. Splittet i to avsnitt med ren beskrivelse av protokoll i ett, og forbeholdet om sammenlignbarhet i et annet.

---

## 2. Innholdsvurdering (per delkapittel)

### 6.1 Arbeidsprosess og modellutvalg
**Observasjon:** MA, Prophet og LSTM begrunnes forkastet; Holt-Winters beholdes som baseline.
**Vurdering:** God i intensjon, men:
- Begrunnelsen «LSTM krever typisk flere tusen observasjoner» (l. 359) var en faglig påstand uten kildehenvisning. Lagt til Hyndman & Athanasopoulos (2021) og Makridakis et al. (2022) i revisjonen.
- ARIMA uten sesongledd (kun den ikke-sesongmessige varianten) var ikke nevnt som vurdert/forkastet. ADF-testen i kap. 7.1 viser stasjonaritet, og leser kunne undres over hvorfor man ikke bare brukte ARMA(p,q). Et eget avsnitt i 6.1 forklarer nå at ARMA(p,q) er et spesialtilfelle av SARIMA-strukturen ($d=0$, $D=0$) og inngår i grid-søket — derfor ikke ført opp som separat kandidat.

### 6.2 Valgte modeller og deres utfyllende roller
**Observasjon:** Åtte modeller listet i nummerert punktliste med utfyllende rolle.
**Vurdering:**
- **Manglende in-tekst-siteringer.** CLAUDE.md §2 krever «metodiske valg skal begrunnes med henvisning til relevant pensum/litteratur **med en gang de tas**». Kapittelet introduserte SARIMA, RF og GBM uten ett eneste in-tekst-sitat, til tross for at Box & Jenkins (1976), Breiman (2001) og Friedman (2001) sto i bibliografien. Sitatene var i kap. 5.1, men skal gjentas der modellen faktisk *begrunnes*. Lagt inn i revisjonen.
- **Modell 5 («RF uten lag_1»):** Beskrevet som «diagnostisk variant» i opprinnelig 6.2, men fungerte i kap. 8 og 9 som *primærkandidat for toppdager*. Den dobbelte rollen er nå eksplisitt flagget i 6.2.
- **Strukturendring:** Punktlisten med åtte nummererte modeller konvertert til **Tabell 4** (modelloversikt) kombinert med løpende prosa som forklarer de fire modellfamiliene.

### 6.3 Datastrukturens påvirkning på modellarkitekturen
**Observasjon:** s=5, ikke-lineæritet og stasjonaritet listet som tre strukturelle trekk.
**Vurdering:**
- **Faglig inkonsistens om d=1.** L. 385 sa: *«SARIMA's differensiering (d=1) er derfor konservativt valgt, ikke strengt nødvendig.»* Men kap. 7.2 (l. 415) viser at d kommer ut av AIC-minimerende grid-søk over $d \in \{0,1\}$, og kap. 9.6 (l. 621) flagger eksplisitt en *risiko for overdifferensiering* med $d=1, D=1$. Tre påstander om samme parameter spriket:
  - 6.3: «konservativt valgt»
  - 7.2: «AIC-resultat»
  - 9.6: «datastyrt, men kan introdusere kunstig MA-struktur»
  Den korrekte framstillingen er at $d=1$ er et *resultat* av grid-søk, ikke et *valg*, og at parsimoni er problematisert i 9.6. Formuleringen i 6.3 er omskrevet til AIC-grid-historien med eksplisitt referanse til 9.6.
- **Strukturendring:** Punktlisten konvertert til løpende fagprosa i tre avsnitt.

### 6.4 Modellspesifikasjon
**Observasjon:** Spesifikasjon av SARIMA, RF, GBM, Holt-Winters og evalueringsprotokoll (én-steg-frem) i punktliste.
**Vurdering:**
- **Uskarp evalueringsprotokoll var en faktisk feil.** L. 392 sa «Alle modeller evalueres som én-steg-frem-prognoser». Verifikasjon mot kode (`analyse_hoved.py` l. 102–110, `modeller.py` l. 173–174) viser at:
  - **SARIMA og Holt-Winters** trenes én gang og produserer **42-stegs multi-step-prognose** for hele testperioden — modellene refittes ikke underveis.
  - **Seasonal Naïve, RF, RF uten lag_1, GBM** bruker faktisk observert serie via `shift` eller lag-features bygd én gang fra hele serien — de facto **én-steg-frem med ekte observert lag**.
  Protokollen er altså blandet, ikke ren én-steg-frem. Den uskarpe formuleringen ble en feilkilde for tolkning av MAE/MAPE i kap. 8 og er rettet i revisjonen.
- **Strukturendring:** Punktlisten konvertert til strukturert prosa i tre avsnitt: (i) statistiske modeller, (ii) maskinlæringsmodeller, (iii) evalueringsprotokoll.

### 6.5 Metodisk refleksjon
**Observasjon:** «Metodisk triangulering» presentert som motivasjon for åtte modeller.
**Vurdering:**
- «Åtte modeller er flere enn minimum nødvendig» (l. 395) var en uklar relativisering uten referansepunkt. Erstattet med forankret begrunnelse: åtte modeller spenner over baselines, parametriske og ikke-parametriske tilnærminger.
- Triangulering var en god akademisk begrunnelse, men koblingen til litteraturen (M5 eller forecast-combinations) manglet. Makridakis et al. (2022) lagt til i revisjonen.
- **Strukturendring:** Punktlisten over modellfamilier konvertert til løpende refleksjonsprosa i to avsnitt.

### 6.6 Oppsummering og videre steg (fjernet 2026-04-30)
**Observasjon:** Bro-avsnitt mot kap. 7.
**Vurdering:** Innholdet var redundant — modellporteføljen er allerede oppsummert i 6.2/Tabell 4, evalueringsprotokollen i 6.4, og kap. 7s eget intro (l. 415) fungerer som naturlig bro. 6.5 lander dessuten med en sterk avslutningssetning. Delkapittelet ble fjernet i sin helhet; ingenting ble flyttet, fordi alt allerede sto et bedre sted.

### Tverrgående: figurer/tabeller
**Observasjon:** Opprinnelig kap. 6 hadde **null figurer og null tabeller** (l. 353–404).
**Vurdering:** CLAUDE.md §7 krever at «figurer skal brukes aktivt for å visualisere mønstre». For et modelleringskapittel var fraværet uvanlig. **Tabell 4** (oversikt over de åtte modellene med kolonner for familie, sesongstruktur, eksogene, lag-features og hyperparametersøk) er lagt til som anker for kap. 7–9.

---

## 3. Identifiserte svakheter (med tiltakskoder)

### Faglige
- **F1:** L. 385 — d=1 omtalt som «konservativt valgt» mens grid-søk i 7.2 og diskusjon i 9.6 forteller en annen historie. Selvmotsigelse mellom kapitler. **Lukket.**
- **F2:** L. 359 — påstand om at «LSTM krever typisk flere tusen observasjoner» manglet kildehenvisning. **Lukket.**
- **F3:** L. 361–378 — manglende in-tekst-sitater for SARIMA (Box & Jenkins, 1976), RF (Breiman, 2001) og GBM (Friedman, 2001) der modellvalget begrunnes. Brudd på CLAUDE.md §2. **Lukket.**
- **F4:** L. 366 — «Holt-Winters (ETS)» likestilte to ulike begreper. **Lukket.**
- **F5:** L. 354 — «208 treningsobservasjoner» kun korrekt for ML-modeller; SARIMA og baselines bruker 218 (jf. kap. 5.5). Misvisende åpningsformulering. **Lukket.**

### Metodiske
- **M1:** L. 392 — uklart om SARIMA/Holt-Winters genererte 42-stegs prognose eller refittet én-stegs rullerende. Direkte konsekvens for sammenlignbarhet mellom modellfamiliene. **Lukket** (verifisert mot kode, blandet protokoll dokumentert i 6.4).
- **M2:** Manglende drøfting av hvorfor ren ARMA(p,q) ikke ble inkludert. **Lukket** (eget avsnitt i 6.1).
- **M3:** Modell 5 (RF uten lag_1) framstilt som «diagnostisk», men brukt som primærmodell på toppdager senere. Den dobbelte rollen var ikke flagget i 6.2. **Lukket.**

### Strukturelle
- **S1:** Tverr-referanser til kap. 7.2 og 9.1 fantes (bra), men kap. 6 refererte ikke til kap. 5.5 (datasplitt) eller kap. 4 (data-EDA), som er forutsetninger for modellvalget. **Lukket** (referanser lagt inn i 6.0 og 6.3).
- **S2:** Ingen oversiktstabell over de åtte modellene som ankerpunkt for kap. 7–9. **Lukket** (Tabell 4 lagt til i 6.2).

### Formidling
- **P1:** Apostrof-feil «SARIMA's» (l. 385). **Lukket.**
- **P2:** L. 357 — MA5/MA10/MA21 forklart som vindusstørrelser. **Lukket.**
- **P3:** L. 392 — lang, sammensatt setning splittet for klarhet. **Lukket.**
- **P4:** L. 395 — «flere enn minimum nødvendig» retorisk uten anker. **Lukket.**

---

## 4. Forbedringsforslag (gjennomført 2026-04-30)

| ID | Forslag | Status |
|---|---|---|
| F1 | Omformuler l. 385 til AIC-grid-historie med ref. til 9.6 | Gjennomført |
| F2 | Tilføy kildehenvisning for LSTM-påstanden (Hyndman & Athanasopoulos, 2021; Makridakis et al., 2022) | Gjennomført |
| F3 | Tilføy in-tekst-sitater i 6.2: SARIMA *(Box & Jenkins, 1976)*, RF *(Breiman, 2001)*, GBM *(Friedman, 2001)*, HW *(Hyndman & Athanasopoulos, 2021)* | Gjennomført |
| F4 | Rett «Holt-Winters (ETS)» → «Holt-Winters» | Gjennomført |
| F5 | Endre «208 treningsobservasjoner» til 218/208 med kontekst | Gjennomført |
| M1 | Presisér evalueringsprotokoll separat for hver modellfamilie etter verifikasjon mot kode | Gjennomført |
| M2 | Begrunn kort hvorfor ren ARMA ikke står som egen kandidat | Gjennomført |
| M3 | Klargjør dobbel rolle for «RF uten lag_1» | Gjennomført |
| S1 | Tverr-referanser til kap. 4 og 5.5 | Gjennomført |
| S2 | Legg til oversiktstabell (Tabell 4) | Gjennomført |
| P1–P4 | Apostrof, MA-forklaring, setningsdeling, retoriske formuleringer | Gjennomført |
| Stil | Konvertér punktlister i 6.2, 6.3, 6.4, 6.5 til løpende fagprosa | Gjennomført |
| Struktur | Fjern redundant 6.6 | Gjennomført |

---

## 5. Samsvar med prosjektplan og status

**Mot proposal (`011 fase 1 - proposal/proposal.md`):** Problemstillingen handler om «tidsserie-baserte prognosemetoder» og effekt av kampanje/pris. Kap. 6 dekker tidsseriedelen godt og inkluderer kampanjeflagg som eksogen variabel. **Pris** er ikke nevnt som forklaringsvariabel i kap. 6, men er drøftet i kap. 5.4 / 9.6 — derfor ikke flagget som mangel her.

**Mot status.md:** Status sa kap. 6 inkluderer «RF-hyperparametere og AIC-tabell». Hyperparametere er nevnt i 6.2 og 6.4, AIC-tabellen ligger i kap. 7.2 / vedlegg A2 — ingen feil, bare en avklaring at status-formuleringen var litt løs. Status oppdatert 2026-04-30 til å reflektere at kap. 6 består av 6.1–6.5 (6.6 fjernet) og at intern review er lukket.

**Mot WBS (ACT-08 i status.md):** Alle leveranser i ACT-08 (åtte modeller, grid-søk, residualanalyse, scenario-sammenligning) er reflektert i kap. 6 (modellbeskrivelse) og kap. 7 (gjennomføring). Ingen avvik.

**Mot CLAUDE.md §11 — kjerneinnhold for kap. 6/7:**
- «Begrunnelse: hvilke modeller som ble vurdert/forkastet» → **dekket** (6.1) inkludert ARMA-begrunnelse.
- «Parametrisering: hvordan parameterkombinasjoner (tuning) er testet» → **dekket** (6.2, 6.4 med detaljer i 7.2).
- «Validering: residualanalyse» → **delvis i 6.4 (lag-håndtering), hovedsakelig i kap. 7.4**. OK gitt skillet mellom kap. 6 (hva) og kap. 7 (hvordan).

---

## 6. Prioritert tiltaksliste (alle gjennomført 2026-04-30)

| Prioritet | Tiltak | Kapittel/linje | Status |
|---|---|---|---|
| 1 | Rett selvmotsigelsen om d=1 (F1) | 6.3, l. 385 | Lukket |
| 1 | Legg til in-tekst-sitater for SARIMA, RF, GBM (F3) | 6.2, l. 369–374 | Lukket |
| 1 | Presiser evalueringsprotokollen for alle modellfamilier (M1) | 6.4, l. 392 | Lukket |
| 1 | Rett «208 treningsobservasjoner» til 218/208 (F5) | 6.1, l. 354 | Lukket |
| 2 | Legg til oversiktstabell (S2) | etter 6.2 | Lukket |
| 2 | Begrunn hvorfor ren ARMA ikke er egen kandidat (M2) | 6.1 | Lukket |
| 2 | Klargjør dobbel rolle for «RF uten lag_1» (M3) | 6.2, l. 373 | Lukket |
| 2 | Kildehenvisning for LSTM-påstanden (F2) | 6.1, l. 359 | Lukket |
| 2 | Rett «Holt-Winters (ETS)» (F4) | 6.2, l. 366 | Lukket |
| 2 | Koble triangulering til Makridakis et al. (2022) | 6.5, l. 395 | Lukket |
| 3 | Apostrof-fiks «SARIMA's» (P1) | 6.3, l. 385 | Lukket |
| 3 | Forklar MA5/MA10/MA21 som vindusstørrelser (P2) | 6.1, l. 357 | Lukket |
| 3 | Splitt lang setning om feature-bygging (P3) | 6.4, l. 392 | Lukket |
| 3 | Tverr-referanser til kap. 4 og 5.5 (S1) | 6.3, l. 380–385 | Lukket |
| 3 | Omformuler «flere enn minimum nødvendig» (P4) | 6.5, l. 395 | Lukket |
| Stil | Konvertér punktlister til løpende prosa | 6.2, 6.3, 6.4, 6.5 | Lukket |
| Struktur | Fjern redundant 6.6 | 6.6 | Lukket |

---

## 7. Samlet vurdering

Kap. 6 var i utgangspunktet godt strukturert og faglig dekkende, med klar inndeling mellom utvalgsprosess (6.1), modellbeskrivelse (6.2), datakobling (6.3), spesifikasjon (6.4) og refleksjon (6.5). Triangulering med åtte modeller er en sterk akademisk tilnærming. Tre forhold trakk likevel ned i opprinnelig versjon: (1) en faktisk selvmotsigelse om SARIMA-differensiering mellom kap. 6.3 og 7.2/9.6, (2) fraværet av in-tekst-sitater for kjernemodellene — referansene sto i bibliografien, men CLAUDE.md §2 krever at de gjentas der modellvalget faktisk gjøres, og (3) en uskarp evalueringsprotokoll i 6.4 som faktisk var feil ved nærmere sjekk mot koden. I tillegg ville en oversiktstabell over de åtte modellene løftet kapittelet vesentlig.

Etter revisjonen 2026-04-30 er alle 15 tiltak lukket, kapittelet er konvertert fra punktliste-tungt til løpende fagprosa i tråd med forfatternes ønske, Tabell 4 er lagt til som anker, og evalueringsprotokollen er verifisert mot `analyse_hoved.py` og `modeller.py`. Kap. 6 består nå av 6.1–6.5 (redundant 6.6 fjernet) og er klart for peer review M-05.

---

## 8. Oppfølgingssaker (utenfor scope for denne reviewen)

- **Vedlegg A1, l. 709:** Inneholder samme «d=1 konservativt valgt»-formulering som ble rettet i 6.3. Må rettes for å unngå motsigelse mellom hovedtekst og vedlegg.

---

*Generert 2026-04-30 som del av intern review-prosess før peer review M-05 (2026-05-01).*
