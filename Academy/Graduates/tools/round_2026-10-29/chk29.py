# -*- coding: utf-8 -*-
# usage: python3 chk29.py "slug1 slug2 ..." "Name One|Name Two"
import json,re,sys,os,difflib
from urllib.parse import unquote
H=os.path.expanduser('~/mnt/Academy/')
s=open(H+'Graduates/index.html',encoding='utf-8').read()
i=s.index('const DATA = ')+13; j=s.index('\nconst SITE_STATS'); g=json.loads(s[i:j].rstrip()[:-1])['grads']
SL={}
for k,r in enumerate(g,1):
    for l in r['links']:
        m=re.search(r'linkedin\.com/(?:in|posts)/([^/_?]+)',l[1])
        if m: SL[unquote(m.group(1)).lower()]=k
EN=[((r.get('en') or '').lower(),k) for k,r in enumerate(g,1)]
def nn(x): return re.sub(r'[^a-z ]','',x.lower().replace('-',' ')).replace(' al ',' al').strip()
slugs=sys.argv[1].split() if len(sys.argv)>1 else []
for sl in slugs:
    k=SL.get(sl.lower())
    if k: print('KNOWN',sl,'#%d'%k,g[k-1]['n']); continue
    base=nn(re.sub(r'-[0-9a-f]{6,}$','',sl).replace('-',' '))
    best=difflib.get_close_matches(base,[nn(e) for e,_ in EN],n=3,cutoff=0.85)
    hits=[(k,g[k-1]['n'],g[k-1]['en'],g[k-1]['prog'][:50],g[k-1]['co'][:25]) for e,k in EN if nn(e) in best][:4]
    print('NEW?',sl,'| namehits:',hits)
