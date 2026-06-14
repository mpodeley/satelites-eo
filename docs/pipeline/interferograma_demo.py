#!/usr/bin/env python3
"""Figura didáctica: cómo se ve un interferograma InSAR sobre una cubeta de subsidencia.

Genera dos paneles a partir de un campo de deformación sintético (dos cubetas que se
hunden): (a) la fase envuelta — las "franjas" que mide el radar— y (b) el desplazamiento
desenrollado en mm. No usa datos reales; es un esquema para explicar el método.

Uso:
    python docs/pipeline/interferograma_demo.py
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parents[1] / "assets" / "interferograma_demo.png"

LAMBDA_C = 0.0555          # longitud de onda banda C (Sentinel-1), m
HALF = LAMBDA_C / 2 * 1000 # mm de movimiento en LOS por franja (~27.7 mm)


def bowl(X, Y, cx, cy, amp_mm, sigma):
    """Cubeta de subsidencia gaussiana (negativa = se hunde), en mm."""
    return -amp_mm * np.exp(-(((X - cx) ** 2 + (Y - cy) ** 2) / (2 * sigma ** 2)))


def main():
    n = 600
    x = np.linspace(-10, 10, n)
    X, Y = np.meshgrid(x, x)

    # Desplazamiento en la línea de vista (mm): dos cubetas de distinto tamaño.
    los_mm = bowl(X, Y, -3.2, 1.5, 90, 2.2) + bowl(X, Y, 3.5, -2.0, 55, 1.5)

    # Fase envuelta: cada franja = media longitud de onda de movimiento en LOS.
    phase = (4 * np.pi / (LAMBDA_C * 1000)) * los_mm
    wrapped = np.angle(np.exp(1j * phase))   # a [-pi, pi]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))

    im1 = ax1.imshow(wrapped, cmap="twilight", extent=[-10, 10, -10, 10], origin="lower")
    ax1.set_title("(a) Interferograma — fase envuelta\ncada franja ≈ %.0f mm en la línea de vista" % HALF,
                  fontsize=11)
    ax1.set_xticks([]); ax1.set_yticks([])
    cb1 = fig.colorbar(im1, ax=ax1, fraction=0.046, pad=0.04, ticks=[-np.pi, 0, np.pi])
    cb1.ax.set_yticklabels(["−π", "0", "+π"]); cb1.set_label("fase (radianes)")

    im2 = ax2.imshow(los_mm, cmap="RdBu", extent=[-10, 10, -10, 10], origin="lower",
                     vmin=-90, vmax=90)   # RdBu: negativo (subsidencia) = rojo
    ax2.set_title("(b) Desplazamiento desenrollado\n(rojo = se hunde, azul = se levanta)", fontsize=11)
    ax2.set_xticks([]); ax2.set_yticks([])
    cb2 = fig.colorbar(im2, ax=ax2, fraction=0.046, pad=0.04)
    cb2.set_label("desplazamiento en LOS (mm)")

    fig.suptitle("De las franjas al milímetro: un interferograma sobre dos cubetas de subsidencia",
                 fontsize=12.5, y=1.02)
    fig.tight_layout()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT, dpi=130, bbox_inches="tight", facecolor="white")
    print(f"OK → {OUT}")


if __name__ == "__main__":
    main()
