import os

css_appends_2 = """
/* Complex Footer */
.footer-complex {
    background-color: #0b1120;
    color: #94a3b8;
    padding: 80px 24px 40px;
    font-size: 14px;
}

.footer-container {
    max-width: 1200px;
    margin: 0 auto;
}

.footer-top {
    display: flex;
    justify-content: space-between;
    gap: 64px;
    margin-bottom: 64px;
}

.footer-brand {
    flex: 1;
    max-width: 320px;
}

.logo-text.text-white {
    color: white;
}

.brand-desc {
    margin-top: 24px;
    margin-bottom: 32px;
    line-height: 1.6;
}

.social-links span {
    display: block;
    margin-bottom: 12px;
    font-weight: 600;
    color: white;
}

.social-icons {
    display: flex;
    gap: 12px;
}

.social-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    border-radius: 8px;
    background: rgba(255,255,255,0.05);
    color: #94a3b8;
    border: 1px solid rgba(255,255,255,0.1);
    transition: all 0.2s;
}

.social-icon:hover {
    background: rgba(255,255,255,0.1);
    color: white;
}

.footer-links-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 48px;
    flex: 2;
}

.footer-link-col h4 {
    color: white;
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 24px;
}

.footer-link-col a {
    display: block;
    color: #94a3b8;
    text-decoration: none;
    margin-bottom: 16px;
    transition: color 0.2s;
}

.footer-link-col a:hover {
    color: white;
}

.footer-newsletter-banner {
    background: linear-gradient(90deg, #164e63, #083344);
    border: 1px solid rgba(6, 182, 212, 0.2);
    border-radius: 16px;
    padding: 32px 48px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 48px;
}

.banner-info {
    display: flex;
    align-items: center;
    gap: 20px;
}

.banner-icon {
    width: 48px;
    height: 48px;
    border-radius: 12px;
    background: rgba(6, 182, 212, 0.2);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #06b6d4;
    border: 1px solid rgba(6, 182, 212, 0.3);
}

.banner-info h3 {
    color: white;
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 4px;
}

.banner-info p {
    color: #cbd5e1;
    font-size: 14px;
}

.btn-primary-cyan {
    background-color: #06b6d4;
    color: white;
    padding: 12px 24px;
    border-radius: 8px;
    font-weight: 600;
    font-size: 15px;
    border: none;
    cursor: pointer;
    box-shadow: 0 4px 14px rgba(6, 182, 212, 0.4);
    transition: all 0.2s;
}

.btn-primary-cyan:hover {
    background-color: #0891b8;
    box-shadow: 0 6px 20px rgba(6, 182, 212, 0.5);
    transform: translateY(-2px);
}

.footer-bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 32px;
    border-top: 1px solid rgba(255,255,255,0.05);
}

.bottom-links {
    display: flex;
    gap: 24px;
}

.bottom-links a {
    color: #94a3b8;
    text-decoration: none;
    transition: color 0.2s;
}

.bottom-links a:hover {
    color: white;
}

@media (max-width: 900px) {
    .footer-top {
        flex-direction: column;
        gap: 48px;
    }
    .footer-links-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 32px;
    }
    .footer-newsletter-banner {
        flex-direction: column;
        text-align: center;
        gap: 24px;
        padding: 24px;
    }
    .banner-info {
        flex-direction: column;
    }
    .footer-bottom {
        flex-direction: column;
        gap: 16px;
        text-align: center;
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_appends_2)

print("CSS Footer apended")
