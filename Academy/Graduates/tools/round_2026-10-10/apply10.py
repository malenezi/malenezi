# -*- coding: utf-8 -*-
# Round 10 Oct 2026 — gaps + new GitHub grads + story check + QA
import json,re,os,sys,shutil,collections
sys.path[:0]=[os.path.dirname(os.path.abspath(__file__)),os.path.expanduser('~/mnt/Academy/Graduates/tools/round_2026-10-07'),os.path.expanduser('~/mnt/Academy/Graduates/tools')]
import load, translit as TR, openpyxl
DRY='--apply' not in sys.argv
H=os.path.expanduser('~/mnt/Academy/'); B='backup-2026-10-10'
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
raw=s[i:j].rstrip(); D=json.loads(raw[:-1]); g=D['grads']; N0=len(g); assert N0==3316,N0
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
# 1) GAPS
setco(2392,'سبتمبر–ديسمبر 2021 (تواريخ مستودعات مشاريع المعسكر)','مستودعات GitHub «LeenaAAlQasem» لمشاريع T5 المتتابعة: MTA-EDA (سبتمبر 2021) · IMDb-Regression (أكتوبر) · Job-stability-classification وNLP-YelpReviews وTraffic-Prediction-DeepLearning (نوفمبر) — تسلسل مشاريع معسكر T5. صفحة LinkedIn المسجلة تعرض «Something went wrong»/غير متاحة')
setco(2405,'يوليو 2024 (تاريخ مستودع T5)','مستودع GitHub «LubnaAlhenaki/T5» (يوليو 2024)')
setco(2511,'يوليو 2025 (تاريخ مستودع المشروع)','مستودعا GitHub «Khalidfa» و«Graduation-project» (يوليو 2025)')
G=g[2510]; G['emp']='Innovation Team Company'; G['role']='مطوّر برمجيات (أكتوبر 2025)'; ws.cell(2512,7).value=G['emp']; ws.cell(2512,8).value=G['role']
if 'job' not in G['cats']: G['cats'].append('job')
note(2511,'صفحة الخبرة (حساب مسجَّل): «Software Developer» — Innovation Team · Full-time منذ أكتوبر 2025 (+3) في مشروع لوزارة الموارد البشرية والتنمية الاجتماعية (UCRM، لوحات مراقبة، Pega). قسم الشهادات فارغ ولا قيد سدايا ظاهر. فحص القصة: التوقيت يجتاز، لكن تطوير الأنظمة/سير العمل (Pega) لا يُنسب إلى برنامج «مفاهيم الذكاء الاصطناعي» — FAIL_RELATEDNESS (البند 5-و، سابقة #2139). لا قصة.'); C['story_checked']+=1
note(404,'⚠ صفحة الخبرة (حساب مسجَّل): Assistant Professor — الجامعة السعودية الإلكترونية (منذ 2021) و«NVIDIA DLI Instructor and University Ambassador» (منذ ديسمبر 2024) — مدرّب معتمد لا متدرب؛ مرشح للاستبعاد بقاعدة «الموظفون والمدربون ليسوا خريجين» عند المراجعة.'); LOG['staff'].append(404); C['trainer_flag']+=1
G=g[1679]; assert not G['en']; G['en']='Sarah Alkhathami'; ws.cell(1681,3).value=G['en']; C['en_set']+=1; note(1680,'الاسم الإنجليزي من اسم المستخدم على GitHub (sarahAlkhathami): «Sarah Alkhathami».')
# 2) ENRICH existing
ENR=[(2573,'مستودع (Storytelling capstone)','https://github.com/c3bod/sdaia-storytelling-tayseer-capstone',16,'برنامج ثانٍ: مستودع «sdaia-storytelling-tayseer-capstone» (6 أكتوبر 2026) — المشروع الختامي لمقرر SDA-DSC-112 «تصور البيانات وسرد القصص» (حالة تيسير). الحساب نفسه (c3bod) المسجل في السجل.'),
 (2590,'GitHub','https://github.com/Mohammed-Ayman-Albilaly',16,'حساب GitHub «Mohammed-Ayman-Albilaly» فيه «tayseer-digital-adoption-capstone» (6 أكتوبر 2026) — المشروع الختامي لـSDA-DSC-112؛ زميل دفعة c3bod (#2573) في برنامج هندسة البيانات (أغسطس 2026) ثم في المقرر نفسه — نسبة مرجّحة بالاسم ومسار الدفعة.'),
 (2535,'GitHub','https://github.com/GhadahAlsubaie',16,'حساب GitHub «GhadahAlsubaie» (يطابق معرّف LinkedIn المسجّل «ghadahalsubaie») فيه «Tamweel-Lite-Advanced-Machine-Learning-Methods-Ghada» (6 أكتوبر 2026) — برنامج ثانٍ: طرق تعلم الآلة المتقدمة (حالة «تمويل»). التقطه فحص المطابقة قبل كتابته سجلًا جديدًا.'),
 (72,'GitHub','https://github.com/progHYA',16,'حساب GitHub «progHYA» فيه مستودع «Haya-Albaqami-SDAIA-NLP» (29 سبتمبر 2026، مشروع معالجة اللغة الطبيعية) — الاسم الكامل في اسم المستودع يطابق السجل؛ برنامج ثانٍ محتمل (NLP، سبتمبر 2026).')]
for k,lab,url,col,txt in ENR:
    if addlink(k,lab,url,col): C['link_added']+=1
    note(k,txt); LOG['enrich'].append(k)
note(2617,'مرشح مطابقة غير محسوم: حساب GitHub «hayaaldossari» (Haya Aldossari — «AI Engineer | Data & Robotics») فيه «SDAIA-Academy-Projects» (5 أكتوبر 2026). لم يُربط لغياب رابط مشترك — لا سجل جديد ولا دمج.'); LOG['enrich'].append(2617)
# 3) NEW
NEW=[
 ('نوف الحارثي','Nouf Alharthi','برنامج أكاديمية سدايا — مشروع ختامي (SDAIA-Capstone؛ البرنامج غير مسمّى)','أكتوبر 2026 (تاريخ مستودع المشروع الختامي)','other',62,[['GitHub','https://github.com/NoufHar'],['مستودع المشروع','https://github.com/NoufHar/SDAIA-Capstone']],'مستودع «SDAIA-Capstone» (7 أكتوبر 2026)؛ الاسم الكامل على ملف GitHub (Nouf Alharthi، السعودية).'),
 ('محمد الحجي','Mohammed Alhijji','برنامج تطوير حلول الذكاء الاصطناعي — أكاديمية سدايا (SDAIA Program for Developing AI Solutions)','أكتوبر 2026 (تاريخ مستودعات البرنامج)','genai',72,[['GitHub','https://github.com/vecxtor0-prog'],['مستودع المشروع','https://github.com/vecxtor0-prog/RAG-Vector-Search-Faiss'],['مستودع المشروع','https://github.com/vecxtor0-prog/Gemini-Semantic-Search']],'مستودعا «RAG-Vector-Search-Faiss» و«Gemini-Semantic-Search» (6 أكتوبر 2026) بوصف «SDAIA Program for Developing AI Solution»؛ الاسم الكامل على ملف GitHub (Mohammed Alhijji).'),
 ('أثير الشهراني','Atheer Alshahrani','تعلم الآلة التطبيقي — أكاديمية سدايا (Applied Machine Learning)','أكتوبر 2026 (تاريخ مستودع مشروع البرنامج)','ai',72,[['GitHub','https://github.com/AtheerJB'],['مستودع المشروع','https://github.com/AtheerJB/Loan-Project-SDAIA']],'مستودع «Loan-Project-SDAIA» (7 أكتوبر 2026) بوصف «Applied Machine Learning project developed as part of SDAIA’s Applied Machine Learning…»؛ الاسم الكامل على ملف GitHub (Atheer Alshahrani).'),
 ('شذى السبيعي','Shatha Alsubaie','طرق تعلم الآلة المتقدمة — أكاديمية سدايا (Advanced Machine Learning Methods)','أكتوبر 2026 (تاريخ مستودع مشروع البرنامج)','ai',68,[['GitHub','https://github.com/shatha-alsubaie'],['مستودع المشروع','https://github.com/shatha-alsubaie/shatha-alsubaie-advanced-machine-learning-methods-tamweel']],'مستودع «shatha-alsubaie-advanced-machine-learning-methods-tamweel» (6 أكتوبر 2026، حالة «تمويل» نفسها)؛ الاسم من اسم المستخدم على GitHub.'),
 ('فرح الربح','Farah Alrebh','دورة الذكاء الاصطناعي — أكاديمية سدايا (مختبرات المقرر)','أكتوبر 2026 (تاريخ مستودع مختبرات المقرر)','ai',62,[['GitHub','https://github.com/farahalrebh'],['مستودع المختبرات','https://github.com/farahalrebh/SDAIA-Farah-Hospital-AI-Labs']],'مستودع «SDAIA-Farah-Hospital-AI-Labs» (6 أكتوبر 2026) بوصف «SDAIA AI course labs»؛ الاسم من اسم المستخدم على GitHub.'),
 ('أسماء مهدي نابه','Asma Mahdi Nabeh','برنامج أكاديمية سدايا — مشروع تحليل الموارد البشرية (البرنامج غير مسمّى)','أكتوبر 2026 (تاريخ مستودع المشروع)','other',60,[['GitHub','https://github.com/asmaMahdiNABEH'],['مستودع المشروع','https://github.com/asmaMahdiNABEH/HR_PROJECT_FOR_SDAIA']],'مستودع «HR_PROJECT_FOR_SDAIA» (7 أكتوبر 2026)؛ الاسم من اسم المستخدم على GitHub. لا يطابق #367 «أسماء عبدالصمد مهدي» (اسم مختلف).'),
 ('فارس الشعشاع','Faris Alshashaa','برنامج النماذج اللغوية الكبيرة — أكاديمية سدايا (مشروع LLM)','أكتوبر 2026 (تاريخ مستودع المشروع)','genai',66,[['GitHub','https://github.com/farisalshashaa'],['مستودع المشروع','https://github.com/farisalshashaa/LLM-Project-SDAIA-Program-']],'مستودع «LLM-Project-SDAIA-Program-» (6 أكتوبر 2026): «مشوار» روبوت محادثة ثنائي اللغة لتأجير السيارات؛ الاسم من اسم المستخدم على GitHub.'),
 ('عزام الزهراني','Azam Alzahrani','تطوير حلول الذكاء الاصطناعي التوليدي — أكاديمية سدايا','أكتوبر 2026 (تاريخ مستودع واجبات المقرر)','genai',62,[['GitHub','https://github.com/AzamAlzahrani'],['مستودع الواجبات','https://github.com/AzamAlzahrani/SDAIA_GenAI']],'مستودع «SDAIA_GenAI» (5 أكتوبر 2026) بوصف «Assignments done for the Generative AI course»؛ الاسم من اسم المستخدم على GitHub.'),
]
idx=TR.build_index(g); new_ids=[]
ghs={l[1].rstrip('/').lower() for r in g for l in r['links']}
for ar,en,prog,co,tr,score,links,d in NEW:
    FP={'Nouf Alharthi':{306,2568},'Asma Mahdi Nabeh':{367,1019},'Faris Alshashaa':{1165}}
    m=TR.match(ar,en,idx); assert {x[0] for x in m}<=FP.get(en,set()),(en,m); assert links[0][1].lower() not in ghs,en
    rid=len(g)+1; r=rid+1; dd=d+' '+TAG.strip()+TL
    g.append({"n":ar,"en":en,"lv":"gh1010","score":score,"prog":prog,"co":co,"win":"ضمن النطاق","edu":"","emp":"","role":"","cats":['program','project'],"d":dd,"links":links,"src":SRC,"tr":tr}); new_ids.append(rid)
    gh=' · '.join(l[1] for l in links)
    vals=[rid,ar,en,prog,TRN[tr],co,None,None,None,None,'gh1010',score,'ضمن النطاق','برنامج · مشروع',None,gh,None,None,None,None,dd,None,SRC]
    for ci,v in enumerate(vals,1): ws.cell(r,ci).value=v
N=len(g); T=collections.Counter(r['tr'] for r in g)
wl=sum(1 for r in g if r.get('links')); uu=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
print('N',N,dict(T),'wl',wl0,'->',wl,'uu',uu0,'->',uu,dict(C),'new',new_ids)
json.dump(dict(N=N,T=T,wl=wl,uu=uu,new=new_ids,C=C,LOG=LOG),open('stats.json','w'),ensure_ascii=False)
if DRY: sys.exit(0)
# =============== WRITE ===============
TOT=format(N,','); OTOT=format(N0,',')
OLD=dict(N=N0,TOT=OTOT,wl=wl0,uu=format(uu0,','),**T0)
VA_O='إصدار 7 أكتوبر 2026 (جولة سد الفجوات واستكمال البيانات'; VA_N='إصدار 10 أكتوبر 2026 (جولة سد الفجوات والخريجين الجدد والتدقيق'
VE_O='version 7 October 2026 (gap-closing and data-completion round'; VE_N='version 10 October 2026 (gap-closing, new-graduates and QA round'
def common(t): return t.replace(OTOT,TOT).replace(VA_O,VA_N).replace(VE_O,VE_N)
head=common(head); tail=common(tail)
tail=rep(tail,"{ value: %d, label: 'سجلًا فرديًا',"%N0,"{ value: %d, label: 'سجلًا فرديًا',"%N,1)
for k,en in (('ai','AI Engineer'),('ds','Data Scientist'),('dmg','Data Management & Governance'),('other','Other / Specialized'),('genai','Gen AI Academy')):
    if T[k]!=T0[k]:
        tail,n=re.subn(r"(en: '%s', value: )%d\b"%(re.escape(en),T0[k]),"\\g<1>%d"%T[k],tail); print('tail',k,n)
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
s=rep(s,"'use strict';","/* %s: جولة سد الفجوات والخريجين الجدد — %s خريجًا (%d سجلات جديدة من GitHub)؛ القصص 167 دون تغيير (فحص قصة واحدة: FAIL_RELATEDNESS). */\n'use strict';"%(DATE,TOT,len(new_ids)),1)
open(P3,'w',encoding='utf-8').write(s); print('data.js leftovers',s.count(OTOT))
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
   'تحديث':f'{DATE} — جولة سد الفجوات والخريجين الجدد: {len(new_ids)} سجلات جديدة ({OTOT} → {TOT})؛ القصص 167 دون تغيير؛ 3 دفعات و1 اسم إنجليزي أُكملت؛ 5 إثراءات؛ 1 مدرّب وُسم للاستبعاد'}
for row in st.iter_rows():
    if row[0].value in M: row[1].value=M[row[0].value]
sh=wb.create_sheet('جولة_10_أكتوبر_2026'); sh.append(['#','الاسم','النوع','التفصيل'])
for k in new_ids: sh.append([k,g[k-1]['n'],'سجل جديد (GitHub)',g[k-1]['prog']])
for k in LOG['co']: sh.append([k,g[k-1]['n'],'تأريخ الدفعة',g[k-1]['co']])
sh.append([1680,g[1679]['n'],'اسم إنجليزي','Sarah Alkhathami'])
for k in LOG['enrich']: sh.append([k,g[k-1]['n'],'إثراء',''])
sh.append([404,g[403]['n'],'⚠ مرشح للاستبعاد (مدرّب NVIDIA DLI)',''])
wb.save(X_)
P5=H+'Graduates/Graduates_Database.md'; s=open(P5,encoding='utf-8').read()
s=rep(s,'**الإصدار:** 7 أكتوبر 2026 — ','**الإصدار:** %s — جولة سد الفجوات والخريجين الجدد والتدقيق (%s → %s · القصص 167). قبله: 7 أكتوبر 2026 — '%(DATE,OTOT,TOT),1)
L=['## جولة سد الفجوات والخريجين الجدد والتدقيق — %s'%DATE,'',f'**الخريجون {OTOT} → {TOT} · القصص 167 (دون تغيير) · جهات العمل 89 (دون تغيير).**','',
 '**1) سد الفجوات:** دفعة #2392 (سبتمبر–ديسمبر 2021، من تسلسل مستودعات T5) · #2405 (يوليو 2024) · #2511 (يوليو 2025) + جهة عمله (Innovation Team، أكتوبر 2025)؛ اسم إنجليزي #1680 Sarah Alkhathami؛ #404 حيدر المبارك وُسم مرشحًا للاستبعاد (مدرّب NVIDIA DLI وأستاذ مساعد — لا متدرب).','',
 f'**2) سجلات جديدة ({len(new_ids)})** من مستودعات GitHub المنشأة 29 سبتمبر – 7 أكتوبر 2026 التي تسمّي سدايا/مقررات الأكاديمية:','','| # | الاسم | الاسم الإنجليزي | البرنامج | الدفعة | الدليل |','|---|---|---|---|---|---|']
for k in new_ids:
    G_=g[k-1]; L.append(f"| {k} | {G_['n']} | {G_['en']} | {G_['prog']} | {G_['co']} | {G_['links'][1][1]} |")
L+=['','**3) إثراءات (لا سجلات جديدة):** #2573 (مشروع SDA-DSC-112) · #2590 (حساب GitHub ومشروع SDA-DSC-112) · #2535 (GitHub يطابق معرّف LinkedIn — التقطه فحص المطابقة قبل كتابته سجلًا جديدًا) · #72 (مستودع NLP باسمها الكامل) · #2617 (مرشح مطابقة غير محسوم، بلا ربط).','',
 '**4) معلّق (أسماء غير كافية):** NoufAbuhaimed (لا ذكر لسدايا في المستودع) · Naif-aln · yalmutairi72-cpu · saud1427446 · sarahmkk11 · nxull9 — اسم أول أو معرّف فقط.','',
 '**5) القصص:** لا قصص جديدة. فحص #2511: التوقيت يجتاز (+3) لكن FAIL_RELATEDNESS (البند 5-و). المرشحان الآليان #2139 و#3085 محسومان سابقًا (FAIL_RELATEDNESS). خريجو أكتوبر 2026 الجدد أحدث من أن يُقاس لهم توظيف.','','---','']
k=s.index('## جولة سد الفجوات واستكمال البيانات — 7 أكتوبر 2026')
s=s[:k]+'\n'.join(L)+'\n'+s[k:]
open(P5,'w',encoding='utf-8').write(s); print('done')
