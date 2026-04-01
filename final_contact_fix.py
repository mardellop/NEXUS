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
            
        # Target only the contact link with higher specificity
        content = re.sub(r'href="mailto:contacto\.nexuss\.brand@gmail\.com">Contacte con nosotros</a>', 
                        'href="mailto:contacto.nexuss.brand@gmail.com" target="_blank" style="position: relative; z-index: 100;">Contacte con nosotros</a>', 
                        content)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated contact links with target and z-index.")
