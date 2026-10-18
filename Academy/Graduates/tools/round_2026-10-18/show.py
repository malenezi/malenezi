import json,sys
s=open('/'.join(__file__.split('/')[:-4])+'/Graduates/index.html',encoding='utf-8').read()
i=s.index('const DATA = ')+len('const DATA = '); j=s.index('\nconst SITE_STATS')
g=json.loads(s[i:j].rstrip()[:-1])['grads']
for k in map(int,sys.argv[1:]):
  r=g[k-1]; print('#%d'%k,r['n'],'/',r['en'],'|',r['prog'][:70],'|',r['co'],'|',r['emp'],r['role'],'|',r['links'],'|',r['d'][:300]);print()
