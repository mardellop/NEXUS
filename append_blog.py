import os

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The blog html section
blog_html = """
        <section id="blog" class="blog-section">
            <div class="badge">NUEVAS ACTUALIZACIONES</div>
            <h2 class="section-title">Últimas noticias de NEXUS S</h2>
            <p class="section-subtitle">Mantente al tanto del desarrollo, innovación y comunidad de nuestro ecosistema.</p>
            
            <div class="blog-grid">
                <article class="blog-card">
                    <div class="blog-image placeholder-image-1"></div>
                    <div class="blog-content">
                        <span class="blog-date">15 Marzo 2026</span>
                        <h3 class="blog-title">El titanio invisible: ¿Cómo fabricamos nuestra malla?</h3>
                        <p class="blog-desc">Descubre el proceso de ingeniería detrás del esqueleto de carbono que hace posible la flexibilidad extrema sin sacrificar durabilidad.</p>
                        <a href="#" class="blog-link">Leer artículo →</a>
                    </div>
                </article>
                
                <article class="blog-card">
                    <div class="blog-image placeholder-image-2"></div>
                    <div class="blog-content">
                        <span class="blog-date">02 Marzo 2026</span>
                        <h3 class="blog-title">Radio-inducción al descubierto</h3>
                        <p class="blog-desc">Una inmersión profunda técnica en nuestro sistema que le permite a tu ordenador cosechar energía electromagnética del aire.</p>
                        <a href="#" class="blog-link">Leer artículo →</a>
                    </div>
                </article>

                <article class="blog-card">
                    <div class="blog-image placeholder-image-3"></div>
                    <div class="blog-content">
                        <span class="blog-date">21 Febrero 2026</span>
                        <h3 class="blog-title">El futuro sin cables es real</h3>
                        <p class="blog-desc">Nuestra presentación detallando por qué hemos decidido eliminar por completo los conectores físicos y puertos USB.</p>
                        <a href="#" class="blog-link">Leer artículo →</a>
                    </div>
                </article>
            </div>
        </section>
"""

# Find where to insert blog part (before preregister)
html = html.replace('<section id="preregister"', blog_html + '\n        <section id="preregister"')

# Fix footer location if needed (moving it out of <main>)
if '<footer ' in html and '</main>' in html:
    # Remove </main> from its current location
    html = html.replace('</main>', '')
    # Inject it before the footer definition
    html = html.replace('<footer class="footer">', '</main>\n\n        <footer class="footer">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# Update style.css
css_appends = """
/* Blog */
.blog-section {
    max-width: 1200px;
    margin: 0 auto;
    padding: 80px 24px;
    text-align: center;
}

.blog-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 32px;
    margin-top: 48px;
}

.blog-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 16px;
    overflow: hidden;
    text-align: left;
    transition: transform 0.2s, box-shadow 0.2s;
    display: flex;
    flex-direction: column;
}

.blog-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 15px 30px rgba(0,0,0,0.08);
}

.blog-image {
    width: 100%;
    height: 200px;
    background-color: var(--border);
}

.placeholder-image-1 { background: linear-gradient(45deg, #06b6d4, #3b82f6); opacity: 0.8; }
.placeholder-image-2 { background: linear-gradient(45deg, #8b5cf6, #ec4899); opacity: 0.8; }
.placeholder-image-3 { background: linear-gradient(45deg, #10b981, #06b6d4); opacity: 0.8; }

.blog-content {
    padding: 24px;
    flex: 1;
    display: flex;
    flex-direction: column;
}

.blog-date {
    font-size: 13px;
    color: var(--primary);
    font-weight: 600;
    margin-bottom: 8px;
}

.blog-title {
    font-size: 18px;
    font-weight: 700;
    line-height: 1.4;
    margin-bottom: 12px;
    color: var(--text-dark);
}

.blog-desc {
    font-size: 14px;
    color: var(--text-gray);
    line-height: 1.6;
    margin-bottom: 24px;
    flex: 1;
}

.blog-link {
    font-size: 14px;
    font-weight: 600;
    color: var(--primary);
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    transition: color 0.2s;
}

.blog-link:hover {
    color: var(--primary-hover);
}

@media (max-width: 900px) {
    .blog-grid {
        grid-template-columns: 1fr;
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_appends)

print("Blog section injected nicely")
