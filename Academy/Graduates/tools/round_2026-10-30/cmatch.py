import json,os,re,sys
sys.path.insert(0,'.'); from cand30 import C
sys.path.insert(0,'..'); 
try:
    from translit import skel
except Exception as e: skel=None; print('no translit',e)
H=os.path.expanduser('~/mnt/Academy/')
s=open(H+'Graduates/index.html',encoding='utf-8').read(); i=s.index('const DATA = ')+13; j=s.index('\nconst SITE_STATS')
g=json.loads(s[i:j].rstrip()[:-1])['grads']
nz=lambda x:re.sub(r'[^a-z]','',(x or '').lower())
for sl,nm,pg,age,_ in C:
    t=nm.lower().replace('dr. ','').split(); f=nz(t[0]); l=nz(t[-1])
    h=[k+1 for k,r in enumerate(g) if l[-5:] in nz(r.get('en')) and f[:4] in nz(r.get('en'))]
    print('==',nm,'|',pg,'|',age,'->',h[:6])
    for k in h[:4]:
        r=g[k-1]; print('    #%d %s / %s | %s | %s | li=%s'%(k,r['n'],r.get('en'),r['prog'][:55],r['co'][:25],any('linkedin' in x[1] for x in r['links'])))
