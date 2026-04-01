import os
import re

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add the <br> line breaks
html = html.replace('<h4>200x Más Resistente</h4>', '<h4>200x Más<br>Resistente</h4>')
html = html.replace('<h4>∞ Carga Ambiental</h4>', '<h4>∞ Carga<br>Ambiental</h4>')

# Find the start and end of specs-highlights
start_idx = html.find('            <div class="specs-highlights">')
end_idx = html.find('            <div class="specs-grid">')

if start_idx != -1 and end_idx != -1:
    # Includes all the whitespace up to the next div
    highlights_block = html[start_idx:end_idx]
    
    # Remove it from its current position
    html = html[:start_idx] + html[end_idx:]
    
    # Now find the end of the section id="specs"
    # We can just look for the first </section> after the relocated block's new position
    # The new position of specs-grid is start_idx.
    section_end_idx = html.find('</section>', start_idx)
    
    # Insert the block right before </section>
    # Note: we should ensure indentation is nice, but highlights_block already has indentation.
    html = html[:section_end_idx] + highlights_block + html[section_end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

css_appends = """

/* Override specs-highlights */
.specs-highlights {
    display: grid !important;
    grid-template-columns: repeat(4, 1fr) !important;
    gap: 16px !important;
    margin-top: 48px !important;
    margin-bottom: 0 !important;
    padding: 0;
}

.spec-highlight {
    background: white;
    border: 1px solid var(--border);
    padding: 40px 24px;
    border-radius: 20px;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.02);
}

.spec-highlight h4 {
    font-size: 26px;
    font-weight: 800;
    color: var(--primary);
    margin-bottom: 16px;
    line-height: 1.3;
}

.spec-highlight p {
    font-size: 15px;
    color: var(--text-gray);
    margin: 0;
    line-height: 1.5;
}

@media (max-width: 900px) {
    .specs-highlights {
        grid-template-columns: repeat(2, 1fr) !important;
    }
}
@media (max-width: 600px) {
    .specs-highlights {
        grid-template-columns: 1fr !important;
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_appends)

print("Highlights moved and styled")
