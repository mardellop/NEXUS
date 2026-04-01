import os

# Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

# Replace logo-circle
css = re.sub(
    r'\.logo-circle\s*\{[^}]+\}',
    r'''.logo-circle {
    width: 32px;
    height: 32px;
    background-color: var(--primary);
    border-radius: 8px;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 16px;
}''',
    css
)

# Replace badge
css = re.sub(
    r'\.badge\s*\{[^}]+\}',
    r'''.badge {
    display: inline-flex;
    align-items: center;
    background-color: #cffafe;
    color: #0891b8;
    padding: 6px 16px;
    border-radius: 9999px;
    font-size: 14px;
    font-weight: 500;
    margin-bottom: 24px;
    text-transform: uppercase;
}''',
    css
)

# Replace btn-primary-small
css = re.sub(
    r'\.btn-primary-small\s*\{[^}]+\}',
    r'''.btn-primary-small {
    background-color: var(--primary);
    color: white !important;
    padding: 8px 24px;
    border-radius: 6px;
    font-weight: 600;
    transition: all 0.2s;
    border: none;
    cursor: pointer;
    text-decoration: none;
    display: inline-flex;
    justify-content: center;
    align-items: center;
}''',
    css
)

# Replace btn-primary
css = re.sub(
    r'\.btn-primary\s*\{[^}]+\}',
    r'''.btn-primary {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background-color: var(--primary);
    color: white !important;
    padding: 16px 32px;
    border-radius: 6px;
    font-weight: 700;
    font-size: 18px;
    text-decoration: none;
    box-shadow: 0 10px 15px -3px rgba(6, 182, 212, 0.3), 0 4px 6px -4px rgba(6, 182, 212, 0.3);
    transition: all 0.2s;
    border: none;
    cursor: pointer;
}''',
    css
)

css = re.sub(
    r'\.btn-primary:hover\s*\{[^}]+\}',
    r'''.btn-primary:hover {
    transform: scale(1.05);
}''',
    css
)

# Replace btn-secondary
css = re.sub(
    r'\.btn-secondary\s*\{[^}]+\}',
    r'''.btn-secondary {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background-color: transparent;
    color: var(--primary) !important;
    padding: 16px 32px;
    border-radius: 6px;
    font-weight: 700;
    font-size: 18px;
    border: 2px solid var(--primary);
    text-decoration: none;
    transition: all 0.2s;
    cursor: pointer;
}''',
    css
)
css = re.sub(
    r'\.btn-secondary:hover\s*\{[^}]+\}',
    r'''.btn-secondary:hover {
    background-color: #ecfeff;
}''',
    css
)

# Replace hero-title
css = re.sub(
    r'\.hero-title\s*\{[^}]+\}',
    r'''.hero-title {
    font-size: 96px;
    font-weight: 700;
    line-height: 1;
    letter-spacing: -0.025em;
    margin-bottom: 24px;
}''',
    css
)

# Add media query for hero title later manually 

# Replace hero-subtitle
css = re.sub(
    r'\.hero-subtitle\s*\{[^}]+\}',
    r'''.hero-subtitle {
    font-size: 20px;
    color: var(--text-gray);
    margin-bottom: 40px;
    line-height: 1.6;
}''',
    css
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('style.css', 'a', encoding='utf-8') as f:
    f.write('''
@media (max-width: 768px) {
    .hero-title {
        font-size: 60px;
    }
}
''')

print("CSS classes perfectly tuned.")
