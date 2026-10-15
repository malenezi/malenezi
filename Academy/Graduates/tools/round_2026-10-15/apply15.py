# -*- coding: utf-8 -*-
# Round 15 Oct 2026 — new graduates (Time Series cohort forks + LinkedIn posts) + story check + QA + cleaning
import json,re,os,sys,shutil,collections
sys.path[:0]=[os.path.expanduser('~/mnt/Academy/Graduates/tools/round_2026-10-07'),os.path.expanduser('~/mnt/Academy/Graduates/tools')]
import translit as TR, openpyxl
DRY='--apply' not in sys.argv
H=os.path.expanduser('~/mnt/Academy/'); B='backup-2026-10-15'
DATE='15 أكتوبر 2026'; TAG='[جولة 15 أكتوبر 2026] '
TL=' تنويه: الاسم العربي نقل حرفي عن الاسم اللاتيني المنشور — غير متحقق علنًا.'
TL2=' تنويه: الاسم العربي نقل حرفي عن اسم المستخدم/الاسم اللاتيني المنشور — غير متحقق علنًا.'
SRC_GH='تفريعات مستودع الأكاديمية «SDAIAAcademy/international-airpassengers-project» مع إيداعات المالكين وسطر «Submitted by» — جولة 15 أكتوبر 2026'
SRC_LI='مسح منشورات LinkedIn (حساب مسجَّل، آخر أسبوع) وقسم الشهادات/الخبرة — جولة 15 أكتوبر 2026'
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
D=json.loads(s[i:j].rstrip()[:-1]); g=D['grads']; N0=len(g); assert N0==3362,N0
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
PTS='التنبؤ بالسلاسل الزمنية لأنظمة الذكاء الاصطناعي (Time Series Forecasting for AI Systems) — أكاديمية سدايا'
COTS='أكتوبر 2026 (تسليم المشروع الختامي: {} أكتوبر 2026)'
AP=GH+'{}/international-airpassengers-project'
def tsd(sub,extra=''):
    return f'تفريعة مستودع الأكاديمية «SDAIAAcademy/international-airpassengers-project» (المشروع الختامي لدورة السلاسل الزمنية — دفعة أكتوبر 2026) مع إيداعات المالك/ة ({sub}) وسطر التسليم في README بالاسم الكامل وإشارة «academy: @SDAIAAcademy» — تسليم فعلي لا تفريع فقط.'+(' '+extra if extra else '')
NEW=[
 ('بيلسان حسن المهداوي','Baylsan Hassan Almehdawi',PTS,COTS.format('15'),'ds',75,'gh1015',[['GitHub',GH+'baylsan20'],['مستودع التسليم',AP.format('baylsan20')]],SRC_GH,tsd('15 أكتوبر 2026: رفع report.md وREADME'),['program','project'],'','',True),
 ('لمى القحطاني','Lama Alqahtani',PTS,COTS.format('15'),'ds',72,'gh1015',[['GitHub',GH+'lamaalqhtaniit-tech'],['مستودع التسليم',AP.format('lamaalqhtaniit-tech')]],SRC_GH,tsd('15 أكتوبر 2026: «Add forecasting report» ودفتر Colab','اسم شائع: لا رابط مشترك مع أي سجل قائم — لا دمج.'),['program','project'],'','',True),
 ('ريناد الجارالله','Renad Aljarallah',PTS,COTS.format('14'),'ds',78,'gh1015',[['GitHub',GH+'renad12345'],['مستودع التسليم',AP.format('renad12345')]],SRC_GH,tsd('14 أكتوبر 2026: «Add final project report on air passenger forecast»','الاسم الكامل «RENAD ALJARALLAH» معروض أيضًا على ملف GitHub.'),['program','project'],'','',True),
 ('تركي محمد الغازي','Turki Mohammed Alghazi',PTS,COTS.format('14'),'ds',70,'gh1015',[['GitHub',GH+'turki0010'],['مستودع التسليم',AP.format('turki0010')]],SRC_GH,tsd('14 أكتوبر 2026: Report.md ودفتر Colab','ملاحظة: كتب اسمه داخل سطر التعليمات بدل السطر العلوي («Submitted by: <Turki Mohammed Alghazi>») — التسليم قائم.'),['program','project'],'','',True),
 ('ليان عبدالرحمن العمري','Layan Abdulrhman Alamri',PTS,COTS.format('14–15'),'ds',75,'gh1015',[['GitHub',GH+'LayamAlamri0'],['مستودع التسليم',AP.format('LayamAlamri0')]],SRC_GH,tsd('14–15 أكتوبر 2026: report.md ودفتر Colab','تنويه: اسم قريب من #2811 «ليان العمري» (معسكر محترفي الذكاء الاصطناعي، ديسمبر 2025 – فبراير 2026) — لا رابط مشترك ولا تعزيز بالبرنامج أو الحساب (الحساب أُنشئ 14 أكتوبر 2026)؛ إشارة تقاطع فقط، لا دمج.'),['program','project'],'','',True),
 ('شهد القداح','Shahad Algadah',PTS,COTS.format('14'),'ds',85,'gh1015',[['GitHub',GH+'ShahadAlgadah'],['مستودع التسليم',AP.format('ShahadAlgadah')],['LinkedIn',LI+'shahad-algadah-841509337/']],SRC_GH,tsd('14 أكتوبر 2026: «Complete forecasting notebook» و«Finalize notebook and verify»','ملف GitHub يحمل الاسم الكامل ويربط ملف LinkedIn نفسه (طالبة علوم حاسب، مطوّرة ذكاء اصطناعي وAIoT).'),['program','project'],'','',True),
 ('باسل سعيد الزهراني','Basel Saeed Alzahrani',PTS,COTS.format('14'),'ds',75,'gh1015',[['GitHub',GH+'BaselSZ'],['مستودع التسليم',AP.format('BaselSZ')]],SRC_GH,tsd('14 أكتوبر 2026: رفع الملفات وتحديث اسم المسلِّم'),['program','project'],'','',True),
 ('نورة تركي بن سعيدان','Norah Turki Bin Saedan',PTS,COTS.format('14'),'ds',75,'gh1015',[['GitHub',GH+'cbvxil'],['مستودع التسليم',AP.format('cbvxil')]],SRC_GH,tsd('14 أكتوبر 2026: إنشاء report.md وتحديث README','الملف الشخصي «norahturki».'),['program','project'],'','',True),
 ('مشاعل العتيبي','Mashael Alotaibi',PTS,COTS.format('15'),'ds',72,'gh1015',[['GitHub',GH+'mashaellna77-maker'],['مستودع التسليم',AP.format('mashaellna77-maker')]],SRC_GH,tsd('15 أكتوبر 2026: report.md ودفتر Colab','اسم شائع: لا رابط مشترك مع أي سجل قائم — لا دمج.'),['program','project'],'','',True),
 ('علي عبدالملك','Ali Abdulmalik',PTS,COTS.format('14'),'ds',70,'gh1015',[['GitHub',GH+'alialnefaie4-oss'],['مستودع التسليم',GH+'alialnefaie4-oss/ali-abdulmalik']],SRC_GH,tsd('14 أكتوبر 2026: إنشاء report.md وتحديث README؛ التفريعة أُعيدت تسميتها «ali-abdulmalik»','اسم المستخدم يوحي بلقب «النفيعي» — غير مؤكد فلم يُضف.'),['program','project'],'','',True),
 ('أحمد باهويرث','Ahmad Bahwerith',PTS,COTS.format('14'),'ds',75,'gh1015',[['GitHub',GH+'Ahmed-Bah'],['مستودع التسليم',GH+'Ahmed-Bah/Global-CO2-Forecasting']],SRC_GH,tsd('14 أكتوبر 2026: «Final: AutoARIMA in harness»؛ التفريعة أُعيدت تسميتها «Global-CO2-Forecasting» — تنبؤ بانبعاثات CO2 العالمية'),['program','project'],'','',True),
 ('صبا صالح الغفيلي','Saba Saleh Alghufaili',PTS,COTS.format('14'),'ds',85,'gh1015',[['GitHub',GH+'uSebaa'],['مستودع التسليم',GH+'uSebaa/CyberPulse-Forecasting'],['LinkedIn',LI+'saba-alghofaili/']],SRC_GH,tsd('14 أكتوبر 2026: «Add CyberPulse forecasting notebook»؛ التفريعة أُعيدت تسميتها «CyberPulse-Forecasting»','ملف GitHub يحمل الاسم «Saba AlGhofaili» ويربط ملف LinkedIn نفسه.'),['program','project'],'','',True),
 ('لمى الدخيل الله','Lama Aldekheelallah',PAG,'أكتوبر 2026 (شهادة الاجتياز صادرة أكتوبر 2026؛ منشور الإتمام 14 أكتوبر 2026)','ai',85,'li1015',[['LinkedIn',LI+'lama-aldekheelallah-935b8b264/']],SRC_LI,'منشور LinkedIn (14 أكتوبر 2026): «earned the Certificate of Achievement in Advanced Agentic AI Systems Engineering from SDAIA Academy»، وقسم الشهادات يعرض «Advanced Agentic AI Systems Engineering — SDAIA | سدايا · Issued Oct 2026». شهادتان سابقتان من سدايا في قسم الشهادات: «Building Data Agents» (يناير 2026) و«Artificial intelligence concepts and advanced applications» (فبراير 2026) — لم تُضافا برنامجين لعدم التحقق من أنهما من برامج الأكاديمية. متدربة ضمان جودة في زين السعودية؛ خريجة علوم حاسب من جامعة الملك سعود.',['program','cert'],'','',True),
]
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
ENR=[
 (3308,[['LinkedIn',LI+'farah-al-rebh-b3b655350/']],'إثراء بدل تكرار: منشور LinkedIn «Farah Al Rebh» (14 أكتوبر 2026): ترشيحها لبرنامج «هندسة تطبيقات النماذج اللغوية الكبيرة LLMs» في الرياض قادمةً من البحرين مقر دراستها الجامعية، وقيادتها فريق المشروع العملي بلغة Python، واجتياز البرنامج مع Certificate of Achievement؛ وقسم الشهادات يعرض «Large Language Model Application Engineering — SDAIA | سدايا · Issued Oct 2026». يطابق هذا السجل بالاسم وشهر المختبرات (مستودع SDAIA-Farah-Hospital-AI-Labs) — ضُبط اسم البرنامج إلى هندسة تطبيقات النماذج اللغوية الكبيرة. متأهلة نهائية في Huawei AI Innovation Challenge 2025–2026.'),
 (3144,[['LinkedIn',LI+'norah-alshamikh-7179b6408/']],'منشور LinkedIn (14 أكتوبر 2026): «successfully completed the Vibe Coding & Agentic Engineering program with SDAIA Academy» — يؤكد إتمام البرنامج؛ أُضيف رابط الملف (طالبة علوم حاسب).'),
 (3070,[],'منشور LinkedIn (14 أكتوبر 2026): «اجتيازي وإتمامي بنجاح لبرنامج هندسة نظم الذكاء الاصطناعي الوكيل المتقدم (Advanced Agentic AI Systems Engineering) المقدم من SDAIA Academy» — يؤكد الإتمام (حواجز الحماية الطبقية، أمان الخوادم والصلاحيات، التتبع واختبارات الأمان).'),
 (2976,[['مستودع التسليم — السلاسل الزمنية',AP.format('Rawan-Alahmadi')]],'برنامج ثانٍ: تفريعة مستودع الأكاديمية «international-airpassengers-project» مع إيداعين للمالكة (15 أكتوبر 2026: «Complete capstone: analysis, harness, report») وسطر README «Submitted by: Rawan Alahmadi — academy: @SDAIAAcademy» — دورة السلاسل الزمنية، دفعة أكتوبر 2026.'),
 (2833,[['مستودع التسليم — السلاسل الزمنية',AP.format('abdullahf-77')]],'برنامج ثالث: تفريعة مستودع الأكاديمية «international-airpassengers-project» مع إيداعات المالك (14 أكتوبر 2026: «Complete capstone… Polish README for final submission») وسطر README «Submitted by: Abdullah Faisal Alsehli — academy: @SDAIAAcademy» — دورة السلاسل الزمنية، دفعة أكتوبر 2026.'),
 (2282,[['LinkedIn',LI+'1noura-alshahrani/']],'صفحة الخبرة على LinkedIn (حساب مسجَّل، قُرئت 15 أكتوبر 2026): «Data Management BootCamp — SDAIA · Internship · Oct 2023 – Nov 2023» ← «Data Management Consultant — Master Works · Full-time · Aug 2024 – Present» (تقييمات نضج حوكمة البيانات وفق NDMO وNDI، وأطر وسياسات الحوكمة، وورش PDPL لجهات حكومية ومالية) — و«T5 Artificial Intelligence and Data Science BootCamp — SDAIA · Jul 2024 – Oct 2024» متزامن مع بدء العمل. حاملة CDMP. ضُبطت الدفعات. PASS_DATED (+9 أشهر من إتمام معسكر إدارة البيانات، والارتباط مباشر) — مُرقّاة إلى قصة نجاح «noura-alshahrani». يحل محل الرابط الوسيط المحذوف في 27 أغسطس.'),
 (2295,[['LinkedIn',LI+'lujain-alattas-906998238/']],'صفحة الخبرة على LinkedIn (حساب مسجَّل، قُرئت 15 أكتوبر 2026): «Data Science & AI T5 Bootcamp — SDAIA · Mar 2024 – Jun 2024» و«Professional Training program in Large Language Models — SDAIA · Jul 2024 – Sep 2024» ← «Associate Consultant — Ascend Solutions · Full-time · Nov 2024 – Nov 2025» ← «Senior Business Analyst — Council Of Health Insurance · Jan 2026 – Present». ضُبطت الدفعات. فحص القصة: FAIL_RELATED — التعيين داخل النافذة (+2) استشاري عام بلا مهام بيانات/ذكاء اصطناعي موثّقة، والتعيين التالي (+16) خارج النافذة. يحل محل الرابط الوسيط المحذوف.'),
 (2319,[['LinkedIn',LI+'yazeed-alshurify/']],'رابط LinkedIn أكّدته الأكاديمية (15 أكتوبر 2026) — كان في السجل، وأُضيف الآن إلى بطاقة القصة «yazeed-alshurify».'),
 (26,[['LinkedIn',LI+'fares-altoukhi/']],'رابط LinkedIn مقدَّم من الأكاديمية (15 أكتوبر 2026) — أُضيف إلى السجل وإلى بطاقة القصة «fares-altoukhi».'),
 (2261,[['LinkedIn',LI+'hamad-almuahytheef/']],'رابط LinkedIn أكّدته الأكاديمية (15 أكتوبر 2026) — كان في السجل، وأُضيف الآن إلى بطاقة القصة «hamad-almuhaythif».'),
 (12,[['LinkedIn',LI+'wadha-m-almattar-phd-93b92a186/']],'رابط LinkedIn أكّدته الأكاديمية (15 أكتوبر 2026) — كان في السجل، وأُضيف الآن إلى بطاقة القصة «wadha-almattar».'),
]
COFIX={2282:'أكتوبر–نوفمبر 2023 (معسكر إدارة البيانات) · يوليو–أكتوبر 2024 (معسكر T5)',2295:'مارس–يونيو 2024 (معسكر T5) · يوليو–سبتمبر 2024 (النماذج اللغوية الكبيرة)'}
LOG=collections.Counter()
for k,lks,t in ENR:
    for lab,u in lks:
        if addlink(k,lab,u): LOG['link']+=1
    note(k,t); LOG['enr']+=1
for k,v in COFIX.items(): setf(k,'co',6,v)
G=g[3308-1]; G['prog']=PLLM+' (مختبرات المقرر على GitHub)'; ws.cell(3309,4).value=G['prog']
if 'cert' not in G['cats']: G['cats'].append('cert')
for k in (2976,2833):
    G=g[k-1]; G['prog']+=' + '+PTS; ws.cell(k+1,4).value=G['prog']
STORY_LINKS={'yazeed-alshurify':LI+'yazeed-alshurify/','fares-altoukhi':LI+'fares-altoukhi/','hamad-almuhaythif':LI+'hamad-almuahytheef/','wadha-almattar':LI+'wadha-m-almattar-phd-93b92a186/'}
ST=[dict(i=2282,id='noura-alshahrani',year=2023,name='نورة الشهراني',nameEn='Noura Alshahrani',role='مستشارة إدارة البيانات',org='ماستر ووركس (Master Works)',
      program='معسكر إدارة البيانات — أكاديمية سدايا (أكتوبر–نوفمبر 2023) + معسكر T5 للذكاء الاصطناعي وعلوم البيانات (يوليو–أكتوبر 2024)',period='أكتوبر–نوفمبر 2023',slug='1noura-alshahrani',
      quote='من معسكر إدارة البيانات إلى قيادة تقييمات نضج حوكمة البيانات لجهات حكومية ومالية.',
      impact='توظيف بدوام كامل «مستشارة إدارة البيانات» في ماستر ووركس في أغسطس 2024 — تسعة أشهر بعد إتمام معسكر إدارة البيانات.',
      story='أتمّت نورة معسكر إدارة البيانات بأكاديمية سدايا (أكتوبر–نوفمبر 2023). وفي أغسطس 2024 — بعد تسعة أشهر — التحقت بشركة ماستر ووركس مستشارةً لإدارة البيانات بدوام كامل، تقود تقييمات نضج حوكمة البيانات وفق إطاري مكتب إدارة البيانات الوطنية (NDMO) ومؤشر البيانات الوطني (NDI)، وتصمم أطر الحوكمة وسياساتها ومعاييرها، وتقدم ورش التوعية بنظام حماية البيانات الشخصية لجهات حكومية ومالية، وحصلت على اعتماد CDMP. وتزامن التحاقها مع معسكر T5 للذكاء الاصطناعي وعلوم البيانات بالأكاديمية (يوليو–أكتوبر 2024). النتيجة المحتسبة هي هذا التعيين، داخل نافذة الأربعة عشر شهرًا من إتمام معسكر إدارة البيانات، وفي صميم تخصصه.',
      ach=['إتمام معسكر إدارة البيانات — أكاديمية سدايا (نوفمبر 2023)','مستشارة إدارة البيانات — ماستر ووركس (أغسطس 2024)','اعتماد CDMP في إدارة البيانات','إتمام معسكر T5 للذكاء الاصطناعي وعلوم البيانات (أكتوبر 2024)'],
      exp='Data Management BootCamp — سدايا، أكتوبر–نوفمبر 2023؛ ماستر ووركس — Data Management Consultant، دوام كامل، أغسطس 2024 – الآن؛ ومعسكر T5 — سدايا، يوليو–أكتوبر 2024')]
stories=[]
for p in ST:
    G=g[p['i']-1]
    st={"id":p['id'],"year":p['year'],"quote":{"text":p['quote'],"kind":"draft"},"name":p['name'],"nameEn":p['nameEn'],"photo":None,
        "role":p['role'],"org":p['org'],"orgLogo":"assets/master-works.png","program":p['program'],"period":p['period'],
        "category":"employment","categories":["employment"],"impact":p['impact'],"story":p['story'],"achievements":p['ach'],
        "links":[{"label":"LinkedIn","url":LI+p['slug']+'/'}],
        "provenance":f"صفحة الخبرة على LinkedIn بحساب مسجَّل (قُرئت {DATE})، بتواريخ بمستوى الشهر: {p['exp']} + سجل الأكاديمية #{p['i']}."}
    stories.append(st)
    G['emp']=p['org']; G['role']=p['role']; ws.cell(p['i']+1,7).value=p['org']; ws.cell(p['i']+1,8).value=p['role']
    if 'job' not in G['cats']: G['cats'].append('job')
NS=len(stories); S0=169; S1=S0+NS; E0=91; E1=E0
N=len(g); T=collections.Counter(r['tr'] for r in g)
wl=sum(1 for r in g if r.get('links')); uu=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
print('N',N0,'->',N,{k:(T0[k],T[k]) for k in T},'wl',wl0,'->',wl,'uu',uu0,'->',uu,dict(LOG),'new',new_ids[0],'-',new_ids[-1],'stories',S1,'emp',E1)
print('matches',MATCHLOG)
for t in [json.dumps(x,ensure_ascii=False) for x in stories]+[g[k-1]['d'] for k,_,_ in ENR]+[g[k-1]['d'] for k in new_ids]: assert '**' not in t
if DRY: sys.exit(0)
TOT=format(N,','); OTOT=format(N0,',')
VA_O='إصدار 13 أكتوبر 2026 (جولة سد الفجوات والخريجين الجدد وفحص القصص'; VA_N='إصدار 15 أكتوبر 2026 (جولة الخريجين الجدد وفحص القصص والتدقيق والتنظيف'
VE_O='version 13 October 2026 (gap-fill, new-graduates and story-check round'; VE_N='version 15 October 2026 (new-graduates, story-check, QA and cleaning round'
def stc(t):
    t=t.replace(OTOT,TOT)
    for a,b in (('%d قصة'%S0,'%d قصة'%S1),('%d stories'%S0,'%d stories'%S1),('%d verified success stories'%S0,'%d verified success stories'%S1)):
        t=t.replace(a,b)
    return t
head=stc(head).replace(VA_O,VA_N).replace(VE_O,VE_N); tail=stc(tail).replace(VA_O,VA_N).replace(VE_O,VE_N)
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
s=rep(s,'data-count="%d"'%N0,'data-count="%d"'%N,1); s=rep(s,'data-count="%d"'%S0,'data-count="%d"'%S1,1)
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
# story-card LinkedIn links supplied by the Academy
lines=s.split('\n'); done=0
for ix,ln in enumerate(lines):
    for sid,url in STORY_LINKS.items():
        if ln.startswith('  {"id": "%s",'%sid):
            body=ln.strip(); comma=body.endswith(','); obj=json.loads(body.rstrip(','))
            if not any(norm(l['url'])==norm(url) for l in obj['links']):
                obj['links'].insert(0,{"label":"LinkedIn","url":url}); done+=1
            lines[ix]='  '+json.dumps(obj,ensure_ascii=False)+(',' if comma else '')
s='\n'.join(lines); assert done==4,done
k=s.index('const STORIES = ['); e=s.index('\n];',k)
prev=s[:e].rstrip()
if not prev.endswith(','): prev+=','
s=prev+'\n'+',\n'.join('  '+json.dumps(x,ensure_ascii=False) for x in stories)+s[e:]
s=rep(s,"'use strict';","/* %s: جولة الخريجين الجدد وفحص القصص والتدقيق والتنظيف — %s ← %s خريجًا (%d سجلًا جديدًا · %d إثراءات)؛ القصص %d ← %d (noura-alshahrani)؛ روابط LinkedIn أُضيفت إلى 4 بطاقات (yazeed-alshurify · fares-altoukhi · hamad-almuhaythif · wadha-almattar)؛ جهات العمل %d (دون تغيير). */\n'use strict';"%(DATE,OTOT,TOT,len(new_ids),LOG['enr'],S0,S1,E1),1)
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
   'تحديث':f'{DATE} — جولة الخريجين الجدد وفحص القصص والتدقيق والتنظيف: {len(new_ids)} سجلًا جديدًا ({OTOT} → {TOT})؛ {LOG["enr"]} إثراءات؛ القصص {S0} → {S1}؛ جهات العمل {E1}'}
for row in st.iter_rows():
    if row[0].value in M: row[1].value=M[row[0].value]
sh=wb.create_sheet('جولة_15_أكتوبر_2026'); sh.append(['#','الاسم','النوع','التفصيل'])
for k in new_ids: sh.append([k,g[k-1]['n'],'سجل جديد ('+('GitHub' if g[k-1]['lv']=='gh1015' else 'LinkedIn')+')',g[k-1]['prog']])
for k,_,t in ENR: sh.append([k,g[k-1]['n'],'إثراء',t[:140]])
for x,p in zip(stories,ST): sh.append([p['i'],x['name'],'قصة جديدة',x['org']+' — '+x['role']])
wb.save(X_)
P5=H+'Graduates/Graduates_Database.md'; s=open(P5,encoding='utf-8').read()
s=rep(s,'**الإصدار:** 13 أكتوبر 2026 — ','**الإصدار:** %s — جولة الخريجين الجدد وفحص القصص والتدقيق والتنظيف (%s → %s · القصص %d → %d · جهات العمل %d). قبله: 13 أكتوبر 2026 — '%(DATE,OTOT,TOT,S0,S1,E1),1)
TSN=[k for k in new_ids if g[k-1]['lv']=='gh1015']
L=['## جولة الخريجين الجدد وفحص القصص والتدقيق والتنظيف — %s'%DATE,'',f'**الخريجون {OTOT} → {TOT} · القصص {S0} → {S1} · جهات العمل {E1} (دون تغيير).**','',
 f'**1) سجلات جديدة ({len(new_ids)}):** {len(TSN)} من دفعة أكتوبر 2026 لدورة السلاسل الزمنية (تفريعات «international-airpassengers-project» مع إيداعات المالكين وسطر «Submitted by» — 14–15 أكتوبر)، و{len(new_ids)-len(TSN)} من منشورات LinkedIn.','','| # | الاسم | الاسم الإنجليزي | البرنامج | الدفعة | المسار | المصدر |','|---|---|---|---|---|---|---|']
for k in new_ids:
    G_=g[k-1]; L.append(f"| {k} | {G_['n']} | {G_['en']} | {G_['prog']} | {G_['co']} | {G_['tr']} | {G_['links'][0][1]} |")
L+=['',f"**2) الإثراء ({LOG['enr']}):** "+' · '.join('#%d %s'%(k,g[k-1]['n']) for k,_,_ in ENR)+' — #3308 فرح الربح: منشور LinkedIn كان سيصبح سجلًا مكررًا، فأُثري السجل القائم وضُبط برنامجه إلى هندسة تطبيقات النماذج اللغوية الكبيرة؛ #2976 و#2833 برنامج إضافي (السلاسل الزمنية، أكتوبر 2026)؛ #3144 و#3070 منشورات إتمام؛ #2282 و#2295 صفحات خبرة بحساب مسجَّل ضبطت الدفعات؛ و4 سجلات قصص أُكّدت روابطها من الأكاديمية.','',
 '**3) قصة جديدة (1) — معيار الأربعة عشر شهرًا:** noura-alshahrani (#2282، معسكر إدارة البيانات أكتوبر–نوفمبر 2023 ← مستشارة إدارة البيانات، ماستر ووركس، أغسطس 2024، +9 أشهر). مرفوض: لجين العطاس (#2295) FAIL_RELATED. معلّق: سعد الزهراني (#42) ويوسف اللحياني (#2278) — لا ملف LinkedIn مطابق بسمتين. وأُضيفت روابط LinkedIn المقدّمة من الأكاديمية إلى 4 بطاقات قصص؛ بقيت بطاقة جهاد الجازي وحدها بلا رابط LinkedIn ضمن قصص 2024–2026.','',
 '**4) معلّق:** shahad12345fg (تسليم بلا اسم) · shahadho123 وLayanharbi9 (تفريعات بلا إيداعات) · Mohanad Alghanim (قبول في هندسة البيانات الحديثة — لم يبدأ) · Alhanouf R. Aldossary (اليوم الأول من ورشة — لم تكتمل) · ABEER AL-GHAMDI وAreej Alshareef (شهادة إنجاز من سدايا دون اسم البرنامج). مستبعد: Najla A. Alsaidalani وMiad Alresheedi (مبادرة «سماي» — ليست برنامجًا للأكاديمية) · Saleh Almahmoud (منصة ساعي). مستودع «SDAIAAcademy/applied-nlp» ما زال بلا تفريعات.','','---','']
k=s.index('## جولة سد الفجوات والخريجين الجدد وفحص القصص — 13 أكتوبر 2026')
s=s[:k]+'\n'.join(L)+'\n'+s[k:]
open(P5,'w',encoding='utf-8').write(s)
for f in ('index.html','Graduates/index.html'):
    t=open(H+f,encoding='utf-8').read(); print(f,'leftover',OTOT,t.count(OTOT),'%d قصة'%S0,t.count('%d قصة'%S0),'new',t.count(TOT))
print('done',new_ids,S1,E1)
