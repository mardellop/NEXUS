import os
import re
import shutil

# directory
d = "c:/Users/familia/.gemini/antigravity/playground/celestial-sunspot"

html_files = [f for f in os.listdir(d) if f.endswith(".html")]

# 1. extract testimonials section from index.html
with open(os.path.join(d, "index.html"), "r", encoding="utf-8") as f:
    idx_content = f.read()

# regex to find testimonials section
testimonials_match = re.search(r'(<section id="testimonials" class="testimonials-section">.*?</section>)', idx_content, flags=re.DOTALL)
if testimonials_match:
    testimonials_html = testimonials_match.group(1)
    # 2. remove testimonials from index.html
    new_idx_content = idx_content.replace(testimonials_html, '<!-- Testimonials section moved to testimonios.html -->')
    
    # 3. Create testimonios.html using faq.html as a template
    with open(os.path.join(d, "faq.html"), "r", encoding="utf-8") as f:
        faq_content = f.read()

    # replace title
    test_content = re.sub(r'<title>.*?</title>', '<title>Testimonios | NEXUS S</title>', faq_content)
    
    # replace main section
    test_content = re.sub(r'<section id="faq".*?</section>', testimonials_html, test_content, flags=re.DOTALL)

    # remove padding from testimonials-section to look like faq
    # test_content = test_content.replace('<section id="testimonials" class="testimonials-section">', '<section id="testimonials" class="testimonials-section" style="padding-top: 60px;">')

    with open(os.path.join(d, "testimonios.html"), "w", encoding="utf-8") as f:
        f.write(test_content)
else:
    new_idx_content = idx_content

# 4. update all links across all html
for fn in html_files + ["testimonios.html"]:
    path = os.path.join(d, fn)
    if not os.path.exists(path):
        continue
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # href="#testimonials" -> href="testimonios.html"
    content = content.replace('href="#testimonials"', 'href="testimonios.html"')
    # href="index.html#testimonials" -> href="testimonios.html"
    content = content.replace('href="index.html#testimonials"', 'href="testimonios.html"')
    
    if fn == "index.html":
        content = new_idx_content
        content = content.replace('href="#testimonials"', 'href="testimonios.html"')
        content = content.replace('href="index.html#testimonials"', 'href="testimonios.html"')
    elif fn == "testimonios.html":
        # in testimonios.html, the self-link should be #
        # wait, let it just be testimonios.html
        pass

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Done generating testimonios.html and updating links")
