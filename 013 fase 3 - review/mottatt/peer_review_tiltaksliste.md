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
| Tiltak lukket | 12 av 12 (alle) |

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

- [x] Status: lukket 2026-05-04
- **Kilde:** PDF s. 2, "Metode", forbedringspunkt; oppsummering s. 6 punkt 3.
- **Mål-kapittel:** Kap. 5 (Metode) eller kap. 6 (Modellering), før resultatene presenteres.
- **Handling:** Eget avsnitt eller boks som eksplisitt sier at SARIMA/Holt-Winters lager multi-step-prognose uten oppdatering, mens RF/GBM bruker faktiske observerte lag-verdier (én-steg-frem). Modellene konkurrerer dermed ikke på helt like vilkår, og dette må tas i betraktning ved tolkning av hvilken modell som er "best".
- **Lukket:** Konsekvensavsnittet i kap. 6.4 (`Prosjektrapport_LOG650_G27.md` l. 423) er omformulert med eksplisitt "modellene konkurrerer ikke på helt like vilkår" og kobling til "hvilken modell som fremstår som best i de aggregerte feilmålene". I tillegg lagt til kort påminnelse i åpningen av kap. 8 (l. 458–460) om protokollforskjellen, før tabellene presenteres, slik G26 ba om "før resultatene".

### T-03: Tabellnummerering og kryssreferanser kvalitetssikres

- [x] Status: lukket 2026-05-04
- **Kilde:** PDF s. 3, "Analyse og resultater"; oppsummering s. 6 punkt 10.
- **Mål-kapittel:** Hele rapporten, men særlig start av kap. 8 (resultater).
- **Konkret feil G26 fant:** Tekst i kap. 8 starter med "Tabell 2, 3 og 4", men de reelle tabellene som vises er Tabell 5–9.
- **Handling:** Gå gjennom alle tabell- og figurreferanser i kap. 1–10, sammenlign med faktisk nummerering, oppdater eventuelle inkonsistenser.
- **Lukket:** Renummerering gjennomført. Duplikatene "Tabell 2" (kap. 5 og 8.1) og "Tabell 4" (kap. 6 og 8.3) er løst. Ny sekvens: Tabell 1 (kap. 4), Tabell 2 (kap. 5), Tabell 3 (kap. 6 modeller), Tabell 4 (kap. 8.1 MAE per scenario), Tabell 5 (kap. 8.2 global), Tabell 6 og 6b (kap. 8.3 segmentert + SARIMA-sammenligning), Tabell 7 (kap. 8.4 Ljung-Box). Krysshenvisninger i kap. 9.3, 9.6 og vedlegg A7 oppdatert. Innledningssetningen i kap. 8 er omformulert til generisk "resultattabellene" siden den uansett refererte feil tabeller.

### T-04: APA 7-format kvalitetssikres i bibliografien

- [x] Status: lukket 2026-05-04
- **Kilde:** PDF s. 4, "Skriveflyt"; oppsummering s. 6 punkt 11.
- **Mål-kapittel:** Kap. 11 (Bibliografi).
- **Handling:** Sammenlign formatet i bibliografien mot `000 templates/Referansestiler/APA 7th norsk v1.12.pdf`. Vurder å fjerne kulepunkter, sjekk hengemarg, formatering av forfatternavn, journals, DOI-er. Den interne reviewen (review_kap_11-12.md) lukket allerede flere APA-tiltak — sjekk hva som gjenstår.
- **Lukket:** Bibliografien har ingen kulepunkter (allerede ren APA-stil — G26s kommentar gjaldt "vurder å fjerne dersom"). Sentence-case rettet i fire titler som tidligere var i title case: McKinney (2010), Pedregosa et al. (2011), Seabold & Perktold (2010), og Seiringer et al. (2022). De øvrige 13 referansene var allerede i sentence case. Hengemargs-rendering håndteres av docx-/pdf-konvertering, ikke i kildedokument. Volum-italic-konvensjon (APA 7-norm "*Journal, vol*(issue)") er ikke endret — gjeldende stil med italic kun på journalnavn er konsekvent gjennomført og akseptabel mot Norsk APA 7 v1.12. Anthropic/AI-henvisning ikke til stede i denne rapporten (var en kommentar om medstudentens rapport).

### T-05: Etikk, personvern og konfidensialitet omtales

- [x] Status: lukket 2026-05-04
- **Kilde:** PDF s. 2, "Metode"; oppsummering s. 6 punkt 5.
- **Mål-kapittel:** Kap. 5 (Metode), egen kort seksjon (f.eks. 5.x "Etiske hensyn og konfidensialitet").
- **Handling:** Forklar kort: data er aggregert/anonymisert, taushetserklæring er signert, hvor data er lagret og hvordan de behandles. G26 bemerker at rapporten er sterk på reliabilitet og datakvalitet, men svakere på etikk.
- **Lukket:** Ny seksjon "5.5 Etiske hensyn og konfidensialitet" lagt til. Dekker (1) taushetserklæring signert med REMA, (2) ingen kunde-/ansatt-/persondata → GDPR ikke direkte berørt, (3) data forretningssensitive og lagret lokalt, (4) deling kun via aggregater og avidentifiserte mellomprodukter, (5) bedriftsspesifikke kampanjedetaljer balansert mot etterprøvbarhet. Renummerert: gamle 5.5 → 5.6 (Oppdeling), 5.6 → 5.7 (Evalueringsmål), 5.7 → 5.8 (Oppsummering). Kryssreferanser oppdatert i kap. 1.2 (delproblem 2), kap. 2 (åpningsavsnitt), kap. 6 (åpning), og kap. 7.3.

### T-06: Konklusjon må eksplisitt svare på delproblem 1

- [x] Status: lukket 2026-05-04
- **Kilde:** PDF s. 4, "Konklusjon"; oppsummering s. 6 punkt 9.
- **Mål-kapittel:** Kap. 10 (Konklusjon).
- **Handling:** Konklusjonen omtaler i dag særlig delproblem 2 og 3. Legg til kort avsnitt som svarer på delproblem 1 (historiske etterspørselsmønstre): lavt normalvolum, høy variasjonskoeffisient, tydelig virkedagseffekt, kraftige kampanjetopper. G26 foreslår en mer konsis konklusjon — vurder samtidig om noen formuleringer kan strammes.
- **Lukket:** Åpningsparagraf utvidet til å nevne alle tre delproblemene. Nytt hovedpunkt 1 "Etterspørselsmønsteret er kampanjedrevet med lavt normalvolum (delproblem 1)" lagt til med konkrete tall fra Tabell 2 (median 19,5 stk, snitt 61,1 stk, std 239,3 stk, maks 2 172 stk), virkedagseffekt med ACF-referanse og kobling til Syntetos & Boylan (2005) sin "lumpy demand"-kategorisering. Eksisterende hovedpunkter renummerert til 2–6, og delproblem-merking lagt til på punkt 2 og 3. Avslutningssetning oppdatert fra "tidsserie-baserte metoder" til "parallell bruk av tidsserie- og maskinlæringsbaserte modeller" for konsistens med ny problemstilling. Ytterligere stramming av konklusjonen er ikke gjort — vurderes som lavprioritet under T-08 (resultat/diskusjon-rydd) hvis tid før M-04.

---

## Tiltak — prioritet "Bør" (gjøres hvis tid før M-04)

### T-07: Symbol-/variabeltabell i modellkapittel

- [x] Status: lukket 2026-05-04
- **Kilde:** PDF s. 3, "Modellering"; oppsummering s. 6 punkt 4.
- **Mål-kapittel:** Kap. 6 (Modellering), tidlig i kapittelet.
- **Handling:** Legg inn kort tabell som forklarer y_t, lag_1, lag_5, rolling_mean_5, is_crazy_days, is_event, og terskelverdien 70,6. Hjelper lesere uten dyp tidsserie-bakgrunn.
- **Lukket:** Variabeloversikt lagt til i kap. 6.4 mellom feature-vektor-paragrafen og evalueringsprotokollen. Dekker $y_t$, lag_1/5/10, rolling_mean_5, kalenderfeatures (is_monday, month, week_of_month, days_since_last_order), kampanjeflagg (is_crazy_days, is_event), SARIMA-parameterstruktur og terskelverdi 70,6. Tabellen er presentert som unummerert "Variabeloversikt" (i stedet for "Tabell 4") for å unngå renummerering av eksisterende Tabell 4–7 etablert under T-03.

### T-08: Resultat og diskusjon ryddes (separasjon)

- [x] Status: lukket 2026-05-04
- **Kilde:** PDF s. 3, "Analyse og resultater"; oppsummering s. 6 punkt 7.
- **Mål-kapittel:** Kap. 8 (Resultater) og kap. 9 (Diskusjon).
- **Handling:** Identifisér steder i kap. 8 der det trekkes konklusjoner om operasjonell robusthet eller modellvaliditet, og vurder å flytte slike vurderinger til kap. 9. Resultatdelen bør holde seg objektiv.
- **Lukket:** Tre tolkningsblokker fjernet/komprimert i kap. 8 (kap. 8.2 "operasjonelt attraktivt" fjernet; kap. 8.3 Seiringer-referanse og "viktig resultat" flyttet, strukturforklaring om |Bias|=MAE på toppdager flyttet til kap. 9.3; kap. 8.4 "sterkt argument for validitet selv om SARIMA har bedre MAE" trimmet). Kap. 9.3 utvidet med strukturforklaring av tidsseriemodellenes systematiske toppdag-underestimering. Resultattabellene og observasjonene står som før — kun tolknings- og verdivurderingssetninger ble flyttet/trimmet.

### T-09: Generaliserbarhet diskuteres bredere

- [x] Status: lukket 2026-05-04
- **Kilde:** PDF s. 3–4, "Diskusjon"; oppsummering s. 6 punkt 8.
- **Mål-kapittel:** Kap. 9 (Diskusjon), generaliserbarhetsavsnitt.
- **Handling:** Kort drøfting: gjelder funnene andre kampanjedrevne tørrvarer? Ferskvarer? Frossenvarer? Produkter med jevnere etterspørsel? Tydeliggjør grenser for overførbarhet.
- **Lukket:** Ny "femte begrensning" lagt til i kap. 9.6 som drøfter generaliserbarhet langs tre dimensjoner: (1) andre kampanjedrevne tørrvarer (sannsynligvis robust), (2) ferskvarer med kort holdbarhet (etterspørselssignal mer forbruksdrevet, modellrangering kan endres), (3) produkter med jevnere etterspørsel uten lumpy-komponent (segmentert tilnærming mister verdi). Eksisterende "siste betraktning" om kampanjekalender renummerert til "sjette betraktning".

### T-10: Kampanjeflagg-begrensning kobles tydeligere til modell-feil

- [x] Status: lukket 2026-05-04
- **Kilde:** PDF s. 3 (Diskusjon); oppsummering s. 6 punkt 12.
- **Mål-kapittel:** Kap. 9 (Diskusjon), eventuelt kap. 8 (Resultater).
- **Handling:** Rapporten sier at binært kampanjeflagg er for grovt — kobl dette tydeligere til *hvorfor* modellene feiler på toppdager (manglende kampanjeintensitet, type, varighet i features).
- **Lukket:** Nytt mekanismeavsnitt lagt til i kap. 9.2 som eksplisitt forklarer kjeden: binært flagg → uniform koding av heterogene kampanjer (Crazy Days vinter > 1 300 stk vs. mindre hendelse 200–400 stk under samme verdi 1) → middelnivå-prediksjon → topp-spesifikke residualer. Avsnittet binder eksplisitt sammen kampanjerepresentasjons-svakheten med toppdag-feilen og grunngir anbefalingen om rikere kampanjedata.

---

## Tiltak — prioritet "Kan vurderes"

### T-11: Skille metode/modellering strammes

- [x] Status: lukket 2026-05-04
- **Kilde:** PDF oppsummering s. 6 punkt 2.
- **Mål-kapittel:** Kap. 5 (Metode) og kap. 6 (Modellering).
- **Vurdering:** Større omflytting kan skape mye churn så sent i prosjektet. Hvis det gjøres, bør det være kirurgisk og målrettet, ikke en omskriving.
- **Lukket:** To kirurgiske endringer gjennomført. (1) Evalueringsprotokoll flyttet fra kap. 6.4 til ny kap. 5.7, slik at multi-step vs. én-steg-frem-distinksjonen står som metodisk kapittel-nivå-valg fremfor som avsnitt i modellspesifikasjon. Renummerert: 5.7 Evalueringsmål → 5.8, 5.8 Oppsummering → 5.9. Kort peker satt inn i 6.4. Kryssreferanser oppdatert i kap. 1.2 (l. 59), kap. 2 (l. 79) og kap. 8-påminnelsen. (2) Kap. 5.2 "Den analytiske prosessen" strammet til ren oversikt — fjernet teknikk-detaljer (grid-search 144 kombinasjoner, TimeSeriesSplit 3-fold, Ljung-Box-test og ADF-test med inline-definisjoner), erstattet med kapittel-pekere til kap. 6, 7.1, 7.2, 7.4, 5.7 og 5.8. Litteraturreferanser (Ljung & Box 1978, Dickey & Fuller 1979, Hyndman & Koehler 2006) flyttet bort fra 5.2 — alle er fortsatt sitert in-text der teknikkene faktisk anvendes.

### T-12: Reduser overlapp litteratur/teori

- [x] Status: lukket 2026-05-04
- **Kilde:** PDF s. 2; oppsummering s. 6 punkt 6.
- **Mål-kapittel:** Kap. 2 (Litteratur) og kap. 3 (Teori).
- **Vurdering:** G26 nevner særlig overlapp i prognosemetoder og feilmål. Vurder kirurgisk fjerning av duplikat-omtaler heller enn full omstrukturering.
- **Lukket:** Skarpere skille mellom kap. 2 (empirisk syntese) og kap. 3 (formler og operasjonalisering). Tre kirurgiske trim i kap. 3: (1) 3.1 fjernet utvidet Syntetos & Boylan-utdypning (CV² > 0,49 og ADI > 1,32) — beholdt "Lumpy Demand"-begrepet med peker til kap. 2.1. (2) 3.3 ved MAPE-formelen fjernet Hyndman & Koehler-advarselsavsnitt — erstattet med kort peker "ustabil ved lavt volum (jf. kap. 2.3)". (3) 3.3 ved Bias-formelen fjernet Seiringer-referanse-paragraf — erstattet med "Operasjonell betydning er drøftet i kap. 2.3 og kap. 9.4". Kap. 2 forblir urørt; ingen kilder forsvinner fra in-text-siteringer (begge fortsatt sitert i kap. 2.3, og Hyndman & Koehler i kap. 8.2-figurtekst og kap. 9.1, Seiringer i kap. 5.8 og kap. 9.4). Kap. 3 leser nå tettere som ren formel- og operasjonaliseringsguide.

---

## Lukkelogg

- **T-01 lukket 2026-05-04:** Problemstilling utvidet fra "tidsserie-baserte prognosemetoder" til "tidsserie- og maskinlæringsbaserte prognosemodeller" i `Prosjektrapport_LOG650_G27.md` (l. 19 sammendrag, l. 43 innledning, l. 50 problemstilling) og parallell `.tex` (l. 73, 87, 95). Delproblem 2 (l. 59) hadde allerede konsistent formulering. Konklusjons-setning revidert under T-06.
- **T-02 lukket 2026-05-04:** Konsekvensavsnittet i kap. 6.4 omformulert med eksplisitt "modellene konkurrerer ikke på helt like vilkår" og kobling til "best i de aggregerte feilmålene". Kort påminnelse om protokollforskjell lagt til i åpningen av kap. 8 før tabellene presenteres.
- **T-03 lukket 2026-05-04:** Tabell-renummerering for å løse duplikater (Tabell 2 i kap. 5 og 8.1, Tabell 4 i kap. 6 og 8.3). Ny sekvens: T1 (kap. 4), T2 (kap. 5), T3 (kap. 6), T4 (kap. 8.1), T5 (kap. 8.2), T6/T6b (kap. 8.3), T7 (kap. 8.4). Krysshenvisninger i kap. 9.3, 9.6 og vedlegg A7 oppdatert.
- **T-04 lukket 2026-05-04:** Sentence-case rettet i fire bibliografiposter (McKinney 2010, Pedregosa et al. 2011, Seabold & Perktold 2010, Seiringer et al. 2022). Ingen kulepunkter å fjerne; volum-italic-konvensjon vurdert konsekvent og akseptabel.
- **T-05 lukket 2026-05-04:** Ny seksjon "5.5 Etiske hensyn og konfidensialitet" lagt til. Renummerert: 5.5→5.6, 5.6→5.7, 5.7→5.8. Kryssreferanser oppdatert i kap. 1.2, 2, 6 og 7.3.
- **T-06 lukket 2026-05-04:** Åpningsparagraf utvidet med delproblem 1, nytt hovedpunkt 1 om etterspørselsmønsteret med konkrete tall og Syntetos & Boylan-referanse. Eksisterende punkter renummerert 2–6 med delproblem-merking på 2 og 3. Avslutningssetning oppdatert for konsistens med ny problemstilling.
- **T-07 lukket 2026-05-04:** Variabeloversikt lagt til i kap. 6.4 (12 variabler/symboler dekket: $y_t$, lag-features, rolling_mean, kalenderfeatures, kampanjeflagg, SARIMA-parametre, terskelverdi). Unummerert for å unngå renummerering av Tabell 4–7.
- **T-08 lukket 2026-05-04:** Tre tolkningsblokker fjernet/komprimert i kap. 8.2, 8.3 og 8.4 (operasjonelle/normative vurderinger, Seiringer-referanse, "viktig resultat"-formuleringer). Strukturforklaring av tidsseriemodellenes systematiske toppdag-underestimering flyttet til kap. 9.3.
- **T-09 lukket 2026-05-04:** Ny femte begrensning om generaliserbarhet i kap. 9.6: drøfter overføring til andre tørrvarer (sannsynlig), ferskvarer (modellrangering kan endres) og produkter uten lumpy-komponent (segmentert tilnærming mister verdi). Eksisterende kampanjekalender-betraktning renummerert til sjette.
- **T-10 lukket 2026-05-04:** Mekanismeavsnitt lagt til i kap. 9.2 som eksplisitt binder binær-flagg-svakhet (uniform koding av heterogene kampanjer) til topp-spesifikke residualer.
- **T-11 lukket 2026-05-04:** Evalueringsprotokoll flyttet fra kap. 6.4 til ny kap. 5.7. Renummerert: 5.7→5.8 (Evalueringsmål), 5.8→5.9 (Oppsummering). Kryssreferanser i kap. 1.2, 2 og kap. 8-påminnelsen oppdatert. Kap. 5.2 strammet til ren oversikt med kapittel-pekere; teknikk-detaljer fjernet og litteraturreferanser flyttet til der teknikkene anvendes.
- **T-12 lukket 2026-05-04:** Tre kirurgiske trim i kap. 3 for skarpere skille mot kap. 2 (empirisk syntese vs. formler og operasjonalisering): (1) 3.1 lumpy demand-utdypning trimmet, (2) 3.3 Hyndman & Koehler MAPE-advarsel fjernet til peker, (3) 3.3 Seiringer bias-referanse fjernet til peker. Kap. 2 urørt; alle kilder fortsatt in-text-sitert flere steder.
