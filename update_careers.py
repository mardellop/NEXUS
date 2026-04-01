import os
import re

d = "c:/Users/familia/.gemini/antigravity/playground/celestial-sunspot"

html_files = [f for f in os.listdir(d) if f.endswith(".html")]

# 1. Create trabaja-con-nosotros.html using faq.html as a template
with open(os.path.join(d, "faq.html"), "r", encoding="utf-8") as f:
    faq_content = f.read()

# replace title
page_content = re.sub(r'<title>.*?</title>', '<title>Trabaja con Nosotros | NEXUS S</title>', faq_content)

new_main = """
    <main>
        <section id="careers" class="careers-section" style="max-width: 900px; margin: 0 auto; padding: 60px 24px 100px;">
            <div class="faq-header-new" style="text-align: center; margin-bottom: 60px;">
                <span class="faq-badge">TRABAJA CON NOSOTROS</span>
                <h2 class="section-title">Únete a la Resonancia</h2>
            </div>

            <div style="display: flex; flex-direction: column; gap: 30px; margin-bottom: 80px;">
                <p style="font-size: 18px; line-height: 1.8; color: #000; text-align: justify;">En NEXUS SEAMLESS, no contratamos para cubrir puestos; buscamos mentes capaces de cuestionar la rigidez del mundo actual. Si crees que el hardware no debería ser un ancla, sino una extensión del movimiento humano, este es tu lugar.</p>
                
                <p style="font-size: 18px; line-height: 1.8; color: #000; text-align: justify;">La verdad es que aquí no construimos ordenadores, diseñamos libertad. Trabajamos con grafeno, titanio y polímeros electroactivos para que la tecnología deje de ser algo que se "lleva a cuestas" y pase a ser algo que fluye contigo. No buscamos la perfección de un ciclo de dos años, sino la excelencia que dura décadas.</p>
                
                <p style="font-size: 18px; line-height: 1.8; color: #000; text-align: justify;">Si te apasiona la física aplicada, la energía inalámbrica y los sistemas sin fricciones, queremos que tu talento se enrolle con nuestra visión.</p>
            </div>

            <h3 style="font-size: 32px; margin-bottom: 40px; color: #111827; text-align: center;">Posiciones Abiertas</h3>
            
            <div style="display: grid; grid-template-columns: 1fr; gap: 32px;">
                <div style="background: white; border: 1px solid rgba(6, 182, 212, 0.2); padding: 40px; border-radius: 24px; transition: all 0.3s ease; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
                    <h4 style="font-size: 22px; color: #06b6d4; font-family: 'Orbitron', sans-serif; margin-bottom: 8px;">1. Ingeniero de Materiales Avanzados (Especialista en Grafeno)</h4>
                    <p style="font-weight: 600; color: #111827; margin-bottom: 16px; font-size: 15px;">Departamento: I+D de Hardware.</p>
                    <p style="font-size: 16px; line-height: 1.8; color: #000; text-align: justify;">Buscamos a alguien que no vea una lámina de carbono, sino un lienzo infinito. Te encargarás de optimizar la integridad estructural de nuestras pantallas monocapa tras un millón de ciclos de flexión. Si los nanotubos de carbono son tu lenguaje nativo, queremos hablar contigo.</p>
                </div>

                <div style="background: white; border: 1px solid rgba(6, 182, 212, 0.2); padding: 40px; border-radius: 24px; transition: all 0.3s ease; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
                    <h4 style="font-size: 22px; color: #06b6d4; font-family: 'Orbitron', sans-serif; margin-bottom: 8px;">2. Desarrollador de Ecosistema NexOS Core</h4>
                    <p style="font-weight: 600; color: #111827; margin-bottom: 16px; font-size: 15px;">Departamento: Software & UX.</p>
                    <p style="font-size: 16px; line-height: 1.8; color: #000; text-align: justify;">Tu misión será que la interfaz se adapte al entorno con la misma fluidez que el hardware se adhiere a una pared. Necesitamos a alguien capaz de diseñar una experiencia de usuario táctil y háptica que se sienta natural, eliminando cualquier rastro de fricción digital.</p>
                </div>

                <div style="background: white; border: 1px solid rgba(6, 182, 212, 0.2); padding: 40px; border-radius: 24px; transition: all 0.3s ease; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
                    <h4 style="font-size: 22px; color: #06b6d4; font-family: 'Orbitron', sans-serif; margin-bottom: 8px;">3. Especialista en Captura Energética RF</h4>
                    <p style="font-weight: 600; color: #111827; margin-bottom: 16px; font-size: 15px;">Departamento: Ingeniería de Energía.</p>
                    <p style="font-size: 16px; line-height: 1.8; color: #000; text-align: justify;">¿Te fascina la radio-inducción ambiental? Serás el responsable de que NEXUS SEAMLESS siga alimentándose de las ondas 5G y Wi-Fi del entorno, garantizando una autonomía que desafíe los límites de la carga tradicional. Ayúdanos a que el usuario se olvide de que los cables existieron alguna vez.</p>
                </div>

                <div style="background: white; border: 1px solid rgba(6, 182, 212, 0.2); padding: 40px; border-radius: 24px; transition: all 0.3s ease; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
                    <h4 style="font-size: 22px; color: #06b6d4; font-family: 'Orbitron', sans-serif; margin-bottom: 8px;">4. Estratega de Sostenibilidad y Ciclo de Vida</h4>
                    <p style="font-weight: 600; color: #111827; margin-bottom: 16px; font-size: 15px;">Departamento: Operaciones y Ética Material.</p>
                    <p style="font-size: 16px; line-height: 1.8; color: #000; text-align: justify;">En NEXUS odiamos la obsolescencia. Buscamos a un perfil que garantice que cada miligramo de titanio y polímero sea 100% recuperable, cumpliendo con los protocolos de residuos cero más estrictos del planeta.</p>
                </div>
            </div>
        </section>
    </main>
"""

# replace main section
page_content = re.sub(r'<main>.*?</main>', new_main, page_content, flags=re.DOTALL)

with open(os.path.join(d, "trabaja-con-nosotros.html"), "w", encoding="utf-8") as f:
    f.write(page_content)


for fn in html_files + ["trabaja-con-nosotros.html"]:
    path = os.path.join(d, fn)
    if not os.path.exists(path): continue
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # href="#careers" -> href="trabaja-con-nosotros.html"
    content = content.replace('href="#careers"', 'href="trabaja-con-nosotros.html"')
    # href="index.html#careers" -> href="trabaja-con-nosotros.html"
    content = content.replace('href="index.html#careers"', 'href="trabaja-con-nosotros.html"')

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Created trabaja-con-nosotros.html and updated links.")
