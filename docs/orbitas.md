# Cómo orbita un satélite (y por qué importa)

Dónde está un satélite define **qué puede ver, de qué tamaño y cada cuánto**. Antes de elegir una
misión conviene entender cuatro ideas: el **tipo de órbita**, la **revisita**, el **swath** y la
**hora local de paso**.

## Tipos de órbita

=== "LEO — órbita baja"

    **~500–800 km de altura.** Es donde vive casi todo satélite de observación (Sentinel, Landsat,
    SAOCOM...). Da **alta resolución** porque está cerca, pero ve una **franja angosta** y pasa
    rápido: completa una vuelta en ~90–100 minutos. Para cubrir todo el planeta necesita muchas
    pasadas a lo largo de días.

=== "SSO — heliosincrónica"

    Una LEO especial, casi polar, sincronizada con el Sol: el satélite **cruza cada lugar siempre a
    la misma hora solar local** (p. ej. ~10:30 de la mañana). Esto mantiene la **iluminación
    constante** entre fechas, clave para comparar imágenes ópticas en el tiempo. La mayoría de los
    satélites de teledetección son SSO.

=== "GEO — geoestacionaria"

    **~35.786 km de altura**, sobre el ecuador. A esa altura el satélite gira a la misma velocidad
    que la Tierra, así que queda **fijo sobre un punto**. Ve **medio planeta de una sola vez** y todo
    el tiempo (ideal para meteorología: GOES, Meteosat sacan una imagen cada 5–15 minutos), pero con
    **baja resolución** porque está lejísimos.

!!! example "La intuición en el globo"
    En el [globo de la portada](index.md) se ve directo: los LEO/SSO corren bajos y rápidos
    rozando los polos; el GEO cuelga quieto, mucho más alto, sobre el ecuador.

## Revisita: cada cuánto vuelve

La **revisita** es la frecuencia con que un satélite vuelve a ver el mismo lugar. Determina si podés
seguir un proceso **diario** (incendios, inundaciones) o solo **cada varias semanas** (un mapa anual
de vegetación).

- Se mejora con **constelaciones**: dos Sentinel-2 dan 5 días en vez de 10; las flotas comerciales
  (Planet, ICEYE) llegan a **diaria o sub-diaria**.
- Los **geoestacionarios** tienen revisita de **minutos**, a costa de resolución.
- Algunos satélites no tienen ciclo fijo: apuntan **a pedido** ("tasking"), típico de los comerciales.

## Swath: el ancho de la franja

El **swath** es el ancho del terreno que el sensor captura en cada pasada. Hay un **compromiso**
constante:

> **Swath ancho ↔ menos detalle.** Un satélite que barre 2330 km (MODIS) cubre el planeta a diario
> pero con píxeles de cientos de metros. Uno de swath angosto (60 km, ASTER) da 15 m pero tarda en
> volver. No existe el satélite que vea todo, todo el tiempo, con todo el detalle.

## Hora local y pasadas ascendente / descendente

Un satélite cruza cada lugar **dos veces** por órbita: subiendo hacia el norte (**ascendente**) y
bajando hacia el sur (**descendente**). En radar esto importa: las dos geometrías miran el suelo
desde **lados opuestos**, y combinarlas permite separar el movimiento vertical del horizontal
(es justo lo que hace el [caso de Vaca Muerta](casos.md)).

## Cómo se teje la cobertura global

Una sola órbita es una franja angosta. Como la Tierra **rota debajo** del satélite, cada pasada cae
un poco más al oeste que la anterior. En un día se acumulan franjas paralelas que, juntas, terminan
cubriendo casi todo el planeta. El planisferio lo muestra:

<iframe src="../assets/cobertura_planisferio.html" width="100%" height="560" style="border:1px solid #ccc;border-radius:6px"></iframe>

*Traza terrestre de un satélite en órbita baja a lo largo de varias órbitas, con su franja de barrido
(swath). Cada pasada se corre al oeste porque la Tierra rota debajo: así una franja angosta termina
cubriendo el globo. Usá el botón de play / el slider.*

Con esto en mente, lo siguiente es **qué sensor lleva** cada satélite, porque eso decide qué tipo de
dato vas a obtener → [Sensores y tipos de dato](sensores.md).
