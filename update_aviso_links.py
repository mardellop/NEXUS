import os
import re

files = [
    "index.html", "blog.html", "especificaciones.html", "faq.html", 
    "sobre-nosotros.html", "equipo.html", "testimonios.html", 
    "trabaja-con-nosotros.html", "articulo-magia-o-fisica.html", 
    "articulo-el-ultimo-objeto-que-compraras.html", "articulo-el-futuro-de-tu-oficina.html", "demo.html", 
    "privacidad.html", "terminos.html", "cookies.html"
]

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = re.sub(r'href="[^"]*">Avisos de cookies</a>', 'href="aviso-cookies.html">Avisos de cookies</a>', content)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated Cookie Notice links.")
