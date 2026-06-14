#!/usr/bin/env python3
"""Renderiza la tabla del catálogo de misiones a partir de docs/data/satelites.csv.

Fuente de verdad = el CSV (editable a mano). Este script reemplaza el contenido
entre los marcadores HTML en docs/catalogo.md, de modo que la prosa se mantiene y
solo se regeneran las tablas:

    <!-- CATALOGO_GRATIS_START --> ... <!-- CATALOGO_GRATIS_END -->
    <!-- CATALOGO_PAGO_START -->   ... <!-- CATALOGO_PAGO_END -->

Uso:
    python docs/pipeline/build_catalogo.py
"""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[2]
CSV = ROOT / "docs" / "data" / "satelites.csv"
PAGE = ROOT / "docs" / "catalogo.md"

# Columnas del CSV → encabezado en la tabla. El orden define el de la tabla.
COLUMNS = [
    ("mision", "Misión"),
    ("operador", "Operador"),
    ("tipo", "Tipo"),
    ("banda_sensor", "Sensor / banda"),
    ("resolucion", "Resolución"),
    ("revisita", "Revisita"),
    ("swath", "Swath"),
    ("periodo", "Período"),
]


def render_table(rows):
    keys = [k for k, _ in COLUMNS]
    head = "| " + " | ".join(h for _, h in COLUMNS) + " |"
    sep = "|" + "|".join("---" for _ in COLUMNS) + "|"
    body = [
        "| " + " | ".join(r.get(k, "").strip() for k in keys) + " |"
        for r in rows
    ]
    return "\n".join([head, sep, *body])


def replace_block(text, start, end, payload):
    a = text.index(start) + len(start)
    b = text.index(end)
    return text[:a] + "\n\n" + payload + "\n\n" + text[b:]


def main():
    with CSV.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    gratis = [r for r in rows if r["grupo"].strip().lower() == "gratis"]
    pago = [r for r in rows if r["grupo"].strip().lower() != "gratis"]

    text = PAGE.read_text(encoding="utf-8")
    text = replace_block(
        text, "<!-- CATALOGO_GRATIS_START -->", "<!-- CATALOGO_GRATIS_END -->",
        render_table(gratis),
    )
    text = replace_block(
        text, "<!-- CATALOGO_PAGO_START -->", "<!-- CATALOGO_PAGO_END -->",
        render_table(pago),
    )
    PAGE.write_text(text, encoding="utf-8")
    print(f"OK: {len(gratis)} misiones gratis, {len(pago)} comerciales → {PAGE.name}")


if __name__ == "__main__":
    main()
