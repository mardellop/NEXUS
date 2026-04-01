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
            
        # First, undo the aggressive replace if possible by replacing mailto back to # for those that AREN'T "Contacte con nosotros"
        # Actually, it's safer to just fix "Contacte con nosotros" and then selectively fix others if needed.
        # But wait, "Nexusbot" should NOT be mailto.
        
        # Reset any mailto that's not followed by "Contacte con nosotros"
        # This is tricky. Let's just fix the specific ones I know were broken.
        content = content.replace('href="mailto:contacto.nexuss.brand@gmail.com">Nexusbot</a>', 'href="#">Nexusbot</a>')
        content = content.replace('href="mailto:contacto.nexuss.brand@gmail.com">Avisos de privacidad', 'href="#">Avisos de privacidad')
        content = content.replace('href="mailto:contacto.nexuss.brand@gmail.com">Términos y condiciones', 'href="#">Términos y condiciones')
        content = content.replace('href="mailto:contacto.nexuss.brand@gmail.com">Configuración de cookies', 'href="#">Configuración de cookies')
        content = content.replace('href="mailto:contacto.nexuss.brand@gmail.com">Avisos de cookies', 'href="#">Avisos de cookies')
        content = content.replace('href="mailto:contacto.nexuss.brand@gmail.com">Política de Privacidad', 'href="#">Política de Privacidad')
        content = content.replace('href="mailto:contacto.nexuss.brand@gmail.com">Términos de Servicio', 'href="#">Términos de Servicio')

        # Now ensure "Contacte con nosotros" IS mailto
        content = re.sub(r'href="[^"]*">Contacte con nosotros</a>', 'href="mailto:contacto.nexuss.brand@gmail.com">Contacte con nosotros</a>', content)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print("Fixed footer links and set contact mailto correctly.")
