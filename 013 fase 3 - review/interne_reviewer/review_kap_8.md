# Intern review av Prosjektrapport_LOG650_G27 — kap. 8 (Resultater)

**Dato:** 2026-04-30
**Reviewer:** Intern gjennomgang (Claude Code-assistert)
**Rapportfil:** `014 fase 4 - report/Prosjektrapport_LOG650_G27.md` (kap. 8, l. 455–572)
**Formål:** Strukturert kvalitetsvurdering av kap. 8 (Resultater) før peer review (M-05, 2026-05-01).

---

## Sammendrag og status

| Punkt | Status |
|---|---|
| Kap. 8 vurdert | Ja |
| Tiltak besluttet | Alle prioritet 1, 2 og 3-tiltak lukket 2026-04-30. Som del av M2 ble en ny Tabell 4b lagt til (SARIMA segmentert MAE for Scenario 1 vs Scenario 2), basert på verdier hentet fra `004 data/scenario_sammendrag.csv`. |
| Forholdet til kap. 7-revisjon | Konsistent: kap. 8 bruker nå P90-terskel 70,6 med eksplisitt kryssreferanse til kap. 7.3, og Ljung-Box-introduksjonen i 8.4 viser til kap. 7.4. |

**Hovedfunn:** Kapittelet oppfyller CLAUDE.md §11-kravene fullt ut (MAE/MAPE/Bias presentert globalt og segmentert, fire klart strukturerte delkapitler 8.1–8.4) og gir en pedagogisk velstrukturert presentasjon av sentrale funn. Tre forhold trekker likevel kvaliteten ned: (1) **fet skrift inne i løpende tekst** i 8.3 og 8.4 bryter med CLAUDE.md §1 (samme typografi-regel som ble lukket i kap. 6 og 7), (2) **hybridmodellene** introduseres først ved Tabell 3 uten en kort definisjon eller kryssreferanse til kap. 9.4 der de faktisk beskrives, og (3) **Tabell 2-tolkningen** rapporterer endringer i prosent men mangler konkrete MAE-par i stk, hvilket gjør størrelsen av forbedringene lite intuitiv. I tillegg refereres Scenario 1-segmentert SARIMA-MAE (45,97) i teksten l. 535, men er ikke synlig i Tabell 4, som kun viser Scenario 2.

---

## 1. Språkvurdering

**Styrker**
- Konsistent bruk av æ/ø/å og generelt godt akademisk fagspråk.
- Fem ulike feilmål (MAE, MAPE, sMAPE, WAPE, Bias) presenteres ryddig i Tabell 3 med tydelig norsk tallformat (komma som desimaltegn, hardt mellomrom som tusenskille).
- Metodisk innsiktsfull tolkning av |Bias|=MAE-observasjonen (l. 540) som kobler matematisk struktur til modellatferd.
- God data-provenance i kap. 8s intro (l. 458): leseren får vite hvilke skript som genererer hvilke tabeller.

**Svakheter**
- **Fet skrift inni løpende tekst (l. 540, 570):** «**Holt-Winters og SARIMA har |Bias| = MAE på toppdager**» og to forekomster i l. 570 («**tidsseriemodellene … har signifikant autokorrelasjon**», «**RF, RF uten lag_1 og hybridene har residualer som er statistisk uavhengige**») bryter med CLAUDE.md §1 (typografi-regelen innført 2026-04-30). Samme type rettelse som ble gjort i kap. 6 og 7.
- **Engelsk fagterm uten norsk parafrase (l. 543, 558):** «(10 lags)» brukes uten norsk parafrase i kap. 8, til tross for at kap. 7.4 nå skriver «ti etterslep (lags)». Konsistens på tvers av kapitler ville styrket leseopplevelsen.
- **Plassivt uttrykk (l. 543):** «ble Ljung-Box Q-test (10 lags) og ACF-plott evaluert» kan strammes til aktiv form: «Ljung-Box Q-testen (10 lags) og ACF-plott evaluerer …», men passiv er akseptabel i et resultatkapittel.
- **«Et slående observasjon» (l. 540):** kongruensfeil — «en slående observasjon» er korrekt (felleskjønn).

---

## 2. Innholdsvurdering (per delkapittel)

### 8.1 Sammenligning av Scenario 1 og Scenario 2 (l. 460–486)

**Observasjon:** Tabell 2 viser MAE for seks modeller × 2 scenarier med endringskolonne i prosent. Figur 5 visualiserer faktisk etterspørsel mot RF Scenario 1 (rødt), RF uten lag_1 Scenario 2 (oransje) og Hybrid terskelbasert (grønn).

**Vurdering:**
- **Tolkningen av Tabell 2 (l. 478) gir kun prosent.** «Marginal global forbedring på SARIMA (−0,4 %) og moderat forbedring på RF uten lag_1 (−5,5 %)» kan tolkes lett feil hvis leseren ikke regner ut absoluttverdiene. SARIMA går fra 174,02 til 173,30 stk (under 1 stk per dag i forskjell), mens RF uten lag_1 går fra 178,99 til 169,11 stk (≈ 10 stk i absolutt forbedring på et nivå rundt 175). Leseren bør få begge tall.
- **Skillet mellom «marginal» og «moderat»** er ikke definert. Per faglig konvensjon vil −5,5 % gjerne kalles «moderat» og −0,4 % «marginal», men en kort fotnotering eller terskel ville vært ryddigere.
- **Figur 5-fargekoding** introduseres først i bildeteksten (l. 484), ikke i den løpende teksten l. 478 før figuren vises. Per CLAUDE.md §7 («introdusert og forklart … *før* de vises») bør fargekodingen gjentas i prosa: «Figur 5 viser faktisk etterspørsel (sort), RF Scenario 1 (rødt), RF uten lag_1 Scenario 2 (oransje) og Hybrid terskelbasert (grønn) over testperioden.»
- **Cross-reference til kap. 8.3 er allerede til stede** («Den segmenterte analysen (kap. 8.3) viser at dette skyldes …»), hvilket er bra.

### 8.2 Global modellytelse (l. 488–508)

**Observasjon:** Tabell 3 sammenfatter åtte modeller × fem feilmål for Scenario 2. Hybridmodellene (kampanje og terskel) inntreffer for første gang her.

**Vurdering:**
- **Hybridmodellene introduseres uten definisjon.** L. 489 sier «Hybridmodellene er kun definert i Scenario 2», men ikke *hva* hybridene gjør. «Hybrid (kampanje)» og «Hybrid (terskel)» dukker opp i Tabell 3 uten å være forankret i kap. 6 eller 7. En setning som «Hybrid (kampanje) bruker SARIMA på dager uten kampanje og RF uten lag_1 på kampanjedager. Hybrid (terskel) velger mellom SARIMA og RF uten lag_1 basert på P90-terskelen 70,6 stk (definert i detalj i kap. 9.4).» ville plassert dem kontekstuelt før tallene presenteres.
- **MAPE-problematikken (l. 508) flagges riktig** men kommer *etter* tabellen. En kort note i tabellbildeteksten («*MAPE-verdier er ekstreme på lavvolum-dager; sMAPE og WAPE er mer robuste*») ville hjulpet leseren å unngå feiltolking allerede ved første blikk på tabellen. Hyndman & Koehler (2006), som er sitert i kap. 5.3, kunne henvises her for å forankre MAPE-svakheten faglig.
- **«RF uten lag_1»** med fet skrift er korrekt brukt som etikett i tabell (CLAUDE.md §1: «kan unntaksvis brukes som etikett i tabeller»). Samme gjelder «Hybrid (terskel)» i l. 502.

### 8.3 Segmentert resultatanalyse (l. 510–540)

**Observasjon:** Tabell 4 viser segmentert MAE og Bias for seks modeller × to segmenter (normale dager n=27, toppdager n=15). Tre tolkningsavsnitt følger.

**Vurdering:**
- **Tabell 4 viser kun Scenario 2-tall, men teksten l. 535 referer til Scenario 1-tall (45,97 → 29,40 = −36 %).** Forbedringen for SARIMA på normale dager mellom Scenario 1 og 2 er en sentral finding, men kun Scenario 2-MAE (29,4) er synlig i Tabell 4. Leseren kan ikke verifisere 45,97 mot tabellen. Forslag: enten utvide Tabell 4 med en Scenario 1-kolonne for normale dager og toppdager, eller plassere SARIMA-forbedringen som egen mini-tabell.
- **Segmenteringsterskelen (P90 = 70,6 stk)** er kort innført i l. 511 men ikke forklart som «90.-persentilen av treningssettet (218 dager)» her. Dette ble lukket i kap. 7.3 etter kap. 7-review (M5/M1), og 8.3 burde henvise til 7.3: «(jf. kap. 7.3)».
- **Punktliste l. 534–536 («På normale dager … På toppdager …»)** bruker fet skrift som etikett, hvilket er akseptabelt, men kunne med fordel konverteres til prosa for konsistens med stilen som ble valgt for revidert kap. 6 (P4 i kap. 7-review).
- **|Bias|=MAE-observasjonen (l. 540)** er pedagogisk sterk og viser metodisk dybde. Selve formuleringen er imidlertid noe oppskrudd («Et slående observasjon», kongruensfeil) og bruker fet skrift inne i løpende tekst (P1).
- **Seiringer et al. (2024)** er korrekt sitert i l. 538 for sammenhengen mellom bias-skjevhet og sikkerhetslagerdimensjonering. God forankring.

### 8.4 Residualdiagnostikk og modellvaliditet (l. 542–572)

**Observasjon:** Tabell 5 viser Ljung-Box Q-test for åtte modeller på testresidualer (10 lags). Figur 6 viser ACF-plott for fem sentrale modeller. Tolkning følger i l. 570–572.

**Vurdering:**
- **Tabell 5 dekker åtte modeller, mens Figur 6 viser kun fem (Naive, HW, SARIMA, RF uten lag_1, Hybrid terskel).** Det er rimelig å begrense ACF-plottet av plasshensyn, men en kort begrunnelse for utvalget («Vi viser de fem modellene som tydeligst illustrerer skillet …») ville hjulpet leseren.
- **Hybrid (terskel) i Figur 6 vs Tabell 5:** Både Tabell 5 og Figur 6 viser at terskelhybriden har uavhengige residualer (p = 0,223). Konsistens mellom statistisk test og visuell ACF er derfor godt dokumentert.
- **Ljung-Box-test refereres uten in-tekst-sitat.** Kap. 7.4 har nå sitatet (Ljung & Box, 1978) etter kap. 7-review (F2 lukket), så leseren kan finne det der. Strengt tatt kunne sitatet gjentas i 8.4 når testen *anvendes* og *resultatene rapporteres*, men dette er på grensen — gitt at testen er etablert i 7.4, er det forsvarlig å la 8.4 stå uten sitat. Hyndman og Athanasopoulos (2021), som ble lagt til i 7.4 (F5), kunne med fordel også henvises i 8.4 ved å skrive «(jf. residualdiagnostikkprotokollen i kap. 7.4)».
- **«Tidsseriemodellene … har signifikant autokorrelasjon» (l. 570)** — denne formuleringen er korrekt, men fet skrift inne i løpende tekst bryter med CLAUDE.md §1.
- **Oppsummeringsavsnittet (l. 572)** er en god overgang til kap. 9 og innfører motivasjonen for hybridroutingen.

### Tverrgående: figurer og tabeller

**Observasjon:** Kap. 8 inneholder fire tabeller (2, 3, 4, 5) og to figurer (5, 6).

**Vurdering:**
- Tabellene er konsistent nummerert og introdusert i tekst før visning. CLAUDE.md §7 oppfylt.
- Figurene er korrekt midtstilt med kursiv bildetekst i mindre skriftstørrelse (CLAUDE.md §7).
- Bildeteksten til Figur 6 (l. 566) forklarer *hva* som plottes, men ikke *hvorfor*. En setning som «Residualer innenfor blått felt indikerer hvit støy (modellen har ekstrahert all systematisk informasjon).» ville styrket pedagogikken.
- **Konsistens med status.md:** status.md l. 101 nevner «Figur 4», men rapporten viser «Figur 5». Dette skyldes drift i figurnummerering underveis og bør oppdateres i status.md ved sluttgjennomgang (allerede notert i kap. 6/7-reviews).

---

## 3. Identifiserte svakheter (med tiltakskoder)

### Faglige
- **F1:** L. 489 — Hybridmodellene innføres ved Tabell 3 uten definisjon eller kryssreferanse til kap. 9.4 der de beskrives. **Status: lukket 2026-04-30.**
- **F2:** L. 543 — Tilføy «(jf. kap. 7.4 for testbeskrivelse og sitering av Ljung & Box, 1978)» eller la 8.4 stå med implisitt forankring. **Status: lukket 2026-04-30** — eksplisitt kryssreferanse «(jf. kap. 7.4)» tilføyd ved Ljung-Box-introduksjonen i 8.4.

### Metodiske
- **M1:** L. 478 — Tolking av Tabell 2 gir kun endring i prosent. Konkrete MAE-par i stk mangler, hvilket gjør forbedringsstørrelsen lite intuitiv. **Status: lukket 2026-04-30.**
- **M2:** L. 535 — Tabell 4 viser kun Scenario 2-tall, men teksten refererer til Scenario 1-MAE (45,97) for SARIMA på normale dager. Leseren kan ikke verifisere tallet i tabellen. **Status: lukket 2026-04-30** — ny Tabell 4b lagt til etter Tabell 4 med SARIMA segmentert MAE for Scenario 1 (46,0 normale / 404,5 toppdager) vs Scenario 2 (29,4 / 432,3). Verdiene er hentet fra `004 data/scenario_sammendrag.csv`. Funnet at Scenario 2 forverrer SARIMA på toppdager (+7 %) er nå eksplisitt nevnt i prosa-avsnittet.
- **M3:** L. 511 — Segmenteringsterskelen (P90 = 70,6 stk) er ikke krysshenvist til kap. 7.3 der den nå er definert som persentil på det fulle treningssettet (218 dager). **Status: lukket 2026-04-30.**
- **M4:** L. 508 — MAPE-svakheten flagges først *etter* Tabell 3. En kort note i tabellbildeteksten (f.eks. «*MAPE-verdier er ekstreme på lavvolum-dager*») ville hjulpet leseren ved første blikk på tabellen. **Status: lukket 2026-04-30.**

### Strukturelle
- **S1:** L. 478–480 — Figur 5-fargekoding introduseres ikke i prosa før figuren vises. Per CLAUDE.md §7 bør fargene navngis i teksten l. 478. **Status: lukket 2026-04-30.**
- **S2:** L. 562–567 — Bildetekst til Figur 6 forklarer *hva* (ACF-plott, blått konfidensintervall), men ikke *hvorfor* (innenfor felt = hvit støy). **Status: lukket 2026-04-30.**

### Formidling
- **P1:** L. 540, 570 (to forekomster i 570) — Fet skrift inne i løpende tekst bryter med CLAUDE.md §1. Samme type rettelse som ble gjort i kap. 6 og 7. **Status: lukket 2026-04-30.**
- **P2:** L. 540 — «Et slående observasjon» kongruensfeil. Bør være «en slående observasjon». **Status: lukket 2026-04-30.**
- **P3:** L. 543, 558 — Engelsk «lags» uten norsk parafrase, til tross for at kap. 7.4 nå bruker «ti etterslep (lags)». **Status: lukket 2026-04-30.**
- **P4:** L. 534–536 — Punktliste («På normale dager … På toppdager …») kan vurderes konvertert til prosa for konsistens med revidert kap. 6 og kap. 7. **Status: lukket 2026-04-30.**

---

## 4. Forbedringsforslag

| ID | Forslag |
|---|---|
| F1 | I 8.2, før Tabell 3: «Tabell 3 inkluderer to hybridmodeller (definert i detalj i kap. 9.4): Hybrid (kampanje) bruker SARIMA på dager uten kampanje og RF uten lag_1 på kampanjedager, mens Hybrid (terskel) velger mellom SARIMA (≤ 70,6 stk) og RF uten lag_1 (> 70,6 stk) basert på P90-terskelen.» |
| F2 | Vurder å føye «(jf. kap. 7.4)» til l. 543 for tydelig metodisk forankring. Alternativt la 8.4 stå uendret, gitt at testen er sitert i 7.4. |
| M1 | I 8.1 l. 478, erstatt prosentrapporteringen med konkret MAE-par: «SARIMA reduseres med under 1 stk per dag (174,0 → 173,3 stk, −0,4 %), mens RF uten lag_1 reduseres med ≈ 10 stk per dag (179,0 → 169,1 stk, −5,5 %).» |
| M2 | Utvid Tabell 4 med en Scenario 1-kolonne for normale dager og toppdager, eller plasser SARIMA Scenario 1 vs 2-segmentert som egen mini-tabell etter Tabell 4. |
| M3 | I 8.3 l. 511, tilføy: «Terskelen 70,6 stk er 90.-persentilen av treningssettet (218 virkedager), jf. kap. 7.3.» |
| M4 | Legg til note i Tabell 3-bildetekst: «*MAPE-verdier er gjennomgående svært høye fordi små nevnere på lavvolum-dager forsterker prosentfeilen; sMAPE og WAPE er mer robuste tolkningsmål (Hyndman & Koehler, 2006).*» |
| S1 | I 8.1 l. 478, før referansen til Figur 5: «Figur 5 viser faktisk etterspørsel (sort) sammenlignet med RF Scenario 1 (rødt), RF uten lag_1 Scenario 2 (oransje) og Hybrid terskelbasert (grønn) over testperioden.» |
| S2 | Endre Figur 6-bildetekst til: «*ACF-plott av residualene for fem sentrale modeller (Seasonal Naive, Holt-Winters, SARIMA, RF uten lag_1 og Hybrid terskel). Blått felt indikerer konfidensintervall for hvit støy. Residualer innenfor feltet betyr at modellen har ekstrahert all systematisk informasjon.*» |
| P1 | Fjern fet skrift i l. 540 («**Holt-Winters og SARIMA har |Bias| = MAE på toppdager**») og l. 570 (to forekomster). |
| P2 | Endre l. 540 fra «Et slående observasjon» til «En slående observasjon». |
| P3 | I 8.4 l. 543 og 558, endre «(10 lags)» til «(10 etterslep / lags)» ved første bruk. |
| P4 | Vurder å konvertere punktlisten i 8.3 l. 534–536 til prosa, f.eks.: «På normale dager er SARIMA best (MAE 29,4); kampanjeinformasjon reduserer feilen fra 45,97 (Scenario 1) til 29,40 (Scenario 2), en forbedring på 36 %. På toppdager er RF uten lag_1 best (MAE 290,2), tett fulgt av Hybrid (terskel) (305,5) som har lavere absolutt bias.» |

---

## 5. Samsvar med prosjektplan og status

**Mot proposal (`011 fase 1 - proposal/proposal.md`):** Problemstillingens delproblem 3 («i hvilken grad kampanjeaktivitet begrenser modellenes presisjon») besvares eksplisitt i 8.1 og videreføres i 8.3. Ingen avvik mot proposal.

**Mot status.md:** Status av 2026-04-30 sier «| 8 Resultater | Ferdig | 8.1 (Scenario 1 vs 2) og 8.2 (åtte modeller globalt) |». Reviewen viser at 8.3 og 8.4 også er på plass i tillegg til det som er angitt i status.md, hvilket er positivt. Status bør beholdes som «Ferdig», med en review-merknad om gjenstående tiltak (P1-rettinger anbefales før peer review M-05).

**Mot WBS / kritisk linje:** Kap. 8 er den primære leveransen for ACT-08/ACT-09 (resultatpresentasjon). Alle planlagte feilmål (MAE, MAPE, sMAPE, WAPE, Bias) og to segmenter (normale/toppdager) er dekket. Ingen avvik.

**Mot CLAUDE.md §11 — kjerneinnhold for kap. 8:**

| Krav i CLAUDE.md §11 | Dekket | Hvor | Kommentar |
|---|---|---|---|
| Hensikt: Presentere faktiske funn | Ja | 8.1–8.4 | Fire klare funn presentert: scenario-effekt, global ytelse, segmentert vinnerstruktur, residualvalidering |
| Tabeller med MAE | Ja | Tab. 2 (8.1), Tab. 3 (8.2), Tab. 4 (8.3) | MAE konsekvent vist; Scenario-sammenligning i Tab. 2 |
| Tabeller med MAPE | Ja | Tab. 3 (8.2) | Vist globalt; tolket som problematisk (MAPE-svakhet flagget l. 508) |
| Tabeller med Bias | Ja | Tab. 3 (8.2), Tab. 4 (8.3) | Globalt og segmentert; metodisk tolket (|Bias|=MAE-observasjon) |
| Gjerne segmentert | Ja | Tab. 4 (8.3) | Normale (n=27) vs toppdager (n=15) tydelig fordelt |

**Mot CLAUDE.md §1 (typografi-regelen 2026-04-30):**
- Fet skrift inne i løpende tekst: brudd i 8.3 l. 540 og 8.4 l. 570 (P1).
- Tankestrek til setningsoppdeling: ikke observert i kap. 8 (godt).

**Mot CLAUDE.md §7:**
- Tabeller og figurer introduseres før visning: hovedsakelig OK; Figur 5-fargekoding kunne vært tydeligere i prosa (S1).
- Aktiv bruk av figurer: Figur 5 og 6 brukes godt; ingen uvist relevant figur (i motsetning til kap. 7s mangelfulle ACF-plott av treningsserien).
- Bildetekst i kursiv og mindre skrift: oppfylt.

**Mot CLAUDE.md §2 (kobling til teori):**
- Seiringer et al. (2024) sitert i 8.3 l. 538 — god forankring.
- Hyndman & Koehler (2006) ikke sitert ved MAPE-tolking i 8.2 l. 508, men kunne tilføyes i tabellbildeteksten (M4).
- Trapero et al. (2015) er ikke sitert i 8.1 ved Scenario-tolking, men siden tolkningen er drøftet i kap. 9.2 er dette akseptabelt — kap. 8 er resultatpresentasjon, og siteringen er forsvarlig plassert i diskusjonen.

---

## 6. Prioritert tiltaksliste

| Prioritet | Tiltak | Kapittel/linje | Estimert innsats |
|---|---|---|---|
| 1 | Definer hybridmodellene før Tabell 3 (F1) | 8.2, før l. 489 | 5 min |
| 1 | Konkretiser Tabell 2-tolking med MAE-par i stk (M1) | 8.1, l. 478 | 5 min |
| 1 | Fjern fet skrift inne i løpende tekst (P1) | 8.3 l. 540, 8.4 l. 570 | 2 min |
| 1 | Rett kongruensfeil «Et slående» → «En slående» (P2) | 8.3, l. 540 | 1 min |
| 2 | Navngi farger i Figur 5 i prosa før figuren vises (S1) | 8.1, l. 478 | 3 min |
| 2 | Vis Scenario 1-segmentert SARIMA i tabell eller mini-tabell (M2) | 8.3, Tab. 4 | 10–15 min |
| 2 | Krysshenvis P90-terskel til kap. 7.3 (M3) | 8.3, l. 511 | 2 min |
| 2 | Tilføy MAPE-note i Tabell 3-bildetekst (M4) | 8.2, Tab. 3 | 3 min |
| 3 | Pedagogisk note i Figur 6-bildetekst (S2) | 8.4, l. 566 | 2 min |
| 3 | Norsk parafrase «(10 etterslep / lags)» (P3) | 8.4, l. 543, 558 | 1 min |
| 3 | Vurder Ljung-Box-kryssreferanse til kap. 7.4 (F2) | 8.4, l. 543 | 1 min |
| 3 | Vurder konvertering av punktliste i 8.3 til prosa (P4) | 8.3, l. 534–536 | 5 min |

**Sum estimert innsats:**
- Prioritet 1: ca. 15 min (kritisk for innlevering — typografi og hybridkontekst).
- Prioritet 2: ca. 25 min (viktig for kvalitet — pedagogikk og kryssreferanser).
- Prioritet 3: ca. 10 min (ønskelig polering).
- **Totalt: ca. 50 min** for full lukking.

---

## 7. Samlet vurdering

Kap. 8 er strukturelt og innholdsmessig solid: fire delkapitler (8.1–8.4) presenterer scenario-effekt, global ytelse, segmentert vinnerstruktur og residualvalidering i en logisk rekkefølge som matcher CLAUDE.md §11-kravene fullt ut. Fire tabeller og to figurer er konsistent introdusert, midtstilt og forklart. Den metodiske refleksjonen rundt |Bias|=MAE på toppdager (l. 540) og koblingen til sikkerhetslager (l. 538, Seiringer et al., 2024) viser faglig dybde og setter kapittelet over et rent deskriptivt nivå.

Tre forhold trekker kvaliteten ned. For det første **fet skrift inne i løpende tekst** i 8.3 og 8.4 (tre forekomster) bryter med typografi-regelen som ble lukket i både kap. 6 og 7 — dette er en triviell men nødvendig opprettelse for konsistens. For det andre **introduseres hybridmodellene** ved Tabell 3 uten definisjon eller kryssreferanse til kap. 9.4 der de faktisk beskrives, hvilket gjør dem opake for en leser som leser kapitlene i rekkefølge. For det tredje **rapporterer Tabell 2-tolkningen** kun prosent, ikke konkrete MAE-par i stk; for SARIMA betyr det at en endring på under 1 stk per dag fremstilles som «marginal» uten at leseren kan vurdere absoluttverdien direkte. I tillegg refereres Scenario 1-MAE for SARIMA segmentert (45,97) i teksten l. 535, men er ikke synlig i Tabell 4.

Ingen av tiltakene er tunge: prioritet 1-listen kan lukkes på ca. 15 min, og full lukking inkludert pedagogisk polering tar omtrent 50 min. Kvalitetsnivået er **øvre middels for LOG650-standard**, og med prioritet 1- og prioritet 2-tiltakene gjennomført vil kapittelet holde et solid akademisk nivå og være klart for peer review M-05.

---

## 8. Oppfølgingssaker (for vurdering)

- **Verifikasjon av MAE/MAPE-tall mot scenario_sammendrag.csv:** Reviewen forutsetter at tallene i Tabell 2–4 er korrekt beregnet av `scenario_analyse.py`. En ad-hoc gjenberegning av minst ett MAE-tall (f.eks. RF uten lag_1 = 169,1 stk) fra `004 data/scenario_sammendrag.csv` ville styrke etterprøvbarheten.
- **Konsistenssjekk Tabell 5 mot Vedlegg A1:** Hvis vedlegg A1 inneholder uavhengig residualanalyse, sikre at Q-statistikkene matcher Tabell 5-verdiene.
- **Figurnummerering vs status.md:** Status.md l. 101 nevner «Figur 4» (`fig_scenario_sammenligning.png`), men rapporten viser «Figur 5» på samme plass. Dette er en mindre drift som bør oppdateres i status.md ved sluttgjennomgang av rapporten.
- **Hybridmodell-definisjonens plassering:** Avgjør om hybridene først skal innføres i kap. 6 (modellvalg), kap. 7 (analyse) eller kap. 9.4 (diskusjon). Per i dag ligger definisjonen kun i kap. 9, hvilket gjør dem «svake» i resultatpresentasjonen i kap. 8.

---

*Generert 2026-04-30 som del av intern review-prosess før peer review M-05 (2026-05-01).*
