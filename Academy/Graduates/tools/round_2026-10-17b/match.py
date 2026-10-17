import json,re,os,sys
sys.path[:0]=[os.path.expanduser('~/mnt/Academy/Graduates/tools/round_2026-10-07'),os.path.expanduser('~/mnt/Academy/Graduates/tools')]
import translit as TR
H=os.path.expanduser('~/mnt/Academy/')
s=open(H+'Graduates/index.html',encoding='utf-8').read()
i=s.index('const DATA = ')+len('const DATA = '); j=s.index('\nconst SITE_STATS')
g=json.loads(s[i:j].rstrip()[:-1])['grads']; idx=TR.build_index(g)
for l in open(sys.argv[1],encoding='utf-8'):
    sl,nm=l.strip().split('|')
    m=sorted({x[0] for x in TR.match(nm,nm,idx)})
    ex=[k+1 for k,r in enumerate(g) if (r.get('en') or '').lower()==nm.lower()]
    lk=[k+1 for k,r in enumerate(g) if any(('/'+sl.lower()) in (x[1] or '').lower() for x in r.get('links') or [])]
    info=' ; '.join(f"#{k} {g[k-1]['n']}/{g[k-1]['en']} [{g[k-1]['prog'][:45]}|{g[k-1]['co'][:18]}]" for k in (ex or m)[:3])
    print(f"{nm} | link{lk} ex{ex} m{m[:5]} | {info}")
