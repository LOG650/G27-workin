# Litteraturreferanser: LOG650 Prognosepresisjon REMA 1000

Dette dokumentet inneholder en oversikt over de 7 kjerneartiklene som er valgt ut for prosjektet. Disse artiklene danner det teoretiske grunnlaget for analysen av daglig etterspørsel og effekten av kampanjer.

---

### 1. Makridakis, S., Spiliotis, E., & Assimakopoulos, V. (2022)
**Tittel:** *The M5 Accuracy Competition: Results, findings, and conclusions*  
**Journal:** *International Journal of Forecasting*  
**Nøkkelfunn:** Dokumenterer resultater fra verdens største prognosekonkurranse (M5), basert på Walmart-data. Viser at moderne maskinlæringsmodeller og hybridmodeller utkonkurrerer klassiske tidsseriemetoder på dagligvaredata på butikk- og lagernivå.  
**Bruk i prosjektet:** Sette prosjektet i en moderne sammenheng og sammenligne våre resultater med state-of-the-art i bransjen.  
**DOI:** [10.1016/j.ijforecast.2021.11.013](https://doi.org/10.1016/j.ijforecast.2021.11.013)

### 2. Fildes, R., Ma, S., & Kolassa, S. (2022)
**Tittel:** *Retail forecasting: Research and practice*  
**Journal:** *International Journal of Forecasting*  
**Nøkkelfunn:** En omfattende gjennomgang av gapet mellom akademia og praksis i varehandelen. Diskuterer utfordringer med volatilitet, kampanjer og store datamengder.  
**Bruk i prosjektet:** Grunnlag for teorikapitlet (2.1 og 2.2) for å forklare hvorfor "retail forecasting" er et eget og komplekst fagfelt.  
**DOI:** [10.1016/j.ijforecast.2019.01.001](https://doi.org/10.1016/j.ijforecast.2019.01.001)

### 3. Trapero, J. R., Pedregal, D. J., & Fildes, R. (2015)
**Tittel:** *Sales forecasting in the presence of promotions*  
**Journal:** *Applied Mathematical Modelling*  
**Nøkkelfunn:** Fokuserer spesifikt på hvordan kampanjer skaper diskontinuerlige salgstoppe som tradisjonelle modeller ikke fanger opp. Foreslår metoder for å integrere kampanjekalendere i prognosene.  
**Bruk i prosjektet:** Forklare og modellere "oktober-toppen" og andre kampanjer (115-enhets-platåene) i dataene fra REMA 1000.  
**DOI:** [10.1016/j.apm.2014.10.043](https://doi.org/10.1016/j.apm.2014.10.043)

### 4. Fildes, R., Goodwin, P., Lawrence, M., & Nikolopoulos, K. (2008)
**Tittel:** *Effective forecasting and judgmental adjustments: an empirical evaluation*  
**Journal:** *Journal of Operations Management*  
**Nøkkelfunn:** Analyserer hvordan og når menneskelige overstyringer (skjønnsmessige justeringer) forbedrer eller forverrer systemgenererte prognoser.  
**Bruk i prosjektet:** Diskutere de flate 115-linjene i dataene, som kan være resultat av menneskelig overstyring/automatiske regler snarere enn ren statistisk historikk.  
**DOI:** [10.1016/j.jom.2008.01.001](https://doi.org/10.1016/j.jom.2008.01.001)

### 5. Hyndman, R. J., & Koehler, A. B. (2006)
**Tittel:** *Another look at measures of forecast accuracy*  
**Journal:** *International Journal of Forecasting*  
**Nøkkelfunn:** Kritisk analyse av feilmål som MAPE. Argumenterer for mer robuste mål som MAE og MASE, spesielt i situasjoner med lav etterspørsel eller nullverdier.  
**Bruk i prosjektet:** Begrunne valget av MAE som hovedmål og forklare svakheter ved vår foreløpige MAPE-verdi i kapittel 4.  
**DOI:** [10.1016/j.ijforecast.2006.03.001](https://doi.org/10.1016/j.ijforecast.2006.03.001)

### 6. Arunraj, N. S., & Ahrens, D. (2015)
**Tittel:** *A hybrid seasonal autoregressive integrated moving average and quantile regression for daily food sales forecasting*  
**Journal:** *International Journal of Forecasting*  
**Nøkkelfunn:** Utvikler modeller spesifikt for daglige matvaresalg i supermarkeder. Tar hensyn til både sesongvariasjoner og kampanjeeffekter.  
**Bruk i prosjektet:** Akademisk støtte for å jobbe på dagsnivå med matvarer (Lasagne Familiepakning) i metodedelen (kapittel 3).  
**DOI:** [10.1016/j.ijforecast.2014.07.006](https://doi.org/10.1016/j.ijforecast.2014.07.006)

### 7. Syntetos, A. A., Boylan, J. E., & Disney, S. M. (2009)
**Tittel:** *Forecasting for inventory planning: a review*  
**Journal:** *Journal of the Operational Research Society*  
**Nøkkelfunn:** Knytter prognosenøyaktighet direkte til lagerstyring (inventory control). Forklarer hvordan forbedret prognosepresisjon reduserer sikkerhetslager og risiko for stock-outs.  
**Bruk i prosjektet:** Løfte diskusjonen (kapittel 7) til å handle om den praktiske logistikk-verdien for REMA 1000 i Trondheim.  
**DOI:** [10.1057/jors.2008.173](https://doi.org/10.1057/jors.2008.173)

### 8. Seiringer, W., Brockmann, F., Altendorfer, K., & Felberbauer, T. (2024)
**Tittel:** *Influence of Forecast Error and Forecast Bias on Safety Stock on a MRP System with Rolling Horizon Forecast Updates*  
**Journal:** *Proceedings of the International Conference on Production Research*  
**Nøkkelfunn:** Analyserer hvordan ulike typer prognosefeil og bias påvirker behovet for sikkerhetslager i komplekse forsyningskjeder. Viser at systematiske feil (bias) har en mer kritisk innvirkning på lagerkostnader enn tilfeldige avvik.  
**Bruk i prosjektet:** Brukes i diskusjonskapittelet for å koble våre funn (MAE/MAPE) til de faktiske økonomiske konsekvensene for REMA 1000s lagerbinding.
