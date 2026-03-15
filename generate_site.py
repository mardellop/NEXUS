import os

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NEXUS S</title>
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
    <div class="bg-gradient"></div>
    <div class="grid-overlay"></div>
    <div class="vignette-overlay"></div>

    <header class="header">
        <div class="header-container">
            <div class="logo">
                <div class="logo-circle">N</div>
                <span class="logo-text">NEXUS S</span>
            </div>
            <nav class="nav">
                <a href="#features">Características</a>
                <a href="#specs">Especificaciones</a>
                <a href="#testimonials">Testimonios</a>
                <a href="#faq">FAQ</a>
                <a href="#blog">Blog</a>
                <a href="#preregister" class="btn-primary-small">Reservar Ahora</a>
            </nav>
        </div>
    </header>

    <main>
        <section class="hero">
            <div class="badge">LA TECNOLOGÍA QUE FLUYE</div>
            <h1 class="hero-title">El futuro no se dobla,<br><span class="hero-highlight">se enrolla</span></h1>
            <p class="hero-subtitle">NEXUS S presenta el primer ordenador de geometría variable del mundo. De un<br>cilindro de titanio a un espacio de trabajo de 2 metros. Sin cables. Sin límites.</p>
            <div class="hero-buttons">
                <a href="#preregister" class="btn-primary">Reserva tu NEXUS S <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
                <a href="#demo" class="btn-secondary"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"/></svg> Ver Demo</a>
            </div>
        </section>

        <section id="demo" class="demo-section">
            <div class="video-container">
                <div class="video-placeholder">NEXUS S Hero Image</div>
            </div>
            
            <div class="scroll-indicator">
                <div class="mouse"></div>
            </div>

            <div class="demo-intro">
                <div class="badge">VE NEXUS S EN ACCIÓN</div>
                <h2 class="section-title">De Bolsillo a Espacio de Trabajo</h2>
                <p class="section-subtitle">Observa cómo NEXUS S se transforma de un cilindro compacto a una estación de<br>trabajo completa en segundos.</p>
            </div>

            <div class="demo-card">
                <div class="play-button-large">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" class="play-icon" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"/></svg>
                </div>
                <div class="video-placeholder-bottom">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="15" rx="2" ry="2"/><polyline points="17 2 12 7 7 2"/></svg>
                    Placeholder para Video Demo - Añade tu video promocional aquí
                </div>
                
                <div class="metrics-grid">
                    <div class="metric">
                        <h3>2m</h3>
                        <p>Pantalla Desplegada</p>
                    </div>
                    <div class="metric">
                        <h3>450g</h3>
                        <p>Peso Portátil</p>
                    </div>
                    <div class="metric">
                        <h3>0</h3>
                        <p>Cables Necesarios</p>
                    </div>
                </div>
            </div>

            <div class="steps-grid">
                <div class="step">
                    <div class="step-number">1</div>
                    <h4>Desenrolla</h4>
                    <p>Extrae la pantalla de grafeno del cilindro de titanio</p>
                </div>
                <div class="step">
                    <div class="step-number">2</div>
                    <h4>Activa</h4>
                    <p>El polímero electroactivo rigidiza la superficie automáticamente</p>
                </div>
                <div class="step">
                    <div class="step-number">3</div>
                    <h4>Trabaja</h4>
                    <p>Disfruta de hasta 2 metros de espacio de trabajo sin cables</p>
                </div>
            </div>
        </section>

        <section id="features" class="features-section">
            <div class="badge">INNOVACIÓN SIN PRECEDENTES</div>
            <h2 class="section-title">Tecnología que Redefine lo Posible</h2>
            <p class="section-subtitle">Cada componente de NEXUS S ha sido reimaginado desde cero para crear una<br>experiencia sin compromisos.</p>

            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l-9 4.9V17L12 22l9-4.9V7L12 2Z"></path><path d="M12 22v-9V2"></path><path d="M12 7 3 11.9l9 4.9 9-4.9L12 7Z"></path></svg>
                    </div>
                    <h3>Arquitectura de Nanotubos</h3>
                    <p>Un esqueleto invisible de carbono que permite que el dispositivo sea tan ligero como una hoja de papel, pero más resistente que el acero.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path></svg>
                    </div>
                    <h3>Energía de Radio-Inducción</h3>
                    <p>No se enchufa. El dispositivo cosecha las ondas electromagnéticas del ambiente (Wi-Fi, 5G, radio) para mantener su batería siempre llena.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M16 8l-8 8"></path><path d="M8 8V16h8"></path></svg>
                    </div>
                    <h3>Geometría Variable</h3>
                    <p>De 35cm portátil a 2 metros de espacio de trabajo. Tu oficina se adapta a ti, no tú a ella.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="2" x2="12" y2="22"></line><line x1="2" y1="12" x2="22" y2="12"></line></svg>
                    </div>
                    <h3>Trama Conductiva Unificada</h3>
                    <p>Olvida los puertos USB. La propia 'piel' del dispositivo transmite datos y energía magnéticamente, logrando latencia cero.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                    </div>
                    <h3>Memoria de Forma</h3>
                    <p>Gracias a polímeros electroactivos, la pantalla puede pasar de ser flexible a un monitor curvo rígido que se sostiene solo.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                    </div>
                    <h3>Materiales del Futuro</h3>
                    <p>Grafeno reforzado y titanio. Dispositivos que duran décadas, no trimestres.</p>
                </div>
            </div>
        </section>
        
    </main>
    <a href="https://app.emergent.sh" target="_blank" class="emergent-badge">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" fill="none">
            <path d="M15.5702 8.13142C15.7729 8.0412 16.0007 8.18878 15.9892 8.4103C15.8374 11.3192 14.0965 14.0405 11.2531 15.3065C8.40964 16.5725 5.2224 16.0453 2.95912 14.2117C2.78676 14.072 2.82955 13.804 3.03219 13.7137L4.95677 12.8568C5.04866 12.8159 5.15446 12.823 5.24204 12.8725C6.73377 13.7153 8.59176 13.8649 10.2772 13.1145C11.9626 12.3641 13.0947 10.8833 13.4665 9.21075C13.4883 9.11256 13.5539 9.02918 13.6457 8.98827L15.5702 8.13142Z" fill="white"/>
            <path fill-rule="evenodd" clip-rule="evenodd" d="M15.3066 4.74698L15.5067 5.19653C15.5759 5.35178 15.5061 5.53366 15.3508 5.60278L1.29992 11.8586C1.14467 11.9278 0.962794 11.8579 0.893675 11.7027L0.701732 11.2716L0.693457 11.2531C-1.10317 7.21778 0.711626 2.49007 4.74692 0.693443C8.78221 -1.10318 13.51 0.711693 15.3066 4.74698ZM2.82356 8.55367C2.63552 8.63739 2.41991 8.51617 2.40853 8.31065C2.28373 6.05724 3.53858 3.85787 5.72286 2.88536C7.90715 1.91286 10.3813 2.45199 11.9724 4.05256C12.1175 4.19854 12.0633 4.43988 11.8753 4.5236L2.82356 8.55367Z" fill="white"/>
        </svg>
        <span>Made with Emergent</span>
    </a>
</body>
</html>
"""

css_content = """* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif;
}

:root {
    --primary: #06b6d4;
    --primary-hover: #0891b8;
    --text-dark: #111827;
    --text-gray: #4b5563;
    --text-light: #9ca3af;
    --border: #e5e7eb;
    --bg-white: #ffffff;
    --bg-gray: #f9fafb;
}

body {
    color: var(--text-dark);
    background-color: var(--bg-white);
    overflow-x: hidden;
    position: relative;
    line-height: 1.5;
}

.bg-gradient {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(circle at center, #ffffff 0%, #f3f4f6 50%, #ecfeff 100%);
    z-index: -3;
    opacity: 0.5;
}

.grid-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image: 
        linear-gradient(to right, rgba(0,0,0,0.03) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(0,0,0,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    z-index: -2;
}

.vignette-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(circle, transparent 60%, rgba(6, 182, 212, 0.05) 100%);
    pointer-events: none;
    z-index: -1;
}

.header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--border);
    z-index: 100;
}

.header-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 24px;
    height: 64px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    display: flex;
    align-items: center;
    gap: 8px;
}

.logo-circle {
    width: 32px;
    height: 32px;
    background-color: var(--primary);
    border-radius: 50%;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 18px;
}

.logo-text {
    font-weight: 700;
    font-size: 18px;
    letter-spacing: -0.5px;
}

.nav {
    display: flex;
    align-items: center;
    gap: 32px;
}

.nav a {
    text-decoration: none;
    color: var(--text-gray);
    font-size: 14px;
    font-weight: 500;
    transition: color 0.2s;
}

.nav a:hover:not(.btn-primary-small) {
    color: var(--text-dark);
}

.btn-primary-small {
    background-color: var(--primary);
    color: white !important;
    padding: 8px 16px;
    border-radius: 6px;
    font-weight: 600;
    transition: background-color 0.2s;
}

.btn-primary-small:hover {
    background-color: var(--primary-hover);
}

.hero {
    padding: 160px 24px 80px;
    text-align: center;
    max-width: 800px;
    margin: 0 auto;
}

.badge {
    display: inline-flex;
    align-items: center;
    background: rgba(6, 182, 212, 0.1);
    color: var(--primary);
    padding: 6px 12px;
    border-radius: 9999px;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.5px;
    margin-bottom: 24px;
    text-transform: uppercase;
}

.hero-title {
    font-size: 72px;
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -2px;
    margin-bottom: 24px;
}

.hero-highlight {
    color: var(--primary);
}

.hero-subtitle {
    font-size: 18px;
    color: var(--text-gray);
    margin-bottom: 40px;
    line-height: 1.6;
}

.hero-buttons {
    display: flex;
    justify-content: center;
    gap: 16px;
}

.btn-primary {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background-color: var(--primary);
    color: white;
    padding: 14px 28px;
    border-radius: 8px;
    font-weight: 600;
    text-decoration: none;
    font-size: 16px;
    transition: background-color 0.2s;
}

.btn-primary:hover {
    background-color: var(--primary-hover);
}

.btn-secondary {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background-color: transparent;
    color: var(--primary);
    padding: 14px 28px;
    border-radius: 8px;
    font-weight: 600;
    text-decoration: none;
    font-size: 16px;
    border: 1px solid var(--primary);
    transition: all 0.2s;
}

.btn-secondary:hover {
    background-color: rgba(6, 182, 212, 0.05);
}

.demo-section {
    max-width: 1000px;
    margin: 0 auto;
    padding: 0 24px 80px;
    text-align: center;
}

.video-container {
    background: #000;
    border-radius: 8px;
    aspect-ratio: 16/9;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--primary);
    font-size: 48px;
    font-weight: 600;
    box-shadow: 0 20px 40px rgba(6, 182, 212, 0.15);
    margin-bottom: 40px;
}

.demo-intro {
    margin-top: 80px;
    margin-bottom: 48px;
}

.section-title {
    font-size: 40px;
    font-weight: 800;
    letter-spacing: -1px;
    margin-bottom: 16px;
}

.section-subtitle {
    font-size: 16px;
    color: var(--text-gray);
}

.demo-card {
    background: rgba(255, 255, 255, 0.6);
    border: 1px solid var(--border);
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 24px;
    margin-bottom: 80px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    position: relative;
    overflow: hidden;
}

.play-button-large {
    width: 64px;
    height: 64px;
    background-color: var(--primary);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    margin: 100px auto;
    cursor: pointer;
    box-shadow: 0 10px 20px rgba(6, 182, 212, 0.3);
    transition: transform 0.2s;
}

.play-button-large:hover {
    transform: scale(1.05);
}

.video-placeholder-bottom {
    display: flex;
    align-items: center;
    gap: 8px;
    background: white;
    padding: 12px 16px;
    border-radius: 6px;
    font-size: 13px;
    color: var(--text-gray);
    margin-bottom: 24px;
    border: 1px solid var(--border);
}

.metrics-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    border-top: 1px solid var(--border);
    padding-top: 24px;
}

.metric {
    text-align: center;
    border-right: 1px solid var(--border);
}

.metric:last-child {
    border-right: none;
}

.metric h3 {
    font-size: 24px;
    font-weight: 800;
    color: var(--primary);
    margin-bottom: 4px;
}

.metric p {
    font-size: 13px;
    color: var(--text-gray);
}

.steps-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    max-width: 800px;
    margin: 0 auto 120px;
}

.step {
    text-align: center;
}

.step-number {
    width: 48px;
    height: 48px;
    background: rgba(6, 182, 212, 0.1);
    color: var(--primary);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    font-weight: 700;
    margin: 0 auto 16px;
    border: 2px solid var(--primary);
}

.step h4 {
    font-size: 16px;
    font-weight: 700;
    margin-bottom: 8px;
}

.step p {
    font-size: 14px;
    color: var(--text-gray);
    line-height: 1.5;
}

.features-section {
    max-width: 1200px;
    margin: 0 auto;
    padding: 80px 24px;
    text-align: center;
}

.features-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    margin-top: 48px;
}

.feature-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 32px;
    text-align: left;
    transition: box-shadow 0.2s, transform 0.2s;
    box-shadow: 0 4px 6px rgba(0,0,0,0.02);
}

.feature-card:hover {
    box-shadow: 0 10px 25px rgba(0,0,0,0.05);
    transform: translateY(-2px);
}

.feature-icon {
    width: 48px;
    height: 48px;
    background: rgba(6, 182, 212, 0.1);
    color: var(--primary);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 24px;
}

.feature-card h3 {
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 12px;
}

.feature-card p {
    font-size: 14px;
    color: var(--text-gray);
    line-height: 1.6;
}

.emergent-badge {
    display: inline-flex !important;
    box-sizing: border-box;
    width: 178px;
    height: 40px;
    padding: 8px 12px;
    align-items: center !important;
    gap: 8px;
    border-radius: 50px !important;
    background: #000 !important;
    position: fixed !important;
    bottom: 16px;
    right: 16px;
    text-decoration: none;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    font-size: 12px !important;
    z-index: 9999 !important;
}

.emergent-badge span {
    color: #FFF !important;
    font-weight: 600 !important;
    line-height: 20px !important;
    white-space: nowrap !important;
}
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css_content)

print("Files written successfully")
