# Intern review av Prosjektrapport_LOG650_G27 — kap. 4 (Casebeskrivelse og datagrunnlag)

**Dato:** 2026-04-29
**Reviewer:** Intern gjennomgang (Claude Code-assistert)
**Rapportfil:** `014 fase 4 - report/Prosjektrapport_LOG650_G27.md`
**Formål:** Strukturert kvalitetsvurdering av kapittel 4 (Casebeskrivelse og datagrunnlag) før innlevering.

---

## Sammendrag og status

| Punkt | Status |
|---|---|
| Kap. 4 vurdert | Ja |
| Tiltak besluttet | Alle prioritet 1, 2 og 3 unntatt F1 (avventer manuell gjennomgang av totalsummer) |

**Hovedfunn:** Kapittelet er strukturelt godt komponert og dekker alle krav fra CLAUDE.md §11. Største faglige svakhet er inkonsistens i totalsummer mellom RELEX og ERP (F1), som behandles separat. Resterende endringer omfatter standardisering av forkortelser, mindre språklige presiseringer og typografi.

---

## 1. Språkvurdering

**Forkortelser og terminologi (inkonsistens):**
- Distribusjonssenteret omtales på fire måter i kapittelet: «REMA 1000 Distribusjon Trondheim», «RD Trondheim», «RDT» (introdusert linje 165), og «DC» (engelsk, linje 184/253). RDT introduseres formelt, men brukes deretter knapt; «RD Trondheim»/«DC» tar over. Bør standardiseres.
- «PK» (produkt-kategoriansvarlig) introduseres i 4.1 (linje 169) og brukes igjen i 4.5 (linje 272), men selve sammensetningen «produkt-kategoriansvarlig» har ikke-standard bindestrek (norsk standard: «produktkategoriansvarlig»). Tilsvarende inkonsistens som bindestrekrettelsene i kap. 1.

**Engelske termer uten parallell norsk forklaring:**
- «stock-outs» brukes første gang i 4.1 (linje 175) i parentes etter «tomme hyller», men gjentas i 4.6 alene (linje 277).
- «"pushes" ut til butikkene» (linje 171) — engelsk hjelpeverb i anførselstegn er informativt, men en norsk parafrasering («distribueres aktivt», «sentralt allokeres») hadde gitt mer akademisk presisjon.
- «pre-campaign stocking» (linje 268) brukes uten oversettelse, selv om mekanismen er forklart godt i avsnittet.

**Skrivefeil og tegnsetting:**
- Ingen åpenbare grammatiske feil identifisert.
- Fet skrift midt i et flytende avsnitt (linje 169) er typografisk uvanlig og avviker fra rapportens øvrige stil.

## 2. Innholdsvurdering (per underkapittel)

### 4 Innledning
Kort, presis, etablerer formålet.

### 4.1 REMA 1000 Distribusjon Trondheim og beslutningssituasjonen
Sterk struktur med to underseksjoner («Bestillings- og leveranseprosess», «Beslutningssituasjoner»). Mandagseffekten introduseres tidlig og kobles til kap. 4.4 — bra rød tråd.

**Faglig styrke:** Påstanden om at «butikkene godkjenner nærmere 100 % av forslagene uten endring» for tørre og frosne varer er kritisk for å motivere prognosens operative betydning, og brukes igjen i 4.6, 8.2 og 9.5.

### 4.2 Produktbeskrivelse: Lasagne Familiepakning
Knapp, men tilstrekkelig. Et par presiseringer mangler:
- «Pallestørrelse i RELEX er 115 stk per D-pakning» (linje 181) — termen «D-pakning» er bransjeterminologi (sannsynligvis displaypakning) som ikke er forklart for leseren. Sammensatt med «pallestørrelse» blir setningen tvetydig: er 115 stk pallekvantum eller D-pakning-kvantum?
- Setningen står løsrevet på slutten av 4.2 og kobles ikke videre til analysen, ettersom modelleringen skjer i stk, ikke pall/D-pakning.

### 4.3 Beskrivelse av datagrunnlaget
Strukturelt godt: kilde, datatype, periode, variabel som punktliste; deretter virkedagsfiltrering, helgesalg-håndtering og ERP-kryssjekk.

**Kritisk faglig svakhet — totalsummene er ikke koherente på tvers av kapittelet:**

| Kilde | Sum | Hvor |
|---|---|---|
| RELEX aggregert (alle 365 dager) | 20 801 | 4.3 linje 195 |
| RELEX virkedager (Tabell 1) | 20 701 | 4.3 linje 204 |
| ERP `Bestilt antall` | 20 934 | 4.3 linje 195, 4.4 linje 253 |
| ERP `Justert antall` | 20 697 | 4.3 linje 195, 4.4 linje 253 |
| «Faktisk utlevert» | 20 697 | 4.4 linje 253 |

Dette skaper to problemer:
1. **«Faktisk utlevert» = 20 697 stk** i 4.4 motsier RELEX-summen 20 801 stk i 4.3, der RELEX nettopp er definert som «utlevert volum». ERP `Justert antall` og RELEX *burde* være tilnærmet identiske mål, men avviker med 104 stk.
2. **Avviksprosenter er beregnet mot ulike basis:** 0,6 % (i 4.3) vs 1,1 % (i 4.4). Begge tall er korrekt regnet, men introduserer unødvendig forvirring.

**Mindre presisering:** «Variabel: `Salg (stk)` per dag, tolket som utlevert volum.» — variabelen heter «Salg» i RELEX, men i denne studiens kontekst er det B2B-utlevering DC → butikk, ikke butikkens salg til sluttkunde. Forskjellen er viktig fordi «etterspørsel» (kap. 1.4) er definert mot butikkens behov, ikke sluttkundens.

### 4.4 Etterspørselsmønstre og visualisering
**Sterk introduksjon av Figur 1, 2 og 3** — alle figurer er introdusert *før* de vises (tråd med CLAUDE.md §7). Fallende ukedagsprofil (mandag → fredag) er forklart presist med koblingen til helgeakkumulering.

**Fin innsikt:** Skille mellom *bestillingsdato* (onsdag dominant) og *plukk-/leveringsdato* (mandag dominant) er kapittelets pedagogiske høydepunkt og motiverer hvorfor det er plukkdato modellene predikerer.

**Strukturell merknad:** Avsnittet om bestillingsdato vs leveringsdato (fra «Det er viktig å skille...» linje 243 til linje 253) er innholdsmessig en *seksjon for seg* og kunne fortjent en egen liten overskrift for å markere bruddet med ukedagseffekten på utleveringssiden.

### 4.5 Kampanjemekanikk og salgstopper
**Faglig sterkeste underkapittel.** Pre-campaign stocking er presist forklart, og diskrepansen mellom kampanjeuken og uken før er empirisk dokumentert (uke 44: 7 131 stk vs uke 45: 504 stk).

**Faglig styrke:** Det negative funnet «ingen julespike» er rapportert ærlig og forklart med plausibel mekanisme.

**Konsistens med kap. 1.4:** «Censored Demand»-diskusjonen (linje 272) repeterer antagelsen fra 1.4 og 4.3, men gir nå *empirisk fundament* (ingen flate platåer, lager aldri utsolgt). God progresjon: antagelse i 1.4 → kort begrunnelse i 4.3 → full dokumentasjon i 4.5 + Vedlegg A8.

### 4.6 Konsekvenser og behov for modeller
Knapp og effektiv. Tre punkter (stock-outs, lagerbinding, uforutsigbarhet) er tilstrekkelige.

**Strukturell forbedring:** Avsnittet ender med «Dette danner grunnlaget for modellvalget i kap. 6.», men kap. 5 (Metode) ligger imellom. Mer presist: «Dette danner grunnlaget for metode (kap. 5) og modellvalg (kap. 6).»

## 3. Identifiserte svakheter (status og tiltak)

### Faglige svakheter
- **F1: Inkonsistente totalsummer** (20 697 vs 20 701 vs 20 801 vs 20 934). Lag en samlet oversikt i 4.3 og bruk konsekvent terminologi. **Status: utsatt — bruker går manuelt gjennom tallene først.**
- **F2: «D-pakning» ikke forklart** (4.2 linje 181). Forklare termen eller fjerne setningen hvis pall-/D-pakning ikke brukes videre i analysen. **Status: rettes nå.**
- **F3: «Salg» vs B2B-utlevering** (4.3 linje 189). Presisere at `Salg (stk)` her betyr DC → butikk-utlevering. **Status: rettes nå.**

### Metodiske svakheter
- **M1: Avviksprosent 1,1 % i 4.4 vs 0,6 % i 4.3.** Bruke samme prosentvise avvik konsekvent, eller forklare valg av basis. **Status: rettes nå.**

### Strukturelle svakheter
- **S1: Forkortelses-inkonsistens** (RDT/RD Trondheim/DC). Velge én primærform. **Status: rettes nå.**
- **S2: Bestillingsdato-avsnittet i 4.4 mangler underoverskrift**. **Status: rettes nå.**
- **S3: «Pallestørrelse»-setningen** (4.2 linje 181) er løsrevet. **Status: rettes nå (sammen med F2).**
- **S4: Overgangsformuleringen 4.6 → 5/6** (linje 280) hopper over kap. 5. **Status: rettes nå.**

### Formidling og typografi
- **K1: Bindestrek i «produkt-kategoriansvarlig»** (4.1 linje 169, 4.5 linje 272) → «produktkategoriansvarlig». **Status: rettes nå.**
- **K2: Fet skrift midt i flytende avsnitt** (linje 169). **Status: rettes nå.**
- **K3: «pushes»** (linje 171) → norsk parafrasering. **Status: rettes nå.**

## 4. Samsvar med CLAUDE.md §11 (Kapittel 4)

| Krav i CLAUDE.md §11 | Dekket | Hvor |
|---|---|---|
| Beslutningssituasjon | Ja | 4.1, 4.6 |
| Data: type, periode, representasjon, visualisering | Ja | 4.3, 4.4 (Fig. 1, 2, 3) |
| Mønstre: sesongvariasjon, spredning, beskrivende statistikk | Ja | 4.3 (Tabell 1), 4.4, 4.5 |
| Konsekvenser ved manglende analyse | Ja | 4.6 |

Alle kjernekrav fra læreren er dekket. Strukturen er solid.

## 5. Samlet vurdering kap. 4

Kapittelet er strukturelt godt komponert og leverer på alle læreren-spesifiserte krav. **Største faglige svakhet er inkonsistensen i totalsummer (F1)**, som risikerer å gi leseren inntrykk av sviktende datakvalitet — det stikk motsatte budskap av det 4.3 forsøker å formidle. F1 utsettes for manuell gjennomgang av bruker.

Underkapittel 4.4 og 4.5 er pedagogiske høydepunkter, særlig skille mellom bestillings- og leveringsdato samt pre-campaign stocking-mekanikken. «Ingen julespike»-funnet styrker rapportens troverdighet ved å rapportere negative funn ærlig.

Med rettelse av F2, F3, M1, S1–S4 og K1–K3 (denne sesjonen) løftes kapittelet fra «godt» til «meget godt» innenfor sine egne premisser. F1 må behandles separat for å sikre konsistens i totaltall mellom kap. 4.3, 4.4 og evt. 5.4.
