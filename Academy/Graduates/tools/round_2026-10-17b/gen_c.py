# -*- coding: utf-8 -*-
import json
exec(open('gen_a.py',encoding='utf-8').read()); exec(open('gen_b.py',encoding='utf-8').read())
LI='https://www.linkedin.com/in/'
NEW=[]
for ar,en,key,co,sc,slug,d,cx in L+L2:
    prog,tr=P[key]; NEW.append([ar,en,prog,co,tr,sc,'li1017b',[['LinkedIn',LI+slug+'/']],SRC_LI,'منشور LinkedIn: '+d,['program']+cx,'','',True])
for ar,en,key,co,sc,links,d,cx in GH:
    prog,tr=P[key]; NEW.append([ar,en,prog,co,tr,sc,'gh1017b',links,SRC_GH,d,['program']+cx,'','',True])
assert len(NEW)==58, len(NEW)
WID=3408+[x[1] for x in NEW].index('Waleed Alsirhani')+1
T='منشور إتمام/شهادة على LinkedIn (حساب مسجَّل، جولة 17 أكتوبر 2026 ب) يطابق الاسم والبرنامج والفترة في السجل الداخلي — أُضيف الرابط العلني والاسم اللاتيني.'
E1=[(1908,'Rawan Almutlaq','rawan-almutlaq-msc-36a51290','CDMP، منشور 26 أبريل 2026'),(1972,'Salman Almajed','salman-almajed-0690693b4','Vibe Coding، منشور 22 أبريل 2026'),
(1583,'Fayez Alhafta','fayez-alhafta','معسكر محترفي الذكاء الاصطناعي، منشور 12 فبراير 2026'),(2100,'Refal Alzweaid','refal-alzweaid-itil-218012245','معسكر محترفي الذكاء الاصطناعي، منشور 19 مايو 2026'),
(2091,'Hatim Alharbi','alharbi-hatim','معسكر محترفي الذكاء الاصطناعي، منشور 12 فبراير 2026'),(2085,'Arwa Almarshadi','arwa-almarshadi-90a614285','معسكر محترفي الذكاء الاصطناعي، منشور 6 فبراير 2026'),
(2114,'Abdulrahman Al-Yami','abdulrahman-alyami-6008ab2ab','معسكر محترفي الذكاء الاصطناعي، منشور 8 فبراير 2026'),(1597,'Amnah Kariri','amnah-n-kariri-a1a1ab349','Vibe Coding، منشور 26 يونيو 2026'),
(2060,'Meshari Bin Anzan','meshari-bin-anzan-40a4753b3','Vibe Coding، منشور 3 مارس 2026'),(1524,'Nada Al-Mutairi','nada-al-mutairi-77102325b','Vibe Coding 23–26 فبراير 2026، منشور 3 مارس 2026'),
(1662,'Turki Alomran','turki-alomran-146462336','الذكاء الاصطناعي التطبيقي، منشور 11 يونيو 2026'),(1682,'Moath Alharthi','moath-alharthi-ai','الذكاء الاصطناعي التطبيقي، منشور 8 يونيو 2026'),
(1671,'Sulaiman Alfawzan','sulaiman-alfawzan','الذكاء الاصطناعي التطبيقي، منشور 7 يونيو 2026'),(1827,'Lujain Alabduljabbar','lujain-alabduljabbar-454109100','نمذجة البيانات ومستودعاتها، منشور 17 مايو 2026'),
(1625,'Shahad AlShayiqi','shahad-alshayiqi','نمذجة وتكامل البيانات، منشور 12 مايو 2026'),(1579,'Shatha Alhasani','shatha-badr-alhasaani','هندسة الأنظمة التوكيلية المتقدمة، منشور 7 يوليو 2026'),
(1858,'Renad Aljuraywi','renad-aljuraywi','تطوير حلول الذكاء الاصطناعي التوليدي، منشور 21 مايو 2026'),(1753,'Abdullah Al Zahrani','abdullah-al-zahrani-a09a11371','تطوير حلول الذكاء الاصطناعي التوليدي، منشور 19 مايو 2026'),
(2088,'Basel Helal Felemban','basel-helal-felemban-931b5723a','معسكر محترفي الذكاء الاصطناعي، منشور 15 فبراير 2026'),(1763,'Mawaheb Altuwaijri','mawaheb-altuwaijri-400b4869','تطوير حلول الذكاء الاصطناعي التوليدي، منشور 8 يونيو 2026'),
(2099,'Ruba Alsulami',None,'مستودع «Nabahan» على GitHub: «Project developed for AI Professionals Bootcamp | SDAIA»'),(968,'Faisal Almufarrih',None,'ملف GitHub: «ML Practitioner Bootcamp – SDAIA»'),
]
ENR=[]
for k,en,slug,t in E1:
    links=[['LinkedIn',LI+slug+'/']] if slug else []
    if k==2099: links=[['GitHub','https://github.com/justRuba'],['LinkedIn',LI+'ruba-alsulami-a05b172b5/']]
    if k==968: links=[['GitHub','https://github.com/faisaluty25'],['LinkedIn',LI+'faisal-almufarrih-b8090628b/']]
    ENR.append({'k':k,'en':'','set_en':en,'links':links,'t':(T if slug else 'ملف GitHub يسمّي برنامج الأكاديمية ويطابق الاسم الكامل والبرنامج في السجل الداخلي — أُضيف الرابطان والاسم اللاتيني.')+' ('+t+')'})
E2=[(1606,'','Shemah Alrwaily','shemah-alrwaily-91b83a313','اجتياز «تطوير حلول الذكاء الاصطناعي التوليدي» (منشور 10 يونيو 2026) — برنامج ثانٍ.','تطوير حلول الذكاء الاصطناعي التوليدي (يونيو 2026)'),
(2211,'Sarah Almohreb',None,'sarah-almohareb-005182363','إتمام Advanced Agentic AI Systems Engineering وشهادة الاجتياز (منشور 13 أغسطس 2026) — برنامج ثانٍ؛ مشروع StudyFlow AI.','هندسة أنظمة الذكاء الاصطناعي التوكيلي المتقدمة (أغسطس 2026)'),
(3121,'Daniyah Aleid',None,'daniyah-al-eid-6a9254244','اجتياز Modern Data Engineering for AI Systems (منشور 19 سبتمبر 2026) يطابق مستودع capstone المسجّل.','هندسة البيانات الحديثة لأنظمة الذكاء الاصطناعي (سبتمبر 2026)'),
(2973,'Yasser Ahmed Alasiri',None,'yasser-al-asiri-39479822a','منشور «completed the Agentic AI Systems Program certificate from SDAIA Academy» (26 أغسطس 2026).',None),
(2828,'Mohammed Turkistani',None,'mohammedaturkistani','منشور إتمام ورشة Vibe Coding ضمن برنامج AthkaX (2 سبتمبر 2026).',None),
(2341,'Saleh Almahmoud',None,'saleh-almahmoud-skm','منشور إتمام برنامج Prompt Engineering and Responsible AI Use (17 أغسطس 2026).',None),
(383,'Lama Abdullah Saeed Alghamdi',None,'lama-alghamdi-39a61b240','منشور إتمام التدريب الاحترافي في النماذج اللغوية الكبيرة برعاية أكاديمية سدايا ونيل NCA-GENL.',None),
(392,'Joud Saqer Aziz Alanazi',None,'joud-saqer-alanazi-002806270','منشور نيل NVIDIA Certified Associate – Generative AI & LLMs ضمن برنامج سدايا الاحترافي.',None),
(240,'Sumayyah Alamoudi',None,'sumayyahalamoudi','منشور إتمام NVIDIA LLM Professional Training Program برعاية سدايا (7 مايو).',None),
(198,'Yazeed Mohammed Ali Alobaidan',None,'yazeedalobaidan','منشور إتمام دورات NVIDIA ضمن برنامج سدايا؛ صفحة الخبرة: Aljazira Bank — Data and AI GDP (أغسطس 2025) ثم AI & Data Analytics Assistant Manager (أغسطس 2026).',None),
(48,'Abdulaziz Almousa',None,'abdalaziz-almousa','منشور «officially completed the SDAIA Applied AI Bootcamp» (24 مايو 2026).',None),
(3107,'Hatem Alawwad',None,'hatem-alawwad','صفحة الخبرة: Software Developer — EJADA (أكتوبر 2025)؛ دور برمجي عام لا يُحتسب قصة (الصلة بالتدريب).',None),
(149,'Hams Alshadwi',None,'hams-alshadwi-33a80525a','رابط الملف الشخصي (الدليل الأصلي منشور طرف ثالث يذكر شهادة ML Practitioner من أكاديمية سدايا).',None),
(3319,'Fahad Alqahtani',None,'fahad-alqahtani-7b19aa35a','منشور «شهادة اجتياز برنامج ممارسات هندسة البرمجيات لأنظمة الذكاء الاصطناعي» (27 سبتمبر 2026).',None),
(3010,'Amal Alotaibi',None,'amal-alotaibi-44111b283','منشور إتمام Modern Data Engineering for AI Systems (17 سبتمبر 2026).',None),
(2217,'Faisal Al-Abdul-Jabbar',None,'faisal-alabduljabbar-132708371','منشور «received a Certificate of Achievement from SDAIA for completing the Vibe Coding program» (23 يوليو 2026).',None),
(1684,'','Hajer Aldhafairi','hajer-aldhafairi-985a74317','منشور «شهادة اجتياز برنامج Generative AI for Productivity» من سدايا (18 سبتمبر 2026) — برنامج ثانٍ؛ الاسم نادر ويطابق السجل الداخلي.','الذكاء الاصطناعي التوليدي لإنتاجية العمل (سبتمبر 2026)'),
(1804,'','Abdulla Asswailem','abdulla-asswailem','منشور «شهادة اجتياز برنامج Certified Data Management Professional (CDMP) من سدايا» (12 مايو 2026) يطابق السجل الداخلي (2026-05-10).',None),
(1870,'','Anfal Alnafisa','anfal-alnafisah','منشور اجتياز «نمذجة وتصميم البيانات ومستودعات البيانات وذكاء الأعمال» من سدايا (12 مايو 2026) يطابق السجل الداخلي.',None),
(1517,'','Abdulrahman Aljaber','abdulrahman-aljaber-98b9943b4','منشور إتمام Vibe Coding وشهادة الإنجاز (27 يوليو 2026) — برنامج ثانٍ بعد «رؤية الحاسب للمطورين» (يوليو 2026).','البرمجة التوليدية (Vibe Coding) — يوليو 2026'),
(3146,'Ruba Alanazi',None,'ruba-alanzi-2a9757422','منشور «حصولي على شهادة في البرمجة التوليدية الـ vibe coding المقدمة من أكاديمية سدايا» (1 أكتوبر 2026).',None),
(1961,'','Afnan Abdullah Alnofal','afnan-abdullah-alnofal','منشور «سعدت باجتياز برنامج البرمجة التوليدية (Vibe Coding)» من سدايا (21 أبريل 2026) يطابق السجل الداخلي (2026-04-19).',None),
]
for k,en,set_en,slug,t,pa in E2:
    e={'k':k,'en':en if en is not None else set_en,'links':[['LinkedIn',LI+slug+'/']],'t':t}
    if en=='' : e['en']=''; e['set_en']=set_en
    if pa: e['prog_add']=pa
    ENR.append(e)
ST=[
{'i':1583,'id':'fayez-alhafta','year':2026,'name':'فايز الهفتاء','nameEn':'Fayez Alhafta','role':'أخصائي حلول الذكاء الاصطناعي','role_db':'أخصائي حلول الذكاء الاصطناعي (Ai Solutions Specialist) — رشد للحلول، سبتمبر 2026','org':'رشد للحلول (Rushd Solutions)','orgLogo':None,'photo':None,
 'program':'معسكر أكاديمية سدايا لمحترفي الذكاء الاصطناعي (ديسمبر 2025 – فبراير 2026) + هندسة أنظمة الذكاء الاصطناعي التوكيلي المتقدمة (يونيو 2026)','period':'ديسمبر 2025 – يونيو 2026','slug':'fayez-alhafta',
 'quote':'من معسكر محترفي الذكاء الاصطناعي والأنظمة التوكيلية إلى بناء حلول الذكاء الاصطناعي للمؤسسات.',
 'impact':'توظيف بدوام كامل «أخصائي حلول الذكاء الاصطناعي» في رشد للحلول في سبتمبر 2026 — سبعة أشهر بعد المعسكر وثلاثة بعد برنامج الأنظمة التوكيلية.',
 'story':'أتمّ فايز معسكر أكاديمية سدايا لمحترفي الذكاء الاصطناعي (ديسمبر 2025 – فبراير 2026) في الذكاء الاصطناعي التوليدي والنماذج اللغوية الكبيرة، ثم برنامج هندسة أنظمة الذكاء الاصطناعي التوكيلي المتقدمة (يونيو 2026). وفي سبتمبر 2026 التحق برشد للحلول بدوام كامل «أخصائيَّ حلول الذكاء الاصطناعي»، يعمل على منتجات الذكاء الاصطناعي المؤسسية والوكلاء والأتمتة مع العملاء. النتيجة المحتسبة هي هذا التعيين بدوام كامل، داخل نافذة الأربعة عشر شهرًا وفي صميم ما تدرّب عليه. وكان قد عمل لدى الجهة نفسها بدوام جزئي مختبرًا للوكلاء (أكتوبر 2025 – يناير 2026) قبل المعسكر، فلا يُحتسب ذلك الدور.',
 'ach':['إتمام معسكر أكاديمية سدايا لمحترفي الذكاء الاصطناعي (فبراير 2026)','إتمام هندسة أنظمة الذكاء الاصطناعي التوكيلي المتقدمة (يونيو 2026)','أخصائي حلول الذكاء الاصطناعي بدوام كامل — رشد للحلول (سبتمبر 2026)'],
 'exp':'Rushd Solutions — Ai Solutions Specialist، دوام كامل، سبتمبر 2026 – الآن (وقبله AI Agent Tester & Prompt Engineer بدوام جزئي، أكتوبر 2025 – يناير 2026)؛ منشور إتمام المعسكر 12 فبراير 2026',
 'note':'صفحة الخبرة على LinkedIn (حساب مسجَّل، قُرئت 17 أكتوبر 2026): «Ai Solutions Specialist — Rushd Solutions · Full-time · Sep 2026 – Present». PASS_DATED (+7 من المعسكر، +3 من البرنامج التوكيلي). الدور الجزئي السابق لدى الجهة نفسها بدأ قبل المعسكر فلا يُحتسب. مُرقّى إلى قصة نجاح «fayez-alhafta».'},
{'i':WID,'id':'waleed-alsirhani','year':2026,'name':'وليد السرحاني','nameEn':'Waleed Alsirhani','role':'مهندس ذكاء اصطناعي','role_db':'مهندس ذكاء اصطناعي (Artificial Intelligence Engineer) — دراية المالية، سبتمبر 2026','org':'دراية المالية (Derayah Financial)','orgLogo':None,'photo':None,
 'program':'تطوير حلول الذكاء الاصطناعي التوليدي — أكاديمية سدايا (26–30 أبريل 2026)','period':'أبريل 2026','slug':'eng-waleed-alsirhani',
 'quote':'من برنامج تطوير حلول الذكاء الاصطناعي التوليدي إلى مهندس ذكاء اصطناعي بدوام كامل في قطاع الاستثمار.',
 'impact':'تعيين بدوام كامل «مهندس ذكاء اصطناعي» في دراية المالية في سبتمبر 2026 — خمسة أشهر بعد إتمام البرنامج.',
 'story':'أتمّ وليد برنامج «تطوير حلول الذكاء الاصطناعي التوليدي» بأكاديمية سدايا (26–30 أبريل 2026)، وبنى خلاله نظام وكيل ذكاء اصطناعي متكاملًا. وفي سبتمبر 2026 — بعد خمسة أشهر — عُيّن «مهندس ذكاء اصطناعي» بدوام كامل في دراية المالية بالرياض. النتيجة المحتسبة هي هذا التعيين بدوام كامل، داخل نافذة الأربعة عشر شهرًا وفي صميم البرنامج. ملاحظة تحريرية: كان متدربًا في الدور نفسه لدى الجهة منذ فبراير 2026، قبل البرنامج، فالمحتسب هو التحويل إلى وظيفة كاملة لا التدريب.',
 'ach':['إتمام برنامج تطوير حلول الذكاء الاصطناعي التوليدي — أكاديمية سدايا (أبريل 2026)','مهندس ذكاء اصطناعي بدوام كامل — دراية المالية (سبتمبر 2026)','بناء نظام وكيل ذكاء اصطناعي متكامل خلال البرنامج'],
 'exp':'Derayah Financial — Artificial Intelligence Engineer، دوام كامل، سبتمبر 2026 – الآن (وقبله Internship، فبراير – سبتمبر 2026)؛ شهادة حضور البرنامج 26–30 أبريل 2026',
 'note':'صفحة الخبرة على LinkedIn (حساب مسجَّل، قُرئت 17 أكتوبر 2026): «Artificial Intelligence Engineer — Derayah Financial · Full-time · Sep 2026 – Present». PASS_DATED (+5). التدريب لدى الجهة بدأ قبل البرنامج فلا يُحتسب؛ المحتسب هو التعيين بدوام كامل. مُرقّى إلى قصة نجاح «waleed-alsirhani».'},
]
json.dump(NEW,open('new17b.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
json.dump(ENR,open('enr17b.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
json.dump(ST,open('stories17b.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
print(len(NEW),len(ENR),len(ST),WID)
