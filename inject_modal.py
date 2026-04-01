import os

files = [
    "index.html", "blog.html", "especificaciones.html", "faq.html", 
    "sobre-nosotros.html", "equipo.html", "testimonios.html", 
    "trabaja-con-nosotros.html", "articulo-magia-o-fisica.html", 
    "articulo-el-ultimo-objeto-que-compraras.html", "articulo-el-futuro-de-tu-oficina.html",
    "demo.html"
]

link_tag = '    <link rel="stylesheet" href="reserve-modal.css">\n'
script_tag = '    <script src="reserve-modal.js"></script>\n'

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        new_lines = []
        head_injected = False
        body_injected = False
        
        for line in lines:
            # Check if tags already exist to avoid duplicates
            if 'reserve-modal.css' in line:
                head_injected = True
            if 'reserve-modal.js' in line:
                body_injected = True
                
            if '</head>' in line and not head_injected:
                new_lines.append(link_tag)
                head_injected = True
            
            if '</body>' in line and not body_injected:
                new_lines.append(script_tag)
                body_injected = True
                
            new_lines.append(line)
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)

print("Injected modal assets into all pages.")
