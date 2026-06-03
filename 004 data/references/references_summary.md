# Litteraturreferanser: LOG650 Prognosepresisjon REMA 1000

Dette dokumentet gir en samlet oversikt over alle 18 kildene som er referert i prosjektet, fordelt på 15 faglige kilder og 3 programvarebibliotek. Oversikten speiler kildene i rapportens kap. 11 Bibliografi (forfattere, år, tittel, tidsskrift og DOI), og er ordnet alfabetisk som i bibliografien for enkel kryssjekk.

---

## Faglige kilder (15)

### 1. Arunraj, N. S., & Ahrens, D. (2015)
**Tittel:** *A hybrid seasonal autoregressive integrated moving average and quantile regression for daily food sales forecasting*  
**Journal:** *International Journal of Production Economics*, 170, 147-160  
**Nøkkelfunn:** Utvikler en hybridmodell (SARIMA kombinert med kvantilregresjon) for daglig matvaresalg som fanger både sesongvariasjon og kampanje-/kalendereffekter, og viser forbedret presisjon for produkter med svingende etterspørsel.  
**Bruk i prosjektet:** Faglig støtte for å modellere på dagsnivå (kap. 2) og for hybrid routing mellom modellfamilier (kap. 6).  
**DOI:** [10.1016/j.ijpe.2015.09.014](https://doi.org/10.1016/j.ijpe.2015.09.014)

### 2. Box, G. E. P., & Jenkins, G. M. (1976)
**Tittel:** *Time series analysis: Forecasting and control* (rev. utg.)  
**Forlag:** Holden-Day  
**Nøkkelfunn:** Etablerer den systematiske Box-Jenkins-metodikken for ARIMA-modellering: identifikasjon, estimering og diagnostisk kontroll av autoregressive og glidende-gjennomsnitt-modeller med sesongkomponent.  
**Bruk i prosjektet:** Metodisk grunnlag for SARIMA/SARIMAX-modellen (kap. 2 og kap. 7).  
**DOI:** — (lærebok; intern lesekopi i artikler-mappen er 5. utgave 2016, jf. README der)

### 3. Breiman, L. (2001)
**Tittel:** *Random forests*  
**Journal:** *Machine Learning*, 45(1), 5-32  
**Nøkkelfunn:** Introduserer Random Forest, en ensemblemetode der mange beslutningstrær trenes på tilfeldige utvalg av observasjoner og variabler, noe som gir robusthet mot overtilpasning og evne til å fange ikke-lineære sammenhenger.  
**Bruk i prosjektet:** Teoretisk grunnlag for Random Forest, en av hovedmodellene i analysen (kap. 2 og kap. 6).  
**DOI:** [10.1023/A:1010933404324](https://doi.org/10.1023/A:1010933404324)

### 4. Dickey, D. A., & Fuller, W. A. (1979)
**Tittel:** *Distribution of the estimators for autoregressive time series with a unit root*  
**Journal:** *Journal of the American Statistical Association*, 74(366a), 427-431  
**Nøkkelfunn:** Utleder fordelingen for estimatorer i autoregressive serier med enhetsrot og danner grunnlaget for (Augmented) Dickey-Fuller-testen for stasjonaritet.  
**Bruk i prosjektet:** Grunnlag for ADF-testen av stasjonaritet i treningsserien før modellering (kap. 5, vedlegg A1).  
**DOI:** [10.1080/01621459.1979.10482531](https://doi.org/10.1080/01621459.1979.10482531)

### 5. Fildes, R., Goodwin, P., Lawrence, M., & Nikolopoulos, K. (2009)
**Tittel:** *Effective forecasting and judgmental adjustments: an empirical evaluation and strategies for improvement in supply-chain planning*  
**Journal:** *International Journal of Forecasting*, 25(1), 3-23  
**Nøkkelfunn:** Empirisk evaluering av menneskelige (skjønnsmessige) justeringer av systemprognoser; viser at justeringer basert på reell tilleggsinformasjon kan forbedre presisjonen, mens ukritiske overstyringer ofte forverrer den.  
**Bruk i prosjektet:** Diskusjon av at lokalkunnskap og menneskelige overstyringer kan forbedre prognoser når de brukes systematisk (kap. 9).  
**DOI:** [10.1016/j.ijforecast.2008.11.010](https://doi.org/10.1016/j.ijforecast.2008.11.010)

### 6. Fildes, R., Ma, S., & Kolassa, S. (2022)
**Tittel:** *Retail forecasting: Research and practice*  
**Journal:** *International Journal of Forecasting*, 38(4), 1269-1295  
**Nøkkelfunn:** Omfattende gjennomgang av gapet mellom akademisk forskning og praksis i varehandelsprognoser, med vekt på volatilitet, kampanjer og store datamengder.  
**Bruk i prosjektet:** Grunnlag for teorikapitlet om hvorfor varehandelsprognoser er et eget og komplekst fagfelt (kap. 2).  
**DOI:** [10.1016/j.ijforecast.2021.11.004](https://doi.org/10.1016/j.ijforecast.2021.11.004)

### 7. Friedman, J. H. (2001)
**Tittel:** *Greedy function approximation: A gradient boosting machine*  
**Journal:** *Annals of Statistics*, 29(5), 1189-1232  
**Nøkkelfunn:** Introduserer gradient boosting, der beslutningstrær trenes sekvensielt slik at hver iterasjon korrigerer residualene fra de foregående.  
**Bruk i prosjektet:** Teoretisk grunnlag for Gradient Boosting-modellen (kap. 2 og kap. 6).  
**DOI:** [10.1214/aos/1013203451](https://doi.org/10.1214/aos/1013203451)

### 8. Hyndman, R. J., & Athanasopoulos, G. (2021)
**Tittel:** *Forecasting: Principles and practice* (3. utg.)  
**Forlag:** OTexts (https://otexts.com/fpp3/)  
**Nøkkelfunn:** Moderne lærebok-syntese som presenterer ETS-, ARIMA- og hybridmetoder innenfor et felles statistisk rammeverk, og beskriver etterspørselens hovedkomponenter (nivå, trend, sesong, støy).  
**Bruk i prosjektet:** Metodisk hovedreferanse for valg, estimering og evaluering av tidsseriemodeller, og for Holt-Winters/ETS (kap. 2 og kap. 6).  
**DOI:** — (åpen nettutgave: https://otexts.com/fpp3/)

### 9. Hyndman, R. J., & Koehler, A. B. (2006)
**Tittel:** *Another look at measures of forecast accuracy*  
**Journal:** *International Journal of Forecasting*, 22(4), 679-688  
**Nøkkelfunn:** Kritisk gjennomgang av feilmål; påpeker svakheter ved MAPE ved lav etterspørsel og anbefaler mer robuste mål som MAE/MASE.  
**Bruk i prosjektet:** Begrunner valg av MAE og bruk av robuste mål (sMAPE, WAPE) som supplement til MAPE (kap. 5 og kap. 8/9).  
**DOI:** [10.1016/j.ijforecast.2006.03.001](https://doi.org/10.1016/j.ijforecast.2006.03.001)

### 10. Ljung, G. M., & Box, G. E. P. (1978)
**Tittel:** *On a measure of lack of fit in time series models*  
**Journal:** *Biometrika*, 65(2), 297-303  
**Nøkkelfunn:** Foreslår Ljung-Box Q-test for autokorrelasjon i residualer, et sentralt verktøy for diagnostisk modellkontroll.  
**Bruk i prosjektet:** Grunnlag for residualdiagnostikken (Ljung-Box Q-test) som validerer modellene (kap. 7 og kap. 8, Tabell 7).  
**DOI:** [10.1093/biomet/65.2.297](https://doi.org/10.1093/biomet/65.2.297)

### 11. Makridakis, S., Spiliotis, E., & Assimakopoulos, V. (2022)
**Tittel:** *The M5 competition: Background, organization, and results*  
**Journal:** *International Journal of Forecasting*, 38(4), 1325-1346  
**Nøkkelfunn:** Dokumenterer bakgrunn, organisering og resultater fra M5-konkurransen (Walmart-data) og viser at maskinlæring og hybridmodeller utkonkurrerer klassiske tidsseriemetoder på dagligvaredata.  
**Bruk i prosjektet:** Setter prosjektet i en moderne sammenheng og forankrer bruken av maskinlæring og hybridmodeller (kap. 2).  
**DOI:** [10.1016/j.ijforecast.2021.01.005](https://doi.org/10.1016/j.ijforecast.2021.01.005)

### 12. Seiringer, W., Brockmann, F., Altendorfer, K., & Felberbauer, T. (2022)
**Tittel:** *Influence of forecast error and forecast bias on safety stock on a MRP system with rolling horizon forecast updates*  
**Kilde:** I *Operations Research Proceedings 2021* (kap. 62). Springer  
**Nøkkelfunn:** Viser at systematisk skjevhet (bias) i prognoser påvirker behovet for sikkerhetslager mer kritisk enn tilfeldige avvik i et MRP-system med rullende horisont.  
**Bruk i prosjektet:** Kobler bias som feilmål til sikkerhetslagerkostnader (kap. 5 og kap. 8/9).  
**DOI:** [10.1007/978-3-031-08623-6_62](https://doi.org/10.1007/978-3-031-08623-6_62)

### 13. Syntetos, A. A., & Boylan, J. E. (2005)
**Tittel:** *The accuracy of intermittent demand estimates*  
**Journal:** *International Journal of Forecasting*, 21(2), 303-314  
**Nøkkelfunn:** Behandler estimering og presisjon for sporadisk (intermittent) etterspørsel og ligger til grunn for klassifisering basert på CV² og gjennomsnittlig intervall mellom etterspørselshendelser.  
**Bruk i prosjektet:** Klassifisering av produktets etterspørsel som "lumpy demand" (CV = 3,23) i casebeskrivelsen (kap. 2 og kap. 4.3).  
**DOI:** [10.1016/j.ijforecast.2004.10.001](https://doi.org/10.1016/j.ijforecast.2004.10.001)

### 14. Syntetos, A. A., Boylan, J. E., & Disney, S. M. (2009)
**Tittel:** *Forecasting for inventory planning: a review*  
**Journal:** *Journal of the Operational Research Society*, 60(1), S149-S160  
**Nøkkelfunn:** Tverrfaglig gjennomgang som knytter prognosenøyaktighet direkte til lagerstyring, og viser hvordan bedre presisjon reduserer sikkerhetslager og risiko for utsolgtsituasjoner.  
**Bruk i prosjektet:** Løfter diskusjonen til praktisk logistikkverdi for REMA 1000 (kap. 9).  
**DOI:** [10.1057/jors.2008.173](https://doi.org/10.1057/jors.2008.173)

### 15. Trapero, J. R., Kourentzes, N., & Fildes, R. (2015)
**Tittel:** *On the identification of sales forecasting models in the presence of promotions*  
**Journal:** *Journal of the Operational Research Society*, 66(2), 299-307  
**Nøkkelfunn:** Foreslår en kampanjemodell som håndterer dimensjonalitet og multikollinearitet ved å kombinere prinsipalkomponentanalyse (PCA) med automatisk identifikasjon av etterspørselsdynamikk, og som låner informasjon på tvers av produkter for varer med kort historikk; utkonkurrerer både ekspertvurderinger og statistiske referansemodeller.  
**Bruk i prosjektet:** Faglig forankring for kampanjemodellering og for poenget om at binære kampanjeindikatorer ikke er tilstrekkelige (kap. 2 og kap. 9).  
**DOI:** [10.1057/jors.2013.174](https://doi.org/10.1057/jors.2013.174)

---

## Programvare og biblioteker (3)

### 16. McKinney, W. (2010)
**Tittel:** *Data structures for statistical computing in Python*  
**Kilde:** *Proceedings of the 9th Python in Science Conference*, 51-56  
**Nøkkelfunn:** Presenterer pandas-biblioteket og dets datastrukturer for tabell- og tidsseriedata i Python.  
**Bruk i prosjektet:** Databehandling og datavask (kap. 5, analyseskript).  
**DOI:** [10.25080/Majora-92bf1922-00a](https://doi.org/10.25080/Majora-92bf1922-00a)

### 17. Pedregosa, F., Varoquaux, G., Gramfort, A., m.fl. (2011)
**Tittel:** *Scikit-learn: Machine learning in Python*  
**Journal:** *Journal of Machine Learning Research*, 12, 2825-2830  
**Nøkkelfunn:** Beskriver scikit-learn, et bredt maskinlæringsbibliotek for Python.  
**Bruk i prosjektet:** Implementasjon av Random Forest og Gradient Boosting samt kryssvalidering og hyperparameter-tuning (kap. 6 og kap. 7).  
**DOI:** — (ingen DOI oppgitt i rapporten)

### 18. Seabold, S., & Perktold, J. (2010)
**Tittel:** *Statsmodels: Econometric and statistical modeling with Python*  
**Kilde:** *Proceedings of the 9th Python in Science Conference*, 92-96  
**Nøkkelfunn:** Presenterer statsmodels for økonometrisk og statistisk modellering i Python.  
**Bruk i prosjektet:** Estimering av SARIMA/SARIMAX, ADF-test og Ljung-Box-diagnostikk (kap. 7).  
**DOI:** [10.25080/Majora-92bf1922-011](https://doi.org/10.25080/Majora-92bf1922-011)
