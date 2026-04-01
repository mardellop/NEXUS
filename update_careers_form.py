import os
import re

d = "c:/Users/familia/.gemini/antigravity/playground/celestial-sunspot"
filepath = os.path.join(d, "trabaja-con-nosotros.html")

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

form_html = """
        <section id="application-form-section" style="max-width: 900px; margin: 80px auto 100px; padding: 0 24px;">
            <div style="background: rgba(6, 182, 212, 0.05); border: 1px solid rgba(6, 182, 212, 0.2); padding: 50px; border-radius: 24px;">
                <div style="text-align: center; margin-bottom: 40px;">
                    <h2 class="section-title">Inicia tu conexión</h2>
                    <p style="font-size: 16px; color: #000; line-height: 1.6; max-width: 600px; margin: 10px auto 0;">No nos envíes un PDF estático. Queremos entender tu estructura. Completa los nodos de información para que tu perfil resuene con el núcleo de NEXUS SEAMLESS.</p>
                </div>

                <form id="careers-form" onsubmit="return submitApplication(event)">
                    <!-- 1. Identificación de Origen -->
                    <h4 style="font-size: 20px; font-family: 'Orbitron', sans-serif; color: #111827; margin-bottom: 20px;">1. Identificación de Origen</h4>
                    
                    <div class="form-group-custom" style="margin-bottom: 20px;">
                        <label>Nombre y Apellidos</label>
                        <input type="text" placeholder="(Como aparecen en tu firma digital)" required style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 8px; font-family: 'Inter', sans-serif;">
                    </div>
                    
                    <div class="form-group-custom" style="margin-bottom: 40px;">
                        <label>Enlace de Resonancia</label>
                        <input type="url" placeholder="(URL de tu LinkedIn, Portfolio en Notion o GitHub)" required style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 8px; font-family: 'Inter', sans-serif;">
                    </div>

                    <!-- 2. Especialización de Núcleo -->
                    <h4 style="font-size: 20px; font-family: 'Orbitron', sans-serif; color: #111827; margin-bottom: 20px;">2. Especialización de Núcleo</h4>
                    <div class="form-group-custom" style="margin-bottom: 40px;">
                        <label>Selecciona tu campo de flujo</label>
                        <select required style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 8px; font-family: 'Inter', sans-serif; background: #fff;">
                            <option value="">Selecciona una opción...</option>
                            <option value="hardware">Arquitectura de Grafeno y Nanotubos (Hardware).</option>
                            <option value="software">Interfaz Adaptativa y NexOS (Software/UX).</option>
                            <option value="energia">Ingeniería de Radio-Inducción Ambiental (Energía).</option>
                            <option value="sostenibilidad">Recuperación de Materiales y Ciclo de Vida (Sostenibilidad).</option>
                        </select>
                    </div>

                    <!-- 3. El Manifiesto Personal -->
                    <h4 style="font-size: 20px; font-family: 'Orbitron', sans-serif; color: #111827; margin-bottom: 20px;">3. El Manifiesto Personal</h4>
                    <div class="form-group-custom" style="margin-bottom: 40px;">
                        <label>¿Por qué quieres dejar de doblar la realidad?</label>
                        <textarea rows="5" placeholder="(En lugar de una carta de presentación tradicional, cuéntanos en 200 palabras cómo tu trabajo anterior ha eliminado fricciones o qué límite de la termodinámica te obsesiona romper)" required style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 8px; font-family: 'Inter', sans-serif; resize: vertical;"></textarea>
                    </div>

                    <!-- 4. Evidencia Técnica -->
                    <h4 style="font-size: 20px; font-family: 'Orbitron', sans-serif; color: #111827; margin-bottom: 20px;">4. Evidencia Técnica</h4>
                    <div class="form-group-custom" style="margin-bottom: 40px;">
                        <label>Cargar historial de trayectoria</label>
                        <div style="border: 2px dashed #06b6d4; padding: 20px; border-radius: 8px; text-align: center; background: white;">
                            <input type="file" required accept=".pdf,.doc,.docx,.zip" style="width: 100%; padding: 10px;">
                            <p style="font-size: 13px; color: #666; margin-top: 10px;">(Aceptamos archivos de alta fidelidad. Peso máximo 10MB. Al igual que el titanio, buscamos ligereza y resistencia).</p>
                        </div>
                    </div>

                    <!-- 5. Protocolo de Privacidad -->
                    <h4 style="font-size: 20px; font-family: 'Orbitron', sans-serif; color: #111827; margin-bottom: 20px;">5. Protocolo de Privacidad</h4>
                    <div class="form-group-custom" style="margin-bottom: 40px; display: flex; align-items: flex-start; gap: 12px;">
                        <input type="checkbox" id="privacy-policy" required style="margin-top: 6px; transform: scale(1.2);">
                        <label for="privacy-policy" style="font-size: 15px; color: #000; line-height: 1.5; font-weight: normal;">Confirmo que mis datos serán tratados bajo el Reglamento Global de Protección de Datos Cuánticos (GDPR-Q) y que mi talento es 100% recuperable para este proyecto.</label>
                    </div>

                    <button type="submit" class="btn-cyan-full" style="width: 100%; border-radius: 8px; font-family: 'Orbitron', sans-serif; font-size: 18px; padding: 16px;">ENVIAR FLUJO</button>
                </form>
            </div>
        </section>

        <!-- Confirmation Section (Hidden by Default) -->
        <section id="confirmation-section" style="max-width: 900px; margin: 80px auto 100px; padding: 0 24px; display: none;">
            <div style="background: rgba(6, 182, 212, 0.05); border: 1px solid rgba(6, 182, 212, 0.2); padding: 60px; border-radius: 24px; text-align: center;">
                <div style="width: 80px; height: 80px; background: #111827; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 30px; box-shadow: 0 0 30px rgba(6, 182, 212, 0.3);">
                    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#06b6d4" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                </div>
                
                <h2 class="section-title" style="margin-bottom: 16px;">Conexión Establecida</h2>
                <h3 style="font-size: 22px; color: #111827; margin-bottom: 30px; font-weight: 600;">Tu talento ya fluye con el núcleo de NEXUS SEAMLESS.</h3>
                
                <p style="font-size: 18px; line-height: 1.8; color: #000; text-align: justify; margin-bottom: 40px;">Gracias por compartir tu estructura con nosotros. Hemos recibido tus datos y, al igual que nuestra trama de memoria molecular, ya los estamos integrando en nuestro análisis de red.</p>
                
                <div style="text-align: left; background: white; padding: 30px; border-radius: 16px; margin-bottom: 40px; border: 1px solid #eee;">
                    <h4 style="font-size: 20px; font-family: 'Orbitron', sans-serif; color: var(--primary); margin-bottom: 20px;">¿Qué ocurre ahora?</h4>
                    <p style="font-size: 16px; line-height: 1.6; margin-bottom: 15px;"><strong style="color:#111827;">Sincronización:</strong> Nuestro Arquitecto de Sistemas revisará cómo tu perfil se adhiere a nuestra visión de hardware sin fricciones.</p>
                    <p style="font-size: 16px; line-height: 1.6; margin-bottom: 15px;"><strong style="color:#111827;">Resonancia:</strong> Si detectamos una frecuencia común, nos pondremos en contacto contigo para una sesión de diseño y estrategia. No buscamos entrevistas rígidas, sino diálogos que fluyan.</p>
                    <p style="font-size: 16px; line-height: 1.6;"><strong style="color:#111827;">Latencia Cero:</strong> Odiamos las esperas innecesarias. Recibirás una actualización de nuestro estado en un ciclo máximo de 7 días naturales.</p>
                </div>

                <p style="font-size: 16px; line-height: 1.8; color: #000; margin-bottom: 30px;">Mientras tanto, te invitamos a seguir explorando <a href="blog.html" style="color: var(--primary); font-weight: 600; text-decoration: none;">Seamless Soul</a>, nuestro blog, para entender mejor cómo estamos rediseñando los límites de la física aplicada.</p>
                
                <p style="font-size: 20px; font-style: italic; font-weight: 600; color: #111827; margin-bottom: 40px;">El futuro no se dobla, se enrolla. Y tú acabas de dar el primer giro.</p>
                
                <button onclick="window.location.href='index.html'" class="btn-cyan-full" style="padding: 14px 40px; border-radius: 8px; font-family: 'Orbitron', sans-serif; font-size: 16px; width: auto; display: inline-block;">VOLVER AL ORIGEN</button>
            </div>
        </section>

        <script>
            function submitApplication(e) {
                e.preventDefault();
                // Ocultar formulario y mostrar ventana de confirmacion
                document.getElementById('application-form-section').style.display = 'none';
                document.getElementById('confirmation-section').style.display = 'block';
                window.scrollTo({ top: document.getElementById('confirmation-section').offsetTop - 100, behavior: 'smooth' });
                return false;
            }
        </script>
    </main>
"""

content = re.sub(r'</main>', form_html, content)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Form added to trabaja-con-nosotros.html")
