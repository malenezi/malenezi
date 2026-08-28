import json
p='/root/x'
import os
HOME=os.path.expanduser('~')
src=HOME+'/mnt/Academy/Graduates/index.html'
s=open(src,encoding='utf-8').read()
j=s.find('const DATA = ')+len('const DATA = ')
depth=0;k=j
while True:
    c=s[k]
    if c=='{':depth+=1
    elif c=='}':
        depth-=1
        if depth==0:break
    k+=1
d=json.loads(s[j:k+1])
json.dump(d,open(HOME+'/work/data.json','w',encoding='utf-8'),ensure_ascii=False)
g=d['grads']
print('grads',len(g))
# collect all linkedin slugs
import re
slugs=set(); gh=set()
for x in g:
    for label,url in x.get('links',[]):
        m=re.search(r'linkedin\.com/in/([^/?#]+)',url,re.I)
        if m: slugs.add(m.group(1).lower().rstrip('/'))
        m2=re.search(r'github\.com/([^/?#]+)',url,re.I)
        if m2: gh.add(m2.group(1).lower())
json.dump({'slugs':sorted(slugs),'gh':sorted(gh)},open(HOME+'/work/links.json','w'),ensure_ascii=False)
print('linkedin slugs',len(slugs),'github',len(gh))
print('with en',sum(1 for x in g if x.get('en')))
