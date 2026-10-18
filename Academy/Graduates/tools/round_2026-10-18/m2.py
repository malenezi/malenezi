import json,re,os,sys,urllib.parse
sys.path[:0]=[os.path.expanduser('~/mnt/Academy/Graduates/tools/round_2026-10-07'),os.path.expanduser('~/mnt/Academy/Graduates/tools')]
import translit as TR
H=os.path.expanduser('~/mnt/Academy/')
s=open(H+'Graduates/index.html',encoding='utf-8').read()
i=s.index('const DATA = ')+len('const DATA = '); j=s.index('\nconst SITE_STATS')
g=json.loads(s[i:j].rstrip()[:-1])['grads']; idx=TR.build_index(g)
for l in open(sys.argv[1],encoding='utf-8'):
    if not l.strip(): continue
    sl,nm=l.strip().split('|')[:2]; slu=urllib.parse.unquote(sl).lower()
    lk=[k+1 for k,r in enumerate(g) if any(('/in/'+slu) in urllib.parse.unquote(x[1] or '').lower().rstrip('/')+'/' and ('/in/'+slu+'/') in urllib.parse.unquote(x[1] or '').lower().rstrip('/')+'/' for x in r.get('links') or [])]
    if lk: print('KNOWN',nm,lk); continue
    m=sorted({x[0] for x in TR.match(nm,nm,idx)})
    ex=[k+1 for k,r in enumerate(g) if (r.get('en') or '').lower()==nm.lower()]
    info=' ; '.join(f"#{k} {g[k-1]['n']}/{g[k-1]['en']} [{g[k-1]['prog'][:40]}|{g[k-1]['co'][:14]}|L{len(g[k-1]['links'])}]" for k in (ex or m)[:3])
    print(('MAYBE ' if (ex or m) else 'NEW   ')+f"{sl}|{nm} | {info}")
