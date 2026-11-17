# Agustín Cohen — Tattoo & Ilustración

Portfolio web estático (HTML + CSS + JS, sin dependencias).

## Estructura
- `index.html` — toda la página (estilos, textos ES/EN y galería).
- `thumb/` — miniaturas de la galería (máx. 720 px), en JPG y WebP.
- `sm/` — miniaturas chicas en WebP (máx. 400 px) para celulares.
- `full/` — imágenes grandes con marca de agua (se abren al hacer clic), en JPG y WebP.
- `imagenes.js` — medidas de cada miniatura. Lo genera `optimizar.py`; no se edita a mano.
- `optimizar.py` — crea las versiones WebP y actualiza `imagenes.js`.
- `og.jpg` — imagen que aparece al compartir el link (WhatsApp, Instagram, etc.).

## Cómo editar
- **Obras y temas:** en `index.html`, buscá `const groups = [`. Cada obra es `["archivo","Título","flash|ilus|poster",año]`.
- **Títulos en inglés:** objeto `titlesEn`.
- **Textos en inglés:** objeto `EN`.
- **Mail:** buscá `agustincohenn@gmail.com` en `index.html` (aparece en contacto, tienda, pie y datos para Google).

## Agregar una obra
1. Poné la imagen en `thumb/` (máx. 720 px) y la versión con marca de agua en `full/`, con el mismo nombre y en `.jpg`.
2. Sumala a `groups` en `index.html`.
3. Corré `python3 optimizar.py` en esta carpeta (necesita `pip install pillow`).
   Si te olvidás de este paso, la obra igual se ve: usa el JPG en vez del WebP.

## Links directos a cada tema
`#tradicional`, `#neotradicional`, `#tarot`, `#cyberpunk`, `#posters`.
Por ejemplo: `https://tuusuario.github.io/tu-repo/#posters`

## Publicar en GitHub Pages
1. Subí esta carpeta a un repo.
2. Settings → Pages → Deploy from branch → `main` / root.
3. Cuando tengas la dirección, en `index.html` cambiá `<meta property="og:image" content="og.jpg">`
   por la URL completa (ej. `https://tuusuario.github.io/tu-repo/og.jpg`) para que la vista previa
   aparezca bien en todas las apps.
