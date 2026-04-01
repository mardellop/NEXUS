import os

d = "c:/Users/familia/.gemini/antigravity/playground/celestial-sunspot"

for fn in os.listdir(d):
    if fn.endswith(".html"):
        path = os.path.join(d, fn)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        content = content.replace('href="index.html#team"', 'href="sobre-nosotros.html#team"')
        content = content.replace('href="#team"', 'href="sobre-nosotros.html#team"')

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
print("Updated team links.")
