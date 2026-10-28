import json,sys,re,difflib
s=open('../../index.html',encoding='utf-8').read()
i=s.index('const DATA = ')+13;j=s.index('\nconst SITE_STATS')
g=json.loads(s[i:j].rstrip()[:-1])['grads']
q=[a.split('|') for a in sys.argv[1:]]
norm=lambda x:re.sub(r'[^a-z]','',x.lower().replace('al-','al'))
for en,slug in q:
  hit=[]
  for k,r in enumerate(g,1):
    L=' '.join(l[1].lower() for l in r['links'])
    if slug and slug.lower() in L: hit.append((k,'SLUG'))
    elif norm(en)==norm(r.get('en') or ''): hit.append((k,'NAME'))
    elif difflib.SequenceMatcher(None,norm(en),norm(r.get('en') or '')).ratio()>0.88: hit.append((k,'fuzzy'))
  print(en,'->',[(k,t,g[k-1]['n'],g[k-1]['en'],g[k-1]['prog'][:50],g[k-1]['co'][:20]) for k,t in hit])
