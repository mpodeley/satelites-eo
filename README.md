# Guía de satélites para observar la Tierra

Suplemento didáctico a cuatro casos reales de teledetección
([vaca-muerta-insar](https://github.com/mpodeley/vaca-muerta-insar),
[litio-insar](https://github.com/mpodeley/litio-insar),
[mineria-dem](https://github.com/mpodeley/mineria-dem)).

**¿Qué herramientas satelitales existen para analizar la Tierra?** Dónde orbitan, si son
gratis o pagas, qué tipo de dato sacan y con qué frecuencia (revisita). Pensada para alguien
que se inicia y para **planificar campañas o estudios**. Incluye un **globo 3D** con órbitas
reales (TLE) y un **planisferio animado** de cobertura.

🌐 **Sitio:** https://mpodeley.github.io/satelites-eo/

## Desarrollo local

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve   # http://127.0.0.1:8000
```

El push a `main` despliega automáticamente a GitHub Pages (ver `.github/workflows/deploy.yml`).

## Regenerar datos y animaciones

```bash
# Tabla del catálogo a partir del CSV editable (docs/data/satelites.csv)
python docs/pipeline/build_catalogo.py

# Planisferio de cobertura (requiere skyfield + plotly)
python docs/pipeline/cobertura_planisferio.py

# Figura didáctica de interferograma InSAR (requiere matplotlib)
python docs/pipeline/interferograma_demo.py
```

El globo 3D (`docs/assets/globo_orbitas.html`) es HTML autocontenido: toma los TLE en vivo
de [Celestrak](https://celestrak.org) con un snapshot embebido como respaldo.
