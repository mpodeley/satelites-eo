# Catálogo de misiones

Un mapa de las misiones más usadas para observar la Tierra, separadas en **gratuitas** (datos
abiertos, ideales para empezar y para presupuestos chicos) y **comerciales** (se compran o se
"taskean", pero ofrecen muy alta resolución o revisita a pedido).

!!! info "Cómo leer esta tabla"
    - **Resolución**: tamaño del píxel en el suelo. Menos metros = más detalle.
    - **Revisita**: cada cuánto el satélite vuelve a pasar por el mismo lugar (la *frecuencia*).
      "Tasking" significa que apunta a pedido, no en un ciclo fijo.
    - **Swath**: ancho de la franja que captura en cada pasada. Más ancho = más cobertura, menos detalle.
    - **Banda SAR**: X (~3 cm) penetra poco y da más detalle; C (~5.6 cm) es el equilibrio;
      L (~24 cm) penetra vegetación y mantiene coherencia en terrenos difíciles. Ver [Sensores](sensores.md).

    Última revisión del catálogo: **junio 2026**. Resoluciones, costos y revisitas cambian;
    confirmá siempre en el portal del operador (ver [Referencias](referencias.md)).

## Misiones gratuitas (datos abiertos)

<!-- CATALOGO_GRATIS_START -->

| Misión | Operador | Tipo | Sensor / banda | Resolución | Revisita | Swath | Período |
|---|---|---|---|---|---|---|---|
| Sentinel-1 | ESA Copernicus | SAR | Banda C (5.4 GHz) | 5×20 m (IW) | 6–12 d | 250 km | 2014– |
| Sentinel-2 | ESA Copernicus | Óptico | Multiespectral 13 bandas | 10 / 20 / 60 m | 5 d | 290 km | 2015– |
| Sentinel-3 | ESA Copernicus | Óptico + Térmico | OLCI / SLSTR | 300 m / 500–1000 m | 1–2 d | 1270 km | 2016– |
| Sentinel-5P | ESA Copernicus | Atmósfera | TROPOMI (gases traza) | 3.5×5.5 km | Diaria | 2600 km | 2017– |
| Landsat 8 / 9 | NASA / USGS | Óptico + Térmico | OLI + TIRS | 30 m (15 pan / 100 térmico) | 16 d (8 d combinados) | 185 km | 2013 / 2021– |
| MODIS | NASA (Terra / Aqua) | Óptico + Térmico | 36 bandas | 250 / 500 / 1000 m | Diaria | 2330 km | 1999 / 2002– |
| VIIRS | NASA / NOAA | Óptico + Térmico + Nocturno | Banda día-noche (DNB) / Black Marble | 375 / 750 m | Diaria | 3060 km | 2011– |
| ASTER | NASA / METI (Terra) | Óptico + Térmico + Estéreo | VNIR / SWIR / TIR | 15 / 30 / 90 m | A demanda (~16 d) | 60 km | 1999– |
| SRTM | NASA | DEM | Interferometría banda C | 30 m (1 arcsec) | Única (feb-2000) | — | 2000 |
| Copernicus DEM GLO-30 | ESA (de TanDEM-X) | DEM | SAR banda X | 30 m | Época ~2011–2015 | — | 2019– |
| NASADEM | NASA | DEM | SRTM reprocesado | 30 m | Época 2000 | — | 2020 |
| SAOCOM 1A / 1B | CONAE (Argentina) | SAR | Banda L (1.275 GHz) | ~10 m (stripmap) | 8–16 d | 30–350 km | 2018 / 2020– |
| SMAP | NASA | Radiómetro | Banda L (humedad de suelo) | 9–36 km | 2–3 d | 1000 km | 2015– |
| GRACE-FO | NASA / GFZ | Gravimetría | Agua subterránea / masa | ~300 km | Mensual | Global | 2018– |
| PRISMA | ASI (Italia) | Hiperespectral | 239 bandas VNIR-SWIR | 30 m (5 m pan) | A demanda | 30 km | 2019– |
| EMIT | NASA JPL (ISS) | Hiperespectral | Mineralogía / polvo | 60 m | A demanda (deriva ISS) | 75 km | 2022– |
| GOES-16 / 18 | NOAA | Óptico + Térmico (GEO) | ABI | 0.5–2 km | 5–15 min | Disco completo | 2017– |

<!-- CATALOGO_GRATIS_END -->

## Misiones comerciales

<!-- CATALOGO_PAGO_START -->

| Misión | Operador | Tipo | Sensor / banda | Resolución | Revisita | Swath | Período |
|---|---|---|---|---|---|---|---|
| ALOS-2 PALSAR-2 | JAXA | SAR | Banda L | 3–10 m | ~14 d | 50–70 km | 2014– |
| PlanetScope | Planet | Óptico | 3–8 bandas | 3–4 m | Diaria | ~24 km | 2016– |
| SkySat | Planet | Óptico | Pan + multiespectral | 0.5 m | Sub-diaria (tasking) | 6.6 km | 2014– |
| WorldView / Legion | Maxar | Óptico | Muy alta resolución | 0.3 m | ~Diaria (tasking) | 13 km | 2014– |
| Pléiades / Neo | Airbus | Óptico | Pan + multiespectral | 0.5 / 0.3 m | Diaria (tasking) | 20 / 14 km | 2011 / 2021– |
| TerraSAR-X / PAZ | Airbus / Hisdesat | SAR | Banda X | 1–3 m (0.25 staring) | ~11 d (tasking) | 5–30 km | 2007 / 2018– |
| COSMO-SkyMed | ASI (Italia) | SAR | Banda X | 1 m | Tasking (constelación) | 10–40 km | 2007– |
| ICEYE | ICEYE | SAR | Banda X (constelación) | 0.25–1 m | Sub-diaria (tasking) | 5–30 km | 2018– |
| Capella Space | Capella | SAR | Banda X | 0.5 m | Tasking | 5–10 km | 2020– |
| Umbra | Umbra | SAR | Banda X | 0.25 m | Tasking | 4–10 km | 2021– |

<!-- CATALOGO_PAGO_END -->

!!! tip "Regla práctica de presupuesto"
    Casi todo análisis serio **empieza por lo gratuito** (Sentinel, Landsat, los DEM) para
    explorar y delimitar la zona. Lo comercial se reserva para cuando hace falta **detalle
    sub-métrico** o una **fecha concreta a pedido** que las misiones abiertas no cubren.
    Los cinco [casos reales](casos.md) de esta guía se hicieron **100 % con datos gratuitos**.

> Las tablas de arriba se generan desde `docs/data/satelites.csv` con
> `python docs/pipeline/build_catalogo.py` — editá el CSV, no las tablas a mano.
