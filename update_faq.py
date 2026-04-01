import os
import re

html_appends = """
        <section id="faq" class="faq-section-new">
            <div class="faq-header-new">
                <span class="faq-badge">PREGUNTAS FRECUENTES</span>
                <h2 class="section-title">Todo lo que Necesitas Saber</h2>
                <p class="section-subtitle">Respuestas a las preguntas más comunes sobre NEXUS S</p>
            </div>
            
            <div class="accordion-new">
                <div class="accordion-item-new">
                    <button class="accordion-header-new" onclick="toggleAccordion(this)">
                        ¿Cómo funciona la carga por inducción ambiental?
                        <svg class="accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
                    </button>
                    <div class="accordion-content-new">
                        <div class="accordion-content-inner">
                            NEXUS S cuenta con antenas microscópicas (rectenas) integradas en su malla de titanio que convierten ondas de radiofrecuencia (Wi-Fi, celular, Bluetooth) en energía de corriente continua, recargando constantemente su batería. No necesitas enchufes.
                        </div>
                    </div>
                </div>

                <div class="accordion-item-new">
                    <button class="accordion-header-new" onclick="toggleAccordion(this)">
                        ¿La pantalla de grafeno es resistente?
                        <svg class="accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
                    </button>
                    <div class="accordion-content-new">
                        <div class="accordion-content-inner">
                            Absolutamente. Al utilizar grafeno multicapa estructurado con nanotubos, es aproximadamente 200 veces más resistente a la tracción que el acero y totalmente invulnerable a los rasguños del uso diario. Puedes enrollarlo miles de veces sin dañarlo.
                        </div>
                    </div>
                </div>

                <div class="accordion-item-new">
                    <button class="accordion-header-new" onclick="toggleAccordion(this)">
                        ¿Cómo conecto periféricos sin puertos USB?
                        <svg class="accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
                    </button>
                    <div class="accordion-content-new">
                        <div class="accordion-content-inner">
                            NEXUS S utiliza una Trama Conductiva Unificada. Toda la superficie del dispositivo puede transmitir datos y energía magnéticamente con latencia cercana a cero. Puedes adherir periféricos magnéticos en cualquier parte de la estructura.
                        </div>
                    </div>
                </div>

                <div class="accordion-item-new">
                    <button class="accordion-header-new" onclick="toggleAccordion(this)">
                        ¿Cuánto tiempo dura la batería?
                        <svg class="accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
                    </button>
                    <div class="accordion-content-new">
                        <div class="accordion-content-inner">
                            En un entorno sin radiación electromagnética (donde la carga ambiental no es posible), la celda de estado sólido de alta densidad proporciona hasta 72 horas de uso continuo gracias a la eficiencia térmica de su arquitectura.
                        </div>
                    </div>
                </div>

                <div class="accordion-item-new">
                    <button class="accordion-header-new" onclick="toggleAccordion(this)">
                        ¿Es compatible con mis aplicaciones actuales?
                        <svg class="accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
                    </button>
                    <div class="accordion-content-new">
                        <div class="accordion-content-inner">
                            Sí. NEXUS S corre un micro-kernel especial que ejecuta contenedores virtuales en tiempo real, lo que le permite emular entornos Windows, macOS y Linux a la perfección y sin pérdida aparente de rendimiento.
                        </div>
                    </div>
                </div>

                <div class="accordion-item-new">
                    <button class="accordion-header-new" onclick="toggleAccordion(this)">
                        ¿Cuándo estará disponible?
                        <svg class="accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
                    </button>
                    <div class="accordion-content-new">
                        <div class="accordion-content-inner">
                            Las entregas para quienes reserven en la fase "Early Adopter" comenzarán en el tercer cuatrimestre del próximo año. Todas las unidades reservadas ahora están garantizadas en la primera ola de fabricación.
                        </div>
                    </div>
                </div>
            </div>
            
            <script>
                function toggleAccordion(btn) {
                    const item = btn.parentElement;
                    const content = item.querySelector('.accordion-content-new');
                    const icon = item.querySelector('.accordion-icon');
                    
                    // Close others
                    document.querySelectorAll('.accordion-item-new').forEach(otherItem => {
                        if (otherItem !== item) {
                            otherItem.classList.remove('is-open');
                            const otherContent = otherItem.querySelector('.accordion-content-new');
                            otherContent.style.maxHeight = '0px';
                            otherItem.querySelector('.accordion-icon').style.transform = 'rotate(0deg)';
                        }
                    });

                    // Toggle current
                    if (item.classList.contains('is-open')) {
                        item.classList.remove('is-open');
                        content.style.maxHeight = '0px';
                        icon.style.transform = 'rotate(0deg)';
                    } else {
                        item.classList.add('is-open');
                        content.style.maxHeight = content.scrollHeight + 'px';
                        icon.style.transform = 'rotate(180deg)';
                    }
                }
            </script>
        </section>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# I am finding the faq-section to replace it. Notice that newsletter-card is inside faq-container.
# We will pull newsletter-card out temporarily, or just abandon it if it's not needed. But wait, we shouldn't delete the newsletter, we can just put it independently.
# Actually, the user wants to replace the faq section aesthetic. I'll detach newsletter card into its own section directly below.

start_idx = html.find('        <section id="faq" class="faq-section">')
end_idx = html.find('        <section id="blog"', start_idx)

if start_idx != -1 and end_idx != -1:
    old_faq_block = html[start_idx:end_idx]
    
    # Isolate newsletter
    news_start = old_faq_block.find('<div class="newsletter-card">')
    news_end = old_faq_block.find('</section>', news_start)
    if news_start != -1 and news_end != -1:
        newsletter_html = '''
        <section class="newsletter-section" style="max-width: 600px; margin: 40px auto 120px; text-align:center;">
''' + old_faq_block[news_start:news_end-22] + '''
        </section>
'''
    else:
        newsletter_html = ''

    new_block = html_appends + "\n" + newsletter_html
    
    html = html[:start_idx] + new_block + html[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

css_appends_6 = """

/* Override FAQ */
.faq-section-new {
    max-width: 800px;
    margin: 0 auto;
    padding: 120px 24px 80px;
    text-align: center;
}

.faq-header-new {
    margin-bottom: 64px;
}

.faq-badge {
    color: var(--primary);
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    display: block;
    margin-bottom: 16px;
}

.faq-header-new .section-title {
    font-size: 48px;
    font-weight: 800;
    color: #0b1120;
    margin-bottom: 12px;
}

.faq-header-new .section-subtitle {
    font-size: 16px;
    color: var(--text-gray);
}

.accordion-new {
    display: flex;
    flex-direction: column;
    gap: 16px;
    text-align: left;
}

.accordion-item-new {
    background: white;
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
    transition: all 0.3s ease;
    box-shadow: 0 2px 4px rgba(0,0,0,0.01);
}

.accordion-item-new:hover {
    border-color: rgba(6, 182, 212, 0.3);
    box-shadow: 0 4px 12px rgba(6, 182, 212, 0.05);
}

.accordion-item-new.is-open {
    border-color: rgba(6, 182, 212, 0.5);
    box-shadow: 0 4px 12px rgba(6, 182, 212, 0.1);
}

.accordion-header-new {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 24px;
    background: none;
    border: none;
    font-size: 16px;
    font-weight: 600;
    color: #0f172a;
    cursor: pointer;
    transition: color 0.2s;
}

.accordion-header-new:hover {
    color: var(--primary);
}

.accordion-icon {
    color: #94a3b8;
    transition: transform 0.3s ease;
}

.accordion-item-new.is-open .accordion-header-new {
    color: var(--primary);
}

.accordion-item-new.is-open .accordion-icon {
    color: var(--primary);
}

.accordion-content-new {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.4s ease-in-out;
}

.accordion-content-inner {
    padding: 0 24px 24px;
    color: var(--text-gray);
    line-height: 1.6;
    font-size: 15px;
}

/* Fix newsletter positioning */
.newsletter-section .newsletter-card {
    position: static;
    margin: 0 auto;
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_appends_6)

print("FAQ Script Injected")
