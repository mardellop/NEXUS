import os

css_appends_7 = """

/* Override Newsletter */
.newsletter-card-new {
    background: white;
    border: 1px solid rgba(6, 182, 212, 0.4);
    border-radius: 24px;
    padding: 64px;
    text-align: center;
    box-shadow: 0 20px 40px -10px rgba(6, 182, 212, 0.15);
    position: relative;
    overflow: hidden;
    z-index: 1;
}

.newsletter-card-new::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(circle at top center, rgba(6, 182, 212, 0.05) 0%, transparent 60%);
    z-index: -1;
    pointer-events: none;
}

.newsletter-icon-new {
    width: 56px;
    height: 56px;
    background: rgba(6, 182, 212, 0.1);
    color: var(--primary);
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 24px;
    border: 1px solid rgba(6, 182, 212, 0.3);
}

.newsletter-card-new h2 {
    font-size: 32px;
    font-weight: 800;
    color: var(--text-dark);
    margin-bottom: 12px;
}

.news-desc {
    font-size: 16px;
    color: var(--text-gray);
    margin-bottom: 32px;
    line-height: 1.6;
}

.newsletter-input-group-new {
    display: flex;
    justify-content: center;
    gap: 12px;
    max-width: 480px;
    margin: 0 auto 24px;
}

.newsletter-input-group-new input {
    flex: 1;
    padding: 14px 20px;
    border: 1px solid var(--border);
    border-radius: 8px;
    font-size: 14px;
    outline: none;
    transition: all 0.2s;
    background: #fdfdfd;
}

.newsletter-input-group-new input:focus {
    border-color: var(--primary);
    box-shadow: 0 0 0 3px rgba(6, 182, 212, 0.1);
    background: white;
}

.news-disclaimer {
    font-size: 11px;
    color: var(--text-light);
    margin-bottom: 48px;
    line-height: 1.5;
}

.news-metrics {
    display: flex;
    justify-content: center;
    gap: 64px;
    max-width: 80%;
    margin: 0 auto;
}

.n-metric h4 {
    font-size: 24px;
    font-weight: 800;
    color: var(--primary);
    margin-bottom: 4px;
}

.n-metric span {
    font-size: 12px;
    color: var(--text-gray);
    font-weight: 500;
}

@media (max-width: 600px) {
    .newsletter-card-new {
        padding: 40px 24px;
    }
    .newsletter-input-group-new {
        flex-direction: column;
    }
    .news-metrics {
        flex-direction: column;
        gap: 32px;
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_appends_7)

print("Newsletter Styling Injected")
