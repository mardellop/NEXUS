import os
import re

d = "c:/Users/familia/.gemini/antigravity/playground/celestial-sunspot"

for fn in os.listdir(d):
    if fn.endswith(".html"):
        path = os.path.join(d, fn)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # Update both variations that might exist
        content = content.replace('href="index.html#press"', 'href="blog.html"')
        content = content.replace('href="#press"', 'href="blog.html"')

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
print("Updated press links to point to blog.html.")
