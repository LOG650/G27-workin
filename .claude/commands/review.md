---
description: Grundig vurdering av prosjektrapporten med forbedringsforslag og prioritert tiltaksliste
argument-hint: [valgfritt: kapittelnummer eller fokusområde, f.eks. "kap 5" eller "metode"]
---

# /review — Grundig vurdering av Prosjektrapport_LOG650_G27

Du skal utføre en grundig akademisk gjennomgang av prosjektrapporten for LOG650-prosjektet (G27). Følg instruksene i `CLAUDE.md` (spesielt seksjon 2, 3, 6, 7, 9 og 11). Rapporten er på norsk og skal vurderes med akademisk standard for LOG650.

## Filer som skal leses

1. **Rapport (hovedobjekt for vurdering):** `014 fase 4 - report/Prosjektrapport_LOG650_G27.md`
2. **Prosjektplan:** `012 fase 2 - plan/prosjektplan.md`
3. **Status:** `012 fase 2 - plan/status.md`
4. **WBS:** `012 fase 2 - plan/wbs.md`
5. **Proposal (problemstilling):** `011 fase 1 - proposal/proposal.md`
6. **Prosjektinstrukser:** `CLAUDE.md` (kvalitetskrav og kapittelføringer)

Hvis brukeren har gitt argument ($ARGUMENTS), avgrens vurderingen til det spesifiserte kapittelet eller fokusområdet. Ellers vurder hele rapporten.

## Slik gjennomfører du vurderingen

Bruk TaskCreate for å holde oversikt over de syv stegene under. Marker hver oppgave som `completed` så snart den er ferdig.

### Steg 1 — Innlesing og kontekst
Les rapporten i sin helhet, samt prosjektplan, status.md og proposal. Identifiser problemstilling, avgrensning og planlagt leveranse.

### Steg 2 — Språkvurdering
Vurder norsk akademisk språk:
- Konsistent bruk av æ/ø/å
- Saklig og konsist fagspråk (jf. CLAUDE.md §1)
- Setningsbygning, flyt og leservennlighet
- Fagterminologi (logistikk, prognoser, statistikk) brukt korrekt
- Konsekvent terminologi gjennom rapporten
- Tegnsetting, rettskriving og typografi

### Steg 3 — Innholdsvurdering
Vurder faglig innhold mot CLAUDE.md §3 og §11:
- **Innledning:** Problemstilling, bakgrunn, avgrensning
- **Kap. 4 Casebeskrivelse:** Beslutningssituasjon, data, mønstre, konsekvenser
- **Kap. 5 Metode og data:** Metodevalg, analyseprosess (klargjøring → modellering → validering → prognose), datakvalitet, oppdeling trening/test, tabell med nøkkeltall
- **Kap. 6–7 Modellering og analyse:** Begrunnelse for modellvalg, forkastede modeller, parametrisering, validering (residualanalyse)
- **Kap. 8 Resultater:** MAE, MAPE og Bias presentert i tabeller
- **Diskusjon og konklusjon:** Tolkning, feilkilder, kobling tilbake til problemstilling
- **Figurer/tabeller:** Introdusert i tekst *før* visning, korte og nøkterne figurtekster
- **Referanser:** APA 7. utgave, korrekt sitering

### Steg 4 — Identifisere svakheter
Lag en konkret liste over svakheter, gruppert etter:
- **Faglige svakheter:** Manglende begrunnelser, svake koblinger til teori/pensum, antagelser uten støtte
- **Metodiske svakheter:** Manglende dokumentasjon av valg, etterprøvbarhet, datakvalitet
- **Strukturelle svakheter:** Rød tråd mellom problemstilling, metode og resultater
- **Formidling:** Uklare avsnitt, manglende introduksjon av figurer/tabeller, sprik mellom tekst og figur

For hver svakhet: oppgi kapittel/seksjon og linjereferanse hvis mulig.

### Steg 5 — Forbedringsforslag
For hver identifiserte svakhet, gi konkrete forslag til forbedring. Vær spesifikk: foreslå formuleringer, tilleggsanalyser eller strukturendringer der det er hensiktsmessig.

### Steg 6 — Samsvar med prosjektplan og status
Sammenlign rapportens innhold med:
- **Prosjektplan:** Er planlagte leveranser dekket? Avvik fra plan?
- **status.md:** Stemmer rapportens fremdrift med dokumentert status? Er aktiviteter på kritisk linje (datavask, modellering) prioritert?
- **WBS:** Er alle planlagte aktiviteter reflektert?

Pek på avvik og om de er begrunnet eller ikke.

### Steg 7 — Prioritert tiltaksliste og samlet vurdering
Avslutt med:
- **Prioritert tiltaksliste:** Tabell med kolonner `Prioritet (1–3)`, `Tiltak`, `Kapittel`, `Estimert innsats`. Prioritet 1 = kritisk for innlevering, 2 = viktig for kvalitet, 3 = ønskelig polering.
- **Samlet vurdering:** Kort tekstlig oppsummering (5–10 setninger) med styrker, svakheter og overordnet kvalitetsnivå (akademisk standard for LOG650).

## Output-format

Strukturer responsen slik:

```
# Review av Prosjektrapport_LOG650_G27 — [dato]

## 1. Språkvurdering
...

## 2. Innholdsvurdering (per kapittel)
...

## 3. Identifiserte svakheter
...

## 4. Forbedringsforslag
...

## 5. Samsvar med prosjektplan og status
...

## 6. Prioritert tiltaksliste
| Prioritet | Tiltak | Kapittel | Estimert innsats |
|---|---|---|---|
...

## 7. Samlet vurdering
...
```

## Viktige regler

- All output på norsk (æ, ø, å).
- Skill mellom **observasjon** (det rapporten faktisk sier) og **vurdering** (din tolkning) — jf. CLAUDE.md §5.
- Vær konkret: pek på kapittel, avsnitt eller linjenummer.
- Ikke endre rapporten selv — dette er en vurderingskommando, ikke en redigeringskommando.
- Hvis noe er uklart, still oppfølgingsspørsmål til slutt.
