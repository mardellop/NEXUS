import os

files = [
    "index.html", "blog.html", "especificaciones.html", "faq.html", 
    "sobre-nosotros.html", "equipo.html", "testimonios.html", 
    "trabaja-con-nosotros.html", "articulo-magia-o-fisica.html", 
    "articulo-el-ultimo-objeto-que-compraras.html", "articulo-el-futuro-de-tu-oficina.html",
    "demo.html"
]

script_tag = '    <script src="chatbot.js"></script>\n'

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        new_lines = []
        script_injected = False
        
        for line in lines:
            if 'chatbot.js' in line:
                script_injected = True
                
            if '</body>' in line and not script_injected:
                new_lines.append(script_tag)
                script_injected = True
                
            new_lines.append(line)
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)

print("Injected chatbot.js into all pages.")
