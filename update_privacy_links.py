import os
import re

files = [
    "index.html", "blog.html", "especificaciones.html", "faq.html", 
    "sobre-nosotros.html", "equipo.html", "testimonios.html", 
    "trabaja-con-nosotros.html", "articulo-magia-o-fisica.html", 
    "articulo-el-ultimo-objeto-que-compraras.html", "articulo-el-futuro-de-tu-oficina.html", "demo.html"
]

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = re.sub(r'href="[^"]*">Avisos de privacidad del consumidor</a>', 'href="privacidad.html">Avisos de privacidad del consumidor</a>', content)
        content = re.sub(r'href="[^"]*">Política de Privacidad</a>', 'href="privacidad.html">Política de Privacidad</a>', content)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated Privacy Policy links.")
