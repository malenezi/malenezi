import json,os,sys,re
sys.path[:0]=[os.path.expanduser('~/mnt/Academy/Graduates/tools/round_2026-10-07'),os.path.expanduser('~/mnt/Academy/Graduates/tools')]
import translit as TR
s=open(os.path.expanduser('~/mnt/Academy/Graduates/index.html'),encoding='utf-8').read()
i=s.index('const DATA = ')+len('const DATA = '); j=s.index('\nconst SITE_STATS')
g=json.loads(s[i:j].rstrip()[:-1])['grads']; idx=TR.build_index(g)
for r in json.load(open('new18.json',encoding='utf-8')):
    ar,en=r[0],r[1]
    m=sorted({x[0] for x in TR.match(ar,en,idx)})
    ex=[k+1 for k,G in enumerate(g) if G['n']==ar or (G.get('en') or '').lower()==en.lower()]
    hits=sorted(set(m)|set(ex))
    if hits: print(en,'|',' ; '.join(f"#{k} {g[k-1]['n']}/{g[k-1]['en']} [{g[k-1]['prog'][:35]}|{g[k-1]['co'][:20]}|L{len(g[k-1]['links'])}]" for k in hits[:4]))
