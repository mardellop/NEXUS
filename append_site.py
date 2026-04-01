import os

html_appends = """
        <section id="specs" class="specs-section">
            <div class="badge">ESPECIFICACIONES TÉCNICAS</div>
            <h2 class="section-title">Ingeniería del Mañana</h2>
            <p class="section-subtitle">Descubre las especificaciones técnicas que hacen del NEXUS S una obra maestra de la ingeniería.</p>
            
            <div class="specs-highlights">
                <div class="spec-highlight">
                    <h4>0.3mm Grosor</h4>
                    <p>Perfil ultradelgado</p>
                </div>
                <div class="spec-highlight">
                    <h4>200x Más Resistente</h4>
                    <p>Que el acero tradicional</p>
                </div>
                <div class="spec-highlight">
                    <h4>72h Autonomía</h4>
                    <p>Batería de alta densidad</p>
                </div>
                <div class="spec-highlight">
                    <h4>∞ Carga Ambiental</h4>
                    <p>Radio-inducción continua</p>
                </div>
            </div>

            <div class="specs-table-container">
                <table class="specs-table">
                    <tbody>
                        <tr>
                            <th>Material</th>
                            <td>Malla de grafeno reforzado con esqueleto de titanio aeroespacial. Polímero electroactivo de memoria de forma.</td>
                        </tr>
                        <tr>
                            <th>Factor de Forma</th>
                            <td>Cilindro base (transporte): 35cm x 5cm diámetro.<br>Desplegado (trabajo): Área de visualización y control hasta 2 metros.</td>
                        </tr>
                        <tr>
                            <th>Energía</th>
                            <td>Células sólidas con recolección de energía electromagnética de radiofrecuencia (Wi-Fi, 5G, ambiental). Cero puertos de carga.</td>
                        </tr>
                        <tr>
                            <th>Conectividad</th>
                            <td>Trama unificada de transmisión de datos sin latencia (< 0.1ms). Enlace neuronal a periféricos biométricos (opcional).</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <section id="testimonials" class="testimonials-section">
            <h2 class="section-title">Lo que dicen los pioneros</h2>
            
            <div class="testimonials-grid">
                <div class="testimonial-card">
                    <p class="quote">"Ha cambiado completamente mi forma de diseñar. Es como llevar una pared entera de estudio creativo en mi mochila."</p>
                    <div class="author">
                        <div class="author-avatar elena">EM</div>
                        <div>
                            <h4>Elena Martínez</h4>
                            <span>Dir. Creativa</span>
                        </div>
                    </div>
                </div>
                <div class="testimonial-card">
                    <p class="quote">"En las obras, desenrollo mi NEXUS S sobre cualquier mesa improvisada y tengo acceso a cada detalle de los planos en tamaño real."</p>
                    <div class="author">
                        <div class="author-avatar david">DC</div>
                        <div>
                            <h4>David Chen</h4>
                            <span>Arquitecto</span>
                        </div>
                    </div>
                </div>
                <div class="testimonial-card">
                    <p class="quote">"Trabajar frente a la playa ya no significa sacrificar mi setup de tres monitores. La conectividad ambiental es simplemente magia pura."</p>
                    <div class="author">
                        <div class="author-avatar sofia">SA</div>
                        <div>
                            <h4>Sofia Andersson</h4>
                            <span>Nómada Digital</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="press-logos">
                <span class="logo">TechCrunch</span>
                <span class="logo">WIRED</span>
                <span class="logo">THE VERGE</span>
                <span class="logo">FAST COMPANY</span>
            </div>
        </section>

        <section id="faq" class="faq-section">
            <div class="faq-container">
                <div class="faq-content">
                    <h2 class="section-title" style="text-align: left;">Preguntas Frecuentes</h2>
                    
                    <div class="accordion">
                        <div class="accordion-item">
                            <button class="accordion-header">
                                ¿Cómo funciona exactamente la carga ambiental?
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
                            </button>
                            <div class="accordion-content">
                                NEXUS S cuenta con antenas microscópicas (rectenas) integradas en su malla de titanio que convierten ondas de radiofrecuencia (Wi-Fi, celular, Bluetooth) en energía de corriente continua, recargando constantemente su batería.
                            </div>
                        </div>
                        <div class="accordion-item">
                            <button class="accordion-header">
                                ¿Qué tan resistente es la pantalla al ser tan delgada?
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
                            </button>
                            <div class="accordion-content">
                                Al utilizar grafeno multicapa estructurado con nanotubos, es aproximadamente 200 veces más resistente a la tracción que el acero y totalmente invulnerable a los rasguños del uso diario.
                            </div>
                        </div>
                        <div class="accordion-item">
                            <button class="accordion-header">
                                ¿Cuándo se enviarán las primeras unidades?
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
                            </button>
                            <div class="accordion-content">
                                Las entregas para quienes reserven en la fase "Cierre/Pre-registro" comenzarán en el tercer cuatrimestre del próximo año.
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="newsletter-card">
                    <div class="newsletter-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                    </div>
                    <h3>Mantente al Día con NEXUS S</h3>
                    <p>Únete a más de <strong>15K+ Suscriptores</strong> y recibe actualizaciones exclusivas del desarrollo y acceso anticipado.</p>
                    <div class="newsletter-input-group">
                        <input type="email" placeholder="tu@email.com">
                        <button class="btn-primary-small">Suscribirse</button>
                    </div>
                </div>
            </div>
        </section>

        <section id="preregister" class="preregister-section">
            <div class="preregister-card">
                <div class="preregister-info">
                    <h2 class="section-title" style="text-align: left; color: white;">Asegura tu lugar en el futuro</h2>
                    <p class="section-subtitle" style="text-align: left; color: rgba(255,255,255,0.7); margin-bottom: 32px;">Regístrate ahora para formar parte del grupo exclusivo de pioneros tecnológicos.</p>
                    
                    <div class="urgency-counter">
                        <div class="urgency-top">
                            <span>Unidades Fundador Disponibles</span>
                            <strong>327 / 1000</strong>
                        </div>
                        <div class="progress-bar-container">
                            <div class="progress-bar" style="width: 32.7%;"></div>
                        </div>
                    </div>
                    
                    <ul class="benefits-list">
                        <li><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Acceso Prioritario (Lote 1)</li>
                        <li><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Paquete Premium "Founder's Edition"</li>
                        <li><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Garantía Extendida de 5 años</li>
                        <li><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Grabado láser personalizado</li>
                    </ul>
                </div>

                <div class="preregister-form-wrapper">
                    <form class="preregister-form">
                        <div class="form-group">
                            <label>Nombre Completo</label>
                            <input type="text" placeholder="Jane Doe">
                        </div>
                        <div class="form-group">
                            <label>Email Profesional</label>
                            <input type="email" placeholder="jane@empresa.com">
                        </div>
                        <div class="form-group">
                            <label>Empresa</label>
                            <input type="text" placeholder="Acme Corp">
                        </div>
                        <div class="form-group">
                            <label>País</label>
                            <select>
                                <option>España</option>
                                <option>México</option>
                                <option>Argentina</option>
                                <option>Chile</option>
                                <option>Colombia</option>
                                <option>Otros</option>
                            </select>
                        </div>
                        <button type="button" class="btn-primary w-full justify-center">Completar Pre-registro</button>
                    </form>
                </div>
            </div>
        </section>

        <footer class="footer">
            <div class="footer-content">
                <div class="footer-logo">
                    <div class="logo-circle">N</div>
                    <span class="logo-text">NEXUS S</span>
                </div>
                <div class="footer-links">
                    <a href="#">Privacidad</a>
                    <a href="#">Términos</a>
                    <a href="#">Prensa</a>
                </div>
                <p class="copyright">© 2026 NEXUS Tech. Todos los derechos reservados.</p>
            </div>
        </footer>
"""

css_appends = """
/* Specifications */
.specs-section {
    max-width: 1000px;
    margin: 0 auto;
    padding: 80px 24px;
    text-align: center;
}

.specs-highlights {
    display: flex;
    justify-content: space-between;
    gap: 16px;
    margin: 48px 0;
}

.spec-highlight {
    flex: 1;
    background: white;
    border: 1px solid var(--border);
    padding: 24px;
    border-radius: 16px;
}

.spec-highlight h4 {
    font-size: 20px;
    font-weight: 800;
    color: var(--primary);
    margin-bottom: 8px;
}

.spec-highlight p {
    font-size: 14px;
    color: var(--text-gray);
}

.specs-table-container {
    background: white;
    border: 1px solid var(--border);
    border-radius: 16px;
    overflow: hidden;
    text-align: left;
}

.specs-table {
    width: 100%;
    border-collapse: collapse;
}

.specs-table tr:not(:last-child) {
    border-bottom: 1px solid var(--border);
}

.specs-table th {
    width: 30%;
    padding: 24px;
    background: #fdfdfd;
    font-weight: 600;
    color: var(--text-dark);
    border-right: 1px solid var(--border);
}

.specs-table td {
    padding: 24px;
    color: var(--text-gray);
    line-height: 1.6;
}

/* Testimonials */
.testimonials-section {
    max-width: 1200px;
    margin: 0 auto;
    padding: 80px 24px;
    text-align: center;
}

.testimonials-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    margin-top: 48px;
}

.testimonial-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 32px;
    text-align: left;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.quote {
    font-size: 16px;
    color: var(--text-dark);
    line-height: 1.6;
    font-style: italic;
    margin-bottom: 24px;
}

.author {
    display: flex;
    align-items: center;
    gap: 16px;
}

.author-avatar {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: 600;
}

.author-avatar.elena { background: #8b5cf6; }
.author-avatar.david { background: #10b981; }
.author-avatar.sofia { background: #f59e0b; }

.author h4 {
    font-size: 15px;
    font-weight: 700;
}

.author span {
    font-size: 13px;
    color: var(--text-gray);
}

.press-logos {
    display: flex;
    justify-content: center;
    gap: 48px;
    margin-top: 48px;
    padding-top: 48px;
    border-top: 1px solid var(--border);
    opacity: 0.5;
}

.press-logos .logo {
    font-weight: 800;
    font-size: 20px;
    letter-spacing: -0.5px;
}

/* FAQ & Newsletter */
.faq-section {
    max-width: 1200px;
    margin: 0 auto;
    padding: 80px 24px;
}

.faq-container {
    display: grid;
    grid-template-columns: 3fr 2fr;
    gap: 64px;
    align-items: start;
}

.accordion-item {
    border-bottom: 1px solid var(--border);
}

.accordion-header {
    width: 100%;
    text-align: left;
    padding: 24px 0;
    background: none;
    border: none;
    font-size: 16px;
    font-weight: 600;
    color: var(--text-dark);
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
}

.accordion-content {
    padding-bottom: 24px;
    color: var(--text-gray);
    line-height: 1.6;
    /* Normally hidden -> display: none; but we'll show it for static demo or add js later */
}

.newsletter-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 32px;
    text-align: center;
    position: sticky;
    top: 100px;
}

.newsletter-icon {
    width: 48px;
    height: 48px;
    background: rgba(6, 182, 212, 0.1);
    color: var(--primary);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 16px;
}

.newsletter-card h3 {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 8px;
}

.newsletter-card p {
    font-size: 14px;
    color: var(--text-gray);
    margin-bottom: 24px;
}

.newsletter-input-group {
    display: flex;
    gap: 8px;
}

.newsletter-input-group input {
    flex: 1;
    padding: 12px 16px;
    border: 1px solid var(--border);
    border-radius: 6px;
    font-size: 14px;
    outline: none;
}

.newsletter-input-group input:focus {
    border-color: var(--primary);
}

/* Preregister */
.preregister-section {
    max-width: 1200px;
    margin: 0 auto;
    padding: 80px 24px 120px;
}

.preregister-card {
    background: var(--text-dark);
    border-radius: 24px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    overflow: hidden;
    position: relative;
    box-shadow: 0 25px 50px rgba(0,0,0,0.25);
}

.preregister-info {
    padding: 64px;
    color: white;
    z-index: 1;
}

.urgency-counter {
    background: rgba(255,255,255,0.1);
    padding: 16px;
    border-radius: 12px;
    margin-bottom: 32px;
}

.urgency-top {
    display: flex;
    justify-content: space-between;
    font-size: 14px;
    margin-bottom: 8px;
}

.progress-bar-container {
    height: 8px;
    background: rgba(255,255,255,0.2);
    border-radius: 9999px;
    overflow: hidden;
}

.progress-bar {
    height: 100%;
    background: var(--primary);
    border-radius: 9999px;
}

.benefits-list {
    list-style: none;
}

.benefits-list li {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 16px;
    font-size: 15px;
}

.preregister-form-wrapper {
    background: white;
    padding: 64px;
}

.preregister-form {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.form-group {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.form-group label {
    font-size: 13px;
    font-weight: 600;
    color: var(--text-dark);
}

.form-group input, .form-group select {
    padding: 12px 16px;
    border: 1px solid var(--border);
    border-radius: 6px;
    font-size: 15px;
    outline: none;
    transition: border-color 0.2s;
    background-color: white;
}

.form-group input:focus, .form-group select:focus {
    border-color: var(--primary);
    box-shadow: 0 0 0 3px rgba(6, 182, 212, 0.1);
}

.w-full {
    width: 100%;
}

.justify-center {
    justify-content: center;
}

/* Footer */
.footer {
    border-top: 1px solid var(--border);
    padding: 40px 24px;
    background: var(--bg-gray);
}

.footer-content {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.footer-logo {
    display: flex;
    align-items: center;
    gap: 8px;
    opacity: 0.5;
    filter: grayscale(1);
}

.footer-links {
    display: flex;
    gap: 24px;
}

.footer-links a {
    color: var(--text-gray);
    text-decoration: none;
    font-size: 14px;
}

.copyright {
    color: var(--text-light);
    font-size: 14px;
}

@media (max-width: 900px) {
    .features-grid, .steps-grid, .testimonials-grid, .metrics-grid {
        grid-template-columns: 1fr;
    }
    .specs-highlights, .faq-container, .preregister-card {
        flex-direction: column;
        grid-template-columns: 1fr;
    }
    .specs-table th, .specs-table td {
        display: block;
        width: 100%;
    }
    .specs-table th {
        border-right: none;
        border-bottom: 1px solid var(--border);
    }
    .footer-content {
        flex-direction: column;
        gap: 24px;
    }
}
"""

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace('</main>', html_appends + '</main>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)


with open("style.css", "a", encoding="utf-8") as f:
    f.write(css_appends)

print("Files appended successfully")
