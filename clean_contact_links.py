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
            
        # Standard clean mailto - sometimes target="_blank" on mailto is a bad idea
        content = re.sub(r'href="mailto:[^"]*"[^>]*>Contacte con nosotros</a>', 
                        'href="mailto:contacto.nexuss.brand@gmail.com?subject=Consulta NEXUS SEAMLESS">Contacte con nosotros</a>', 
                        content)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated contact links to standard clean mailto.")
