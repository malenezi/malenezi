# -*- coding: utf-8 -*-
# 18 Oct 2026 (b): Lamia Salem Alasmari story (full name supplied by Prof. Mamdouh) + supplied photos/logos wired.
import json,re,os,sys,shutil,collections
from PIL import Image
import openpyxl
H=os.path.expanduser('~/mnt/Academy/'); A=H+'SuccessStories/website/assets/'
BK=H+'_backups/2026-10-18b/'; os.makedirs(BK,exist_ok=True)
FILES=['SuccessStories/website/js/data.js','SuccessStories/website/index.html','index.html','Graduates/index.html','Graduates/Graduates_Database.xlsx','Graduates/Graduates_Database.md']
for f in FILES:
    t=BK+f.replace('/','__')
    if not os.path.exists(t): shutil.copy2(H+f,t)
TAG='[جولة 18 أكتوبر 2026 (ب)] '
def rep(s,a,b,count=None):
    n=s.count(a); assert n>=1,('missing',a[:90])
    if count is not None: assert n==count,(a[:90],n)
    return s.replace(a,b)
# ---------- images ----------
OG=H+'_to_delete/2026-10-18b/assets-originals/'; os.makedirs(OG,exist_ok=True)
def lb(src,dst,bg,W=1200,Hh=820):
    im=Image.open(A+src).convert('RGB'); sc=min(W/im.width,Hh/im.height); im=im.resize((round(im.width*sc),round(im.height*sc)),Image.LANCZOS)
    c=Image.new('RGB',(W,Hh),bg); c.paste(im,((W-im.width)//2,(Hh-im.height)//2)); c.save(A+dst,quality=90)
def crop(src,dst,y0=0.0,W=1200,Hh=820):
    im=Image.open(A+src).convert('RGB'); sc=W/im.width; im=im.resize((W,round(im.height*sc)),Image.LANCZOS)
    y=int(min(max(0,(im.height-Hh)*y0), im.height-Hh)); im.crop((0,y,W,y+Hh)).save(A+dst,quality=90)
def logo(src,dst,maxh=300):
    im=Image.open(A+src).convert('RGBA'); bb=im.getbbox()
    if bb: im=im.crop(bb)
    sc=min(1,maxh/im.height); im=im.resize((round(im.width*sc),round(im.height*sc)),Image.LANCZOS); im.save(A+dst)
crop('samah-aljuhani.png','samah-aljuhani.jpg',0.0)
lb('rewaa-hummedi.jpeg','rewaa-hummedi.jpg',(255,255,255),600,410)
im=Image.open(A+'lujain-almogren.jpeg').convert('RGB'); lb('lujain-almogren.jpeg','lujain-almogren.jpg',im.getpixel((5,5)))
im=Image.open(A+'dalya-alanazi.jpeg').convert('RGB'); lb('dalya-alanazi.jpeg','dalya-alanazi.jpg',im.getpixel((5,5)))
logo('Saudi_Ministry_of_Justice_Logo.svg.webp','moj.png',360)
logo('Logo_Ministry_of_Commerce.svg.webp','moc.png',240)
shutil.copy2(A+'Adaa-logo.svg',A+'adaa.svg')
for f in ['samah-aljuhani.png','rewaa-hummedi.jpeg','lujain-almogren.jpeg','dalya-alanazi.jpeg','Saudi_Ministry_of_Justice_Logo.svg.webp','Logo_Ministry_of_Commerce.svg.webp','Adaa-logo.svg']:
    shutil.move(A+f,OG+f)
IMG={'samah-aljuhani':('assets/samah-aljuhani.jpg','assets/moj.png'),'rewaa-hummedi':('assets/rewaa-hummedi.jpg','assets/sdm.png'),
     'lujain-almogren':('assets/lujain-almogren.jpg','assets/adaa.svg'),'dalya-alanazi':('assets/dalya-alanazi.jpg','assets/moc.png'),
     'sara-alamri':(None,'assets/elm.png'),'abdullah-alowais':(None,'assets/sdaia.svg')}
# ---------- graduate record #3505 ----------
K=3505
P=H+'Graduates/index.html'; s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+len('const DATA = '); j=s.index('\nconst SITE_STATS')
D=json.loads(s[i:j].rstrip()[:-1]); g=D['grads']; N=len(g); assert N==3514
G=g[K-1]; assert G['en']=='Lamia S.',G['en']
NOTE='الاسم الكامل «لمياء سالم الأسمري / Lamia Salem Alasmari» زوّد به المدير العام للأكاديمية (18 أكتوبر 2026) فرُفع التعليق؛ ونُشرت القصة: مسؤولة إدارة بيانات المؤسسة في البنك الأهلي السعودي من ديسمبر 2024 — بعد ستة أشهر من المعسكر.'
G['n']='لمياء سالم الأسمري'; G['en']='Lamia Salem Alasmari'; G['score']=85
G['d']=G['d'].replace(' تنويه: الاسم العربي نقل حرفي عن الاسم اللاتيني المنشور — غير متحقق علنًا.','')+' '+TAG+NOTE
G['emp']='البنك الأهلي السعودي (SNB)'; G['role']='مسؤولة إدارة بيانات المؤسسة (Enterprise Data Management Associate) — ديسمبر 2024'
if 'job' not in G['cats']: G['cats'].append('job')
X_=H+'Graduates/Graduates_Database.xlsx'; wb=openpyxl.load_workbook(X_); ws=wb['قاعدة البيانات']; r=K+1
assert ws.cell(r,1).value==K
ws.cell(r,2).value=G['n']; ws.cell(r,3).value=G['en']; ws.cell(r,12).value=85; ws.cell(r,7).value=G['emp']; ws.cell(r,8).value=G['role']; ws.cell(r,21).value=G['d']; ws.cell(r,14).value='برنامج · شهادة · توظيف'
head=s[:i]; tail=s[j:]
S0,S1,E0,E1=189,190,103,104
def stc(t):
    for a,b in (('%d قصة'%S0,'%d قصة'%S1),('%d stories'%S0,'%d stories'%S1),('%d verified success stories'%S0,'%d verified success stories'%S1),('%d جهة عمل'%E0,'%d جهة عمل'%E1),('%d employers'%E0,'%d employers'%E1)):
        t=t.replace(a,b)
    return t
head=stc(head); tail=stc(tail)
tail,n=re.subn(r"(\{ value: )%d(,\s+label: 'قصة نجاح)"%S0,r"\g<1>%d\2"%S1,tail); print('grad story kpi',n)
D['grads']=g; open(P,'w',encoding='utf-8').write(head+json.dumps(D,ensure_ascii=False)+';'+tail)
P2=H+'index.html'; t=stc(open(P2,encoding='utf-8').read()); t=rep(t,'data-count="%d"'%S0,'data-count="%d"'%S1,1); t=rep(t,'data-count="%d"'%E0,'data-count="%d"'%E1,1); open(P2,'w',encoding='utf-8').write(t)
# ---------- story ----------
P3=H+'SuccessStories/website/js/data.js'; t=open(P3,encoding='utf-8').read()
a=t.index('const STORIES = [')+len('const STORIES = '); b=t.index('\n];',a)+2; ST=json.loads(t[a:b])
for x in ST:
    if x['id'] in IMG:
        ph,lg=IMG[x['id']]
        if ph: x['photo']=ph
        if lg: x['orgLogo']=lg
st={"id":"lamia-alasmari","year":2024,"quote":{"text":"أتممت معسكر T5 في يونيو 2024، وبعد ستة أشهر كنت أعمل في إدارة بيانات المؤسسة في البنك الأهلي السعودي — الحوكمة وجودة البيانات صارتا عملي اليومي.","kind":"draft"},
 "name":"لمياء سالم الأسمري","nameEn":"Lamia Salem Alasmari","photo":None,"role":"مسؤولة إدارة بيانات المؤسسة (Enterprise Data Management)","org":"البنك الأهلي السعودي (SNB)",
 "program":"معسكر T5 لعلوم البيانات والذكاء الاصطناعي — أكاديمية سدايا","period":"مارس – يونيو 2024","category":"employment","categories":["employment"],
 "impact":"تعيين في إدارة بيانات المؤسسة بالبنك الأهلي السعودي في ديسمبر 2024 — بعد ستة أشهر من إتمام المعسكر — ثم مسؤولة إدارة بيانات المؤسسة من مارس 2025.",
 "story":"أتمّت لمياء معسكر T5 لعلوم البيانات والذكاء الاصطناعي في أكاديمية سدايا (مارس – يونيو 2024) بشهادة إتمام، وهي خريجة جامعة الأميرة نورة بنت عبدالرحمن. ثم التحقت بالبنك الأهلي السعودي متدربةً تعاونية في إدارة بيانات المؤسسة (أغسطس – نوفمبر 2024)، وفي ديسمبر 2024 — بعد ستة أشهر من المعسكر — عُيّنت فيه «Enterprise Data Management Associate» بدوام كامل، ثم مسؤولةً لإدارة بيانات المؤسسة من مارس 2025، تعمل على تحليلات البيانات وإدارة الطلب على البيانات. التواريخ موثّقة بمستوى الشهر في صفحة خبرتها، والاسم الكامل مؤكد من سجلات الأكاديمية.",
 "achievements":["تعيين في إدارة بيانات المؤسسة بالبنك الأهلي السعودي — ديسمبر 2024، بعد ستة أشهر من المعسكر","مسؤولة إدارة بيانات المؤسسة منذ مارس 2025","شهادة إتمام معسكر T5 لعلوم البيانات والذكاء الاصطناعي (يونيو 2024)"],
 "links":[{"label":"LinkedIn","url":"https://www.linkedin.com/in/lamia-s-195639232/"}],
 "provenance":"صفحة الخبرة على LinkedIn بحساب مسجَّل (قُرئت 18 أكتوبر 2026)، بتواريخ بمستوى الشهر: معسكر سدايا مارس – يونيو 2024 · البنك الأهلي السعودي: تدريب تعاوني أغسطس – نوفمبر 2024، Associate من ديسمبر 2024، Officer من مارس 2025 + الاسم الكامل من المدير العام للأكاديمية (18 أكتوبر 2026) + سجل الأكاديمية #3505."}
ST.append(st)
t=t[:a]+'[\n'+',\n'.join('  '+json.dumps(x,ensure_ascii=False) for x in ST)+'\n]'+t[b-1:] if False else t
# rebuild STORIES block preserving file layout (one story per line)
k=t.index('const STORIES = ['); e=t.index('\n];',k)
t=t[:k]+'const STORIES = [\n'+',\n'.join('  '+json.dumps(x,ensure_ascii=False) for x in ST)+t[e:]
t,n=re.subn(r"(\{ value: )%d(,\s+label: 'قصة نجاح)"%S0,r"\g<1>%d\2"%S1,t); assert n==1
t,n=re.subn(r"(\{ value: )%d(,\s+label: 'جهة عمل')"%E0,r"\g<1>%d\2"%E1,t); assert n==1
t=rep(t,"'use strict';","/* 18 أكتوبر 2026 (ب): قصة لمياء سالم الأسمري (البنك الأهلي السعودي) بعد تزويد الاسم الكامل — القصص 189 ← 190، جهات العمل 103 ← 104؛ صور وشعارات مزوّدة: سماح الجهني · روعة حميدي · لجين المقرن · داليا العنزي + شعارات وزارة العدل ووزارة التجارة وأداء وSDM وعلم وسدايا. */\n'use strict';",1)
open(P3,'w',encoding='utf-8').write(t)
P4=H+'SuccessStories/website/index.html'; u=open(P4,encoding='utf-8').read(); u=rep(u,'"numberOfItems": %d'%S0,'"numberOfItems": %d'%S1,1); open(P4,'w',encoding='utf-8').write(stc(u))
st_=wb['إحصاءات']
for row in st_.iter_rows():
    if row[0].value=='سجلات بجهة عمل موثّقة': row[1].value=sum(1 for r in g if r.get('emp'))
    if row[0].value=='تحديث': row[1].value='18 أكتوبر 2026 (ب) — قصة لمياء سالم الأسمري (#3505) بعد تزويد الاسم الكامل؛ القصص 190؛ جهات العمل 104؛ صور وشعارات مزوّدة'
sh=wb['جولة_18_أكتوبر_2026']; sh.append([K,G['n'],'قصة جديدة (ب)','البنك الأهلي السعودي (SNB) — مسؤولة إدارة بيانات المؤسسة'])
wb.save(X_)
P5=H+'Graduates/Graduates_Database.md'; m=open(P5,encoding='utf-8').read()
m=rep(m,'**الإصدار:** 18 أكتوبر 2026 — ','**الإصدار:** 18 أكتوبر 2026 (ب) — قصة لمياء سالم الأسمري #3505 بعد تزويد الاسم الكامل (القصص 189 → 190 · جهات العمل 104). قبله: 18 أكتوبر 2026 — ',1)
open(P5,'w',encoding='utf-8').write(m)
print('ok stories',len(ST),'imgs',{k:v for k,v in IMG.items()})
