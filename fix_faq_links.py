import os

files_to_fix = [
    "especificaciones.html",
    "blog.html",
    "articulo-magia-o-fisica.html",
    "articulo-el-futuro-de-tu-oficina.html",
    "articulo-el-ultimo-objeto-que-compraras.html",
    "sobre-nosotros.html",
    "equipo.html",
    "testimonios.html"
]

for filename in files_to_fix:
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Fixing both index.html#faq and just #faq for good measure
        new_content = content.replace('href="index.html#faq"', 'href="faq.html"')
        new_content = new_content.replace('href="#faq"', 'href="faq.html"')
        
        if new_content != content:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"No changes needed for {filename}")
