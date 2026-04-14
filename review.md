# Prosjektreview: Prognosepresisjon REMA 1000 (LOG650 G27)

**Dato:** 14. april 2026
**Reviewer:** Claude (AI-assistert gjennomgang)
**Omfang:** Rapport, Python-kode, data, prosjektplan og lærerkommentarer

---

## 1. Overordnet vurdering

Prosjektet er godt organisert og ligger foran skjema. Analysen er metodisk solid med tre modeller (Seasonal Naïve, SARIMA, Random Forest) testet i to scenarier. Rapporten har en sterk akademisk forankring med relevant litteratur, og det er god rød tråd fra problemstilling til konklusjon.

Hovedutfordringene er knyttet til **ufullstendigheter i rapporten** (vedlegg, Scenario 2-presentasjon, tekniske detaljer) og **metodiske valg som bør revurderes** (helgehåndtering, sesongparameter, modellutvidelser).

---

## 2. Lærerens tilbakemeldinger og vår vurdering

### 2.1 Manglende helgedatoer i salgsdataene

**Lærerens kommentar:** Datoer hopper fra lørdag til mandag — er distribusjonssenteret stengt, eller mangler det data?

**Vår vurdering:** Distribusjonssenteret er stengt i helger, men bestillinger kan oppstå selv om det er helg. Dette er **ikke dokumentert i rapporten** og har direkte konsekvenser for modellvalget:

- **Koden bruker `asfreq('D').fillna(0)`** (`scenario_analyse.py:13`, `analyse_hoved.py:16`) som setter helger til 0 etterspørsel. Dette forurenser modellene — SARIMA tolker det som faktiske null-dager, og lag-features i Random Forest henter inn kunstige nuller.
- **SARIMA bruker `s=7`**, men den faktiske syklusen er **5 virkedager**. Med `s=5` kan SARIMA fange den reelle ukedagsrytmen uten kunstige helgedager.
- **Mandagseffekten** (høyest volum, Figur 2) skyldes trolig akkumulerte helgebestillinger. En eksplisitt feature som `is_monday` eller `days_since_last_order` kan gi bedre forklaring enn den implisitte lag-strukturen.

**Anbefalt tiltak:**
- [ ] Dokumenter i rapporten (kap. 4 eller 5) at distribusjonssenteret er stengt i helger, at helgebestillinger registreres på mandager, og at dette forklarer mandagseffekten
- [ ] Vurder å fjerne helgedager fra tidsserien i stedet for å fylle med 0, og bruk `s=5` i SARIMA
- [ ] Legg til en `is_monday`-feature i Random Forest for å fange helgeakkumuleringseffekten
- [ ] Kjør modellene på nytt med disse endringene og sammenlign med eksisterende resultater

### 2.2 Kampanjekalender mangler som fil

**Lærerens kommentar:** Kampanjer nevnes som sentral forklaringsvariabel, men ingen kampanjekalender-fil finnes i datasettet.

**Vår vurdering:** Kampanjeinformasjonen er **hardkodet i Python-skriptene** basert på ukenumre:
- `is_crazy_days`: Uke 45 (2025) og uke 5 (2026) — `scenario_analyse.py:17-19`
- `is_event`: Uke 16 (Påske), uke 33 (Skolestart), uke 51 (Jul) — `scenario_analyse.py:21-24`

Denne informasjonen ble mottatt muntlig/via e-post fra REMA underveis i prosjektet. Det finnes kun **to Crazy Days-perioder** i datasettet, noe som begrenser muligheten for å trene modeller som *lærer* kampanjeeffekter.

**Anbefalt tiltak:**
- [ ] Opprett en kampanjekalender-fil (f.eks. `004 data/kampanjekalender.csv`) med kolonner: startdato, sluttdato, type (Crazy Days / hendelse), kilde
- [ ] Dokumenter i rapporten hvordan og når kampanjeinformasjonen ble mottatt
- [ ] Les kampanjedata fra fil i Python-skriptene i stedet for hardkoding, for etterprøvbarhet
- [ ] Diskuter i rapporten at to kampanjeperioder gir begrenset grunnlag for å modellere kampanjeeffekter

### 2.3 Utvidelse av modellene

**Lærerens kommentar:** MAPE på 68-85% er svakt. Neste steg bør være utvidede modeller.

**Vår vurdering:** Scenariosammenligningen (Scenario 1 vs 2) viser allerede effekten av å legge til kampanjeinfo. Men læreren etterspør trolig mer ambisiøse modellutvidelser. Med to kampanjeperioder og 306 treningsdager er mulighetene begrensede, men det finnes realistiske utvidelser:

**Realistiske utvidelser å implementere:**

1. **Endre sesongparameter fra s=7 til s=5** — Fjern helgedager og bruk virkedagssyklus. Enkel endring som viser metodisk modenhet og svarer direkte på lærerens helgekommentar.

2. **Mandagseffekt / helgeakkumulering** — Legg til `is_monday` eller `days_since_last_order` som feature i Random Forest. Fanger den operasjonelle årsaken bak det høye mandagsvolumet.

3. **Utvidede features i Random Forest:**
   - `week_of_month` (uke 1 vs uke 4 — mulig lønningseffekt)
   - `month` (sesongvariasjon utover ukesyklus)
   - `days_to_next_campaign` / `days_since_campaign` (avstandsmål til kampanjer)

4. **Segmentert modellering** — Tren separate modeller for normale dager og kampanjedager i stedet for én modell med kampanjeflagg. Normale dager har allerede MAE 6.56, så forbedringsfokuset bør ligge på toppdagene.

**Å diskutere som videre arbeid (ikke nok data til å implementere):**
- Kampanjevolum-modellering (krever flere kampanjeperioder)
- LSTM/nevrale nettverk (overkill for 306 dager, utenfor LOG650-scope)
- Prisdata som forklaringsvariabel (nevnt i proposal, men ikke mottatt)

**Anbefalt tiltak:**
- [ ] Implementer punkt 1-3 over og kjør ny sammenligning
- [ ] Inkluder resultatene i rapporten som en utvidet analyse
- [ ] Diskuter punkt 4 og videre arbeid i konklusjonen

---

## 3. Rapportgjennomgang

### 3.1 Kapittel mot lærerens krav (GEMINI.md §11)

| Kapittel | Oppfyllelse | Viktigste mangel |
|----------|-------------|------------------|
| 4 Case | 95% | Helgedata og kampanjekalender ikke dokumentert |
| 5 Metode | 90% | Grid-search-detaljer mangler, Python-ref. mangler |
| 6-7 Modellering/Analyse | 85% | RF-hyperparametere (n_estimators, max_depth) ikke oppgitt, AIC-tabell mangler |
| 8 Resultater | 70% | **Scenario 2 ikke tydelig presentert**, tabeller ikke introdusert i tekst |
| 9 Diskusjon | 80% | Scenario 2 refereres som "Fase 1/2" uten tydelig kobling til kap. 8 |
| 10 Konklusjon | 80% | Mangler konkrete implementeringsanbefalinger for REMA |

### 3.2 Scenario 2-problemet

Problemstillingen (kap. 1.2) definerer tydelig Scenario 1 (blind) og Scenario 2 (med kampanjeinfo). Koden i `scenario_analyse.py` implementerer dette korrekt og genererer resultater for begge. Men **kapittel 8 presenterer kun det som ser ut som Scenario 1-resultater** (eller muligens Scenario 2, det er uklart). Diskusjonen (kap. 9.1) refererer til "Fase 1 og Fase 2" uten at disse er tydelig definert i resultatkapitlet.

**Anbefalt tiltak:**
- [ ] Legg til en eksplisitt Scenario 1 vs 2-sammenligning i kapittel 8 med separate tabeller
- [ ] Bruk konsistent terminologi — enten "Scenario 1/2" eller "Fase 1/2", ikke begge
- [ ] Inkluder figuren `fig_scenario_sammenligning.png` i kapittel 8

### 3.3 Vedlegg (Kap. 12)

Vedlegget er tomt. For etterprøvbarhet bør det inneholde:

- [ ] Random Forest-hyperparametere: `n_estimators=100, random_state=42` (fra `analyse_hoved.py:66`)
- [ ] Grid-search-tabell med AIC-verdier for testede SARIMA-kombinasjoner
- [ ] Feature importance-verdier for Random Forest
- [ ] Kodesnutter eller lenke til repository
- [ ] Kampanjekalender

### 3.4 Figurer og tabeller

| Element | Status | Problem |
|---------|--------|---------|
| Figur 1 (Tidsserie) | OK | Introdusert og forklart |
| Figur 2 (Ukedag) | OK | Introdusert og forklart |
| Figur 3 (Lagerstatus) | Delvis | Filnavn er `Skjermbilde 2026-03-23...` — bør renames |
| `fig3_4_modellsammenligning.png` | Ubrukt | Finnes på disk men ikke referert i rapporten |
| `fig5_kampanjeeffekt.png` | Ubrukt | Finnes på disk men ikke referert i rapporten |
| `fig_scenario_sammenligning.png` | Ubrukt | Bør inn i kap. 8 for Scenario-sammenligningen |
| Figur 6 (Residual ACF) | OK | Introdusert og forklart |
| Tabell 2 (Global ytelse) | Delvis | Ikke introdusert i tekst *før* visning |
| Tabell 3 (Segmentert) | Delvis | Ikke introdusert i tekst *før* visning |

**Anbefalt tiltak:**
- [ ] Introduser Tabell 2 og 3 i teksten *før* de vises (GEMINI.md §7)
- [ ] Rename Figur 3-filen til `fig3_lagerstatus.png`
- [ ] Vurder å inkludere `fig3_4_modellsammenligning.png` og `fig5_kampanjeeffekt.png`, eller slett dem
- [ ] Inkluder `fig_scenario_sammenligning.png` i kap. 8

### 3.5 Referanser

- APA 7 brukt konsekvent
- **Mangler referanser til Python-bibliotekene** brukt i analysen (Pandas, Statsmodels, Scikit-learn)
- Hyndman & Koehler (2006) bør også refereres i kap. 8.1 der MAPE kritiseres

### 3.6 Formalia

- [ ] Egenerklæring og publiseringsavtale er placeholders — må fylles inn
- [ ] Tabell 1 forekommer to ganger (kap. 4.3 og 5.6) med litt ulikt innhold
- [ ] Dato på rapporten er 17. mars 2026 — bør oppdateres ved innlevering

---

## 4. Kodegjennomgang

### 4.1 Kritiske bugs

| Fil | Linje | Problem | Konsekvens |
|-----|-------|---------|------------|
| `scenario_analyse.py` | 13 | `asfreq('D').fillna(0)` setter helger til 0 | Forurenser SARIMA og lag-features |
| `analyse_hoved.py` | 16 | Samme som over | Samme |
| `split_innkjop.py` | 30 | Leser fra `vasket_innkjop_daglig.csv` men vask_data.py lagrer til `vasket_salg_daglig.csv` | FileNotFoundError |
| `modell_test.py` | 8 | `parse_dates=['dato']` men kolonne heter `'Dato'` (stor D) | Parsingfeil |
| `modell_test.py` | 44 | `.fillna(0)` på Seasonal Naive | Manglende dager regnes som 0 i stedet for å ekskluderes |
| `modell_test.py` | 14 | `is_crazy_day` basert på threshold >100 | Inkonsistent med kampanjekalender-metoden i analyse_hoved.py |

### 4.2 Modellimplementering

- **analyse_hoved.py** og **scenario_analyse.py** er solide — korrekt MAE/MAPE/Bias, random seed, god segmentering
- Scenariosammenligningen er godt implementert
- SARIMA-parametere `(1,1,1)(1,1,1)_7` — teknisk korrekt, men `s=7` bør revurderes (se §2.1)

### 4.3 Kommentarer og dokumentasjon

GEMINI.md krever "forklarende kommentarer på norsk" i all kode:
- `analyse_hoved.py`: Delvis oppfylt (noen seksjonskommentarer)
- `scenario_analyse.py`: Delvis oppfylt
- `split_innkjop.py`: **Ingen kommentarer**
- `modell_test.py`: Minimale kommentarer
- `visualiser_resultater.py`: Minimale kommentarer

### 4.4 Reproduserbarhet

- Alle skript bruker **relative filstier** — fungerer kun hvis kjørt fra `012 fase 2 - plan/`
- Random seed satt i analyse_hoved.py og scenario_analyse.py (bra)
- Ingen `requirements.txt` eller lignende for Python-avhengigheter
- Ingen `os.makedirs()` for figur-mapper (unntatt visualiser_resultater.py)

**Anbefalt tiltak:**
- [ ] Fiks bugs i split_innkjop.py og modell_test.py
- [ ] Legg til norske kommentarer i alle skript
- [ ] Opprett requirements.txt
- [ ] Bruk `pathlib.Path` eller `os.path` for robuste filstier

---

## 5. Data og prosjektplan

### 5.1 Datakvalitet
- `vasket_salg_daglig.csv`: 267 rader (virkedager) — strukturert og komplett
- `scenario_resultater.csv`: 52 rader × 21 kolonner — inneholder prediksjoner for begge scenarier
- Rå data finnes i `004 data/`

### 5.2 Konsistens mellom proposal og analyse
- Proposal nevner prisdata som ønsket — dette er **ikke inkludert** i analysen og bør kommenteres som avgrensning
- WBS (19.03) og status.md (26.03) er ikke synkronisert

---

## 6. Prioritert handlingsliste

### Høy prioritet (før innlevering)

1. **Dokumenter helgedata** i rapporten — at distribusjonssenteret er stengt, at helgebestillinger registreres mandager, og at dette forklarer mandagseffekten
2. **Revurder sesongparameter** — test `s=5` (virkedager) vs `s=7` og dokumenter valget
3. **Opprett kampanjekalender-fil** og dokumenter kilde i rapporten
4. **Presenter Scenario 2 tydelig** i kap. 8 med separate tabeller og konsistent terminologi
5. **Fyll vedlegg** med RF-parametere, grid-search-tabell, feature importance
6. **Implementer modellutvidelser** — mandagseffekt, utvidede RF-features, eventuelt segmentert modellering

### Medium prioritet

7. Introduser Tabell 2 og 3 i tekst før visning
8. Inkluder ubrukte figurer eller slett dem
9. Fiks filnavn på Figur 3
10. Legg til Python-bibliotek-referanser i bibliografien
11. Fyll inn egenerklæring og publiseringsavtale
12. Fiks bugs i split_innkjop.py og modell_test.py
13. Legg til norske kommentarer i alle skript

### Lav prioritet

14. Opprett requirements.txt
15. Synkroniser WBS og status.md
16. Oppdater dato på rapporten
17. Bruk robuste filstier i Python-skript

---

## 7. Konklusjon

Prosjektet har en solid kjerne — god problemstilling, relevant litteratur, fungerende modeller og meningsfulle resultater. De viktigste grepene for å styrke rapporten er:

1. **Svare direkte på lærerens kommentarer** (helgedata, kampanjekalender, modellutvidelser)
2. **Synliggjøre Scenario 2-resultatene** som allerede er beregnet men ikke presentert
3. **Utvide modellene** med virkedagssyklus (s=5), mandagseffekt og flere features
4. **Styrke etterprøvbarheten** med vedlegg, kampanjekalender-fil og kodedokumentasjon

Med disse endringene vil rapporten være godt posisjonert for peer review (01.05.26) og endelig innlevering (31.05.26).
