import os

files = [
    "index.html", "blog.html", "especificaciones.html", "faq.html", 
    "sobre-nosotros.html", "equipo.html", "testimonios.html", 
    "trabaja-con-nosotros.html", "articulo-magia-o-fisica.html", 
    "articulo-el-ultimo-objeto-que-compraras.html", "articulo-el-futuro-de-tu-oficina.html"
]

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace('href="#demo"', 'href="demo.html"')
        content = content.replace('href="index.html#demo"', 'href="demo.html"')
        # Specific match for the footer links that were using # per my previous view_file
        content = content.replace('<a href="#">Demo</a>', '<a href="demo.html">Demo</a>')
        
        # In the menu the class is dropdown-item
        content = content.replace('class="dropdown-item">Demo</a>', 'class="dropdown-item">Demo</a>') # Already should have been replaced if #demo was used

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated links.")
