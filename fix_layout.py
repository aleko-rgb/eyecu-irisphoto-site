import re

files = ['pl/index.html', 'en/index.html', 'fr/index.html']

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Move event image OUT of dark-grid and make it independent
    # Replace dark-grid with events-image inside to just be after it
    content = re.sub(
        r'(<div class="dark-grid reveal">.*?</div>\n  </div>\n  <ul class="feat-list reveal">)',
        lambda m: m.group(0).replace(
            '    <figure class="events-image"><img src="/images/event1.webp" loading="lazy" decoding="async" alt="Stanowisko fotograficzne EYE C U na wydarzeniu"></figure>\n  </div>',
            '  </div>\n  <figure class="events-image" style="margin: 2rem 0;"><img src="/images/event1.webp" loading="lazy" decoding="async" alt="Event"></figure>'
        ),
        content,
        flags=re.DOTALL
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed event image layout")
