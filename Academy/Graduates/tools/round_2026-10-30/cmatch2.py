import json,os,re,sys
sys.path.insert(0,'.'); sys.path.insert(0,'..')
from cand30 import C
from translit import tokens
H=os.path.expanduser('~/mnt/Academy/')
s=open(H+'Graduates/index.html',encoding='utf-8').read(); i=s.index('const DATA = ')+13; j=s.index('\nconst SITE_STATS')
g=json.loads(s[i:j].rstrip()[:-1])['grads']
idx=[(k+1,tokens(r['n']),tokens(r.get('en') or '')) for k,r in enumerate(g)]
for sl,nm,pg,age,_ in C:
    ct=tokens(nm.replace('Dr. ',''))
    h=[]
    for k,a,b in idx:
        for rt in (a,b):
            if rt and ct and rt[0]==ct[0] and set(ct[1:])&set(rt[1:]): h.append(k); break
    print('==',nm,'|',pg,'|',age,'->',len(h))
    for k in h[:5]:
        r=g[k-1]; print('    #%d %s / %s | %s | %s | li=%s'%(k,r['n'],r.get('en'),r['prog'][:50],r['co'][:22],any('linkedin' in x[1] for x in r['links'])))
