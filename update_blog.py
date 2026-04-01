import os

html_appends = """        <section id="blog" class="blog-section-new">
            <div class="blog-header-new">
                <h2 class="section-title">Últimas Actualizaciones</h2>
                <p class="section-subtitle">Mantente al día con las últimas innovaciones, artículos técnicos y noticias de NEXUS S</p>
            </div>
            
            <div class="blog-layout">
                <!-- Left Column -->
                <div class="blog-main-col">
                    <h3 class="col-title">Artículos Destacados</h3>
                    
                    <article class="featured-card">
                        <div class="f-image p-grafeno">
                            <span class="f-badge">Tecnología</span>
                        </div>
                        <div class="f-content">
                            <div class="f-meta">
                                <span>15 de diciembre de 2025</span>
                                <span class="dot">•</span>
                                <span><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:inline;vertical-align:-2px;margin-right:4px;"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>5 min</span>
                            </div>
                            <h4 class="f-title">El Grafeno: El Material que Cambiará Todo</h4>
                            <p class="f-desc">Descubre cómo este material de un átomo de grosor está revolucionando la tecnología del futuro y por qué es el...</p>
                            <a href="#" class="f-link">Leer más &rarr;</a>
                        </div>
                    </article>

                    <article class="featured-card">
                        <div class="f-image p-radio">
                            <span class="f-badge">Innovación</span>
                            <span class="f-word">Radio Induction</span>
                        </div>
                        <div class="f-content">
                            <div class="f-meta">
                                <span>10 de diciembre de 2025</span>
                                <span class="dot">•</span>
                                <span><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:inline;vertical-align:-2px;margin-right:4px;"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>7 min</span>
                            </div>
                            <h4 class="f-title">Radio-Inducción: Adiós a los Cargadores</h4>
                            <p class="f-desc">Cómo NEXUS S cosecha energía del aire y por qué nunca más tendrás que buscar un enchufe.</p>
                            <a href="#" class="f-link">Leer más &rarr;</a>
                        </div>
                    </article>

                    <article class="featured-card">
                        <div class="f-image p-design">
                            <span class="f-badge">Diseño</span>
                            <span class="f-word">Design Process</span>
                        </div>
                        <div class="f-content">
                            <div class="f-meta">
                                <span>5 de diciembre de 2025</span>
                                <span class="dot">•</span>
                                <span><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:inline;vertical-align:-2px;margin-right:4px;"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>6 min</span>
                            </div>
                            <h4 class="f-title">Diseñando para la Libertad de Forma</h4>
                            <p class="f-desc">El proceso creativo detrás del primer ordenador que se adapta a tu entorno, no al revés.</p>
                            <a href="#" class="f-link">Leer más &rarr;</a>
                        </div>
                    </article>
                </div>

                <!-- Right Column -->
                <div class="blog-side-col">
                    <h3 class="col-title">Últimas Noticias</h3>
                    
                    <div class="news-list-card">
                        <ul class="n-list">
                            <li>
                                <div class="n-item-title"><span class="dot-cyan"></span>NEXUS S gana el Premio Red Dot 2025</div>
                                <div class="n-item-meta"><span>18 dic</span><span>Red Dot Awards</span></div>
                            </li>
                            <li>
                                <div class="n-item-title"><span class="dot-cyan"></span>Entrevista exclusiva en TechCrunch</div>
                                <div class="n-item-meta"><span>12 dic</span><span>TechCrunch</span></div>
                            </li>
                            <li>
                                <div class="n-item-title"><span class="dot-cyan"></span>1000 unidades pre-vendidas en 48 horas</div>
                                <div class="n-item-meta"><span>8 dic</span><span>NEXUS S Press</span></div>
                            </li>
                            <li>
                                <div class="n-item-title"><span class="dot-cyan"></span>Colaboración con NASA para materiales espaciales</div>
                                <div class="n-item-meta"><span>1 dic</span><span>Space Tech News</span></div>
                            </li>
                        </ul>
                    </div>

                    <div class="side-newsletter">
                        <div class="sn-header">
                            <span class="sn-icon">📫</span>
                            <h4>Newsletter Semanal</h4>
                        </div>
                        <p>Recibe las últimas actualizaciones directamente en tu inbox</p>
                        <button class="btn-primary-small" style="width: 100%; border-radius: 6px; font-weight: 600;">Suscribirse</button>
                    </div>
                </div>
            </div>

            <div class="blog-footer">
                <button class="btn-primary" style="padding: 12px 32px; border-radius: 24px; font-size: 14px; box-shadow: 0 4px 12px rgba(6, 182, 212, 0.4);">Ver Todos los Artículos</button>
            </div>
        </section>"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_idx = html.find('        <section id="blog"')
end_idx = html.find('        <section id="preregister"', start_idx)

if start_idx != -1 and end_idx != -1:
    html = html[:start_idx] + html_appends + "\n" + html[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

css_appends_8 = """

/* Override Blog Structure */
.blog-section-new {
    max-width: 1200px;
    margin: 0 auto;
    padding: 80px 24px;
}

.blog-header-new {
    text-align: center;
    margin-bottom: 64px;
}

.blog-header-new .section-title {
    font-size: 40px;
    font-weight: 800;
    color: #0b1120;
    margin-bottom: 16px;
}

.blog-header-new .section-subtitle {
    font-size: 16px;
    color: var(--text-gray);
    max-width: 600px;
    margin: 0 auto;
    line-height: 1.5;
}

.col-title {
    font-size: 20px;
    font-weight: 700;
    color: #0b1120;
    margin-bottom: 24px;
}

.blog-layout {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 40px;
    margin-bottom: 48px;
}

/* Featured Articles */
.featured-card {
    display: flex;
    background: white;
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
    margin-bottom: 24px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.02);
    min-height: 200px;
}

.f-image {
    width: 35%;
    background-color: #0A0A0A;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}

.f-badge {
    position: absolute;
    top: 16px;
    left: 16px;
    background: var(--primary);
    color: white;
    font-size: 11px;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 20px;
}

.f-word {
    color: var(--primary);
    font-size: 28px;
    font-weight: 600;
    letter-spacing: -0.5px;
}

.f-content {
    padding: 24px 32px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.f-meta {
    font-size: 12px;
    color: var(--text-light);
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.f-meta .dot {
    opacity: 0.5;
}

.f-title {
    font-size: 20px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 12px;
    line-height: 1.3;
}

.f-desc {
    font-size: 14px;
    color: var(--text-gray);
    line-height: 1.6;
    margin-bottom: 16px;
    flex: 1;
}

.f-link {
    font-size: 14px;
    font-weight: 700;
    color: var(--primary);
    text-decoration: none;
    display: inline-flex;
    align-items: center;
}

/* Latest News List */
.news-list-card {
    background: white;
    border: 1px solid rgba(6, 182, 212, 0.2);
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    margin-bottom: 24px;
}

.n-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.n-list li {
    padding: 24px;
    border-bottom: 1px solid rgba(0,0,0,0.04);
}

.n-list li:last-child {
    border-bottom: none;
}

.n-item-title {
    font-size: 14px;
    font-weight: 600;
    color: #0f172a;
    margin-bottom: 16px;
    display: flex;
    align-items: baseline;
    gap: 8px;
    line-height: 1.4;
}

.dot-cyan {
    display: inline-block;
    width: 6px;
    height: 6px;
    background: var(--primary);
    border-radius: 50%;
    flex-shrink: 0;
}

.n-item-meta {
    display: flex;
    justify-content: space-between;
    font-size: 11px;
    color: var(--text-light);
    padding-left: 14px;
    font-weight: 500;
}

.n-item-meta span:last-child {
    color: var(--primary);
    font-weight: 600;
    opacity: 0.8;
}

/* Side Newsletter */
.side-newsletter {
    background: linear-gradient(135deg, #e0f2fe, #cffafe);
    border: 1px solid rgba(6, 182, 212, 0.3);
    border-radius: 12px;
    padding: 24px;
    box-shadow: 0 4px 12px rgba(6, 182, 212, 0.1);
}

.sn-header {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 12px;
}

.sn-header h4 {
    font-size: 16px;
    font-weight: 700;
    color: #083344;
}

.sn-icon {
    font-size: 16px;
}

.side-newsletter p {
    font-size: 13px;
    color: #164e63;
    line-height: 1.5;
    margin-bottom: 20px;
}

.blog-footer {
    text-align: center;
    margin-top: 24px;
}

@media (max-width: 900px) {
    .blog-layout {
        grid-template-columns: 1fr;
    }
    .f-image {
        width: 100%;
        height: 160px;
    }
    .featured-card {
        flex-direction: column;
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_appends_8)

print("Blog Structure updated via Python")
