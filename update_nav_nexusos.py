import os

target_dir = r"c:\Users\familia\.gemini\antigravity\playground\celestial-sunspot"
# We want to add NexusOS Core to the product dropdown
old_pattern = '<li><a href="demo.html" class="dropdown-item">Demo</a></li>'
new_pattern = '<li><a href="demo.html" class="dropdown-item">Demo</a></li>\n                        <li><a href="nexusos-core.html" class="dropdown-item">NexusOS Core</a></li>'

for filename in os.listdir(target_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(target_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if old_pattern in content:
            new_content = content.replace(old_pattern, new_pattern)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
