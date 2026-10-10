# -*- coding: utf-8 -*-
# Round 10 Oct 2026 — gaps + new GitHub grads + story check + QA
import json,re,os,sys,shutil,collections
sys.path[:0]=[os.path.dirname(os.path.abspath(__file__)),os.path.expanduser('~/mnt/Academy/Graduates/tools/round_2026-10-07'),os.path.expanduser('~/mnt/Academy/Graduates/tools')]
import load, translit as TR, openpyxl
DRY='--apply' not in sys.argv
H=os.path.expanduser('~/mnt/Academy/'); B='backup-2026-10-10b'
DATE='10 أكتوبر 2026'; TAG='[جولة 10 أكتوبر 2026] '
TL=' تنويه: الاسم العربي نقل حرفي عن اسم المستخدم/الاسم اللاتيني المنشور — غير متحقق علنًا.'
SRC='بحث مستودعات GitHub المنشأة 29 سبتمبر – 7 أكتوبر 2026 (كلمة «SDAIA») — جولة 10 أكتوبر 2026'
TRN={'ai':'مهندس ذكاء اصطناعي — AI Engineer','ds':'عالم بيانات — Data Scientist','other':'برامج متخصصة أخرى — Other / Specialized','dmg':'إدارة وحوكمة البيانات — Data Management & Governance','genai':'أكاديمية الذكاء الاصطناعي التوليدي — Gen AI Academy'}
def rep(s,a,b,count=None):
    n=s.count(a); assert n>=1,('missing',a[:90])
    if count is not None: assert n==count,(a[:90],n)
    return s.replace(a,b)
def rrep(s,pat,b,count=1,flags=0):
    s2,n=re.subn(pat,b,s,flags=flags); assert n==count,(pat,n); return s2
def bk(p):
    a,b=os.path.splitext(p); t=f'{a}.{B}{b}'
    if not os.path.exists(t): shutil.copy2(p,t)
FILES=['SuccessStories/website/js/data.js','index.html','Graduates/index.html','Graduates/Graduates_Database.xlsx','Graduates/Graduates_Database.md']
if not DRY:
    for f in FILES: bk(H+f)
P=H+'Graduates/index.html'; s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+len('const DATA = '); j=s.index('\nconst SITE_STATS')
raw=s[i:j].rstrip(); D=json.loads(raw[:-1]); g=D['grads']; N0=len(g); assert N0==3324,N0
head=s[:i]; tail=s[j:]
T0=collections.Counter(r['tr'] for r in g); wl0=sum(1 for r in g if r.get('links')); uu0=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
X_=H+'Graduates/Graduates_Database.xlsx'; wb=openpyxl.load_workbook(X_); ws=wb['قاعدة البيانات']
assert ws.cell(N0+1,1).value==N0
def note(k,t):
    g[k-1]['d']+=' '+TAG+t; r=k+1; assert ws.cell(r,1).value==k; ws.cell(r,21).value=(ws.cell(r,21).value or '')+' '+TAG+t
def addlink(k,label,url,col):
    G=g[k-1]; norm=lambda u:re.sub(r'^https?://(www\.|[a-z]{2}\.)?','',u).rstrip('/').lower()
    if any(norm(l[1])==norm(url) for l in G['links']): return False
    G['links'].append([label,url]); r=k+1; cur=ws.cell(r,col).value; ws.cell(r,col).value=(cur+' · ' if cur else '')+url; return True
C=collections.Counter(); LOG=collections.defaultdict(list)
def setco(k,co,ev):
    G=g[k-1]; old=G['co']; G['co']=co; ws.cell(k+1,6).value=co; C['co_set']+=1; LOG['co'].append(k)
    note(k,f'تأريخ الدفعة: {ev} (كانت: «{old or "فارغة"}»).')
exec(open('mid_b.py',encoding='utf-8').read())
N=len(g); T=collections.Counter(r['tr'] for r in g)
wl=sum(1 for r in g if r.get('links')); uu=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
print('N',N,dict(T),'wl',wl0,'->',wl,'uu',uu0,'->',uu,dict(C),'new',new_ids)
json.dump(dict(N=N,T=T,wl=wl,uu=uu,new=new_ids,C=C,LOG=LOG),open('stats.json','w'),ensure_ascii=False)
if DRY: sys.exit(0)
# =============== WRITE ===============
TOT=format(N,','); OTOT=format(N0,',')
OLD=dict(N=N0,TOT=OTOT,wl=wl0,uu=format(uu0,','),**T0)
VA_O='@@none@@'; VA_N='إصدار 10 أكتوبر 2026 (جولة سد الفجوات والخريجين الجدد والتدقيق'
VE_O='@@none@@'; VE_N='version 10 October 2026 (gap-closing, new-graduates and QA round'
def common(t): return t.replace(OTOT,TOT).replace(VA_O,VA_N).replace(VE_O,VE_N)
head=common(head); tail=common(tail)
tail=rep(tail,"{ value: %d, label: 'سجلًا فرديًا',"%N0,"{ value: %d, label: 'سجلًا فرديًا',"%N,1)
for k,en in (('ai','AI Engineer'),('ds','Data Scientist'),('dmg','Data Management & Governance'),('other','Other / Specialized'),('genai','Gen AI Academy')):
    if T[k]!=T0[k]:
        tail,n=re.subn(r"(en: '%s', value: )%d\b"%(re.escape(en),T0[k]),"\\g<1>%d"%T[k],tail); print('tail',k,n)
    else: pass
tail=rrep(tail,r"\{ value: %d,(\s+)label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(wl0,OLD['uu']),"{ value: %d,\\1label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(wl,format(uu,',')))
tail=rep(tail,"noteEn: '%s unique source links'"%OLD['uu'],"noteEn: '%s unique source links'"%format(uu,','),1)
D['grads']=g
open(P,'w',encoding='utf-8').write(head+json.dumps(D,ensure_ascii=False)+';'+tail)
print('grad leftovers',(head+tail).count(OTOT),(head+tail).count(VA_O))
P2=H+'index.html'; s=open(P2,encoding='utf-8').read(); s=common(s)
s=rep(s,'data-count="%d"'%N0,'data-count="%d"'%N,1)
for k in ('ai','ds','dmg','other','genai','coop'):
    pc='%.1f'%(100*T[k]/N)
    pat=r'(data-count=")%d(">0</div>.*?--w:)[\d.]+(%%.*?data-ar=")[\d.]+(%% من السجل" data-en=")[\d.]+(%% of the registry")'%T0[k]
    s,n=re.subn(pat,lambda m:m.group(1)+str(T[k])+m.group(2)+pc+m.group(3)+pc+m.group(4)+pc+m.group(5),s,count=1,flags=re.S); assert n==1,k
open(P2,'w',encoding='utf-8').write(s); print('portal leftovers',s.count(OTOT))
P3=H+'SuccessStories/website/js/data.js'; s=open(P3,encoding='utf-8').read()
s=rep(s,"{ value: %d, label: 'خريجًا موثّقًا',"%N0,"{ value: %d, label: 'خريجًا موثّقًا',"%N,1)
for k,en in (('ai','AI Engineer'),('ds','Data Scientist'),('dmg','Data Management & Governance'),('other','Other / Specialized'),('genai','Gen AI Academy')):
    if T[k]!=T0[k]: s=rrep(s,r"(en: '%s',\s+value: )%d\b"%(re.escape(en),T0[k]),"\\g<1>%d"%T[k])
s=common(s)
s=s.replace('(8 سجلات جديدة من GitHub)','(16 سجلًا جديدًا من GitHub)')
open(P3,'w',encoding='utf-8').write(s); print('data.js leftovers',s.count(OTOT))

# data.js coop/genai etc handled; tail genai handled above
st=wb['إحصاءات']
hi=sum(1 for r in g if r.get('score',0)>=75); mid=sum(1 for r in g if 45<=r.get('score',0)<75); lo=N-hi-mid
emp=sum(1 for r in g if r.get('emp')); yc=collections.Counter()
for r in g:
    ys=set(re.findall(r'20(2[1-6])',r.get('co') or ''))
    if not ys: yc['none']+=1
    for y in ys: yc['20'+y]+=1
M={'الإجمالي':TOT,'مهندس ذكاء اصطناعي':T['ai'],'عالم بيانات':T['ds'],'أكاديمية الذكاء الاصطناعي التوليدي':T['genai'],'إدارة وحوكمة البيانات':T['dmg'],'التدريب التعاوني':T['coop'],'برامج متخصصة أخرى':T['other'],
   'ثقة مرتفعة (≥75)':hi,'ثقة متوسطة (45–74)':mid,'ثقة منخفضة (<45)':lo,'سجلات بجهة عمل موثّقة':emp,'سجلات بروابط تحقق علنية':wl,'روابط مصدر فريدة':uu,
   'سجلات بدفعة 2026':yc['2026'],'سجلات بلا دفعة محددة':yc['none'],
   'تحديث':f'{DATE} — جولة سد الفجوات والخريجين الجدد: 16 سجلًا جديدًا (3,316 → {TOT})؛ القصص 167 دون تغيير؛ 3 دفعات و1 اسم إنجليزي أُكملت؛ 8 إثراءات؛ 1 مدرّب وُسم للاستبعاد؛ 5 مرشحي دمج'}
for row in st.iter_rows():
    if row[0].value in M: row[1].value=M[row[0].value]
sh=wb['جولة_10_أكتوبر_2026']
for k in new_ids: sh.append([k,g[k-1]['n'],'سجل جديد (GitHub، الدفعة الثانية)',g[k-1]['prog']])
for k in LOG['enrich']: sh.append([k,g[k-1]['n'],'إثراء',''])
for k in LOG['fix']: sh.append([k,g[k-1]['n'],'تصحيح المسار/اسم البرنامج',g[k-1]['prog']+' · '+g[k-1]['tr']])
wb.save(X_)
P5=H+'Graduates/Graduates_Database.md'; s=open(P5,encoding='utf-8').read()
s=rep(s,'(3,316 → 3,324 · القصص 167)','(3,316 → %s · القصص 167)'%TOT,1)
s=rep(s,'**الخريجون 3,316 → 3,324 ·','**الخريجون 3,316 → %s ·'%TOT,1)
L=[f'**2-ب) سجلات جديدة — الدفعة الثانية ({len(new_ids)})** من مستودعات مقرر SDA-DSC-211 «أساليب تعلم الآلة المتقدمة» (حالة «تمويل لايت»، 4–7 أكتوبر 2026) ومقرر SDA-AIE-113؛ الاسم الكامل في اسم المستودع أو الحساب:','','| # | الاسم | الاسم الإنجليزي | البرنامج | الدفعة | الدليل |','|---|---|---|---|---|---|']
for k in new_ids:
    G_=g[k-1]; L.append(f"| {k} | {G_['n']} | {G_['en']} | {G_['prog']} | {G_['co']} | {G_['links'][1][1]} |")
L+=['','**تصحيحات:** وُحّد اسم البرنامج والمسار لسجلات الدفعة الأولى (#3317–3324) على التسميات القائمة: «تطوير حلول الذكاء الاصطناعي التوليدي» ← مسار مهندس الذكاء الاصطناعي (لا أكاديمية الذكاء الاصطناعي التوليدي)، و«أساليب تعلم الآلة المتقدمة» ← مسار عالم البيانات. **إثراءات إضافية:** #3214 (GitHub JanaAlkha) · #3202 (GitHub noufalohali-24، مستودع «رفيق») · #2869 (مرشح مطابقة: Dalonazi). **معلّق إضافي:** Raghad1015 · nfsh46655-jpg (اسم أول فقط) · RaghadAlbeladi1 (مستودع «SDAIA_Drug_Safety_Pipeline» بلا برنامج — قد يكون مشروعًا داخليًا) · almiyead-rgb (قالب الطالب — مدرّب محتمل) · مستودعات «tayseer-capstone» لـ Abdullah-FZN وAhm-445 وA-edu (بلا اسم كامل).','']
k=s.index('**3) إثراءات (لا سجلات جديدة):**'); s=s[:k]+'\n'.join(L)+'\n'+s[k:]
open(P5,'w',encoding='utf-8').write(s); print('done')
