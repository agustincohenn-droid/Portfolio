#!/usr/bin/env python3
"""Genera las versiones WebP de la galería y el archivo imagenes.js.

Uso:  python3 optimizar.py            (desde la carpeta de la web)
      python3 optimizar.py RUTA_WEB

Requiere Pillow:  pip install pillow
Por cada JPG de thumb/ crea:
  sm/<nombre>.webp     (máx. 400 px, para celulares)
  thumb/<nombre>.webp  (misma medida que el JPG)
  full/<nombre>.webp   (si existe full/<nombre>.jpg)
y escribe imagenes.js con el ancho y alto de cada miniatura.
Solo regenera lo que falta o cambió.
"""
import json, os, sys
from PIL import Image

root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
def p(*a): return os.path.join(root, *a)
os.makedirs(p("sm"), exist_ok=True)

def fresh(src, dst):
    return os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(src)

def to_webp(src, dst, max_side=None, q=82):
    if fresh(src, dst): return
    im = Image.open(src).convert("RGB")
    if max_side and max(im.size) > max_side:
        im.thumbnail((max_side, max_side), Image.LANCZOS)
    im.save(dst, "WEBP", quality=q, method=6)

dims = {}
for fn in sorted(os.listdir(p("thumb"))):
    if not fn.lower().endswith(".jpg"): continue
    name = fn[:-4]
    src = p("thumb", fn)
    with Image.open(src) as im: dims[name] = list(im.size)
    to_webp(src, p("thumb", name + ".webp"))
    to_webp(src, p("sm", name + ".webp"), max_side=400, q=80)
    full = p("full", fn)
    if os.path.exists(full): to_webp(full, p("full", name + ".webp"), q=84)

with open(p("imagenes.js"), "w", encoding="utf-8") as f:
    f.write("// Generado por optimizar.py — no editar a mano.\n")
    f.write("window.IMGS=" + json.dumps(dims, separators=(",", ":")) + ";\n")
print(f"Listo: {len(dims)} imágenes.")
