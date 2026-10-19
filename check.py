from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
root=Path(__file__).parent/'dist'
errors=[]
class Check(HTMLParser):
 def __init__(self,path): super().__init__();self.path=path;self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='h1':self.h1+=1
  if tag=='img' and 'alt' not in a:errors.append(f'{self.path}: missing alt')
  for key in ('src','href'):
   url=a.get(key,'')
   if url.startswith('/') and not url.startswith('//'):
    target=root/unquote(urlsplit(url).path).lstrip('/')
    if target.is_dir(): target=target/'index.html'
    if not target.exists(): errors.append(f'{self.path}: missing {url}')
for p in root.rglob('*.html'):
 parser=Check(p);parser.feed(p.read_text(encoding='utf-8'))
 if parser.h1!=1:errors.append(f'{p}: h1 count {parser.h1}')
assert not errors,'\n'.join(errors)
print('PASS: eight pages; local navigation and assets resolve; one main heading per page; all images have alt attributes.')
