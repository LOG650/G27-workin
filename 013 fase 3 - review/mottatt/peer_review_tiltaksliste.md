# Tiltaksliste — peer review fra G26 (Hovden & Lunde)

**Dato mottatt:** 2026-05-03
**Kilde:** `013 fase 3 - review/mottatt/Peer-review_Rema1000.pdf`
**Vurderende gruppe:** G26 (Tord Hovden, David Johan Lunde)
**Rapportfil som revideres:** `014 fase 4 - report/Prosjektrapport_LOG650_G27.md`
**Formål:** Strukturert klassifisering og lukking av forbedringspunktene fra mottatt peer review (ACT-10 / M-05).

---

## Sammendrag

| Punkt | Status |
|---|---|
| Reviewen lest og klassifisert | Ja, 2026-05-04 |
| Antall styrker identifisert av G26 | 12 (krever ingen tiltak — bekrefter sterke sider) |
| Antall forbedringspunkter | 12, fordelt på 6 må / 4 bør / 2 kan vurderes |
| Helhetsvurdering fra G26 | "Sterk rapport med høy faglig og teknisk kvalitet" |
| Tiltak lukket | 1 av 12 (T-01) |

**G26s helhetsvurdering:** Reviewen kaller rapporten samlet sett en sterk rapport. Forbedringspunktene er primært finsliping (problemstillingsformulering, kapittelgrenser, formelle ryddetiltak). Ingen punkter krever ny analyse, modellering eller dataarbeid.

---

## Styrker fremhevet av G26 (referanse, ingen tiltak)

1. Tydelig praktisk relevans for REMA 1000.
2. God kobling mellom prognose og operasjonelle konsekvenser (lagerbinding, stock-outs, bemanning, transport).
3. Konkret problemstilling med tydelige avgrensninger (ett produkt, én lokasjon, én periode).
4. Sterkt datagrunnlag — RELEX×ERP-kryssjekk og dokumentert datafeil-korrigering trekkes spesielt frem.
5. God forklaring av etterspørselsmønsteret (lavt normalvolum, høy variasjon, kraftige kampanjetopper).
6. Bredt modellutvalg (baselines, statistisk, ML, hybrid).
7. Segmentering normale dager vs. toppdager — kalt "klar styrke".
8. Flere evalueringsmål (MAE, MAPE, sMAPE, WAPE, Bias).
9. Ærlig metodisk refleksjon om datafeil, testperiode, overdifferensiering.
10. Konkrete praktiske anbefalinger til REMA.
11. God figur- og tabellbruk.
12. Relevant litteraturgrunnlag.

---

## Tiltak — prioritet "Må" (lukkes før M-05)

### T-01: Justér problemstilling så den matcher modellutvalget

- [x] Status: lukket 2026-05-04
- **Kilde:** PDF s. 1, "Innledning", forbedringspunkt 1; oppsummering s. 6 punkt 1.
- **Mål-kapittel:** Kap. 1 (Innledning), problemstillingsformulering.
- **Forslag fra G26:** "I hvilken grad kan tidsserie- og maskinlæringsbaserte prognosemodeller predikere daglig etterspørsel for ett utvalgt produkt ved REMA 1000 Distribusjon Trondheim?"
- **Handling:** Endre formuleringen i kap. 1 og verifisér at samme formulering er konsistent brukt i sammendrag og konklusjon.
- **Lukket:** Problemstillingen oppdatert i `Prosjektrapport_LOG650_G27.md` l. 50 (og parallell .tex l. 95) til G26s foreslåtte formulering, med beholdt operasjonalisering "målt ved prognosepresisjon (forecast accuracy)". Oppfølgings-formuleringer i sammendrag (l. 19 / .tex l. 73) og innledningens åpningsavsnitt (l. 43 / .tex l. 87) utvidet til "tidsserie- og maskinlæringsbaserte modeller". Delproblem 2 (l. 59) brukte allerede "tidsserie-baserte og maskinlæringsbaserte" — ingen endring nødvendig. Setningen i konklusjon (l. 668 / .tex l. 792) "tidsserie-baserte metoder gir akseptabel presisjon i normaldrift" er bevart fordi det er en finding-statement om at SARIMA (en tidsserie-modell) fungerer i normaldrift, ikke en scope-statement; revurderes ev. under T-06.

### T-02: Multi-step vs. én-steg-frem-forskjell løftes tydeligere

- [ ] Status: åpen
- **Kilde:** PDF s. 2, "Metode", forbedringspunkt; oppsummering s. 6 punkt 3.
- **Mål-kapittel:** Kap. 5 (Metode) eller kap. 6 (Modellering), før resultatene presenteres.
- **Handling:** Eget avsnitt eller boks som eksplisitt sier at SARIMA/Holt-Winters lager multi-step-prognose uten oppdatering, mens RF/GBM bruker faktiske observerte lag-verdier (én-steg-frem). Modellene konkurrerer dermed ikke på helt like vilkår, og dette må tas i betraktning ved tolkning av hvilken modell som er "best".

### T-03: Tabellnummerering og kryssreferanser kvalitetssikres

- [ ] Status: åpen
- **Kilde:** PDF s. 3, "Analyse og resultater"; oppsummering s. 6 punkt 10.
- **Mål-kapittel:** Hele rapporten, men særlig start av kap. 8 (resultater).
- **Konkret feil G26 fant:** Tekst i kap. 8 starter med "Tabell 2, 3 og 4", men de reelle tabellene som vises er Tabell 5–9.
- **Handling:** Gå gjennom alle tabell- og figurreferanser i kap. 1–10, sammenlign med faktisk nummerering, oppdater eventuelle inkonsistenser.

### T-04: APA 7-format kvalitetssikres i bibliografien

- [ ] Status: åpen
- **Kilde:** PDF s. 4, "Skriveflyt"; oppsummering s. 6 punkt 11.
- **Mål-kapittel:** Kap. 11 (Bibliografi).
- **Handling:** Sammenlign formatet i bibliografien mot `000 templates/Referansestiler/APA 7th norsk v1.12.pdf`. Vurder å fjerne kulepunkter, sjekk hengemarg, formatering av forfatternavn, journals, DOI-er. Den interne reviewen (review_kap_11-12.md) lukket allerede flere APA-tiltak — sjekk hva som gjenstår.

### T-05: Etikk, personvern og konfidensialitet omtales

- [ ] Status: åpen
- **Kilde:** PDF s. 2, "Metode"; oppsummering s. 6 punkt 5.
- **Mål-kapittel:** Kap. 5 (Metode), egen kort seksjon (f.eks. 5.x "Etiske hensyn og konfidensialitet").
- **Handling:** Forklar kort: data er aggregert/anonymisert, taushetserklæring er signert, hvor data er lagret og hvordan de behandles. G26 bemerker at rapporten er sterk på reliabilitet og datakvalitet, men svakere på etikk.

### T-06: Konklusjon må eksplisitt svare på delproblem 1

- [ ] Status: åpen
- **Kilde:** PDF s. 4, "Konklusjon"; oppsummering s. 6 punkt 9.
- **Mål-kapittel:** Kap. 10 (Konklusjon).
- **Handling:** Konklusjonen omtaler i dag særlig delproblem 2 og 3. Legg til kort avsnitt som svarer på delproblem 1 (historiske etterspørselsmønstre): lavt normalvolum, høy variasjonskoeffisient, tydelig virkedagseffekt, kraftige kampanjetopper. G26 foreslår en mer konsis konklusjon — vurder samtidig om noen formuleringer kan strammes.

---

## Tiltak — prioritet "Bør" (gjøres hvis tid før M-04)

### T-07: Symbol-/variabeltabell i modellkapittel

- [ ] Status: åpen
- **Kilde:** PDF s. 3, "Modellering"; oppsummering s. 6 punkt 4.
- **Mål-kapittel:** Kap. 6 (Modellering), tidlig i kapittelet.
- **Handling:** Legg inn kort tabell som forklarer y_t, lag_1, lag_5, rolling_mean_5, is_crazy_days, is_event, og terskelverdien 70,6. Hjelper lesere uten dyp tidsserie-bakgrunn.

### T-08: Resultat og diskusjon ryddes (separasjon)

- [ ] Status: åpen
- **Kilde:** PDF s. 3, "Analyse og resultater"; oppsummering s. 6 punkt 7.
- **Mål-kapittel:** Kap. 8 (Resultater) og kap. 9 (Diskusjon).
- **Handling:** Identifisér steder i kap. 8 der det trekkes konklusjoner om operasjonell robusthet eller modellvaliditet, og vurder å flytte slike vurderinger til kap. 9. Resultatdelen bør holde seg objektiv.

### T-09: Generaliserbarhet diskuteres bredere

- [ ] Status: åpen
- **Kilde:** PDF s. 3–4, "Diskusjon"; oppsummering s. 6 punkt 8.
- **Mål-kapittel:** Kap. 9 (Diskusjon), generaliserbarhetsavsnitt.
- **Handling:** Kort drøfting: gjelder funnene andre kampanjedrevne tørrvarer? Ferskvarer? Frossenvarer? Produkter med jevnere etterspørsel? Tydeliggjør grenser for overførbarhet.

### T-10: Kampanjeflagg-begrensning kobles tydeligere til modell-feil

- [ ] Status: åpen
- **Kilde:** PDF s. 3 (Diskusjon); oppsummering s. 6 punkt 12.
- **Mål-kapittel:** Kap. 9 (Diskusjon), eventuelt kap. 8 (Resultater).
- **Handling:** Rapporten sier at binært kampanjeflagg er for grovt — kobl dette tydeligere til *hvorfor* modellene feiler på toppdager (manglende kampanjeintensitet, type, varighet i features).

---

## Tiltak — prioritet "Kan vurderes"

### T-11: Skille metode/modellering strammes

- [ ] Status: åpen — vurderes, kan medføre større omstrukturering
- **Kilde:** PDF oppsummering s. 6 punkt 2.
- **Mål-kapittel:** Kap. 5 (Metode) og kap. 6 (Modellering).
- **Vurdering:** Større omflytting kan skape mye churn så sent i prosjektet. Hvis det gjøres, bør det være kirurgisk og målrettet, ikke en omskriving.

### T-12: Reduser overlapp litteratur/teori

- [ ] Status: åpen — vurderes, kan medføre større omskriving
- **Kilde:** PDF s. 2; oppsummering s. 6 punkt 6.
- **Mål-kapittel:** Kap. 2 (Litteratur) og kap. 3 (Teori).
- **Vurdering:** G26 nevner særlig overlapp i prognosemetoder og feilmål. Vurder kirurgisk fjerning av duplikat-omtaler heller enn full omstrukturering.

---

## Lukkelogg

- **T-01 lukket 2026-05-04:** Problemstilling utvidet fra "tidsserie-baserte prognosemetoder" til "tidsserie- og maskinlæringsbaserte prognosemodeller" i `Prosjektrapport_LOG650_G27.md` (l. 19 sammendrag, l. 43 innledning, l. 50 problemstilling) og parallell `.tex` (l. 73, 87, 95). Delproblem 2 (l. 59) hadde allerede konsistent formulering. Konklusjons-setning l. 668 bevart som finding-statement.
