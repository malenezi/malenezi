import json,re,urllib.request,html,concurrent.futures as cf
def get(u,raw=False):
    try:
        r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=20); b=r.read().decode('utf-8','ignore'); return b
    except Exception as e: return ''
s=open('../../index.html',encoding='utf-8').read().lower()
out=[]
for repo in ['qafila-margin-project','international-airpassengers-project','deep-research-agent-langgraph-project','data-engineering']:
    forks=[]
    for p in (1,2):
        d=json.loads(get(f'https://api.github.com/repos/SDAIAAcademy/{repo}/forks?per_page=100&page={p}') or '[]')
        forks+=d
        if len(d)<100: break
    for f in forks:
        o=f['owner']['login']; inDB=('github.com/'+o.lower()) in s
        out.append(dict(repo=repo,owner=o,full=f['full_name'],branch=f['default_branch'],created=f['created_at'][:10],pushed=f['pushed_at'][:10],inDB=inDB))
print({r:sum(1 for x in out if x['repo']==r) for r in set(x['repo'] for x in out)}, 'notInDB',sum(1 for x in out if not x['inDB']))
def enrich(x):
    if x['inDB']: return x
    rd=get(f"https://raw.githubusercontent.com/{x['full']}/{x['branch']}/README.md")
    m=re.search(r'Submitted by:?\s*(.+)',rd); x['submitted']=m.group(1).strip()[:120] if m else ''
    au=re.search(r'##\s*Author[^\n]*\n+([^\n]+)',rd); x['author']=au.group(1).strip()[:100] if au else ''
    pg=get('https://github.com/'+x['owner'])
    m=re.search(r'itemprop="name">\s*([^<]*)<',pg); x['pname']=html.unescape(m.group(1).strip()) if m else ''
    m=re.search(r'itemprop="url"[^>]*href="([^"]+)"',pg) or re.search(r'rel="nofollow me"[^>]*href="(https://[^"]*linkedin[^"]+)"',pg)
    li=re.findall(r'href="(https://(?:www\.)?linkedin\.com/in/[^"]+)"',pg); x['li']=li[0] if li else ''
    at=get(f"https://github.com/{x['full']}/commits/{x['branch']}.atom")
    auth=re.findall(r'<author>\s*<name>([^<]+)</name>',at); x['commit_authors']=sorted(set(auth))[:5]
    return x
with cf.ThreadPoolExecutor(8) as ex: out=list(ex.map(enrich,out))
json.dump(out,open('forks.json','w'),ensure_ascii=False,indent=0)
for x in out:
    if not x['inDB']: print(x['repo'][:8],x['owner'],x['created'],'|',x.get('submitted'),'|',x.get('author'),'|',x.get('pname'),'|',x.get('li'),'|',x.get('commit_authors'))
