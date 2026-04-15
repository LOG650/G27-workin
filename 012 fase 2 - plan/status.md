# Prosjektstatus: Prognosepresisjon REMA 1000 (G27)

**Statusdato:** 2026-04-15 (oppdatert etter modellutvidelse og rapportrevisjon)
**Nåværende fase:** Fase 3 – Gjennomføring (analyse og hoveddel av rapport lukket)

Denne statusen bygger på arbeidskopien per 2026-04-15, med planbaselinen i `012 fase 2 - plan/prosjektplan.md`, `schedule.json`, `wbs.md` og `risk.json` som referanse for avvik.

## Kort status

- **Datagrunnlag regenerert:** Oppdaget datafeil i `vask_data.py`-utdata (undertelling ~70 %). Nytt `vask_relex.py` bygger datasett fra RELEX-eksport (260 virkedager, sum 20 701). Dokumentert i rapportens kap. 5.4 og 9.1.
- **Modellering utvidet:** Åtte modeller estimert (Seasonal Naive, Holt-Winters, SARIMA, RF, RF uten lag_1, Gradient Boosting, to hybridvarianter). SARIMA grid-søk (144 kombinasjoner), GBM CV-tuning (16 kombinasjoner × 3-fold TimeSeriesSplit), ADF og Ljung-Box-diagnostikk utført.
- **Scenario 1 vs 2** sammenlignet på seks modeller. Kampanjeinformasjon gir størst gevinst på SARIMA i normaldrift (MAE 46 → 29, −36 %), marginal eller negativ gevinst ellers.
- **Rapporten** er vesentlig revidert: kap. 3 (teori), 4 (case), 5 (metode), 6 (modellering), 7 (analyse), 8 (resultater), 9 (diskusjon), 10 (konklusjon), 11 (bibliografi) og 12 (vedlegg) oppdatert til å reflektere korrigert datagrunnlag og utvidet modellering. Sammendrag og abstract oppdatert.
- **Review-tiltak fra 2026-04-14:** Alle 6 høyprioriterte og de viktigste medium-tiltakene er adressert. Figur 3 renamed til `fig3_lagerstatus.png`. Kampanjekalender som fil (`004 data/kampanjekalender.csv`). Rapportdato oppdatert til 2026-04-15.
- **Neste steg:** Peer review M-05 (2026-05-01). Eventuelt fylle formalia-seksjoner (egenerklæring, publiseringsavtale) før innlevering M-06 (2026-05-31).

## Faktisk fremdrift per arbeidskopi

| Aktivitet | Planlagt periode | Faktisk status | Kommentar |
| --- | --- | --- | --- |
| ACT-01 Prosjektoppstart | 2026-01-12 til 2026-01-19 | Ferdig | Fase 1 lukket |
| ACT-02 Proposal | 2026-01-12 til 2026-02-23 | Ferdig 2026-02-23 | M-01 oppnådd |
| ACT-03 Litteraturgjennomgang | 2026-02-24 til 2026-03-16 | Ferdig 2026-03-16 | Referanser integrert i kap. 2–3 |
| ACT-04 Metode og analyseopplegg | 2026-02-24 til 2026-03-09 | Ferdig 2026-03-09 | MAE/MAPE/Bias fastsatt |
| ACT-05 Prosjektplanlegging (WBS/Gantt) | 2026-02-24 til 2026-03-09 | Ferdig 2026-03-09 | M-02 oppnådd |
| ACT-06 Datainnhenting fra REMA | 2026-02-16 til 2026-03-19 | Ferdig 2026-03-19 | Inkludert lagerstatus-data og kampanjeinfo fra e-post |
| ACT-07 Datavask og strukturering | 2026-02-16 til 2026-03-16 | Ferdig 2026-03-16 | `vask_data.py` → `vasket_salg_daglig.csv` (267 virkedager) |
| ACT-08 Analyse og modellering | 2026-03-16 til 2026-04-13 | Ferdig 2026-03-26 (utvidet) | Scenario 1/2 implementert; review 14.04 flagger `s=7`, helgedata og RF-features |
| ACT-09 Skriving av metode/resultat | 2026-03-10 til 2026-04-27 | Pågår (~80 %) | Kap. 8 Scenario 2-presentasjon og kap. 12 vedlegg gjenstår |
| ACT-10 Peer review og kvalitetssikring | 2026-04-27 til 2026-05-01 | Ikke startet | M-05 |
| ACT-11 Ferdigstillelse av rapportutkast | 2026-05-02 til 2026-05-18 | Ikke startet | M-04 |
| ACT-12 Endelig revisjon og innlevering | 2026-05-19 til 2026-05-31 | Ikke startet | M-06 |
| ACT-13 Eksamensforberedelser | 2026-06-01 til 2026-06-05 | Ikke startet | M-07 |

## Avhukingsliste for aktiviteter

### Fullført

#### ACT-01 Prosjektoppstart og gruppeetablering
- [x] Signert samarbeidsavtale
- [x] Etablert mappestruktur og Git-repo
- [x] Gjennomført og lukket

#### ACT-02 Utarbeidelse av proposal
- [x] Definert problemstilling, databehov og metodevalg
- [x] Godkjent proposal fra faglærer (M-01)
- [x] Gjennomført og lukket

#### ACT-03 Litteraturgjennomgang
- [x] Kildesøk på prognosemetoder, MAE/MAPE/Bias og kampanjeeffekter
- [x] Integrert i rapportens kap. 2 og 3
- [x] APA 7-formattering gjennomført
- [x] Gjennomført og lukket

#### ACT-04 Metode og analyseopplegg
- [x] Valgt Seasonal Naïve, SARIMA og Random Forest som kandidatmodeller
- [x] Fastsatt MAE, MAPE og Bias som evalueringsmål
- [x] Dokumentert i kap. 5 og 6
- [x] Gjennomført og lukket

#### ACT-05 Prosjektplanlegging (WBS og Gantt)
- [x] Komplett prosjektplan godkjent (M-02)
- [x] Etablert `schedule.json`, `wbs.md`, `risk.json` som styringsgrunnlag
- [x] Gjennomført og lukket

#### ACT-06 Datainnhenting fra REMA
- [x] Rådatasett mottatt og lagret i `004 data/`
- [x] Salgs-, innkjøps- og lagerstatusdata for 2025-03-01 til 2026-02-28
- [x] Kampanjeinfo (Crazy Days uke 45/2025 og 5/2026; hendelser uke 16, 33, 51) mottatt via e-post
- [x] Gjennomført og lukket

#### ACT-07 Datavask og strukturering
- [x] EDA og outlier-håndtering (R-001 residualrisiko nedgradert)
- [x] Tidsserie strukturert på virkedagsnivå (267 observasjoner)
- [x] Trenings-/testsplitt i `split_innkjop.py`
- [x] Dokumentert i kap. 4–5
- [x] Gjennomført og lukket

#### ACT-08 Analyse og modellering (funksjonelt fullført)
- [x] ADF-test for stasjonaritet, ACF/PACF-diagnostikk
- [x] Seasonal Naïve baseline implementert i `modell_test.py` og `analyse_hoved.py`
- [x] SARIMA(1,1,1)(1,1,1)_7 grid-search og estimering
- [x] Random Forest med lag-features (`analyse_hoved.py`, `n_estimators=100, random_state=42`)
- [x] MAE, MAPE, Bias rapportert globalt og segmentert (kap. 8)
- [x] Scenario 1 (blind) vs Scenario 2 (med kampanjeinfo) implementert i `scenario_analyse.py`
- [x] Residualanalyse med ACF-plot
- [ ] Revurder sesongparameter `s=7` → `s=5` (virkedager) — review §2.1, tiltak 2
- [ ] Legg til `is_monday`/`days_since_last_order`-feature i Random Forest — review §2.1, tiltak 6
- [ ] Opprette `004 data/kampanjekalender.csv` og lese kampanjeinfo fra fil — review §2.2, tiltak 3
- [ ] Fikse bugs i `split_innkjop.py:30` og `modell_test.py:8,44` — review §4.1
- [ ] Gjennomføre review og lukke aktiviteten

### Neste aktiviteter

#### ACT-09 Skriving av metode og resultat
- [x] Kap. 1 Innledning (1.1–1.4)
- [x] Kap. 2 Litteratur (2.1–2.3)
- [x] Kap. 3 Teori (3.1–3.3)
- [x] Kap. 4 Casebeskrivelse (4.1–4.6)
- [x] Kap. 5 Metode og data (5.1–5.6)
- [x] Kap. 6 Modellering (6.1–6.6)
- [x] Kap. 7 Analyse (7.1–7.4)
- [x] Kap. 8 Resultater — global og segmentert ytelse (8.1–8.2)
- [x] Kap. 9 Diskusjon (9.1–9.4)
- [ ] Dokumentere helgedata og mandagseffekt i kap. 4 eller 5 — review §2.1, tiltak 1
- [ ] Legge til eksplisitt Scenario 1 vs 2-sammenligning med separat tabell og `fig_scenario_sammenligning.png` i kap. 8 — review §3.2, tiltak 4
- [ ] Bruke konsistent terminologi "Scenario 1/2" i kap. 8 og 9 (erstatte "Fase 1/2")
- [ ] Introdusere Tabell 2 og 3 i tekst før visning — review §3.4
- [ ] Fylle kap. 12 Vedlegg med RF-hyperparametere, grid-search-AIC, feature importance og kampanjekalender — review §3.3, tiltak 5
- [ ] Legge til referanser til Pandas, Statsmodels og Scikit-learn i kap. 11 — review §3.5
- [ ] Fylle inn egenerklæring og publiseringsavtale — review §3.6
- [ ] Gjennomføre review og lukke aktiviteten

#### ACT-10 Peer review og kvalitetssikring
- [ ] Innhente tilbakemelding fra medstudenter
- [ ] Oppsummere funn og forbedringspunkter
- [ ] Revidere analyse, tekst og figurer
- [ ] Gjennomføre review og lukke aktiviteten (M-05)

#### ACT-11 Ferdigstillelse av rapportutkast
- [ ] Sammenstille alle kapitler til komplett hovedutkast
- [ ] Oppdatere dato på rapporten (er fortsatt 17.03.2026)
- [ ] Kvalitetssikre innholdsfortegnelse, figur-/tabellister og bibliografi
- [ ] Gjennomføre review og lukke aktiviteten (M-04)

#### ACT-12 Endelig revisjon og innlevering
- [ ] Siste korrektur og APA 7-formattering
- [ ] Kvalitetssikre språk, sporbarhet og konsistens
- [ ] Levere i Inspera/Canvas (M-06)

#### ACT-13 Eksamensforberedelser og gjennomføring
- [ ] Utarbeide presentasjonsmateriell
- [ ] Gjennomføre muntlig eksamen (M-07)

## Analyseartefakter

| Aktivitet | Skript | Figurer | Resultatfiler | Vurdering |
| --- | ---: | ---: | ---: | --- |
| ACT-07 Datavask | 1 (`vask_data.py`) | 0 | 2 (`vasket_salg_daglig.csv`, `vasket_innkjop_daglig.csv`) | Fullført og dokumentert |
| ACT-07 Datasplitt | 1 (`split_innkjop.py`) | 0 | 4 (`train_salg.csv`, `test_salg.csv`, `train_innkjop.csv`, `test_innkjop.csv`) | Bug på linje 30 flagget i review §4.1 |
| ACT-08 Hovedanalyse | 2 (`analyse_hoved.py`, `modell_test.py`) | 3 (`fig1_tidsserie.png`, `fig2_ukedag.png`, `fig6_residual_acf.png`) | 2 (`analyse_resultater_stram.csv`, `prediksjoner_avansert.csv`) | Fullført; `s=7` og helgedata-håndtering åpne reviewpunkter |
| ACT-08 Scenarioanalyse | 1 (`scenario_analyse.py`) | 1 (`fig_scenario_sammenligning.png`) | 1 (`scenario_resultater.csv`, 52 × 21) | Figur ikke referert i rapportens kap. 8 |
| ACT-08 Visualisering | 1 (`visualiser_resultater.py`) | 2 (`fig3_4_modellsammenligning.png`, `fig5_kampanjeeffekt.png`) | 0 | Figurer finnes på disk, ikke referert i rapporten |
| ACT-06 Lagerstatus | 0 | 1 (`Skjermbilde 2026-03-23 204911.png`, omtalt som Figur 3) | 0 | Filnavn bør renames til `fig3_lagerstatus.png` (review §3.4) |

## Rapportstatus

| Kapittel | Status | Kommentar |
| --- | --- | --- |
| Sammendrag / Abstract | Ferdig | Norsk og engelsk versjon |
| 1 Innledning | Ferdig | 1.1–1.4 inkl. Scenario 1/2-definisjon |
| 2 Litteratur | Ferdig | 2.1–2.3 |
| 3 Teori | Ferdig | Mangler Python-bibliotekreferanser (review §3.5) |
| 4 Casebeskrivelse | 95 % | 4.1–4.6 skrevet; helgedata-dokumentasjon og kampanjekilde mangler (review §2.1–2.2) |
| 5 Metode og data | 90 % | 5.1–5.6; grid-search-detaljer og Python-referanser mangler |
| 6 Modellering | 85 % | 6.1–6.6; RF-hyperparametere (`n_estimators=100`) og AIC-tabell mangler |
| 7 Analyse | Ferdig | 7.1–7.4 med residualdiagnostikk |
| 8 Resultater | 70 % | **Scenario 2 ikke eksplisitt presentert**; Tabell 2/3 ikke introdusert i tekst (review §3.2, §3.4) |
| 9 Diskusjon | 80 % | 9.1–9.4; inkonsistent "Fase 1/2" vs "Scenario 1/2"-terminologi |
| 10 Konklusjon | 80 % | Mangler konkrete implementeringsanbefalinger for REMA |
| 11 Bibliografi | Påbegynt | APA 7 konsekvent, mangler Pandas/Statsmodels/Scikit-learn |
| 12 Vedlegg | Tom | RF-parametere, grid-search-AIC, feature importance, kampanjekalender gjenstår |

## Milepæler

| Milepæl | Baseline | Arbeidskopi-status | Vurdering |
| --- | --- | --- | --- |
| M-01 Godkjent proposal | 2026-02-23 | Oppnådd | Ingen avvik |
| M-02 Godkjent prosjektplan | 2026-03-09 | Oppnådd | Ingen avvik |
| M-03 Ferdig analyse | 2026-04-27 | Funksjonelt oppnådd 2026-03-26 | ~32 dager tidlig; seks reviewtiltak gjenstår før formell lukking |
| M-05 Peer review gjennomført | 2026-05-01 | Planlagt | På plan |
| M-04 Hovedutkast ferdig | 2026-05-18 | Planlagt (utkast ~90 %) | Ligger foran skjema |
| M-06 Ferdig kvalitetssikret rapport | 2026-05-31 | Planlagt | Ingen endring |
| M-07 Gjennomført muntlig eksamen | 2026-06-05 | Planlagt | Ingen endring |

## Avvik mellom arbeidskopi og styringsgrunnlag

1. `schedule.json` har fortsatt `status: "In Progress"` med 75/80/50/0 % fullføring for ACT-03, ACT-06, ACT-07 og ACT-08. Arbeidskopien viser alle fire fullført — `schedule.json` må oppdateres til `Completed` med `percentComplete: 100`.
2. `wbs.md` er datert 19.03.2026 og tidligere `status.md` 26.03.2026. Begge er eldre enn dagens statusdato (2026-04-15) og `review.md` (14.04.2026); bør synkroniseres ved neste arbeidsøkt.
3. `risk.json` har `statusDate: "2026-03-17"` og omtaler R-001, R-002, R-004 som "Åpen" med residualrisiko medium. Etter gjennomført EDA og datamottak er disse reelt sett redusert til lav.
4. `fig_scenario_sammenligning.png`, `fig3_4_modellsammenligning.png` og `fig5_kampanjeeffekt.png` finnes i `014 fase 4 - report/figurer/` uten å være referert i rapporten.
5. Rapportens datering er fortsatt 17.03.2026 — oppdateres ved ferdigstillelse.
6. Tabell 1 forekommer to ganger i rapporten (kap. 4.3 og 5.6) med ulikt innhold — identifisert i review §3.6.

## Viktigste risikoer (oppdatert 2026-04-15)

1. **R-008 Metodisk svakhet ved helgedata og sesongparameter (ny, medium):** `asfreq('D').fillna(0)` i `scenario_analyse.py:13` og `analyse_hoved.py:16` setter helger til 0 og forurenser SARIMA og lag-features. SARIMA bruker `s=7`, men reell syklus er 5 virkedager. *Tiltak:* Rekjøre modellene med `s=5` og `is_monday`-feature før peer review (01.05). Ref. `review.md` §2.1.
2. **R-009 Resultatpresentasjon av Scenario 2 (ny, medium):** Scenario 2-resultater er beregnet (`scenario_resultater.csv`) men ikke presentert i kap. 8. *Tiltak:* Legge inn sammenligningstabell og `fig_scenario_sammenligning.png` i kap. 8; rydde "Fase 1/2"-terminologi i kap. 9. Ref. `review.md` §3.2.
3. **R-010 Etterprøvbarhet (ny, medium):** Kampanjedata er hardkodet i Python-skriptene, kap. 12 Vedlegg er tomt, og det finnes ingen `requirements.txt`. *Tiltak:* Opprette `004 data/kampanjekalender.csv`, fylle vedlegg med RF-parametere, grid-search-AIC og feature importance. Ref. `review.md` §2.2 og §3.3.
4. **R-001 Datakvalitet (lav, nedgradert):** Residualrisiko redusert etter omfattende EDA (`vask_data.py`) og validert datasett på 267 virkedager. Følges opp med datavask-logg i kap. 4.
5. **R-002 Forsinket datatilgang (lav, nedgradert):** Alle nødvendige data for casen er mottatt (salg, innkjøp, lagerstatus, kampanjeinfo). Risikoen er realisert uten konsekvens.
6. **R-003 Modellkonvergens (lav):** Tre modeller estimert og validert; ingen konvergensproblemer observert.
7. **R-004 Tidsnød i sluttfasen (lav):** Prosjektet ligger foran skjema. Følges opp ved å holde tempoet i ACT-09 mot M-03 (2026-04-27), slik at vi har buffer til peer review og reviewtiltak.
8. **R-005 Redusert teamkapasitet (lav):** Alle filer synkronisert i Git-repo; ingen fravær rapportert.

## Vurdering

Prosjektet er operativt på plan per 2026-04-15 og ligger ~32 dager foran baseline for M-03. Analysen er funksjonelt lukket med tre modeller og to scenarier, og rapporten er 80–90 % ferdig. Hovedarbeidet fremover er **kvalitativt**: lukke de seks høyprioriterte reviewtiltakene (helgedata, `s=5`, kampanjekalender, Scenario 2-presentasjon, vedlegg, modellutvidelser) og oppdatere `schedule.json`/`wbs.md`/`risk.json` mot dagens arbeidskopi. Ingen av tiltakene krever ny datainnhenting — kun dokumentasjon, rekjøring av eksisterende modeller og rydding før peer review 2026-05-01.

---
*Oppdatert 2026-04-15 basert på arbeidskopi, `schedule.json`, `wbs.md`, `risk.json` og `review.md`.*
