import os

files = [
    "privacidad.html", 
    "cookies.html", 
    "aviso-cookies.html", 
    "terminos.html"
]

search_text = """        .legal-body {
            line-height: 1.8;
            font-size: 17px;
        }"""
        
replace_text = """        .legal-body {
            line-height: 1.8;
            font-size: 17px;
            text-align: justify;
        }"""

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace(search_text, replace_text)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated text justification in legal pages.")
