# usage: python chk.py cands.txt   lines: en|url   -> prints NEW / match ids
import json,re,os,sys
sys.path[:0]=[os.path.expanduser('~/mnt/Academy/Graduates/tools/round_2026-10-07'),os.path.expanduser('~/mnt/Academy/Graduates/tools')]
import translit as TR
s=open(os.path.expanduser('~/mnt/Academy/Graduates/index.html'),encoding='utf-8').read()
i=s.index('const DATA = ')+13; j=s.index('\nconst SITE_STATS'); g=json.loads(s[i:j].rstrip()[:-1])['grads']
norm=lambda u:re.sub(r'^https?://(www\.|[a-z]{2}\.)?','',u).split('?')[0].rstrip('/').lower()
L={}
for k,r in enumerate(g,1):
    for l in r['links']: L[norm(l[1])]=k
idx=TR.build_index(g)
print('N',len(g))
for line in open(sys.argv[1],encoding='utf-8'):
    line=line.strip()
    if not line: continue
    en,url=(line.split('|')+[''])[:2]
    if url and norm(url) in L: print('LINK',L[norm(url)],en); continue
    m=sorted({x[0] for x in TR.match('',en,idx)}|{k for k,r in enumerate(g,1) if (r.get('en') or '').lower()==en.lower()})
    print(('MATCH '+str(m)) if m else 'NEW', en, url, ' | '.join('%d:%s/%s/%s'%(k,g[k-1]['n'],g[k-1]['en'],g[k-1]['co'][:20]) for k in m[:3]))
