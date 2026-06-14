# Sensores y tipos de dato

El satélite es el vehículo; el **sensor** es lo que decide qué dato sacás. Hay dos grandes familias
—**pasivos** (captan la luz/calor que ya existe) y **activos** (emiten su propia señal y miden el
eco)— y dentro de ellas, varios tipos.

## Óptico (pasivo)

Como una cámara, pero con más "colores". Capta la luz solar reflejada en distintas **bandas** del
espectro.

- **Pancromático**: una sola banda en blanco y negro, máxima resolución.
- **Multiespectral**: varias bandas (visible + infrarrojo cercano). Con ellas se calculan índices
  como el **NDVI** (vigor de la vegetación) o se detecta agua, suelo desnudo, cultivos.
- **Limitación clave**: necesita **luz de día y cielo despejado**. Las nubes lo tapan.
- Ejemplos: Sentinel-2, Landsat, MODIS, PlanetScope, WorldView.

## Radar / SAR (activo)

El **SAR** (radar de apertura sintética) emite microondas y mide el eco. Como pone su propia
"linterna", **funciona de noche y atraviesa las nubes** — enorme ventaja en zonas nubladas o para
monitoreo garantizado. Mide rugosidad, humedad, estructura... y, con **interferometría (InSAR)**,
**movimientos del suelo de milímetros**.

La **banda** (longitud de onda) define cuánto penetra y qué tan estable es la señal:

| Banda | Long. de onda | Penetra | Bueno para |
|---|---|---|---|
| **X** | ~3 cm | poco | máximo detalle, zonas urbanas, objetos |
| **C** | ~5.6 cm | media | uso general, deformación (Sentinel-1) |
| **L** | ~24 cm | mucho | vegetación densa, mantiene coherencia donde C falla (SAOCOM, ALOS) |

!!! tip "Por qué la banda decide el resultado"
    En el [caso del litio](casos.md), el piso húmedo del salar **decorrelaciona** en banda C
    (Sentinel-1) y no se puede medir el núcleo: ahí la palanca correcta es **banda L** (SAOCOM).
    Elegir mal la banda puede dar un resultado nulo que no es culpa del método.

## Térmico (pasivo)

Mide la **radiación infrarroja térmica**, es decir, la **temperatura** de la superficie. Sirve para
islas de calor urbano, estrés hídrico de cultivos, actividad volcánica, incendios. Suele tener menos
resolución que el óptico (decenas a cientos de metros). Ejemplos: Landsat TIRS, Sentinel-3 SLSTR,
MODIS, ECOSTRESS.

## Hiperespectral (pasivo)

En vez de unas pocas bandas, capta **cientos** de bandas muy finas y contiguas: una "huella
espectral" de cada píxel. Permite **identificar materiales** específicos (tipos de mineral,
plásticos, especies vegetales, contaminantes). Ejemplos: PRISMA, EMIT, EnMAP.

## Modelos de elevación (DEM) y estéreo

Un **DEM** (modelo digital de elevación) es la **altura del terreno**. Restando dos DEM de fechas
distintas se mide **cuánto material se removió o depositó** (volúmenes en minería, obra, erosión).
Se obtienen por:

- **Interferometría radar** (SRTM, Copernicus DEM de TanDEM-X).
- **Estéreo óptico**: dos imágenes del mismo lugar desde ángulos distintos (ASTER, Pléiades) — el
  mismo principio que la visión en 3D de dos ojos.

El [caso de minería](casos.md) compara el DEM **SRTM (2000)** contra el **Copernicus DEM (~2012)**
para medir lo excavado en un open-pit, todo gratis.

## Otros (radiómetros, gravimetría, altimetría)

- **Radiómetros de microondas** (SMAP, banda L): **humedad del suelo** a baja resolución (km).
- **Gravimetría** (GRACE-FO): cambios de masa → **agua subterránea**, hielo, a escala regional.
- **Altimetría** (Sentinel-3, ICESat-2): altura de océanos, lagos, hielo con láser o radar.

---

Ya sabés **dónde** orbitan y **qué** miden. El siguiente paso es la lista concreta de misiones con
sus números → [Catálogo de misiones](catalogo.md).
