# Los tres casos reales

Esta guía nació como suplemento de tres estudios hechos **100 % con datos satelitales gratuitos**.
Cada uno ilustra una decisión distinta de las que vimos en [Cómo planificar](planificar.md): qué
medir, qué sensor, qué banda, y —sobre todo— qué se puede y qué **no** se puede afirmar.

## 1. Subsidencia en Vaca Muerta (InSAR)

**Pregunta:** ¿se hunde el suelo sobre la explotación no convencional de Vaca Muerta?

- **Sensor / misión:** SAR banda C, **Sentinel-1** (gratis).
- **Técnica:** InSAR / serie temporal SBAS (HyP3 + MintPy), corregida por atmósfera (ERA5).
- **Resultado:** mapa de velocidad creíble sobre ~210×210 km; fondo estable con cubetas de
  subsidencia localizadas (hasta ~12 mm/año). El contraste Bandurria Norte (uplift por inyección)
  vs Sur (subsidencia por producción), confirmado vertical combinando órbitas ascendente +
  descendente.
- **Lección:** sin corrección atmosférica y con series cortas, es fácil "ver" subsidencia que no
  existe. El preprocesamiento define la conclusión.

🔗 **[vaca-muerta-insar →](https://mpodeley.github.io/vaca-muerta-insar/)**

## 2. Subsidencia por extracción de litio (InSAR en salares)

**Pregunta:** ¿se mide deformación sobre la extracción de salmuera de litio (Salar del Hombre
Muerto)?

- **Sensor / misión:** SAR banda C, **Sentinel-1** (gratis).
- **Resultado honesto = límite del método:** el piso húmedo del salar **decorrelaciona** en banda C,
  así que solo ~16 % del área (las lomas, no los pozos) da datos confiables, y ahí está estable.
- **Lección:** *no* es un límite de la banda C en abstracto (en Atacama otros midieron cm sobre
  halita estable), sino de **esta geometría y este terreno**. La palanca correcta es **banda L**
  (SAOCOM / ALOS-2), que penetra y mantiene coherencia. Un caso perfecto de **elegir la banda**.

🔗 **[litio-insar →](https://mpodeley.github.io/litio-insar/)**

## 3. Volumen removido en minería a cielo abierto (DEM-differencing)

**Pregunta:** ¿cuánto material se excavó en un open-pit, sin datos de la empresa?

- **Sensor / misión:** **no es InSAR**, son **DEM**. SRTM (gratis) vs Copernicus DEM (gratis).
- **Truco temporal:** la mina de Veladero arrancó en 2005 → comparar **SRTM (2000, prístino)** contra
  **Copernicus DEM (~2012, pit excavado)**, ambos gratis. Para fechas recientes, **ASTER estéreo**.
- **Resultado:** ~285 Mm³ excavados / ~267 depositados (2000→2012), del mismo orden de magnitud que
  la producción reportada. También aplicado a un open-pit de carbón en China.
- **Lección:** el dato gratuito **histórico** (SRTM 2000) vale oro como línea de base, y la elección
  del método (DEM-differencing) sale directo del objetivo (volumen, no movimiento).

🔗 **[mineria-dem →](https://mpodeley.github.io/mineria-dem/)**

---

!!! note "El hilo común"
    Los tres parten de la misma pregunta —**¿qué quiero medir?**— y de ahí derivan sensor, banda y
    técnica. Y los tres son **honestos con el límite del método**: a veces el resultado más valioso
    es entender *por qué* un dato gratuito no alcanza y cuál sería la palanca correcta.
