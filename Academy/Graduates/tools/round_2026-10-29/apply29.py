# -*- coding: utf-8 -*-
# Round 29 Oct 2026 — supplied posts (9) + Oct 2023–Jun 2026 sweep + gap-closing experience reads + 4 stories.
import json,re,os,sys,shutil,collections,openpyxl
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from data29 import NEW,ENR,STORIES
DRY='--apply' not in sys.argv
H=os.path.expanduser('~/mnt/Academy/')
DATE='29 أكتوبر 2026'; TAG='[جولة 29 أكتوبر 2026] '
TL=' تنويه: الاسم العربي نقل حرفي عن الاسم اللاتيني المنشور — غير متحقق علنًا.'
TRN={'ai':'مهندس ذكاء اصطناعي — AI Engineer','ds':'عالم بيانات — Data Scientist','other':'برامج متخصصة أخرى — Other / Specialized','dmg':'إدارة وحوكمة البيانات — Data Management & Governance','genai':'أكاديمية الذكاء الاصطناعي التوليدي — Gen AI Academy','coop':'التدريب التعاوني — Cooperative Training (COOP)'}
EN={'ai':'AI Engineer','ds':'Data Scientist','dmg':'Data Management & Governance','other':'Other / Specialized','genai':'Gen AI Academy','coop':'Cooperative Training (COOP)'}
def rep(s,a,b,count=None):
    n=s.count(a); assert n>=1,('missing',a[:90])
    if count is not None: assert n==count,(a[:90],n)
    return s.replace(a,b)
def rrep(s,pat,b,count=1,flags=0):
    s2,n=re.subn(pat,b,s,flags=flags); assert n==count,(pat,n); return s2
FILES=['SuccessStories/website/js/data.js','SuccessStories/website/index.html','index.html','Graduates/index.html','Graduates/Graduates_Database.xlsx','Graduates/Graduates_Database.md','about.html','Catalog/index.html']
BK=H+'_backups/2026-10-29/'
if not DRY:
    os.makedirs(BK,exist_ok=True)
    for f in FILES:
        t=BK+f.replace('/','__')
        if not os.path.exists(t): shutil.copy2(H+f,t)
P_=H+'Graduates/index.html'; s=open(P_,encoding='utf-8').read()
i=s.index('const DATA = ')+len('const DATA = '); j=s.index('\nconst SITE_STATS')
D=json.loads(s[i:j].rstrip()[:-1]); g=D['grads']; N0=len(g); assert N0==3915,N0
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
    G['links'].append([label,url]); ALL.add(norm(url)); col=15 if 'linkedin.com/in/' in url else 16
    cur=ws.cell(k+1,col).value; ws.cell(k+1,col).value=(cur+' · ' if cur else '')+url; return True
LOG=collections.Counter(); new_ids=[]
exist_en={(r.get('en') or '').lower().replace(' ','') for r in g}
for ar,en,links,prog,co,tr,score,d,emp,role in NEW:
    assert en.lower().replace(' ','') not in exist_en,('dup en',en)
    for l in links: assert norm(l[1]) not in ALL,(en,l)
    rid=len(g)+1; rr=rid+1; dd=TAG+d+TL
    src='LinkedIn (حساب مسجَّل) — '+('منشورات زوّد بها أ. د. ممدوح العنزي' if 'زوّد به' in d else 'بحث المنشورات حسب البرامج (مسح أكتوبر 2023 – يونيو 2026 والأحدث)')+' — جولة 29 أكتوبر 2026'
    rec={"n":ar,"en":en,"lv":"li1029","score":score,"prog":prog,"co":co,"win":"ضمن النطاق","edu":"","emp":emp,"role":role,"cats":["program"],"d":dd,"links":links,"src":src,"tr":tr}
    g.append(rec); new_ids.append(rid); exist_en.add(en.lower().replace(' ',''))
    for l in links: ALL.add(norm(l[1]))
    lic=' · '.join(u for _,u in links if 'linkedin.com/in/' in u) or None
    oth=' · '.join(u for _,u in links if 'linkedin.com/in/' not in u) or None
    vals=[rid,ar,en,prog,TRN[tr],co,emp or None,role or None,None,None,'li1029',score,'ضمن النطاق','برنامج',lic,oth,None,None,None,None,dd,None,src]
    for ci,v in enumerate(vals,1): ws.cell(rr,ci).value=v
for e in ENR:
    k=e['k']; G=g[k-1]
    for lab,u in e.get('links',[]):
        if addlink(k,lab,u): LOG['link']+=1
    if e.get('prog_add') and e['prog_add'] not in G['prog']: G['prog']+=' + '+e['prog_add']; ws.cell(k+1,4).value=G['prog']; LOG['prog_add']+=1
    if e.get('en') and not G.get('en'): G['en']=e['en']; ws.cell(k+1,3).value=e['en']; LOG['en']+=1
    if e.get('co'): G['co']=e['co']; ws.cell(k+1,6).value=e['co']; LOG['co']+=1
    if e.get('emp') and not G.get('emp'):
        G['emp']=e['emp']; G['role']=e['role']; ws.cell(k+1,7).value=e['emp']; ws.cell(k+1,8).value=e['role']; LOG['emp']+=1
    note(k,e['t']); LOG['enr']+=1
# ---- stories ----
dj=H+'SuccessStories/website/js/data.js'; sj=open(dj,encoding='utf-8').read()
orgs0=set(re.findall(r'"org": "([^"]+)"',sj))
stories=[]
for p in STORIES:
    assert len(p['q'])<=100 and len(p['qe'])<=100,(p['id'],len(p['q']),len(p['qe']))
    assert ('"id": "%s"'%p['id']) not in sj, p['id']
    if p['logo']: assert os.path.exists(H+'SuccessStories/website/'+p['logo']),p['logo']
    G=g[p['k']-1]; li=[l[1] for l in G['links'] if 'linkedin.com/in/' in l[1]][0]
    st={"id":p['id'],"year":p['year'],"quote":{"text":p['q'],"textEn":p['qe'],"kind":"draft"},"name":G['n'],"nameEn":G['en'],"photo":None,"role":p['role'],"org":p['org']}
    if p['logo']: st["orgLogo"]=p['logo']
    st.update({"program":G['prog'],"period":G['co'],"category":"employment","categories":["employment"],"impact":p['impact'],"story":p['story'],"achievements":p['ach'],"links":[{"label":"LinkedIn","url":li}],
       "provenance":f"صفحة الخبرة على LinkedIn بحساب مسجَّل (قُرئت {DATE})، بتواريخ بمستوى الشهر: {p['exp']} + سجل الأكاديمية #{p['k']}. وفق السياسة v1.0 (معيار 14 شهرًا)."})
    stories.append(st)
    if 'job' not in G['cats']: G['cats'].append('job')
    G['emp']=p['org']; G['role']=p['role']; k=p['k']; ws.cell(k+1,7).value=p['org']; ws.cell(k+1,8).value=p['role']
    note(k,'نُشرت قصة نجاح «%s» وفق السياسة v1.0 (معيار 14 شهرًا): %s'%(p['id'],p['ach'][0]))
for x in stories: assert '**' not in json.dumps(x,ensure_ascii=False)
for r in g: assert '**' not in r['d']
newemp={p['org'] for p in STORIES}-orgs0
S0=212; S1=S0+len(stories); E0=113; E1=E0+len(newemp)
N=len(g); TT=collections.Counter(r['tr'] for r in g); wl=sum(1 for r in g if r.get('links')); uu=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
print('N',N0,'->',N,{k:(T0[k],TT[k]) for k in TT if T0[k]!=TT[k]},'wl',wl0,wl,'uu',uu0,uu,dict(LOG),'new',new_ids[0],'..',new_ids[-1],'stories',S0,S1,'emp',E0,E1,newemp)
if DRY: sys.exit(0)
T=TT; TOT=format(N,','); OTOT=format(N0,',')
VA_old='28 أكتوبر 2026 (مسار NCA-ADS ومسح أكتوبر 2026 والتدقيق'; VA_new='29 أكتوبر 2026 (منشورات مزوّدة ومسح أكتوبر 2023 – يونيو 2026 والتدقيق'
VE_old='28 October 2026 (NCA-ADS track + October 2026 sweep and QA round'; VE_new='29 October 2026 (supplied posts + Oct 2023 – Jun 2026 sweep and QA round'
def counts(t):
    for a,b in (('%d قصة'%S0,'%d قصة'%S1),('%d stories'%S0,'%d stories'%S1),('%d verified success stories'%S0,'%d verified success stories'%S1),
                ('%d جهة عمل'%E0,'%d جهة عمل'%E1),('%d employers'%E0,'%d employers'%E1),(VA_old,VA_new),(VE_old,VE_new),
                ('إصدار 28 أكتوبر 2026','إصدار 29 أكتوبر 2026'),('version 28 October 2026','version 29 October 2026')):
        t=t.replace(a,b)
    return t
# Graduates page
head=counts(head.replace(OTOT,TOT)); tail=counts(tail.replace(OTOT,TOT))
tail=rep(tail,"{ value: %d, label: 'سجلًا فرديًا',"%N0,"{ value: %d, label: 'سجلًا فرديًا',"%N,1)
for k,en in EN.items():
    if T[k]!=T0[k]:
        tail,n=re.subn(r"(en: '%s', value: )%d\b"%(re.escape(en),T0[k]),"\\g<1>%d"%T[k],tail); assert n>=1,k
tail=rrep(tail,r"\{ value: %d,(\s+)label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(wl0,format(uu0,',')),"{ value: %d,\\1label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(wl,format(uu,',')))
tail=rep(tail,"noteEn: '%s unique source links'"%format(uu0,','),"noteEn: '%s unique source links'"%format(uu,','),1)
tail=rrep(tail,r"(\{ value: )%d(,\s+label: 'قصة نجاح)"%S0,r"\g<1>%d\2"%S1)
D['grads']=g; open(P_,'w',encoding='utf-8').write(head+json.dumps(D,ensure_ascii=False)+';'+tail)
# Portal
P2=H+'index.html'; s=counts(open(P2,encoding='utf-8').read().replace(OTOT,TOT))
s=rep(s,'data-count="%d"'%N0,'data-count="%d"'%N,1); s=rep(s,'data-count="%d"'%S0,'data-count="%d"'%S1,1); s=rep(s,'data-count="%d"'%E0,'data-count="%d"'%E1,1)
for k in ('ai','ds','dmg','other','genai','coop'):
    pc='%.1f'%(100*T[k]/N)
    pat=r'(data-count=")%d(">0</div>.*?--w:)[\d.]+(%%.*?data-ar=")[\d.]+(%% من السجل" data-en=")[\d.]+(%% of the registry")'%T0[k]
    s,n=re.subn(pat,lambda mm:mm.group(1)+str(T[k])+mm.group(2)+pc+mm.group(3)+pc+mm.group(4)+pc+mm.group(5),s,count=1,flags=re.S); assert n==1,k
open(P2,'w',encoding='utf-8').write(s)
# data.js
s=sj.replace(OTOT,TOT)
s=rep(s,"{ value: %d, label: 'خريجًا موثّقًا',"%N0,"{ value: %d, label: 'خريجًا موثّقًا',"%N,1)
for k,en in EN.items():
    if T[k]!=T0[k]: s=rrep(s,r"(en: '%s',\s+value: )%d\b"%(re.escape(en),T0[k]),"\\g<1>%d"%T[k])
s=rrep(s,r"(\{ value: )%d(,\s+label: 'قصة نجاح)"%S0,r"\g<1>%d\2"%S1)
s=rrep(s,r"(\{ value: )%d(,\s+label: 'جهة عمل')"%E0,r"\g<1>%d\2"%E1)
k=s.index('const STORIES = ['); e=s.index('\n];',k); prev=s[:e].rstrip()
if not prev.endswith(','): prev+=','
s=prev+'\n'+',\n'.join('  '+json.dumps(x,ensure_ascii=False) for x in stories)+s[e:]
s=rep(s,"'use strict';","/* %s: منشورات زوّد بها أ. د. ممدوح العنزي (9: سجلان جديدان و6 إثراءات) + مسح أكتوبر 2023 – يونيو 2026 + سد فجوات جهات العمل من صفحات الخبرة — %s ← %s خريجًا (%d جديدًا)؛ القصص %d ← %d (faisal-almufarrih · sulaiman-alkurbi · fatimah-sammar · nawaf-alomeir)؛ جهات العمل %d ← %d. */\n'use strict';"%(DATE,OTOT,TOT,len(new_ids),S0,S1,E0,E1),1)
open(dj,'w',encoding='utf-8').write(s)
# SS index, about, catalog
P4=H+'SuccessStories/website/index.html'; t=counts(open(P4,encoding='utf-8').read()); t=rep(t,'"numberOfItems": %d'%S0,'"numberOfItems": %d'%S1,1); open(P4,'w',encoding='utf-8').write(t)
for f in ('about.html','Catalog/index.html'):
    t=open(H+f,encoding='utf-8').read(); t=rep(t,'إصدار 28 أكتوبر 2026','إصدار 29 أكتوبر 2026'); t=rep(t,'version 28 October 2026','version 29 October 2026'); open(H+f,'w',encoding='utf-8').write(t)
# xlsx
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
   'تحديث':f'{DATE} — منشورات مزوّدة + مسح أكتوبر 2023 – يونيو 2026 + سد فجوات: {len(new_ids)} سجلًا جديدًا ({OTOT} → {TOT})؛ {LOG["enr"]} إثراءً/ملاحظة؛ القصص {S0} → {S1}؛ جهات العمل {E0} → {E1}'}
for row in st.iter_rows():
    if row[0].value in M: row[1].value=M[row[0].value]
sh=wb.create_sheet('جولة_29_أكتوبر_2026'); sh.sheet_view.rightToLeft=True; sh.append(['#','الاسم','النوع','التفصيل'])
for k in new_ids: sh.append([k,g[k-1]['n'],'سجل جديد (li1029)',g[k-1]['prog'][:90]+' — '+g[k-1]['co']])
for p in STORIES: sh.append([p['k'],g[p['k']-1]['n'],'قصة نجاح جديدة',p['org']+' — '+p['ach'][0]])
for e in ENR: sh.append([e['k'],g[e['k']-1]['n'],'إثراء/ملاحظة',e['t'][:220]])
wb.save(X_)
# md
P5=H+'Graduates/Graduates_Database.md'; s=open(P5,encoding='utf-8').read()
s=rrep(s,r'\*\*الإصدار:\*\* ',f'**الإصدار:** {DATE} — منشورات مزوّدة ومسح أكتوبر 2023 – يونيو 2026 ({OTOT} → {TOT} · القصص {S1} · جهات العمل {E1}). قبله: ',1)
L=['## منشورات مزوّدة ومسح أكتوبر 2023 – يونيو 2026 — %s'%DATE,'',
   f'**الخريجون {OTOT} → {TOT} · القصص {S0} → {S1} · جهات العمل {E0} → {E1}.** المنشورات التسعة التي زوّد بها أ. د. ممدوح العنزي: سبعة لسجلات قائمة (أُضيفت روابط المنشورات، وبرنامج تصور البيانات لشريفة الجهني #3906 مع ترشيحها للدمج مع #3389) وسجلان جديدان: محمد بن طياش (تصور البيانات) وسارة الزهراني (هندسة البيانات الحديثة). مسح المنشورات حسب البرامج أضاف {len(new_ids)-2} سجلًا (البرمجة التوليدية، CDMP، رفع الإنتاجية) وربط 10 سجلات داخلية بحساباتها على LinkedIn. سدّ الفجوات: قراءة صفحات الخبرة لـ 33 سجلًا من نافذة أكتوبر 2023 – يونيو 2026 بلا جهة عمل → 13 جهة عمل جديدة و4 قصص: faisal-almufarrih (بوبا العربية) · sulaiman-alkurbi (واكب) · fatimah-sammar (MsGiraffe) · nawaf-alomeir (مصرف الإنماء). قيد الحكم: #3103 · #952 · #2095 · #2253 · #3452 · #3458.','','---','']
k=re.search(r'\n## ',s).start()+1; s=s[:k]+'\n'.join(L)+'\n'+s[k:]; open(P5,'w',encoding='utf-8').write(s)
for f in ('index.html','Graduates/index.html','SuccessStories/website/js/data.js'):
    t=open(H+f,encoding='utf-8').read()
    if f=='Graduates/index.html': t=t[:t.index('const DATA = ')]+t[t.index('\nconst SITE_STATS'):]
    print(f,'leftover',OTOT,t.count(OTOT),'new',t.count(TOT),'| 212 قصة',t.count('212 قصة'),'| 113 جهة',t.count('113 جهة'),'| 28 أكتوبر',t.count('28 أكتوبر 2026'))
print('done',dict(LOG))
