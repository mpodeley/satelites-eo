# Satélites para observar la Tierra: una guía para empezar

Hay **decenas de satélites** mirando la Tierra ahora mismo. Algunos sacan fotos en color, otros
"ven" en la oscuridad o a través de las nubes con radar, otros miden la altura del terreno, la
temperatura, la humedad del suelo o hasta cambios en la gravedad. Muchos son **gratis**.

Esta guía es un **suplemento didáctico** a tres estudios reales hechos solo con datos satelitales
públicos (ver [Los tres casos](casos.md)). Acá no analizamos un lugar puntual: explicamos
**qué herramientas hay, dónde están, qué dato sacan, cada cuánto y a qué costo**, para que puedas
**planificar tu propia campaña o estudio**.

<iframe src="assets/globo_orbitas.html" width="100%" height="560" style="border:1px solid #ccc;border-radius:6px"></iframe>

*Globo 3D con satélites reales orbitando (posiciones calculadas desde sus datos orbitales TLE) y su
**cono de visión** —lo que cada uno "ve" en el suelo—. **Filtrá por tipo** (óptico, SAR, térmico,
hiperespectral, GEO) y **tocá un satélite en la leyenda** para iluminar su cono, ver su traza terrestre
y un panel con qué dato saca. Fijate el contraste: PRISMA mira una franja angosta, Sentinel-3 barre
ancho, y el geoestacionario GOES ve casi un hemisferio entero de una sola vez. El **terminador
día/noche** sobre el planeta muestra qué mitad está iluminada en cada momento —clave para los sensores
ópticos, que necesitan luz solar—.*

## ¿Para qué sirve mirar la Tierra desde el espacio?

- **Medir cómo se mueve el suelo** (subsidencia, deslizamientos, volcanes) con radar InSAR.
- **Medir cuánto material se sacó o se puso** (minería, obra) comparando modelos de elevación.
- **Seguir la vegetación, el agua, los incendios, la temperatura** con sensores ópticos y térmicos.
- **Identificar materiales** (minerales, contaminantes) con sensores hiperespectrales.
- Y todo esto **en serie temporal**: lo potente no es una foto, es ver el cambio a lo largo de años.

## Cómo recorrer esta guía

1. **[Cómo orbita un satélite](orbitas.md)** — dónde está cada uno y por qué eso define qué puede
   ver. Órbita baja vs geoestacionaria, revisita, swath, hora de paso. Con un planisferio animado.
2. **[Sensores y tipos de dato](sensores.md)** — óptico, radar (SAR), térmico, hiperespectral,
   modelos de elevación... qué mide cada uno y cuándo conviene.
3. **[Catálogo de misiones](catalogo.md)** — la tabla grande: gratis vs pago, resolución, revisita,
   acceso. Tu lista de compras.
4. **[Cómo elegir / planificar](planificar.md)** — un árbol de decisión: *tengo esta pregunta,
   ¿qué satélite uso?*
5. **[Los tres casos](casos.md)** — de la teoría a la práctica, con resultados reales.

!!! note "Honestidad metodológica"
    Esta guía es introductoria y prioriza la **intuición** sobre la exactitud de cada número.
    Las posiciones del globo son **ilustrativas** (los datos orbitales cambian a diario) y las cifras
    del catálogo se desactualizan: confirmá siempre en el portal del operador.
    Se usó **Claude (Anthropic)** para asistir en la redacción; el contenido fue revisado por el autor.
