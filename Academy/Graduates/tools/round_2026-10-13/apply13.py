# -*- coding: utf-8 -*-
# Round 13 Oct 2026 — gap fill + new graduates (GitHub + logged-in LinkedIn posts) + story check (2 new stories)
import json,re,os,sys,shutil,collections
sys.path[:0]=[os.path.expanduser('~/mnt/Academy/Graduates/tools/round_2026-10-07'),os.path.expanduser('~/mnt/Academy/Graduates/tools')]
import translit as TR, openpyxl
DRY='--apply' not in sys.argv
H=os.path.expanduser('~/mnt/Academy/'); B='backup-2026-10-13'
DATE='13 أكتوبر 2026'; TAG='[جولة 13 أكتوبر 2026] '
TL=' تنويه: الاسم العربي نقل حرفي عن الاسم اللاتيني المنشور — غير متحقق علنًا.'
TL2=' تنويه: الاسم العربي نقل حرفي عن اسم المستخدم/الاسم اللاتيني المنشور — غير متحقق علنًا.'
SRC_GH='مستودعات GitHub (أكتوبر 2026) وتسليمات مشروع «وكيل البحث العميق» لأكاديمية سدايا — جولة 13 أكتوبر 2026'
SRC_LI='مسح منشورات LinkedIn (حساب مسجَّل، آخر أسبوع) وقسم الشهادات/الخبرة — جولة 13 أكتوبر 2026'
TRN={'ai':'مهندس ذكاء اصطناعي — AI Engineer','ds':'عالم بيانات — Data Scientist','other':'برامج متخصصة أخرى — Other / Specialized','dmg':'إدارة وحوكمة البيانات — Data Management & Governance','genai':'أكاديمية الذكاء الاصطناعي التوليدي — Gen AI Academy','coop':'التدريب التعاوني — Cooperative Training (COOP)'}
def rep(s,a,b,count=None):
    n=s.count(a); assert n>=1,('missing',a[:90])
    if count is not None: assert n==count,(a[:90],n)
    return s.replace(a,b)
def rrep(s,pat,b,count=1,flags=0):
    s2,n=re.subn(pat,b,s,flags=flags); assert n==count,(pat,n); return s2
FILES=['SuccessStories/website/js/data.js','SuccessStories/website/index.html','index.html','Graduates/index.html','Graduates/Graduates_Database.xlsx','Graduates/Graduates_Database.md']
if not DRY:
    for f in FILES:
        a,b=os.path.splitext(H+f); t=f'{a}.{B}{b}'
        if not os.path.exists(t): shutil.copy2(H+f,t)
P=H+'Graduates/index.html'; s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+len('const DATA = '); j=s.index('\nconst SITE_STATS')
D=json.loads(s[i:j].rstrip()[:-1]); g=D['grads']; N0=len(g); assert N0==3352,N0
head=s[:i]; tail=s[j:]
T0=collections.Counter(r['tr'] for r in g); wl0=sum(1 for r in g if r.get('links')); uu0=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
X_=H+'Graduates/Graduates_Database.xlsx'; wb=openpyxl.load_workbook(X_); ws=wb['قاعدة البيانات']
assert ws.cell(N0+1,1).value==N0
norm=lambda u:re.sub(r'^https?://(www\.|[a-z]{2}\.)?','',u).rstrip('/').lower()
ALL={norm(l[1]) for r in g for l in r['links']}
def note(k,t):
    g[k-1]['d']+=' '+TAG+t; r=k+1; assert ws.cell(r,1).value==k; ws.cell(r,21).value=(ws.cell(r,21).value or '')+' '+TAG+t
def setf(k,field,col,val):
    g[k-1][field]=val; ws.cell(k+1,col).value=val
def addlink(k,label,url):
    G=g[k-1]
    if any(norm(l[1])==norm(url) for l in G['links']): return False
    assert norm(url) not in ALL,(k,url)
    G['links'].append([label,url]); ALL.add(norm(url)); col=15 if 'linkedin.com' in url else 16
    r=k+1; cur=ws.cell(r,col).value; ws.cell(r,col).value=(cur+' · ' if cur else '')+url; return True
GH='https://github.com/'; LI='https://www.linkedin.com/in/'
PAG='هندسة أنظمة الذكاء الاصطناعي الوكيلي المتقدمة (Advanced Agentic AI Systems Engineering) — أكاديمية سدايا'
PLLM='هندسة تطبيقات النماذج اللغوية الكبيرة (SDA-AIE-213 — LLM Application Engineering) — أكاديمية سدايا'
PCV='تطوير أنظمة الرؤية الحاسوبية (SDA-AIE-212 — Computer Vision Systems Development) — أكاديمية سدايا'
PDRA='مشروع «وكيل البحث العميق» (Deep Research Agent — LangGraph) — أكاديمية سدايا'
PGEN='تطوير حلول الذكاء الاصطناعي التوليدي (Developing Generative AI Solutions) — أكاديمية سدايا'
P214='هندسة البيانات الحديثة لأنظمة الذكاء الاصطناعي (Modern Data Engineering for AI Systems) — أكاديمية سدايا'
P112='تصوّر البيانات وسرد القصص (SDA-DSC-112) — أكاديمية سدايا (Data Visualization & Storytelling)'
PLLMBC='معسكر النماذج اللغوية الكبيرة (Large Language Models Bootcamp) — سدايا'
DRA=GH+'{}/deep-research-agent-langgraph-project'
# (ar,en,prog,co,tr,score,lv,links,src,d,cats,emp,role,translit?)
NEW=[
 ('أماني عيد العنزي','Amani Eid Alanazi',PCV,'أكتوبر 2026 (إنشاء مستودع المشروع النهائي: 12 أكتوبر 2026)','ai',80,'gh1013',[['GitHub',GH+'amanialanazi'],['مستودع المشروع',GH+'amanialanazi/FER2013-Emotion-Recognition']],SRC_GH,'مستودع «FER2013-Emotion-Recognition» (12 أكتوبر 2026): «Final Project — Computer Vision Systems Development (تطوير أنظمة الرؤية الحاسوبية) · SDAIA Academy» — «Student: Amani Eid Alanazi — أماني عيد العنزي». نظام تعرّف على المشاعر من الوجه بثلاث استراتيجيات للتعلم بالنقل (EfficientNet-B0، أفضل دقة 67.75%) مع نشر ONNX وواجهة Gradio. الاسم العربي منشور في التسليم نفسه.',['program','project'],'','',False),
 ('أثير العنزي','Atheer Alenezi',PDRA,'أكتوبر 2026 (تسليم المشروع: 8 أكتوبر 2026)','ai',70,'gh1013',[['GitHub',GH+'atheeraziz03-cmd'],['مستودع التسليم',DRA.format('atheeraziz03-cmd')]],SRC_GH,'تفريعة مستودع الأكاديمية «SDAIAAcademy/deep-research-agent-langgraph-project» مع إيداعات المالكة (5–8 أكتوبر 2026: رفع دفتر research_agent وEVALUATION.md) وسطر التسليم في README: «Submitted by: Atheer Alenezi – academy: @SDAIAAcademy».',['program','project'],'','',True),
 ('أحمد الحربي','Ahmad Alharbi',PDRA,'أكتوبر 2026 (تسليم المشروع: 8 أكتوبر 2026)','ai',68,'gh1013',[['GitHub',GH+'EngAhmadAlharbi'],['مستودع التسليم',DRA.format('EngAhmadAlharbi')]],SRC_GH,'تفريعة مستودع الأكاديمية «deep-research-agent-langgraph-project» مع إيداعين للمالك (8 أكتوبر 2026: «Finish research agent project» و«Add submission note») وسطر README: «Submitted by: Eng Ahmad Alharbi - academy: @SDAIAAcademy». كان مرفوضًا في 24 سبتمبر لغياب التسليم — حُسم بالإيداع. اسم شائع: لا رابط مشترك مع #1528 «أحمد الحربي» (برنامج إدارة البيانات، فبراير–يوليو 2026) — لا دمج.',['program','project'],'','',True),
 ('حسن مهدي الحسين','Hasan Mahdi Alhussain',PAG,'أكتوبر 2026 (الأسبوع الأول؛ منشور الإتمام مع شهادة الاجتياز 13 أكتوبر 2026)','ai',88,'li1013',[['LinkedIn',LI+'hasan-alhussain/'],['GitHub',GH+'EngHasanAlhussain']],SRC_LI+' + '+SRC_GH,'منشور LinkedIn (13 أكتوبر 2026) مع شهادة اجتياز ظاهرة باسم «Hasan Mahdi Al Hussain» لبرنامج «Advanced Agentic AI Systems Engineering»؛ المشروع الختامي «AI Research Paper Assistant» (وكيلان: أسئلة وأجوبة على الورقة واكتشاف/ترتيب الأوراق) مع عبدالله السهلي (#2833). حساب GitHub «EngHasanAlhussain» يحمل الاسم الكامل ويربط ملف LinkedIn نفسه، ويملك تفريعة مستودع «وكيل البحث العميق» للأكاديمية (7 أكتوبر 2026، دون إيداعات). مهندس عمليات مصرفية رقمية؛ ماجستير علوم حاسب (إدنبرة). شخص مختلف عن #524 Hassan Adel Alhussain.',['program','cert','project'],'','',False),
 ('حسن علي المكينه','Hassan Ali Almakinah',PLLM,'4–7 أكتوبر 2026','ai',88,'li1013',[['LinkedIn',LI+'hassan-almakinah-33b00b332/']],SRC_LI,'منشور LinkedIn (13 أكتوبر 2026) مع شهادة اجتياز ظاهرة: «Hassan Ali Almakinah — حسن علي المكينه — Large Language Model Application Engineering — From 4/10/2026 To 7/10/2026». أخصائي معلوماتية صحية. كان معلّقًا في 11 أكتوبر (قبول/بداية فقط) — حُسم بالشهادة.',['cert'],'','',False),
 ('شموخ خالد المليفي','Shmookh Kahlid Almoliafai',PAG,'4–8 أكتوبر 2026','ai',88,'li1013',[['LinkedIn',LI+'sii6-h/']],SRC_LI,'منشور LinkedIn «Shmookh Kahlid» (13 أكتوبر 2026) مع شهادة اجتياز ظاهرة: «Shmookh Kahlid Almoliafai — شموخ خالد المليفي — Advanced Agentic AI Systems Engineering — From 4/10/2026 To 8/10/2026»؛ المشروع: «AI Career Advisor» بستة وكلاء متخصصين. خريجة علوم حاسب (جامعة الملك سعود)، متدربة في KACST.',['cert','project'],'','',False),
 ('يارا القرني','Yara Algarni',PGEN,'أكتوبر 2026 (منشور الإتمام 13 أكتوبر 2026)','ai',75,'li1013',[['LinkedIn',LI+'yara-algarni-829233276/']],SRC_LI,'منشور LinkedIn (13 أكتوبر 2026): «I recently completed the Developing Generative AI Solutions program at SDAIA Academy» — مشروع «Hackathon Finder» متعدد الوكلاء (n8n + Tavily) مع واجبات RAG/LLM في Colab. مهندسة برمجيات في SARsatX.',['program','project'],'','',True),
 ('لطيفة اليوسف','Latifah Alyousef',P214,'سبتمبر–أكتوبر 2026 (منشور الإتمام 12 أكتوبر 2026)','ds',78,'li1013',[['LinkedIn',LI+'latifah-alyousef-015821208/']],SRC_LI,'منشور LinkedIn (12 أكتوبر 2026): «سعيدة بإتمام برنامج «هندسة البيانات الحديثة لأنظمة الذكاء الاصطناعي» المقدّم من أكاديمية سدايا» — المشروع النهائي: Data Pipeline لتذاكر خدمة العملاء (Spark · فحوص جودة مع بوابة PASS/FAIL وعزل · Delta Lake · مساعد دعم RAG). خريجة علم بيانات.',['program','project'],'','',True),
 ('الدانة السهلي','Aldana Alsahli',PGEN,'أكتوبر 2026 (منشور الإتمام 12 أكتوبر 2026)','ai',75,'li1013',[['LinkedIn',LI+'aldana-alsahli-90a6a1245/']],SRC_LI,'منشور LinkedIn (12 أكتوبر 2026): «يسعدني مشاركتكم إتمامي لبرنامج "تطوير حلول الذكاء الاصطناعي التوليدي" المقدم من SDAIA Academy» — RAG واسترجاع البيانات وتصميم الوكلاء. محاسبة (IPSAS).',['program'],'','',True),
 ('محمد الدوسري','Mohammed Aldawsari',PLLMBC,'يناير 2024 (تاريخ إصدار الشهادة)','ai',82,'li1013',[['LinkedIn',LI+'mohammed-aldawsari-8ab71624b/']],SRC_LI,'قسم الشهادات في ملفه على LinkedIn (حساب مسجَّل): «Large Language Models Bootcamp — SDAIA | سدايا — Issued Jan 2024». صفحة الخبرة: AI Engineer (تدريب) في Wakeb_Data يونيو–سبتمبر 2025 · مدرّب ذكاء اصطناعي بدوام جزئي في أكاديمية طويق يوليو–أكتوبر 2025 · AI Engineer بدوام كامل في Wakeb_Data منذ أكتوبر 2025. اكتُشف عبر منشور تعريفي لصفحة «شبكة النخبة» (وسيط — لا يُعتمد دليلًا؛ الأدلة كلها من ملفه الشخصي). فحص القصة: FAIL_TIMING — أول توظيف ذي صلة بعد نحو 17 شهرًا (التدريب) و21 شهرًا (الدوام الكامل) من الشهادة، خارج نافذة الأربعة عشر شهرًا؛ كما أتمّ معسكر طويق للذكاء الاصطناعي وعلوم البيانات (عامل مشترك).',['cert','job'],'Wakeb_Data','AI Engineer (أكتوبر 2025)',True),
]
FP={'Ahmad Alharbi':{1528},'Hasan Mahdi Alhussain':{524}}
idx=TR.build_index(g); new_ids=[]; MATCHLOG=[]
for row in NEW:
    ar,en,prog,co,tr,score,lv,links,src,d,cats,emp,role,tl=row
    m={x[0] for x in TR.match(ar,en,idx)}
    ex={k+1 for k,r in enumerate(g) if (r.get('en') or '').lower()==en.lower() or r['n']==ar}
    MATCHLOG.append((en,sorted(m|ex)))
    for l in links: assert norm(l[1]) not in ALL,(en,l)
    rid=len(g)+1; rr=rid+1; dd=TAG+d+(TL if tl else '')
    rec={"n":ar,"en":en,"lv":lv,"score":score,"prog":prog,"co":co,"win":"ضمن النطاق","edu":"","emp":emp,"role":role,"cats":cats,"d":dd,"links":links,"src":src,"tr":tr}
    g.append(rec); new_ids.append(rid)
    for l in links: ALL.add(norm(l[1]))
    li=' · '.join(l[1] for l in links if 'linkedin.com' in l[1]) or None; gh=' · '.join(l[1] for l in links if 'github.com' in l[1]) or None
    catl={'program':'برنامج','project':'مشروع','cert':'شهادة','job':'توظيف'}
    vals=[rid,ar,en,prog,TRN[tr],co,emp or None,role or None,None,None,lv,score,'ضمن النطاق',' · '.join(catl[c] for c in cats),li,gh,None,None,None,None,dd,None,src]
    for ci,v in enumerate(vals,1): ws.cell(rr,ci).value=v
HASAN=new_ids[3]; assert g[HASAN-1]['en']=='Hasan Mahdi Alhussain'
ENR=[
 (2833,[],'برنامج ثانٍ: منشور LinkedIn (13 أكتوبر 2026): «successfully completed the Advanced Agentic AI Systems Engineering course at SDAIA Academy» — المشروع الختامي «AI Research Paper Assistant» مع حسن الحسين (#%d).'%HASAN),
 (3035,[],'شهادة اجتياز ظاهرة في منشور LinkedIn (12 أكتوبر 2026): «Shrouq Saeed Alzahrani — شروق سعيد الزهراني — Generative AI for Productivity — From 13/9/2026 To 15/9/2026» (بعد اختبار عملي وتقييم مشروع). ضُبطت الدفعة وأُخذ الاسم العربي من الشهادة.'),
 (3305,[['LinkedIn',LI+'mohammed-alhijji-a9692a353/']],'منشور LinkedIn (12 أكتوبر 2026) مع شهادة اجتياز ظاهرة: «Mohammed Ahmed Alhijji — محمد احمد الحجي — Developing Generative AI Solutions — From 4/10/2026 To 7/10/2026». ضُبطت الدفعة وأُخذ الاسم العربي من الشهادة (كان نقلًا حرفيًا). أخصائي أمن سيبراني (Brains Valley).'),
 (3310,[['LinkedIn',LI+'faris-alshashaa-043a8929b/']],'منشور LinkedIn (أكتوبر 2026) مع شهادة اجتياز ظاهرة: «Fares Nidal Alshashaa — فارس نضال الشعشاع — Large Language Model Application Engineering — From 4/10/2026 To 7/10/2026». ضُبط اسم البرنامج والدفعة وأُخذ الاسم العربي من الشهادة.'),
 (3028,[['LinkedIn',LI+'lujainabdulaziz1/']],'منشور LinkedIn «Lujain Abdulaziz» (12 أكتوبر 2026): «completed the Generative AI for Productivity program by SDAIA» مع شكر المدرّب م. فهد النهي — يطابق السجل بالاسم والبرنامج والدفعة (حساب GitHub lojainAbdulaziz).'),
 (2564,[['LinkedIn',LI+'nawaf-alsayari-1a9bb9366/']],'منشور LinkedIn (13 أكتوبر 2026) مع ملف «شهادتين اجتياز»: مسار «علم البيانات» (5 معسكرات، بمقر DAICO) — اجتاز المعسكر الأول «Time Series Analysis & Forecasting» (يطابق مستودع التسليم) والثاني «Data Visualization & Storytelling» (برنامج إضافي)، والقادم: أساليب تعلم الآلة المتقدمة، والتجارب واختبارات A/B، وهندسة البيانات الحديثة. تنبيه للمراجعة: المنشور يضع «هندسة البيانات الحديثة» ضمن المعسكرات القادمة، بينما يربطه السجل بفريق مشروع هندسة البيانات (c3bod، أغسطس 2026) — قد يكون الاسم في ذلك الجدول لزميل آخر أو تسجيلًا مبكرًا؛ أُبقي البرنامج مع هذا التنبيه.'),
 (2277,[['LinkedIn',LI+'basil-alaqeel/']],'صفحة الخبرة على LinkedIn (حساب مسجَّل، قُرئت 13 أكتوبر 2026): «T5 Bootcamp - Data Science and Artificial Intelligence — SDAIA · Apprenticeship · Jul 2024 – Oct 2024» (نظام إدارة المرور بالذكاء الاصطناعي) ← «Data Science Specialist — Wedo Solutions · Full-time · Mar 2025 – Present» (تحليلات وذكاء أعمال لمشاريع المدن الذكية، منها CityView لوزارة البلديات والإسكان). التعليم: بكالوريوس علوم حاسب، جامعة القصيم 2019–2024. ضُبطت الدفعة يوليو–أكتوبر 2024. PASS_DATED (+5 أشهر) — مُرقّى إلى قصة نجاح «basil-alaqeel».'),
 (2322,[['LinkedIn',LI+'abdulkarim-mahboob/']],'صفحة الخبرة على LinkedIn (حساب مسجَّل، قُرئت 13 أكتوبر 2026): «T5 & Traffic Management Technologies Bootcamp — SDAIA · Internship · Jul 2024 – Oct 2024» ← أخصائي مكتب مساعدة (تدريب، مجموعة زاهد، ديسمبر 2024 – أبريل 2025) ← «Junior AI Engineer — WTDcare | وتد الطبية · Full-time · Sep 2025 – Jun 2026» (أتمتة n8n وفّرت ~500 ساعة عمل يدوي، ولوحات Looker Studio وDAX) ← «WCC Operator — SETE Energy Saudia · Aug 2026 – Present». ضُبطت الدفعة يوليو–أكتوبر 2024. PASS_DATED (+11 شهرًا) — مُرقّى إلى قصة نجاح «abdulkarim-mahboob»؛ الدور الحالي (منذ أغسطس 2026) تشغيلي ولا يُحتسب.'),
]
COFIX={3035:'13–15 سبتمبر 2026',3305:'4–7 أكتوبر 2026',3310:'4–7 أكتوبر 2026',2277:'يوليو–أكتوبر 2024',2322:'يوليو–أكتوبر 2024'}
LOG=collections.Counter()
for k,lks,t in ENR:
    for lab,u in lks:
        if addlink(k,lab,u): LOG['link']+=1
    note(k,t); LOG['enr']+=1
for k,v in COFIX.items(): setf(k,'co',6,v)
G=g[2833-1]; G['prog']+=' + '+PAG; ws.cell(2834,4).value=G['prog']
G=g[3310-1]; G['prog']=PLLM; ws.cell(3311,4).value=PLLM
G=g[2564-1]; G['prog']+=' + '+P112; ws.cell(2565,4).value=G['prog']
for k,ar in ((3305,'محمد أحمد الحجي'),(3310,'فارس نضال الشعشاع'),(3035,'شروق سعيد الزهراني')):
    G=g[k-1]; G['n']=ar; ws.cell(k+1,2).value=ar
    G['d']=G['d'].replace(TL2,'').replace(TL,'')
    ws.cell(k+1,21).value=(ws.cell(k+1,21).value or '').replace(TL2,'').replace(TL,'')
for k in (3305,3310):
    if 'cert' not in g[k-1]['cats']: g[k-1]['cats'].append('cert')
# ---- STORIES ----
ST=[
 dict(i=2277,id='basil-alaqeel',year=2024,name='باسل العقيل',nameEn='Basil Alaqeel',role='أخصائي علم بيانات',org='ويدو سوليوشنز (Wedo Solutions)',
      program='معسكر T5 لعلوم البيانات والذكاء الاصطناعي — أكاديمية سدايا',period='يوليو–أكتوبر 2024',slug='basil-alaqeel',
      quote='من مشروع إدارة المرور في معسكر T5 إلى لوحات بيانات تخدم قرارات المدن الذكية — خلال خمسة أشهر.',
      impact='توظيف بدوام كامل «أخصائي علم بيانات» في ويدو سوليوشنز في مارس 2025 — خمسة أشهر بعد إتمام المعسكر.',
      story='أتمّ باسل معسكر T5 لعلوم البيانات والذكاء الاصطناعي بأكاديمية سدايا (يوليو–أكتوبر 2024)، وطوّر فيه نظامًا لإدارة الحركة المرورية بالذكاء الاصطناعي يتنبأ بالكثافة ويكتشف الحوادث، بعد تخرجه في علوم الحاسب من جامعة القصيم (2024). وفي مارس 2025 — بعد خمسة أشهر — التحق بشركة ويدو سوليوشنز أخصائيًا لعلم البيانات بدوام كامل، يقدّم حلول التحليلات وذكاء الأعمال لمشاريع المدن الذكية والبلديات، ومنها قيادة جمع المتطلبات لمشروع CityView لدى وزارة البلديات والإسكان وتسليم لوحاته لمتخذي القرار. النتيجة المحتسبة هي التوظيف الأول، بعد خمسة أشهر من الإتمام — داخل نافذة الأربعة عشر شهرًا.',
      ach=['إتمام معسكر T5 لعلوم البيانات والذكاء الاصطناعي — أكاديمية سدايا (أكتوبر 2024)','أخصائي علم بيانات — ويدو سوليوشنز (مارس 2025)','قيادة متطلبات لوحات CityView لوزارة البلديات والإسكان'],
      exp='ويدو سوليوشنز — Data Science Specialist، دوام كامل، مارس 2025 – الآن؛ ومعسكر T5 — سدايا، يوليو–أكتوبر 2024'),
 dict(i=2322,id='abdulkarim-mahboob',year=2024,name='عبدالكريم محبوب',nameEn='Abdulkarim Mahboob',role='مهندس ذكاء اصطناعي مبتدئ',org='وتد الطبية (WTDcare)',
      program='معسكر T5 لتقنيات إدارة الزحام المروري — أكاديمية سدايا',period='يوليو–أكتوبر 2024',slug='abdulkarim-mahboob',
      quote='المعسكر فتح لي باب الذكاء الاصطناعي، وبعده بنيت أتمتة وفّرت مئات الساعات من العمل اليدوي.',
      impact='توظيف بدوام كامل «مهندس ذكاء اصطناعي مبتدئ» في وتد الطبية في سبتمبر 2025 — أحد عشر شهرًا بعد إتمام المعسكر.',
      story='أتمّ عبدالكريم، خريج هندسة البرمجيات، معسكر T5 لتقنيات إدارة الزحام المروري بأكاديمية سدايا (يوليو–أكتوبر 2024)، وعمل بعده أخصائيًا لمكتب المساعدة التقنية بتدريب في مجموعة زاهد (ديسمبر 2024 – أبريل 2025). وفي سبتمبر 2025 — بعد أحد عشر شهرًا من الإتمام — التحق بشركة وتد الطبية مهندسَ ذكاء اصطناعي مبتدئًا بدوام كامل (سبتمبر 2025 – يونيو 2026)، فصمّم سير عمل أتمتة بـn8n خفّض زمن تهيئة الموظف الجديد إلى نحو دقيقتين ووفّر قرابة 500 ساعة من العمل اليدوي، وبنى لوحات Looker Studio وحسابات DAX لمتابعة مؤشرات الأداء. النتيجة المحتسبة هي الالتحاق بوتد الطبية، داخل نافذة الأربعة عشر شهرًا؛ ودوره الحالي منذ أغسطس 2026 تشغيلي ولا يُحتسب.',
      ach=['إتمام معسكر T5 لتقنيات إدارة الزحام المروري — أكاديمية سدايا (أكتوبر 2024)','مهندس ذكاء اصطناعي مبتدئ — وتد الطبية (سبتمبر 2025)','أتمتة تهيئة الموظفين بـn8n وفّرت ~500 ساعة عمل يدوي'],
      exp='وتد الطبية — Junior AI Engineer، دوام كامل، سبتمبر 2025 – يونيو 2026؛ ومعسكر T5 & Traffic Management Technologies — سدايا، يوليو–أكتوبر 2024'),
]
stories=[]
for p in ST:
    G=g[p['i']-1]
    st={"id":p['id'],"year":p['year'],"quote":{"text":p['quote'],"kind":"draft"},"name":p['name'],"nameEn":p['nameEn'],"photo":None,
        "role":p['role'],"org":p['org'],"orgLogo":None,"program":p['program'],"period":p['period'],
        "category":"employment","categories":["employment"],"impact":p['impact'],"story":p['story'],"achievements":p['ach'],
        "links":[{"label":"LinkedIn","url":LI+p['slug']+'/'}],
        "provenance":f"صفحة الخبرة على LinkedIn بحساب مسجَّل (قُرئت {DATE})، بتواريخ بمستوى الشهر: {p['exp']} + سجل الأكاديمية #{p['i']}."}
    stories.append(st)
    G['emp']=p['org']; G['role']=p['role']; ws.cell(p['i']+1,7).value=p['org']; ws.cell(p['i']+1,8).value=p['role']
    if 'job' not in G['cats']: G['cats'].append('job')
NS=len(stories); S0=167; S1=S0+NS; E0=89; E1=E0+2
N=len(g); T=collections.Counter(r['tr'] for r in g)
wl=sum(1 for r in g if r.get('links')); uu=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
print('N',N0,'->',N,{k:(T0[k],T[k]) for k in T},'wl',wl0,'->',wl,'uu',uu0,'->',uu,dict(LOG),'new',new_ids[0],'-',new_ids[-1],'stories',S1,'emp',E1)
print('matches',MATCHLOG)
for t in [json.dumps(x,ensure_ascii=False) for x in stories]+[g[k-1]['d'] for k,_,_ in ENR]+[g[k-1]['d'] for k in new_ids]: assert '**' not in t
if DRY: sys.exit(0)
TOT=format(N,','); OTOT=format(N0,',')
VA_O='إصدار 11 أكتوبر 2026 (جولة الخريجين الجدد والتنظيف 2024–2026'; VA_N='إصدار 13 أكتوبر 2026 (جولة سد الفجوات والخريجين الجدد وفحص القصص'
VE_O='version 11 October 2026 (new-graduates and cleaning round, 2024–2026 focus'; VE_N='version 13 October 2026 (gap-fill, new-graduates and story-check round'
VA2_O='إصدار 11 أكتوبر 2026 (جولة الخريجين الجدد 2024–2026)'; VA2_N='إصدار 13 أكتوبر 2026 (جولة سد الفجوات والخريجين الجدد وفحص القصص)'
VE2_O='version 11 October 2026 (new-graduates round, 2024–2026 focus)'; VE2_N='version 13 October 2026 (gap-fill, new-graduates and story-check round)'
def stc(t):
    t=t.replace(OTOT,TOT)
    for a,b in (('%d قصة'%S0,'%d قصة'%S1),('%d stories'%S0,'%d stories'%S1),('%d verified success stories'%S0,'%d verified success stories'%S1),
                ('%d جهة عمل'%E0,'%d جهة عمل'%E1),('%d employers'%E0,'%d employers'%E1),('across %d government'%E0,'across %d government'%E1)):
        t=t.replace(a,b)
    return t
head=stc(head).replace(VA2_O,VA2_N).replace(VE2_O,VE2_N); tail=stc(tail).replace(VA2_O,VA2_N).replace(VE2_O,VE2_N)
tail=rep(tail,"{ value: %d, label: 'سجلًا فرديًا',"%N0,"{ value: %d, label: 'سجلًا فرديًا',"%N,1)
EN={'ai':'AI Engineer','ds':'Data Scientist','dmg':'Data Management & Governance','other':'Other / Specialized','genai':'Gen AI Academy'}
for k,en in EN.items():
    if T[k]!=T0[k]:
        tail,n=re.subn(r"(en: '%s', value: )%d\b"%(re.escape(en),T0[k]),"\\g<1>%d"%T[k],tail); print('tail',k,n); assert n>=1
tail=rrep(tail,r"\{ value: %d,(\s+)label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(wl0,format(uu0,',')),"{ value: %d,\\1label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(wl,format(uu,',')))
tail=rep(tail,"noteEn: '%s unique source links'"%format(uu0,','),"noteEn: '%s unique source links'"%format(uu,','),1)
tail,n=re.subn(r"(\{ value: )%d(,\s+label: 'قصة نجاح)"%S0,r"\g<1>%d\2"%S1,tail); print('grad story kpi',n)
D['grads']=g; open(P,'w',encoding='utf-8').write(head+json.dumps(D,ensure_ascii=False)+';'+tail)
P2=H+'index.html'; s=stc(open(P2,encoding='utf-8').read()).replace(VA_O,VA_N).replace(VE_O,VE_N)
s=rep(s,'data-count="%d"'%N0,'data-count="%d"'%N,1); s=rep(s,'data-count="%d"'%S0,'data-count="%d"'%S1,1); s=rep(s,'data-count="%d"'%E0,'data-count="%d"'%E1,1)
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
s=rrep(s,r"(\{ value: )%d(,\s+label: 'جهة عمل')"%E0,r"\g<1>%d\2"%E1)
k=s.index('const STORIES = ['); e=s.index('\n];',k)
s=s[:e]+'\n'+',\n'.join('  '+json.dumps(x,ensure_ascii=False) for x in stories)+','+s[e:]
s=rep(s,"'use strict';","/* %s: جولة سد الفجوات والخريجين الجدد وفحص القصص — %s ← %s خريجًا (%d سجلات جديدة · %d إثراءات)؛ القصص %d ← %d (basil-alaqeel · abdulkarim-mahboob)؛ جهات العمل %d ← %d (ويدو سوليوشنز · وتد الطبية). */\n'use strict';"%(DATE,OTOT,TOT,len(new_ids),LOG['enr'],S0,S1,E0,E1),1)
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
   'تحديث':f'{DATE} — جولة سد الفجوات والخريجين الجدد وفحص القصص: {len(new_ids)} سجلات جديدة ({OTOT} → {TOT})؛ {LOG["enr"]} إثراءات؛ القصص {S0} → {S1}؛ جهات العمل {E0} → {E1}'}
for row in st.iter_rows():
    if row[0].value in M: row[1].value=M[row[0].value]
sh=wb.create_sheet('جولة_13_أكتوبر_2026'); sh.append(['#','الاسم','النوع','التفصيل'])
for k in new_ids: sh.append([k,g[k-1]['n'],'سجل جديد ('+('GitHub' if g[k-1]['lv']=='gh1013' else 'LinkedIn')+')',g[k-1]['prog']])
for k,_,t in ENR: sh.append([k,g[k-1]['n'],'إثراء',t[:140]])
for x,p in zip(stories,ST): sh.append([p['i'],x['name'],'قصة جديدة',x['org']+' — '+x['role']])
wb.save(X_)
P5=H+'Graduates/Graduates_Database.md'; s=open(P5,encoding='utf-8').read()
s=rep(s,'**الإصدار:** 11 أكتوبر 2026 — ','**الإصدار:** %s — جولة سد الفجوات والخريجين الجدد وفحص القصص (%s → %s · القصص %d → %d · جهات العمل %d → %d). قبله: 11 أكتوبر 2026 — '%(DATE,OTOT,TOT,S0,S1,E0,E1),1)
L=['## جولة سد الفجوات والخريجين الجدد وفحص القصص — %s'%DATE,'',f'**الخريجون {OTOT} → {TOT} · القصص {S0} → {S1} · جهات العمل {E0} → {E1}.**','',
 f'**1) سجلات جديدة ({len(new_ids)}):**','','| # | الاسم | الاسم الإنجليزي | البرنامج | الدفعة | المسار | المصدر |','|---|---|---|---|---|---|---|']
for k in new_ids:
    G_=g[k-1]; L.append(f"| {k} | {G_['n']} | {G_['en']} | {G_['prog']} | {G_['co']} | {G_['tr']} | {G_['links'][0][1]} |")
L+=['',f"**2) سد الفجوات والإثراء ({LOG['enr']}):** "+' · '.join('#%d %s'%(k,g[k-1]['n']) for k,_,_ in ENR)+' — روابط LinkedIn وشهادات بتواريخ يومية ضبطت الدفعات (#3035 · #3305 · #3310 · #2277 · #2322)، وأسماء عربية من الشهادات (#3305 · #3310 · #3035)، وبرامج ثانية (#2833 · #2564).','',
 '**3) قصص جديدة (2) — معيار الأربعة عشر شهرًا:** basil-alaqeel (#2277، معسكر T5 يوليو–أكتوبر 2024 ← أخصائي علم بيانات، ويدو سوليوشنز، مارس 2025، +5 أشهر) · abdulkarim-mahboob (#2322، معسكر T5 لإدارة الزحام يوليو–أكتوبر 2024 ← مهندس ذكاء اصطناعي مبتدئ، وتد الطبية، سبتمبر 2025، +11 شهرًا). مرفوض: محمد الدوسري (#%d) FAIL_TIMING (17–21 شهرًا). معلّق: #2520 محمد السياري و#2262 حسين اليافعي (لا ملف LinkedIn مطابق بسمتين).'%new_ids[9],'',
 '**4) معلّق:** Alhanouf R. Aldossary (اليوم الأول من ورشة هندسة الأوامر — لم تكتمل) · Rana Almohethef (قُبلت في برنامج معالجة اللغة الطبيعية التطبيقية — لم يبدأ) · Abdullah Alfuwaynid (شهادة تدريب تعاوني تحمل اسمًا آخر) · Mohammed Alshehri (دورة «مفاهيم الذكاء الاصطناعي وتطبيقاته المتقدمة» من سدايا — غير مؤكد أنها برنامج للأكاديمية) · Feras Sebeeh («Fundamentals of AI through SDAIA» — غير محدد) · m7ya505 (تفريعة دون إيداعات). مستبعد: Ruba Fahd (برنامج Women Elevate من ICAIRE). مستودع جديد للأكاديمية: «SDAIAAcademy/applied-nlp» (12 أكتوبر 2026، 0 تفريعات) — دفعة معالجة اللغة الطبيعية التطبيقية بدأت؛ يُعاد فحصه بعد انتهائها.','','---','']
k=s.index('## جولة التنظيف والتدقيق — 11 أكتوبر 2026')
s=s[:k]+'\n'.join(L)+'\n'+s[k:]
open(P5,'w',encoding='utf-8').write(s)
for f in ('index.html','Graduates/index.html'):
    t=open(H+f,encoding='utf-8').read(); print(f,'leftover',OTOT,t.count(OTOT),'%d قصة'%S0,t.count('%d قصة'%S0),'%d جهة'%E0,t.count('%d جهة'%E0),'new',t.count(TOT))
print('done',new_ids,S1,E1)
