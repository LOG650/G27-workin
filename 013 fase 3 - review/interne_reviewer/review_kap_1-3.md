# Interne reviewer av Prosjektrapport_LOG650_G27 — kap. 1, 2 og 3

**Dato:** 2026-04-29
**Reviewer:** Intern gjennomgang (Claude Code-assistert)
**Rapportfil:** `014 fase 4 - report/Prosjektrapport_LOG650_G27.md`
**Formål:** Strukturert kvalitetsvurdering av kapittel 1 (Innledning), kapittel 2 (Litteratur) og kapittel 3 (Teori) før innlevering.

---

## Sammendrag og status

| Kapittel | Review gjennomført | Tiltak gjennomført |
|---|---|---|
| 1. Innledning | Ja | Alle prioritet 1, 2 og 3 |
| 2. Litteratur | Ja | Alle prioritet 1, 2 og 3 + F2 (Syntetos & Boylan) + F3 (Hyndman & Athanasopoulos) |
| 3. Teori | Ja | Alle prioritet 1, 2 og 3 + brukerens egne notater (MA-fordeler, SARIMA/SARIMAX-presisering, ensemble-forklaring) |

**Bibliografi-tilføyelser i denne sesjonen:**
- Box, G. E. P., & Jenkins, G. M. (1976) — for SARIMA
- Breiman, L. (2001) — for Random Forest
- Friedman, J. H. (2001) — for Gradient Boosting
- Hyndman, R. J., & Athanasopoulos, G. (2021) — for ETS, firkomponent-dekomponering og generell metodisk støtte
- Syntetos, A. A., & Boylan, J. E. (2005) — for lumpy demand-klassifisering

**Tverrgående endringer:**
- Tankestreker som deler opp setninger fjernet i flytende tekst gjennom hele rapporten (datointervaller, overskrifter, tabelltitler beholdt som typografisk standard).
- Fildes-årstall korrigert fra (2008) til (2009) i kap. 2.2 og kap. 9.5.
- Forkastet leveranse «utvidet kampanjekalender» dokumentert i kap. 9.6 (med generell anbefaling) og kap. 10 (videre arbeid).

---

# Review 1 — Kapittel 1 (Innledning)

## 1. Språkvurdering

**Observasjon — grammatikk og rettskriving:**
- «største» → «størst» (komparativ predikativ uten artikkel).
- Inkonsekvent bruk av bindestrek i sammensetninger («svinn-regnskapet», «matsvinn-potensialet»). Norsk standard er sammenskriving.
- Overskrift «1.3 Avgrensinger» — norsk standardform er «avgrensninger».

**Observasjon — fagspråk og terminologi:**
- «Lasagne Familiepakning» konsistent gjennom rapporten. Avvik mot prosjektplan §2.1 («Toro familiepakning lasagne») er kun navngivning og påvirker ikke innholdet.
- «(Censored Demand)» med norsk forklaring «sensurert etterspørsel» er pedagogisk korrekt.
- «forecast accuracy» — engelsk parentes etter norsk hovedterm er konsistent med CLAUDE.md §1.

**Vurdering:** Språket er saklig og konsist. Identifiserte feil er rettet i denne sesjonen.

## 2. Innholdsvurdering (per underkapittel)

### 1 Innledning
Sterk åpning som etablerer både fag og praktisk relevans. Original kobling mellom tørrvareprognose og indirekte matsvinneffekt. Litteraturreferanse (Fildes et al., 2022; Syntetos et al., 2009) er tilføyd.

### 1.1 Problemstilling
Problemstillingen er konsistent med proposal og prosjektplan, spisset fra «utvalgte produkter» til «ett utvalgt produkt», begrunnet i 1.3.

**Tidligere intern selvmotsigelse** (linje 52 vs 54): Avsnittet sa at analysen var begrenset til historiske salgs- og kalenderdata, men neste avsnitt utvidet til Scenario 2 med kampanjeinformasjon. Rettet ved omformulering: «den primære modelleringen avgrenset til historiske salgs-, kalender- og kampanjedata, og inkluderer ikke pris eller reklamevariabler».

**Disponering**: Detaljert metodisk argumentasjon for to-scenarie-design er flyttet til kort forhåndsvarsling med kryssreferanse til kap. 5.

### 1.2 Delproblemer
Tre delproblemer dekker hhv. deskriptiv analyse (kap. 4), modellsammenligning (kap. 8.2–8.3) og scenariosammenligning (kap. 8.1).

**Tidligere inkonsistens**: Delproblem 2 utelot MAPE selv om rapporten rapporterer fem feilmål. Rettet til «(målt ved MAE, MAPE, sMAPE, WAPE og Bias, jf. kap. 5.6)».

### 1.3 Avgrensninger
Strukturen følger god akademisk praksis. Tilføyd:
- Tidsperiode (1. mars 2025 til 28. februar 2026, 12 måneder)
- Varestrøm (kun utgående, inngående og markedsføringsdata avgrenset bort)

Overskrift rettet fra «Avgrensinger» til «Avgrensninger».

### 1.4 Antagelser
Fire antagelser rasjonalisert til tre etter at duplisert prisdata-punkt er fjernet (lå allerede i 1.3). Stabilitetsantagelsen er konkretisert til etterprøvbar form: «ingen vesentlige strukturelle endringer ... herunder produktrelanseringer, varige prisendringer eller introduksjon av nye konkurrentprodukter».

## 3. Identifiserte svakheter (status: alle rettet)

### Faglige svakheter
- ✅ F1: Mangler litteraturreferanse for prognosens kritikalitet — rettet
- ✅ F2: Stabilitetsantagelse for upresis — rettet

### Metodiske svakheter
- ✅ M1: Selvmotsigelse linje 52 vs 54 — rettet
- ✅ M2: Detaljert metodisk diskusjon i innledning — flyttet til kap. 5

### Strukturelle svakheter
- ✅ S1: Prisdata-overflødighet 1.3 vs 1.4 — rettet
- ✅ S2: Tidsperiode mangler i 1.3 — tilføyd

### Formidling
- ✅ K1: «Avgrensinger» → «Avgrensninger»
- ✅ K2: Bindestrekbruk i sammensetninger — normalisert
- ✅ K3: «største» → «størst»
- ✅ K4: Delproblem 2 utelot MAPE — rettet

## 4. Samsvar med prosjektplan og status

**Mot proposal.md:** Problemstilling er identisk i innhold, spisset til ett produkt med faglig begrunnelse i 1.3. Forsvarlig.

**Mot prosjektplan §2.1:** Avvik fra prosjektplan om reklame, prising og inngående varestrøm var ikke tidligere eksplisitt avgrenset i 1.3 — er nå tilføyd som avgrensning «Varestrøm».

**Mot WBS (prosjektplan §2.4):** WBS-leveransen «Estimert kampanje- og priseffekt» er bare delvis dekket. Kampanjeeffekt adressert (Scenario 1 vs 2), priseffekt avgrenset bort. Begrunnet og dokumentert.

## 5. Samlet vurdering kap. 1

Kapittelet er strukturelt godt og følger CLAUDE.md §3 med tydelig problemstilling, delproblemer, avgrensninger og antagelser. Etter redigering er kapittelet løftet fra «godt» til «meget godt». Original kobling mellom tørrvareprognose og indirekte matsvinneffekt gir kapittelet en faglig signatur.

---

# Review 2 — Kapittel 2 (Litteratur)

## 1. Språkvurdering

**Observasjon — skrivefeil og tegnsetting:**
- Skrivefeil «salgstoppe» → «salgstopper» (rettet).
- Unødvendig komma før «kan man redusere» (rettet).
- Etterhengte mellomrom på flere linjer (rettet).

**Observasjon — terminologi:**
- Termvariasjon «flate topper» (kap. 2.2) vs «flate platåer» (kap. 4.5) — fjernet ved omformulering av kap. 2.2.

## 2. Innholdsvurdering (per underkapittel)

### 2 Innledning
Tematisk struktur (utfordringer, kampanjer, evaluering) er klar. Utvidet med kobling til rapportens egne valg: «danner det faglige grunnlaget for valg av modellutvalg (kap. 6), scenariodesign (kap. 5) og evalueringsmål (kap. 5.6)».

### 2.1 Kompleksitet i dagligvareprognoser
Tre kjernebidrag: Fildes et al. (2022), Makridakis et al. (2022), Arunraj og Ahrens (2015).

**Tidligere svakhet — koblingen Arunraj og Ahrens til lasagne**: «produkter med kort holdbarhet eller svingende etterspørsel ... direkte relevant for vår analyse» kunne tolkes som at lasagne har kort holdbarhet. Presisert: det er den svingende etterspørselen drevet av kampanjer som er relevant, ettersom produktet selv er en tørrvare med lang holdbarhet.

**Faglig styrking**: Syntetos og Boylan (2005) lagt til i nytt avsnitt, med klassifisering av lumpy demand basert på CV² og ADI. Direkte relevant for produktet (CV = 3,23, lumpy demand).

### 2.2 Kampanjer og menneskelig skjønn
Trapero et al. (2015) for kampanjekalender; Fildes et al. (2009) for menneskelige overstyringer.

**Kritisk APA-feil rettet**: «Fildes et al. (2008)» → «Fildes et al. (2009)» i samsvar med bibliografi (IJF 25(1), 2009). Også rettet i kap. 9.5.

**Spekulativ påstand om «flate topper»** som motsa kap. 4.5 (lageret aldri utsolgt) — fjernet og omformulert til konstaterende kobling: «Dette perspektivet er relevant når vi vurderer hvordan kampanjeflagg, pre-kampanje-stocking og eventuelle manuelle overstyringer påvirker den observerte etterspørselen ved RD Trondheim.»

### 2.3 Evaluering og logistisk verdi
Sterkt strukturert avsnitt: Hyndman og Koehler (2006) → Syntetos et al. (2009) → Seiringer et al. (2024). Rapportens beste underkapittel mht. faglig forankring.

**Faglig styrking**: Hyndman og Athanasopoulos (2021) lagt til som metodisk støtte for tidsserieprognoser.

### Avsluttende synteseavsnitt (nytt)
«Samlet underbygger litteraturen rapportens metodiske valg: kombinasjonen av klassiske tidsseriemodeller og maskinlæringsmodeller, eksplisitt integrasjon av kampanjekalender (Scenario 2), bruk av komplementære feilmål og særlig fokus på systematisk bias som operasjonelt sentralt mål.»

## 3. Identifiserte svakheter (status: alle rettet)

### Faglige svakheter
- ✅ F1: Tvetydig kobling Arunraj og Ahrens — presisert
- ✅ F2: Manglende ref. til lumpy demand-klassikere — Syntetos & Boylan (2005) tilføyd
- ✅ F3: Manglende ref. til standard tidsserielærebok — Hyndman & Athanasopoulos (2021) tilføyd

### Metodiske svakheter
- ✅ M1: «Flate topper»-hypotese motsa kap. 4.5 — fjernet

### Strukturelle svakheter
- ✅ S1: Manglende avsluttende syntese — tilføyd
- ✅ S2: Kapittelinnledning manglet kobling — utvidet

### Formidling og APA
- ✅ K1: Fildes-årstall (2008 → 2009) i kap. 2.2 og 9.5
- ✅ K2: «salgstoppe» → «salgstopper»
- ✅ K3: «flate topper» → fjernet ved omformulering
- ✅ K4: Unødvendig komma fjernet
- ✅ K5: Etterhengte mellomrom fjernet

## 4. Samsvar med prosjektplan og status

**Mot WBS-leveransen «Dokumentert litteraturgjennomgang»**: Dekket. 10 fagfellevurderte hovedreferanser + 3 programvarereferanser. Tilstrekkelig for LOG650-nivå.

**Mot CLAUDE.md §1 (APA 7. utgave)**: Bibliografien følger APA 7. In-text-sitering er nå konsistent etter Fildes-årstall-rettelsen.

## 5. Samlet vurdering kap. 2

Strukturelt godt komponert med tre tematiske underkapitler. Kap. 2.3 er sterkest forankret. Etter redigering har kapittelet fått (i) faglig styrket forankring av lumpy demand (Syntetos & Boylan), (ii) rettet APA-konsistens, (iii) fjernet intern selvmotsigelse mot kap. 4.5, og (iv) avsluttende syntese som binder til metodevalg. Løftet fra «funksjonell oversikt» til «strukturert fundament».

---

# Review 3 — Kapittel 3 (Teori)

## 1. Språkvurdering

**Observasjon — overskrifter og terminologi:**
- Overskrift «Distribusjonsleddet» → «distribusjonsleddet» (norsk overskriftskonvensjon).
- «Eventer» → «hendelser» (norsk fagspråk og konsistens med kap. 4.5, 6.4, A6).
- «logistikkfaglige teoriene» → «statistiske og metodiske rammene» (presisjon: SARIMA/RF/GBM er ikke logistikkfaglige teorier).
- «tradisjonelle prognosemetoder mindre treffsikre» → «lineære og utglattende metoder (f.eks. Moving Average eller enkel eksponensiell utglatning) mindre treffsikre, jf. kap. 6.1» (presisering).

**Vurdering:** Språket er presist og fagsterkt etter redigering.

## 2. Innholdsvurdering (per underkapittel)

### 3 Innledning
Utvidet med navigasjonskart over 3.1, 3.2 og 3.3.

### 3.1 Etterspørselsmønstre i distribusjonsleddet
- Firkomponent-dekomponering med Hyndman og Athanasopoulos (2021) som referanse.
- Lumpy demand-kriterium presisert: vi bruker CV som primærindikator fordi datasettet ikke har null-perioder mellom etterspørselshendelser; ADI fra Syntetos og Boylan er nevnt med begrunnelse for å forenkle.

### 3.2 Prognosemetoder for tidsserier
**Modellutvalg utvidet til fire nivåer**: Baselines, statistisk hovedmodell, ML-modeller, hybridmodeller (tidligere kun tre).

**Brukerens notater innarbeidet:**
- **MA-fordeler**: «MA er konseptuelt enkel, krever ingen parametriske antagelser utover vinduslengden $n$, er beregningsbillig og kommunikasjonseffektiv overfor operative brukere. Modellen er robust mot enkeltvise outliers og fungerer godt på stabile serier uten trend eller tydelig sesong.»
- **SARIMA/SARIMAX-presisering**: «I Scenario 1 brukes ren SARIMA, mens Scenario 2 utvider til SARIMAX ved å legge til kampanje- og hendelsesflagg som eksogene regressorer. Av leservennlighet brukes betegnelsen «SARIMA» som kortform gjennom rapporten.»
- **Ensemble — norsk forklaring**: «En ensemble-modell (kombinasjon av flere modeller der sluttprognosen er gjennomsnittet av enkeltmodellene)».

**Faglig styrking — referanser tilføyd:**
- Holt-Winters → Hyndman og Athanasopoulos (2021)
- SARIMA → Box og Jenkins (1976)
- Random Forest → Breiman (2001)
- Gradient Boosting → Friedman (2001)

**Strukturelle tilføyelser:**
- Lag-features og rolling means introdusert som teoretisk konsept: «ML-modellene benytter etterslepte verdier av tidsserien selv ($y_{t-1}, y_{t-5}, y_{t-10}$, kalt lag-features) og rullende gjennomsnitt (`rolling_mean_5`) som forklaringsvariabler».
- Hybridmodeller introdusert med Arunraj og Ahrens (2015) som referanse.

### 3.3 Måling av prognosepresisjon
Beste forankret underkapittel allerede før redigering. Fem feilmål (MAE, MAPE, sMAPE, WAPE, Bias) med korrekte formler og to litteraturreferanser (Hyndman & Koehler, 2006; Seiringer et al., 2024).

**Konsistens av fortegnskonvensjon**: MAE/MAPE/sMAPE/WAPE bruker $|A_t - F_t|$, Bias bruker $(F_t - A_t)$. «Positiv = overestimering» er korrekt.

## 3. Identifiserte svakheter (status: alle rettet)

### Faglige svakheter
- ✅ F1: Manglende referanser for SARIMA, HW, RF, GBM — Box & Jenkins, Breiman, Friedman, H&A tilføyd
- ✅ F2: Firkomponent uten kilde — H&A tilføyd
- ✅ F3: Forenklet lumpy demand-kriterium — presisert

### Strukturelle svakheter
- ✅ S1: Hybrid manglet i 3.2 — tilføyd som fjerde modellnivå
- ✅ S2: Lag-features uten teoretisk forklaring — tilføyd
- ✅ S3: Innledning uten navigasjonskart — utvidet

### Formidling
- ✅ K1: Overskriftskonvensjon
- ✅ K2: «Eventer» → «hendelser»
- ✅ K3: «logistikkfaglige» → «statistiske og metodiske»
- ✅ K4: «tradisjonelle prognosemetoder» presisert

## 4. Samsvar med prosjektplan og status

**Mot CLAUDE.md §3:** Kap. 3 forbereder modellvalg og evalueringskriterier som forventet. Litteraturforankring er nå solid etter tilføyelse av fire nye referanser.

**Konsistens med kap. 5.6, 6.2, 8.2:** Modellnavn og feilmål er konsistente. Bias-konvensjon konsistent på tvers av kapitlene.

## 5. Samlet vurdering kap. 3

Strukturelt godt komponert med tre tematiske underkapitler. Etter redigering har kapittelet fått solid faglig forankring av alle modellfamilier (fire nye primærreferanser) og konseptuell forberedelse av hybridmodeller og feature engineering. Brukerens notater (MA-fordeler, SARIMAX-presisering, ensemble-forklaring) er innarbeidet og styrker pedagogikken. Løftet fra «tynn lærebok-paraphrase» til «solid teoretisk fundament».

---

# Tverrgående endringer i rapporten

## Tankestreker fjernet i flytende tekst
Setningsbrytende tankestreker (« – », « — ») erstattet med passende tegnsetting (komma, punktum, kolon, parentes) på følgende linjer i rapportens flytende tekst:

| Kapittel | Linjenummer (omtrent) |
|---|---|
| 1.1 | 45 |
| 3.3 | 134 |
| 4.2 | 171 |
| 4.3 | 208, 233, 243 |
| 5.3 | 289 |
| 5.4 | 296 |
| 5.6 | 313–317 (definisjonsliste) |
| 6.2 | 331–344 (definisjonsliste) |
| 6.4 | 358 |
| 8.1 | 410 |
| 8.3 | 484, 489 |
| 8.4 | 519 |
| 9.1 | 527 |
| 9.2 | 542, 544 |
| 9.3 | 547, 555 |
| 9.4 | 562 |
| 9.5 | 571 |
| 9.6 | 583 |
| 10 | 601 |
| Vedlegg A1 | 648 |
| Vedlegg A8 | 764 |

## Beholdt som typografisk standard
- Datointervaller (f.eks. «mars 2025 – februar 2026»)
- Em-dash i overskrifter, tabell- og figurtitler
- Em-dash som beskrivelses-separator i filtreet (Vedlegg A7)
- Tankestrek som tabell-placeholder (Vedlegg A4)

## Forkastet leveranse: utvidet kampanjekalender
Dokumentert i kap. 9.6 (med generell faglig anbefaling) og kap. 10 (videre arbeid):
- **Kap. 9.6**: Reflekterer over at en mer detaljert kampanjekalenderfil med forventet volum, varighet per dag og prismetadata ble vurdert som leveranse, men forkastet pga. for tynt empirisk grunnlag (12 måneder, kun to Crazy Days-sykluser). Generell anbefaling om at slike kalendere bør bygges opp i operativt prognosearbeid med kampanjedrevet etterspørsel.
- **Kap. 10**: Punkt (i) i «videre arbeid» utvidet med formell kobling til en strukturert, flerårig kampanjekalender.

---

# Status og videre arbeid

**Gjennomført i denne sesjonen:**
- Kap. 1, 2, 3 grundig vurdert og redigert
- Bibliografi utvidet med 5 nye fagfellevurderte referanser
- Tankestreker som bryter setninger fjernet i flytende tekst
- Kampanjekalender-refleksjon dokumentert i kap. 9.6 og 10

**Ikke gjennomført ennå:**
- Review av kap. 4 (Casebeskrivelse), 5 (Metode), 6 (Modellering), 7 (Analyse), 8 (Resultater), 9 (Diskusjon — kun delvis berørt), 10 (Konklusjon — kun delvis berørt)
- Git-commit av sesjonens endringer
- Oppdatering av `012 fase 2 - plan/status.md`
- Eventuell fagfellevurdering (formell peer review)

**Anbefalt neste steg:**
1. Lese kap. 1–3 sammenhengende for å vurdere flyt etter alle redigeringer
2. Fortsette review av kap. 4 (Casebeskrivelse), evt. videre til kap. 5–10
3. Når review-runden er ferdig, samle alle endringer i én eller flere git-commits med tydelige meldinger
4. Oppdatere status.md
