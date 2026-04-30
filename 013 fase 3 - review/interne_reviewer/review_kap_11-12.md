# Intern review av Prosjektrapport_LOG650_G27 — kap. 11 (Bibliografi) og 12 (Vedlegg)

**Dato:** 2026-04-30
**Reviewer:** Intern gjennomgang (Claude Code-assistert)
**Rapportfil:** `014 fase 4 - report/Prosjektrapport_LOG650_G27.md` (kap. 11, l. 672–708; kap. 12, l. 710–849)
**Formål:** Strukturert kvalitetsvurdering av kap. 11 (Bibliografi) og 12 (Vedlegg A1–A8) før peer review (M-05, 2026-05-01).

---

## Sammendrag og status

| Punkt | Status |
|---|---|
| Kap. 11 og 12 vurdert | Ja |
| Tiltak besluttet | Alle prioritet 1, 2 og 3-tiltak lukket 2026-04-30 (totalt 9 tiltak). Bonus-rettelse: Seiringer et al. (2024) korrigert til (2022) etter WebSearch-verifikasjon (DOI 10.1007/978-3-031-08623-6_62, Operations Research Proceedings 2021, utgitt 2022). Fil `fig3_lagerstatus.png` omdøpt til `fig_a8_lagerstatus.png` for å unngå forvirring med Figur 3. |
| Dekning | 18 referanser i bibliografi; alle 15 faglige kilder + 3 programvare-referanser nå verifisert som in-tekst-sitert (kap. 5.2 l. 308 oppdatert med APA-sitater). |

**Hovedfunn:** Bibliografien er konsistent APA 7-formattert, alfabetisk sortert, med DOI/URL for de fleste kildene. Vedleggene er omfattende (A1–A8) og dekker alle metodiske detaljer som rapporten henviser til. To forhold trekker likevel kvaliteten ned: (1) **programvare-bibliotekene Pandas, Statsmodels og Scikit-learn nevnes i kap. 5.2 l. 308 uten formell in-tekst-sitering**, til tross for at McKinney (2010), Seabold & Perktold (2010) og Pedregosa et al. (2011) er ført opp i bibliografien, og (2) **Seiringer et al. (2024) mangler DOI/URL og sidetall**, noe som svekker etterprøvbarheten av denne kilden. I tillegg har Vedlegg A2 AIC-verdier med to desimaler (2 510,06) mens kap. 7.2 etter revisjon bruker hele AIC-poeng (2 510), som skaper en mindre presisjons-inkonsistens.

---

## 1. Språkvurdering

**Styrker**
- Konsistent norsk i hele kap. 12 (vedlegg).
- Bibliografien følger APA 7-format med kursiv på journals/bok-titler, korrekt kommatering og DOI-formatering som «https://doi.org/...».
- Skille mellom faglig litteratur og programvare-bibliotek (### Programvare og biblioteker) er ryddig og konsistent.

**Svakheter**
- **Kap. 11 l. 675: «(rev. utg.)»** for Box & Jenkins (1976) er korrekt norsk APA-tilpasning. Ingen rettelse nødvendig.
- **Vedlegg A2 l. 734–738:** AIC-verdier vist med to desimaler (2 510,06; 2 511,96; ...), mens kap. 7.2 (l. 439) bruker hele AIC-poeng (2 510, 2 558, 2 481) etter revisjon 2026-04-30. Konsistens på tvers av kapittel og vedlegg styrker leseopplevelsen.
- **Vedlegg A3 l. 747:** «**Valgt hyperparametersett:**» bruker fet skrift som etikett før liste — OK per CLAUDE.md §1 (etikett i liste-element).
- **Vedlegg A2 l. 728:** «144 kombinasjoner av $(p,d,q)(P,D,Q)_5$» bruker subscript-notasjon, mens samme tabell på l. 734 viser «(0,1,1,5)» med s inni parentes. Mindre notasjons-inkonsistens; bør være konsistent med kap. 7.2 ($(P,D,Q)_5$).

---

## 2. Innholdsvurdering

### 2.1 Kap. 11 — Bibliografi (l. 672–708)

**Observasjon:** 18 referanser totalt — 15 faglige (Arunraj & Ahrens 2015, Box & Jenkins 1976, Breiman 2001, Dickey & Fuller 1979, Fildes et al. 2009 og 2022, Friedman 2001, Hyndman & Athanasopoulos 2021, Hyndman & Koehler 2006, Ljung & Box 1978, Makridakis et al. 2022, Seiringer et al. 2024, Syntetos & Boylan 2005, Syntetos et al. 2009, Trapero et al. 2015) og 3 programvare (McKinney 2010, Pedregosa et al. 2011, Seabold & Perktold 2010).

**Vurdering — in-tekst-sitering vs bibliografi:**

| Referanse | Bibliografi | In-tekst | Hvor sitert |
|---|---|---|---|
| Arunraj & Ahrens (2015) | Ja | Ja | Kap. 2.1 l. 84, kap. 3.2 l. 135 |
| Box & Jenkins (1976) | Ja | Ja | Kap. 3.2 l. 127, kap. 5.1 l. 305, kap. 6.3 l. 383 |
| Breiman (2001) | Ja | Ja | Kap. 3.2 l. 131, kap. 5.1 l. 305 |
| Dickey & Fuller (1979) | Ja | Ja | Kap. 5.2 l. 312, kap. 7.1 l. 434 |
| Fildes et al. (2009) | Ja | Ja | Kap. 2.2 l. 91, kap. 9.5 l. 638 |
| Fildes et al. (2022) | Ja | Ja | Kap. 1 l. 45, kap. 2.1 l. 82 |
| Friedman (2001) | Ja | Ja | Kap. 3.2 l. 132 |
| Hyndman & Athanasopoulos (2021) | Ja | Ja | Kap. 2.3 l. 98, kap. 3.1 l. 106, kap. 3.2 l. 123, kap. 6.1 l. 372 og 376, kap. 6.4 l. 423, kap. 7.4 l. 451, kap. 9.6 l. 646 |
| Hyndman & Koehler (2006) | Ja | Ja | Kap. 2.3 l. 94, kap. 3.3 l. 144, kap. 5.2 l. 313, kap. 8.2 (Tab. 3-bildetekst), kap. 9.1 l. 595 |
| Ljung & Box (1978) | Ja | Ja | Kap. 5.2 l. 312, kap. 7.4 l. 451 |
| Makridakis et al. (2022) | Ja | Ja | Kap. 2.1 l. 82, kap. 6.1 l. 376, kap. 6.5 l. 426 |
| Seiringer et al. (2024) | Ja | Ja | Kap. 2.3 l. 96, kap. 3.3 l. 156, kap. 5.2 l. 344, kap. 8.3 l. 549, kap. 9.4 l. 626 |
| Syntetos & Boylan (2005) | Ja | Ja | Kap. 2.1 l. 86 |
| Syntetos et al. (2009) | Ja | Ja | Kap. 1 l. 45, kap. 2.3 l. 96 |
| Trapero et al. (2015) | Ja | Ja | Kap. 2.2 l. 89, kap. 9.2 l. 606 |
| McKinney (2010) | Ja | **Nei** | Kap. 5.2 l. 308 nevner «Pandas» uten in-tekst-sitering |
| Pedregosa et al. (2011) | Ja | **Nei** | Kap. 5.2 l. 308 nevner «Scikit-learn» uten in-tekst-sitering |
| Seabold & Perktold (2010) | Ja | **Nei** | Kap. 5.2 l. 308 nevner «Statsmodels» uten in-tekst-sitering |

**Vurdering:**
- **15 av 18 kilder har korrekt in-tekst-sitering.** God dekning av faglig litteratur.
- **Programvare-referansene (3 kilder)** nevnes i kap. 5.2 l. 308 «ved bruk av **Python 3** og bibliotekene **Pandas**, **Statsmodels** og **Scikit-learn**», men uten parentes-sitering. Per APA 7 bør programvare som brukes som metodisk verktøy enten ha in-tekst-sitering eller en egen «Software»-note. Dette er F1.
- **Seiringer et al. (2024)** mangler DOI/URL og sidetall. Konferansebidrag har vanligvis enten DOI (når publisert i digitale proceedings) eller URL til konferansens publikasjon. Dette er F2.
- **Trapero et al. (2015)s genitive form (kap. 9.2 l. 606)** er noe uvanlig norsk. Bedre: «Trapero et al. (2015) sitt poeng om...» eller omformulering.

### 2.2 Kap. 12 — Vedlegg (l. 710–849)

**Vedlegg A1 — ADF-test for stasjonaritet (l. 712–725)**

Observasjon: Tabell med 3 serier, ADF-stat, p-verdi, kritisk verdi og stasjonaritetsvurdering. Henvisning til `004 data/adf_test.csv` og kryssreferanse til kap. 7.2 og 9.6.

Vurdering: Klar og presis. Forklaringen «Serien er stasjonær uten differensiering. AIC-minimerende grid-søk ... valgte likevel en modell med både vanlig og sesongdifferensiering» er ærlig metodisk dokumentasjon. ✓

**Vedlegg A2 — SARIMA grid-search (l. 727–742)**

Observasjon: Topp 5 konvergerte kombinasjoner med ordre, sesongordre, AIC, BIC og konvergensstatus. Forbedring mot opprinnelig konfigurasjon dokumentert.

Vurdering:
- **Tallinkonsistens:** AIC-verdier vist med to desimaler (2 510,06), mens kap. 7.2 etter revisjon bruker hele AIC-poeng (2 510). Bør harmoniseres til samme presisjon på begge steder. P1.
- **Notasjons-inkonsistens:** Tabellen viser «(0,1,1,5)» med s inni parentes, mens kap. 7.2 og A2-intro bruker «$(0,1,1)_5$»-notasjon. Bør være konsistent. P3.
- **«Helt ned mot 2 480»** for ikke-konvergerte modeller — kunne være mer presist (f.eks. «AIC 2 481, jf. kap. 7.2 l. 439» som krysshenvisning).

**Vedlegg A3 — GBM hyperparameter-tuning (l. 744–753)**

Observasjon: 16 kombinasjoner via 3-fold TimeSeriesSplit. Valgt hyperparametersett listet med fire parametere. Henvisning til `004 data/gbm_tuning.csv`.

Vurdering:
- «Tunet GBM gir ~30 % bedre MAE enn utunet standard» — «utunet standard» er nå definert i kap. 7.2 l. 443 (Sklearn-defaults: `learning_rate=0,1`, `max_depth=3`, `n_estimators=100`) etter F3-lukking i kap. 7-review. A3 kunne henvise til denne definisjonen for sporbarhet.

**Vedlegg A4 — Feature importance (l. 755–772)**

Observasjon: Tabell med 8 features for tre RF-varianter (full, GBM, uten lag_1).

Vurdering:
- Konsistent med kap. 7.2 l. 441 og kap. 9.3 l. 613 (lag_1 = 84 % i full RF, 79 % i GBM). ✓
- «Øvrige (dag-dummier, kampanjeflagg)» som samlet kategori er pragmatisk; kunne brutt ned hvis ønskelig, men leseren henvises til `rf_feature_importance.csv`. ✓

**Vedlegg A5 — Random Forest-hyperparametere (l. 774–787)**

Observasjon: Tabell med 6 parametere og verdier for RF.

Vurdering: Klar og kompakt. ✓ Kunne supplert med en kort note om at `random_state=42` er valgt for reproduserbarhet.

**Vedlegg A6 — Kampanjekalender (l. 789–802)**

Observasjon: 5 hendelser (3 kalenderhendelser, 2 Crazy Days) med startdato, sluttdato, type, beskrivelse og kilde.

Vurdering: Konsistent med kap. 4 og kap. 8 (testperioden inneholder Crazy Days uke 5 og uke 6 etterpåvirkning). ✓

**Vedlegg A7 — Filstruktur og reproduserbarhet (l. 804–837)**

Observasjon: Treebasert oversikt over `004 data/`, `012 fase 2 - plan/` og `014 fase 4 - report/figurer/`.

Vurdering:
- **«scenario_sammendrag.csv — Scenario 1 vs 2 (Tabell 2)»** i A7 er litt upresis: filen inneholder ALLE evalueringsdata for begge scenarier (Tabell 2, 3, 4 og 4b), ikke bare Tabell 2. Bør oppdateres til «scenario_sammendrag.csv — Scenario 1 vs 2, alle modeller og segmenter (kilde for Tabell 2, 3, 4 og 4b)».
- **«fig3_lagerstatus.png (RELEX-skjermbilde, Vedlegg A8)»** — filnavnet «fig3_lagerstatus.png» er forvirrende fordi A8 ikke er Figur 3. Konsistent navngivning ville være «fig_a8_lagerstatus.png» eller «fig_lagerstatus_relex.png». Mindre kosmetisk.
- **Andre skript som ikke er listet:** `metrics.py`, `modell_test.py` (nevnt i status.md ACT-08) er ikke listet i A7. Vurder om disse skal være med (kanskje under «Hjelpemoduler»).
- Reproduksjonsinstruksjon på slutten («Alle analysene kan reproduseres ved å kjøre ...») er klar og presis. ✓

**Vedlegg A8 — Lagerstatus fra RELEX (l. 839–849)**

Observasjon: RELEX-skjermbilde med faktisk salg, lagernivå og prognose for hele perioden mars 2025 – februar 2026. Bildetekst forklarer fargene og kryssreferer til kap. 5.3 og 4.5.

Vurdering: Sterk metodisk dokumentasjon — viser at lageret aldri var utsolgt og at observerte salgstall kan tolkes som reell utlevert etterspørsel. ✓

### Tverrgående: figurer/tabeller-konsistens

- Tabeller A1–A6 har ikke separate «*Tabell A1:*»-bildetekster, kun kontekstuell innledning over tabellen. Dette er akseptabel praksis for vedlegg.
- A8 har proper «*Vedlegg A8:*»-bildetekst i tråd med CLAUDE.md §7. ✓

---

## 3. Identifiserte svakheter (med tiltakskoder)

### Faglige
- **F1:** Kap. 5.2 l. 308 — Pandas, Statsmodels og Scikit-learn nevnes uten in-tekst-sitering, til tross for at McKinney (2010), Seabold & Perktold (2010) og Pedregosa et al. (2011) er i bibliografien. **Status: lukket 2026-04-30.**
- **F2:** Kap. 11 l. 695 — Seiringer et al. (2024) mangler DOI/URL og sidetall. **Status: lukket 2026-04-30** — DOI 10.1007/978-3-031-08623-6_62 lagt til; samtidig korrigert år fra 2024 til 2022 (Operations Research Proceedings 2021, utgitt av Springer 2022) etter WebSearch-verifikasjon. Alle 5 in-tekst-sitater oppdatert tilsvarende.
- **F3:** Vedlegg A3 — Henvisning til kap. 7.2 (Sklearn-defaults-definisjon for «utunet standard») mangler. **Status: lukket 2026-04-30** — Sklearn-defaults eksplisitt definert i A3-tekst med kryssreferanse til kap. 7.2.

### Metodiske
- **M1:** Vedlegg A7 — «scenario_sammendrag.csv — Scenario 1 vs 2 (Tabell 2)» er upresis; filen er kilde for Tabell 2, 3, 4 og 4b. **Status: lukket 2026-04-30.**

### Strukturelle
- **S1:** Vedlegg A2 og A4 — Kunne ha eksplisitte kryssreferanser ved AIC-tall og lag_1 = 84 % som peker tilbake til hovedkapitlene (omvendt retning). Mindre. **Status: lukket 2026-04-30** — A2-intro endret til «(omtalt i kap. 7.2)» og A4-intro tilføyd referanse til kap. 7.2 og kap. 9.3.

### Formidling
- **P1:** Vedlegg A2 l. 734–738 — AIC-verdier vist med to desimaler, mens kap. 7.2 etter revisjon bruker hele AIC-poeng. Bør harmoniseres. **Status: lukket 2026-04-30.**
- **P2:** Vedlegg A2 l. 734 — Notasjon «(0,1,1,5)» bør konverteres til «$(0,1,1)_5$»-format for konsistens med kap. 6.3 og 7.2. **Status: lukket 2026-04-30** — alle 5 rader i A2-tabellen oppdatert til (P,D,Q)_5-notasjon.
- **P3:** Vedlegg A7 — Filnavn «fig3_lagerstatus.png» refererer til Vedlegg A8, ikke Figur 3; navnet er forvirrende. **Status: lukket 2026-04-30** — fil omdøpt med `git mv` til `fig_a8_lagerstatus.png`; A7-filstrukturlisten og A8-bildereferansen oppdatert tilsvarende.
- **P4:** Vedlegg A5 — Kunne supplert med kort note om at `random_state=42` sikrer reproduserbarhet. **Status: lukket 2026-04-30** — note tilføyd under A5-tabellen.

---

## 4. Forbedringsforslag

| ID | Forslag |
|---|---|
| F1 | Endre kap. 5.2 l. 308 fra «**Pandas**, **Statsmodels** og **Scikit-learn**» til «Pandas (McKinney, 2010), Statsmodels (Seabold & Perktold, 2010) og Scikit-learn (Pedregosa et al., 2011)». Fjerner samtidig fet skrift inni løpende tekst (CLAUDE.md §1). |
| F2 | I kap. 11 l. 695, supplementer Seiringer et al. (2024) med DOI eller URL hvis tilgjengelig, og legg til sidetall. Eksempel: «*Proceedings of the International Conference on Production Research*, [sidenummer]. [DOI/URL hvis tilgjengelig]». |
| F3 | I Vedlegg A3 l. 753, tilføy: «(jf. kap. 7.2 for definisjon av Sklearn-defaults).» |
| M1 | I Vedlegg A7, endre «scenario_sammendrag.csv — Scenario 1 vs 2 (Tabell 2)» til «scenario_sammendrag.csv — Scenario 1 vs 2, alle modeller og segmenter (kilde for Tabell 2, 3, 4 og 4b)». |
| P1 | Avgjør konsistent presisjon for AIC: enten endre Vedlegg A2 til hele AIC-poeng (2 510, 2 512, 2 534, 2 538, 2 552), eller endre kap. 7.2 til samme to-desimal-presisjon som A2. Anbefaling: behold A2 med to desimaler (vedlegget skal være den presise referansen) og merk i A2-bildetekst at hovedteksten bruker avrundede verdier. |
| P2 | I Vedlegg A2 l. 734–738, endre «(0,1,1,5)» til «(0,1,1)_5» for notasjons-konsistens. |
| P3 | Vurder å gi nytt filnavn til `fig3_lagerstatus.png` (f.eks. `fig_a8_lagerstatus.png`) for å unngå forvirring med Figur 3 i hovedrapporten. Krever oppdatering av A7-listen og A8-bildereferanse. |
| P4 | I Vedlegg A5, tilføy: «`random_state=42` sikrer reproduserbarhet av tilfeldig utvalg i bootstrap og feature subsampling.» |

---

## 5. Samsvar med prosjektplan og status

**Mot proposal og prosjektplan:** Bibliografien dekker alle pensumområder relevante for problemstillingen (retail forecasting, kampanjer, residualdiagnostikk, sikkerhetslager). Vedleggene reflekterer all teknisk infrastruktur (grid-search, tuning, residualtester, feature importance) og dokumenterer reproduserbarhet (A7).

**Mot status.md:** Status av 2026-04-30 sier «| 11 Bibliografi | Ferdig | APA 7; Pandas, Statsmodels, Scikit-learn sitert |» og «| 12 Vedlegg | Ferdig | A1–A7 utfylt |». Reviewen viser at bibliografien faktisk har programvare-referansene i bibliografilisten, men ikke som in-tekst-sitater (F1) — status.md kan derfor strikt sett være misvisende. I tillegg er A8 nå utfylt (lagerstatus-skjermbilde), så status.md bør oppdateres til «A1–A8 utfylt».

**Mot WBS / kritisk linje:** Kap. 11 og 12 er en del av ACT-09 (Skriving av metode og resultat). Begge er strukturelt komplette. Ingen avvik.

**Mot CLAUDE.md §2 (APA 7):**
- Hovedformat: korrekt ✓
- DOI-formatering: korrekt ✓
- Alfabetisk sortering: korrekt ✓
- In-tekst-sitering: hovedsakelig korrekt, men F1-mangel for programvare.

**Mot CLAUDE.md §7 (figurer/tabeller):**
- A8 har proper bildetekst ✓
- A1–A6 mangler «*Tabell Ax:*»-bildetekster — akseptabelt for vedlegg, men kunne vært konsistent med hovedrapporten.

**Mot CLAUDE.md §9 (etterprøvbarhet, rød tråd):**
- Vedlegg A1–A8 + filstruktur i A7 gir solid grunnlag for etterprøvbarhet ✓
- Reproduksjonsinstruksjon på slutten av A7 ✓

---

## 6. Prioritert tiltaksliste

| Prioritet | Tiltak | Kapittel/linje | Estimert innsats |
|---|---|---|---|
| 1 | Tilføy in-tekst-sitater for Pandas/Statsmodels/Scikit-learn (F1) | 5.2, l. 308 | 3 min |
| 1 | Harmoniser AIC-presisjon mellom A2 og kap. 7.2 (P1) | A2 l. 734–738 eller 7.2 l. 439 | 5 min |
| 2 | Supplementer Seiringer et al. (2024) med DOI/URL og sidetall (F2) | 11, l. 695 | 5–10 min (krever søk) |
| 2 | Presiser scenario_sammendrag.csv-beskrivelse i A7 (M1) | A7 | 2 min |
| 2 | Henvis fra A3 til kap. 7.2 (Sklearn-defaults) (F3) | A3 l. 753 | 2 min |
| 2 | Konvertere notasjon (0,1,1,5) til (0,1,1)_5 i A2 (P2) | A2 l. 734–738 | 3 min |
| 3 | Tilføy reproduserbarhet-note i A5 (P4) | A5 | 2 min |
| 3 | Vurder navngivning av fig3_lagerstatus.png (P3) | A7, A8 | 5 min (krever fil-rename) |
| 3 | Vurder kryssreferanser fra A2 og A4 til hovedkapitler (S1) | A2, A4 | 3 min |

**Sum estimert innsats:**
- Prioritet 1: ca. 8 min (kritisk for innlevering — APA 7-fullstendighet og presisjons-konsistens).
- Prioritet 2: ca. 12–17 min (viktig for kvalitet — kildedetaljer og kryssreferanser).
- Prioritet 3: ca. 10 min (ønskelig polering).
- **Totalt: ca. 30–35 min** for full lukking.

---

## 7. Samlet vurdering

Kap. 11 (Bibliografi) er strukturelt solid med 18 referanser i konsistent APA 7-format, alfabetisk sortert med DOI/URL for de fleste kildene. 15 av 18 kilder har verifisert in-tekst-sitering. Kap. 12 (Vedlegg) er omfattende og dekker alle metodiske detaljer (A1 ADF-test, A2 SARIMA grid, A3 GBM-tuning, A4 feature importance, A5 RF-hyperparametere, A6 kampanjekalender, A7 filstruktur, A8 RELEX-lagerstatus). Reproduksjonsinstruksjonen i A7 og RELEX-skjermbildet i A8 er sterke transparens-styrker.

To forhold trekker kvaliteten ned. For det første **mangler programvare-bibliotekene Pandas, Statsmodels og Scikit-learn formelle in-tekst-sitater** i kap. 5.2 l. 308, til tross for at McKinney, Seabold & Perktold og Pedregosa et al. er ført opp i bibliografien. For det andre **mangler Seiringer et al. (2024) DOI/URL og sidetall**, noe som svekker etterprøvbarheten. I tillegg har Vedlegg A2 en mindre presisjons-inkonsistens med kap. 7.2 (to desimaler vs hele AIC-poeng).

Ingen av tiltakene er tunge: prioritet 1-listen kan lukkes på ca. 8 min (forutsatt at Seiringer-DOI ikke krever lengre søk), og full lukking inkludert polering tar omtrent 30–35 min. Kvalitetsnivået er **sterkt for LOG650-standard**, og med prioritet 1- og prioritet 2-tiltakene gjennomført vil kapitlene holde et solid akademisk nivå og være klart for peer review M-05.

---

## 8. Oppfølgingssaker (for vurdering)

- **Status.md-oppdatering:** Linje 160 («| 12 Vedlegg | Ferdig | A1–A7 utfylt |») er utdatert; A8 er nå på plass. Bør endres til «A1–A8 utfylt».
- **Egen mappe for nedlastede artikler (`003 references/artikler/`):** Brukeren har bedt om å opprette en mappe for nedlastede PDF-versjoner av siterte forskningsartikler. Dette håndteres som separat leveranse parallelt med denne reviewen, med en indeksfil som lister alle 18 kilder med DOI/URL og foreslått filnavn-konvensjon (siden binærfil-nedlasting ikke er mulig fra reviewer-prosessen).
- **Seiringer (2024) DOI:** Hvis konferansen har proceedings-DOI (f.eks. ICPR 2024), bør denne hentes inn. Ellers kan URL til konferanse-/workshop-publikasjon brukes.
- **Trapero et al. (2015)s genitive form** (kap. 9.2 l. 606): «Trapero et al. (2015)s» er noe uvanlig norsk; vurder om det skal stå som «Trapero et al. (2015) sitt poeng» eller omformuleres. Mindre språklig polering, ikke kritisk.

---

*Generert 2026-04-30 som del av intern review-prosess før peer review M-05 (2026-05-01).*
