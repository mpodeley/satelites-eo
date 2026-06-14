#!/usr/bin/env python3
"""Planisferio 2D animado: cómo un satélite en órbita baja teje la cobertura global.

Propaga un satélite (SGP4 vía Skyfield) a lo largo de varias órbitas, dibuja su traza
terrestre y "pinta" la franja de barrido (swath). Cada pasada cae más al oeste porque la
Tierra rota debajo: así una franja angosta termina cubriendo el globo. Exporta un HTML
autocontenido que se embebe en docs/orbitas.md.

Uso:
    python docs/pipeline/cobertura_planisferio.py

Requiere: skyfield, plotly, numpy (ver environment.yml).
"""
from pathlib import Path
import numpy as np
import plotly.graph_objects as go
from skyfield.api import EarthSatellite, load, wgs84

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs" / "assets" / "cobertura_planisferio.html"

# Sentinel-2A (SSO, swath ~290 km). Snapshot TLE; las órbitas son ilustrativas.
NAME = "Sentinel-2A"
TLE1 = "1 40697U 15028A   26165.20769247 -.00000152  00000+0 -41298-4 0  9996"
TLE2 = "2 40697  98.5689 240.1014 0001096  91.2008 268.9300 14.30813743573301"

SWATH_KM = 290                 # ancho de barrido
HALF_DEG = (SWATH_KM / 2) / 111.0   # medio swath en grados (~1 km = 1/111 grados)
N_ORBITS = 6                   # cuántas órbitas simular
STEP_MIN = 2                   # muestreo temporal (minutos)
N_FRAMES = 60                  # cuadros de la animación


def break_antimeridian(lats, lons):
    """Inserta None donde la traza cruza el antimeridiano, para no dibujar una raya."""
    out_lat, out_lon = [], []
    for i in range(len(lons)):
        if i and abs(lons[i] - lons[i - 1]) > 180:
            out_lat.append(None); out_lon.append(None)
        out_lat.append(lats[i]); out_lon.append(lons[i])
    return out_lat, out_lon


def main():
    ts = load.timescale()
    sat = EarthSatellite(TLE1, TLE2, NAME, ts)

    period_min = (2 * np.pi) / sat.model.no_kozai  # min por órbita
    total_min = N_ORBITS * period_min
    mins = np.arange(0, total_min, STEP_MIN)

    t = ts.tt_jd(sat.epoch.tt + mins / 1440.0)
    sub = wgs84.geographic_position_of(sat.at(t))
    lat = sub.latitude.degrees
    lon = sub.longitude.degrees

    # Borde izquierdo/derecho del swath: offset perpendicular a la dirección de avance.
    dlat = np.gradient(lat)
    dlon = np.gradient(lon) * np.cos(np.radians(lat))
    norm = np.hypot(dlat, dlon)
    norm[norm == 0] = 1
    perp_lat, perp_lon = -dlon / norm, dlat / norm  # perpendicular unitario
    left_lat = lat + perp_lat * HALF_DEG
    left_lon = lon + perp_lon * HALF_DEG / np.maximum(np.cos(np.radians(lat)), 0.2)
    right_lat = lat - perp_lat * HALF_DEG
    right_lon = lon - perp_lon * HALF_DEG / np.maximum(np.cos(np.radians(lat)), 0.2)

    # Traza completa (estática, tenue) con cortes en el antimeridiano.
    tk_lat, tk_lon = break_antimeridian(lat, lon)

    geo = dict(
        projection_type="natural earth", showland=True, showocean=True,
        landcolor="#2a2f3a", oceancolor="#11151c", lakecolor="#11151c",
        coastlinecolor="#5b6473", countrycolor="#3a414e",
        showcountries=True, bgcolor="rgba(0,0,0,0)",
    )

    def coverage(k):
        """Puntos de swath acumulados hasta el cuadro k (pintan la cobertura)."""
        idx = int(len(mins) * (k + 1) / N_FRAMES)
        cl = np.concatenate([left_lat[:idx], right_lat[:idx]])
        cn = np.concatenate([left_lon[:idx], right_lon[:idx]])
        return cl, cn, idx

    base_track = go.Scattergeo(
        lat=tk_lat, lon=tk_lon, mode="lines",
        line=dict(width=1, color="rgba(120,160,200,0.35)"),
        name="traza terrestre", hoverinfo="skip",
    )

    def cov_trace(k):
        cl, cn, _ = coverage(k)
        return go.Scattergeo(
            lat=cl, lon=cn, mode="markers",
            marker=dict(size=6, color="rgba(6,214,160,0.18)"),
            name="cobertura", hoverinfo="skip",
        )

    def sat_trace(k):
        _, _, idx = coverage(k)
        j = max(idx - 1, 0)
        return go.Scattergeo(
            lat=[lat[j]], lon=[lon[j]], mode="markers",
            marker=dict(size=11, color="#ffd166", line=dict(width=1.5, color="#222")),
            name=NAME, hovertemplate=f"{NAME}<br>%{{lat:.1f}}°, %{{lon:.1f}}°<extra></extra>",
        )

    frames = [
        go.Frame(name=str(k), data=[base_track, cov_trace(k), sat_trace(k)])
        for k in range(N_FRAMES)
    ]

    fig = go.Figure(
        data=[base_track, cov_trace(0), sat_trace(0)],
        frames=frames,
    )
    fig.update_layout(
        geo=geo, paper_bgcolor="#11151c",
        margin=dict(l=0, r=0, t=44, b=0),
        title=dict(
            text=f"{NAME} · {N_ORBITS} órbitas — cada pasada cae al oeste y teje cobertura",
            font=dict(color="#e8e8e8", size=14), x=0.5,
        ),
        font=dict(color="#cdd3dc"),
        legend=dict(orientation="h", y=-0.02, x=0.5, xanchor="center",
                    bgcolor="rgba(0,0,0,0)"),
        updatemenus=[dict(
            type="buttons", showactive=False, x=0.02, y=0.04, xanchor="left",
            buttons=[
                dict(label="▶ Reproducir", method="animate",
                     args=[None, dict(frame=dict(duration=120, redraw=True),
                                      fromcurrent=True, transition=dict(duration=0))]),
                dict(label="⏸ Pausa", method="animate",
                     args=[[None], dict(frame=dict(duration=0, redraw=False),
                                        mode="immediate")]),
            ],
        )],
        sliders=[dict(
            active=0, x=0.16, len=0.8, y=0.04,
            currentvalue=dict(prefix="cuadro ", font=dict(color="#9aa3b2", size=11)),
            steps=[dict(method="animate", label=str(k),
                        args=[[str(k)], dict(mode="immediate",
                              frame=dict(duration=0, redraw=True),
                              transition=dict(duration=0))])
                   for k in range(N_FRAMES)],
        )],
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.write_html(OUT, include_plotlyjs="cdn", full_html=True,
                   config={"displayModeBar": False, "responsive": True})
    print(f"OK: {len(mins)} muestras, {N_FRAMES} cuadros → {OUT}")


if __name__ == "__main__":
    main()
