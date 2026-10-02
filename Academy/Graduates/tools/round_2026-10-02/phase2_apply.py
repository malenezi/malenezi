import json,openpyxl
SRC='مسح منشورات LinkedIn (حساب مسجَّل) لإتمام برامج أكاديمية سدايا — 2 أكتوبر 2026'
TR={'ai':'مهندس ذكاء اصطناعي — AI Engineer','ds':'عالم بيانات — Data Scientist','other':'برامج متخصصة أخرى — Other / Specialized'}
TL=' تنويه: الاسم العربي نقل حرفي عن الاسم اللاتيني المنشور — غير متحقق علنًا.'
LI=lambda s:'https://www.linkedin.com/in/'+s+'/'
NEW=[
 dict(n='البندري العتيبي',en='Albandri Alotaibi',prog='هندسة البيانات الحديثة لأنظمة الذكاء الاصطناعي (Modern Data Engineering for AI Systems) — أكاديمية سدايا',tr='ds',co='سبتمبر 2026 (منشور الإتمام 27 سبتمبر 2026)',edu='',score=82,li='albandri-alotaibi-707942276',
  d='منشور إتمام من الشخص نفسه: «Modern Data Engineering program with SDAIA Academy» مع شهادة اجتياز (Certificate of Achievement). عتبة الهوية مستوفاة بسمتين: الاسم الكامل على الملف الشخصي + منشور ذاتي يسمّي البرنامج والأكاديمية، والعنوان المهني «Data Analyst | Power BI, SQL, Python | AWS Certified | Data Engineering».'+TL),
 dict(n='بيان الخالدي',en='Bayan Alkhaldi',prog='التجارب واختبارات A/B والاستدلال السببي (SDA-DSC-213 — Experimentation & Causal Inference) — أكاديمية سدايا',tr='ds',co='سبتمبر 2026 (منشور الإتمام 21 سبتمبر 2026)',edu='Information Systems & Business Analytics — Imam Abdulrahman Bin Faisal University (IAU)',score=82,li='bayanalkhaldi',
  d='منشور إتمام من الشخص نفسه: «Experimentation, A/B Testing & Causal Inference program with SDAIA | سدايا». عتبة الهوية مستوفاة: الاسم الكامل على الملف الشخصي + منشور ذاتي يسمّي البرنامج + العنوان المهني (خريجة نظم معلومات وتحليلات أعمال، جامعة الإمام عبدالرحمن بن فيصل).'+TL),
 dict(n='سارة الشهراني',en='Sara Alshahrany',prog='هندسة تطبيقات النماذج اللغوية الكبيرة (SDA-AIE-213 — LLM Application Engineering) — أكاديمية سدايا',tr='ai',co='سبتمبر 2026 (منشور الإتمام 20 سبتمبر 2026)',edu='Computer Science — Princess Nourah bint Abdulrahman University (PNU)',score=84,li='sara-alshahrany-a3bb0931b',
  d='منشور إتمام من الشخص نفسه: «LLM Application Engineering program at SDAIA Academy» مع صورة شهادة الاجتياز وصور من مقر البرنامج. عتبة الهوية مستوفاة: الاسم الكامل على الملف الشخصي + منشور ذاتي بشهادة + العنوان المهني (خريجة علوم حاسب من جامعة الأميرة نورة، متدربة سابقة في stc، CAPM).'+TL),
 dict(n='يزيد الحيدر',en='Yazeed AlHaidar',prog='أساليب تعلم الآلة المتقدمة (Advanced Machine Learning Methods) — أكاديمية سدايا',tr='ai',co='سبتمبر 2026 (منشور الإتمام 15 سبتمبر 2026)',edu='',score=80,li='yazeed-alhaidar-019038252',
  d='منشور إتمام من الشخص نفسه بالعربية: «شهادة اجتياز مسار أساليب تعلم الآلة المتقدمة من أكاديمية سدايا (SDAIA Academy)». عتبة الهوية مستوفاة: الاسم الكامل على الملف الشخصي + منشور ذاتي يسمّي البرنامج والأكاديمية.'+TL),
 dict(n='لمى خالد الرشيد',en='Lama Khalid Alrsheed',prog='أساليب تعلم الآلة المتقدمة (Advanced Machine Learning Methods) — أكاديمية سدايا',tr='ai',co='6–9 سبتمبر 2026',edu='',score=90,li='lama-alrasheed1',
  d='منشور إتمام من الشخص نفسه مع صورة شهادة الاجتياز الصادرة من سدايا: «Lama Khalid Alrsheed / لمى خالد الرشيد — أساليب تعلم الآلة المتقدمة (Advanced Machine Learning Methods) — من 6/9/2026 إلى 9/9/2026». الاسمان العربي والإنجليزي متحققان من الشهادة نفسها.'),
 dict(n='حسين العبدالله',en='Hussain Alabdullah',prog='معسكر الحوسبة الكمية (Quantum Computing Bootcamp) — سدايا',tr='other',co='مارس 2026 (إعلان الشهادة 2 مارس 2026)',edu='Computer Science — King Fahd University of Petroleum & Minerals (KFUPM) — طالب',score=72,li='hussain-alabdullah-289b93347',
  d='منشور «Celebrating a new certification» من الشخص نفسه: «Quantum Computing Bootcamp from SDAIA | سدايا». عتبة الهوية مستوفاة: الاسم الكامل على الملف الشخصي + العنوان المهني (طالب علوم حاسب في جامعة الملك فهد للبترول والمعادن). تنويه برنامج: المعسكر صادر باسم سدايا ويُستضاف في مراكز تستضيف برامج الأكاديمية (DAICO)، ولم يُعثر على صفحة رسمية تسمّيه ضمن برامج أكاديمية سدايا — يلزم تأكيد تبعيته.'+TL),
 dict(n='فارس عبدالله',en='Faris Abdullah',prog='معسكر الحوسبة الكمية (Quantum Computing Bootcamp) — سدايا بالشراكة مع الجمعية السعودية للحوسبة الكمية (ISQA)',tr='other',co='فبراير 2026 (منشور الإتمام 25 فبراير 2026)',edu='Computer Engineering — King Fahd University of Petroleum & Minerals (KFUPM) — طالب',score=72,li='faris-abdullah-h',
  d='منشور إتمام من الشخص نفسه: «completed the Quantum Computing Bootcamp organized by SDAIA and the Saudi Quantum Computing Association (ISQA)» بالعمل على IBM Qiskit (الدوائر الكمية، التراكب، التشابك، الخوارزميات الكمية). عتبة الهوية مستوفاة: الاسم المعروض + العنوان المهني (هندسة حاسب في جامعة الملك فهد للبترول والمعادن، من خريجي موهبة). تنويه: «عبدالله» قد يكون اسم الأب لا اللقب. تنويه برنامج كما في السجل السابق.'+TL),
 dict(n='سما الحربي',en='Sama Alharbi',prog='بناء أنظمة وكلاء الذكاء الاصطناعي (Building Agentic AI Systems) — أكاديمية سدايا',tr='ai',co='سبتمبر 2026 (منشور الإتمام 20 سبتمبر 2026)',edu='',score=80,li='sama-alharbi-831753201',
  d='منشور إتمام من الشخص نفسه: «completed the Building Agentic AI Systems program by SDAIA Academy». عتبة الهوية مستوفاة: الاسم الكامل على الملف الشخصي + منشور ذاتي يسمّي البرنامج. إشارة متبادلة غير مدموجة: #39 «سما الحربي» (معسكر T5 ~2024، بلا ملف LinkedIn) — اسم شائع بلا معزّز مشترك.'+TL),
]
TAG='[مسح منشورات LinkedIn — 2 أكتوبر 2026] '
ENR={2048:dict(en='Yara Al-Hazzaee',li='yara-al-hazzaee-399636383',d='منشور من الشخص نفسه (يونيو 2026): حضور «Quantum Computing Bootcamp» المقدّم من سدايا بمركز DAICO — برنامج ثانٍ. الملف: طالبة في جامعة الملك سعود. المطابقة بالاسم الأول واللقب المميّز (الهزاعي ↔ Al-Hazzaee).'),
 2949:dict(li='lamaaldaej',d='منشور إتمام من الشخص نفسه (20 سبتمبر 2026): «أتممت برنامج هندسة أنظمة الذكاء الاصطناعي التوليدي المتقدمة المقدم من أكاديمية سدايا» — برنامج ثانٍ، ورابط LinkedIn مضاف. المطابقة بالاسم الكامل المميّز (الدعيج) والشهر نفسه.'),
 3020:dict(li='manar-albader-317240275',d='منشور إتمام من الشخص نفسه مع صورة الشهادة: «Manar Abdulla Albader / منار عبدالله البدر — هندسة البيانات الحديثة لأنظمة الذكاء الاصطناعي، من 13/9/2026 إلى 17/9/2026» — الاسم العربي متحقق الآن من الشهادة. ومنشور ثانٍ (17 سبتمبر 2026): إتمام «Large Language Model Application Engineering» من أكاديمية سدايا — برنامج ثانٍ.'),
 3180:dict(li='sarah-alshabib-811563339',d='الملف الشخصي موسوم في منشور زميلتها تالين العمار عن إتمام «Computer Vision for Developers» — أُضيف الرابط بالوسم المباشر.')}
P1=json.load(open('tools/round_2026-10-02/phase1_pending.json'))
wb=openpyxl.load_workbook('Graduates_Database.xlsx'); ws=wb['قاعدة البيانات']
last=ws.max_row
while ws.cell(last,1).value is None: last-=1
nid=ws.cell(last,1).value; assert nid==3180
p='index.html'; s=open(p,encoding='utf-8').read()
i0=s.index('const DATA = {"grads"'); j=s.index('[',i0); d=0;k=j
while True:
    c=s[k]
    if c=='[': d+=1
    elif c==']':
        d-=1
        if d==0: break
    elif c=='"':
        k+=1
        while s[k]!='"':
            if s[k]=='\\': k+=1
            k+=1
    k+=1
g=json.loads(s[j:k+1]); assert len(g)==3180
for rec in NEW:
    nid+=1; r=last+(nid-3180)
    vals=[nid,rec['n'],rec['en'],rec['prog'],TR[rec['tr']],rec['co'],None,None,None,rec['edu'] or None,'li1002',rec['score'],'ضمن النطاق','برنامج',LI(rec['li']),None,None,None,None,None,rec['d'],None,SRC]
    for ci,v in enumerate(vals,1): ws.cell(r,ci).value=v
    g.append({"n":rec['n'],"en":rec['en'],"lv":"li1002","score":rec['score'],"prog":rec['prog'],"co":rec['co'],"win":"ضمن النطاق","edu":rec['edu'],"emp":"","role":"","cats":["program"],"d":rec['d'],"links":[["LinkedIn",LI(rec['li'])]],"src":SRC,"tr":rec['tr']})
for i,e in ENR.items():
    r=i+1; assert ws.cell(r,1).value==i
    if e.get('en') and not ws.cell(r,3).value: ws.cell(r,3).value=e['en']
    cur=ws.cell(r,15).value; ws.cell(r,15).value=(cur+' · ' if cur else '')+LI(e['li'])
    ws.cell(r,21).value=(ws.cell(r,21).value or '')+' '+TAG+e['d']
    G=g[i-1]; assert G['n']==ws.cell(r,2).value
    if e.get('en') and not G.get('en'): G['en']=e['en']
    G['links']=(G.get('links') or [])+[["LinkedIn",LI(e['li'])]]; G['d']=(G.get('d') or '')+' '+TAG+e['d']
for i,(co,note) in P1.items():
    i=int(i); r=i+1; old=ws.cell(r,6).value; ws.cell(r,6).value=co
    t=' [إكمال الفجوات — 2 أكتوبر 2026] تاريخ الإتمام من قسم الشهادات على LinkedIn (حساب مسجَّل): '+note+f'. (كانت الدفعة: «{old}»).'
    ws.cell(r,21).value=(ws.cell(r,21).value or '')+t
    G=g[i-1]; assert G['n']==ws.cell(r,2).value; G['co']=co; G['d']+=t
wb.save('Graduates_Database.xlsx')
s=s[:j]+json.dumps(g,ensure_ascii=False)+s[k+1:]; open(p,'w',encoding='utf-8').write(s)
print('records',len(g))
