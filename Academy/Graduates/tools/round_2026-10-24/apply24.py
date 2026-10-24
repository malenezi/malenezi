# -*- coding: utf-8 -*-
# Round 21 Oct 2026 — LinkedIn content (mentionsOrganization) + people search + GitHub sweep; avatars localised; 8 employer logos
# Inputs (same folder): new21.json, enr21.json, stories21.json.  Dry run by default; --apply writes.  --emp N = new named employers.
import json,re,os,sys,shutil,collections
sys.path[:0]=[os.path.expanduser('~/mnt/Academy/Graduates/tools/round_2026-10-07'),os.path.expanduser('~/mnt/Academy/Graduates/tools')]
import translit as TR, openpyxl
DRY='--apply' not in sys.argv
H=os.path.expanduser('~/mnt/Academy/'); B='backup-2026-10-24'; T=H+'Graduates/tools/round_2026-10-24/'
DATE='24 أكتوبر 2026'; TAG='[جولة 24 أكتوبر 2026] '
TL=' تنويه: الاسم العربي نقل حرفي عن الاسم اللاتيني المنشور — غير متحقق علنًا.'
TRN={'ai':'مهندس ذكاء اصطناعي — AI Engineer','ds':'عالم بيانات — Data Scientist','other':'برامج متخصصة أخرى — Other / Specialized','dmg':'إدارة وحوكمة البيانات — Data Management & Governance','genai':'أكاديمية الذكاء الاصطناعي التوليدي — Gen AI Academy','coop':'التدريب التعاوني — Cooperative Training (COOP)'}
def rep(s,a,b,count=None):
    n=s.count(a); assert n>=1,('missing',a[:90])
    if count is not None: assert n==count,(a[:90],n)
    return s.replace(a,b)
def rrep(s,pat,b,count=1,flags=0):
    s2,n=re.subn(pat,b,s,flags=flags); assert n==count,(pat,n); return s2
FILES=['SuccessStories/website/js/data.js','SuccessStories/website/index.html','index.html','Graduates/index.html','Graduates/Graduates_Database.xlsx','Graduates/Graduates_Database.md']
BK=H+'_backups/2026-10-24/'
if not DRY:
    os.makedirs(BK,exist_ok=True)
    for f in FILES:
        t=BK+f.replace('/','__')
        if not os.path.exists(t): shutil.copy2(H+f,t)
P=H+'Graduates/index.html'; s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+len('const DATA = '); j=s.index('\nconst SITE_STATS')
D=json.loads(s[i:j].rstrip()[:-1]); g=D['grads']; N0=len(g); assert N0==3537,N0
head=s[:i]; tail=s[j:]
T0=collections.Counter(r['tr'] for r in g); wl0=sum(1 for r in g if r.get('links')); uu0=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
X_=H+'Graduates/Graduates_Database.xlsx'; wb=openpyxl.load_workbook(X_); ws=wb['قاعدة البيانات']
assert ws.cell(N0+1,1).value==N0
norm=lambda u:re.sub(r'^https?://(www\.|[a-z]{2}\.)?','',u).rstrip('/').lower()
ALL={norm(l[1]) for r in g for l in r['links']}
def note(k,t):
    g[k-1]['d']+=' '+TAG+t; ws.cell(k+1,21).value=(ws.cell(k+1,21).value or '')+' '+TAG+t
def setf(k,field,col,val):
    g[k-1][field]=val; ws.cell(k+1,col).value=val
def addlink(k,label,url):
    G=g[k-1]
    if any(norm(l[1])==norm(url) for l in G['links']): return False
    if norm(url) in ALL: print('  skip link (on another record)',k,url); return False
    G['links'].append([label,url]); ALL.add(norm(url)); col=15 if 'linkedin.com' in url else 16
    cur=ws.cell(k+1,col).value; ws.cell(k+1,col).value=(cur+' · ' if cur else '')+url; return True
NEW=json.load(open(T+'new24.json',encoding='utf-8'))
DNOTE={}
ENR=json.load(open(T+'enr24.json',encoding='utf-8'))
ST=json.load(open(T+'stories24.json',encoding='utf-8'))
idx=TR.build_index(g); new_ids=[]; MATCHLOG=[]
catl={'program':'برنامج','project':'مشروع','cert':'شهادة','job':'توظيف','story':'قصة نجاح'}
for row in NEW:
    ar,en,prog,co,tr,score,lv,links,src,d,cats,emp,role,tl=row
    assert tr in TRN,(en,tr)
    m={x[0] for x in TR.match(ar,en,idx)}
    ex={k+1 for k,r in enumerate(g) if (r.get('en') or '').lower()==en.lower() or r['n']==ar}
    MATCHLOG.append((en,sorted(m|ex)))
    for l in links: assert norm(l[1]) not in ALL,(en,l)
    rid=len(g)+1; rr=rid+1; dd=TAG+d+DNOTE.get(en,'')+(TL if tl else '')
    rec={"n":ar,"en":en,"lv":lv,"score":score,"prog":prog,"co":co,"win":"ضمن النطاق","edu":"","emp":emp,"role":role,"cats":[c for c in cats if c!='story'],"d":dd,"links":links,"src":src,"tr":tr}
    g.append(rec); new_ids.append(rid)
    for l in links: ALL.add(norm(l[1]))
    li=' · '.join(l[1] for l in links if 'linkedin.com' in l[1]) or None; gh=' · '.join(l[1] for l in links if 'github.com' in l[1]) or None
    vals=[rid,ar,en,prog,TRN[tr],co,emp or None,role or None,None,None,lv,score,'ضمن النطاق',' · '.join(catl[c] for c in rec['cats']),li,gh,None,None,None,None,dd,None,src]
    for ci,v in enumerate(vals,1): ws.cell(rr,ci).value=v
LOG=collections.Counter()
for e in ENR:
    k=e['k']; assert e['en']=='' or g[k-1]['en'].lower()==e['en'].lower(),(k,g[k-1]['en'],e['en'])
    if e.get('set_en') and not g[k-1]['en']: setf(k,'en',3,e['set_en'])
    for lab,u in e.get('links',[]):
        if addlink(k,lab,u): LOG['link']+=1
    if e.get('co'): setf(k,'co',6,e['co'])
    if e.get('prog_set'): setf(k,'prog',4,e['prog_set'])
    if e.get('score_set'): setf(k,'score',12,e['score_set'])
    if e.get('prog_add'):
        G=g[k-1]; G['prog']+=' + '+e['prog_add']; ws.cell(k+1,4).value=G['prog']
    for c in e.get('cats_add',[]):
        if c not in g[k-1]['cats']: g[k-1]['cats'].append(c)
    note(k,e['t']); LOG['enr']+=1
stories=[]
LI='https://www.linkedin.com/in/'
for p in ST:
    if p['i'] is None:
        hit=[k for k in new_ids if g[k-1]['en'].lower()==p['nameEn'].lower()]; assert len(hit)==1,(p['nameEn'],hit); p['i']=hit[0]
    G=g[p['i']-1]; assert G['en'].lower()==p['nameEn'].lower(),(p['i'],G['en'])
    st={"id":p['id'],"year":p['year'],"quote":{"text":p['quote'],"textEn":p['quoteEn'],"kind":"draft"},"name":p['name'],"nameEn":p['nameEn'],"photo":p.get('photo'),
        "role":p['role'],"org":p['org'],"orgLogo":p.get('orgLogo'),"program":p['program'],"period":p['period'],
        "category":"employment","categories":["employment"],"impact":p['impact'],"story":p['story'],"achievements":p['ach'],
        "links":[{"label":"LinkedIn","url":LI+p['slug']+'/'}],
        "provenance":f"صفحة الخبرة على LinkedIn بحساب مسجَّل (قُرئت {DATE})، بتواريخ بمستوى الشهر: {p['exp']} + سجل الأكاديمية #{p['i']}."}
    if st['orgLogo'] is None: del st['orgLogo']
    stories.append(st)
    if not G.get('emp'): G['emp']=p['org']; G['role']=p['role_db']; ws.cell(p['i']+1,7).value=p['org']; ws.cell(p['i']+1,8).value=p['role_db']
    if 'job' not in G['cats']: G['cats'].append('job')
    note(p['i'],p['note'])
NS=len(stories); S0=193; S1=S0+NS; E0=105; E1=E0+int(sys.argv[sys.argv.index('--emp')+1]) if '--emp' in sys.argv else E0
N=len(g); TT=collections.Counter(r['tr'] for r in g)
wl=sum(1 for r in g if r.get('links')); uu=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
print('N',N0,'->',N,{k:(T0[k],TT[k]) for k in TT},'wl',wl0,'->',wl,'uu',uu0,'->',uu,dict(LOG),'new',new_ids[:1],'-',new_ids[-1:],'stories',S1,'emp',E1)
for en,m in MATCHLOG:
    if m: print('  match',en,m)
for t in [json.dumps(x,ensure_ascii=False) for x in stories]+[g[e['k']-1]['d'] for e in ENR]+[g[k-1]['d'] for k in new_ids]: assert '**' not in t
if DRY: sys.exit(0)
T=TT
TOT=format(N,','); OTOT=format(N0,',')
def stc(t):
    t=t.replace(OTOT,TOT)
    for a,b in (('%d قصة'%S0,'%d قصة'%S1),('%d stories'%S0,'%d stories'%S1),('%d verified success stories'%S0,'%d verified success stories'%S1)):
        t=t.replace(a,b)
    if E1!=E0:
        for a,b in (('%d جهة عمل'%E0,'%d جهة عمل'%E1),('%d employers'%E0,'%d employers'%E1)): t=t.replace(a,b)
    return t
head=stc(head); tail=stc(tail)
tail=rep(tail,"{ value: %d, label: 'سجلًا فرديًا',"%N0,"{ value: %d, label: 'سجلًا فرديًا',"%N,1)
EN={'ai':'AI Engineer','ds':'Data Scientist','dmg':'Data Management & Governance','other':'Other / Specialized','genai':'Gen AI Academy','coop':'Cooperative Training (COOP)'}
for k,en in EN.items():
    if T[k]!=T0[k]:
        tail,n=re.subn(r"(en: '%s', value: )%d\b"%(re.escape(en),T0[k]),"\\g<1>%d"%T[k],tail); print('tail',k,n); assert n>=1
tail=rrep(tail,r"\{ value: %d,(\s+)label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(wl0,format(uu0,',')),"{ value: %d,\\1label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(wl,format(uu,',')))
tail=rep(tail,"noteEn: '%s unique source links'"%format(uu0,','),"noteEn: '%s unique source links'"%format(uu,','),1)
tail,n=re.subn(r"(\{ value: )%d(,\s+label: 'قصة نجاح)"%S0,r"\g<1>%d\2"%S1,tail); print('grad story kpi',n)
D['grads']=g; open(P,'w',encoding='utf-8').write(head+json.dumps(D,ensure_ascii=False)+';'+tail)
P2=H+'index.html'; s=stc(open(P2,encoding='utf-8').read())
s=rep(s,'data-count="%d"'%N0,'data-count="%d"'%N,1); s=rep(s,'data-count="%d"'%S0,'data-count="%d"'%S1,1)
if E1!=E0: s=rep(s,'data-count="%d"'%E0,'data-count="%d"'%E1,1)
for k in ('ai','ds','dmg','other','genai','coop'):
    pc='%.1f'%(100*T[k]/N)
    pat=r'(data-count=")%d(">0</div>.*?--w:)[\d.]+(%%.*?data-ar=")[\d.]+(%% من السجل" data-en=")[\d.]+(%% of the registry")'%T0[k]
    s,n=re.subn(pat,lambda mm:mm.group(1)+str(T[k])+mm.group(2)+pc+mm.group(3)+pc+mm.group(4)+pc+mm.group(5),s,count=1,flags=re.S); assert n==1,k
open(P2,'w',encoding='utf-8').write(s)
P3=H+'SuccessStories/website/js/data.js'; s=open(P3,encoding='utf-8').read()
s=rep(s,"{ value: %d, label: 'خريجًا موثّقًا',"%N0,"{ value: %d, label: 'خريجًا موثّقًا',"%N,1)
for k,en in EN.items():
    if T[k]!=T0[k]: s=rrep(s,r"(en: '%s',\s+value: )%d\b"%(re.escape(en),T0[k]),"\\g<1>%d"%T[k])
s=rrep(s,r"(\{ value: )%d(,\s+label: 'قصة نجاح)"%S0,r"\g<1>%d\2"%S1)
if E1!=E0: s=rrep(s,r"(\{ value: )%d(,\s+label: 'جهة عمل')"%E0,r"\g<1>%d\2"%E1)
k=s.index('const STORIES = ['); e=s.index('\n];',k)
prev=s[:e].rstrip()
if not prev.endswith(','): prev+=','
if stories: s=prev+'\n'+',\n'.join('  '+json.dumps(x,ensure_ascii=False) for x in stories)+s[e:]
s=rep(s,"'use strict';","/* %s: مسح خريجي يناير 2023 – أبريل 2026 (بحث الأشخاص في LinkedIn وصفحات الخبرة) — %s ← %s خريجًا (%d سجلًا جديدًا · %d إثراء)؛ القصص %d ← %d (%s)؛ جهات العمل %d. */\n'use strict';"%(DATE,OTOT,TOT,len(new_ids),LOG['enr'],S0,S1,' · '.join(x['id'] for x in stories),E1),1)
WIRE=[]
for sid,fld,val in WIRE:
    assert os.path.exists(H+'SuccessStories/website/'+val),val
    m=re.search(r'\{\s*"id": "%s"[^\n]*'%re.escape(sid),s); assert m,sid; line=m.group(0)
    m2=re.search(r'"%s": (?:"[^"]*"|null)'%fld,line)
    if m2: nl=line.replace(m2.group(0),'"%s": "%s"'%(fld,val),1)
    else: nl=line.replace('"photo":','"%s": "%s", "photo":'%(fld,val),1)
    assert nl!=line,sid; s=s.replace(line,nl,1)
open(P3,'w',encoding='utf-8').write(s)
P4=H+'SuccessStories/website/index.html'; s=open(P4,encoding='utf-8').read(); s=rep(s,'"numberOfItems": %d'%S0,'"numberOfItems": %d'%S1,1); open(P4,'w',encoding='utf-8').write(s)
hi=sum(1 for r in g if r.get('score',0)>=75); mid=sum(1 for r in g if 45<=r.get('score',0)<75); lo=N-hi-mid
emp=sum(1 for r in g if r.get('emp')); yc=collections.Counter()
for r in g:
    ys=set(re.findall(r'20(2[1-6])',r.get('co') or ''))
    if not ys: yc['none']+=1
    for y in ys: yc['20'+y]+=1
st=wb['إحصاءات']
M={'الإجمالي':TOT,'مهندس ذكاء اصطناعي':T['ai'],'عالم بيانات':T['ds'],'أكاديمية الذكاء الاصطناعي التوليدي':T['genai'],'إدارة وحوكمة البيانات':T['dmg'],'التدريب التعاوني':T['coop'],'برامج متخصصة أخرى':T['other'],
   'ثقة مرتفعة (≥75)':hi,'ثقة متوسطة (45–74)':mid,'ثقة منخفضة (<45)':lo,'سجلات بجهة عمل موثّقة':emp,'سجلات بروابط تحقق علنية':wl,'روابط مصدر فريدة':uu,
   'سجلات بدفعة 2021':yc['2021'],'سجلات بدفعة 2022':yc['2022'],'سجلات بدفعة 2023':yc['2023'],'سجلات بدفعة 2024':yc['2024'],'سجلات بدفعة 2025':yc['2025'],'سجلات بدفعة 2026':yc['2026'],'سجلات بلا دفعة محددة':yc['none'],
   'تحديث':f'{DATE} — مسح خريجي يناير 2023 – أبريل 2026: {len(new_ids)} سجلًا جديدًا ({OTOT} → {TOT})؛ {LOG["enr"]} إثراء؛ القصص {S0} → {S1}؛ جهات العمل {E1}'}
for row in st.iter_rows():
    if row[0].value in M: row[1].value=M[row[0].value]
sh=wb.create_sheet('جولة_24_أكتوبر_2026'); sh.append(['#','الاسم','النوع','التفصيل'])
for k in new_ids: sh.append([k,g[k-1]['n'],('سجل جديد (GitHub)' if g[k-1]['lv'].startswith('gh') else 'سجل جديد (LinkedIn)'),g[k-1]['prog']+' — '+g[k-1]['co']])
for e in ENR: sh.append([e['k'],g[e['k']-1]['n'],'إثراء',e['t'][:140]])
for x,p in zip(stories,ST): sh.append([p['i'],x['name'],'قصة جديدة',x['org']+' — '+x['role']])
wb.save(X_)
P5=H+'Graduates/Graduates_Database.md'; s=open(P5,encoding='utf-8').read()
s=rep(s,'**الإصدار:** 21 أكتوبر 2026 (ب) — ','**الإصدار:** %s — مسح خريجي يناير 2023 – أبريل 2026 (%s → %s · القصص %d · جهات العمل %d). قبله: 21 أكتوبر 2026 (ب) — '%(DATE,OTOT,TOT,S1,E1),1)
san=lambda x:(x or '').replace('|','/')
L=['## جولة مسح خريجي يناير 2023 – أبريل 2026 — %s'%DATE,'',f'**الخريجون {OTOT} → {TOT} · القصص {S0} → {S1} · جهات العمل {E1}.**','',
 f'**1) سجلات جديدة ({len(new_ids)}):** بحث الأشخاص في LinkedIn بعبارات «Bootcamp at SDAIA» و«Trainee at SDAIA» و«Coop Trainee SDAIA» و«SDAIA Academy trainee»، ثم صفحة الخبرة لكل مرشح لتثبيت البرنامج والتاريخ بمستوى الشهر. نحو 85٪ من النتائج موجودة مسبقًا. ثلاثة سجلات (علي الجنبي، أثير أ.، أفراح المطيري) من 2021–2022 خارج النافذة أُضيفت لثبوتها.','','| # | الاسم | الاسم الإنجليزي | البرنامج | الدفعة | المسار | المصدر |','|---|---|---|---|---|---|---|']
for k in new_ids:
    G_=g[k-1]; L.append(f"| {k} | {san(G_['n'])} | {san(G_['en'])} | {san(G_['prog'])} | {san(G_['co'])} | {G_['tr']} | {G_['links'][0][1] if G_['links'] else ''} |")
L+=['',f"**2) الإثراء ({LOG['enr']}):** "+' · '.join('#%d %s'%(e['k'],g[e['k']-1]['n']) for e in ENR)+'.','',
 '**3) قصص النجاح ('+str(NS)+'):** '+' · '.join(x['id'] for x in stories)+'. معلّقة: رويدا الشهري (حوكمة البيانات ← تحليلات متقدمة في هيئة الزكاة، ارتباط غير محسوم). محتجزة: عبدالله البدراني (معسكر مبرمجي المستقبل، بدء ديسمبر 2022 بلا إتمام)، علي الغامدي (Trainee مارس–يونيو 2024 بلا اسم برنامج).','','---','']
k=re.search(r'\n## ',s).start()+1
s=s[:k]+'\n'.join(L)+'\n'+s[k:]
open(P5,'w',encoding='utf-8').write(s)
for f in ('index.html','Graduates/index.html'):
    t=open(H+f,encoding='utf-8').read(); print(f,'leftover',OTOT,t.count(OTOT),'%d قصة'%S0,t.count('%d قصة'%S0),'new',t.count(TOT))
print('done',S1,E1)
