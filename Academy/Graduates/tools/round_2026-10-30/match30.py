import json,re,sys,os,difflib
sys.path.insert(0,'.'); from posts30 import POSTS
H=os.path.expanduser('~/mnt/Academy/')
s=open(H+'Graduates/index.html',encoding='utf-8').read(); i=s.index('const DATA = ')+13; j=s.index('\nconst SITE_STATS')
g=json.loads(s[i:j].rstrip()[:-1])['grads']; print('N',len(g))
nz=lambda x:re.sub(r'[^a-z]','',(x or '').lower())
for slug,nm,prog,dt,path in POSTS:
    hits=[k+1 for k,r in enumerate(g) if any(slug.lower() in l[1].lower() for l in r['links'])]
    ph=[k+1 for k,r in enumerate(g) if any(path[:40].lower() in l[1].lower() for l in r['links'])]
    toks=nm.lower().replace('.','').split(); last=nz(toks[-1]); first=nz(toks[0])
    nm_hits=[k+1 for k,r in enumerate(g) if last and last in nz(r.get('en')) and first[:4] in nz(r.get('en'))]
    print('==',nm,'| slug',hits,'| post',bool(ph),'| name',nm_hits[:8])
    for k in sorted(set(hits+nm_hits))[:6]:
        r=g[k-1]; print('   #%d %s / %s | %s | %s | emp=%s'%(k,r['n'],r.get('en'),r['prog'][:70],r['co'][:40],r.get('emp')))
