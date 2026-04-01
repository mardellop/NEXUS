import os

css_appends_4 = """

/* Grid Specifications Override */
.specs-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 32px;
}

.spec-card {
    background: white;
    border: 1px solid rgba(6, 182, 212, 0.2);
    border-radius: 12px;
    padding: 32px;
    text-align: left;
    box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    position: relative;
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
}

.spec-card:hover {
    box-shadow: 0 10px 25px rgba(6, 182, 212, 0.1);
    transform: translateY(-2px);
}

.spec-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 24px;
}

.spec-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background-color: var(--primary);
}

.spec-header h3 {
    font-size: 20px;
    font-weight: 700;
    color: var(--text-dark);
}

.spec-header h3.active {
    color: var(--primary);
}

.spec-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(6, 182, 212, 0.2) 20%, rgba(6, 182, 212, 0.2) 80%, transparent);
    margin-bottom: 24px;
}

.spec-list {
    list-style: none;
    flex: 1;
}

.spec-list li {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 16px 0;
    border-bottom: 1px solid rgba(0,0,0,0.03);
    font-size: 14px;
}

.spec-list li:last-child {
    border-bottom: none;
    margin-bottom: 48px;
}

.spec-label {
    color: var(--text-gray);
    font-weight: 500;
}

.spec-value {
    color: var(--text-dark);
    font-weight: 500;
    text-align: right;
    max-width: 60%;
    line-height: 1.4;
}

.spec-bottom-lines {
    position: absolute;
    bottom: 32px;
    left: 32px;
    right: 32px;
}

.spec-line-light {
    height: 2px;
    background: rgba(6, 182, 212, 0.1);
    border-radius: 2px;
    margin-bottom: 12px;
}

.spec-line-brand {
    height: 3px;
    background: var(--primary);
    border-radius: 3px;
    width: 80%; /* Aesthetic choice from image */
}

@media (max-width: 900px) {
    .specs-grid {
        grid-template-columns: 1fr;
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_appends_4)

print("Spec Grid Applied")
