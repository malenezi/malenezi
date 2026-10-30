import json,re,os,collections,openpyxl,unicodedata
H=os.path.expanduser('~/mnt/Academy/')
s=open(H+'Graduates/index.html',encoding='utf-8').read()
i=s.index('const DATA = ')+13;j=s.index('\nconst SITE_STATS');g=json.loads(s[i:j].rstrip()[:-1])['grads'];N=len(g);gt=s[:i]+s[j:]
T=collections.Counter(r['tr'] for r in g); wl=sum(1 for r in g if r['links']); uu=len({l[1].rstrip('/') for r in g for l in r['links']})
sj=open(H+'SuccessStories/website/js/data.js',encoding='utf-8').read()
k=sj.index('const STORIES = [');e=sj.index('\n];',k)
ST=[json.loads(l.strip().rstrip(',')) for l in sj[k:e].split('\n')[1:] if l.strip().startswith('{')]
S=len(ST); EX={'award','finalist','team','undisclosed'}
print('N',N,dict(T),'wl',wl,'uu',uu,'stories',S)
P=open(H+'index.html',encoding='utf-8').read(); SS=open(H+'SuccessStories/website/index.html',encoding='utf-8').read()
issues=[]
def chk(name,cond): 
    if not cond: issues.append(name)
f=format(N,',')
chk('portal N',P.count('data-count="%d"'%N)==1); chk('portal S',P.count('data-count="%d"'%S)==1)
chk('portal N text',f in P); chk('grads N text',f in gt)
chk('jsonld',('"numberOfItems": %d'%S) in SS)
chk('datajs grads',re.search(r"value: %d, label: 'خريجًا موثّقًا'"%N,sj) is not None)
chk('datajs stories',re.search(r"value: %d,\s+label: 'قصة نجاح"%S,sj) is not None)
chk('grads stories kpi',re.search(r"value: %d,\s+label: 'قصة نجاح"%S,gt) is not None)
for tk,en in {'ai':'AI Engineer','ds':'Data Scientist','dmg':'Data Management & Governance','other':'Other / Specialized','genai':'Gen AI Academy','coop':'Cooperative Training (COOP)'}.items():
    chk('grads track '+tk,re.search(r"en: '%s', value: %d\b"%(re.escape(en),T[tk]),gt) is not None)
    chk('datajs track '+tk,re.search(r"en: '%s',\s+value: %d\b"%(re.escape(en),T[tk]),sj) is not None)
    chk('portal track '+tk,('data-count="%d"'%T[tk]) in P)
chk('links kpi',re.search(r"value: %d,\s+label: 'سجلًا برابط تحقق علني', note: '%s رابط"%(wl,format(uu,',')),gt) is not None)
# stale
for fn,t in (('portal',P),('grads',gt),('ss',SS)):
    for old in ('208 قصة','208 stories','119 جهة','119 employers','226 قصة','226 stories','122 جهة','122 employers','226 verified','14-month criterion','معيار الأربعة عشر شهرًا ·','مستوفية معيار الأربعة عشر','204 verified','across 109','30 أكتوبر 2026 (منشورات','30 October 2026 (supplied'):
        if old in t and not (old.startswith('27') and fn=='grads' and False): issues.append(f'stale {old} in {fn}')
# xlsx
wb=openpyxl.load_workbook(H+'Graduates/Graduates_Database.xlsx',read_only=True); ws=wb['قاعدة البيانات']
rows=list(ws.iter_rows(min_row=2,values_only=True)); rows=[r for r in rows if r[0] is not None]
chk('xlsx rows',len(rows)==N)
mis=[r[0] for r,G in zip(rows,g) if (r[1] or '').strip()!=G['n'].strip()]; chk('xlsx names',not mis)
stt={r[0]:r[1] for r in wb['إحصاءات'].iter_rows(values_only=True)}
chk('xlsx total',str(stt.get('الإجمالي')).replace(',','') in (str(N),))
md=open(H+'Graduates/Graduates_Database.md',encoding='utf-8').read(); chk('md version',(f'→ {f}' in md.split(chr(10))[2]) or (f'{f} · القصص {S}' in md))
# stories
ids=collections.Counter(x['id'] for x in ST); chk('dup story ids',max(ids.values())==1)
for x in ST:
    q=x.get('quote') or {}
    if len(q.get('text',''))>100 or len(q.get('textEn',''))>100: issues.append('quote>100 '+x['id'])
    for fld in ('photo','orgLogo'):
        v=x.get(fld)
        if v and not v.startswith('http') and not os.path.exists(H+'SuccessStories/website/'+v): issues.append(f'missing {fld} {x["id"]}')
    if '**' in json.dumps(x,ensure_ascii=False): issues.append('** '+x['id'])
    refs=re.findall(r'#(\d{1,4})\b',x.get('provenance',''))
    if refs and int(refs[-1])<=N:
        G=g[int(refs[-1])-1]
        if 'job' not in G['cats'] and x.get('category')=='employment': issues.append(f'story rec no job cat {x["id"]} #{refs[-1]}')
# employers
orgs={x['org'].strip() for x in ST if x.get('org')}
print('distinct orgs raw',len(orgs))
# DB hygiene
nrm=lambda u:re.sub(r'^https?://(www\.|[a-z]{2}\.)?','',u).rstrip('/').lower()
LS=collections.defaultdict(set)
for kk,r in enumerate(g,1):
    for _,u in r['links']:
        m=re.match(r'(linkedin\.com/in/[^/]+|github\.com/[^/]+)$',nrm(u))
        if m: LS[m.group(1)].add(kk)
sh=[(a,sorted(v)) for a,v in LS.items() if len(v)>1]; chk('shared identity links '+str(sh[:3]),not sh)
for kk,r in enumerate(g,1):
    for fld in ('n','en','prog','co','d','emp','role'):
        v=r.get(fld) or ''
        if '**' in v or '  ' in v or v!=v.strip(): issues.append(f'ws {kk} {fld}')
    if not r['prog'] or not r['n']: issues.append(f'empty {kk}')
    if r['tr'] not in T: issues.append(f'tr {kk}')
# exact dup en (non-cross-noted)
en=collections.defaultdict(list)
for kk,r in enumerate(g,1):
    x=re.sub(r'[^a-z]','',(r.get('en') or '').lower())
    if len(x)>8: en[x].append(kk)
d=[(a,v) for a,v in en.items() if len(v)>1]
unnoted=[v for a,v in d if not any(('#%d'%o) in g[v[-1]-1]['d'] or ('#%d'%v[-1]) in g[o-1]['d'] for o in v[:-1])]
print('dup en groups',len(d),'without cross-note',len(unnoted),unnoted[:15])
# catalog
C=open(H+'Catalog/index.html',encoding='utf-8').read(); m=re.search(r'<script id="catalog-data"[^>]*>(.*?)</script>',C,re.S); CD=json.loads(m.group(1))
chk('catalog 37',len(CD['programs'])==37); chk('catalog certs',len(CD.get('certifications',[]))==2)
chk('catalog days 132',sum(p['days'] for p in CD['programs'])==132); chk('catalog hours',all(p['hours']==p['days']*5 for p in CD['programs']))
# footer stamps
for fn in ('index.html','about.html','Catalog/index.html','Graduates/index.html','SuccessStories/website/index.html'):
    t=open(H+fn,encoding='utf-8').read()
    if 'إصدار 30 أكتوبر 2026' not in t or 'version 30 October 2026' not in t: issues.append('stamp '+fn)
st=os.path.getmtime(H+'SuccessStories/website/sdaia-success-stories-standalone.html'); dm=os.path.getmtime(H+'SuccessStories/website/js/data.js')
chk('standalone fresh',st>=dm)
print('ISSUES',len(issues)); print('\n'.join(issues[:60]))
# ---- v2.0 checks ----
iss2=[]
for x in ST:
    q=x['quote']
    if q.get('kind')!='verified': iss2.append('draft '+x['id'])
    if len(q['text'])>97 or len(q['textEn'])>97: iss2.append('quote>97 '+x['id'])
    if x['category'] not in ('employment','promotion','founder'): iss2.append('cat '+x['id'])
    if not x.get('photo'): iss2.append('nophoto '+x['id'])
    if re.search(r'أربعة عشر شهرًا|14 شهرًا|14-month',json.dumps(x,ensure_ascii=False)): iss2.append('14m '+x['id'])
cats={c['id'] for c in json.loads('['+re.search(r"const CATEGORIES = \[(.*?)\];",sj,re.S).group(1).replace("'",'"').replace('id:','"id":').replace('labelEn:','"labelEn":').replace('label:','"label":').rstrip().rstrip(',')+']')}
print('categories',cats)
print('V2 ISSUES',len(iss2),iss2[:20])
