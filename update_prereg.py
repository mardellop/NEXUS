import os

html_replacement = """        <section id="preregister" class="preregister-section-new">
            <div class="prereg-header">
                <span class="prereg-badge">RESERVA AHORA</span>
                <h2 class="section-title">Sé de los Primeros en Experimentar el Futuro</h2>
                <p class="section-subtitle">Los primeros 1000 usuarios que reserven recibirán acceso prioritario, paquete de accesorios premium y 3 años de garantía extendida</p>
            </div>

            <div class="prereg-container">
                <!-- Left: Form Card -->
                <div class="prereg-form-card">
                    <form class="main-prereg-form">
                        <div class="form-group-custom">
                            <label>Nombre Completo *</label>
                            <div class="input-with-icon">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i-icon"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                                <input type="text" placeholder="Tu nombre">
                            </div>
                        </div>

                        <div class="form-group-custom">
                            <label>Email *</label>
                            <div class="input-with-icon">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i-icon"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                                <input type="email" placeholder="tu@email.com">
                            </div>
                        </div>

                        <div class="form-group-custom">
                            <label>Empresa *</label>
                            <div class="input-with-icon">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i-icon"><rect x="4" y="2" width="16" height="20" rx="2" ry="2"></rect><line x1="9" y1="22" x2="9" y2="2"></line><line x1="15" y1="22" x2="15" y2="2"></line><line x1="4" y1="6" x2="20" y2="6"></line><line x1="4" y1="10" x2="20" y2="10"></line><line x1="4" y1="14" x2="20" y2="14"></line><line x1="4" y1="18" x2="20" y2="18"></line></svg>
                                <input type="text" placeholder="Nombre de tu empresa">
                            </div>
                        </div>

                        <div class="form-group-custom">
                            <label>País *</label>
                            <div class="input-with-icon">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i-icon"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
                                <select>
                                    <option>Selecciona tu país</option>
                                    <option>España</option>
                                    <option>México</option>
                                    <option>Estados Unidos</option>
                                </select>
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="select-arrow"><polyline points="6 9 12 15 18 9"></polyline></svg>
                            </div>
                        </div>

                        <button type="button" class="btn-cyan-full">Reservar Mi NEXUS S</button>
                        <p class="form-card-footer">No se requiere pago inicial. Te contactaremos para finalizar tu reserva.</p>
                    </form>
                </div>

                <!-- Right: Benefits Column -->
                <div class="prereg-benefits-col">
                    <h3 class="b-title">Beneficios del Pre-registro</h3>
                    
                    <div class="benefit-item-card">
                        <div class="b-icon-wrap">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        </div>
                        <div class="b-info">
                            <h4>Acceso Prioritario</h4>
                            <p>Sé de los primeros en recibir tu NEXUS S en Q2 2026</p>
                        </div>
                    </div>

                    <div class="benefit-item-card">
                        <div class="b-icon-wrap">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        </div>
                        <div class="b-info">
                            <h4>Paquete Premium</h4>
                            <p>Incluye teclado magnético, estuche de titanio y stylus de grafeno</p>
                        </div>
                    </div>

                    <div class="benefit-item-card">
                        <div class="b-icon-wrap">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        </div>
                        <div class="b-info">
                            <h4>Garantía Extendida</h4>
                            <p>3 años de cobertura completa sin costo adicional</p>
                        </div>
                    </div>

                    <div class="benefit-item-card">
                        <div class="b-icon-wrap">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        </div>
                        <div class="b-info">
                            <h4>Soporte Exclusivo</h4>
                            <p>Línea directa con el equipo de ingeniería 24/7</p>
                        </div>
                    </div>

                    <div class="benefit-item-card">
                        <div class="b-icon-wrap">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        </div>
                        <div class="b-info">
                            <h4>Actualizaciones Prioritarias</h4>
                            <p>Acceso anticipado a nuevas características y mejoras</p>
                        </div>
                    </div>

                    <!-- Progress Bar Card -->
                    <div class="units-card">
                        <div class="u-header">
                            <span>Unidades Disponibles</span>
                            <strong>327 / 1000</strong>
                        </div>
                        <div class="u-progress-bg">
                            <div class="u-progress-fill" style="width: 32.7%;"></div>
                        </div>
                        <div class="u-footer">
                            <span class="bolt">⚡</span> Solo quedan 327 unidades disponibles para pre-registro
                        </div>
                    </div>
                </div>
            </div>
        </section>"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
html = re.sub(r'<section id="preregister" class="preregister-section">.*?</section>', html_replacement, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

css_appends_9 = """

/* Override Preregister Section */
.preregister-section-new {
    background-color: #f0f9ff; /* Light blue background */
    padding: 100px 24px;
}

.prereg-header {
    text-align: center;
    margin-bottom: 64px;
}

.prereg-badge {
    color: var(--primary);
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    display: block;
    margin-bottom: 24px;
}

.prereg-header .section-title {
    font-size: 48px;
    font-weight: 800;
    color: #0b1120;
    margin-bottom: 16px;
}

.prereg-header .section-subtitle {
    font-size: 18px;
    color: var(--text-gray);
    max-width: 700px;
    margin: 0 auto;
    line-height: 1.5;
}

.prereg-container {
    max-width: 1100px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 64px;
    align-items: start;
}

.prereg-form-card {
    background: white;
    border: 2px solid #bae6fd;
    border-radius: 32px;
    padding: 48px;
    box-shadow: 0 10px 25px rgba(6, 182, 212, 0.05);
}

.form-group-custom {
    margin-bottom: 24px;
}

.form-group-custom label {
    display: block;
    font-size: 14px;
    font-weight: 700;
    color: #475569;
    margin-bottom: 10px;
}

.input-with-icon {
    position: relative;
    display: flex;
    align-items: center;
}

.input-with-icon .i-icon {
    position: absolute;
    left: 16px;
    color: #94a3b8;
    pointer-events: none;
}

.input-with-icon input, 
.input-with-icon select {
    width: 100%;
    padding: 14px 16px 14px 48px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    font-size: 14px;
    color: #1e293b;
    outline: none;
    appearance: none;
    transition: all 0.2s;
}

.input-with-icon input:focus, 
.input-with-icon select:focus {
    border-color: var(--primary);
    background: white;
    box-shadow: 0 0 0 3px rgba(6, 182, 212, 0.1);
}

.select-arrow {
    position: absolute;
    right: 16px;
    color: #94a3b8;
    pointer-events: none;
}

.btn-cyan-full {
    width: 100%;
    background: #06b6d4;
    color: white;
    font-size: 16px;
    font-weight: 700;
    padding: 16px;
    border-radius: 12px;
    border: none;
    cursor: pointer;
    margin-top: 16px;
    transition: all 0.3s;
    box-shadow: 0 10px 15px -3px rgba(6, 182, 212, 0.3);
}

.btn-cyan-full:hover {
    background: #0891b2;
    transform: translateY(-2px);
    box-shadow: 0 20px 25px -5px rgba(6, 182, 212, 0.4);
}

.form-card-footer {
    text-align: center;
    font-size: 12px;
    color: #64748b;
    margin-top: 24px;
}

.b-title {
    font-size: 24px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 32px;
}

.benefit-item-card {
    background: white;
    border: 1px solid #f1f5f9;
    border-radius: 16px;
    padding: 24px;
    display: flex;
    gap: 20px;
    margin-bottom: 20px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    transition: transform 0.2s;
}

.benefit-item-card:hover {
    transform: translateX(8px);
    border-color: rgba(6, 182, 212, 0.2);
}

.b-icon-wrap {
    width: 44px;
    height: 44px;
    background: white;
    border: 2px solid #22d3ee;
    color: #22d3ee;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}

.b-info h4 {
    font-size: 16px;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 4px;
}

.b-info p {
    font-size: 13px;
    color: #64748b;
    line-height: 1.5;
}

.units-card {
    background: #cffafe;
    border: 2px solid #22d3ee;
    border-radius: 16px;
    padding: 32px;
    margin-top: 40px;
    box-shadow: 0 10px 20px rgba(6, 182, 212, 0.1);
}

.u-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}

.u-header span {
    font-size: 14px;
    font-weight: 700;
    color: #0e7490;
}

.u-header strong {
    font-size: 14px;
    font-weight: 800;
    color: #0891b2;
}

.u-progress-bg {
    height: 10px;
    background: #e2e8f0;
    border-radius: 10px;
    margin-bottom: 20px;
    overflow: hidden;
}

.u-progress-fill {
    height: 100%;
    background: #0891b2;
    border-radius: 10px;
}

.u-footer {
    font-size: 12px;
    color: #06b6d4;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 6px;
}

.u-footer .bolt {
    font-size: 14px;
}

@media (max-width: 1000px) {
    .prereg-container {
        grid-template-columns: 1fr;
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_appends_9)

print("Preregister section updated")
