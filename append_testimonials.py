import os

css_appends_5 = """

/* Override Testimonials */
.testimonial-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 32px;
    text-align: left;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 4px 6px rgba(0,0,0,0.02);
}

.testimonial-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 24px;
}

.stars {
    display: flex;
    gap: 4px;
}

.quote-icon {
    opacity: 0.5;
}

.quote {
    font-size: 15px;
    color: var(--text-dark);
    line-height: 1.6;
    font-style: italic;
    margin-bottom: 32px;
    flex: 1;
}

.testimonial-divider {
    height: 1px;
    background: rgba(0, 0, 0, 0.05);
    margin-bottom: 24px;
}

.author {
    display: flex;
    align-items: center;
    gap: 16px;
}

.author-avatar.default-cyan {
    background: var(--primary);
}

.author-info h4 {
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 2px;
    color: var(--text-dark);
}

.author-info span {
    font-size: 13px;
    color: var(--text-gray);
    line-height: 1.4;
    display: block;
}

.author-company {
    color: var(--primary);
}

/* Metrics Banner */
.metrics-banner {
    background: linear-gradient(90deg, #cffafe, #a5f3fc);
    border: 1px solid rgba(6, 182, 212, 0.3);
    border-radius: 16px;
    padding: 40px;
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin-top: 64px;
    box-shadow: 0 10px 30px -10px rgba(6, 182, 212, 0.3);
}

.metric-item {
    text-align: center;
}

.metric-item h3 {
    font-size: 40px;
    font-weight: 800;
    color: #083344;
    margin-bottom: 8px;
    line-height: 1;
}

.metric-item p {
    font-size: 14px;
    color: #164e63;
    font-weight: 500;
}

/* Simple Press Logos */
.press-logos-simple {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 48px;
    margin-top: 48px;
    padding-top: 0;
}

.p-label {
    font-size: 14px;
    color: var(--text-light);
    font-weight: 500;
}

.p-logo {
    font-size: 16px;
    font-weight: 700;
    color: var(--text-gray);
    opacity: 0.6;
}

@media (max-width: 900px) {
    .metrics-banner {
        flex-direction: column;
        gap: 32px;
        padding: 32px;
    }
    .press-logos-simple {
        flex-direction: column;
        gap: 24px;
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_appends_5)

print("Testimonial CSS replaced")
