# Intern review av Prosjektrapport_LOG650_G27 — kap. 7 (Analyse)

**Dato:** 2026-04-30
**Reviewer:** Intern gjennomgang (Claude Code-assistert)
**Rapportfil:** `014 fase 4 - report/Prosjektrapport_LOG650_G27.md` (kap. 7, l. 414–444)
**Formål:** Strukturert kvalitetsvurdering av kap. 7 (Analyse) før peer review (M-05, 2026-05-01).

---

## Sammendrag og status

| Punkt | Status |
|---|---|
| Kap. 7 vurdert | Ja |
| Tiltak besluttet | Alle prioritet 1 og 2-tiltak lukket 2026-04-30. Bonus-rettelse av faktisk feil i ACF-omtale i 7.1 (sterke topper ved lag 5/10/15 stemte ikke med dataene; rå serie er AR(1)-dominert). |
| Forholdet til kap. 6-revisjon | Inkonsistens 208/218 nå rettet i 7.3; P90-grunnlag flyttet til 218 (terskel 70,6) for konsistens på tvers av rapporten. |

**Hovedfunn:** Kapittelet er teknisk dekkende og dokumenterer alle fire delkapitler i tråd med CLAUDE.md §11 (stasjonaritet, parametersøk, estimering/segmentering, residualdiagnostikk). Tre forhold trekker likevel kvaliteten ned: (1) en **faktisk inkonsistens** med kap. 5.5 og revidert kap. 6 om treningssettets størrelse (208 vs 218 virkedager), (2) **manglende in-tekst-sitater** for ADF-test (Dickey & Fuller, 1979), Ljung-Box-test (Ljung & Box, 1978) og ARIMA-rammeverket (Box & Jenkins, 1976) der testene faktisk anvendes, og (3) at **ACF-plottet av treningsserien** omtalt i 7.1 ikke er vist som figur — kun ACF-plottet av residualene (Figur 6) eksisterer, og det ligger først i kap. 8.3.

---

## 1. Språkvurdering

**Styrker**
- Konsistent bruk av æ/ø/å og generelt godt akademisk fagspråk.
- Konkrete tall (AIC, andel av varians, persentilterskel) gjør analysen etterprøvbar.
- Norsk tallformat (tusenskille med hardt mellomrom, komma som desimaltegn) er i hovedsak fulgt.

**Svakheter**
- **Fet skrift inni løpende tekst (l. 432, 444):** «evalueres modellene **segmentert** basert på …» og «I tillegg analyseres **systematisk bias** per segment …» bryter med CLAUDE.md §1 (typografi-regelen som ble innført 2026-04-30). Fet skrift i kap. 7 brukes ellers konsistent som *label* foran kolon (f.eks. «**SARIMA grid-search:**»), noe som er akseptabelt etter den nye regelen, men de to tilfellene over er fet skrift inne i løpende tekst og må endres.
- **Inkonsistent talluttrykk (l. 423):** «AIC 2 510,06» har to desimaler, mens «AIC 2 558» rett ved siden av er rundet til hele tall. Begge bør ha samme presisjon (forslag: rund konsekvent til hele AIC-poeng, evt. én desimal).
- **Engelsk fagterm uten parafrase (l. 442):** «(10 lags)» — termen «lag» er innarbeidet, men i 7.4 blir den brukt to ganger uten kort norsk forklaring. Forslag: «(ti etterslep / lags)» ved første bruk, eller en kort henvisning til 7.1 der lag-begrepet allerede er introdusert.
- **Passive konstruksjoner (l. 420, 432):** «ACF-plott av treningsserien viste sterke topper …», «evalueres modellene segmentert». OK i et metodekapittel, men kan strammes ved aktiv form der det er naturlig.
- **Forkortelse uten ekspansjon (l. 423):** «MLE-optimeringen ikke konvergerte» — MLE (Maximum Likelihood Estimation) blir ikke ekspandert ved første bruk i kap. 7. Antas kjent fra kap. 5/6, men minst én parafrase i parentes ville lette leseren.

---

## 2. Innholdsvurdering (per delkapittel)

### 7.1 Stasjonaritet og ACF-vurdering (l. 417–420)

**Observasjon:** ADF-test rapportert med p < 0,001 for tre serie-varianter. ACF-plott omtalt verbalt ved sterke topper på lag 5, 10 og 15.

**Vurdering:**
- **ADF-testen mangler in-tekst-sitering.** Dickey & Fuller (1979) er sitert i kap. 5.2 (l. 297) men er ikke gjentatt i 7.1, der testen faktisk anvendes. CLAUDE.md §2 tilsier at sitatet skal følge anvendelsen.
- **ACF-plottet av treningsserien er ikke vist.** 7.1 omtaler ACF-toppene som om plottet er kjent for leseren, men det finnes ikke som figur i rapporten. Den eneste ACF-figuren er Figur 6 (residualer) i kap. 8.3. CLAUDE.md §7 («Aktiv bruk … visualisere mønstre») og kap. 11-føringene for kap. 4 («grafer over tid») skulle tilsi at trenings-ACF-plottet vises eksplisitt, evt. som Figur 5 før modelleringen begynner. Dette er en pedagogisk svakhet: leser må stole på vår tekst i stedet for å se mønsteret selv.
- **Sammenheng mellom ADF og ACF:** 7.1 skiller ikke tydelig mellom *enhetsrot-test* (ADF, om serien har stokastisk trend) og *autokorrelasjonsstruktur* (ACF, om observasjoner avhenger av tidligere). En setning som binder de to testene sammen ville gjort delkapittelet mer pedagogisk.

### 7.2 Parametersøk og tuning (l. 422–427)

**Observasjon:** Tre tuningsanalyser dokumentert: SARIMA grid-search (144 kombinasjoner), RF feature importance og GBM hyperparameter-tuning (16 kombinasjoner × 3-fold TimeSeriesSplit). Henvisninger til vedlegg A2/A3/A4.

**Vurdering:**
- **«Ca. 30 % bedre MAE enn utunet standard-konfigurasjon» (l. 427)** er en konkret påstand som mangler tabell- eller vedleggsreferanse. Hva er «utunet standard-konfigurasjon»? Sklearn-defaults (`learning_rate=0,1`, `max_depth=3`, `n_estimators=100`)? Tallet bør enten dokumenteres med et MAE-par (utunet vs tunet) eller henvises til vedlegg A3.
- **«Den opprinnelige $(1,1,1)(1,1,1)_7$» (l. 423)** kommer uten kontekst. Leseren forventer å forstå hvorfor det er en «opprinnelig» modell. Dette er den modellen som ble brukt før virkedagskorrigeringen i kap. 9.1 (overgangen fra $s=7$ til $s=5$), og koblingen bør gjøres eksplisitt med en kryssreferanse.
- **Box & Jenkins (1976)** er sitert i kap. 5.2 og kap. 6.2, men ikke i 7.2 der grid-søket faktisk gjennomføres. Mindre kritisk enn for ADF/Ljung-Box, fordi rammeverket allerede er etablert i kap. 5–6, men en kort henvisning ville styrket den røde tråden.
- **MLE-konvergensvurdering** er metodisk korrekt, men kan virke teknisk uten en kort forklaring av hvorfor ikke-konvergens kvalifiserer for kassasjon (parametre er ikke pålitelig estimert; AIC er da ikke meningsfullt). Én setning ville løftet pedagogikken.
- **Feature importance-tallene** er konsistente med vedlegg A4. Sjekkpunkt OK.

### 7.3 Estimering og segmentering (l. 429–436)

**Observasjon:** «Modellene trenes på 208 virkedager (mars–desember 2025) og evalueres på 42 virkedager». 90.-persentilterskel på 69,3 stk brukes for segmentering, og 27/15-fordelingen i testsettet rapporteres.

**Vurdering:**
- **Faktisk inkonsistens med kap. 5.5 og revidert kap. 6.0.** Kap. 5.5 (l. 318) sier «Treningssett … 218 virkedager» for SARIMA og baselines, og 208 dager kun for ML-modeller etter lag-padding. Revidert kap. 6.0 (l. 354) sier eksplisitt «218 virkedager (208 for maskinlæringsmodellene)». 7.3 sier udifferensiert «208 virkedager», hvilket er feil for SARIMA, Holt-Winters og Seasonal Naive. Dette er **samme feil som ble lukket i kap. 6** (tiltak F5) og må også rettes i 7.3.
- **Manglende kryssreferanse til kap. 5.5** der trenings-/testsplitten er definert opprinnelig. 7.3 burde åpne med en kort referanse «(jf. kap. 5.5)» og ikke gjenoppfinne tallene.
- **27/15-splitten** er konsistent med totalen i Tabell 2 (testsett 42, toppdager > P90 trening = 5 i Tabell 2 men 15 i 7.3). Forskjellen skyldes at Tabell 2 bruker 90.-persentilen fra *testsettet selv* (508,8 stk → 5 dager over) mens 7.3 bruker 90.-persentilen fra *treningssettet* (69,3 stk → 15 dager over). Dette er en kritisk distinksjon som ikke er forklart i 7.3, og den kan forvirre leseren som ser begge tall i samme rapport. Anbefaling: ett ekstra setning som klargjør at terskelen er definert på trening og deretter brukt på test.
- **27 og 15 dager bør oppsummeres i en mini-tabell** (eller minst en figur som viser hvilke dager i testsettet som klassifiseres som hva), gitt segmenteringens betydning for hele analysen.

### 7.4 Validering: residualdiagnostikk (l. 438–444)

**Observasjon:** To valideringsmetoder: visuell ACF-inspeksjon (Figur 6) og Ljung-Box Q-test (10 lags). I tillegg analyseres systematisk bias per segment.

**Vurdering:**
- **Ljung-Box-testen mangler in-tekst-sitering.** Ljung & Box (1978) er sitert i kap. 5.2 (l. 297) men ikke i 7.4, der testen faktisk gjennomføres. Samme svakhet som for ADF.
- **Figur 6 introduseres i 7.4 men plasseres i kap. 8.3.** CLAUDE.md §7 krever at figurer introduseres og forklares i teksten *før* de vises. Her vises figuren i kap. 8.3 etter at den allerede er omtalt i 7.4 — det er på grensen til brudd. Enten bør figuren flyttes til 7.4, eller 7.4 bør referere til den som «(presenteres sammen med resultatene i kap. 8.3, Figur 6)».
- **Bias-analysen hører strengt tatt hjemme i kap. 8.** 7.4 er definert som *valideringskapittel*, men bias-analyse per segment er en *resultatpresentasjon*. Skillet mellom prosess (kap. 7) og resultat (kap. 8), som kap. 11 i CLAUDE.md eksplisitt krever, blir derfor litt utvasket. Forslag: 7.4 nevner at bias rapporteres som en *del av valideringen*, og selve tallene/tabellene presenteres i kap. 8.3.
- **Hyndman & Athanasopoulos (2021)** er en naturlig referanse for residualdiagnostikk-protokollen og burde nevnes minst én gang i 7.4.

### Tverrgående: figurer og tabeller

**Observasjon:** Kap. 7 inneholder ingen egne figurer eller tabeller; alt er henvist til vedlegg eller kap. 8.

**Vurdering:**
- For et analysekapittel som dokumenterer den operative gjennomføringen, er fraværet av egne illustrasjoner uvanlig. Minst tre figurer/tabeller burde vurderes:
  1. **ACF-plott av treningsserien** (jf. mangel i 7.1).
  2. **AIC-tabell for topp 5 SARIMA-kandidater** med markering av valgt modell — i dag kun i vedlegg A2.
  3. **Mini-tabell for 27/15-splitten** i 7.3 som viser hvordan segmentene fordeler seg over testperioden.

---

## 3. Identifiserte svakheter (med tiltakskoder)

### Faglige
- **F1:** L. 418 — ADF-testen mangler in-tekst-sitering (Dickey & Fuller, 1979) der testen anvendes. **Status: lukket 2026-04-30.**
- **F2:** L. 442 — Ljung-Box-testen mangler in-tekst-sitering (Ljung & Box, 1978) der testen anvendes. **Status: lukket 2026-04-30.**
- **F3:** L. 427 — «Ca. 30 % bedre MAE enn utunet standard-konfigurasjon» mangler tabell- eller vedleggsreferanse og definisjon av «utunet». **Status: lukket 2026-04-30** — utunet referanse definert som Sklearn-defaults (`learning_rate=0,1`, `max_depth=3`, `n_estimators=100`) og henvisning til vedlegg A3 lagt til.
- **F4:** L. 423 — MLE-konvergensvurdering er udokumentert pedagogisk; én setning om hvorfor ikke-konvergens kvalifiserer for kassasjon mangler. **Status: lukket 2026-04-30.**
- **F5:** L. 444 — Hyndman & Athanasopoulos (2021) som residualdiagnostikk-referanse mangler. **Status: lukket 2026-04-30.**

### Metodiske
- **M1:** L. 430 — «Modellene trenes på 208 virkedager» er feil for SARIMA, Holt-Winters og Seasonal Naive (218 dager, jf. kap. 5.5 og kap. 6.0). Faktisk inkonsistens som må rettes. **Status: lukket 2026-04-30.** Rettet til presisering om 218 (statistisk) og 208 (ML) med kryssreferanse til 5.5. Som del av samme rydding ble også P90-terskelen flyttet fra 69,3 (208 ML) til 70,6 (218 fullt treningssett) i koden, og rapporttall i sammendrag, abstract, Tabell 2–4 samt kap. 9 oppdatert.
- **M2:** L. 420 — ACF-plottet av treningsserien er omtalt verbalt, men ikke vist som figur. Brudd på CLAUDE.md §7 om aktiv bruk av figurer. **Status: lukket 2026-04-30** — i stedet for nytt plott er konkrete ACF-verdier (lag 1 = 0,79, lag 2 = 0,51, lag 3 = 0,20, lag 5 etter sesongdifferensiering = −0,51) lagt inn i 7.1, og det opprinnelige feilaktige utsagnet om «sterke topper ved lag 5, 10, 15» korrigert.
- **M3:** L. 444 — Bias-analyse er plassert i 7.4 (validering), men hører strengt tatt hjemme i kap. 8 (resultater) jf. CLAUDE.md §11-skillet mellom prosess og resultat. **Status: lukket 2026-04-30** — 7.4 begrunner nå bias som validerings­indikator og deferrer tabelldata til 8.3.
- **M4:** L. 423 — «Den opprinnelige $(1,1,1)(1,1,1)_7$» mangler kontekst og kryssreferanse til kap. 9.1 (overgangen fra $s=7$ til $s=5$). **Status: lukket 2026-04-30.**
- **M5:** L. 432 — 27/15-segmenteringen bruker P90 fra trening, men kap. 5.5/Tabell 2 bruker P90 fra testet selv. Forskjellen er ikke forklart og kan forvirre leseren. **Status: lukket 2026-04-30** — løst ved at terskelen nå er 70,6 fra 218 dager (felles for hele rapporten).

### Strukturelle
- **S1:** L. 430 — Manglende kryssreferanse til kap. 5.5 der trenings-/testsplitten er definert. **Status: lukket 2026-04-30.**
- **S2:** L. 441 — Figur 6 introduseres i 7.4 men vises først i kap. 8.3. På grensen til brudd på CLAUDE.md §7. **Status: lukket 2026-04-30** — Figur 6-referansen er nå eksplisitt: «(presenteres sammen med resultatene i kap. 8.3, Figur 6)».
- **S3:** Kap. 7 mangler egne figurer/tabeller. Tre kandidater (trenings-ACF, AIC-tabell, segmenteringsoversikt) bør vurderes. **Status: lukket 2026-04-30** — løst ved tydeligere henvisninger til vedlegg A2 (AIC-topp-5), A3 (GBM-tuning) og A4 (RF feature importance) i 7.2, og konkrete ACF-tall i 7.1. Ingen ny figur lagt til, fordi vedleggene allerede inneholder de relevante tabellene.

### Formidling
- **P1:** L. 432, 444 — Fet skrift inni løpende tekst («**segmentert**», «**systematisk bias**») bryter med CLAUDE.md §1 (ny typografi-regel 2026-04-30). **Status: lukket 2026-04-30.**
- **P2:** L. 423 — Inkonsistent tallpresisjon for AIC (2 510,06 vs 2 558). **Status: lukket 2026-04-30** — alle AIC-tall i 7.2 rundet til hele AIC-poeng (2 510, 2 558, 2 481).
- **P3:** L. 442 — Engelsk «lags» uten norsk parafrase ved første bruk i 7.4. **Status: lukket 2026-04-30** — endret til «ti etterslep (lags)».
- **P4:** Punktlister i 7.3 (Normale/Toppdager) og 7.4 (ACF/Ljung-Box) kan vurderes konvertert til løpende prosa, i tråd med stilen som ble valgt for revidert kap. 6. **Status: lukket 2026-04-30** — begge punktlister konvertert til prosa.

---

## 4. Forbedringsforslag

| ID | Forslag |
|---|---|
| F1 | Tilføy «(Dickey & Fuller, 1979)» i 7.1 ved første bruk av ADF-testen. |
| F2 | Tilføy «(Ljung & Box, 1978)» i 7.4 ved første bruk av Q-testen. |
| F3 | Erstatt «ca. 30 % bedre MAE» med konkret MAE-par (f.eks. «MAE går fra X stk med Sklearn-defaults til Y stk etter tuning, en forbedring på Z %»), eller henvis til vedlegg A3 der tallene står. |
| F4 | Føy til én setning i 7.2: «Ikke-konvergerte modeller ble kassert fordi parameterestimatene ikke er pålitelige og AIC-verdien dermed ikke er en meningsfull sammenligningsstørrelse.» |
| F5 | Tilføy en kort henvisning til Hyndman og Athanasopoulos (2021) for residualdiagnostikk-protokollen i 7.4. |
| M1 | Rett 7.3 l. 430: «Modellene trenes på 218 virkedager (208 for ML-modeller etter lag-padding, jf. kap. 5.5)». |
| M2 | Lag og inkluder ACF-plott av treningsserien som ny figur i 7.1 (nummerering må håndteres mot eksisterende Figur 5 og 6). Alternativt: flytt referansen til vedlegg og marker eksplisitt at plottet ligger der. |
| M3 | Flytt selve bias-tabelldata til kap. 8.3, og la 7.4 bare slå fast at bias inngår i valideringsprotokollen. |
| M4 | I 7.2: «den opprinnelige $(1,1,1)(1,1,1)_7$ fra første iterasjon før overgangen til 5-dagers virkedagssyklus (jf. kap. 9.1)». |
| M5 | I 7.3: «Merk at terskelen 69,3 stk er P90 fra treningssettet og brukes operasjonelt på testsettet, ikke testsettets egen P90 (508,8 stk i Tabell 2).» |
| S1 | Åpne 7.3 med «(jf. kap. 5.5)» og fjern duplikatdefinisjonene. |
| S2 | Endre l. 441 til «(presenteres i kap. 8.3, Figur 6)» eller flytt figuren til 7.4. |
| S3 | Vurder å tilføy minst én figur/tabell i kap. 7 (trenings-ACF og/eller AIC-topp-5-tabell). |
| P1 | Fjern fet skrift i l. 432 og 444 («segmentert», «systematisk bias»). |
| P2 | Bruk én konsistent presisjon for AIC (forslag: én desimal eller hele tall). |
| P3 | Skriv «(ti etterslep / lags)» ved første bruk i 7.4. |
| P4 | Vurder å konvertere punktlistene i 7.3 og 7.4 til prosa for konsistens med revidert kap. 6. |

---

## 5. Samsvar med prosjektplan og status

**Mot proposal (`011 fase 1 - proposal/proposal.md`):** Problemstillingen handler om i hvilken grad tidsserie-baserte metoder predikerer daglig etterspørsel. Kap. 7 dekker den operative gjennomføringen av analysen og gir grunnlaget for evaluering i kap. 8. Ingen avvik mot proposal.

**Mot status.md:** Status av 2026-04-30 sier «| 7 Analyse | Ferdig | 7.1–7.4 med residualdiagnostikk |». Reviewen viser at kapittelet i hovedsak er ferdig, men inneholder én faktisk inkonsistens (208/218) og fem manglende sitater som bør lukkes før peer review M-05. Statusen «Ferdig» bør beholdes, men med en review-merknad om gjenstående tiltak.

**Mot WBS (ACT-08 i status.md):** Alle leveranser i ACT-08 (grid-søk, residualanalyse, segmentering) er reflektert i kap. 7. Ingen avvik.

**Mot CLAUDE.md §11 — kjerneinnhold for kap. 6/7:**
- «Begrunnelse: hvilke modeller som ble vurdert/forkastet» → dekket i kap. 6 (ikke i kap. 7).
- «Parametrisering: hvordan parameterkombinasjoner (tuning) er testet» → **dekket i 7.2**.
- «Validering: hvordan modellvalget er gjort og validert (residualanalyse)» → **dekket i 7.4**, men bias-tabellplassering er på grensen.

**Mot CLAUDE.md §1 (nye regler 2026-04-30):**
- Fet skrift inni tekst: brudd i 7.3 og 7.4 (P1).
- Setningsoppdeling med tankestrek: ikke observert i kap. 7 (godt).

**Mot CLAUDE.md §7:**
- Tabeller og figurer skal introduseres i tekst før visning: Figur 6 introduseres i 7.4 men vises først i 8.3 — på grensen til brudd (S2).
- Aktiv bruk av figurer: ACF-plottet av trening er ikke vist (M2).

---

## 6. Prioritert tiltaksliste

| Prioritet | Tiltak | Kapittel/linje | Estimert innsats |
|---|---|---|---|
| 1 | Rett «208 virkedager» til 218/208 med kryssreferanse til kap. 5.5 (M1, S1) | 7.3, l. 430 | 5 min |
| 1 | Tilføy in-tekst-sitater for ADF (F1) og Ljung-Box (F2) | 7.1 og 7.4 | 5 min |
| 1 | Klargjør «opprinnelig $(1,1,1)(1,1,1)_7$» med kryssreferanse til kap. 9.1 (M4) | 7.2, l. 423 | 5 min |
| 1 | Fjern fet skrift inni tekst (P1) | 7.3 l. 432, 7.4 l. 444 | 2 min |
| 2 | Forklar 27/15-segmenteringens P90-grunnlag (M5) | 7.3, l. 432 | 5 min |
| 2 | Erstatt «ca. 30 % bedre» med konkrete tall eller vedleggsreferanse (F3) | 7.2, l. 427 | 10 min |
| 2 | Legg til ACF-plott av treningsserien som ny figur i 7.1 (M2) | 7.1 | 30–45 min |
| 2 | Tydeliggjør Figur 6-plassering (S2) | 7.4, l. 441 | 2 min |
| 2 | Flytt bias-tabellinnhold til kap. 8.3, behold prinsipp i 7.4 (M3) | 7.4, l. 444 | 10 min |
| 2 | Forklar MLE-konvergensvurdering (F4) | 7.2, l. 423 | 5 min |
| 2 | Tilføy Hyndman & Athanasopoulos-referanse (F5) | 7.4 | 2 min |
| 3 | Konsistent AIC-presisjon (P2) | 7.2, l. 423 | 2 min |
| 3 | Parafrase «lags» ved første bruk (P3) | 7.4, l. 442 | 1 min |
| 3 | Vurder AIC-topp-5-tabell og segmenteringsoversiktstabell (S3) | 7.2, 7.3 | 30–60 min |
| 3 | Vurder konvertering av punktlister til prosa (P4) | 7.3, 7.4 | 15 min |

**Sum estimert innsats:**
- Prioritet 1: ca. 15–20 min (kritisk for innlevering).
- Prioritet 2: ca. 1,5 timer (viktig for kvalitet).
- Prioritet 3: ca. 50 min (ønskelig polering).
- **Totalt: ca. 2,5 timer** for full lukking.

---

## 7. Samlet vurdering

Kap. 7 er teknisk dekkende og strukturelt godt: stasjonaritetsvurdering (7.1), parametersøk og tuning (7.2), estimering og segmentering (7.3) og residualdiagnostikk (7.4) er alle på plass og henviser til vedlegg A1–A4 der det trengs. Kapittelet bærer preg av å være skrevet i samme stil som kap. 6 var før revisjonen 2026-04-30, det vil si med fet skrift som etiketter og enkle punktlister.

Tre forhold trekker kvaliteten ned. For det første inneholder 7.3 en **faktisk inkonsistens** med kap. 5.5 og revidert kap. 6 om treningssettets størrelse — dette er samme feil som ble lukket i kap. 6 og må rettes i 7.3 før peer review. For det andre **mangler in-tekst-sitater** for ADF, Ljung-Box og deler av residualdiagnostikken der testene faktisk anvendes, et brudd på CLAUDE.md §2. For det tredje er **ACF-plottet av treningsserien** omtalt verbalt i 7.1 men ikke vist som figur, noe som svekker den pedagogiske verdien for et analysekapittel.

I tillegg er fet skrift inni tekst (l. 432, 444) et brudd på den nye typografi-regelen i CLAUDE.md §1, og Figur 6-plasseringen er på grensen til brudd på §7. Ingen av tiltakene er tunge i seg selv: prioritet 1-listen kan lukkes på 15–20 min, og full lukking inkludert ny ACF-figur og tabellforslag tar omtrent 2,5 timer. Kvalitetsnivået er **øvre middels for LOG650-standard**, og med prioritet 1-tiltakene gjennomført vil kapittelet være på solid akademisk nivå og klart for peer review.

---

## 8. Oppfølgingssaker (for vurdering)

- **Bias-analyse i 7.4 vs kap. 8.3:** Avgjør om bias-resultatene skal flyttes helt til kap. 8.3, eller om det er pedagogisk forsvarlig å la 7.4 nevne at bias inngår i valideringsprotokollen og at tallene presenteres i kap. 8.3.
- **Vedlegg A1, l. 709:** Inneholder fortsatt formuleringen «SARIMAs `d=1` er derfor konservativt valgt», som motsier revidert kap. 6.3, kap. 7.2 og kap. 9.6. Bør rettes når dere går gjennom hele rapporten samlet.
- **Stilkonsistens med revidert kap. 6:** Hvis dere ønsker å konvertere kap. 7 til samme prosa-stil som revidert kap. 6 (færre punktlister, mer fulltekst), bør det skje før peer review for konsekvent leseopplevelse.

---

*Generert 2026-04-30 som del av intern review-prosess før peer review M-05 (2026-05-01).*
