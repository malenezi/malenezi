import json
s=open('index.html',encoding='utf-8').read()
i=s.index('const DATA = ')+len('const DATA = '); j=s.index('\nconst SITE_STATS')
g=json.loads(s[i:j].rstrip()[:-1])['grads']
out=[{'k':k+1,**{f:r.get(f) for f in ('n','en','alias','prog','co','tr','edu','emp','role','lv','score','cats','src')}} for k,r in enumerate(g)]
json.dump(out,open('tools/round_2026-10-26/db_min.json','w',encoding='utf-8'),ensure_ascii=False)
print(len(g)); print(json.dumps(g[-1],ensure_ascii=False)[:1500]); print(sorted(g[0].keys()))
import collections; print(collections.Counter(r['tr'] for r in g)); print(collections.Counter(r['lv'] for r in g).most_common(30))
