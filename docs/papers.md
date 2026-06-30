# Qué se extrae de datos públicos (papers)

Una selección **curada y verificada** de trabajos que muestran cómo, con **datos satelitales
públicos**, se extrae información de valor real: cuánto se hunde el suelo, dónde hay actividad, cuánto
material se movió, cuánto gas se quema o se emite. No es una revisión exhaustiva: son puntos de entrada
sólidos y muy citados para ver **hasta dónde llega cada método** antes de planificar un estudio (ver
[Cómo elegir / planificar](planificar.md)). Cada referencia tiene su **DOI verificado**.

## 1. Subsidencia y deformación del suelo (InSAR)

Radar satelital comparado entre fechas para medir movimientos milimétricos. Es la base de los casos
[Vaca Muerta](casos.md) y [litio](casos.md) de esta guía — y hay un paper sobre **exactamente** esa
zona:

- **Tamburini-Beliveau et al. · 2022.** *Assessment of ground deformation and seismicity in two areas
  of intense hydrocarbon production in the Argentinian Patagonia.* Scientific Reports 12, 19198.
  [10.1038/s41598-022-23160-6](https://doi.org/10.1038/s41598-022-23160-6)
  *Qué extrae:* con **Sentinel-1** (DInSAR + SBAS) mide desplazamientos verticales 2017–2020 sobre
  pozos no convencionales de **Vaca Muerta** y los correlaciona con inyección/extracción de fluidos.
- **Ferretti, Prati, Rocca · 2001.** *Permanent scatterers in SAR interferometry.* IEEE TGRS 39(1),
  8–20. [10.1109/36.898661](https://doi.org/10.1109/36.898661)
  *Qué extrae:* el método **PS-InSAR** — seguir reflectores estables en largas series para medir
  deformación milimétrica superando la decorrelación.
- **Berardino, Fornaro, Lanari, Sansosti · 2002.** *A new algorithm for surface deformation monitoring
  based on small baseline differential SAR interferograms.* IEEE TGRS 40(11), 2375–2383.
  [10.1109/TGRS.2002.803792](https://doi.org/10.1109/TGRS.2002.803792)
  *Qué extrae:* el método **SBAS** (el que usan los casos InSAR de esta guía) para reconstruir series
  temporales preservando la coherencia.
- **Amelung, Galloway, Bell, Zebker, Laczniak · 1999.** *Sensing the ups and downs of Las Vegas: InSAR
  reveals structural control of land subsidence and aquifer-system deformation.* Geology 27(6),
  483–486. <a href="https://doi.org/10.1130/0091-7613(1999)027%3C0483:STUADO%3E2.3.CO;2">10.1130/0091-7613(1999)027&lt;0483&gt;</a>
  *Qué extrae:* mapea hasta 19 cm de subsidencia por bombeo de acuíferos y revela el control de las
  fallas — un clásico de InSAR aplicado.

## 2. Actividad económica desde las luces nocturnas

Las luces de noche como proxy de actividad humana — la idea detrás del caso
[nightlights](casos.md):

- **Henderson, Storeygard, Weil · 2012.** *Measuring Economic Growth from Outer Space.* American
  Economic Review 102(2), 994–1028. [10.1257/aer.102.2.994](https://doi.org/10.1257/aer.102.2.994)
  *Qué extrae:* usa luces nocturnas (DMSP-OLS) como proxy del crecimiento del PIB donde las cuentas
  nacionales son pobres.
- **Elvidge et al. · 1997.** *Relation between satellite observed visible-near infrared emissions,
  population, economic activity and electric power consumption.* Int. J. Remote Sensing 18(6),
  1373–1379. [10.1080/014311697218485](https://doi.org/10.1080/014311697218485)
  *Qué extrae:* establece la relación entre luces nocturnas y población, PIB y consumo eléctrico.

## 3. Volúmenes y cambios de topografía (diferencia de DEM)

Restar modelos de elevación de distintas fechas para medir cuánto material se movió — el método del
caso [minería](casos.md):

- **Chu, Lee · 2023.** *Estimation of the Amount of Mining and Waste Rocks at Musan Mine... Using a
  Historical Map and SRTM and Copernicus Global Digital Elevation Models.* Korean J. Remote Sensing
  39(5), 495–505. [10.7780/kjrs.2023.39.5.1.3](https://doi.org/10.7780/kjrs.2023.39.5.1.3)
  *Qué extrae:* volumen de mineral extraído y de estéril acumulado en una **mina a cielo abierto**
  diferenciando **SRTM y Copernicus DEM** gratuitos — casi idéntico al caso minería.
- **Brun, Berthier, Wagnon, Kääb, Treichler · 2017.** *A spatially resolved estimate of High Mountain
  Asia glacier mass balances from 2000 to 2016.* Nature Geoscience 10, 668–673.
  [10.1038/ngeo2999](https://doi.org/10.1038/ngeo2999)
  *Qué extrae:* balance de masa glaciar (cambio de volumen) diferenciando series de DEMs **ASTER**.
- **Berthier, Arnaud, Vincent, Rémy · 2006.** *Biases of SRTM in high-mountain areas: Implications for
  the monitoring of glacier volume changes.* Geophysical Research Letters 33, L08502.
  [10.1029/2006GL025862](https://doi.org/10.1029/2006GL025862)
  *Qué extrae:* cuantifica y corrige el **sesgo del SRTM** (penetración del radar) — clave para que la
  diferencia de DEM no engañe.

## 4. Emisiones de CO₂ y metano

Espectrómetros que "huelen" gases de efecto invernadero desde la órbita:

- **Lauvaux et al. · 2022.** *Global assessment of oil and gas methane ultra-emitters.* Science 375,
  557–561. [10.1126/science.abj4351](https://doi.org/10.1126/science.abj4351)
  *Qué extrae:* detecta y cuantifica **ultra-emisores de metano** de petróleo y gas con **TROPOMI /
  Sentinel-5P** (datos abiertos de Copernicus).
- **Thorpe et al. · 2023.** *Attribution of individual methane and carbon dioxide emission sources
  using EMIT observations from space.* Science Advances 9(46).
  [10.1126/sciadv.adh2391](https://doi.org/10.1126/sciadv.adh2391)
  *Qué extrae:* identifica y atribuye **>750 plumas** puntuales de CH₄ y CO₂ con el hiperespectral
  **EMIT** (NASA, en la ISS).
- **Eldering et al. · 2017.** *The Orbiting Carbon Observatory-2: first 18 months of science data
  products.* Atmospheric Measurement Techniques 10(2), 549–563.
  [10.5194/amt-10-549-2017](https://doi.org/10.5194/amt-10-549-2017)
  *Qué extrae:* los productos públicos de **OCO-2** (NASA) de CO₂ en columna (XCO₂).

## 5. Flaring de gas (quema en antorcha)

El calor de las antorchas de gas, visible de noche — la otra cara del caso
[nightlights](casos.md):

- **Elvidge, Zhizhin, Hsu, Baugh · 2013.** *VIIRS Nightfire: Satellite Pyrometry at Night.* Remote
  Sensing 5(9), 4423–4449. [10.3390/rs5094423](https://doi.org/10.3390/rs5094423)
  *Qué extrae:* detecta fuentes de calor subpíxel (incluidas **antorchas**) de noche con **VIIRS**,
  estimando temperatura y área del foco.
- **Elvidge, Zhizhin, Baugh, Hsu, Ghosh · 2016.** *Methods for Global Survey of Natural Gas Flaring
  from VIIRS Data.* Energies 9(1), 14. [10.3390/en9010014](https://doi.org/10.3390/en9010014)
  *Qué extrae:* identifica sitios individuales de quema y estima el **volumen de gas quemado** por
  sitio y país.
- **Elvidge et al. · 2009.** *A Fifteen Year Record of Global Natural Gas Flaring Derived from
  Satellite Data.* Energies 2(3), 595–622. [10.3390/en20300595](https://doi.org/10.3390/en20300595)
  *Qué extrae:* estimaciones nacionales y globales de flaring (1994–2008) con luces nocturnas
  **DMSP-OLS** calibradas.

## 6. Otros usos de datos públicos

- **Hansen et al. · 2013.** *High-Resolution Global Maps of 21st-Century Forest Cover Change.* Science
  342, 850–853. [10.1126/science.1244693](https://doi.org/10.1126/science.1244693)
  *Qué extrae:* mapas globales de pérdida/ganancia de bosque (2000–2012) a 30 m con **Landsat** gratis.
- **Pekel, Cottam, Gorelick, Belward · 2016.** *High-resolution mapping of global surface water and its
  long-term changes.* Nature 540, 418–422. [10.1038/nature20584](https://doi.org/10.1038/nature20584)
  *Qué extrae:* mapas globales de agua superficial y su cambio en 30 años con 3 millones de imágenes
  **Landsat**.
- **Rodell, Velicogna, Famiglietti · 2009.** *Satellite-based estimates of groundwater depletion in
  India.* Nature 460, 999–1002. [10.1038/nature08238](https://doi.org/10.1038/nature08238)
  *Qué extrae:* estima el **agotamiento de acuíferos** con anomalías gravimétricas de **GRACE**.

## 7. Espectrometría de alteración hidrotermal (exploración minera)

Mapear los **minerales de alteración** (arcillas, alunita, sílice, óxidos de hierro) que deja un sistema
hidrotermal para **acotar blancos de exploración** — la base del caso
[San Juan / espectrometría](casos.md):

- **Mars et al. · 2019.** *Porphyry Copper Potential of the United States Southern Basin and Range Using
  ASTER Data Integrated with Geochemical and Geologic Datasets.* Economic Geology 114(6), 1095–1121.
  [10.5382/econgeo.4675](https://doi.org/10.5382/econgeo.4675)
  *Qué extrae:* **screening regional** de pórfidos de cobre — polígonos de alteración argílica / fílica /
  propilítica de **ASTER** integrados con geoquímica y geofísica → depósitos no descubiertos.
- **Wan, Fan, Jin · 2021.** *Application of hyperspectral remote sensing for supplementary investigation
  of polymetallic deposits in Huaniushan ore region, NW China.* Scientific Reports 11, 440.
  [10.1038/s41598-020-79864-0](https://doi.org/10.1038/s41598-020-79864-0)
  *Qué extrae:* mapeo **hiperespectral** de minerales de alteración con **SAM, MNF, PCA y MTMF**; ~80 %
  de exactitud validada a campo.
- **Yousefi et al. · 2018.** *Integrating geologic and Landsat-8 and ASTER remote sensing data for gold
  exploration: Zarshuran Carlin-type gold deposit, NW Iran.* Arabian Journal of Geosciences 11, 482.
  [10.1007/s12517-018-3822-x](https://doi.org/10.1007/s12517-018-3822-x)
  *Qué extrae:* halos de alteración (argílica, alunita, sílice, óxidos) con **cocientes de bandas, PCA,
  Crosta, SAM y Matched Filtering** + lineamientos.
- **Chirinos · 2026.** *Teledetección de depósitos minerales ocultos mediante imágenes multiespectrales
  ASTER. Una revisión.* Revista de Teledetección 68, e24590.
  [10.4995/raet.2026.24590](https://doi.org/10.4995/raet.2026.24590)
  *Qué extrae (revisión, en español):* el alcance y los **límites** de ASTER para depósitos **ocultos** —
  técnicas, índices e integración multifuente.

!!! note "Sobre las citas"
    Lista no exhaustiva y curada; cada referencia se verificó contra su DOI. Las métricas y enlaces
    pueden cambiar: ante la duda, buscá el DOI. ¿Falta un trabajo que valga la pena? Se agradece el
    aporte vía el [repositorio](https://github.com/mpodeley/satelites-eo).
