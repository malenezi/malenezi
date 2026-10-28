# -*- coding: utf-8 -*-
# Round 28 Oct 2026 — NCA-ADS (new GenAI Academy track) + NVIDIA/PE/MDE/Agentic/AdvML sweep (LinkedIn content + GitHub), enrichments, QA.
import json,re,os,sys,shutil,collections,openpyxl
DRY='--apply' not in sys.argv
H=os.path.expanduser('~/mnt/Academy/'); T=H+'Graduates/tools/round_2026-10-28/'
DATE='28 أكتوبر 2026'; TAG='[جولة 28 أكتوبر 2026] '
TL=' تنويه: الاسم العربي نقل حرفي عن الاسم اللاتيني المنشور — غير متحقق علنًا.'
TRN={'ai':'مهندس ذكاء اصطناعي — AI Engineer','ds':'عالم بيانات — Data Scientist','other':'برامج متخصصة أخرى — Other / Specialized','dmg':'إدارة وحوكمة البيانات — Data Management & Governance','genai':'أكاديمية الذكاء الاصطناعي التوليدي — Gen AI Academy','coop':'التدريب التعاوني — Cooperative Training (COOP)'}
def rep(s,a,b,count=None):
    n=s.count(a); assert n>=1,('missing',a[:90])
    if count is not None: assert n==count,(a[:90],n)
    return s.replace(a,b)
def rrep(s,pat,b,count=1,flags=0):
    s2,n=re.subn(pat,b,s,flags=flags); assert n==count,(pat,n); return s2
FILES=['SuccessStories/website/js/data.js','SuccessStories/website/index.html','index.html','Graduates/index.html','Graduates/Graduates_Database.xlsx','Graduates/Graduates_Database.md']
BK=H+'_backups/2026-10-28/'
if not DRY:
    os.makedirs(BK,exist_ok=True)
    for f in FILES:
        t=BK+f.replace('/','__')
        if not os.path.exists(t): shutil.copy2(H+f,t)
X=json.load(open(T+'data28.json',encoding='utf-8'))
P=H+'Graduates/index.html'; s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+len('const DATA = '); j=s.index('\nconst SITE_STATS')
D=json.loads(s[i:j].rstrip()[:-1]); g=D['grads']; N0=len(g); assert N0==3904,N0
head=s[:i]; tail=s[j:]
T0=collections.Counter(r['tr'] for r in g); wl0=sum(1 for r in g if r.get('links')); uu0=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
X_=H+'Graduates/Graduates_Database.xlsx'; wb=openpyxl.load_workbook(X_); ws=wb['قاعدة البيانات']; assert ws.cell(N0+1,1).value==N0
norm=lambda u:re.sub(r'^https?://(www\.|[a-z]{2}\.)?','',u).rstrip('/').lower()
ALL={norm(l[1]) for r in g for l in r['links']}
def note(k,t):
    g[k-1]['d']=(g[k-1]['d']+' '+TAG+t).strip(); ws.cell(k+1,21).value=((ws.cell(k+1,21).value or '')+' '+TAG+t).strip()
def addlink(k,label,url):
    G=g[k-1]
    if any(norm(l[1])==norm(url) for l in G['links']): return False
    assert norm(url) not in ALL,('link on another record',k,url)
    G['links'].append([label,url]); ALL.add(norm(url)); col=15 if 'linkedin.com' in url else 16
    cur=ws.cell(k+1,col).value; ws.cell(k+1,col).value=(cur+' · ' if cur else '')+url; return True
def progadd(k,pa):
    if pa in g[k-1]['prog']: return
    g[k-1]['prog']+=' + '+pa; ws.cell(k+1,4).value=g[k-1]['prog']
new_ids=[]; LOG=collections.Counter(); SLUG2ID={}
exist_en={(r.get('en') or '').lower().replace(' ','') for r in g}
LI='https://www.linkedin.com/in/'
for ar,en,links,prog,co,tr,score,d,tl,ad in X['new']:
    assert ad or en.lower().replace(' ','') not in exist_en,('dup en',en)
    slug=en
    for l in links: assert norm(l[1]) not in ALL,(en,l)
    rid=len(g)+1; rr=rid+1; dd=TAG+d+(TL if tl else '')
    rec={"n":ar,"en":en,"lv":"li1028","score":score,"prog":prog,"co":co,"win":"ضمن النطاق","edu":"","emp":"","role":"","cats":["program"],"d":dd,"links":links,"src":("LinkedIn (حساب مسجَّل) — بحث المنشورات: NCA-ADS / NCA-GENL / NVIDIA+سدايا / SDAIA Academy (آخر أسبوع–شهر)" if "linkedin" in links[0][1] else "GitHub — بحث المستودعات «SDAIA Academy» المنشأة بعد 10 أكتوبر 2026 وتفريعات SDAIAAcademy/agentic-ai")+" — جولة 28 أكتوبر 2026","tr":tr}
    g.append(rec); new_ids.append(rid); exist_en.add(en.lower().replace(' ','')); SLUG2ID[slug]=rid
    for l in links: ALL.add(norm(l[1]))
    lic=' · '.join(u for _,u in links if 'linkedin.com/in/' in u) or None; oth=' · '.join(u for _,u in links if 'linkedin.com/in/' not in u) or None
    vals=[rid,ar,en,prog,TRN[tr],co,None,None,None,None,'li1028',score,'ضمن النطاق','برنامج',lic,oth,None,None,None,None,dd,None,rec['src']]
    for ci,v in enumerate(vals,1): ws.cell(rr,ci).value=v
NOHA=SLUG2ID['Noha Alshehri']
for e in X['enr']:
    e['t']=e['t'].replace('%NOHA%',str(NOHA)); k=e['k']
    for lab,u in e.get('links',[]):
        if addlink(k,lab,u): LOG['link']+=1
    if e.get('prog_add'): progadd(k,e['prog_add']); LOG['prog_add']+=1
    if e.get('en') and not g[k-1].get('en'): g[k-1]['en']=e['en']; ws.cell(k+1,3).value=e['en']
    note(k,e['t']); LOG['enr']+=1
dj=H+'SuccessStories/website/js/data.js'; sj=open(dj,encoding='utf-8').read()
stories=[]
for p in X['stories']:
    slug=[n[2] for n in X['new'] if n[1]==p['en']][0]; k=SLUG2ID[slug]; G=g[k-1]
    assert ('"id": "%s"'%p['slug']) not in sj
    st={"id":p['slug'],"year":p['year'],"quote":{"text":p['q'],"textEn":p['qe'],"kind":"draft"},"name":G['n'],"nameEn":G['en'],"photo":None,"role":p['role'],"org":p['org'],"program":G['prog'],"period":G['co'],"category":"employment","categories":["employment"],"impact":p['impact'],"story":p['story'],"achievements":p['ach'],"links":[{"label":"LinkedIn","url":LI+slug+'/'}],"provenance":f"صفحة الخبرة على LinkedIn بحساب مسجَّل (قُرئت {DATE})، بتواريخ بمستوى الشهر: {p['exp']} + سجل الأكاديمية #{k}."}
    stories.append(st)
    G['cats'].append('job'); G['emp']=p['org']; G['role']=p['role']; ws.cell(k+1,7).value=p['org']; ws.cell(k+1,8).value=p['role']
    note(k,'نُشرت قصة نجاح «%s» وفق السياسة v1.0 (معيار 14 شهرًا): %s'%(p['slug'],p['ach'][0]))
orgs0=set(re.findall(r'"org": "([^"]+)"',sj)); newemp=sorted({p['org'] for p in X['stories']}-orgs0)
N=len(g); TT=collections.Counter(r['tr'] for r in g); wl=sum(1 for r in g if r.get('links')); uu=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
for t in [json.dumps(x,ensure_ascii=False) for x in stories]+[r['d'] for r in g]: assert '**' not in t
S0=209; S1=S0+len(stories); E0=113; E1=E0+len(newemp)
print('N',N0,'->',N,{k:(T0[k],TT[k]) for k in TT},'wl',wl0,wl,'uu',uu0,uu,dict(LOG),'new',new_ids[0],'-',new_ids[-1],'stories',S1,'emp',E1,newemp)
if DRY: sys.exit(0)
T=TT; TOT=format(N,','); OTOT=format(N0,',')
def stc(t):
    t=t.replace(OTOT,TOT)
    for a,b in (('%d قصة'%S0,'%d قصة'%S1),('%d stories'%S0,'%d stories'%S1),('%d verified success stories'%S0,'%d verified success stories'%S1),('%d جهة عمل'%E0,'%d جهة عمل'%E1),('%d employers'%E0,'%d employers'%E1)):
        t=t.replace(a,b)
    return t
head=stc(head); tail=stc(tail)
tail=rep(tail,"{ value: %d, label: 'سجلًا فرديًا',"%N0,"{ value: %d, label: 'سجلًا فرديًا',"%N,1)
EN={'ai':'AI Engineer','ds':'Data Scientist','dmg':'Data Management & Governance','other':'Other / Specialized','genai':'Gen AI Academy','coop':'Cooperative Training (COOP)'}
for k,en in EN.items():
    if T[k]!=T0[k]:
        tail,n=re.subn(r"(en: '%s', value: )%d\b"%(re.escape(en),T0[k]),"\\g<1>%d"%T[k],tail); assert n>=1,k
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
s=sj
s=rep(s,"{ value: %d, label: 'خريجًا موثّقًا',"%N0,"{ value: %d, label: 'خريجًا موثّقًا',"%N,1)
for k,en in EN.items():
    if T[k]!=T0[k]: s=rrep(s,r"(en: '%s',\s+value: )%d\b"%(re.escape(en),T0[k]),"\\g<1>%d"%T[k])
s=rrep(s,r"(\{ value: )%d(,\s+label: 'قصة نجاح)"%S0,r"\g<1>%d\2"%S1)
if E1!=E0: s=rrep(s,r"(\{ value: )%d(,\s+label: 'جهة عمل')"%E0,r"\g<1>%d\2"%E1)
if stories:
    k=s.index('const STORIES = ['); e=s.index('\n];',k); prev=s[:e].rstrip()
    if not prev.endswith(','): prev+=','
    s=prev+'\n'+',\n'.join('  '+json.dumps(x,ensure_ascii=False) for x in stories)+s[e:]
s=rep(s,"'use strict';","/* %s: مسار NCA-ADS الجديد ومسح المنشورات والمستودعات — %s ← %s خريجًا (%d جديدًا · %d إثراء)؛ القصص %d؛ جهات العمل %d. */\n'use strict';"%(DATE,OTOT,TOT,len(new_ids),LOG['enr'],S1,E1),1)
open(dj,'w',encoding='utf-8').write(s)
P4=H+'SuccessStories/website/index.html'; t=open(P4,encoding='utf-8').read(); t=rep(t,'"numberOfItems": %d'%S0,'"numberOfItems": %d'%S1,1); open(P4,'w',encoding='utf-8').write(t)
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
   'تحديث':f'{DATE} — مسار NCA-ADS ومسح أكتوبر 2026: {len(new_ids)} سجلًا جديدًا ({OTOT} → {TOT})؛ {LOG["enr"]} إثراء؛ القصص {S1}؛ جهات العمل {E1}'}
for row in st.iter_rows():
    if row[0].value in M: row[1].value=M[row[0].value]
sh=wb.create_sheet('جولة_28_أكتوبر_2026'); sh.sheet_view.rightToLeft=True; sh.append(['#','الاسم','النوع','التفصيل'])
for k in new_ids: sh.append([k,g[k-1]['n'],'سجل جديد (li1028)',g[k-1]['prog'][:90]+' — '+g[k-1]['co']])
for e in X['enr']: sh.append([e['k'],g[e['k']-1]['n'],'إثراء',e['t'][:200]])
for p in stories: sh.append([SLUG2ID[[n[2] for n in X['new'] if n[1]==p['nameEn']][0]],p['name'],'قصة جديدة',p['org']+' — '+p['role']])
wb.save(X_)
P5=H+'Graduates/Graduates_Database.md'; s=open(P5,encoding='utf-8').read()
s=rrep(s,r'\*\*الإصدار:\*\* ',f'**الإصدار:** {DATE} — مسار NCA-ADS ومسح أكتوبر 2026 ({OTOT} → {TOT} · القصص {S1} · جهات العمل {E1}). قبله: ',1)
L=['## مسار NCA-ADS الجديد ومسح أكتوبر 2026 — %s'%DATE,'',f'**الخريجون {OTOT} → {TOT} · القصص {S1} · جهات العمل {E1}.** أُضيف مسار «NVIDIA-Certified Associate: Accelerated Data Science (NCA-ADS)» ضمن أكاديمية الذكاء الاصطناعي التوليدي. السجلات الجديدة #{new_ids[0]}–#{new_ids[-1]}: 4 شهادات NVIDIA NCA-GENL، و3 هندسة الأوامر والاستخدام المسؤول، و2 هندسة الأنظمة الوكيلية (SDA-AIE-311)، و1 هندسة البيانات الحديثة، و1 أساليب تعلم الآلة المتقدمة. إثراء {LOG["enr"]} سجلات، منها أول خريجة NCA-ADS (#3076). لا قصص جديدة.','','---','']
k=re.search(r'\n## ',s).start()+1; s=s[:k]+'\n'.join(L)+'\n'+s[k:]; open(P5,'w',encoding='utf-8').write(s)
for f in ('index.html','Graduates/index.html'):
    t=open(H+f,encoding='utf-8').read(); print(f,'leftover',OTOT,t.count(OTOT),'new',t.count(TOT))
print('done',dict(LOG))
