import json
LI='https://www.linkedin.com/in/'
SRC='LinkedIn (حساب مسجَّل) — بحث الأشخاص «Bootcamp at SDAIA» / «Trainee at SDAIA» / «Coop Trainee SDAIA» ثم صفحة الخبرة /details/experience/ بتواريخ بمستوى الشهر — جولة 24 أكتوبر 2026'
T5='معسكر T5 لعلوم البيانات والذكاء الاصطناعي — أكاديمية سدايا'
COOP='التدريب التعاوني — أكاديمية سدايا (COOP)'
R=[
# ar, en, slug, prog, co, tr, score, entry-text, extra
('العنود عواجي','Alanoud Awaji','alanoud-awaji',T5,'مارس – يونيو 2024','ds',80,'«SDAIA T5 Data Science Bootcamp — SDAIA · Internship, Mar 2024 – Jun 2024»',''),
('نبيل ب.','Nabeel B.','nabeel-bukhari','معسكر هندسة تطبيقات الذكاء الاصطناعي (سدايا – جامعة أكسفورد) — أكاديمية سدايا','أغسطس – أكتوبر 2025','ai',75,'«SDAIA - University of Oxford AI Applications Engineering Bootcamp — SDAIA · Internship, Aug 2025 – Oct 2025»',' الاسم المعروض مختصر (Nabeel B.)؛ الرابط nabeel-bukhari.'),
('رزان القرني','Rzan Algarni','rzan-algarni-79545b172','معسكر حوكمة البيانات (Data Governance Bootcamp) — أكاديمية سدايا','يناير – فبراير 2024','dmg',80,'«Data Governance Bootcamp — SDAIA · Internship, Jan 2024 – Feb 2024»',''),
('إسلام الحربي','Islam Alharbi','islam-alharbi','معسكر T5 — تقنيات إدارة الحركة المرورية (زحام) — أكاديمية سدايا','يوليو – أكتوبر 2024','ds',80,'«Traffic Management Technologies Bootcamp — SDAIA · Internship, Jul 2024 – Oct 2024»',''),
('نورة المطرفي','Noura Almatrafi','noura-almatrafi','معسكر ServiceNow — أكاديمية سدايا','أغسطس – أكتوبر 2025','other',80,'«ServiceNow Bootcamp — SDAIA, Aug 2025 – Oct 2025»',''),
('ربى الفليح','Ruba Alfelaih','ruba-abdullah-alfelaih','معسكر علوم البيانات (T5) — أكاديمية سدايا','سبتمبر – ديسمبر 2023','ds',80,'«Data Science Bootcamp — SDAIA, Sep 2023 – Dec 2023»',''),
('بتول أ.','Batool A.','batoolaalghamdi',T5+' + معسكر تعلم الآلة (ML Bootcamp)','سبتمبر – ديسمبر 2023؛ يناير – فبراير 2024','ds',70,'«Data Science and Artificial Intelligence T5 Bootcamp, Sep 2023 – Dec 2023» و«ML Bootcamp, Jan 2024 – Feb 2024» — SDAIA',' الاسم المعروض مختصر (Batool A.)؛ الرابط batoolaalghamdi.'),
('ليان البراق','Layan Albarraq','layan-albarraq-4673a2310','معسكر إدارة الأنظمة السحابية (Cloud Systems Management Bootcamp) — أكاديمية سدايا','أكتوبر – ديسمبر 2025','other',80,'«Cloud systems management Bootcamp — SDAIA, Oct 2025 – Dec 2025»',''),
('رويدا الشهري','Ruwayda Alshehri','ruwayda-alshehri','معسكر حوكمة البيانات (Data Governance Bootcamp) — أكاديمية سدايا','مايو – يونيو 2024','dmg',85,'«Data Governance Bootcamp — SDAIA · Apprenticeship, May 2024 – Jun 2024»؛ حاصلة على CDMP',' قصة معلّقة (ارتباط): متدربة تحليلات متقدمة في هيئة الزكاة والضريبة والجمارك ديسمبر 2024 (+6)، ثم أخصائية تحليلات متقدمة أغسطس 2025 (+14) عبر upsource — هل التحليلات المتقدمة مرتبطة بحوكمة البيانات؟'),
('جنى الزامل','Jana Alzamil','jana-alzamil-7a4318209','معسكر بناء تطبيقات الذكاء الاصطناعي (AI Application Building) — أكاديمية سدايا','يناير 2025','ai',75,'«AI Application Building bootcamp — SDAIA, Jan 2025»',''),
('دانة الصالحي','Dona Alsalhi','donaalsalhi','معسكر سدايا – جامعة أكسفورد للذكاء الاصطناعي (بالشراكة مع كاوست) — أكاديمية سدايا','أغسطس – أكتوبر 2025','ai',90,'«SDAIA - University of Oxford AI Bootcamp — SDAIA · Internship, Aug 2025 – Oct 2025» (برنامج متقدم 9 أسابيع لأفضل 30 مرشحًا)',''),
('علي الجنبي','Ali Aljanbi','alialjanbi','معسكر سدايا للأمن السيبراني — أكاديمية سدايا','أكتوبر 2021 – أبريل 2022','other',75,'«SDAIA Cyber Security Bootcamp — SDAIA Academy · Internship, Oct 2021 – Apr 2022»',' خارج نافذة الجولة (2023–أبريل 2026).'),
('أثير أ.','Atheer A.','atheeralghamdi2',T5,'ديسمبر 2021 – يناير 2022','ds',65,'«T5 Data Science Bootcamp — SDAIA, Dec 2021 – Jan 2022»',' الاسم المعروض مختصر؛ خارج نافذة الجولة.'),
('مها أ.','Maha A.','maha-almutair','معسكر علوم البيانات والذكاء الاصطناعي (T5) — أكاديمية سدايا','سبتمبر – ديسمبر 2023','ds',65,'«Data Science and AI Bootcamp — SDAIA · Internship, Sep 2023 – Dec 2023»',' الاسم المعروض مختصر (Maha A.)؛ الرابط maha-almutair.'),
('لجين سندي','Lujeen Sendy','lujeensendy','المسارات المتقدمة في الذكاء الاصطناعي (Advanced Pathways in AI) — أكاديمية سدايا','نوفمبر 2024','ai',75,'«The Advanced Pathways in Artificial Intelligence Training Bootcamp — SDAIA · Internship, Nov 2024»',''),
('مريم ج.','Maryam J.','qmaryamj','معسكر علوم البيانات والذكاء الاصطناعي (T5) — أكاديمية سدايا','يوليو – أكتوبر 2024','ds',60,'«Data Science and Artificial Intelligence BootCamp — SDAIA, Jul 2024 – Oct 2024»',' الاسم المعروض مختصر (Maryam J.).'),
('رند الفيفي','Rand Alfaifi','rand-alfaifi','معسكر أكاديمية سدايا (لم يُسمَّ البرنامج)','أكتوبر – ديسمبر 2025','other',60,'«SDAIA Bootcamp — SDAIA, Oct 2025 – Dec 2025»',' اسم البرنامج غير محدد في الملف.'),
('أفراح المطيري','Afrah AlMutairi','afrah-almutairii',T5,'سبتمبر – ديسمبر 2021','ds',80,'«Junior Data Scientist (Bootcamp) — SDAIA · Internship, Sep 2021 – Dec 2021»',' خارج نافذة الجولة.'),
('رائد الشمري','Rayid Al Shammari','rayid-al-shammari-337272293','معسكر أكاديمية سدايا لمحترفي الذكاء الاصطناعي (AI Professionals Bootcamp)','ديسمبر 2025 – فبراير 2026','ai',80,'«AI Professional Trainee — SDAIA · Internship, Dec 2025 – Feb 2026»',''),
('شروق الشمراني','Shroog Alshamrani','shroog-alshamrani-msc-b17ba1252','معسكر النماذج اللغوية الكبيرة (LLM Bootcamp) — أكاديمية سدايا','يوليو – سبتمبر 2024','ai',85,'«LLM Trainee — SDAIA · Internship, Jul 2024 – Sep 2024»',''),
('نورة العبيواني','Norah Awad Alobiwani','norah-awad-alobiwani','ممارس تعلم الآلة (ML Practitioner — Machine Learning Bootcamp) — أكاديمية سدايا','نوفمبر – ديسمبر 2023','ai',85,'«ML Practitioner (Machine Learning Bootcamp) — SDAIA · Internship, Nov 2023 – Dec 2023»',' إشارة: ليست #3488 «Norah A.» (رابط مختلف norah-a-77a86a1ab وبرنامج T5) — لم يُدمج.'),
('راما الشهري','Rama Alshehri','rama-alshehri',COOP,'يونيو – أغسطس 2025','coop',75,'«Co-op Trainee — SDAIA · Internship, Jun 2025 – Aug 2025»',''),
('ملاف الخثران','Melaf Al Khathran','melafalkhathran',COOP+' — الهوية والسحابة (IAM & Cloud Security)','يناير – مايو 2026','coop',75,'«COOP Trainee at SDAIA (IAM & Cloud Security) — Jan 2026 – May 2026»',''),
('إياد الفيفي','Eyad Alfaifi','eyad-alfaifi',COOP,'أغسطس – نوفمبر 2025','coop',75,'«COOP Trainee — SDAIA · Internship, Aug 2025 – Nov 2025»',''),
('رغد النملة','Raghad Alnamlah','raghadalnamlah',COOP,'يناير – أبريل 2026','coop',75,'«COOP Trainee — SDAIA · Internship, Jan 2026 – Apr 2026»',''),
('نورة القرناس','Norah Algarnas','norah-algarnas-ecba%E2%84%A2-6a7402316',COOP,'أغسطس – أكتوبر 2025','coop',75,'«Co-op Trainee — SDAIA · Internship, Aug 2025 – Oct 2025»',''),
('ليان الكنهل','Layan Alkanhal','layan-alkanhal-b5586a328',COOP,'سبتمبر – أكتوبر 2025','coop',75,'«Cooperative Training — SDAIA · Internship, Sep 2025 – Oct 2025»',''),
]
NEW=[]
for ar,en,slug,prog,co,tr,sc,ent,ex in R:
    NEW.append([ar,en,prog,co,tr,sc,'li1024',[['LinkedIn',LI+slug+'/']],SRC,'صفحة الخبرة على LinkedIn: '+ent+'.'+ex,['program'],'','',True])
json.dump(NEW,open('new24.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
E=[(2382,'Shahad Alameel','shahadalameel','',None),(2101,'','rana-alabbas','Rana Alabbas',None),(3109,'Khalid F. AlBakr','khalid-albakr-8840ba331','',None),
(1156,'','majid-almuhaihi-67936a203','Majid Almuhaihi',None),(1050,'','shouq-qahl-55b440270','Shouq Qahl',None),(2273,'Lubna Alqahtani','lubna-alqahtani','',None),
(174,'Mohammed Alrowais','mohammedalrowais','',None),(597,'Najwa Anwar Almuafi','eng-najwa-anwar','',None),(1676,'','abdulmajeed-alsafari','Abdulmajeed Alsafari',None),
(11,'Aljawharah Bin Tamran','aljawharah-bin-tamran-1121461a7','',None),(2465,'Abdullah Alshami','shami-am','',None),(2496,'Modhi Alhbrdi','modhi-alhbrdi','',None),
(2808,'Abdulrhman Bagasher','abdulrhman-bagasher','',None),(851,'','razan-albalhareth-79649227a','Razan AlBalhareth',None),(2306,'Randa Alshehri','randa-alshehri-97b7b023b','',None),
(976,'','anfal-saad','Anfal Alkuraydis',None),(957,'','hasan-alshanqiti','Hassan Alshanqiti',None),(1660,'','asrarmoh','Asrar Alqarni',None)]
ENR=[{'k':k,'en':en,'links':[['LinkedIn',LI+s+'/']],'set_en':se,'t':'إضافة رابط LinkedIn المطابق (نتيجة بحث الأشخاص «Bootcamp at SDAIA»/«SDAIA Academy trainee» بنفس البرنامج).'} for k,en,s,se,_ in E]
json.dump(ENR,open('enr24.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
print(len(NEW),len(ENR))
