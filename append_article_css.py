
css_to_append = """
/* Article Page Styles */
.article-page {
    padding-top: 120px;
    padding-bottom: 100px;
    max-width: 800px;
    margin: 0 auto;
    padding-left: 24px;
    padding-right: 24px;
}

.article-header {
    margin-bottom: 48px;
    text-align: left;
}

.article-category {
    color: var(--primary);
    font-weight: 700;
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 16px;
    display: block;
}

.article-title {
    font-size: 48px;
    font-weight: 800;
    line-height: 1.1;
    color: var(--text-dark);
    margin-bottom: 24px;
}

.article-meta {
    display: flex;
    align-items: center;
    gap: 16px;
    color: var(--text-light);
    font-size: 14px;
    margin-bottom: 32px;
}

.article-hero-img {
    width: 100%;
    height: 400px;
    background-color: #0c111d;
    border-radius: 24px;
    margin-bottom: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    position: relative;
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
}

.article-hero-img .hero-word {
    font-size: 80px;
    font-weight: 800;
    color: var(--primary);
    opacity: 0.8;
}

.article-body {
    font-size: 18px;
    line-height: 1.8;
    color: #374151;
}

.article-body p {
    margin-bottom: 24px;
}

.article-body h2 {
    font-size: 28px;
    font-weight: 700;
    color: var(--text-dark);
    margin-top: 48px;
    margin-bottom: 20px;
}

.article-body h3 {
    font-size: 22px;
    font-weight: 700;
    color: var(--text-dark);
    margin-top: 32px;
    margin-bottom: 16px;
}

.article-quote {
    border-left: 4px solid var(--primary);
    padding-left: 24px;
    font-size: 24px;
    font-style: italic;
    color: var(--text-dark);
    margin: 48px 0;
    font-weight: 500;
}

.article-body ul {
    margin-bottom: 24px;
    padding-left: 24px;
}

.article-body li {
    margin-bottom: 12px;
}

.article-footer {
    margin-top: 80px;
    padding-top: 40px;
    border-top: 1px solid var(--border);
    display: flex;
    justify-content: space-between;
    align-items: center;
}

@media (max-width: 768px) {
    .article-title {
        font-size: 32px;
    }
    .article-hero-img {
        height: 250px;
    }
    .article-hero-img .hero-word {
        font-size: 40px;
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_to_append)
