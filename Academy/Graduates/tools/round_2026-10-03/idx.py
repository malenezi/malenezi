import json,re
s=open('index.html',encoding='utf-8').read()
i0=s.index('const DATA = {"grads"'); j=s.index('[',i0)
dec=json.JSONDecoder(); g,_=dec.raw_decode(s[j:])
print(len(g))
slugs={};gh={}
for i,r in enumerate(g,1):
    for l in r.get('links') or []:
        u=l[1]
        m=re.search(r'linkedin\.com/in/([^/?#]+)',u)
        if m: slugs[m.group(1).lower()]=i
        m=re.search(r'github\.com/([^/?#]+)',u)
        if m: gh[m.group(1).lower()]=i
json.dump({'slugs':slugs,'gh':gh,'names':[[i,r['n'],r.get('en',''),r.get('prog','')[:60],r.get('co','')] for i,r in enumerate(g,1)]},open('tools/round_2026-10-03/idx.json','w',encoding='utf-8'),ensure_ascii=False)
print(len(slugs),len(gh))
from collections import Counter
print(Counter(r.get('tr') for r in g))
