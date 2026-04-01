document.addEventListener('DOMContentLoaded', function() {
    // 1. Create Modal HTML
    const modalHTML = `
    <div class="reserve-modal-overlay" id="reserveModal">
        <div class="reserve-modal-content">
            <button class="close-reserve-modal" id="closeReserve">&times;</button>
            
            <div class="prereg-header">
                <span class="prereg-badge">RESERVA AHORA</span>
                <h2>Sé de los primeros en experimentar el futuro</h2>
                <p>Los primeros 1000 usuarios recibirán un paquete de accesorios premium y 3 años de garantía extendida</p>
            </div>

            <div class="prereg-container">
                <!-- Left: Form -->
                <div class="prereg-form-card">
                    <form class="main-prereg-form">
                        <div class="form-group-custom">
                            <label>Nombre completo *</label>
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
                                <input type="text" placeholder="Dime tu país">
                            </div>
                        </div>

                        <button type="button" class="btn-cyan-full">Reservar mi NEXUS SEAMLESS</button>
                        <p class="form-card-footer">No se requiere pago inicial. Te contactaremos para finalizar tu reserva.</p>
                    </form>
                </div>

                <!-- Right: Benefits -->
                <div class="prereg-benefits-col">
                    <h3 class="b-title">Beneficios del pre-registro</h3>
                    
                    <div class="benefit-item-card">
                        <div class="b-icon-wrap">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        </div>
                        <div class="b-info">
                            <h4>Acceso prioritario</h4>
                            <p>Sé de los primeros en recibir tu NEXUS SEAMLESS</p>
                        </div>
                    </div>

                    <div class="benefit-item-card">
                        <div class="b-icon-wrap">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        </div>
                        <div class="b-info">
                            <h4>Accesorios premium</h4>
                            <p>Incluye teclado magnético, estuche de titanio y stylus de grafeno</p>
                        </div>
                    </div>

                    <div class="benefit-item-card">
                        <div class="b-icon-wrap">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        </div>
                        <div class="b-info">
                            <h4>Garantía extendida</h4>
                            <p>3 años de cobertura completa sin coste adicional</p>
                        </div>
                    </div>

                    <div class="benefit-item-card">
                        <div class="b-icon-wrap">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        </div>
                        <div class="b-info">
                            <h4>Soporte exclusivo</h4>
                            <p>Línea directa con el equipo de ingeniería 24/7</p>
                        </div>
                    </div>

                    <div class="benefit-item-card" style="margin-bottom: 0;">
                        <div class="b-icon-wrap">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        </div>
                        <div class="b-info">
                            <h4>Actualizaciones prioritarias</h4>
                            <p>Acceso anticipado a nuevas características y mejoras</p>
                        </div>
                    </div>

                    <!-- Progress Bar -->
                    <div class="units-card">
                        <div class="u-header">
                            <span>Unidades disponibles</span>
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
        </div>
    </div>
    `;

    // 2. Inject Modal
    document.body.insertAdjacentHTML('beforeend', modalHTML);

    const modal = document.getElementById('reserveModal');
    const closeBtn = document.getElementById('closeReserve');

    function getSuccessHTML() {
        return `
            <div id="reserveSuccessMessage" style="text-align: center; padding: 60px 20px;">
                <div style="width: 80px; height: 80px; background: #ecfeff; color: #0891b2; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px; border: 2px solid #22d3ee;">
                    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                </div>
                <h2 style="font-size: 32px; font-weight: 800; color: #1e293b; margin-bottom: 16px;">¡Reserva completada!</h2>
                <p style="font-size: 18px; color: #64748b; margin-bottom: 32px; max-width: 500px; margin-left: auto; margin-right: auto;">
                    El equipo de NEXUS ha recibido tu solicitud correctamente. Pronto recibirás noticias nuestras en tu correo electrónico para finalizar los detalles.
                </p>
                <button class="btn-cyan-full" id="closeSuccessBtn" style="max-width: 200px;">Cerrar</button>
            </div>
        `;
    }

    // 3. Global Handler for forms
    function setupFormSubmissions() {
        const forms = document.querySelectorAll('.main-prereg-form');
        forms.forEach(form => {
            const submitBtn = form.querySelector('.btn-cyan-full');
            if (!submitBtn) return;
            
            submitBtn.addEventListener('click', function(e) {
                e.preventDefault();
                const container = form.closest('.prereg-container');
                const header = container.previousElementSibling; 
                
                if (header && header.classList.contains('prereg-header')) {
                    header.style.display = 'none';
                }
                
                container.innerHTML = getSuccessHTML();
                container.style.display = 'block';
                
                // Ensure the message is visible
                container.scrollIntoView({ behavior: 'smooth', block: 'center' });
                
                // Add event listener to the new close button
                const closeBtn = document.getElementById('closeSuccessBtn');
                if (closeBtn) {
                    closeBtn.addEventListener('click', function() {
                        const modal = document.getElementById('reserveModal');
                        if (modal && modal.classList.contains('active')) {
                            closeModal();
                        } else {
                            // If it's the in-page form, replace with a 'Thanks' small badge
                            container.innerHTML = '<div style="text-align:center; padding: 40px; color: #0891b2; font-weight: 700;">Gracias por tu reserva. Pronto contactaremos contigo.</div>';
                        }
                    });
                }
            });
        });
    }

    // 4. Find and setup all trigger buttons
    function setupTriggerButtons() {
        const buttons = document.querySelectorAll('a, button');
        buttons.forEach(btn => {
            const text = btn.innerText.toLowerCase();
            const href = btn.getAttribute('href');
            
            // Check if it's a trigger for the MODAL (not the submit button of a form)
            const isTrigger = text.includes('reservar ahora') || (href && href.includes('preregister')) || text.includes('reserva ya tu nexus');
            const isInForm = btn.closest('.main-prereg-form');
            
            if (isTrigger && !isInForm) {
                btn.addEventListener('click', function(e) {
                    // Only open modal if we are NOT on index.html (where we just want to scroll)
                    // Wait, the user wants the modal even on index.html? 
                    // Actually, if they are already on index, scrolling is nicer, but the user says "este mensaje debe aparecer tambien".
                    // If they scroll, they see the form, then they submit and get the message.
                    // If they are on another page, they get the modal, submit and get the message.
                    
                    if (window.location.pathname.includes('index.html') || window.location.pathname === '/') {
                        // Let it scroll normally to #preregister
                    } else {
                        e.preventDefault();
                        openModal();
                    }
                });
            }
        });
    }

    function openModal() {
        modal.classList.add('active');
        document.body.style.overflow = 'hidden'; 
    }

    function closeModal() {
        modal.classList.remove('active');
        document.body.style.overflow = '';
    }

    closeBtn.addEventListener('click', closeModal);
    modal.addEventListener('click', function(e) {
        if (e.target === modal) closeModal();
    });
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.classList.contains('active')) closeModal();
    });

    function setupNewsletterForms() {
        // Handle all buttons with 'Suscribirme'
        const buttons = document.querySelectorAll('button');
        buttons.forEach(btn => {
            if (btn.innerText.toLowerCase().includes('suscribirme')) {
                btn.addEventListener('click', function(e) {
                    // Only handle if it looks like a newsletter group (not part of the main prereg form)
                    const isNewsletter = btn.closest('.newsletter-card-new') || btn.closest('.side-newsletter');
                    
                    if (isNewsletter) {
                        e.preventDefault();
                        const input = isNewsletter.querySelector('input[type="email"]');
                        if (input && !input.value.trim().includes('@')) {
                            alert('Por favor, introduce un email válido.');
                            return;
                        }
                        
                        const successHTML = `
                            <div style="text-align: center; padding: 20px; animation: fadeIn 0.5s ease;">
                                <div style="font-size: 32px; margin-bottom: 12px;">✅</div>
                                <h3 style="font-size: 20px; font-weight: 700; color: #0f172a; margin-bottom: 8px;">¡Gracias por suscribirte!</h3>
                                <p style="font-size: 14px; color: #64748b;">Pronto recibirás la magia de NEXUS SEAMLESS en tu bandeja de entrada.</p>
                            </div>
                        `;
                        
                        // Select the container to replace
                        const container = isNewsletter.querySelector('.newsletter-input-group-new') || isNewsletter.querySelector('form');
                        if (container) {
                            container.innerHTML = successHTML;
                            // For index.html card, we might want to hide subtitle etc.
                            const desc = isNewsletter.querySelector('.news-desc') || isNewsletter.querySelector('p');
                            if (desc) desc.style.opacity = '0.5';
                        }
                    }
                });
            }
        });
    }

    setupFormSubmissions();
    setupTriggerButtons();
    setupNewsletterForms();
});
