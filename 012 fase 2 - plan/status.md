# Prosjektstatus: Prognosepresisjon REMA 1000 (G27)

**Statusdato:** 2026-04-30 (intern review av kap. 6 lukket)
**Nåværende fase:** Fase 3 – Gjennomføring (analyse lukket, rapport ~92 % ferdig)

Denne statusen bygger på arbeidskopien per 2026-04-16, med planbaselinen i `012 fase 2 - plan/prosjektplan.md`, `schedule.json`, `wbs.md` og `risk.json` som referanse for avvik.

## Kort status

- **Datagrunnlag regenerert:** Oppdaget datafeil i `vask_data.py`-utdata (undertelling ~70 %). Nytt `vask_relex.py` bygger datasett fra RELEX-eksport (260 virkedager, sum 20 701). Dokumentert i rapportens kap. 5.4 og 9.1.
- **Modellering utvidet:** Åtte modeller estimert (Seasonal Naive, Holt-Winters, SARIMA, RF, RF uten lag_1, Gradient Boosting, to hybridvarianter). SARIMA grid-søk (144 kombinasjoner) med `s=5`, GBM CV-tuning (16 kombinasjoner × 3-fold TimeSeriesSplit), ADF og Ljung-Box-diagnostikk utført. `is_monday` og `days_since_last_order`-features lagt til i RF (`modeller.py`).
- **Scenario 1 vs 2** sammenlignet på seks modeller. Kampanjeinformasjon gir størst gevinst på SARIMA i normaldrift (MAE 46 → 29, −36 %), marginal eller negativ gevinst ellers.
- **Rapporten** er vesentlig revidert: kap. 3 (teori), 4 (case), 5 (metode), 6 (modellering), 7 (analyse), 8 (resultater), 9 (diskusjon), 10 (konklusjon), 11 (bibliografi) og 12 (vedlegg A1–A7) oppdatert til å reflektere korrigert datagrunnlag og utvidet modellering. Sammendrag og abstract oppdatert.
- **Review-tiltak fra 2026-04-14:** Alle 6 høyprioriterte og de viktigste mediumtiltakene er lukket: helgedata/mandagseffekt dokumentert, `s=5`, kampanjekalender som fil (`004 data/kampanjekalender.csv`), Scenario 2 eksplisitt presentert i kap. 8.1, konsistent «Scenario 1/2»-terminologi, Tabell 2/3 introdusert i tekst, kap. 12 Vedlegg utfylt, Pandas/Statsmodels/Scikit-learn sitert i kap. 11. Figur 3 renamed til `fig3_lagerstatus.png`. Rapportdato 2026-04-15.
- **M-03 Ferdig analyse:** Oppnådd 2026-04-16 (baseline 2026-04-27, 11 dager foran skjema).
- **Neste steg:** Forberede peer review M-05 (2026-05-01) — eksportere rapport til PDF/DOCX, dele med medstudenter, opprette `requirements.txt` for etterprøvbarhet. Formalia (egenerklæring, publiseringsavtale) fylles ved M-06 (2026-05-31).

## Faktisk fremdrift per arbeidskopi

| Aktivitet | Planlagt periode | Faktisk status | Kommentar |
| --- | --- | --- | --- |
| ACT-01 Prosjektoppstart | 2026-01-12 til 2026-01-19 | Ferdig | Fase 1 lukket |
| ACT-02 Proposal | 2026-01-12 til 2026-02-23 | Ferdig 2026-02-23 | M-01 oppnådd |
| ACT-03 Litteraturgjennomgang | 2026-02-24 til 2026-03-16 | Ferdig 2026-03-16 | Referanser integrert i kap. 2–3 |
| ACT-04 Metode og analyseopplegg | 2026-02-24 til 2026-03-09 | Ferdig 2026-03-09 | MAE/MAPE/Bias fastsatt |
| ACT-05 Prosjektplanlegging (WBS/Gantt) | 2026-02-24 til 2026-03-09 | Ferdig 2026-03-09 | M-02 oppnådd |
| ACT-06 Datainnhenting fra REMA | 2026-02-16 til 2026-03-19 | Ferdig 2026-03-19 | Inkludert lagerstatus-data og kampanjeinfo fra e-post |
| ACT-07 Datavask og strukturering | 2026-02-16 til 2026-03-16 | Ferdig 2026-04-15 | `vask_relex.py` → `vasket_salg_daglig.csv` (260 virkedager, sum 20 701) |
| ACT-08 Analyse og modellering | 2026-03-16 til 2026-04-13 | Ferdig 2026-04-16 | Alle seks høyprioriterte reviewtiltak lukket; M-03 oppnådd |
| ACT-09 Skriving av metode/resultat | 2026-03-10 til 2026-04-27 | Pågår (~90 %) | Formalia (egenerklæring/publiseringsavtale) fylles ved M-06 |
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
- [x] EDA og outlier-håndtering (R-001 lukket)
- [x] Tidsserie strukturert på virkedagsnivå (260 observasjoner fra RELEX-eksport via `vask_relex.py`)
- [x] Trenings-/testsplitt håndtert inline via `SPLITT_DATO = '2026-01-01'` i `analyse_hoved.py`/`scenario_analyse.py`
- [x] Dokumentert i kap. 4–5
- [x] Gjennomført og lukket

#### ACT-08 Analyse og modellering
- [x] ADF-test for stasjonaritet, ACF/PACF-diagnostikk
- [x] Seasonal Naïve baseline implementert i `modell_test.py` og `analyse_hoved.py`
- [x] SARIMA grid-search (144 kombinasjoner) med `s=5`; beste modell (0,1,1)(0,1,1,5) — review §2.1 tiltak 2 lukket
- [x] Random Forest med lag-features, `is_monday` og `days_since_last_order` (`modeller.py`) — review §2.1 tiltak 6 lukket
- [x] MAE, MAPE, Bias rapportert globalt og segmentert (kap. 8)
- [x] Scenario 1 (blind) vs Scenario 2 (med kampanjeinfo) implementert i `scenario_analyse.py`
- [x] Residualanalyse med ACF-plot
- [x] Kampanjeinformasjon eksternalisert til `004 data/kampanjekalender.csv` — review §2.2 tiltak 3 lukket
- [x] Gjennomført og lukket (M-03 oppnådd 2026-04-16)

### Neste aktiviteter

#### ACT-09 Skriving av metode og resultat
- [x] Kap. 1 Innledning (1.1–1.4)
- [x] Kap. 2 Litteratur (2.1–2.3)
- [x] Kap. 3 Teori (3.1–3.3)
- [x] Kap. 4 Casebeskrivelse (4.1–4.6) inkl. helgedata/mandagseffekt — review §2.1 tiltak 1 lukket
- [x] Kap. 5 Metode og data (5.1–5.6)
- [x] Kap. 6 Modellering (6.1–6.6) inkl. RF-hyperparametere og AIC-tabell
- [x] Kap. 7 Analyse (7.1–7.4)
- [x] Kap. 8 Resultater — global og segmentert ytelse; eksplisitt Scenario 1 vs 2-sammenligning med Tabell 2 og `fig_scenario_sammenligning.png` (Figur 4) — review §3.2 tiltak 4 lukket
- [x] Kap. 9 Diskusjon (9.1–9.4) med konsistent «Scenario 1/2»-terminologi
- [x] Tabell 2 og 3 introdusert i tekst før visning — review §3.4 lukket
- [x] Kap. 11 Bibliografi: Pandas (McKinney 2010), Statsmodels (Seabold & Perktold 2010), Scikit-learn (Pedregosa et al. 2011) sitert i APA 7 — review §3.5 lukket
- [x] Kap. 12 Vedlegg A1–A7: ADF-test, SARIMA grid-AIC, GBM-tuning, feature importance, RF-hyperparametere, kampanjekalender, filstruktur — review §3.3 tiltak 5 lukket
- [ ] Fylle inn egenerklæring og publiseringsavtale (rapport linje 10–14, plassholdere) — utsatt til M-06
- [ ] Gjennomføre review og lukke aktiviteten

#### ACT-10 Peer review og kvalitetssikring
- [ ] Eksportere rapport til PDF/DOCX for distribusjon (mal i `000 templates/Mal prosjekt LOG650 v2.docx`)
- [ ] Dele rapport og `scenario_resultater.csv` med medstudenter
- [ ] Innhente tilbakemelding fra medstudenter
- [ ] Oppsummere funn og forbedringspunkter
- [ ] Revidere analyse, tekst og figurer
- [ ] Gjennomføre review og lukke aktiviteten (M-05)

#### ACT-11 Ferdigstillelse av rapportutkast
- [ ] Sammenstille alle kapitler til komplett hovedutkast
- [ ] Oppdatere rapportdato til innleveringsdato
- [ ] Kvalitetssikre innholdsfortegnelse, figur-/tabellister og bibliografi
- [ ] Gjennomføre review og lukke aktiviteten (M-04)

#### ACT-12 Endelig revisjon og innlevering
- [ ] Fylle inn egenerklæring og publiseringsavtale (mal i `000 templates/`)
- [ ] Siste korrektur og APA 7-formattering
- [ ] Kvalitetssikre språk, sporbarhet og konsistens
- [ ] Levere i Inspera/Canvas (M-06)

#### ACT-13 Eksamensforberedelser og gjennomføring
- [ ] Utarbeide presentasjonsmateriell
- [ ] Gjennomføre muntlig eksamen (M-07)

## Analyseartefakter

| Aktivitet | Skript | Figurer | Resultatfiler | Vurdering |
| --- | ---: | ---: | ---: | --- |
| ACT-07 Datavask | 1 (`vask_relex.py`) | 0 | 1 (`vasket_salg_daglig.csv`, 260 rader) | Fullført og dokumentert; `vask_data.py` utgått |
| ACT-07 Datasplitt | 0 (inline i `analyse_hoved.py`/`scenario_analyse.py` via `SPLITT_DATO = '2026-01-01'`) | 0 | 0 | `split_innkjop.py` utgått; gamle CSV-splitter fjernet |
| ACT-08 Hovedanalyse | 3 (`modeller.py`, `analyse_hoved.py`, `modell_test.py`) | 3 (`fig1_tidsserie.png`, `fig2_ukedag.png`, `fig6_residual_acf.png`) | 2 (`analyse_resultater_stram.csv`, `prediksjoner_avansert.csv`) | Fullført; SARIMA `s=5` og virkedagsfeatures på plass |
| ACT-08 Scenarioanalyse | 1 (`scenario_analyse.py`) | 1 (`fig_scenario_sammenligning.png`, Figur 4) | 1 (`scenario_resultater.csv`, 52 × 21) | Fullført; presentert i kap. 8.1 |
| ACT-08 Kampanjedata | 0 | 0 | 1 (`004 data/kampanjekalender.csv`, 5 rader) | Eksternalisert fra Python-skript; dokumentert i vedlegg A6 |
| ACT-06 Lagerstatus | 0 | 1 (`fig3_lagerstatus.png`) | 0 | Filnavn oppdatert |

## Rapportstatus

| Kapittel | Status | Kommentar |
| --- | --- | --- |
| Sammendrag / Abstract | Ferdig | Norsk og engelsk versjon |
| 1 Innledning | Ferdig | 1.1–1.4 inkl. Scenario 1/2-definisjon |
| 2 Litteratur | Ferdig | 2.1–2.3 |
| 3 Teori | Ferdig | 3.1–3.3 |
| 4 Casebeskrivelse | Ferdig | 4.1–4.6 inkl. helgedata/mandagseffekt |
| 5 Metode og data | Ferdig | 5.1–5.6 inkl. grid-search-detaljer |
| 6 Modellering | Ferdig | 6.1–6.5 inkl. Tabell 4 (modelloversikt), in-tekst-sitater for SARIMA/RF/GBM/HW, presisert blandet evalueringsprotokoll og rettet d=1-framstilling. Redundant 6.6 fjernet. Intern review lukket 2026-04-30 |
| 7 Analyse | Ferdig | 7.1–7.4 med residualdiagnostikk |
| 8 Resultater | Ferdig | 8.1 (Scenario 1 vs 2) og 8.2 (åtte modeller globalt) |
| 9 Diskusjon | 90 % | 9.1–9.4; mangler konkrete implementeringsanbefalinger (ryddes etter peer review) |
| 10 Konklusjon | 90 % | Utfylles endelig etter peer review |
| 11 Bibliografi | Ferdig | APA 7; Pandas, Statsmodels, Scikit-learn sitert |
| 12 Vedlegg | Ferdig | A1–A7 utfylt |
| Egenerklæring | Tom | Plassholder linje 10–11; fylles ved M-06 |
| Publiseringsavtale | Tom | Plassholder linje 13–14; fylles ved M-06 |

## Milepæler

| Milepæl | Baseline | Arbeidskopi-status | Vurdering |
| --- | --- | --- | --- |
| M-01 Godkjent proposal | 2026-02-23 | Oppnådd | Ingen avvik |
| M-02 Godkjent prosjektplan | 2026-03-09 | Oppnådd | Ingen avvik |
| M-03 Ferdig analyse | 2026-04-27 | Oppnådd 2026-04-16 | 11 dager foran baseline |
| M-05 Peer review gjennomført | 2026-05-01 | Planlagt | På plan (15 dager unna) |
| M-04 Hovedutkast ferdig | 2026-05-18 | Planlagt (utkast ~90 %) | Ligger foran skjema |
| M-06 Ferdig kvalitetssikret rapport | 2026-05-31 | Planlagt | Ingen endring |
| M-07 Gjennomført muntlig eksamen | 2026-06-05 | Planlagt | Ingen endring |

## Avvik mellom arbeidskopi og styringsgrunnlag

1. `schedule.json`, `wbs.md` og `risk.json` synkronisert til 2026-04-16 med arbeidskopien.
2. Rapportens datering er 2026-04-15 — oppdateres ved ferdigstillelse i M-04/M-06.
3. `requirements.txt` opprettet i repo-rot 2026-04-18 med pinned versjoner (pandas 3.0.1, numpy 2.4.3, matplotlib 3.10.8, scikit-learn 1.8.0, statsmodels 0.14.6) — R-010 lukket.
4. Tallrydding gjennomført 2026-04-30: P90-terskel flyttet fra 208 ML-trening (69,3) til 218 statistisk trening (70,6) i `analyse_hoved.py` og `scenario_analyse.py`; analysen rekjørt og berørte tabeller/sammendrag oppdatert. Volumtall i kap. 4.3 strukturert som flytkjede (Bestilt → Justert → RELEX virkedager → RELEX hele perioden) med eksplisitte definisjoner. F1 (kap. 4) og M1 (kap. 7) lukket.

## Viktigste risikoer (oppdatert 2026-04-16)

1. **R-004 Tidsnød i sluttfasen (Lav):** Prosjektet ligger ~32 dager foran baseline for M-03. Rapporten er ~90 % ferdig, og peer review M-05 er 15 dager unna. *Tiltak:* Holde tempo i ACT-09 og bruke bufferen til kvalitetssikring. Residualrisiko redusert fra medium til lav.
2. **R-005 Redusert teamkapasitet (Lav, åpen):** Ingen fravær rapportert. Følges opp løpende via Git-repo-synkronisering.
3. **R-010 Etterprøvbarhet (Lukket 2026-04-18):** Kampanjedata eksternalisert, vedlegg utfylt og `requirements.txt` opprettet i repo-rot med pinned versjoner.
4. **R-001 Datakvalitet (Lukket 2026-04-15):** Undertelling i `vask_data.py` korrigert via RELEX-pipen.
5. **R-002 Forsinket datatilgang (Lukket):** Alle data mottatt uten konsekvens.
6. **R-003 Modellkonvergens (Lukket):** Åtte modeller estimert uten konvergensproblemer.
7. **R-008 Helgedata/sesongparameter (Lukket):** SARIMA rekjørt med `s=5`; `is_monday`/`days_since_last_order` i RF.
8. **R-009 Scenario 2-presentasjon (Lukket):** Kap. 8.1 presenterer sammenligning med Tabell 2 og Figur 4.

## Vurdering

Prosjektet er operativt på plan per 2026-04-16 og ligger 11 dager foran baseline for M-03. Analysen er formelt lukket (åtte modeller, to scenarier), alle seks høyprioriterte reviewtiltak og de viktigste mediumtiltakene er adressert og dokumentert i rapporten. Styringsdokumentene (`schedule.json`, `wbs.md`, `risk.json`) er synkronisert. Hovedarbeidet fremover er **kvalitativt** og **logistisk**: eksportere rapporten til delbart format, gjennomføre peer review M-05 (2026-05-01), lukke gjenværende tekstrevideringer etter tilbakemelding, og fylle formalia ved M-06. Ingen av de gjenværende oppgavene krever ny datainnhenting eller ny modellering.

---
*Oppdatert 2026-04-16 basert på arbeidskopi, `schedule.json`, `wbs.md`, `risk.json`, `review.md` og verifikasjon av rapportens kapittel- og vedleggsinnhold.*
