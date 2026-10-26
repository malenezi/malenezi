import json,re,os,collections,openpyxl,subprocess
H=os.path.expanduser('~/mnt/Academy/'); os.chdir(H); R=collections.defaultdict(list)
s=open('Graduates/index.html',encoding='utf-8').read();i=s.index('const DATA = ')+13;j=s.index('\nconst SITE_STATS');g=json.loads(s[i:j].rstrip()[:-1])['grads']
N=len(g); T=collections.Counter(r['tr'] for r in g); wl=sum(1 for r in g if r.get('links')); uu=len({l[1].rstrip('/') for r in g for l in r['links']})
print('N',N,dict(T),'wl',wl,'uu',uu)
TR={'ai','ds','dmg','genai','other','coop'}
norm=lambda u:re.sub(r'^https?://(www\.|[a-z]{2}\.)?','',u).rstrip('/').lower()
LK=collections.defaultdict(set)
for k,r in enumerate(g,1):
    for f in ('n','prog','tr','d','src'):
        if not (r.get(f) or '').strip(): R['empty_'+f].append(k)
    if r['tr'] not in TR: R['bad_tr'].append(k)
    for f,v in r.items():
        if isinstance(v,str):
            if '**' in v: R['stars'].append((k,f))
            if re.search(r'  |^\s|\s$',v) and f!='d': R['ws'].append((k,f))
            if '​' in v or '﻿' in v: R['zw'].append((k,f))
    if 'alias' in r and not isinstance(r['alias'],str): R['alias_type'].append(k)
    if r.get('en') and r['en'].isupper() and len(r['en'])>4: R['en_caps'].append(k)
    seen=set()
    for lab,u in r['links']:
        if not re.match(r'^https://',u): R['url_scheme'].append((k,u))
        if ' ' in u: R['url_space'].append((k,u))
        n_=norm(u)
        if n_ in seen: R['dup_link_in_rec'].append((k,u))
        seen.add(n_); LK[n_].add(k)
    if not isinstance(r.get('score'),int): R['score_type'].append(k)
for u,ks in LK.items():
    if len(ks)>1 and re.search(r'linkedin\.com/in/[^/]+$|github\.com/[^/]+$',u): R['shared_identity_link'].append((u,sorted(ks)))
# stories
dj=open('SuccessStories/website/js/data.js',encoding='utf-8').read()
st=[json.loads(l.strip().rstrip(',')) for l in dj.split('\n') if l.startswith('  {"id": ')]
ids=collections.Counter(x['id'] for x in st); R['dup_story_id']=[k for k,v in ids.items() if v>1]
for x in st:
    for f in ('photo','orgLogo'):
        p=x.get(f)
        if p and not p.startswith('http') and not os.path.exists('SuccessStories/website/'+p): R['missing_'+f].append((x['id'],p))
    q=x.get('quote',{})
    if len(q.get('text',''))>100 or len(q.get('textEn',''))>100: R['quote_len'].append(x['id'])
    if not q.get('text') or not q.get('textEn'): R['quote_missing'].append(x['id'])
    for f,v in x.items():
        if isinstance(v,str) and '**' in v: R['story_stars'].append(x['id'])
    refs=[int(m) for m in re.findall(r'سجل (?:الأكاديمية|الخريج) #(\d+)',x.get('provenance',''))]
    if not refs: R['story_no_ref'].append(x['id'])
    for rf in refs[:1]:
        if rf>N: R['story_ref_oob'].append((x['id'],rf)); continue
        rec=g[rf-1]; names=' '.join([rec['n'],rec.get('en') or '',rec.get('alias') or '']).lower()
        tok=[t for t in re.split(r'[\s\-]+',(x['nameEn'] or '').lower()) if len(t)>2]
        atok=[t for t in x['name'].split() if len(t)>1]
        if not (sum(t in names for t in tok)>=1 and (any(t in names for t in atok) or sum(t in names for t in tok)>=2)): R['story_ref_name'].append((x['id'],rf,rec['n'],rec.get('en')))
orgs=collections.Counter(x['org'] for x in st)
print('stories',len(st),'distinct orgs',len(orgs))
# counters across files
SS=re.search(r'const SITE_STATS = \[(.*?)\];',dj,re.S).group(1); print('data.js SITE_STATS values',re.findall(r'value: (\d+)',SS)[:6])
print('data.js TRACKS',re.findall(r"key: '(\w+)'.*?value: (\d+)",dj[dj.index('const TRACKS'):dj.index('const TRACKS')+2500]))
gt=s[j:]; print('Graduates SITE_STATS',re.findall(r'\{ value: (\d+),\s+label: \'([^\']+)\'',gt)[:8])
p=open('index.html',encoding='utf-8').read(); print('portal data-counts',re.findall(r'data-count="(\d+)"',p))
print('portal numbers in prose ar/en:',collections.Counter(re.findall(r'\b\d{1,2},\d{3}\b',p)).most_common(6))
print('JSON-LD',re.findall(r'"numberOfItems": (\d+)',open('SuccessStories/website/index.html',encoding='utf-8').read()))
wb=openpyxl.load_workbook('Graduates/Graduates_Database.xlsx',read_only=True); ws=wb['قاعدة البيانات']
rows=[r for r in ws.iter_rows(min_row=2,values_only=True) if r[0] is not None]; print('xlsx rows',len(rows),'last id',rows[-1][0])
bad=[r[0] for k,r in enumerate(rows,1) if r[0]!=k or (r[1] or '')!=g[k-1]['n']]; R['xlsx_misalign']=bad[:10]
stt={r[0]:r[1] for r in wb['إحصاءات'].iter_rows(values_only=True) if r[0]}; print('xlsx stats',{k:stt.get(k) for k in ('الإجمالي','التدريب التعاوني','سجلات بروابط تحقق علنية','روابط مصدر فريدة')})
md=open('Graduates/Graduates_Database.md',encoding='utf-8').read(); print('md header',re.search(r'\*\*الإصدار:\*\*[^\n]{0,160}',md).group(0))
# asset refs
refs=set()
for f in ['index.html','about.html','Graduates/index.html','SuccessStories/website/index.html','SuccessStories/website/js/data.js','Catalog/index.html']:
    t=open(f,encoding='utf-8').read(); base=os.path.dirname(f)
    for m in re.findall(r'(?:src|href)=["\']([^"\'#?]+)["\']|"(assets/[^"]+)"',t):
        u=m[0] or m[1]
        if re.match(r'^(https?:|mailto:|data:|javascript:|//)',u) or not u: continue
        pth=os.path.normpath(os.path.join(base if not f.endswith('data.js') else 'SuccessStories/website',u)); refs.add(pth)
        if not os.path.exists(pth): R['missing_asset'].append((f,u))
un=[a for d in ('assets','SuccessStories/website/assets') for a in [os.path.normpath(os.path.join(d,x)) for x in os.listdir(d)] if os.path.isfile(a) and a not in refs]
other=''.join(open(f,encoding='utf-8',errors='ignore').read() for f in ['SuccessStories/website/build_standalone.py','SuccessStories/website/css/'+os.listdir('SuccessStories/website/css')[0]] )
R['unreferenced_assets']=[a for a in un if os.path.basename(a) not in other]
for k,v in R.items():
    if v: print(k,len(v),v[:8])
