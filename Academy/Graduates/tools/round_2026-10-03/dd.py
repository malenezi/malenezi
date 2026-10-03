import json,sys,re,difflib
I=json.load(open('idx.json',encoding='utf-8'))
def norm(x): return re.sub(r'[^a-z ]','',x.lower().replace('-',' ')).replace(' al ',' al').strip()
ens={}
for i,n,en,p,co in I['names']:
    for v in (n,en):
        if v: ens.setdefault(norm(v) if re.search('[a-z]',v.lower()) else v.strip(),[]).append(i)
def look(slug,name):
    if slug.lower() in I['slugs']: return 'SLUG#%d'%I['slugs'][slug.lower()]
    k=norm(name); k2=k.replace('al ','al')
    hits=[]
    for key,ids in ens.items():
        if not re.search('[a-z]',key): continue
        kk=key.replace('al ','al')
        if kk==k2 or kk.replace(' ','')==k2.replace(' ',''): hits+=ids
    if hits: return 'NAME#'+','.join(map(str,hits[:5]))
    close=difflib.get_close_matches(k2,[x.replace('al ','al') for x in ens if re.search('[a-z]',x)],n=2,cutoff=0.88)
    return 'NEW'+(' ~'+'/'.join(close) if close else '')
for item in sys.stdin.read().strip().split(';'):
    if '|' not in item: continue
    s,n=item.split('|',1); print(look(s,n),'\t',s,'\t',n)
