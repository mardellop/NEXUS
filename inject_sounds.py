import os

html_files = [
    "especificaciones.html",
    "demo.html",
    "sobre-nosotros.html",
    "blog.html",
    "faq.html",
    "testimonios.html",
    "nexusos-core.html",
    "equipo.html",
    "trabaja-con-nosotros.html",
    "privacidad.html",
    "terminos.html",
    "cookies.html",
    "aviso-cookies.html"
]

script_tag = '<script src="ui-sounds.js"></script>\n'

for filename in html_files:
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        
        if 'ui-sounds.js' not in content:
            # Inject before reserve-modal.js or before </body>
            if '<script src="reserve-modal.js"></script>' in content:
                new_content = content.replace('<script src="reserve-modal.js"></script>', script_tag + '    <script src="reserve-modal.js"></script>')
            else:
                new_content = content.replace('</body>', '    ' + script_tag + '</body>')
            
            with open(filename, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated {filename}")
