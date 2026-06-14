# Los cinco casos reales

Esta guía nació como suplemento de cinco estudios hechos **100 % con datos satelitales gratuitos**.
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

## 4. Actividad O&G desde el espacio (luz nocturna)

**Pregunta:** ¿se puede ver **dónde y cuándo** se perfora, fractura y produce en Vaca Muerta mirando la
**huella lumínica nocturna**, sin esperar los registros oficiales?

- **Sensor / misión:** **VIIRS** banda día-noche (NASA **Black Marble**, ~500 m, gratis) — el mismo
  sensor que "ve" el lado oscuro del planeta en el [globo](index.md). Las perforadoras y los *frac
  spreads* trabajan iluminados de noche, y la producción suele **quemar gas (flaring)**.
- **Técnica:** cruzar **~22.000 detecciones nocturnas** con **~20.000 eventos de pozo** del ciclo de
  vida público (Cap IV / Adjunto IV) y las concesiones, para etiquetar qué actividad hay, dónde y de
  qué operador. Más un **nowcast** (*gradient boosting*) que adelanta el dato oficial.
- **Resultado:** la luz nocturna **confirma el 71 %** de los eventos conocidos (recall ~79 % en
  fractura); el nowcast predice la actividad del mes con **ROC-AUC 0.85–0.91**, meses antes de que el
  Cap IV se publique (sale con **~13,5 meses de atraso**).
- **Lección:** la **precisión es baja** (la mayoría de las luces son producción/flaring/pueblos, no
  eventos nuevos) — y está **bien explicado**: el valor está en el **recall** y en **adelantar** un
  dato público lento. Un caso de teledetección que mide **actividad**, no deformación ni volumen.

🔗 **[vaca-muerta-nightlights →](https://mpodeley.github.io/vaca-muerta-nightlights/)**

## 5. Emisiones de CO₂ y metano por operador

**Pregunta:** ¿cuánto **CO₂** (por quema de gas en antorcha) y **metano** emite la producción de Vaca
Muerta, y se puede **atribuir a cada operador** con datos públicos, sin información de las empresas?

- **Sensores / misiones — tres distintos, uno por gas:** **VIIRS Nightfire** (EOG, el canal **infrarrojo
  de combustión**, ≠ la banda día-noche del [caso 4](#4-actividad-og-desde-el-espacio-luz-nocturna))
  para el flaring; **Sentinel-5P / TROPOMI** (espectrómetro, columna de CH₄ a ~7 km) para el metano de
  cuenca; **NASA EMIT** (espectrómetro de imágenes en la ISS, plumas a 60 m). Todos gratis.
- **Técnica:** las antorchas son **infraestructura fija y geolocalizada** → point-in-polygon a la
  concesión → operador, y se cruza el volumen quemado (→ CO₂) con la **producción** (Cap IV) para sacar
  la **intensidad por barril** (kg CO₂/BOE). El metano se promedia a escala de cuenca (TROPOMI
  multi-año) y se rastrean **plumas puntuales** en el catálogo de EMIT.
- **Resultado:** 2024 → **113 antorchas, ~2,4 Mt CO₂**; la intensidad **no se reparte pareja**: los
  gasíferos queman ~1 % de su gas (~2–3 kg CO₂/BOE), los petroleros queman el gas asociado (Vista 16 %,
  Chevron 33 % → ~32 kg CO₂/BOE). El metano queda como **contexto de cuenca** (TROPOMI); EMIT observó la
  zona **132 veces** y catalogó **una sola pluma** (→ concesión de YPF) → pocas fuentes puntuales grandes.
- **Lección:** el satélite atribuye bien lo que es **puntual y fijo** (una antorcha → un operador), pero
  **no** lo que es **difuso** (el metano a 7 km de TROPOMI, o fuentes por debajo del umbral de EMIT pese
  a su buena cobertura). El caso elige conscientemente el **numerador atribuible** (flaring) y se niega a
  repartir el metano por empresa: eso sería **falsa precisión**.

🔗 **[vaca-muerta-emisiones →](https://mpodeley.github.io/vaca-muerta-emisiones/)**

---

!!! note "El hilo común"
    Los cinco parten de la misma pregunta —**¿qué quiero medir?**— y de ahí derivan sensor, banda y
    técnica. Y los cinco son **honestos con el límite del método**: a veces el resultado más valioso
    es entender *por qué* un dato gratuito no alcanza, cuál sería la palanca correcta, o qué tan lejos
    se puede confiar en lo que el satélite sí ve.
