import json,sys
from translit import tokens
g=json.load(open('data.json'))['grads']
idx=[]
for i,x in enumerate(g,1):
    ts=[tokens(x.get('n','')),tokens(x.get('en',''))]
    idx.append((i,x.get('n',''),x.get('en',''),ts,x.get('prog','')[:60]))
def check(ar,en):
    cs=[tokens(ar),tokens(en)]
    hits=[]
    for rid,a,e,ts,p in idx:
        best=0
        for c in cs:
            for t in ts:
                if c and t and c[0]==t[0]:
                    sh=len(set(c[1:])&set(t[1:]))
                    best=max(best,sh)
        if best>=1: hits.append((best,rid,a,e,p))
    return sorted(hits,reverse=True)[:3]
if __name__=='__main__':
    exec(open(sys.argv[1]).read())
    for h,(en,ar,*r) in A.items():
        hs=check(ar,en)
        if hs: print(h,en,ar,'->',[(b,rid,a,e,p[:40]) for b,rid,a,e,p in hs])
