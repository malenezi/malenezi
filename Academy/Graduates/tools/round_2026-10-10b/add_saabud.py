# -*- coding: utf-8 -*-
# 10 Oct 2026 (b) — single Academy-supplied record: Saad Al Abbud, AI Agents Development Program 7–9 Sep 2025
import json,re,os,sys,shutil,collections
sys.path[:0]=[os.path.expanduser('~/mnt/Academy/Graduates/tools/round_2026-10-07'),os.path.expanduser('~/mnt/Academy/Graduates/tools')]
import translit as TR, openpyxl
DRY='--apply' not in sys.argv
H=os.path.expanduser('~/mnt/Academy/'); B='backup-2026-10-10d'
TAG='[جولة 10 أكتوبر 2026 (ب)] '
def rep(s,a,b,count=None):
    n=s.count(a); assert n>=1,('missing',a[:90])
    if count is not None: assert n==count,(a[:90],n)
    return s.replace(a,b)
def rrep(s,pat,b,count=1,flags=0):
    s2,n=re.subn(pat,b,s,flags=flags); assert n==count,(pat,n); return s2
FILES=['SuccessStories/website/js/data.js','index.html','Graduates/index.html','Graduates/Graduates_Database.xlsx','Graduates/Graduates_Database.md']
P=H+'Graduates/index.html'; s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+len('const DATA = '); j=s.index('\nconst SITE_STATS')
D=json.loads(s[i:j].rstrip()[:-1]); g=D['grads']; N0=len(g); assert N0==3327,N0
head=s[:i]; tail=s[j:]
T0=collections.Counter(r['tr'] for r in g); wl0=sum(1 for r in g if r.get('links')); uu0=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
LI='https://www.linkedin.com/in/saabud/'
norm=lambda u:re.sub(r'^https?://(www\.|[a-z]{2}\.)?','',u).rstrip('/').lower()
assert not any(norm(l[1])==norm(LI) for r in g for l in r['links']),'slug exists'
idx=TR.build_index(g); m=TR.match('سعد أحمد العبود','Saad Al Abbud',idx); print('matches',[(x[0],g[x[0]-1]['n'],g[x[0]-1]['en'],g[x[0]-1]['prog'][:50]) for x in m])
PROG='برنامج وكلاء الذكاء الاصطناعي (AI Agents) — أكاديمية سدايا'
CO='7–9 سبتمبر 2025'
SRC='بيانات مزوّدة من أ. د. ممدوح العنزي (10 أكتوبر 2026) + صفحة الخبرة على LinkedIn (حساب مسجَّل)'
EMP='منتجع إكوينوكس أمالا Equinox Resort Amaala'; ROLE='منسق تقنية المعلومات — ما قبل الافتتاح (IT Coordinator, Pre-Opening)'
d=(TAG+'سجل مضاف من بيانات زوّدها أ. د. ممدوح العنزي: «برنامج وكلاء الذكاء الاصطناعي — AI Agents Development Program»، من 7 إلى 9 سبتمبر 2025، '
   'مع الاسم العربي الكامل ورابط LinkedIn. صفحة الخبرة على LinkedIn «Saad Al Abbud» (saabud): Information Technology Coordinator (Pre-Opening) — Equinox Resort Amaala منذ أبريل 2026؛ '
   'قبلها Information Technology Specialist — Ejadah Training & Consultancy Group (مارس 2024 – مارس 2026)، وIT Trainee — وزارة التجارة (مايو – أغسطس 2023). '
   'فحص القصة: التعيين الجديد (أبريل 2026) بعد البرنامج بنحو 7 أشهر فيجتاز التوقيت، لكنه دور تشغيلي في تقنية المعلومات لا يُنسب إلى تدريب وكلاء الذكاء الاصطناعي ⇒ FAIL_RELATEDNESS (البند 5-و). '
   'الدفعة نفسها (سبتمبر 2025) لـ#2641 بدر الشمراني.')
rec={"n":"سعد أحمد العبود","en":"Saad Al Abbud","lv":"super26","score":78,"prog":PROG,"co":CO,"win":"ضمن النطاق","edu":"","emp":EMP,"role":ROLE,"cats":["cert","job"],"d":d,"links":[["LinkedIn",LI]],"src":SRC,"tr":"ai"}
g.append(rec); N=len(g); rid=N
T=collections.Counter(r['tr'] for r in g); wl=sum(1 for r in g if r.get('links')); uu=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
print('N',N0,'->',N,'ai',T0['ai'],'->',T['ai'],'wl',wl0,'->',wl,'uu',uu0,'->',uu)
if DRY: sys.exit(0)
for f in FILES:
    a,b=os.path.splitext(H+f); t=f'{a}.{B}{b}'
    if not os.path.exists(t): shutil.copy2(H+f,t)
TOT=format(N,','); OTOT=format(N0,',')
c=lambda t:t.replace(OTOT,TOT)
head=c(head); tail=c(tail)
tail=rep(tail,"{ value: %d, label: 'سجلًا فرديًا',"%N0,"{ value: %d, label: 'سجلًا فرديًا',"%N,1)
tail,n=re.subn(r"(en: 'AI Engineer', value: )%d\b"%T0['ai'],"\\g<1>%d"%T['ai'],tail); print('tail ai',n)
tail=rrep(tail,r"\{ value: %d,(\s+)label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(wl0,format(uu0,',')),"{ value: %d,\\1label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(wl,format(uu,',')))
tail=rep(tail,"noteEn: '%s unique source links'"%format(uu0,','),"noteEn: '%s unique source links'"%format(uu,','),1)
D['grads']=g; open(P,'w',encoding='utf-8').write(head+json.dumps(D,ensure_ascii=False)+';'+tail)
P2=H+'index.html'; s=c(open(P2,encoding='utf-8').read())
s=rep(s,'data-count="%d"'%N0,'data-count="%d"'%N,1)
for k in ('ai','ds','dmg','other','genai','coop'):
    pc='%.1f'%(100*T[k]/N)
    pat=r'(data-count=")%d(">0</div>.*?--w:)[\d.]+(%%.*?data-ar=")[\d.]+(%% من السجل" data-en=")[\d.]+(%% of the registry")'%T0[k]
    s,n=re.subn(pat,lambda mm:mm.group(1)+str(T[k])+mm.group(2)+pc+mm.group(3)+pc+mm.group(4)+pc+mm.group(5),s,count=1,flags=re.S); assert n==1,k
open(P2,'w',encoding='utf-8').write(s)
P3=H+'SuccessStories/website/js/data.js'; s=open(P3,encoding='utf-8').read()
s=rep(s,"{ value: %d, label: 'خريجًا موثّقًا',"%N0,"{ value: %d, label: 'خريجًا موثّقًا',"%N,1)
s=rrep(s,r"(en: 'AI Engineer',\s+value: )%d\b"%T0['ai'],"\\g<1>%d"%T['ai'])
s=c(s); open(P3,'w',encoding='utf-8').write(s)
X_=H+'Graduates/Graduates_Database.xlsx'; wb=openpyxl.load_workbook(X_); ws=wb['قاعدة البيانات']
assert ws.cell(N0+1,1).value==N0 and ws.cell(N+1,1).value is None
vals=[rid,rec['n'],rec['en'],PROG,'مهندس ذكاء اصطناعي — AI Engineer',CO,EMP,ROLE,None,None,'super26',78,'ضمن النطاق','شهادة · توظيف',LI,None,None,None,None,None,d,None,SRC]
for ci,v in enumerate(vals,1): ws.cell(N+1,ci).value=v
st=wb['إحصاءات']
hi=sum(1 for r in g if r.get('score',0)>=75); mid=sum(1 for r in g if 45<=r.get('score',0)<75); lo=N-hi-mid
emp=sum(1 for r in g if r.get('emp')); yc=collections.Counter()
for r in g:
    ys=set(re.findall(r'20(2[1-6])',r.get('co') or ''))
    if not ys: yc['none']+=1
    for y in ys: yc['20'+y]+=1
M={'الإجمالي':TOT,'مهندس ذكاء اصطناعي':T['ai'],'ثقة مرتفعة (≥75)':hi,'ثقة متوسطة (45–74)':mid,'ثقة منخفضة (<45)':lo,'سجلات بجهة عمل موثّقة':emp,'سجلات بروابط تحقق علنية':wl,'روابط مصدر فريدة':uu,'سجلات بدفعة 2026':yc['2026'],'سجلات بلا دفعة محددة':yc['none'],
   'تحديث':f'10 أكتوبر 2026 (ب) — سجل مزوّد واحد: #{rid} سعد أحمد العبود (برنامج وكلاء الذكاء الاصطناعي، 7–9 سبتمبر 2025)؛ {OTOT} → {TOT}؛ القصص 167 دون تغيير (FAIL_RELATEDNESS)'}
for row in st.iter_rows():
    if row[0].value in M: row[1].value=M[row[0].value]
wb['جولة_10_أكتوبر_2026'].append([rid,rec['n'],'سجل جديد (مزوّد من أ. د. ممدوح) — لا قصة: FAIL_RELATEDNESS',PROG])
wb.save(X_)
P5=H+'Graduates/Graduates_Database.md'; s=open(P5,encoding='utf-8').read()
s=rep(s,'(3,316 → 3,327 · القصص 167)','(3,316 → %s · القصص 167)'%TOT,1)
s=rep(s,'**الخريجون 3,316 → 3,327 ·','**الخريجون 3,316 → %s ·'%TOT,1)
add=(f"\n\n**8) سجل مزوّد (10 أكتوبر 2026، بعد الدمج):** #{rid} سعد أحمد العبود / Saad Al Abbud — {PROG} — {CO} — {LI} — "
     "مهندس ذكاء اصطناعي — AI Engineer · super26 · 78. جهة العمل الحالية من صفحة الخبرة: IT Coordinator (Pre-Opening) — Equinox Resort Amaala منذ أبريل 2026. "
     "لا قصة: التوقيت يجتاز (~7 أشهر) لكن الدور تشغيلي في تقنية المعلومات ⇒ FAIL_RELATEDNESS (البند 5-و). فحص التكرار: لا اسم مطابق ولا معرّف LinkedIn مشترك.")
k=s.index('**7) الدمج (بقرار'); k2=s.index('\n\n',k); s=s[:k2]+add+s[k2:]
open(P5,'w',encoding='utf-8').write(s)
for f in ('index.html','Graduates/index.html','SuccessStories/website/js/data.js'):
    t=open(H+f,encoding='utf-8').read(); print(f,'leftover',OTOT,t.count(OTOT),'new',t.count(TOT))
print('done id',rid)
