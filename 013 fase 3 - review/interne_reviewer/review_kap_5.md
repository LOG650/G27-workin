# Intern review av Prosjektrapport_LOG650_G27 — kap. 5 (Metode og data)

**Dato:** 2026-04-29
**Reviewer:** Intern gjennomgang (Claude Code-assistert)
**Rapportfil:** `014 fase 4 - report/Prosjektrapport_LOG650_G27.md` (kap. 5, l. 284–329)
**Formål:** Strukturert kvalitetsvurdering av kap. 5 (Metode og data) før peer review (M-05, 2026-05-01).

---

## Sammendrag og status

| Punkt | Status |
|---|---|
| Kap. 5 vurdert | Ja |
| Tiltak besluttet | Prioritet 1 (F3, F5, M5) gjennomført 2026-04-29; prioritet 2 og 3 åpne |

**Hovedfunn:** Kapittelet er teknisk velskrevet og dekker fire av fem CLAUDE.md §11-krav. Største svakheter er (1) **manglende oppsummeringstabell med tekniske nøkkeltall** — strengt tatt et brudd på CLAUDE.md §11 — (2) manglende kildehenvisninger for kjernemetodene (SARIMA, RF, Ljung-Box, ADF), og (3) repetisjon av evalueringsmål mellom 5.2 og 5.6.

---

## 1. Språkvurdering

**Engelske termer (inkonsistent håndtering):**
- «"Lumpy Demand"» (l. 290) — i anførselstegn, men ikke parafrasert. Termen er sentral for resten av rapporten og bør parafraseres første gang («uregelmessig/sporadisk etterspørsel»).
- «*out-of-sample*» (l. 317) i kursiv uten norsk parafrase. Forslag: «(*out-of-sample*, dvs. testet på data utenfor treningsperioden)».
- «"Censored Demand"» (l. 312) — termen er forklart i konteksten («Det er ingen … -effekter»), men en kort norsk parafrase ved første bruk («kapasitetsbegrenset etterspørsel») ville lette leseren.
- «*grid-search* (systematisk rutenettsøk)» og «*feature engineering* (variabelutvikling)» (l. 296) — korrekt parafrasert i parentes. Bevar samme stil for de øvrige termene.
- «3-fold TimeSeriesSplit» (l. 296, l. 305) — «3-fold» er engelsk og kan på norsk hete «trefoldig» eller «3-folds». «TimeSeriesSplit» er navnet på Scikit-learn-klassen og kan beholdes uendret.

**Forkortelser og fagtermer:**
- ADF (Augmented Dickey-Fuller) introdusert l. 297 — første introduksjon i rapporten. OK.
- ACF (l. 297) brukes uten parafrase. Forslag: «ACF-analyse (autokorrelasjonsfunksjon)» ved første bruk.
- MAE, MAPE, sMAPE, WAPE og Bias defineres tydelig i 5.6 — utmerket.

**Skrivefeil og tegnsetting:**
- l. 311: «12 helgdager» → «12 helgedager» (mangler «e»).
- l. 290: «"Lumpy Demand"» — sjekk anførselstegnstil mot resten av rapporten (rette doble vs norske «…»).
- l. 314: parentesreferanse til «vask_data.py» bør krysshenvises til kap. 9.1, ikke detaljeres her (se M3 nedenfor).

**Generell flyt:**
- 5.1 og 5.2 er konsist og presist skrevet.
- 5.3 har god struktur (narrativt avsnitt etterfulgt av punktliste).
- 5.6 mangler innledende setning som binder til 5.2 — leseren slipper rett inn i listen.

## 2. Innholdsvurdering (per underkapittel)

### 5 Innledning (l. 284–285)
Kort, presis innledningsavsnitt. Setningen «Formålet er å sikre at analysen er transparent og etterprøvbar» speiler CLAUDE.md §11-hensikten direkte — bra forankring.

### 5.1 Metodevalg og forskningsstruktur (l. 287–290)
**Faglig styrke:** Begrunnelse for kvantitativt design er klar. Triangulering (SARIMA + Random Forest) introdusert tidlig som metodisk argument.

**Svakhet (F1):** Ingen referanse til metodologi-litteratur. Påstanden «kvantitativt forskningsdesign basert på en case-studie» er en metodologisk klassifisering som vanligvis krever kildehenvisning (Yin 2018, Bryman). CLAUDE.md §2 sier eksplisitt at «metodiske valg skal begrunnes med henvisning til relevant pensum/litteratur».

**Svakhet (F2):** «"Lumpy Demand"» (l. 290) er en sentral kategorisering av etterspørselsmønsteret, men termen brukes uten kildehenvisning. Klassisk referanse: Syntetos & Boylan (2005) eller Croston (1972). En kilde her ville bundet metodevalget til pensum.

### 5.2 Den analytiske prosessen (l. 292–298)
**Faglig styrke:** Fire-fase-modellen (Dataklargjøring → Modellering → Validering → Evaluering) speiler CLAUDE.md §8 («Datavask → Deskriptiv analyse → Modellering → Evaluering»). Tekniske detaljer (144 SARIMA-kombinasjoner, 3-fold TimeSeriesSplit, 16 GBM-kombinasjoner) gir god transparens.

**Svakhet (M1 — repetisjon):** Punkt 4 i 5.2 nevner allerede MAE/MAPE/sMAPE/WAPE/Bias og at de er «segmentert på normale dager og toppdager». Disse målene defineres så på nytt i 5.6. Forslag: la 5.2 punkt 4 kort si «evalueres med fem komplementære mål, definert i 5.6», og la 5.6 ha den fulle definisjonen.

**Svakhet (M2):** Punkt 3 (Validering) nevner Ljung-Box-test med eksplisitt H0, men ADF-test omtales uten H0. Inkonsistent presisjon. ADF: H0 = serien har enhetsrot (er ikke-stasjonær).

**Svakhet (F3 — manglende kilder):** Hverken SARIMA, Random Forest, Gradient Boosting, Ljung-Box-test, ADF-test, AIC eller TimeSeriesSplit har kildehenvisning. Klassiske referanser:
- SARIMA / Box-Jenkins: Box, Jenkins, Reinsel & Ljung (2015)
- Random Forest: Breiman (2001)
- Gradient Boosting: Friedman (2001)
- Ljung-Box: Ljung & Box (1978)
- ADF: Dickey & Fuller (1979)
- AIC: Akaike (1974)

For et metodekapittel med transparenskrav er minst 2–3 av disse forventet.

### 5.3 Datagrunnlag, struktur og lagerstatus (l. 300–305)
**Faglig styrke:** Validering av data via lagerstatus-skjermbilde (Vedlegg A8) er en god metodisk grep — den begrunner kjerneantakelsen (utlevert volum = etterspørsel) empirisk.

**Mindre punkt (S1):** Tittelen lover «struktur» (datastruktur), men selve avsnittet behandler kilde, periode og variabel — mens datastrukturen (langt format, virkedager, daglig granularitet) ligger spredt mellom 5.2 (pivot fra bredt til langt format) og 5.5. To-tre setninger om endelig datastruktur ville styrket 5.3.

### 5.4 Datakvalitet, antagelser og begrensninger (l. 307–314)
**Faglig styrke:** Tydelige punkter for antagelser, eksplisitt om virkedagsfiltrering (s=5 vs s=7), og åpenhet om datafeil og rettelse.

**Svakhet (M3 — plassering av datafeil):** «Oppdaget datafeil korrigert» (l. 314) hører bedre i kap. 9.1 (refleksjon over arbeidsprosess). Plassering i 5.4 bryter med kapitlets formål: å beskrive *gjeldende, vellykkede* metode. Forslag: kort henvisning «(se kap. 9.1 for dokumentasjon av tidligere datafeil)» her, og full forklaring i kap. 9.1.

**Svakhet (M4 — uklar referanse):** «Tapet på 100 stk (12 helgdager med observert salg > 0) utgjør 0,5 % av totalen» (l. 311) — hvilken total? RELEX-aggregert (20 801) eller virkedager (20 701)? Bør spesifiseres for konsistens med kap. 4.3, der F1 i kap.-4-review allerede flagger inkonsistente totaltall.

**Svakhet (F4):** «Dataene anses som høyt reliable» (l. 308) er en sterk påstand uten formell reliabilitetstest. Krysstemming på 0,6 % er én indikator, men «høyt reliable» er en kvalitetsbedømmelse som vanligvis krever flere indikatorer eller en eksplisitt grense. Nedtoning til konkret formulering («konsistente innen 0,6 % på transaksjonsnivå») ville være mer presist.

### 5.5 Oppdeling av data (trening og test) (l. 316–321)
**Faglig styrke:** Begrunnelse for splitten (out-of-sample, kampanjeevaluering) er gjennomtenkt. Inkludering av Crazy Days uke 5/2026 i testperioden er metodisk relevant og forsvares eksplisitt.

**Svakhet (M5 — uklar treningsstørrelse):** «218 virkedager rå, 208 effektivt etter at de 10 første droppes fordi lag- og rolling-features ikke er definert der» — gjelder dette alle modeller? SARIMA bruker antakelig hele 218 dager, og baseliner (Seasonal Naïve, Holt-Winters) trenger ikke lag-features. Bør spesifiseres at «208 effektivt» kun gjelder ML-modeller med eksplisitte lag/rolling-features. Nåværende formulering kan tolkes som at alle modeller får 208 dager.

**Mindre punkt (S2):** «Splitten tilsvarer ~83/17 %» — basis er ikke spesifisert. 83/17 av virkedager (260) eller av effektive treningsdager (208 + 42 = 250)? 218/260 = 83,8 %, 218/250 = 87,2 %, 208/250 = 83,2 %. Formuleringen bør ha eksplisitt nevner.

### 5.6 Evalueringsmål (l. 323–329)
**Faglig styrke:** Fem mål med tydelig rolle og presis tekstlig tolkning. Bias-definisjonen kobler eksplisitt til sikkerhetslagerdimensjonering — bra praktisk relevans.

**Svakhet (S3 — manglende formler):** Målene defineres tekstlig, men ingen formler oppgis. For et metodekapittel om transparens og etterprøvbarhet er det vanlig å oppgi formler for MAE, MAPE, sMAPE, WAPE og Bias — særlig fordi sMAPE og WAPE har flere konkurrerende definisjoner i litteraturen. Forslag: legg til en kompakt formelboks eller tabell.

**Mindre punkt (K-ref):** «Hyndman & Koehler, 2006» (l. 298) og «Seiringer et al., 2024» (l. 329) — sjekk at begge ligger i bibliografien (kap. 11) og at APA 7-formatering er korrekt.

## 3. Identifiserte svakheter (status og tiltak)

Alle tiltak markert som **«Status: åpen — avventer brukerens vurdering»** per brukerens instruks.

### Faglige svakheter
- **F1:** Manglende referanse til metodologi-litteratur for kvantitativt design (5.1, l. 288). **Status: åpen.**
- **F2:** «Lumpy Demand» mangler kildehenvisning (5.1, l. 290). **Status: åpen.**
- **F3:** Ingen kilder for SARIMA / RF / GBM / Ljung-Box / ADF / AIC (5.2). **Status: rettet 2026-04-29** — Box & Jenkins (1976) og Breiman (2001) lagt til i 5.1; Ljung & Box (1978) og Dickey & Fuller (1979) lagt til i 5.2. Bibliografi oppdatert tilsvarende.
- **F4:** «Høyt reliable» (5.4, l. 308) er en sterk påstand uten formell reliabilitetstest. **Status: åpen.**
- **F5 (kritisk — CLAUDE.md §11):** Manglende oppsummeringstabell med tekniske nøkkeltall (min, maks, gjennomsnitt) — eksplisitt krav. **Status: rettet 2026-04-29** — ny seksjon 5.7 med Tabell 2 (min, maks, gjennomsnitt, median, std, P90, toppdager, sum) for trening- og testsett, regnet fra `vasket_salg_daglig.csv`.

### Metodiske svakheter
- **M1:** Repetisjon av evalueringsmål mellom 5.2 punkt 4 og 5.6. **Status: åpen.**
- **M2:** Inkonsistent presisjon — Ljung-Box H0 oppgis, ADF H0 mangler (5.2, l. 297). **Status: åpen.**
- **M3:** Datafeil-historikk i 5.4 (l. 314) hører bedre i kap. 9.1. **Status: åpen.**
- **M4:** «100 stk = 0,5 %» — basis ikke spesifisert (5.4, l. 311). **Status: åpen.**
- **M5:** «218 vs 208» — uklart om gjelder kun ML-modeller (5.5, l. 318). **Status: rettet 2026-04-29** — formuleringen presisert: SARIMA og baseliner trenes på hele 218 dager, mens RF og GBM får 208 effektive dager pga. lag/rolling-features.

### Strukturelle svakheter
- **S1:** Tittelen 5.3 lover «struktur», men datastrukturbeskrivelse er spredt. **Status: åpen.**
- **S2:** «~83/17 %» — basis (260 vs 250) ikke spesifisert (5.5, l. 321). **Status: åpen.**
- **S3:** Ingen formler i 5.6. **Status: åpen.**
- **S4:** Manglende overgang fra 5.6 til kap. 6 — leser slipper brått ut av metodekapittelet. **Status: åpen.**
- **S5:** Ingen visuell oppsummering (flytdiagram av 4-fase-prosessen) i 5.2. **Status: åpen.**

### Formidling og typografi
- **K1:** «12 helgdager» → «12 helgedager» (5.4, l. 311). **Status: åpen.**
- **K2:** Engelske termer inkonsistent oversatt («out-of-sample», «Censored Demand», «Lumpy Demand»). **Status: åpen.**
- **K3:** ACF brukes uten parafrase (5.2, l. 297). **Status: åpen.**
- **K4:** Anførselstegn-typografi rundt «Lumpy Demand» — sjekk konsistens (5.1, l. 290). **Status: åpen.**

## 4. Forbedringsforslag (konkrete formuleringer)

**F1 — metodologi-kilde i 5.1:**
> «Studien benytter et kvantitativt forskningsdesign basert på en case-studie av REMA 1000 Distribusjon Trondheim (Yin, 2018). Valget…»

**F2 — Lumpy Demand-kilde:**
> «…for å håndtere uregelmessig etterspørsel («Lumpy Demand»; Syntetos & Boylan, 2005).»

**F3 — kjernemodeller:**
> «…kombinerer klassisk statistikk (SARIMA; Box, Jenkins, Reinsel & Ljung, 2015) med maskinlæring (Random Forest; Breiman, 2001)…»
> «…ACF-analyse og formell Ljung-Box-test (Ljung & Box, 1978; H0: residualer uavhengige). ADF-test (Augmented Dickey-Fuller; Dickey & Fuller, 1979; H0: serien har enhetsrot) vurderer stasjonariteten…»

**F4 — reliabilitet:**
> «Dataene viser høy intern konsistens: RELEX-eksporten krysstemmer innen 0,6 % mot et uavhengig ERP-uttrekk på transaksjonsnivå (kap. 4.3).»

**F5 — oppsummeringstabell (kritisk):** Legg til tabell etter 5.5 (eller som nytt 5.7) etter mønster:

| Statistikk | Treningssett (218 dager) | Testsett (42 dager) |
|---|---|---|
| Min | … | … |
| Maks | … | … |
| Gjennomsnitt | … | … |
| Median | … | … |
| Standardavvik | … | … |
| Toppdager (>P90) | … | … |

Dette tilfredsstiller eksplisitt CLAUDE.md §11 «Oppsummering: Tabell med tekniske nøkkeltall (min, maks, gjennomsnitt)».

**M1 — fjern repetisjon:** I 5.2 punkt 4: «Modellene sammenlignes med fem komplementære mål, definert i 5.6, segmentert på normale dager og toppdager.»

**M2 — H0 for ADF:** «…ADF-test (Augmented Dickey-Fuller, H0: serien har enhetsrot) vurderer stasjonariteten…»

**M3 — flytt datafeil til kap. 9:** I 5.4: «(For dokumentasjon av tidligere datafeil og rettelse, se kap. 9.1.)» — fjern detaljnivået med «6 201 stk vs ~20 900 stk» fra metodekapittelet.

**M4 — spesifiser basis:** «Tapet på 100 stk (12 helgedager med observert salg > 0) utgjør ~0,5 % av RELEX-totalvolumet (20 801 stk)…»

**M5 — klarere treningsstørrelse:**
> «Treningssett: 218 virkedager. For ML-modeller med lag- og rolling-features (RF, GBM) reduseres effektivt treningssett til 208 dager fordi de 10 første dagene mangler komplette features. SARIMA og baseliner (Seasonal Naïve, Holt-Winters) bruker hele 218 dager.»

**S2 — spesifiser %-basis:** «Splitten tilsvarer ~83 % / 17 % av tilgjengelige virkedager (218 av 260 i trening, 42 av 260 i test).»

**S3 — formler i 5.6:** Legg til en formelboks med matematiske definisjoner for hver av de fem målene (særlig sMAPE og WAPE som har flere konkurrerende definisjoner).

**S4 — overgang til kap. 6:** Avsluttende setning i 5.6: «I neste kapittel begrunnes konkret valg av åtte modeller og deres komplementære roller i den metodiske trianguleringen.»

**S5 — flytdiagram:** Vurder enkel figur i 5.2 (Mermaid-diagram eller boksdiagram): Dataklargjøring → Modellering → Validering → Evaluering, med biblioteknavn og hovedoperasjoner.

**K1:** «12 helgdager» → «12 helgedager».
**K2:** Standardiser engelske termer — første gang: norsk parafrase + engelsk i parentes; deretter konsekvent valg av én form.
**K3:** «ACF (autokorrelasjonsfunksjon)» ved første bruk.
**K4:** Standardiser anførselstegn (norsk «…» eller rette doble " ", konsekvent gjennom kapitlet).

## 5. Samsvar med CLAUDE.md §11 (Kapittel 5)

| Krav i CLAUDE.md §11 | Dekket | Hvor | Kommentar |
|---|---|---|---|
| Metodevalg (type analyse, stegvis struktur) | Ja | 5.1, 5.2 | Mangler kildehenvisning (F1) |
| Analyseprosess (Dataklargjøring → Modellering → Validering → Prognose) | Ja | 5.2 | «Prognose» heter «Evaluering» i rapporten — semantisk samme |
| Datakvalitet (antagelser, begrensninger, reliabilitet) | Ja | 5.4 | F4-merknad om «høyt reliable» |
| Oppdeling (begrunnelse for trening/test) | Ja | 5.5 | M5/S2-merknader om uklarhet |
| **Tabell med tekniske nøkkeltall (min, maks, gjennomsnitt)** | **Nei** | — | **F5: kritisk mangel** |

**Konklusjon:** Fire av fem CLAUDE.md §11-krav er dekket. Manglende oppsummeringstabell (F5) er strengt tatt et brudd på lærerens føringer — Tabell 1 i kap. 4.3 dekker virkedagsserien, men ikke trening/test-segmenteringen.

## 6. Samsvar med prosjektplan og status

**Prosjektplan (`012 fase 2 - plan/prosjektplan.md`):**
- Metodevalg (kvantitativ tidsserie + ML-triangulering) samsvarer med ACT-04 og ACT-08 i WBS.
- Leveranser knyttet til prognosebias og presisjon (MAE/MAPE) er dekket gjennom 5.6 og videre i kap. 8.
- Avgrensning fra prosjektplan (én produktfamilie, daglig nivå) reflekteres riktig.

**Status (`012 fase 2 - plan/status.md`):**
- M-03 «Ferdig analyse» oppnådd 2026-04-16 (11 dager foran plan) — kap. 5 er konsistent.
- Datafeil i `vask_data.py` er dokumentert i status.md og krysshenvist i 5.4.
- Kritisk linje (datavask, modellering) er reflektert i 5.2 og 5.4.

**WBS (`012 fase 2 - plan/wbs.md`):**
- ACT-07 (Datavask), ACT-08 (Analyse og modellering) er 100 % i WBS — samsvarer med metodebeskrivelse i 5.2.
- ACT-09 (Skriving) er 90 % — denne reviewen er en del av aktiviteten.

**Proposal (`011 fase 1 - proposal/proposal.md`):**
- Problemstillingen ivaretatt: kvantitativ måling av prognosepresisjon (MAE/MAPE m.fl.).
- Avgrensningen «ett distribusjonssenter, ett produkt» reflektert konsekvent.

**Avvik fra plan:** Ingen vesentlige avvik. Et opprinnelig planlagt fokus på prising-data fra proposal er avgrenset bort (dokumentert i kap. 1.3). Dette berører ikke kap. 5 direkte, men metoderommen er smalere enn proposalens videste ramme.

## 7. Prioritert tiltaksliste

Prioritet: **1 = kritisk for innlevering, 2 = viktig for kvalitet, 3 = ønskelig polering**.

| Prioritet | Tiltak | Kapittel | Estimert innsats |
|---|---|---|---|
| 1 | F5: Legg til oppsummeringstabell (min/maks/gjennomsnitt for trening/test) — CLAUDE.md §11-krav | 5.5 (eller nytt 5.7) | 1–2 t |
| 1 | F3: Legg til kildehenvisninger for SARIMA, RF, Ljung-Box, ADF (minst 3 av 5) | 5.1, 5.2 | 30 min |
| 1 | M5: Klargjør at «208 effektivt» kun gjelder ML-modeller med lag-features | 5.5 | 10 min |
| 2 | F1+F2: Kilder for kvantitativt design (Yin) og «Lumpy Demand» (Syntetos & Boylan) | 5.1 | 20 min |
| 2 | M1: Fjern repetisjon mellom 5.2 punkt 4 og 5.6 | 5.2, 5.6 | 10 min |
| 2 | M2: Legg til H0 for ADF-test | 5.2 | 5 min |
| 2 | M3: Flytt detaljert datafeil-historikk fra 5.4 til kap. 9.1 (kun krysshenvisning igjen i 5.4) | 5.4 → 9.1 | 15 min |
| 2 | M4: Spesifiser basis for «0,5 %» | 5.4 | 5 min |
| 2 | S2: Spesifiser %-basis for trening/test-splitt | 5.5 | 5 min |
| 2 | S3: Legg til formler for de fem evalueringsmålene | 5.6 | 30 min |
| 2 | F4: Tone ned «høyt reliable» til konkret formulering | 5.4 | 5 min |
| 3 | S4: Overgangssetning til kap. 6 | 5.6 | 5 min |
| 3 | S5: Flytdiagram av 4-fase-prosessen | 5.2 | 30–60 min |
| 3 | S1: Strukturell oppstramming av 5.3-tittel og innhold | 5.3 | 5 min |
| 3 | K1: «helgdager» → «helgedager» | 5.4 (l. 311) | 1 min |
| 3 | K2: Standardiser engelske termer | 5.1, 5.4, 5.5 | 15 min |
| 3 | K3: ACF parafraseres ved første bruk | 5.2 | 2 min |
| 3 | K4: Anførselstegn-typografi | 5.1 | 5 min |

**Estimert total innsats (alle prioriteter):** ~5–6 timer.
**Prioritet 1 alene:** ~2 timer.

## 8. Samlet vurdering kap. 5

Kapittelet er teknisk velskrevet og dekker fire av fem læreren-spesifiserte kjernekrav (CLAUDE.md §11). Strukturen er logisk (5.1 metodevalg → 5.2 prosess → 5.3 data → 5.4 kvalitet → 5.5 oppdeling → 5.6 evalueringsmål) og overgangen fra kap. 4 er god. Detaljnivået i 5.2 (144 SARIMA-kombinasjoner, 3-fold TimeSeriesSplit, 16 GBM-kombinasjoner) gir god transparens.

**Største svakhet** er manglende oppsummeringstabell med tekniske nøkkeltall (F5) — et eksplisitt CLAUDE.md §11-krav. **Andre svakhet** er manglende kildehenvisninger for kjernemetodene (SARIMA, RF, Ljung-Box, ADF, AIC), som svekker kapitlets faglige forankring og bryter med CLAUDE.md §2.

Tre mindre, men presise punkter:
1. Repetisjon av evalueringsmål mellom 5.2 og 5.6 (M1) gir leseren samme informasjon to ganger.
2. Treningsstørrelsen «208 effektivt» (M5) er teknisk korrekt for ML-modeller, men skaper inntrykk av at alle modeller får 208 dager.
3. Plassering av datafeil-historikk i 5.4 (M3) bryter med kapitlets formål (gjeldende metode) — bør flyttes til kap. 9.1.

Med rettelse av prioritet 1-tiltakene (F5, F3, M5, ~2 timer) er kapitlet «meget godt». Inkludering av prioritet 2-tiltakene løfter det til solid akademisk standard for LOG650 og styrker etterprøvbarheten betydelig før peer review (M-05).

Etter prioritet 3 vil rapportens kap. 5 være på et nivå som tåler ekstern faglig vurdering uten reservasjoner.
