import os
import re

files = [
    "index.html", "blog.html", "especificaciones.html", "faq.html", 
    "sobre-nosotros.html", "equipo.html", "testimonios.html", 
    "trabaja-con-nosotros.html", "articulo-magia-o-fisica.html", 
    "articulo-el-ultimo-objeto-que-compraras.html", "articulo-el-futuro-de-tu-oficina.html", "demo.html", "privacidad.html"
]

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = re.sub(r'href="[^"]*">Términos y condiciones</a>', 'href="terminos.html">Términos y condiciones</a>', content)
        content = re.sub(r'href="[^"]*">Términos de Servicio</a>', 'href="terminos.html">Términos de Servicio</a>', content)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated Terms and Conditions links.")
