import os
import re

files_to_fix = [
    "especificaciones.html",
    "demo.html",
    "sobre-nosotros.html",
    "blog.html",
    "faq.html",
    "testimonios.html",
    "nexusos-core.html",
    "equipo.html",
    "trabaja-con-nosotros.html",
    "privacidad.html",
    "terminos.html",
    "cookies.html",
    "aviso-cookies.html",
    "articulo-magia-o-fisica.html",
    "articulo-el-futuro-de-tu-oficina.html",
    "articulo-el-ultimo-objeto-que-compraras.html",
]

# Patterns to catch various ways the parent link might be written
patterns = [
    (r'<a href="#about"[^>]*>Nuestra empresa', '<a href="javascript:void(0)" style="cursor: default;">Nuestra empresa'),
    (r'<a href="index.html#about"[^>]*>Nuestra empresa', '<a href="javascript:void(0)" style="cursor: default;">Nuestra empresa'),
    (r'<a href="#features"[^>]*>Producto', '<a href="javascript:void(0)" style="cursor: default;">Producto'),
    (r'<a href="index.html#features"[^>]*>Producto', '<a href="javascript:void(0)" style="cursor: default;">Producto'),
]

for filename in files_to_fix:
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        
        new_content = content
        for pattern, replacement in patterns:
            new_content = re.sub(pattern, replacement, new_content)
        
        if new_content != content:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"No changes needed for {filename}")
