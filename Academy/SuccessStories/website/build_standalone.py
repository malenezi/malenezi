# -*- coding: utf-8 -*-
"""Python port of build-standalone.ps1 (device_bash cannot run PowerShell).
Builds sdaia-success-stories-standalone.html — one self-contained file with CSS, JS,
icons and every local image inlined. Keeps every assert the PowerShell script had."""
import base64, os, re, sys, urllib.parse

SITE    = os.path.dirname(os.path.abspath(__file__))
ACADEMY = os.path.abspath(os.path.join(SITE, '..', '..'))
MIME = {'.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg',
        '.webp':'image/webp','.svg':'image/svg+xml','.gif':'image/gif'}

def read(*p): return open(os.path.join(*p), encoding='utf-8').read()
def data_uri(path):
    mime = MIME.get(os.path.splitext(path)[1].lower())
    if not mime: return None
    with open(path,'rb') as f:
        return 'data:%s;base64,%s' % (mime, base64.b64encode(f.read()).decode('ascii'))

html   = read(SITE, 'index.html')
ui_css = read(ACADEMY, 'assets', 'sdaia-ui.css')
st_css = read(SITE, 'css', 'style.css')
icons  = read(ACADEMY, 'assets', 'sdaia-icons.js')
ui_js  = read(ACADEMY, 'assets', 'sdaia-ui.js')
data   = read(SITE, 'js', 'data.js')
main   = read(SITE, 'js', 'main.js')

html = html.replace('<html lang="ar" dir="rtl">', '<html lang="ar" dir="rtl" data-root="../../">')

logo = data_uri(os.path.join(ACADEMY, 'assets', 'academy-logo.png'))
ui_js = ui_js.replace("' + ROOT + 'assets/academy-logo.png", logo)
assert 'assets/academy-logo.png' not in ui_js, 'shared logo path not inlined (sdaia-ui.js changed?)'

ASSET_RE = re.compile(r'assets/[A-Za-z0-9_\-\.؀-ۿ%\(\) ]+?\.(?:png|jpg|jpeg|webp|svg|gif)')
missing = set()
def inline_assets(text):
    def sub(m):
        rel  = urllib.parse.unquote(m.group(0))
        path = os.path.join(SITE, rel.replace('/', os.sep))
        if os.path.isfile(path):
            d = data_uri(path)
            if d: return d
        missing.add(rel)
        return m.group(0)
    return ASSET_RE.sub(sub, text)

html = inline_assets(html)
data = inline_assets(data)

for name, blob in (('ui.css',ui_css),('style.css',st_css),('icons',icons),('ui.js',ui_js),('data.js',data),('main.js',main)):
    assert '</script' not in blob, 'inlined file %s contains a closing script tag' % name

for needle, repl in (
    ('<link rel="stylesheet" href="../../assets/sdaia-ui.css">', '<style>\n'+ui_css+'\n</style>'),
    ('<link rel="stylesheet" href="css/style.css">',             '<style>\n'+st_css+'\n</style>'),
    ('<script src="../../assets/sdaia-icons.js"></script>',      '<script>\n'+icons+'\n</script>'),
    ('<script src="../../assets/sdaia-ui.js"></script>',         '<script>\n'+ui_js+'\n</script>'),
    ('<script src="js/data.js"></script>',                       '<script>\n'+data+'\n</script>'),
    ('<script src="js/main.js"></script>',                       '<script>\n'+main+'\n</script>')):
    assert needle in html, 'reference not found: %s' % needle
    html = html.replace(needle, repl)

for needle in ('href="../../assets/sdaia-ui.css"','src="../../assets/sdaia-icons.js"',
               'src="../../assets/sdaia-ui.js"','src="js/data.js"','src="js/main.js"','href="css/style.css"'):
    assert needle not in html, 'reference not inlined: %s' % needle

left = ASSET_RE.findall(html)
if left or missing:
    print('!! unresolved assets/ paths still in output:', sorted(set(missing))[:20], file=sys.stderr)
assert not left, 'standalone still contains assets/ paths — every image must be inlined'

out = os.path.join(SITE, 'sdaia-success-stories-standalone.html')
open(out, 'w', encoding='utf-8', newline='').write(html)
print('Built %s (%.2f MB)' % (out, os.path.getsize(out)/1048576))
