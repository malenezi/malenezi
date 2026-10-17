# -*- coding: utf-8 -*-
# QA + data cleaning, 13 Oct 2026. Default: report only. --apply writes fixes.
import json,re,os,sys,collections,hashlib,glob
import openpyxl
APPLY='--apply' in sys.argv
H=os.path.expanduser('~/mnt/Academy/'); TAG='[تدقيق 17 أكتوبر 2026] '
P=H+'Graduates/index.html'; s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+len('const DATA = '); j=s.index('\nconst SITE_STATS')
D=json.loads(s[i:j].rstrip()[:-1]); g=D['grads']; N=len(g)
X_=H+'Graduates/Graduates_Database.xlsx'; wb=openpyxl.load_workbook(X_); ws=wb['قاعدة البيانات']
R=collections.defaultdict(list); FIX=collections.Counter()
def note(k,t):
    g[k-1]['d']+=' '+TAG+t; ws.cell(k+1,21).value=(ws.cell(k+1,21).value or '')+' '+TAG+t
# ---------- 1. text hygiene ----------
for k,r in enumerate(g,1):
    for f in ('n','en','prog','co','emp','role','edu'):
        v=r.get(f)
        if isinstance(v,str):
            nv=re.sub(r'[ \t ]{2,}',' ',v).strip().replace('**','')
            if nv!=v: r[f]=nv; FIX['ws_'+f]+=1; R['ws'].append(k)
    if r.get('emp','').strip() in ('—','-','غير موثّق علنًا','غير موثق','N/A','n/a'): r['emp']=''; FIX['emp_placeholder']+=1
# ---------- 2. URLs ----------
def canon(u):
    o=u.strip()
    u=re.sub(r'^http://','https://',o)
    u=re.sub(r'^https://([a-z]{2})\.linkedin\.com','https://www.linkedin.com',u)
    u=re.sub(r'^https://linkedin\.com','https://www.linkedin.com',u)
    m=re.match(r'^(https://www\.linkedin\.com/in/[^/?#]+)/?(?:(?:ar|en)/?)?(?:\?.*)?$',u)
    if m: u=m.group(1)+'/'
    return u
nrm=lambda u:re.sub(r'^https?://(www\.|[a-z]{2}\.)?','',u).rstrip('/').lower()
for k,r in enumerate(g,1):
    seen=set(); out=[]
    for lab,u in r['links']:
        cu=canon(u)
        if cu!=u: FIX['url_canon']+=1
        key=nrm(cu)
        if key in seen: FIX['dup_link_in_record']+=1; continue
        seen.add(key); out.append([lab,cu])
    r['links']=out
# ---------- 3. shared identity links ----------
def li_slug(u):
    m=re.match(r'https://www\.linkedin\.com/in/([^/]+)/?$',u); return m.group(1).lower() if m else None
def gh_user(u):
    m=re.match(r'https://github\.com/([^/]+)/?$',u); return m.group(1).lower() if m else None
LS=collections.defaultdict(set); GS=collections.defaultdict(set)
for k,r in enumerate(g,1):
    for lab,u in r['links']:
        a=li_slug(u); b=gh_user(u)
        if a: LS[a].add(k)
        if b: GS[b].add(k)
R['shared_li']=[(a,sorted(v)) for a,v in LS.items() if len(v)>1]
R['shared_gh']=[(a,sorted(v)) for a,v in GS.items() if len(v)>1]
# ---------- 4. validity ----------
TR={'ai','ds','dmg','genai','other','coop'}
for k,r in enumerate(g,1):
    if r['tr'] not in TR: R['bad_tr'].append(k)
    if not isinstance(r.get('score'),int) or not 0<=r['score']<=100: R['bad_score'].append(k)
    if not r.get('n'): R['no_name'].append(k)
    if not r.get('prog'): R['no_prog'].append(k)
    if not r.get('lv'): R['no_lv'].append(k)
R['win_values']=collections.Counter(r.get('win') for r in g).most_common()
# ---------- 5. same Arabic name among this round's new records ----------
byn=collections.defaultdict(list)
for k,r in enumerate(g,1): byn[re.sub(r'\s+',' ',r['n'].strip())].append(k)
for k in range(3377,N+1):
    others=[x for x in byn[g[k-1]['n'].strip()] if x!=k]
    if others: R['samename_new'].append((k,g[k-1]['n'],others))
# ---------- 6. xlsx alignment ----------
assert ws.cell(N+1,1).value==N and ws.cell(N+2,1).value is None,'xlsx row count'
for k,r in enumerate(g,1):
    row=k+1
    if ws.cell(row,1).value!=k or (ws.cell(row,2).value or '').strip()!=r['n'].strip(): R['xlsx_mis'].append(k)
# ---------- 7. stories ----------
DJ=H+'SuccessStories/website/js/data.js'; js=open(DJ,encoding='utf-8').read()
a=js.index('const STORIES = [')+len('const STORIES = '); b=js.index('\n];',a)+2
ST=json.loads(js[a:b])
R['stories']=len(ST)
ids=collections.Counter(x['id'] for x in ST); R['dup_story_ids']=[x for x,c in ids.items() if c>1]
AS=H+'SuccessStories/website/'
for x in ST:
    for f in ('photo','orgLogo'):
        v=x.get(f)
        if v and not v.startswith('http') and not os.path.exists(AS+v): R['missing_'+f].append((x['id'],v))
    if not x.get('photo'): R['no_photo'].append(x['id'])
    if not x.get('orgLogo'): R['no_logo'].append(x['id'])
    if not x.get('provenance'): R['no_prov'].append(x['id'])
    refs=[int(m) for m in re.findall(r'#(\d{1,4})\b',x.get('provenance',''))]
    for ref in refs:
        if ref>N: R['prov_out_of_range'].append((x['id'],ref)); continue
        tok=[t for t in re.split(r'\s+',x['name']) if len(t)>2][:1]
        rn=g[ref-1]['n']+' '+(g[ref-1].get('alias') or '')+' '+(g[ref-1].get('en') or '')
        if tok and tok[0] not in rn: R['prov_name_mismatch'].append((x['id'],x['name'],ref,g[ref-1]['n']))
    if not refs: R['prov_no_ref'].append(x['id'])
R['story_keys']=sorted({k for x in ST for k in x})
emp=collections.Counter((x.get('org') or x.get('employer') or '').strip() for x in ST)
R['story_org_count']=len([e for e in emp if e])
R['story_years']=sorted(collections.Counter(x['year'] for x in ST).items())
R['quote_kinds']=collections.Counter((x.get('quote') or {}).get('kind') for x in ST).most_common()
# ---------- 8. counters ----------
T=collections.Counter(r['tr'] for r in g); wl=sum(1 for r in g if r['links']); uu=len({l[1].rstrip('/') for r in g for l in r['links']})
R['counts']=dict(N=N,T=dict(T),wl=wl,uu=uu)
for k,v in R.items():
    if isinstance(v,list) and len(v)>12: print(k,len(v),v[:12])
    else: print(k,v)
print('FIX',dict(FIX))
if APPLY:
    for k,r in enumerate(g,1):
        row=k+1
        for col,f in ((2,'n'),(3,'en'),(4,'prog'),(6,'co'),(7,'emp'),(8,'role')):
            cur=ws.cell(row,col).value
            if isinstance(cur,str) and cur.strip()!=(r.get(f) or ''):
                if re.sub(r'\s+',' ',cur).strip().replace('**','')==(r.get(f) or ''): ws.cell(row,col).value=r.get(f) or None
        for col in (15,16,17,18,19,20):
            cur=ws.cell(row,col).value
            if isinstance(cur,str) and 'http' in cur:
                nv=re.sub(r'https?://[^\s·]+',lambda m:canon(m.group(0)),cur)
                if nv!=cur: ws.cell(row,col).value=nv
    json.dump({k:(v if not isinstance(v,collections.Counter) else dict(v)) for k,v in R.items()},open(H+'Graduates/tools/round_2026-10-15/qa_report.json','w',encoding='utf-8'),ensure_ascii=False,indent=1,default=str)
    s=s[:i]+json.dumps(D,ensure_ascii=False)+';'+s[j:]; open(P,'w',encoding='utf-8').write(s)
    wb.save(X_); print('applied')
