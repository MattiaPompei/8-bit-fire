"""Costruisce l'app e le pagine per GitHub Pages da src/app.html.
- src/app.html: sorgente dell'app (formato artifact, senza <head>), con {{AUDIO_LOW}} e {{AUDIO_HIGH}} al posto dell'audio.
- dist/app-artifact.html: sorgente + audio in base64, da pubblicare come artifact su Claude.
- docs/play.html: la stessa app avvolta in un documento completo (viewport, meta iPhone, manifest, service worker).
- docs/sw.js: service worker con la cache legata al contenuto, così ogni build aggiorna i telefoni.
Uso: python3 tools/build.py            (build normale)
     python3 tools/build.py --snapshot  (in più salva AAAA-MM-GG_8-bit-fire_App_vNN.html con il numero successivo)"""
import base64, datetime, glob, hashlib, os, re, sys

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
b64 = lambda f: base64.b64encode(open(f'audio/{f}.m4a', 'rb').read()).decode()
body = (open('src/app.html', encoding='utf-8').read()
        .replace('{{AUDIO_LOW}}', b64('fuoco-basso')).replace('{{AUDIO_HIGH}}', b64('fuoco-alto')))
os.makedirs('dist', exist_ok=True)
open('dist/app-artifact.html', 'w', encoding='utf-8').write(body)
src = 'src/app.html'

if '--snapshot' in sys.argv:
    nums = [int(re.search(r'_v(\d+)\.html$', p).group(1)) for p in glob.glob('*_App_v*.html')]
    snap = f"{datetime.date.today():%Y-%m-%d}_8-bit-fire_App_v{max(nums, default=0) + 1:02d}.html"
    open(snap, 'w', encoding='utf-8').write(body)
    print('snapshot', snap)

HEAD = '''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>8-bit fire</title>
<meta name="description" content="Un fuoco in pixel da accendere, scaldare e piegare al vento con un dito.">
<meta name="theme-color" content="#0c0a09">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="8-bit fire">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icons/favicon-32.png" type="image/png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<style>
/* Base che nell'artifact aggiunge la piattaforma: margini di sicurezza del telefono e [hidden] */
:root { padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); }
body { margin: 0; }
[hidden] { display: none !important; }
</style>
<script>
if ('serviceWorker' in navigator && location.protocol === 'https:') {
  addEventListener('load', () => navigator.serviceWorker.register('sw.js').catch(() => {}));
}
</script>
</head>
<body>
'''
page = HEAD + '<!-- generato da ' + src + ' con tools/build.py -->\n' + body + '\n</body>\n</html>\n'
open('docs/play.html', 'w', encoding='utf-8').write(page)

version = hashlib.sha1((page + open('docs/index.html', encoding='utf-8').read()).encode()).hexdigest()[:10]
open('docs/sw.js', 'w', encoding='utf-8').write(f'''// Service worker di 8-bit fire: l'app funziona anche offline dopo la prima apertura.
// Pagine: prima la rete (così gli aggiornamenti arrivano), poi la cache. Icone e manifest: prima la cache.
// Font di Google: cache con aggiornamento in background. Versione generata da tools/build.py.
const CACHE = '8bit-fire-{version}';
const CORE = ['./', 'index.html', 'play.html', 'manifest.webmanifest',
  'icons/icon-192.png', 'icons/icon-512.png', 'icons/icon-maskable-512.png', 'icons/apple-touch-icon.png', 'icons/favicon-32.png'];

self.addEventListener('install', e => {{
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(CORE)).then(() => self.skipWaiting()));
}});
self.addEventListener('activate', e => {{
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
}});
self.addEventListener('fetch', e => {{
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  const isFont = url.hostname === 'fonts.googleapis.com' || url.hostname === 'fonts.gstatic.com';
  if (isFont) {{
    e.respondWith(caches.open(CACHE).then(async c => {{
      const hit = await c.match(req);
      const net = fetch(req).then(r => {{ c.put(req, r.clone()); return r; }}).catch(() => hit);
      return hit || net;
    }}));
    return;
  }}
  if (url.origin !== location.origin) return;
  if (req.mode === 'navigate' || url.pathname.endsWith('.html')) {{
    e.respondWith(fetch(req).then(r => {{ const copy = r.clone(); caches.open(CACHE).then(c => c.put(req, copy)); return r; }})
      .catch(() => caches.match(req).then(r => r || caches.match('play.html'))));
    return;
  }}
  e.respondWith(caches.match(req).then(r => r || fetch(req).then(res => {{
    const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); return res;
  }})));
}});
''')
print('docs/play.html <-', src, '| cache', version)
