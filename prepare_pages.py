"""Create and validate the GitHub Pages artifact without changing local preview files."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
import re
import shutil
import hashlib

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'dist'
DEST = ROOT / '_site'
PREFIX = '/QuadMannGaming'
shutil.copytree(SOURCE, DEST, dirs_exist_ok=True)

for page in DEST.rglob('*.html'):
    content = page.read_text(encoding='utf-8')
    content = re.sub(r'((?:href|src)=["\'])/(?!/)', lambda m: m[1] + PREFIX + '/', content)
    for asset in ('styles.css', 'app.js'):
        version = hashlib.sha256((SOURCE / asset).read_bytes()).hexdigest()[:12]
        content = content.replace(f'/{asset}"', f'/{asset}?v={version}"')
    page.write_text(content, encoding='utf-8')

script = DEST / 'app.js'
script.write_text(script.read_text(encoding='utf-8').replace("fetch('/gallery.json')", "fetch('/QuadMannGaming/gallery.json')"), encoding='utf-8')
gallery_path = DEST / 'gallery.json'
gallery = json.loads(gallery_path.read_text(encoding='utf-8'))
for photo in gallery:
    photo['src'] = PREFIX + photo['src']
gallery_path.write_text(json.dumps(gallery), encoding='utf-8')
(DEST / '.nojekyll').touch()

def check_url(url):
    if not url.startswith('/') or url.startswith('//'):
        return
    assert url.startswith(PREFIX + '/'), f'Unprefixed local URL: {url}'
    target = DEST / unquote(urlsplit(url).path[len(PREFIX):]).lstrip('/')
    if target.is_dir():
        target /= 'index.html'
    assert target.is_file(), f'Missing resource: {url}'

class Links(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('href', 'src') and value:
                check_url(value)

for page in DEST.rglob('*.html'):
    Links().feed(page.read_text(encoding='utf-8'))
for photo in gallery:
    check_url(photo['src'])
assert "fetch('/gallery.json')" not in script.read_text(encoding='utf-8')
assert len(list(DEST.rglob('*.html'))) == 7
print('GitHub Pages artifact ready: all seven pages, links, assets, and gallery paths checked.')
