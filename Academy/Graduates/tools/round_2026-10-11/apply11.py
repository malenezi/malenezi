# -*- coding: utf-8 -*-
# Round 11 Oct 2026 — new graduates (focus 2024–2026): GitHub team-roster vector + logged-in LinkedIn post sweep
import json,re,os,sys,shutil,collections
sys.path[:0]=[os.path.expanduser('~/mnt/Academy/Graduates/tools/round_2026-10-07'),os.path.expanduser('~/mnt/Academy/Graduates/tools')]
import translit as TR, openpyxl
DRY='--apply' not in sys.argv
H=os.path.expanduser('~/mnt/Academy/'); B='backup-2026-10-11'
DATE='11 أكتوبر 2026'; TAG='[جولة 11 أكتوبر 2026] '
TL=' تنويه: الاسم العربي نقل حرفي عن الاسم اللاتيني المنشور — غير متحقق علنًا.'
SRC_GH='مستودعات GitHub (سبتمبر–أكتوبر 2026) وجداول «الفريق» في ملفات README لمشاريع مقررات الأكاديمية — جولة 11 أكتوبر 2026'
SRC_LI='مسح منشورات LinkedIn (حساب مسجَّل، آخر شهر) لإتمام برامج أكاديمية سدايا — جولة 11 أكتوبر 2026'
TRN={'ai':'مهندس ذكاء اصطناعي — AI Engineer','ds':'عالم بيانات — Data Scientist','other':'برامج متخصصة أخرى — Other / Specialized','dmg':'إدارة وحوكمة البيانات — Data Management & Governance','genai':'أكاديمية الذكاء الاصطناعي التوليدي — Gen AI Academy'}
def rep(s,a,b,count=None):
    n=s.count(a); assert n>=1,('missing',a[:90])
    if count is not None: assert n==count,(a[:90],n)
    return s.replace(a,b)
def rrep(s,pat,b,count=1,flags=0):
    s2,n=re.subn(pat,b,s,flags=flags); assert n==count,(pat,n); return s2
FILES=['SuccessStories/website/js/data.js','index.html','Graduates/index.html','Graduates/Graduates_Database.xlsx','Graduates/Graduates_Database.md']
if not DRY:
    for f in FILES:
        a,b=os.path.splitext(H+f); t=f'{a}.{B}{b}'
        if not os.path.exists(t): shutil.copy2(H+f,t)
P=H+'Graduates/index.html'; s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+len('const DATA = '); j=s.index('\nconst SITE_STATS')
D=json.loads(s[i:j].rstrip()[:-1]); g=D['grads']; N0=len(g); assert N0==3328,N0
head=s[:i]; tail=s[j:]
T0=collections.Counter(r['tr'] for r in g); wl0=sum(1 for r in g if r.get('links')); uu0=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
X_=H+'Graduates/Graduates_Database.xlsx'; wb=openpyxl.load_workbook(X_); ws=wb['قاعدة البيانات']
assert ws.cell(N0+1,1).value==N0
norm=lambda u:re.sub(r'^https?://(www\.|[a-z]{2}\.)?','',u).rstrip('/').lower()
ALL={norm(l[1]) for r in g for l in r['links']}
def note(k,t):
    g[k-1]['d']+=' '+TAG+t; r=k+1; assert ws.cell(r,1).value==k; ws.cell(r,21).value=(ws.cell(r,21).value or '')+' '+TAG+t
def addlink(k,label,url):
    G=g[k-1]
    if any(norm(l[1])==norm(url) for l in G['links']): return False
    G['links'].append([label,url]); col=15 if 'linkedin.com' in url else 16
    r=k+1; cur=ws.cell(r,col).value; ws.cell(r,col).value=(cur+' · ' if cur else '')+url; return True
GH='https://github.com/'; LI='https://www.linkedin.com/in/'
P112='تصوّر البيانات وسرد القصص (SDA-DSC-112) — أكاديمية سدايا (Data Visualization & Storytelling)'
P211='أساليب تعلم الآلة المتقدمة (Advanced Machine Learning Methods) — أكاديمية سدايا'
P214='هندسة البيانات الحديثة لأنظمة الذكاء الاصطناعي (Modern Data Engineering for AI Systems) — أكاديمية سدايا'
PNLP='معالجة اللغة الطبيعية بالمحوّلات (SDA-AIE-211 «بيان») — أكاديمية سدايا'
P113='ممارسات هندسة البرمجيات لأنظمة الذكاء الاصطناعي (SDA-AIE-113) — أكاديمية سدايا'
PCV='تطوير أنظمة الرؤية الحاسوبية (SDA-AIE-212 — Computer Vision Systems Development) — أكاديمية سدايا'
PLLM='هندسة تطبيقات النماذج اللغوية الكبيرة (SDA-AIE-213 — LLM Application Engineering) — أكاديمية سدايا'
PAG='هندسة أنظمة الذكاء الاصطناعي الوكيلي المتقدمة (Advanced Agentic AI Systems Engineering) — أكاديمية سدايا'
PPROD='الذكاء الاصطناعي التوليدي لإنتاجية العمل (L0-FGP — Generative AI for Workplace Productivity) — أكاديمية سدايا'
PFAE='أساسيات الذكاء الاصطناعي لبيئة العمل (L0-FAE — AI Fundamentals for the Workplace) — أكاديمية سدايا'
PWF='أتمتة سير العمل باستخدام الذكاء الاصطناعي (Workflow Automation using AI) — أكاديمية سدايا'
PNV='التدريب الاحترافي في النماذج اللغوية الكبيرة (سدايا×NVIDIA) + شهادة NVIDIA NCA-GENL'
R_RAED=GH+'Raed1231/Tayseer-Digital-Adoption'; R_FZN=GH+'Abdullah-FZN/tayseer-capstone-project'; R_AEDU=GH+'A-edu/tayseer-digital-adoption-capstone'
TEAM112='مشروع «تيسير» الختامي لمقرر SDA-DSC-112 (أكتوبر 2026)'
# (ar,en,prog,co,tr,score,lv,links,src,d,cats,emp,role,alias)
NEW=[
 ('رائد العقيلي','Raed Alokaili',P112,'أكتوبر 2026 (إنشاء مستودع المشروع الختامي: 7 أكتوبر 2026)','ds',72,'gh1011',[['GitHub',GH+'Raed1231'],['مستودع المشروع',R_RAED]],SRC_GH,f'مستودع «Tayseer-Digital-Adoption» — {TEAM112}: «completed as part of a SDAIA Academy training programme Data Visualization & Storytelling». جدول الفريق: Rayan Aloraydi (#2806) · Raed Alokaili · Mohammed Alarifi · Khaled Alromaizan. الاسم الكامل على ملف GitHub (Raed Alokaili، الرياض).'),
 ('محمد العريفي','Mohammed Alarifi',P112,'أكتوبر 2026 (تاريخ مستودع المشروع الختامي للفريق)','ds',62,'gh1011',[['مستودع الفريق',R_RAED]],SRC_GH,f'عضو في جدول فريق مستودع «Raed1231/Tayseer-Digital-Adoption» — {TEAM112}. لا حساب شخصي مرتبط. لا يُدمج مع سجلات «محمد العريفي» الأخرى إن وُجدت لغياب رابط مشترك.'),
 ('خالد الرميزان','Khaled Alromaizan',P112,'أكتوبر 2026 (تاريخ مستودع المشروع الختامي للفريق)','ds',62,'gh1011',[['مستودع الفريق',R_RAED]],SRC_GH,f'عضو في جدول فريق مستودع «Raed1231/Tayseer-Digital-Adoption» — {TEAM112}. لا حساب شخصي مرتبط.'),
 ('عبدالعزيز المحيسري','Abdulaziz Almehsari',P112,'أكتوبر 2026 (تاريخ مستودع المشروع الختامي للفريق)','ds',62,'gh1011',[['مستودع الفريق',R_FZN]],SRC_GH,f'عضو في «Team Members» لمستودع «Abdullah-FZN/tayseer-capstone-project» — {TEAM112}؛ زملاؤه: Abdullah Alfawzan (#2799) · Abdullah Alzahrani · Ahmed Bakhashwain (#2802).'),
 ('عبدالعزيز الفريح','Abdulaziz Alfuraih',P112,'أكتوبر 2026 (إنشاء مستودع المشروع الختامي: 7 أكتوبر 2026)','ds',70,'gh1011',[['GitHub',GH+'A-edu'],['مستودع المشروع',R_AEDU]],SRC_GH,f'مستودع «tayseer-digital-adoption-capstone» («SDAIA Academy · SDA-DSC-112») — {TEAM112}. جدول الفريق يربط الاسم بالحساب: Abdulaziz Alfuraih (@A-EDU) · Abdulmajeed Alnashwan (@a-Nash1) · Naif Alsmari (@Naxf1، #3057) · Khalid Alhaidary (@k-alh). كان معلّقًا في 10 أكتوبر (معرّف فقط) — حُسم بجدول الفريق.'),
 ('عبدالمجيد النشوان','Abdulmajeed Alnashwan',P112,'أكتوبر 2026 (تاريخ مستودع المشروع الختامي للفريق)','ds',68,'gh1011',[['GitHub',GH+'a-Nash1'],['مستودع الفريق',R_AEDU]],SRC_GH,f'جدول فريق مستودع «A-edu/tayseer-digital-adoption-capstone» — {TEAM112}: Abdulmajeed Alnashwan (@a-Nash1)، الشرائح 3–4.'),
 ('خالد الحيدري','Khalid Alhaidary',P112,'أكتوبر 2026 (تاريخ مستودع المشروع الختامي للفريق)','ds',68,'gh1011',[['GitHub',GH+'k-alh'],['مستودع الفريق',R_AEDU]],SRC_GH,f'جدول فريق مستودع «A-edu/tayseer-digital-adoption-capstone» — {TEAM112}: Khalid Alhaidary (@k-alh)، الشريحتان 6–7. حسابه k-alh يحمل أيضًا «Capstone-Project» المسجّل على #3057 نايف الصماري (زميل فريق في مقرر السلاسل الزمنية، سبتمبر 2026).'),
 ('عبدالعزيز الضعيان','Abdulaziz Aldhaayan',P211,'أكتوبر 2026 (إنشاء مستودع المشروع: 8 أكتوبر 2026)','ds',72,'gh1011',[['GitHub',GH+'AbdulazizAldhaayan'],['مستودع المشروع',GH+'AbdulazizAldhaayan/SDA-DSC-211-S06']],SRC_GH,'مستودع «SDA-DSC-211-S06»: «developed as part of the Advanced Machine Learning Methods course at SDAIA Academy» (حالة «تمويل»). الاسم الكامل على ملف GitHub (Abdulaziz Aldhaayan، الرياض).'),
 ('سعود العبدان','Saud Alabdan',P214,'سبتمبر 2026 (تشغيل دفتر المشروع 15 سبتمبر 2026؛ منشور الإتمام 26 سبتمبر 2026)','ds',85,'li1011',[['LinkedIn',LI+'saudalabdan/'],['GitHub',GH+'saud-alabdan'],['مستودع المشروع',GH+'saud-alabdan/saud-masar-modern-data-engineering']],SRC_LI+' + '+SRC_GH,'منشور LinkedIn (26 سبتمبر 2026) «المستشار سعود العبدان»: إتمام «برنامج هندسة البيانات الحديثة لأنظمة الذكاء الاصطناعي» لدى سدايا خلال سبتمبر باجتياز مشروع تطبيقي. المستودع «saud-masar-modern-data-engineering» يصرّح «SDA-DSC-214 — SDAIA Academy» (حالة «مسار»). جهة العمل: المؤسس والشريك الإداري في «ليدار» (سابقة للبرنامج — لا قصة).',['program','project','job'],'ليدار (Lidar)','المؤسس والشريك الإداري'),
 ('ديما عبدالله','Deema Abdullah',P211,'أكتوبر 2026 (إنشاء مستودع المشروع: 6 أكتوبر 2026)','ds',64,'gh1011',[['GitHub',GH+'dee2002al-c'],['مستودع المشروع',GH+'dee2002al-c/Advanced-Machine-Learning-Techniques-211--Deema-Abdullah']],SRC_GH,'مستودع «Advanced-Machine-Learning-Techniques-211--Deema-Abdullah» (حالة «تمويل»؛ «independent learner project» لمقرر Advanced Machine Learning Methods). الاسم من اسم المستودع — اسم العائلة غير منشور.'),
 ('طيف السفياني','Taif Alsufiani',P113,'سبتمبر 2026 (إنشاء مستودع المقرر: 20 سبتمبر 2026)','ai',70,'gh1011',[['GitHub',GH+'taCSif'],['مستودع المقرر',GH+'taCSif/SDA-AIE-113--Taif-Alsufiani']],SRC_GH,'مستودع «SDA-AIE-113--Taif-Alsufiani» (20 سبتمبر 2026) — الاسم الكامل في اسم المستودع.'),
 ('راكان الدوسري','Rakan Aldosari',PCV,'سبتمبر 2026 (إنشاء مستودع المشروع الختامي: 9 سبتمبر 2026)','ai',70,'gh1011',[['GitHub',GH+'RakanAldosari17'],['مستودع المشروع',GH+'RakanAldosari17/Capstone-project-Computer-Vision-Systems-Development-SDA-AIE-212-SDAIA-Academy-']],SRC_GH,'مستودع «Capstone-project-Computer-Vision-Systems-Development-SDA-AIE-212-SDAIA-Academy-» (9 سبتمبر 2026). الاسم من اسم المستخدم على GitHub.'),
 ('محمد يوسف','Mohammad Yusif',PLLM,'سبتمبر 2026 (إنشاء مستودع المقرر: 5 سبتمبر 2026)','ai',62,'gh1011',[['GitHub',GH+'MohammadYusif'],['مستودع المقرر',GH+'MohammadYusif/llm-application-engineering']],SRC_GH,'مستودع «llm-application-engineering»: «هندسة تطبيقات النماذج اللغوية الكبيرة · SDAIA Academy · four days, 20 hours». الاسم من ملف GitHub.'),
 ('رناد عمر','Renad Omar',P113,'سبتمبر 2026 (إنشاء مستودع المشروع: 22 سبتمبر 2026)','ai',64,'gh1011',[['GitHub',GH+'Renad11Omar'],['مستودع المشروع',GH+'Renad11Omar/Muwajjih-Renad-SDAIA']],SRC_GH,'مستودع «Muwajjih-Renad-SDAIA» (22 سبتمبر 2026): مشروع «مُوجّه» ضمن «SDA-AIE-113 — Software Engineering Practices for AI Systems training program at SDAIA Academy». الاسم من اسم المستخدم (قد يكون «عمر» اسم الأب).'),
 ('حنين صليح','Haneen Saleeh','برمجة Python — مختبرات برنامج تدريبي في أكاديمية سدايا','سبتمبر 2026 (إنشاء مستودع المختبرات: 16 سبتمبر 2026)','ai',58,'gh1011',[['GitHub',GH+'HaneenSaleeh07'],['مستودع المختبرات',GH+'HaneenSaleeh07/SDAIA-PROJECT']],SRC_GH,'مستودع «SDAIA-PROJECT»: «SDAIA Python Project — Python programming labs completed as part of the SDAIA training program». الاسم من اسم المستخدم؛ البرنامج غير مسمّى بدقة.'),
 ('ياسر الدرغام','Yasser Aldergham',PAG,'سبتمبر 2026 (إنشاء مستودع «رفيق»: 20 سبتمبر 2026)','ai',64,'gh1011',[['GitHub',GH+'yasseraldergham'],['مستودع المشروع',GH+'yasseraldergham/Rafeeq-yasser.sdaia']],SRC_GH,'مستودع «Rafeeq-yasser.sdaia» (20 سبتمبر 2026) — «رفيق» هو مشروع برنامج هندسة أنظمة الذكاء الاصطناعي الوكيلي المتقدمة. الاسم من اسم المستخدم.'),
 # ---- LinkedIn posts ----
 ('صالح الدوسري','Saleh Aldosari','تطوير حلول الذكاء الاصطناعي التوليدي (Developing Generative AI Solutions) + تصوّر البيانات وسرد القصص (SDA-DSC-112) — أكاديمية سدايا','سبتمبر 2026 (منشور إتمام البرنامجين 1 أكتوبر 2026)','ai',80,'li1011',[['LinkedIn',LI+'saleh-m-aldosari/']],SRC_LI,'منشور LinkedIn (1 أكتوبر 2026) «Saleh M. A.»: «سعيد بإتمام برنامجين من أكاديمية سدايا» — Developing Generative AI Solutions وData Visualization and Storytelling، مع شهادتي اجتياز. اسم العائلة من معرّف الحساب (saleh-m-aldosari).'),
 ('مها فايز الحلافي','Maha Fayez Alhalafi',PPROD,'27–29 سبتمبر 2026','other',85,'li1011',[['LinkedIn',LI+'mahaalhalafi/']],SRC_LI,'منشور LinkedIn (7 أكتوبر 2026) مع شهادة اجتياز ظاهرة: «Maha Fayez Alhalafi — Generative AI for Productivity — From 27/9/2026 To 29/9/2026».',['cert']),
 ('تالا الشويمان','Tala Alshowiman',PPROD,'سبتمبر 2026 (منشور الإتمام 30 سبتمبر 2026)','other',75,'li1011',[['LinkedIn',LI+'tala-alshowiman-9036ba384/']],SRC_LI,'منشور LinkedIn (30 سبتمبر 2026): «completed the Generative AI for Productivity course by DAICO» (#SDAIAAcademy). طالبة علوم حاسب في جامعة الملك سعود.'),
 ('دارين الشمري','Dareen Al-Shammari',PFAE,'سبتمبر–أكتوبر 2026 (منشور الإتمام 5 أكتوبر 2026)','other',75,'li1011',[['LinkedIn',LI+'dareen-al-shammari-663b07334/']],SRC_LI,'منشور LinkedIn (5 أكتوبر 2026): إتمام وحصول على شهادة حضور «AI Fundamentals for the Workplace» (#SDAIAAcademy). خريجة هندسة حاسب.'),
 ('وليد حمود الحربي','Waleed Hamoud Alharbi','رفع الإنتاجية وتحسين العمليات — أكاديمية سدايا','9–11 أغسطس 2026','other',85,'li1011',[['LinkedIn',LI+'waleed-alwesidi-40533517b/']],SRC_LI,'منشور LinkedIn «Waleed Alwesidi» (أكتوبر 2026) مع شهادة حضور ظاهرة: «Waleed Hamoud Alharbi — Increase Productivity and Improve Efficiency — From 9/8/2026 To 11/8/2026». الاسم في الشهادة هو المعتمد؛ «Alwesidi» اسم الحساب.',['cert'],'','','Waleed Alwesidi'),
 ('أحمد الربيعة','Ahmed Alrabiah','جودة البيانات (Data Quality) — أكاديمية سدايا','سبتمبر–أكتوبر 2026 (منشور الإتمام 10 أكتوبر 2026)','dmg',72,'li1011',[['LinkedIn',LI+'ahmed-a-alrabiah-8973b3288/']],SRC_LI,'منشور LinkedIn (10 أكتوبر 2026): «أتممت حضور البرنامج التدريبي "جودة البيانات"، المقدم من SDAIA Academy». مجال عمله: التحول الرقمي وإدارة البيانات وحوكمتها.'),
 ('نورة الهلال','Noura Alhelal',PWF,'أكتوبر 2026 (منشور الإتمام 10 أكتوبر 2026)','other',78,'li1011',[['LinkedIn',LI+'noura-alhelal-9644a8288/']],SRC_LI,'منشور LinkedIn (10 أكتوبر 2026): «completed the "Workflow Automation using AI" program by the SDAIA Academy». طالبة علوم حاسب (سنة أخيرة) في جامعة الملك سعود.'),
 ('محمد القحطاني','Mohammed Alqahtani',PAG,'أكتوبر 2026 (منشور الإتمام 8 أكتوبر 2026)','ai',80,'li1011',[['LinkedIn',LI+'mohammed-alqahtani-a888b02b4/']],SRC_LI,'منشور LinkedIn (8 أكتوبر 2026): «successfully completed the Advanced Agentic AI Systems Engineering Program» — مشروع AI Product Decision Agent؛ ويذكر مشاركة سابقة في «Agentic AI Engineering Bootcamp with SDA». مهندس بنية تحتية لتقنية المعلومات. معرّف LinkedIn مختلف عن #2615 (a655a328b) ولا رابط مشترك مع #2836 (moali2002) — لا دمج.'),
 ('محمد صالح العباس','Mohammed Saleh Alabbas',PAG,'أكتوبر 2026 (منشور الإتمام 8 أكتوبر 2026)','ai',80,'li1011',[['LinkedIn',LI+'mohammed-saleh-alabbas/']],SRC_LI,'منشور LinkedIn (8 أكتوبر 2026): إتمام «Advanced Agentic AI Systems Engineering Program» مع SDAIA Academy (الفريق نفسه: AI Product Decision Agent). أخصائي أشعة يتجه إلى هندسة الذكاء الاصطناعي.'),
 ('عمار آل حيدر','Ammar Al Haider',PAG,'أكتوبر 2026 (منشور الإتمام 8 أكتوبر 2026)','ai',80,'li1011',[['LinkedIn',LI+'ammar-al-haider/']],SRC_LI,'منشور LinkedIn (8 أكتوبر 2026): إتمام «Advanced Agentic AI Systems Engineering Program» (الفريق نفسه: AI Product Decision Agent) بعد «Agentic AI Engineering Bootcamp».'),
 ('سلوان حلواني','Selwan Halawani',PNV,'أكتوبر 2026 (تاريخ شهادة NVIDIA: 2 أكتوبر 2026)','genai',85,'li1011',[['LinkedIn',LI+'selwan-halawani/']],SRC_LI,'منشور LinkedIn (8 أكتوبر 2026) مع شهادة «NVIDIA-Certified Associate: Generative AI for LLMs» (2 أكتوبر 2026): «Through SDAIA Academy\'s LLM Professional Training Program (NVIDIA – AI Track)». خريجة ذكاء اصطناعي.',['cert']),
 ('رغد الربيان','Raghad Alrubayan',PAG,'أكتوبر 2026 (منشور الإتمام 8 أكتوبر 2026)','ai',72,'li1011',[['LinkedIn',LI+'raghad-alrubayan-220aa52b3/']],SRC_LI,'منشور LinkedIn (8 أكتوبر 2026): «concluded my training in the "Advanced Generative AI Systems Engineering" program at SDAIA Academy» — الاسم كما كتبته؛ المطابق في الحافظة هو برنامج الأنظمة الوكيلية المتقدمة (صور القاعة نفسها). طالبة نظم معلومات إدارية.'),
 ('أنس الشمري','Anas AlShammari',PLLM,'أكتوبر 2026 (منشور الإتمام 7 أكتوبر 2026)','ai',82,'li1011',[['LinkedIn',LI+'eng-anas-alshammari-791234419/']],SRC_LI,'منشور LinkedIn (7 أكتوبر 2026): «أنهيت اليوم برنامج "هندسة تطبيقات النماذج اللغوية الكبيرة"» — مشروع «وسيط» (مساعد ذكي لوسيط اللاعبين) مع رابط GitHub. مهندس برمجيات (Flutter).'),
 ('شيخة التميمي','Shaykhah Altamimi',PPROD,'سبتمبر–أكتوبر 2026 (منشور الإتمام 4 أكتوبر 2026)','other',78,'li1011',[['LinkedIn',LI+'shaykhah-altamimi/']],SRC_LI,'منشور LinkedIn (4 أكتوبر 2026): «completed the Generative AI for Productivity program by SDAIA Academy» — مشروع مساعد اجتماعات متكامل مع Microsoft Teams. خريجة هندسة برمجيات.'),
 ('لمى العنزي','Lama Alanazi',PAG,'سبتمبر–أكتوبر 2026 (منشور الإتمام 3 أكتوبر 2026)','ai',78,'li1011',[['LinkedIn',LI+'lama-alanazi28/']],SRC_LI,'منشور LinkedIn «Lama (CAPM®)» (3 أكتوبر 2026): «completed the Advanced Agentic AI Systems Engineering course, in collaboration with SDAIA Academy» — مشروع «Rafeeq Mini» متعدد الوكلاء مع رابط GitHub. اسم العائلة من معرّف الحساب.'),
 ('محمد النغموش','Mohammad Alnaghmoush',PNV,'سبتمبر–أكتوبر 2026 (منشور الشهادة 3 أكتوبر 2026)','genai',82,'li1011',[['LinkedIn',LI+'mohammad-alnaghmoush-398202420/']],SRC_LI,'منشور LinkedIn (3 أكتوبر 2026): «NVIDIA-Certified Associate: Generative AI LLMs (NCA-GENL)» بعد «learning journey delivered through a collaboration between SDAIA Academy and NVIDIA, including 5 specialized stages».',['cert']),
]
FP={'Mohammed Alarifi':{2271},'Mohammad Yusif':{1418},'Renad Omar':{160,2989},'Waleed Hamoud Alharbi':{1452},'Mohammed Alqahtani':None,'Ammar Al Haider':{1528,1252}}
idx=TR.build_index(g); new_ids=[]
for row in NEW:
    ar,en,prog,co,tr,score,lv,links,src,d=row[:10]
    cats=row[10] if len(row)>10 else ['program','project'] if lv=='gh1011' else ['cert']
    emp=row[11] if len(row)>11 else ''; role=row[12] if len(row)>12 else ''; alias=row[13] if len(row)>13 else ''
    m={x[0] for x in TR.match(ar,en,idx)}
    ex={k+1 for k,r in enumerate(g) if (r.get('en') or '').lower()==en.lower()}
    allowed=FP.get(en,set())
    if allowed is not None: assert (m|ex)<=allowed,(en,m,ex)
    if 0: print('MATCH?',en,[(x,g[x-1]['n'],g[x-1]['en'],g[x-1]['prog'][:40],g[x-1]['co'][:20],[l[1][-30:] for l in g[x-1]['links']][:2]) for x in (m|ex)-allowed])
    for l in links:
        if l[0] in ('GitHub','LinkedIn'): assert norm(l[1]) not in ALL or en=='Khalid Alhaidary',(en,l)
    rid=len(g)+1; rr=rid+1; dd=TAG+d+('' if en in ('Saud Alabdan','Maha Fayez Alhalafi','Waleed Hamoud Alharbi') else TL)
    rec={"n":ar,"en":en,"lv":lv,"score":score,"prog":prog,"co":co,"win":"ضمن النطاق","edu":"","emp":emp,"role":role,"cats":cats,"d":dd,"links":links,"src":src,"tr":tr}
    if alias: rec['alias']=alias
    g.append(rec); new_ids.append(rid)
    li=' · '.join(l[1] for l in links if 'linkedin.com' in l[1]) or None; gh=' · '.join(l[1] for l in links if 'github.com' in l[1]) or None
    catl={'program':'برنامج','project':'مشروع','cert':'شهادة','job':'توظيف'}
    vals=[rid,ar,en,prog,TRN[tr],co,emp or None,role or None,None,None,lv,score,'ضمن النطاق',' · '.join(catl[c] for c in cats),li,gh,None,None,None,None,dd,alias or None,src]
    for ci,v in enumerate(vals,1): ws.cell(rr,ci).value=v
# ---- ENRICH ----
ENR=[
 (2649,[['GitHub',GH+'WesalFadhl'],['مستودع (SDA-AIE-211)',GH+'WesalFadhl/SDA-AIE-211-Bayan']],'برنامج ثانٍ: مستودع «SDA-AIE-211-Bayan» (7 سبتمبر 2026) — معالجة اللغة الطبيعية بالمحوّلات. حساب GitHub «WesalFadhl» (Computer Science | AI Enthusiast، الرياض) — التقطه فحص المطابقة قبل كتابته سجلًا جديدًا.'),
 (3161,[['GitHub',GH+'owAziz'],['مستودع (SDA-DSC-112)',GH+'owAziz/data-visualization-and-storytelling']],'برنامج ثانٍ: مستودع «data-visualization-and-storytelling» (6 أكتوبر 2026، «SDAIA Academy · SDA-DSC-112») وفي قسم «Group»: Abdulaziz Al-Abdulkareem وKhalid Aljohar (#2798).'),
 (2798,[['مستودع (SDA-DSC-112)',GH+'owAziz/data-visualization-and-storytelling']],'برنامج ثانٍ: عضو «Group» في مستودع SDA-DSC-112 «owAziz/data-visualization-and-storytelling» (أكتوبر 2026) مع #3161.'),
 (2799,[['GitHub',GH+'Abdullah-FZN'],['مستودع (SDA-DSC-112)',R_FZN]],'برنامج ثانٍ: مستودع «tayseer-capstone-project» (7 أكتوبر 2026) — مشروع «تيسير» الختامي لمقرر تصور البيانات وسرد القصص؛ الفريق: Abdullah Alfawzan · Abdullah Alzahrani · Ahmed Bakhashwain (#2802) · Abdulaziz Almehsari. الحساب Abdullah-FZN كان معلّقًا في 10 أكتوبر — حُسم بجدول الفريق.'),
 (2802,[['مستودع (SDA-DSC-112)',R_FZN]],'برنامج ثانٍ: عضو فريق «Abdullah-FZN/tayseer-capstone-project» (SDA-DSC-112، أكتوبر 2026) مع #2799.'),
 (2806,[['مستودع (SDA-DSC-112)',R_RAED]],'برنامج ثانٍ: «Rayan Aloraydi» في جدول فريق «Raed1231/Tayseer-Digital-Adoption» (SDA-DSC-112، أكتوبر 2026).'),
 (3057,[['GitHub',GH+'Naxf1'],['مستودع (SDA-DSC-112)',R_AEDU]],'برنامج ثانٍ: «Naif Alsmari (@Naxf1)» في جدول فريق «A-edu/tayseer-digital-adoption-capstone» (SDA-DSC-112، أكتوبر 2026، الشريحة 5).'),
 (3132,[['مستودع (SDA-DSC-112)',GH+'yalmutairi72-cpu/tayseer-capstone']],'برنامج ثانٍ: مستودع «tayseer-capstone» (6 أكتوبر 2026، «SDAIA Academy · SDA-DSC-112»)؛ الفريق: Yousef Almutairi · Abdulwahab Alnassar (#2619) · Feras Alnasser (#3156).'),
 (3156,[['مستودع (SDA-DSC-112)',GH+'yalmutairi72-cpu/tayseer-capstone']],'برنامج ثانٍ: «Feras Alnasser» في فريق «yalmutairi72-cpu/tayseer-capstone» (SDA-DSC-112، أكتوبر 2026).'),
 (2619,[['مستودع (SDA-DSC-112)',GH+'yalmutairi72-cpu/tayseer-capstone']],'برنامج ثالث: عضو فريق «yalmutairi72-cpu/tayseer-capstone» (SDA-DSC-112، أكتوبر 2026).'),
 (137,[['GitHub',GH+'AljawharaAlbahlalDev'],['مستودع (SDA-AIE-211)',GH+'AljawharaAlbahlalDev/SDA-AIE-211-Bayan-Course']],'برنامج ثانٍ (2026): مستودع «SDA-AIE-211-Bayan-Course» (5 سبتمبر 2026) — معالجة اللغة الطبيعية بالمحوّلات. ملف GitHub: «Aljawhara Albahlal — new account; previous @ALJAWHARA-ALBAHLAL».'),
 (126,[['GitHub',GH+'NoufAbuhaimed'],['مستودع المشروع',GH+'NoufAbuhaimed/agentic-news-agents']],'برنامج ثانٍ (2026): مستودع «agentic-news-agents» (7 أكتوبر 2026، نظام LangGraph متعدد الوكلاء) — «Submitted by: Nouf Abuhaimed · Academy: @SDAIAAcademy». كان معلّقًا في 10 أكتوبر — حُسم من README.'),
 (3196,[['GitHub',GH+'norahalsuwailem'],['مستودع المقرر',GH+'norahalsuwailem/SDAIA-Data-Visualization']],'مستودع «SDAIA-Data-Visualization» (16 سبتمبر 2026) يؤكد البرنامج والدفعة.'),
 (3091,[['LinkedIn',LI+'aisha-almajed-b19851238/']],'منشور LinkedIn (5 أكتوبر 2026) مع شهادة اجتياز ظاهرة: «Aeshah Abdulrahman Almajed — Data Visualization and Storytelling — From 27/9/2026 To 29/9/2026» — تُضبط الدفعة.'),
 (2224,[['LinkedIn',LI+'nada-alamri9/']],'برنامج ثانٍ: منشور LinkedIn (10 أكتوبر 2026): «completed the Advanced Agentic AI Systems Engineering training program at SDAIA Academy» — مشروع ModelRank متعدد الوكلاء. حساب LinkedIn nada-alamri9 يقابل GitHub nadaalamri-9.'),
 (2451,[],'برنامج ثانٍ: منشور LinkedIn (6 أكتوبر 2026): «completed the Workflow Automation using AI program at SDAIA Academy» (شهادة حضور «دانا موسى السعيدان»، بالتعاون مع DAICO) — مشروع لعبة «ABYSS» مع وعد السيف (#190).'),
 (190,[['LinkedIn',LI+'waad-alsaif-08b051423/']],'برنامج ثانٍ مرجّح: شريكة دانة السيدان (#2451) في مشروع «ABYSS» ضمن «Workflow Automation using AI» (أكتوبر 2026، DAICO) — منشور دانة يذكر حسابها على LinkedIn.'),
 (2871,[],'شهادة إضافية: منشور LinkedIn (1 أكتوبر 2026): «NVIDIA Certified Associate: Generative AI and LLMs» عبر أكاديمية سدايا.'),
 (2554,[],'إتمام: منشوران على LinkedIn (3 أكتوبر 2026): إتمام «Professional Training Program in LLMs» (سدايا×NVIDIA، خمس دورات) والحصول على شهادة NVIDIA.'),
 (999,[],'برنامج ثانٍ (2026): منشور LinkedIn (3 أكتوبر 2026): إتمام «Advanced Agentic AI Systems Engineering» — مشروع فريق متعدد الوكلاء لمراجعة وثائق «مؤشر نضج البيانات الوطني (نضيء)».'),
]
LOG=collections.Counter()
for k,lks,t in ENR:
    for lab,u in lks:
        if addlink(k,lab,u): LOG['link']+=1
    note(k,t); LOG['enr']+=1
N=len(g); T=collections.Counter(r['tr'] for r in g)
wl=sum(1 for r in g if r.get('links')); uu=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
print('N',N0,'->',N,{k:(T0[k],T[k]) for k in T},'wl',wl0,'->',wl,'uu',uu0,'->',uu,dict(LOG),'new',new_ids[0],'-',new_ids[-1])
if DRY: sys.exit(0)
TOT=format(N,','); OTOT=format(N0,',')
VA_O='إصدار 10 أكتوبر 2026 (جولة سد الفجوات والخريجين الجدد والتدقيق والدمج'; VA_N='إصدار 11 أكتوبر 2026 (جولة الخريجين الجدد 2024–2026'
VE_O='version 10 October 2026 (gap-closing, new-graduates, QA and merge round'; VE_N='version 11 October 2026 (new-graduates round, 2024–2026 focus'
def common(t): return t.replace(OTOT,TOT).replace(VA_O,VA_N).replace(VE_O,VE_N)
head=common(head); tail=common(tail)
tail=rep(tail,"{ value: %d, label: 'سجلًا فرديًا',"%N0,"{ value: %d, label: 'سجلًا فرديًا',"%N,1)
EN={'ai':'AI Engineer','ds':'Data Scientist','dmg':'Data Management & Governance','other':'Other / Specialized','genai':'Gen AI Academy'}
for k,en in EN.items():
    if T[k]!=T0[k]:
        tail,n=re.subn(r"(en: '%s', value: )%d\b"%(re.escape(en),T0[k]),"\\g<1>%d"%T[k],tail); print('tail',k,n)
tail=rrep(tail,r"\{ value: %d,(\s+)label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(wl0,format(uu0,',')),"{ value: %d,\\1label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(wl,format(uu,',')))
tail=rep(tail,"noteEn: '%s unique source links'"%format(uu0,','),"noteEn: '%s unique source links'"%format(uu,','),1)
D['grads']=g; open(P,'w',encoding='utf-8').write(head+json.dumps(D,ensure_ascii=False)+';'+tail)
P2=H+'index.html'; s=common(open(P2,encoding='utf-8').read())
s=rep(s,'data-count="%d"'%N0,'data-count="%d"'%N,1)
for k in ('ai','ds','dmg','other','genai','coop'):
    pc='%.1f'%(100*T[k]/N)
    pat=r'(data-count=")%d(">0</div>.*?--w:)[\d.]+(%%.*?data-ar=")[\d.]+(%% من السجل" data-en=")[\d.]+(%% of the registry")'%T0[k]
    s,n=re.subn(pat,lambda mm:mm.group(1)+str(T[k])+mm.group(2)+pc+mm.group(3)+pc+mm.group(4)+pc+mm.group(5),s,count=1,flags=re.S); assert n==1,k
open(P2,'w',encoding='utf-8').write(s)
P3=H+'SuccessStories/website/js/data.js'; s=open(P3,encoding='utf-8').read()
s=rep(s,"{ value: %d, label: 'خريجًا موثّقًا',"%N0,"{ value: %d, label: 'خريجًا موثّقًا',"%N,1)
for k,en in EN.items():
    if T[k]!=T0[k]: s=rrep(s,r"(en: '%s',\s+value: )%d\b"%(re.escape(en),T0[k]),"\\g<1>%d"%T[k])
s=common(s)
s=rep(s,"'use strict';","/* %s: جولة الخريجين الجدد — %s خريجًا (%d سجلًا جديدًا من GitHub وLinkedIn)؛ القصص 167 دون تغيير. */\n'use strict';"%(DATE,TOT,len(new_ids)),1)
open(P3,'w',encoding='utf-8').write(s)
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
   'تحديث':f'{DATE} — جولة الخريجين الجدد (تركيز 2024–2026): {len(new_ids)} سجلًا جديدًا ({OTOT} → {TOT})؛ {LOG["enr"]} إثراءً؛ القصص 167 دون تغيير'}
for row in st.iter_rows():
    if row[0].value in M: row[1].value=M[row[0].value]
sh=wb.create_sheet('جولة_11_أكتوبر_2026'); sh.append(['#','الاسم','النوع','التفصيل'])
for k in new_ids: sh.append([k,g[k-1]['n'],'سجل جديد ('+('GitHub' if g[k-1]['lv']=='gh1011' else 'LinkedIn')+')',g[k-1]['prog']])
for k,_,t in ENR: sh.append([k,g[k-1]['n'],'إثراء',t[:120]])
wb.save(X_)
P5=H+'Graduates/Graduates_Database.md'; s=open(P5,encoding='utf-8').read()
s=rep(s,'**الإصدار:** 10 أكتوبر 2026 — ','**الإصدار:** %s — جولة الخريجين الجدد، تركيز 2024–2026 (%s → %s · القصص 167). قبله: 10 أكتوبر 2026 — '%(DATE,OTOT,TOT),1)
L=['## جولة الخريجين الجدد (تركيز 2024–2026) — %s'%DATE,'',f'**الخريجون {OTOT} → {TOT} · القصص 167 (دون تغيير) · جهات العمل 89 (دون تغيير).**','',
 f'**1) سجلات جديدة ({len(new_ids)}):** كلها دفعات سبتمبر–أكتوبر 2026؛ لم تُعثر على سجلات 2024–2025 جديدة قابلة للتحقق في هذه الجولة.','','| # | الاسم | الاسم الإنجليزي | البرنامج | الدفعة | المسار | المصدر |','|---|---|---|---|---|---|---|']
for k in new_ids:
    G_=g[k-1]; L.append(f"| {k} | {G_['n']} | {G_['en']} | {G_['prog']} | {G_['co']} | {G_['tr']} | {G_['links'][0][1]} |")
L+=['','**2) الأسلوب الجديد — جداول «الفريق» في README:** مشاريع «تيسير» الختامية لمقرر SDA-DSC-112 تحمل جدول فريق يربط الاسم بحساب GitHub؛ أعطت 7 أسماء جديدة وحسمت حسابين كانا معلّقين (A-edu، Abdullah-FZN).','',
 '**3) إثراءات ('+str(LOG['enr'])+'):** '+' · '.join('#%d'%k for k,_,_ in ENR)+' — برامج ثانية وروابط GitHub/LinkedIn وتواريخ شهادات.','',
 '**4) معلّق:** Shatha Alghamdi (shatha-alghamdi-34b3342ba — سجلان بالاسم نفسه #2115/#2404) · Layan Al-Shehri (مطابق محتمل #1983) · Abdulaziz B. (ds-abdulaziz، اسم ناقص) · Raghad1015 · nfsh46655-jpg · Naif-aln · Afnan633 · Lalnefaie · arwam-m · sfom30 · Reema D. Alanazi. غير مكتمل (قبول/بداية فقط): Hassan Almakinah · Essa Almaymuni · Hamad Al-Mutairi · Rana Almohethef · Alhanouf Aldossary. مدربون مستبعدون: Alaa Alharthi · Latifa Alabdulmuhsin · Naif Al Mehmadi · Fetoun AlZahrani · Sultan Alsarra · Mohammad Albeladi.','',
 '**5) القصص:** لا قصص جديدة — الخريجون الجدد أحدث من أن يُقاس لهم توظيف؛ سعود العبدان (#'+str(new_ids[8])+') يعمل في «ليدار» منذ ما قبل البرنامج.','','---','']
k=s.index('## جولة سد الفجوات والخريجين الجدد والتدقيق والدمج — 10 أكتوبر 2026')
s=s[:k]+'\n'.join(L)+'\n'+s[k:]
open(P5,'w',encoding='utf-8').write(s)
for f in ('index.html','Graduates/index.html','SuccessStories/website/js/data.js'):
    t=open(H+f,encoding='utf-8').read(); print(f,'leftover',OTOT,t.count(OTOT),'new',t.count(TOT))
print('done',new_ids[0],'-',new_ids[-1])
