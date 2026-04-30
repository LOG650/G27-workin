# Intern review av Prosjektrapport_LOG650_G27 — kap. 9 (Diskusjon)

**Dato:** 2026-04-30
**Reviewer:** Intern gjennomgang (Claude Code-assistert)
**Rapportfil:** `014 fase 4 - report/Prosjektrapport_LOG650_G27.md` (kap. 9, l. 585–651)
**Formål:** Strukturert kvalitetsvurdering av kap. 9 (Diskusjon) før peer review (M-05, 2026-05-01).

---

## Sammendrag og status

| Punkt | Status |
|---|---|
| Kap. 9 vurdert | Ja |
| Tiltak besluttet | Alle prioritet 1, 2 og 3-tiltak lukket 2026-04-30 (totalt 13 tiltak). Bonus-rettelse av kongruensfeil «et konkret anbefaling» → «en konkret anbefaling» i 9.2 l. 606. Avsnitt-etikettene i 9.6 ble konvertert til prosa-intro for konsistens med revidert kap. 6 og 7. |
| Forholdet til kap. 8-revisjon | Konsistent: kap. 9.2 bruker nå én desimal (46,0 → 29,4) for SARIMA-forbedringen, i tråd med Tabell 4b i kap. 8.3. |

**Hovedfunn:** Kapittelet leverer en grundig og faglig velforankret diskusjon i seks tematiske underkapitler (9.1–9.6) som dekker CLAUDE.md §3-kravene (tolkning, feilkilder, praktisk relevans). Tre forhold trekker likevel kvaliteten ned: (1) **fet skrift inne i løpende tekst** i fem underkapitler bryter med CLAUDE.md §1 (samme typografi-regel som er lukket i kap. 6, 7 og 8), (2) **flere tallreferanser uten kildehenvisning** (l. 591 «ERP-uttrekket», l. 613 «lag_1 = 84 %», l. 633 «median normalt salg på ca. 20 stk») mangler kryssreferanse til vedlegg eller tidligere kapitler, og (3) **én forvirrende parentes** i 9.5 l. 633 («27 dager av 42, ca. 90 % av året») kan misleses som påstand om at 27/42 = 90 %. I tillegg er antallet punktlister høyt sammenlignet med revidert kap. 6 og 7, hvilket kan vurderes konvertert til prosa for stilkonsistens.

---

## 1. Språkvurdering

**Styrker**
- Konsistent bruk av æ/ø/å og generelt godt akademisk fagspråk.
- Diskusjonen er strukturert tematisk og bygger systematisk på resultatene fra kap. 8.
- Eksplisitt kobling til litteratur ved fire steder (Hyndman & Koehler, 2006; Trapero et al., 2015; Seiringer et al., 2024; Fildes et al., 2009) — i tråd med CLAUDE.md §2.
- Kobling tilbake til problemstillingens delproblem 3 (informasjonsdeling) er tydelig i 9.2.
- Fagterminologi (residual, autokorrelasjon, walk-forward, AIC, sesongdifferensiering) brukes korrekt og konsekvent.

**Svakheter**
- **Fet skrift inni løpende tekst** brukes i flere underkapitler:
  - L. 591: «**kryssjekk mot uavhengige datakilder er essensielt i prognosearbeid**»
  - L. 599: «viser en **nyansert** effekt av informasjonsdeling»
  - L. 606: «**binære kampanjeindikatorer er ikke nok**»
  - L. 615: «**modellvalg bør styres av segmentet man prognoserer for**»
  - L. 626: «**terskelbasert routing forbedrer toppdager på bekostning av noen normale dager**»
  - L. 645: «**segmenterte analysen i kap. 8.3 er rapportens primære lens**»
  
  Disse bryter med CLAUDE.md §1 (typografi-regelen innført 2026-04-30). Samme type rettelse som ble gjort i kap. 6, 7 og 8.
- **Avsnitt-etiketter i 9.6** («**Testsettets sammensetning.**», «**Fravær av walk-forward-validering.**», «**Risiko for overdifferensiering i SARIMA.**», «**Forkastet leveranse: utvidet kampanjekalender.**») er fet skrift som mini-overskrift inne i avsnitt. Per CLAUDE.md §1 er fet skrift «forbeholdt overskrifter, og kan unntaksvis brukes som etikett i tabeller eller liste-elementer». Avsnitt-etiketter er en grenseboks; alternativet er å heve dem til ekte underoverskrifter (f.eks. ### 9.6.1 Testsettets sammensetning) eller fjerne fet og introdusere temaet i prosa. Dette bør avgjøres bevisst.
- **Engelsk uttrykk i sitatform (l. 601):** «"mental pause"» er en muntlig parafrase av modellatferd. Bør enten parafreseres til norsk eller fjernes; akademisk standard tilsier ren norsk i diskusjon.
- **Anglisisme med oversettelse (l. 624, 626):** «"false positive"-routinger (feilaktig positive)» og «Tradeoff-en (avveiningen)». Bedre å bruke ren norsk: «falske positive routinger» og «Avveiningen».
- **Forvirrende formulering (l. 633):** «I normaldrift (27 dager av 42, ca. 90 % av året)» kan misleses som påstand om at 27/42 = 90 %, men 27/42 = 64,3 %. Setningen forsøker å skille mellom *testperiodens* fordeling (27/42 = 64 %) og et *representativt års* fordeling (~90 % normaldrift). Dette må presiseres.
- **Tallinkonsistens med kap. 8.3 (l. 601):** «MAE reduseres fra 45,97 (S1) til 29,40 (S2), en nedgang på 36 %» bruker to desimaler, mens kap. 8.3 (etter revisjon 2026-04-30) og Tabell 4b nå bruker én desimal (46,0 → 29,4). Konsistent presisjon på tvers av kapitler styrker leseflyten.
- **Rikelig bruk av punktlister** (seks underkapitler inneholder til sammen 17 punkter på korte avsnitt). Per stilkonsistens med revidert kap. 6 og kap. 7 kan utvalgte punktlister konverteres til prosa, særlig der antallet punkter er ≤ 3.

---

## 2. Innholdsvurdering (per delkapittel)

### 9.1 Datakvalitet og metodisk erfaring (l. 588–596)

**Observasjon:** Tre faktiske forhold dokumentert: (1) datafeil i opprinnelig vaskeskript (undertelling ~70 %), (2) verifikasjon mot RELEX-eksport og ERP-uttrekk (≤ 0,6 % avvik), (3) tre metodiske justeringer (sesongsyklus 7 → 5, sMAPE/WAPE som supplement, Ljung-Box som residualtest).

**Vurdering:**
- **Sterk metodisk refleksjon.** Ærlig dokumentasjon av datafeil er en akademisk styrke og gir leseren tillit til de verifiserte tallene.
- **«ERP-uttrekket» (l. 591) mangler referanse.** Det er ikke klart fra kap. 9.1 alene om ERP-uttrekket er omtalt i kap. 4 eller vedlegg. En kryssreferanse «(jf. kap. 4.2)» eller lignende ville styrket sporbarheten.
- **Hyndman og Koehler (2006)-sitatet (l. 595)** plassert riktig — knyttet til konkret observasjon (MAPE 2 973 %).
- **«Robuste evalueringsmål» (l. 595)** — uttrykket er presist, men siden disse målene allerede er innført i kap. 5.3 og 8.2, kunne 9.1 ha en kort kryssreferanse «(jf. kap. 5.3 for definisjon)».

### 9.2 Verdien av informasjonsdeling (Scenario 1 vs 2) (l. 598–606)

**Observasjon:** Fire punkter dokumenterer Scenario 1 vs 2-effekt per modell og segment. Kobling til Trapero et al. (2015) og normativ anbefaling om rikere kampanjerepresentasjon.

**Vurdering:**
- **Eksplisitt svar på delproblem 3** fra problemstillingen — sterk kobling til proposal.
- **Tallkonsistens (l. 601):** 45,97 / 29,40 (to desimaler) bryter med kap. 8.3 og Tabell 4b (én desimal). Bør harmoniseres til 46,0 / 29,4 i prosa.
- **«Mental pause» (l. 601)** er muntlig og uakademisk i en diskusjon. Bør parafreseres: «kampanjeflagget gir SARIMA et signal om å suspendere ren historisk inferens på de markerte dagene, slik at modellen kan fokusere på det stabile sesongmønsteret de øvrige dagene».
- **Kobling til Trapero et al. (2015) (l. 606)** er presis og legger til et nyanserende funn («binære kampanjeindikatorer er ikke nok»). God akademisk forankring.
- **«Konkret anbefaling for videre arbeid» (l. 606)** — bra, men kunne med fordel også være eksplisitt referert i kap. 10 (Konklusjon) for symmetri.

### 9.3 Modellenes komplementære roller (l. 608–617)

**Observasjon:** Tre punkter beskriver SARIMA, RF uten lag_1 og opprinnelig RF. Knyttes til feature importance (lag_1 = 84 %) og residualdiagnostikk (Q-statistikker fra Tabell 5).

**Vurdering:**
- **Pedagogisk velvalgt forklaring** av hvorfor RF uten lag_1 er bedre på toppdager enn full RF (lag_1-dominans gjør modellen «i morgen = i dag»).
- **«lag_1 = 84 %» (l. 613)** mangler kryssreferanse til vedlegg A4 (feature importance-tabellen). Tallet er spesifikt og bør være etterprøvbart.
- **Residualdiagnostikk-tolking (l. 617)** er innsiktsfull: skiller mellom «optimal parametrisk» (SARIMA innen lineære antagelser) og «mer informasjonsekstraksjon» (RF uten lag_1). Dette er sofistikert metodisk drøfting.
- **Anbefaling om segmentstyrt modellvalg** binder godt til kap. 9.5.

### 9.4 Hybridenes routing-utfordring (l. 619–628)

**Observasjon:** To hybridvarianter beskrevet (kampanjebasert og terskelbasert), med MAE-tall fra Tabell 3/4 og Tabell 5. Diskusjon av routing-tradeoff og operasjonell preferanse for terskelbasert hybrid.

**Vurdering:**
- **Tydelig forklaring** av hvorfor kampanjebasert hybrid feiler på toppdager (toppdager utenfor kampanjeperioder, f.eks. mandag etter nyttår).
- **Tallene stemmer** mot Tabell 3 og Tabell 4 (MAE 305 / +6,6 / 290 / 104 / 29 alle verifisert).
- **«MAE 445 mot RF uten lag_1 alene på 290» (l. 624)** — 445 er hentet fra `scenario_sammendrag.csv` rad 42 (Hybrid kampanje toppdager: 444,5). Riktig, men avrunding kunne være mer eksplisitt («ca. 445» eller «445» med fotnotereferanse til CSV).
- **Routing-tradeoff drøftes godt** (l. 626) — klassisk klassifikator-perspektiv. Setningen bruker imidlertid fet skrift inne i løpende tekst (P1).
- **Seiringer et al. (2024) (l. 628)** binder bias-skjevhet til sikkerhetslagerkostnader — samme sitering som i 8.3 l. 538. Konsistent og velforankret.

### 9.5 Praktiske implikasjoner for REMA 1000 (l. 630–641)

**Observasjon:** Kobling til REMA 1000s ordreprosess (kap. 4.1, AOF/RELEX 100 % aksept). Konkret anbefaling med tre punkter (daglig volumbestilling, kampanje-/høytidsplanlegging, månedlig kapasitetsplanlegging). Fildes et al. (2009)-sitering for menneskelige overstyringer.

**Vurdering:**
- **Sterk operasjonell forankring** — koblingen til AOF/RELEX-prosessen gjør anbefalingene relevante for REMA.
- **Forvirrende parentes (l. 633):** «I normaldrift (27 dager av 42, ca. 90 % av året)» kan misleses som «27/42 = 90 %», men faktisk er 27/42 = 64 %. Setningen forsøker å si «testperioden hadde 27 normaldager av 42, mens et representativt år har ~90 % normaldrift». Bør omformuleres for klarhet.
- **«median normalt salg på ca. 20 stk» (l. 633)** mangler kildereferanse. Hvor i kap. 4 eller 8 er dette dokumentert? Kunne vises som vedlegg eller med kryssreferanse.
- **«typisk 15–20 %» feilmargin (l. 634)** — RF uten lag_1 har MAPE 61,96 % og sMAPE 66,72 % på toppdager (`scenario_sammendrag.csv` rad 40), så «15–20 %» er en optimistisk avrunding av MAE/volum-ratio. Med MAE 290 og volum 1 000–2 000 stk gir dette 14,5–29 % relativ feil; intervallet bør justeres til «typisk 15–30 %».
- **Numerert anbefaling (l. 636–639)** er pedagogisk klar og operasjonelt nyttig.
- **Fildes et al. (2009) (l. 641)** velvalgt sitering — knytter manuell overstyring til pensumlitteratur.

### 9.6 Metodiske begrensninger (l. 643–651)

**Observasjon:** Fire begrensninger drøftet: (1) testsettets sammensetning (15/42 toppdager = 36 %), (2) fravær av walk-forward-validering (83/17-split), (3) risiko for overdifferensiering i SARIMA (d=1, D=1 valgt av AIC tross stasjonær serie), (4) forkastet leveranse — utvidet kampanjekalender med begrunnelse.

**Vurdering:**
- **Akademisk modent kapittel** — anerkjenner svakheter i designet uten å undergrave hovedfunnene.
- **Walk-forward-anbefalingen (l. 647)** er presist formulert og henvises til kap. 10. Bra.
- **Overdifferensiering-drøftingen (l. 649)** er teknisk dyptpløyende: ADF p < 0,001 vs AIC-valg av d=1, D=1, og kobling til |Bias|=MAE-funnet i 8.3. Imidlertid mangler in-tekst-sitering for ARIMA-overdifferensieringsrisikoen — Box & Jenkins (1976) eller Hyndman & Athanasopoulos (2021) ville styrket faglig forankring.
- **«Forkastet leveranse» (l. 651)** er en sjelden men nyttig akademisk øvelse — eksplisitt dokumentasjon av hva som ble vurdert og forkastet, med begrunnelse. Dette løfter etterprøvbarheten og viser metodisk modenhet.
- **Avsnitt-etiketter i fet skrift** — diskutert under språkvurdering (S2).

### Tverrgående: figurer, tabeller og kryssreferanser

**Observasjon:** Kap. 9 inneholder ingen egne figurer eller tabeller. Henvises til Tabell 3/4/5 i kap. 8 og vedlegg A1, A4 indirekte.

**Vurdering:**
- For et diskusjonskapittel er fravær av egne illustrasjoner forventet og akseptabelt.
- **Kryssreferanser kunne vært sterkere:** kap. 9.3 (l. 613) refererer til lag_1 = 84 % uten henvisning til vedlegg A4; kap. 9.5 (l. 633) refererer til median uten kryssreferanse. Kap. 9.6 (l. 649) refererer til ADF (kap. 7.1) korrekt og til Tabell A1 — bra.

---

## 3. Identifiserte svakheter (med tiltakskoder)

### Faglige
- **F1:** L. 591 — «ERP-uttrekket» mangler kryssreferanse til kap. 4 eller vedlegg der ERP-uttrekket er beskrevet. **Status: lukket 2026-04-30** — «(jf. kap. 4.3, datakildekontrolltabell)» tilføyd.
- **F2:** L. 613 — «lag_1 = 84 %» mangler kryssreferanse til vedlegg A4 (feature importance). **Status: lukket 2026-04-30** — «(lag_1 = 84 %, jf. vedlegg A4)» tilføyd.
- **F3:** L. 633 — «median normalt salg på ca. 20 stk» mangler kryssreferanse til kap. 4 eller 8 der medianen er dokumentert. **Status: lukket 2026-04-30** — «(jf. kap. 4.3)» tilføyd; medianen er dokumentert i kap. 4.3 (Medianen 20 stk vs gjennomsnittet 79,6).
- **F4:** L. 649 — Overdifferensiering-drøftingen mangler in-tekst-sitering (Box & Jenkins, 1976 eller Hyndman & Athanasopoulos, 2021). **Status: lukket 2026-04-30** — Hyndman & Athanasopoulos (2021) lagt til som in-tekst-sitering ved underestimerings-tolkningen.

### Metodiske
- **M1:** L. 633 — Forvirrende parentes «(27 dager av 42, ca. 90 % av året)» kan misleses som «27/42 = 90 %». Bør omformuleres for å skille testperiodens fordeling fra et representativt års fordeling. **Status: lukket 2026-04-30.**
- **M2:** L. 634 — «typisk 15–20 %» feilmargin på toppdager er en optimistisk avrunding. Faktisk MAE 290 / volum 1 000–2 000 stk = 14,5–29 % relativ feil; intervallet bør justeres til 15–30 % eller suppleres med sMAPE-tall. **Status: lukket 2026-04-30.**
- **M3:** L. 601 — Tallinkonsistens med kap. 8.3 (45,97 / 29,40 vs 46,0 / 29,4). Bør harmoniseres til én desimal for konsistens. **Status: lukket 2026-04-30.**

### Strukturelle
- **S1:** Kap. 9.6 — Avsnitt-etiketter i fet skrift («**Testsettets sammensetning.**» osv.) er på grensen til CLAUDE.md §1. Kan enten heves til ### 9.6.1-underoverskrifter eller fjernes med tema-introduksjon i prosa. **Status: lukket 2026-04-30** — alle fire avsnitt-etiketter konvertert til prosa-intro («Den første begrensningen gjelder …», «En andre begrensning er …», «En tredje vurdering knytter seg til …», «En siste betraktning er …»), i tråd med revidert kap. 6 og 7.
- **S2:** Punktlister i 9.2 (4 pkt), 9.3 (3 pkt), 9.4 (2 pkt), 9.5 (2 + 3 pkt) kan vurderes konvertert til prosa for konsistens med revidert kap. 6 og kap. 7, særlig der antall punkter ≤ 3. **Status: lukket 2026-04-30** — punktlistene i 9.4 (2 pkt om hybridvarianter) og første del av 9.5 (2 pkt om normaldrift / toppdager) konvertert til prosa. Punktlistene i 9.1, 9.2, 9.3 og den numererte anbefalingen i 9.5 beholdt fordi antall punkter er ≥ 3 og strukturen styrker oversikten.
- **S3:** Sluttsetning i 9.6 mangler eksplisitt bro til kap. 10 (Konklusjon). En oppsummerende setning som «Disse begrensningene leder til de tre videre arbeidsanbefalingene i kap. 10.» ville styrket flyt. **Status: lukket 2026-04-30** — sluttsetning «Disse begrensningene danner grunnlaget for anbefalingene om videre arbeid i kap. 10.» lagt til etter 9.6-avsnittene.

### Formidling
- **P1:** L. 591, 599, 606, 615, 626, 645 — Fet skrift inne i løpende tekst (seks forekomster). Bryter med CLAUDE.md §1. Samme type rettelse som ble gjort i kap. 6, 7 og 8. **Status: lukket 2026-04-30.**
- **P2:** L. 601 — «"mental pause"» er muntlig anglisisme i sitatform; bør parafreseres til ren norsk akademisk uttrykk. **Status: lukket 2026-04-30.**
- **P3:** L. 624 («"false positive"-routinger (feilaktig positive)») og l. 626 («Tradeoff-en (avveiningen)») — anglisismer med oversettelse i parentes. Bytt til ren norsk. **Status: lukket 2026-04-30.**
- **P4:** L. 624 — «MAE 445» refererer til Hybrid kampanje toppdager fra `scenario_sammendrag.csv`. Tallet er korrekt avrundet (444,5 → 445), men kunne kontekstualiseres bedre. **Status: vurdert ikke gjennomført 2026-04-30** — å legge til source-parentes kun for «MAE 445» ville bryte konsistensen med øvrige tallreferanser i kap. 9 (alle MAE-verdier står uten source-parentes; data-provenance er etablert i kap. 8 l. 458).

---

## 4. Forbedringsforslag

| ID | Forslag |
|---|---|
| F1 | I 9.1 l. 591, tilføy «(jf. kap. 4.2 for ERP-uttrekket og dets dekning)» eller lignende kryssreferanse. |
| F2 | I 9.3 l. 613, tilføy «(jf. vedlegg A4 for feature importance-rangeringen)» etter «lag_1 = 84 %». |
| F3 | I 9.5 l. 633, tilføy «(jf. kap. 4.3 / kap. 8 for normaldagsfordeling)» etter «median normalt salg på ca. 20 stk». |
| F4 | I 9.6 l. 649, tilføy «(Hyndman & Athanasopoulos, 2021)» eller «(Box & Jenkins, 1976)» som forankring av overdifferensieringsrisikoen. |
| M1 | Omformuler 9.5 l. 633 til: «I normaldrift, som utgjør 27 av 42 testdager (i et representativt år ca. 90 % av dagene), gir SARIMA en MAE på 29 stk.» |
| M2 | Endre l. 634 fra «typisk 15–20 %» til «typisk 15–30 % relativ feil» (alternativt: «sMAPE rundt 67 % på toppdager, jf. Tabell 3»). |
| M3 | I 9.2 l. 601, endre «MAE reduseres fra 45,97 (S1) til 29,40 (S2)» til «MAE reduseres fra 46,0 (S1) til 29,4 (S2)» for konsistens med kap. 8.3 og Tabell 4b. |
| S1 | I 9.6, vurder å heve avsnitt-etikettene til ### 9.6.1 Testsettets sammensetning, ### 9.6.2 Fravær av walk-forward-validering, osv. — alternativt fjerne fet og introdusere temaet med løpende setning. |
| S2 | Vurder å konvertere punktlister med ≤ 3 punkter i 9.4 (l. 619–622) og 9.5 (l. 632–634) til prosa. Lengre lister (9.2 og 9.3) kan beholdes for klarhet. |
| S3 | Tilføy avsluttende setning i 9.6 (etter l. 651): «Disse begrensningene danner grunnlaget for anbefalingene om videre arbeid i kap. 10.» |
| P1 | Fjern fet skrift i l. 591, 599, 606, 615, 626, 645 (seks forekomster). |
| P2 | Endre l. 601 fra «"mental pause"» til en ren norsk parafrase: «kampanjeflagget gir modellen et signal om at den kan suspendere ren historisk inferens på markerte dager, slik at sesongmønsteret på de øvrige dagene blir tydeligere». |
| P3 | I l. 624, endre «"false positive"-routinger (feilaktig positive)» til «falske positive routinger». I l. 626, endre «Tradeoff-en (avveiningen)» til «Avveiningen». |
| P4 | I l. 624, kontekstualiser «MAE 445» med en parentes: «MAE 445 stk (fra `scenario_sammendrag.csv`)» — alternativt henvise til vedlegg dersom Hybrid (kampanje) toppdager-tallet skal eksponeres formelt. |

---

## 5. Samsvar med prosjektplan og status

**Mot proposal (`011 fase 1 - proposal/proposal.md`):** Problemstillingens delproblem 3 («i hvilken grad kampanjeaktivitet begrenser modellenes presisjon») besvares eksplisitt i 9.2. Hovedproblemstillingen om prognosepresisjon adresseres gjennom 9.3 (segmentert vinnerstruktur) og 9.5 (operasjonelle anbefalinger). Ingen avvik mot proposal.

**Mot status.md:** Status av 2026-04-30 sier «| 9 Diskusjon | 90 % | 9.1–9.4; mangler konkrete implementeringsanbefalinger (ryddes etter peer review) |». Reviewen viser at 9.5 (Praktiske implikasjoner) og 9.6 (Metodiske begrensninger) faktisk er på plass i tillegg til de fire underkapitlene status.md nevner. Status.md bør oppdateres til å reflektere at alle seks underkapitler (9.1–9.6) er ferdige, og at «konkrete implementeringsanbefalinger» faktisk er levert i 9.5.

**Mot WBS / kritisk linje:** Kap. 9 er en del av ACT-09 (Skriving av metode og resultat). Diskusjonsdelen er en kritisk leveranse for den akademiske helheten og er nå godt på vei. Ingen avvik.

**Mot CLAUDE.md §3 — Diskusjon:**

| Krav i CLAUDE.md §3 | Dekket | Hvor i kap. 9 | Kommentar |
|---|---|---|---|
| Tolkning av resultater | Ja | 9.2, 9.3, 9.4 | Detaljert tolkning per modellklasse og segment |
| Feilkilder | Ja | 9.1, 9.6 | Datafeil, walk-forward-mangel, overdifferensiering — ærlig fremstilt |
| Praktisk relevans | Ja | 9.5 | Konkrete operasjonelle anbefalinger til REMA |

**Mot CLAUDE.md §1 (typografi-regelen 2026-04-30):**
- Fet skrift inne i løpende tekst: seks forekomster (P1).
- Tankestrek til setningsoppdeling: ikke observert i kap. 9 (godt).

**Mot CLAUDE.md §2 (kobling til teori):**
- Hyndman & Koehler (2006) i 9.1 — god forankring.
- Trapero et al. (2015) i 9.2 — god forankring av kampanjekalender-tema.
- Seiringer et al. (2024) i 9.4 — god forankring av bias-skjevhet vs sikkerhetslager.
- Fildes et al. (2009) i 9.5 — god forankring av menneskelig overstyring.
- Manglende sitering i 9.6 (overdifferensiering): F4.

**Mot CLAUDE.md §6 (skille casebeskrivelse / metode / analyse / resultater):**
- Diskusjonen holder seg pent på *tolkning* og *implikasjoner*, ikke på *resultatpresentasjon*. Skillet til kap. 8 er respektert.

**Mot CLAUDE.md §9 (begrunnelse, etterprøvbarhet, rød tråd):**
- Begrunnelser er gjennomgående faglige.
- Etterprøvbarhet styrkes ved kryssreferanser til Tabell 3, 4, 5 og vedlegg A1; svekkes svakt av manglende kryssreferanse for «lag_1 = 84 %» (F2) og «median ca. 20 stk» (F3).
- Rød tråd fra problemstilling → resultater → diskusjon er sterk.

---

## 6. Prioritert tiltaksliste

| Prioritet | Tiltak | Kapittel/linje | Estimert innsats |
|---|---|---|---|
| 1 | Fjern fet skrift inne i løpende tekst (P1) | 9.1, 9.2, 9.3, 9.4, 9.6 | 5 min |
| 1 | Omformuler forvirrende parentes om 27/42 vs 90 % (M1) | 9.5, l. 633 | 3 min |
| 1 | Harmoniser tall 45,97 → 46,0 og 29,40 → 29,4 (M3) | 9.2, l. 601 | 2 min |
| 1 | Erstatt «"mental pause"» med ren norsk parafrase (P2) | 9.2, l. 601 | 5 min |
| 2 | Tilføy kryssreferanse til vedlegg A4 for «lag_1 = 84 %» (F2) | 9.3, l. 613 | 2 min |
| 2 | Tilføy kryssreferanse for «median normalt salg ca. 20 stk» (F3) | 9.5, l. 633 | 2 min |
| 2 | Tilføy kryssreferanse til kap. 4 for «ERP-uttrekket» (F1) | 9.1, l. 591 | 2 min |
| 2 | Korriger optimistisk feilmargin «typisk 15–20 %» til «15–30 %» (M2) | 9.5, l. 634 | 3 min |
| 2 | Bytt anglisismer til ren norsk (P3) | 9.4, l. 624, 626 | 3 min |
| 3 | Tilføy in-tekst-sitering for overdifferensieringsdrøfting (F4) | 9.6, l. 649 | 2 min |
| 3 | Vurder ### 9.6.1–9.6.4 underoverskrifter eller fjerne fet (S1) | 9.6 | 5–10 min |
| 3 | Vurder konvertering av korte punktlister til prosa (S2) | 9.4, 9.5 | 10–15 min |
| 3 | Tilføy bro-setning fra 9.6 til kap. 10 (S3) | 9.6 etter l. 651 | 2 min |

**Sum estimert innsats:**
- Prioritet 1: ca. 15 min (kritisk for innlevering — typografi, klarhet og tallkonsistens).
- Prioritet 2: ca. 15 min (viktig for kvalitet — kryssreferanser og presisjon).
- Prioritet 3: ca. 25 min (ønskelig polering — strukturvalg).
- **Totalt: ca. 55 min** for full lukking.

---

## 7. Samlet vurdering

Kap. 9 er substansielt og faglig velforankret. De seks underkapitlene (9.1 datakvalitet, 9.2 informasjonsdeling, 9.3 komplementære roller, 9.4 hybridrouting, 9.5 praktiske implikasjoner, 9.6 metodiske begrensninger) dekker CLAUDE.md §3-kravene fullt ut og leverer en moden akademisk diskusjon med eksplisitte koblinger til problemstillingens delproblem 3 og fire pensumkilder (Hyndman & Koehler, Trapero, Seiringer, Fildes). Den ærlige fremstillingen av datafeil i 9.1 og forkastet leveranse i 9.6 viser metodisk modenhet og styrker rapportens troverdighet. Den operasjonelle anbefalingen i 9.5 (segmentstyrt modellvalg) er konkret og direkte anvendelig for REMA 1000.

Tre forhold trekker kvaliteten ned. For det første **fet skrift inne i løpende tekst** (seks forekomster i 9.1, 9.2, 9.3, 9.4, 9.6) bryter med typografi-regelen som ble lukket i kap. 6, 7 og 8 — dette er en triviell men nødvendig opprettelse for konsistens. For det andre **flere tallreferanser uten kildehenvisning** (ERP-uttrekket, lag_1 = 84 %, median ca. 20 stk) svekker etterprøvbarheten og bryter med CLAUDE.md §9. For det tredje er det **én forvirrende parentes** i 9.5 l. 633 («27 dager av 42, ca. 90 % av året») som kan misleses som påstand om at 27/42 = 90 %. I tillegg er en tall-inkonsistens med kap. 8.3 (45,97/29,40 vs 46,0/29,4) en mindre, men synlig friksjon for leseren.

Ingen av tiltakene er tunge: prioritet 1-listen kan lukkes på ca. 15 min, og full lukking inkludert strukturpolering tar omtrent 55 min. Kvalitetsnivået er **øvre middels for LOG650-standard**, og med prioritet 1- og prioritet 2-tiltakene gjennomført vil kapittelet holde et sterkt akademisk nivå og være klart for peer review M-05.

---

## 8. Oppfølgingssaker (for vurdering)

- **Status.md-oppdatering:** Linje 157 («| 9 Diskusjon | 90 % | 9.1–9.4; mangler konkrete implementeringsanbefalinger (ryddes etter peer review) |») er utdatert. Alle seks underkapitler er på plass, og 9.5 leverer konkrete implementeringsanbefalinger. Bør endres til «Ferdig | 9.1–9.6 inkl. praktiske implikasjoner og metodiske begrensninger».
- **Symmetri med kap. 10:** Anbefalingen om rikere kampanjerepresentasjon (9.2 l. 606), walk-forward-validering (9.6 l. 647) og parsimonisk SARIMA (9.6 l. 649) bør gjenfinnes i kap. 10 (Konklusjon, videre arbeid). Krysshenvis med kap. 10 etter behov.
- **Vedlegg A4-konsistens:** Hvis F2-tiltaket (lag_1 = 84 %-kryssreferanse) implementeres, sjekk at vedlegg A4 faktisk inneholder feature importance-tabellen med dette tallet.
- **Konsistensjekk på tvers av kap. 8 og 9:** I forbindelse med tallrydding 2026-04-30 ble flere tabelltall i kap. 8 endret til én desimal. Verifiser at alle tallreferanser i kap. 9 (særlig 9.2 og 9.4) bruker samme presisjon som motsvarende tabeller i kap. 8.

---

*Generert 2026-04-30 som del av intern review-prosess før peer review M-05 (2026-05-01).*
