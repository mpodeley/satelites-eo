# Cómo elegir / planificar un estudio

La pregunta correcta no es "¿qué satélite es el mejor?" sino **"¿qué quiero medir?"**. De ahí sale
el sensor, y del sensor las misiones candidatas. Esta página es una guía de decisión para armar una
campaña sin gastar de más.

## Paso 1 — Partí del objetivo

| Quiero medir... | Tipo de dato | Misiones para empezar (gratis) |
|---|---|---|
| Movimiento del suelo (mm/año): subsidencia, deslizamientos, volcanes | **SAR / InSAR** | Sentinel-1 (banda C); SAOCOM (banda L) si hay vegetación o suelo húmedo |
| Volumen removido / depositado (minería, obra, erosión) | **DEM-differencing / estéreo** | SRTM 2000 vs Copernicus DEM; ASTER estéreo para una fecha puntual |
| Vegetación, cultivos, deforestación (NDVI) | **Óptico multiespectral** | Sentinel-2, Landsat 8/9 |
| Temperatura de superficie, incendios, estrés hídrico | **Térmico** | Landsat TIRS, Sentinel-3, MODIS |
| Identificar minerales / materiales | **Hiperespectral** | PRISMA, EMIT |
| Actividad industrial nocturna / flaring de gas | **Nocturno (día-noche)** | VIIRS día-noche (NASA Black Marble) |
| Humedad del suelo (regional) | **Radiómetro microondas** | SMAP |
| Agua subterránea / cambios de masa (regional) | **Gravimetría** | GRACE-FO |
| Algo que cambia rápido (horas): humo, inundación, tormenta | **GEO / revisita alta** | GOES (geoestacionario), MODIS/VIIRS (diario) |
| Mapa de muy alto detalle (sub-métrico) de una fecha | **Óptico/SAR comercial** | Planet, Maxar, Pléiades, ICEYE (de pago) |

## Paso 2 — Chequeá las cuatro restricciones

1. **Resolución** — ¿el objeto/proceso entra en el píxel? Una grieta de metros no se ve a 30 m.
2. **Revisita** — ¿el proceso es lento (anual) o rápido (diario)? Define la misión y si necesitás
   constelación. Ver [revisita](orbitas.md#revisita-cada-cuanto-vuelve).
3. **Profundidad temporal** — ¿desde cuándo hay datos? Para series largas o "antes/después"
   históricos importa el **año de lanzamiento** (columna *Período* del [catálogo](catalogo.md)).
   Truco clásico: **SRTM (2000)** como "estado prístino" para comparar con algo reciente.
4. **Condiciones** — ¿hay nubes, es de noche, hay vegetación densa o suelo húmedo? Si sí → **SAR**
   en vez de óptico, y ojo con la **banda** (C vs L).

## Paso 3 — Gratis primero, pago solo si hace falta

```
¿Lo resuelve un dato gratuito (Sentinel / Landsat / DEM)?
        │
   ┌────┴─────┐
  Sí          No
   │           │
 Usalo.   ¿Necesito sub-métrico o una fecha exacta a pedido?
              │
         ┌────┴────┐
        Sí         No
         │          │
   Comercial   Revisá banda/sensor: quizá otro dato gratuito sí sirve
   (tasking)   (p. ej. pasar de óptico a SAR, o de banda C a L)
```

!!! tip "Empezá siempre explorando con lo abierto"
    Aunque el resultado final sea comercial, conviene **delimitar la zona y la fecha con datos
    gratuitos** primero. Es más barato equivocarse con Sentinel que con una imagen taskeada.

## Paso 4 — Conseguí los datos

Cada misión tiene su portal (ASF, Copernicus Data Space, USGS EarthExplorer, NASA Earthdata...).
La lista completa está en [Referencias y portales](referencias.md).

## Paso 5 — Mirá cómo se hizo de verdad

Los [cinco casos](casos.md) recorren este proceso de punta a punta —objetivo, elección de satélite y
banda, descarga, procesamiento y resultado honesto— y todo el código es público y reproducible.
