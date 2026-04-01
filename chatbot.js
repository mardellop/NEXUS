document.addEventListener('DOMContentLoaded', function() {
    const chatbotHTML = `
    <div class="chatbot-container">
        <button class="chatbot-button" id="toggleChatBtn">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
        </button>
        
        <div class="chatbot-window" id="chatWindow">
            <div class="chatbot-header">
                <div class="header-info">
                    <div class="logo-mini">N</div>
                    <div>
                        <div style="font-weight: 700; font-size: 14px;">Nexusbot</div>
                        <div style="font-size: 11px; opacity: 0.8;">En línea</div>
                    </div>
                </div>
                <button class="close-chat" id="closeChatBtn">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                </button>
            </div>
            <div class="chatbot-messages" id="chatMessages">
                <div class="message bot">
                    Hola, soy el asistente virtual de NEXUS SEAMLESS. Estoy aquí para resolver todas tus dudas sobre el Nexus Seamless Gen 1. ¿En qué puedo ayudarte?
                </div>
            </div>
            <div id="typing" class="typing-indicator" style="padding-left: 20px;">Nexusbot está pensando...</div>
            <div class="chatbot-input-area">
                <input type="text" id="chatInput" placeholder="Escribe tu pregunta...">
                <button class="chatbot-send-btn" id="sendChatBtn">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                </button>
            </div>
        </div>

        <style>
            .rating-stars {
                display: flex;
                gap: 8px;
                margin-top: 10px;
                justify-content: center;
                background: rgba(255,255,255,0.1);
                padding: 10px;
                border-radius: 12px;
            }
            .star {
                font-size: 28px;
                cursor: pointer;
                color: #e5e7eb;
                transition: all 0.2s ease;
                filter: drop-shadow(0 0 2px rgba(0,0,0,0.1));
            }
            .star:hover {
                transform: scale(1.2);
                color: #3cb3d3;
            }
            .star.active {
                color: #3cb3d3;
                filter: drop-shadow(0 0 8px rgba(60, 179, 211, 0.4));
            }
            .rating-confirmed {
                font-size: 11px;
                color: #3cb3d3;
                text-align: center;
                margin-top: 5px;
                font-weight: 600;
                display: none;
            }
        </style>
    </div>
    `;

    document.body.insertAdjacentHTML('beforeend', chatbotHTML);

    const NEXUS_KNOWLEDGE = [
        {
            keys: ["precio", "comprar", "disponibilidad", "reserva", "cuanto cuesta", "valor", "tarifas", "coste", "importe", "presupuesto", "inversión", "cuantía", "precio final", "precio exacto", "qué vale", "cuál es el precio", "a cuánto sale", "por cuánto sale", "qué cuesta", "desglose", "precio con iva", "pvp", "precio oficial", "listado de precios", "precio de mercado", "precio por unidad", "adquirir", "pedir", "encargar", "contratar", "pago", "abonar", "factura", "carrito", "checkout", "finalizar compra", "suscribirse", "alta", "registro", "conseguir", "obtener", "acceso", "licencia", "paquete", "plan", "oferta comercial", "preventa", "early bird", "lanzamiento", "promoción inicial", "precio especial", "reserva anticipada", "descuento lanzamiento", "unidades limitadas", "stock", "fecha de entrega", "lista de espera", "acceso prioritario", "fundadores", "primera edición", "exclusivo", "cupos", "pre-pedido", "inscripción", "plazo de entrega", "disponibilidad inmediata", "barato", "económico", "rebajado", "en oferta", "chollo", "ganga", "mejor precio", "calidad-precio", "comparar precios", "descuento", "rebajas", "outlet", "low cost", "asequible", "competitivo", "precio mínimo", "ajustado", "rentabilidad", "ahorro", "beneficio", "cuotas", "financiación", "pago a plazos", "sin intereses", "mensualidad", "suscripción", "pago único", "garantía", "prueba gratuita", "demo", "reembolso", "métodos de pago", "bizum", "tarjeta", "paypal", "transferencia", "envío gratis", "gastos de envío", "mantenimiento", "soporte"],
            ans: "¡Estamos en plena fase de lanzamiento! Puedes reservar una de las 1000 unidades de Nexus Seamless Gen 1 directamente aquí en la web. Las primeras entregas empezarán en junio de 2026."
        },
        {
            keys: ["pantalla", "como funciona", "desenrollar", "grafeno", "tecnología", "resolución", "8k", "flexible", "resistente", "lámina", "características", "especificaciones", "cómo se usa", "funcionamiento", "material", "durabilidad", "plegable", "enrollable", "calidad de imagen", "píxeles", "nitidez", "brillo", "panel", "display", "innovación", "hardware", "componentes", "resistencia a golpes", "impermeable", "ligero", "fino", "delgado", "portátil", "multitarea", "rendimiento", "potencia", "velocidad de refresco", "hercios", "colores", "hdr", "oled", "tecnología punta", "futurista", "vanguardia", "diseño", "ergonomía", "tacto", "sensibilidad", "táctil", "precisión", "latencia", "conectividad", "batería", "autonomía", "carga rápida", "procesador", "chip", "gráficos", "gpu", "experiencia de usuario", "interfaz", "sistema", "software", "compatibilidad", "dispositivo", "gadget", "wearable", "tamaño", "pulgadas", "dimensiones", "peso", "grosor", "transparente", "curvo", "ángulo de visión", "reflejos", "protección ocular", "luz azul", "novedad", "patente", "fabricación", "proceso", "calidad", "premium", "lujo", "profesional", "trabajo", "productividad", "ocio", "gaming", "streaming", "cine", "fotografía", "edición", "diseño gráfico", "arquitectura", "ingeniería", "médico", "militar", "seguridad", "garantía técnica", "soporte", "manual", "guía"],
            ans: "Nexus Seamless es un dispositivo que cuenta con una lámina de grafeno increíblemente resistente y flexible. Es perfecta para trabajar con resolución 8K."
        },
        {
            keys: ["especificaciones tecnicas", "procesador", "npu", "memoria", "ram", "almacenamiento", "2nm", "arquitectura", "flujo cuántico", "64gb", "4tb", "potencia", "rendimiento", "peso", "450 gramos", "cilindro", "hardware", "cpu", "gpu", "nanómetros", "velocidad", "teraflops", "capacidad", "disco duro", "ssd", "nvme", "memoria unificada", "ancho de banda", "transferencia de datos", "procesamiento", "inteligencia artificial", "ia", "aprendizaje automático", "machine learning", "núcleos", "cores", "frecuencia", "ghz", "overclocking", "refrigeración", "disipación", "térmico", "silencioso", "eficiencia energética", "consumo", "vatios", "batería interna", "autonomía", "arquitectura de red", "chips", "semiconductores", "tecnología 2 nanómetros", "rendimiento extremo", "multitarea real", "latencia cero", "renderizado", "edición de video", "procesado de datos", "compilación", "servidor portátil", "estación de trabajo", "workstation", "compacto", "ligero", "portabilidad", "diseño cilíndrico", "aleación", "fibra de carbono", "durabilidad", "resistencia", "conexiones", "puertos", "thunderbolt", "usb-c", "wifi 7", "bluetooth 5.4", "conectividad", "velocidad de lectura", "velocidad de escritura", "caché", "bus de datos", "optimización", "ecosistema", "seguridad", "encriptación por hardware", "biometría", "reconocimiento", "sensores", "giroscopio", "acelerómetro", "innovación técnica", "vanguardia", "futuro", "gama alta", "tope de gama", "premium", "profesional", "especificaciones completas", "ficha técnica", "comparativa hardware", "benchmark"],
            ans: "Lleva una NPU de 2nm con arquitectura de flujo cuántico, 64GB de memoria y hasta 4TB de almacenamiento. Es potencia pura encerrada en un cilindro que solo pesa 450 gramos."
        },
        {
            keys: ["puertos", "usb", "conectores", "hdmi"],
            ans: "No tiene puertos físicos. Es un diseño 'Zero-Port'. Todo el intercambio de datos y energía ocurre de forma magnética e inalámbrica a través de su superficie, eliminando cualquier estorbo mecánico."
        },
{
    keys: ["que es nexus", "nexus seamless", "qué es nexus", "definición", "concepto", "ordenador cilindro", "futuro informática", "revolución tecnológica", "pc sin pantalla", "ordenador enrollable", "tecnología gecko", "imán", "magnético", "adherible", "pegar en pared", "sin puertos", "inalámbrico total", "lámina de grafeno", "micras", "espesor", "ultrafino", "portabilidad extrema", "ergonomía", "trabajar de pie", "trabajar tumbado", "flexibilidad", "espacio de trabajo", "oficina nómada", "minimalismo", "diseño funcional", "titanio", "cilindro", "desplegable", "pantalla flexible", "sin marcos", "sin cables", "innovación española", "gadget del año", "nuevo paradigma", "sustituto portátil", "tablet flexible", "monitor enrollable", "tecnología de adhesión", "sujeción magnética", "sin taladros", "superficies", "cristal", "madera", "metal", "versatilidad", "productividad", "comodidad", "salud postural", "espalda", "cuello", "visión", "adaptable", "entorno", "inteligente", "invisible", "seamless", "sin costuras", "integración", "hogar inteligente", "domótica", "decoración", "estética", "limpieza visual", "vanguardia", "exclusivo", "lanzamiento 2026", "tecnología punta", "hardware oculto", "npu", "potencia compacta", "ligero", "fácil de llevar", "mochila", "viajes", "presentaciones", "reuniones", "colaborativo", "pantalla gigante", "cine en cualquier parte", "estudio creativo", "diseñadores", "arquitectos", "programadores", "escritura", "lectura", "interfaz táctil", "gestos", "voz", "futurista", "ciencia ficción", "realidad", "dispositivo único", "patente", "ingeniería", "lujo tecnológico", "experiencia nexus"],
    ans: "NEXUS SEAMLESS es el primer ordenador del mundo contenido en un cilindro de titanio que despliega una pantalla de grafeno de micras de espesor. Gracias a su sistema magnético con tecnología gecko, puedes adherirlo a cualquier pared y trabajar como quieras: de pie, sentado o tumbado, sin cables ni puertos físicos."
},
        {
            keys: ["materiales", "titanio", "resistente", "duracion", "golpes", "carbono", "aeroespacial", "nanotubos", "ligero", "acero", "décadas", "calidad", "irrompible", "blindado", "fibra de carbono", "titanio grado 5", "resistencia extrema", "anti-arañazos", "anti-golpes", "protección", "robusto", "sólido", "fiable", "eterno", "larga vida", "sin obsolescencia", "sostenible", "ecológico", "reciclable", "premium", "lujo", "acabado", "textura", "tacto", "minimalista", "industrial", "ingeniería", "fabricación", "proceso", "ensamblado", "calidad percibida", "estándar militar", "certificación", "ip68", "sumergible", "hermético", "polvo", "agua", "humedad", "temperatura", "clima", "corrosión", "oxidación", "desgaste", "uso diario", "todoterreno", "aventura", "viaje", "nómada digital", "portabilidad", "peso pluma", "densidad", "dureza", "flexibilidad", "maleabilidad", "vanguardia", "tecnología de materiales", "innovación", "exclusividad", "diseño suizo", "artesanía", "precisión", "ajuste", "estructura", "chasis", "esqueleto", "carcasa", "funda", "protector", "seguridad", "confianza", "inversión", "valor", "reventa", "herencia", "clásico", "atemporal", "estética", "elegancia", "fuerza", "potencia visual", "impacto", "caídas", "accidentes", "reparabilidad", "mantenimiento", "limpieza", "pulido", "mate", "brillo", "color", "personalización"],
            ans: "Usamos titanio aeroespacial y nanotubos de carbono. Es tan ligero como el papel pero más fuerte que el acero. Está pensado para durar décadas, no para caducar a los dos años."
        },
    ];

    window.toggleChat = function() {
        const win = document.getElementById('chatWindow');
        win.style.display = (win.style.display === 'flex') ? 'none' : 'flex';
    };

    const toggleBtn = document.getElementById('toggleChatBtn');
    const closeBtn = document.getElementById('closeChatBtn');
    const sendBtn = document.getElementById('sendChatBtn');
    const chatInput = document.getElementById('chatInput');

    toggleBtn.addEventListener('click', toggleChat);
    closeBtn.addEventListener('click', toggleChat);

    chatInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') sendMessage();
    });

    sendBtn.addEventListener('click', sendMessage);

    function sendMessage() {
        const input = document.getElementById('chatInput');
        const msg = input.value.trim();
        if (!msg) return;

        addMessage(msg, 'user');
        input.value = '';

        const typing = document.getElementById('typing');
        typing.style.display = 'block';

        setTimeout(() => {
            const botMsg = getBotResponse(msg);
            typing.style.display = 'none';

            if (typeof botMsg === 'object' && botMsg.isGoodbye) {
                // First: Goodbye message
                addMessage(botMsg.ans, 'bot');
                
                // Second: Experience survey after a short delay
                setTimeout(() => {
                    const surveyHTML = `
                        <div>¿Cómo te resultó la experiencia?</div>
                        <div class="rating-stars" id="ratingContainer">
                            <span class="star" onclick="rateExperience(1)">★</span>
                            <span class="star" onclick="rateExperience(2)">★</span>
                            <span class="star" onclick="rateExperience(3)">★</span>
                            <span class="star" onclick="rateExperience(4)">★</span>
                            <span class="star" onclick="rateExperience(5)">★</span>
                        </div>
                        <div id="ratingConfirmed" class="rating-confirmed">¡Gracias por tu valoración!</div>
                    `;
                    addMessage(surveyHTML, 'bot', true);

                    // AUTO-FINALIZE TIMER: 10 seconds grace period
                    window.finalizeTimer = setTimeout(() => {
                        finalizeSession();
                    }, 10000);

                }, 800);
            } else {
                addMessage(botMsg, 'bot');
            }
        }, 1000);
    }

    window.rateExperience = function(val) {
        // Clear the auto-finalize timer as the user interacted
        if (window.finalizeTimer) clearTimeout(window.finalizeTimer);

        const stars = document.querySelectorAll('.star');
        stars.forEach((s, idx) => {
            s.classList.toggle('active', idx < val);
        });
        document.getElementById('ratingConfirmed').style.display = 'block';
        
        const container = document.getElementById('ratingContainer');
        if (container) container.style.pointerEvents = 'none';
        
        setTimeout(() => {
            finalizeSession();
        }, 1000);
        
        console.log("User rating recorded:", val);
    };

    function finalizeSession() {
        const input = document.getElementById('chatInput');
        if (!input || input.disabled) return; // Already finalized

        addMessage("Conversación finalizada. ¡Hasta pronto!", "bot");
        
        const sendBtn = document.getElementById('sendChatBtn');
        input.disabled = true;
        input.placeholder = "Sesión finalizada";
        input.parentElement.style.opacity = "0.5";
        input.parentElement.style.pointerEvents = "none";
        if (sendBtn) sendBtn.style.display = 'none';
    }

    function addMessage(content, side, isHTML = false) {
        const container = document.getElementById('chatMessages');
        const div = document.createElement('div');
        div.className = `message ${side}`;
        if (isHTML) {
            div.innerHTML = content;
        } else {
            div.innerText = content;
        }
        container.appendChild(div);
        container.scrollTop = container.scrollHeight;
    }

    function levenshteinDistance(a, b) {
        if (a.length === 0) return b.length;
        if (b.length === 0) return a.length;
        const matrix = [];
        for (let i = 0; i <= b.length; i++) matrix[i] = [i];
        for (let j = 0; j <= a.length; j++) matrix[0][j] = j;
        for (let i = 1; i <= b.length; i++) {
            for (let j = 1; j <= a.length; j++) {
                if (b.charAt(i - 1) === a.charAt(j - 1)) {
                    matrix[i][j] = matrix[i - 1][j - 1];
                } else {
                    matrix[i][j] = Math.min(matrix[i - 1][j - 1] + 1, Math.min(matrix[i][j - 1] + 1, matrix[i - 1][j] + 1));
                }
            }
        }
        return matrix[b.length][a.length];
    }

    function isSimilar(word, key) {
        if (word.includes(key) || key.includes(word)) return true;
        const dist = levenshteinDistance(word, key);
        // Allow 1 typo for words of 4-6 chars, 2 typos for longer words
        if (key.length <= 3) return dist === 0;
        if (key.length <= 6) return dist <= 1;
        return dist <= 2;
    }

    function getBotResponse(input) {
        input = input.toLowerCase().replace(/[?¿!¡,. ]+/g, ' ');
        const inputWords = input.split(' ').filter(w => w.length > 2);
        
        const greetings = ["hola", "buenos dias", "buenas tardes", "buenas noches", "hey", "saludos"];
        if (greetings.some(g => input.includes(g) || inputWords.some(w => isSimilar(w, g)))) {
            const hour = new Date().getHours();
            let welcome = "¡Hola!";
            if (hour >= 6 && hour < 13) welcome = "¡Buenos días!";
            else if (hour >= 13 && hour < 20) welcome = "¡Buenas tardes!";
            else welcome = "¡Buenas noches!";
            
            return welcome + " Cuentame, ¿Qué te gustaría saber?";
        }

        const farewells = ["gracias", "adios", "chao", "hasta luego", "luego", "bye", "gracias por todo", "muchas gracias"];
        if (farewells.some(f => input.includes(f) || inputWords.some(w => isSimilar(w, f)))) {
            return {
                ans: "Gracias por contactar con nosotros. Si tienes cualquier duda o sugerencia, no dudes en ponerte en contacto con nosotros a través de nuestro email.",
                isGoodbye: true
            };
        }

        let bestItem = null;
        let maxScore = 0;

        for (const item of NEXUS_KNOWLEDGE) {
            let currentScore = 0;
            for (const key of item.keys) {
                if (input.includes(key)) {
                    currentScore += key.length * 2; // Direct matches are more important
                } else {
                    // Check word by word for fuzzy matches
                    for (const word of inputWords) {
                        if (isSimilar(word, key)) {
                            currentScore += key.length;
                            break;
                        }
                    }
                }
            }
            if (currentScore > maxScore) {
                maxScore = currentScore;
                bestItem = item;
            }
        }

        if (bestItem && maxScore > 0) {
            return bestItem.ans;
        }

        return "Aún no tengo esa información detallada, pero no te preocupes. Puedes ponerte en contacto con nosotros directamente a través de contacto.nexuss.brand@gmail.com y nuestro equipo te responderá encantado.";
    }

    // Handle footer special links
    const footerLinks = document.querySelectorAll('a');
    footerLinks.forEach(link => {
        const text = link.innerText.toLowerCase();
        
        if (text.includes('nexusbot')) {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const win = document.getElementById('chatWindow');
                if (win.style.display !== 'flex') toggleChat();
                win.scrollIntoView({ behavior: 'smooth', block: 'end' });
            });
        }
        
        if (text.includes('contacte con nosotros')) {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                // Create a temporary hidden link and click it - more reliable on some systems
                const tempLink = document.createElement('a');
                tempLink.href = 'mailto:contacto.nexuss.brand@gmail.com?subject=Consulta NEXUS SEAMLESS';
                tempLink.style.display = 'none';
                document.body.appendChild(tempLink);
                tempLink.click();
                document.body.removeChild(tempLink);
                
                // Fallback attempt
                setTimeout(() => {
                    window.location.href = "mailto:contacto.nexuss.brand@gmail.com?subject=Consulta NEXUS SEAMLESS";
                }, 100);
            });
        }
    });
});
