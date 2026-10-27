import json
OX='معسكر هندسة تطبيقات الذكاء الاصطناعي (سدايا – جامعة أكسفورد) — أكاديمية سدايا'
CL='معسكر إدارة الأنظمة السحابية (SRE) — أكاديمية سدايا بالتعاون مع Rackspace'
AP='المسارات المتقدمة في الذكاء الاصطناعي — سدايا / SDAIA Advanced Pathway (بالتعاون مع ستانفورد وDeepLearning.AI)'
E='صفحة الخبرة على LinkedIn (حساب مسجَّل، قُرئت 27 أكتوبر 2026): '
P='منشور إتمام على LinkedIn: '
new=[
# ar,en,slug,prog,co,tr,score,d,translit
('بسام النفيعي','Bassam Alnefaie','bassam-alnefaie-b9b985370',OX,'أغسطس – أكتوبر 2025','ai',85,E+'«SDAIA-University of Oxford Bootcamp — SDAIA · Internship, Aug 2025 – Oct 2025»؛ و'+P+'«أتممت مشاركتي في معسكر هندسة تطبيقات الذكاء الاصطناعي مع سدايا بالتعاون مع جامعة أكسفورد… ثمانية أسابيع».',True),
('نايف المحمادي','Naif Al Mehmadi','naif-al-mehmadi',OX,'2025 (منشور الإتمام قبل نحو سنة من 27 أكتوبر 2026)','ai',72,P+'«اعلن إتمامي لـ SDAIA-Oxford AI Engineering Bootcamp، وهو برنامج متخصص تم بالتعاون بين University of Oxford و SDAIA». لا قيد للمعسكر في صفحة الخبرة. إشارة: يختلف عن #361 «نايف مرسال المحمادي» (NVIDIA) و#2018 «نايف المحمادي» (CDMP) — لم يُدمج لعدم وجود تعزيز.',True),
('وديان المشدق','Wedyan Almushaddag','wedyanfawaz',OX,'أغسطس – أكتوبر 2025','ai',85,E+'«Artificial Intelligence Application Engineering Bootcamp — University of Oxford · Internship, Aug 2025 – Oct 2025»؛ و'+P+'«انتهينا من معسكر هندسة تطبيقات الذكاء الاصطناعي المقدم من SDAIA».',True),
('عبدالإله خلف','Abdulelah Khalaf','abdulelah-khalaf-b3b8942b5',OX,'أغسطس – أكتوبر 2025','ai',85,'قسم التعليم على LinkedIn: «University of Oxford — AI Program, Aug 2025 – Oct 2025 … organized by SDAIA in collaboration with the University of Oxford»؛ و'+P+'«completed the AI Application Engineering Bootcamp». إشارة: قد يكون هو #1858 «عبدالاله خلف» (تطوير حلول الذكاء الاصطناعي التوليدي، أبريل 2026) — لم يُدمج لعدم وجود تعزيز.',True),
('سامر المنتشري','Samer Almontasheri','samer-almontasheri',OX,'سبتمبر – نوفمبر 2025','ai',82,E+'«AI Trainee — SDAIA · Internship, Sep 2025 – Nov 2025 · Oxford»؛ و'+P+'«completed the AI Application Engineering Bootcamp».',True),
('عمار الصهلي','Ammar Alsehli','ammar-alsehli',OX,'أغسطس – أكتوبر 2025','ai',85,E+'«AI Training Program — SDAIA · Apprenticeship, Aug 2025 – Oct 2025» (ورش في جامعة أكسفورد ومشروع ختامي في يوم الملصقات بسدايا).',True),
('سلطان الحربي','Sultan Alharbi','sultan-alharbi-2a784b2a8',OX,'2025 (منشور الإتمام قبل نحو 11 شهرًا من 27 أكتوبر 2026)','ai',72,P+'«completed the AI Application Engineering Bootcamp conducted by SDAIA, that was held at the University of Oxford». لا قيد للمعسكر في صفحة الخبرة.',True),
('أبرار أ.','Abrar A.','abrar-a-625941216',OX,'أغسطس – أكتوبر 2025','ai',78,E+'«Artificial Intelligence Applications Engineering — SDAIA · Internship, Aug 2025 – Oct 2025 · Oxford»؛ و'+P+'«فخورة جداً بمشاركتي في معسكر سدايا لهندسة تطبيقات…». الاسم المعروض مختصر.',False),
('فهد الغامدي','Fahad Alghamdi','fahad-alghamdi-0ba72438a',OX,'أغسطس – أكتوبر 2025','ai',82,E+'«AI Application Engineer — SDAIA · Apprenticeship, Aug 2025 – Oct 2025 · University of Oxford | SDAIA».',True),
('سمر كلفدن','Samar Kilfaden','samar-kilfaden-aa275224b',OX,'2025 (منشور الإتمام قبل نحو سنة من 27 أكتوبر 2026)','ai',74,P+'«officially completed the SDAIA–Oxford AI Program at the University of Oxford».',True),
('عروب الرزق','Aroub Al Rizq','aroub-al-rizq-36077322b',OX,'أغسطس – أكتوبر 2025','ai',82,E+'«Oxford- SDAIA AI Program Alumni — SDAIA · Internship, Aug 2025 – Oct 2025».',True),
('هاشم المبارك','Hashem Almubarak','hashem-almubarak',OX,'سبتمبر – أكتوبر 2025','ai',85,E+'«AI Engineer — SDAIA · Internship, Sep 2025 – Oct 2025 · Oxford» (برنامج مكثف 9 أسابيع)؛ و'+P+'«Now officially a SDAIA AI alumni and recognized during #ICAN2026 as a graduate».',True),
('حمد القحطاني','Hamad AlQahtani','hamad-alqahtani1',OX,'أغسطس – نوفمبر 2025','ai',82,E+'«SDAIA x University of Oxford AI Bootcamp — SDAIA · Internship, Aug 2025 – Nov 2025» مع شهادة إنجاز.',True),
('حصة وليد','Hessa Waleed','hessa-waleed-2535b2217',OX,'أغسطس – أكتوبر 2025','ai',82,E+'«AI Applications Engineering Bootcamp — SDAIA · Internship, Aug 2025 – Oct 2025»؛ و'+P+'«completed the AI Engineering Program at University of Oxford, delivered by SDAIA».',True),
('ريما جبران القحطاني','Reema Jubran Alqahtani','-reema-alqahtani',OX,'أغسطس – أكتوبر 2025','ai',82,E+'«(AI Intern) Artificial Intelligence in Application Software Engineering Bootcamp — SDAIA, Aug 2025 – Oct 2025 · Oxford» مع شهادة إنجاز.',True),
('أمجاد الناصر','Amjad Alnasser','amjadaln',OX,'سبتمبر – أكتوبر 2025','ai',85,E+'«SDAIA X Oxford AI Applications Engineering Academic Program — SDAIA, Sep 2025 – Oct 2025»؛ و'+P+'«Just wrapped up an incredible journey at University of Oxford with SDAIA’s AI Engineering Program».',True),
('جنى الشهري','Jana Alshehri','janaalshehri',CL,'أكتوبر – ديسمبر 2025','other',82,E+'«Cloud Management Bootcamp Trainee — SDAIA · Internship, Oct 2025 – Dec 2025»؛ و'+P+'«completed the Cloud Management Bootcamp by SDAIA Academy in collaboration with Rackspace Technology».',True),
('أكرم الخليفي','Akram Alkhulaifi','akram-alkhulaifi-5939402b1',CL,'أكتوبر – ديسمبر 2025','other',85,E+'«Cloud Systems Management (SRE) Trainee – SDAIA & Rackspace — Apprenticeship, Oct 2025 – Dec 2025»؛ و'+P+'«completed the Cloud Systems Management (SRE) Bootcamp offered by SDAIA Academy».',True),
('جود العليان','Jood Alolayan','jood-alolayan',CL,'ديسمبر 2025 تقريبًا (منشور الإتمام قبل نحو 10 أشهر)','other',72,P+'«completed the Cloud Management Bootcamp by SDAIA Academy and Rackspace Technology — an intensive 9-week journey». لا قيد للمعسكر في صفحة الخبرة.',True),
('منار فهد الحميد','Manar Alhumaid','manar-alhumaid-1a5b112bb',CL,'أكتوبر – ديسمبر 2025','other',85,E+'«Cloud Systems Management Bootcamp (SRE) — SDAIA, Oct 2025 – Dec 2025» مع شهادة باسم «Manar Fahad Al Humaid»؛ و'+P+'عن المعسكر بالشراكة مع Rackspace.',True),
('أسامة الفهيد','Osama Alfahid','osamaalfahid',CL,'أكتوبر – ديسمبر 2025','other',82,E+'«Cloud Training Program — SDAIA, Oct 2025 – Dec 2025»؛ و'+P+'«completed the Cloud Systems Management Bootcamp by SDAIA».',True),
('خالد الحارثي','Khalid Alharthi','khalid-alharthi-ksjh',CL,'ديسمبر 2025 تقريبًا (منشور الإتمام قبل نحو 10 أشهر)','other',70,P+'«successfully completed the Cloud Systems Management…» (أكاديمية سدايا وRackspace). لا قيد للمعسكر في صفحة الخبرة. إشارة: الاسم شائع؛ #1618 «خالد الحارثي» (جودة البيانات، 2026) لم يُدمج لعدم وجود تعزيز.',True),
('شهد الإبراهيم','Shahad Alibrahim','shahad-alibrahim-08182432a',AP,'3 – 28 نوفمبر 2024','ai',76,P+'«completed the Advanced Pathways in Artificial Intelligence program offered by SDAIA… held from November 3 to November 28, 2024».',True),
('هيفاء السديري','Haifa Alsudairy','haifa-alsudairy-32a7a5260',AP+' — مسار تعلم الآلة','أواخر 2024 – 2025 (منشور الإتمام قبل أكثر من سنة)','ai',72,P+'«completed the Advanced Pathways in Artificial Intelligence Program under the Machine Learning Pathway, offered by SDAIA in collaboration with Stanford University and DeepLearning.AI».',True),
]
enr=[
 {'k':2093,'links':[['LinkedIn','https://www.linkedin.com/in/danah-alghamdi-7a8ba0345/']],'en':'Danah Alghamdi','t':'منشور على LinkedIn (قبل نحو 7 أشهر) عن مشروع «سياج» ضمن معسكر أكاديمية سدايا لمحترفي الذكاء الاصطناعي بالاشتراك مع يارا الرشيدي (#2137، الدفعة نفسها) — تطابق الاسم والبرنامج والدفعة؛ أُضيف الرابط والاسم اللاتيني.'},
 {'k':3108,'links':[['LinkedIn','https://www.linkedin.com/in/mustafa-alalii/']],'prog_add':'تطوير حلول الذكاء الاصطناعي التوليدي (Developing Generative AI Solutions) — أكاديمية سدايا (منشور إتمام ~يونيو 2026)','t':'منشور إتمام على LinkedIn (قبل نحو 4 أشهر): «completed the “Developing Generative AI Solutions” program by SDAIA» — الاسم المعروض «Mustafa O. Al Ali» مطابق للسجل؛ أُضيف البرنامج الثاني والرابط.'},
 {'k':3631,'links':[['LinkedIn','https://www.linkedin.com/in/lina-alzeghaibi-781a43172/']],'prog_add':'معسكر إدارة الأنظمة السحابية (SRE) — بالتعاون مع Rackspace (9 أسابيع؛ منشور إتمام ~ديسمبر 2025)','t':'منشور إتمام على LinkedIn (قبل نحو 10 أشهر): «completed the 9-week Cloud Systems Management (SRE) Bootcamp offered by SDAIA Academy, in partnership with Rackspace Technology» — لقب الزغيبي مميز ومطابق لسجل التدريب التعاوني في قطاع الحوسبة السحابية؛ أُضيف البرنامج والرابط.'},
]
LI='https://www.linkedin.com/in/'
stories=[
 dict(slug='bassam-alnefaie',en='Bassam Alnefaie',year=2025,role='مهندس ذكاء اصطناعي مشارك (AI Associate Engineer)',org='PYXON',
  impact='التحق مهندسَ ذكاء اصطناعي مشاركًا بدوام كامل في PYXON في سبتمبر 2026 — بعد أحد عشر شهرًا من إتمام المعسكر.',
  story='أتمّ بسام معسكر هندسة تطبيقات الذكاء الاصطناعي (سدايا – جامعة أكسفورد) بين أغسطس وأكتوبر 2025، وهو برنامج مكثف لثمانية أسابيع اختير له ثلاثون متدربًا. وبعد تدريب صيفي أخصائيًا لعلوم البيانات في الخطوط السعودية للشحن (يونيو – سبتمبر 2026)، التحق في سبتمبر 2026 بشركة PYXON مهندسَ ذكاء اصطناعي مشاركًا بدوام كامل.',
  ach=['مهندس ذكاء اصطناعي مشارك — PYXON، سبتمبر 2026 (+11 شهرًا)','تدريب أخصائي علوم بيانات — الخطوط السعودية للشحن، يونيو – سبتمبر 2026','إتمام معسكر سدايا – أكسفورد لهندسة تطبيقات الذكاء الاصطناعي (أكتوبر 2025)'],
  exp='معسكر سدايا – أكسفورد: أغسطس – أكتوبر 2025 · Data Science Specialist (تدريب)، الخطوط السعودية للشحن: يونيو – سبتمبر 2026 · AI Associate Engineer، PYXON، دوام كامل: سبتمبر 2026 – الآن',
  q='معسكر سدايا – أكسفورد نقلني من التدريب إلى هندسة الذكاء الاصطناعي في PYXON.',qe='The SDAIA–Oxford bootcamp took me from training to AI engineering at PYXON.'),
 dict(slug='hashem-almubarak',en='Hashem Almubarak',year=2025,role='مهندس ذكاء اصطناعي (AI Engineer)',org='SiFi',
  impact='انضم بدوام كامل إلى Si-Ware Systems في أبريل 2026 لأبحاث التعلم العميق، ثم مهندسَ ذكاء اصطناعي في SiFi في أغسطس 2026.',
  story='أتمّ هاشم برنامج سدايا – أكسفورد المكثف لهندسة تطبيقات الذكاء الاصطناعي (سبتمبر – أكتوبر 2025)، وكُرّم خريجًا في #ICAN2026. عمل بعدها مدربًا للذكاء الاصطناعي في أكاديمية كاوست (يناير 2026)، ثم التحق في أبريل 2026 بشركة Si-Ware Systems بدوام كامل في أبحاث التعلم العميق على بيانات المستشعرات، وفي أغسطس 2026 أصبح مهندس ذكاء اصطناعي في SiFi.',
  ach=['مهندس ذكاء اصطناعي — SiFi، أغسطس 2026 (+10 أشهر)','أبحاث التعلم العميق — Si-Ware Systems، دوام كامل، أبريل 2026 (+6 أشهر)','مدرب ذكاء اصطناعي — أكاديمية كاوست، يناير – أغسطس 2026'],
  exp='AI Engineer (SDAIA · Internship، أكسفورد): سبتمبر – أكتوبر 2025 · AI Instructor، أكاديمية كاوست: يناير – أغسطس 2026 · Si-Ware Systems، دوام كامل: أبريل – أغسطس 2026 · AI Engineer، SiFi، دوام كامل: أغسطس 2026 – الآن',
  q='بعد برنامج سدايا – أكسفورد صرت أبني نماذج التعلم العميق في الصناعة.',qe='After the SDAIA–Oxford program, I build deep-learning models in industry.'),
 dict(slug='abdulelah-khalaf',en='Abdulelah Khalaf',year=2025,role='مهندس ذكاء اصطناعي (AI Engineer)',org='Nagarro',
  impact='التحق مهندسَ ذكاء اصطناعي بدوام كامل في Nagarro بالرياض في ديسمبر 2025 — بعد شهرين من إتمام البرنامج.',
  story='أتمّ عبدالإله برنامج الذكاء الاصطناعي الذي نظمته سدايا مع جامعة أكسفورد (أغسطس – أكتوبر 2025)، والمعلن عنه بوصفه معسكر هندسة تطبيقات الذكاء الاصطناعي. وفي ديسمبر 2025 التحق بشركة Nagarro في الرياض مهندسَ ذكاء اصطناعي بدوام كامل.',
  ach=['مهندس ذكاء اصطناعي — Nagarro، ديسمبر 2025 (+2 شهر)','إتمام برنامج سدايا – أكسفورد للذكاء الاصطناعي (أكتوبر 2025)'],
  exp='قسم التعليم: University of Oxford — AI Program (تنظيم سدايا): أغسطس – أكتوبر 2025 · AI Engineer، Nagarro، دوام كامل: ديسمبر 2025 – الآن',
  q='برنامج سدايا – أكسفورد قادني إلى وظيفة مهندس ذكاء اصطناعي في Nagarro.',qe='The SDAIA–Oxford program led me to an AI Engineer role at Nagarro.'),
 dict(slug='ammar-alsehli',en='Ammar Alsehli',year=2025,role='محلل أعمال — الذكاء الاصطناعي (Business Analyst – AI)',org='الهيئة العليا للأمن الصناعي',
  impact='التحق محللَ أعمال في الذكاء الاصطناعي بدوام كامل في الهيئة العليا للأمن الصناعي في أغسطس 2026 — بعد عشرة أشهر من الإتمام.',
  story='اختير عمار ضمن معسكر سدايا للذكاء الاصطناعي (أغسطس – أكتوبر 2025)، الذي جمع التأسيس في الذكاء الاصطناعي مع تدريب متقدم في الرؤية الحاسوبية ومعالجة اللغة والذكاء التوليدي وورشٍ في جامعة أكسفورد، وقدّم مشروعه الختامي في يوم الملصقات بسدايا. وفي أغسطس 2026 التحق بالهيئة العليا للأمن الصناعي محللَ أعمال في الذكاء الاصطناعي بدوام كامل.',
  ach=['محلل أعمال – الذكاء الاصطناعي — الهيئة العليا للأمن الصناعي، أغسطس 2026 (+10 أشهر)','تقديم المشروع الختامي في يوم الملصقات بسدايا','إتمام معسكر سدايا – أكسفورد (أكتوبر 2025)'],
  exp='AI Training Program، SDAIA · Apprenticeship: أغسطس – أكتوبر 2025 · Business Analyst & Artificial Intelligence، الهيئة العليا للأمن الصناعي، دوام كامل: أغسطس 2026 – الآن',
  q='من ورش أكسفورد إلى تحليل حلول الذكاء الاصطناعي في الهيئة العليا للأمن الصناعي.',qe='From Oxford workshops to analysing AI solutions at the Supreme Authority for Industrial Security.'),
 dict(slug='amjad-alnasser',en='Amjad Alnasser',year=2025,role='محللة أنظمة — الأمن السيبراني بالذكاء الاصطناعي (AI Cybersecurity – IT System Analyst)',org='أرامكو السعودية',
  impact='التحقت بأرامكو السعودية في أغسطس 2026 محللةَ أنظمة في الأمن السيبراني المعزّز بالذكاء الاصطناعي — بعد عشرة أشهر من الإتمام.',
  story='أتمّت أمجاد البرنامج الأكاديمي لهندسة تطبيقات الذكاء الاصطناعي (سدايا × أكسفورد) بين سبتمبر وأكتوبر 2025. ثم تدربت في الذكاء الاصطناعي الوكيلي لدى «صانع» (يونيو – أغسطس 2026)، وفي أغسطس 2026 التحقت بأرامكو السعودية في دور «AI Cybersecurity – Lead Assistant IT System Analyst». بحكم 21 أكتوبر 2026: لا يحجب برنامج غير تابع للأكاديمية بين الإتمام والتوظيف نسبة القصة.',
  ach=['محللة أنظمة – الأمن السيبراني بالذكاء الاصطناعي — أرامكو السعودية، أغسطس 2026 (+10 أشهر)','متدربة الذكاء الاصطناعي الوكيلي — صانع (SANI)، يونيو – أغسطس 2026','إتمام برنامج سدايا × أكسفورد (أكتوبر 2025)'],
  exp='SDAIA X Oxford AI Applications Engineering Academic Program: سبتمبر – أكتوبر 2025 · Agentic AI Trainee، صانع: يونيو – أغسطس 2026 · AI Cybersecurity – Lead Assistant IT System Analyst، أرامكو: أغسطس 2026 – الآن',
  q='برنامج سدايا × أكسفورد فتح لي باب الأمن السيبراني بالذكاء الاصطناعي في أرامكو.',qe='The SDAIA × Oxford program opened AI-driven cybersecurity at Aramco for me.'),
]
json.dump(dict(new=new,enr=enr,stories=stories),open('data27.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
for s in stories:
  for t in (s['q'],s['qe']): assert len(t)<=100,(len(t),t)
print(len(new),len(enr),len(stories))
