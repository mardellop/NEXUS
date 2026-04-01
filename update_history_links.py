import os

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
            
        # Specific match for the footer links that were using # per my previous view_file
        content = content.replace('<a href="sobre-nosotros.html">Nuestra historia</a>', '<a href="sobre-nosotros.html#story">Nuestra historia</a>')
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated footer history links.")
