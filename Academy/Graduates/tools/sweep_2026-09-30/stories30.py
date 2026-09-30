import json,os,re,shutil,subprocess
H=os.path.expanduser('~/mnt/Academy/')
BK='backup-2026-09-30b'
def bk(p):
    r,e=os.path.splitext(p); b='%s.%s%s'%(r,BK,e)
    if not os.path.exists(b): shutil.copy2(p,b)
def rep(s,a,b,n=None):
    c=s.count(a); assert c>=1,('missing',a[:70])
    if n is not None: assert c==n,(a[:70],c)
    return s.replace(a,b)
VER='تحقّق 30 سبتمبر 2026 (فحص قصص النجاح لقاعدة الخريجين).'
ST=[
{"id":"saleh-altuwaijri","year":2024,"quote":{"text":"معسكر زحام في أكاديمية سدايا نقلني من إدارة المشاريع إلى علوم البيانات، ومنه بدأت مسيرتي عالمَ بيانات ثم مهندسَ بيانات وذكاء اصطناعي.","kind":"draft"},
 "name":"صالح التويجري","nameEn":"Saleh Altuwaijri","photo":None,"role":"مهندس بيانات وذكاء اصطناعي","org":"المركز الوطني لنظم الموارد الحكومية (NCGR)","orgLogo":"assets/ncgr.png",
 "program":"معسكر T5 لتقنيات إدارة الزحام (زحام) — أكاديمية سدايا","period":"يوليو–نوفمبر 2024","category":"employment","categories":["employment"],
 "impact":"انتقال إلى «Data & AI Engineer» بدوام كامل في المركز الوطني لنظم الموارد الحكومية (NCGR) في سبتمبر 2025 — بعد عشرة أشهر من إتمام المعسكر.",
 "story":"أتمّ صالح معسكر T5 لتقنيات إدارة الزحام بأكاديمية سدايا (نوفمبر 2024) وطوّر مع فريقه مشروع DeepTraffic لإدارة إشارات المرور بـYOLO وU-Net وDeep SORT. وفي نوفمبر 2024 التحق بوظيفة «عالم بيانات» بدوام كامل في برق — في شهر الإتمام نفسه، فلا تُحتسب وفق قاعدة التزامن — ثم انتقل في سبتمبر 2025 إلى «مهندس بيانات وذكاء اصطناعي» بدوام كامل في المركز الوطني لنظم الموارد الحكومية. النتيجة المحتسبة هي هذا الانتقال إلى جهة عمل جديدة في دور بيانات وذكاء اصطناعي، بعد عشرة أشهر من الإتمام. وكان قبل المعسكر مدير مشاريع في «أنيس».",
 "achievements":["إتمام معسكر T5 لتقنيات إدارة الزحام — أكاديمية سدايا (نوفمبر 2024)، مشروع DeepTraffic","عالم بيانات بدوام كامل — برق (نوفمبر 2024)","مهندس بيانات وذكاء اصطناعي بدوام كامل — NCGR (سبتمبر 2025)"],
 "links":[{"label":"LinkedIn","url":"https://www.linkedin.com/in/saleh-altuwaijri"}],
 "provenance":"صفحة الخبرة على LinkedIn بحساب مسجَّل، بتواريخ بمستوى الشهر (barq — Data Scientist · Full-time نوفمبر 2024 – سبتمبر 2025؛ NCGR — Data & AI Engineer · Full-time منذ سبتمبر 2025) + منشور تخرّجه من المعسكر + سجل الأكاديمية #49. "+VER},
{"id":"majid-almadani","year":2024,"quote":{"text":"قيادة فريق «سُم» في معسكر T5 علّمتني أن أحوّل البيانات إلى قرار، وهذا ما أفعله اليوم في التحليلات المتقدمة والذكاء الاصطناعي.","kind":"draft"},
 "name":"ماجد المدني","nameEn":"Majid Almadani","photo":None,"role":"أخصائي أول تحليلات متقدمة وذكاء اصطناعي","org":"البنك السعودي للاستثمار (SAIB)","orgLogo":None,
 "program":"معسكر T5 — أكاديمية سدايا (قائد فريق «سُم»)","period":"أكتوبر 2024","category":"employment","categories":["employment"],
 "impact":"ترقية إلى «Senior Specialist Advanced Analytics & AI» في البنك السعودي للاستثمار في أكتوبر 2025 — بعد اثني عشر شهرًا من إتمام المعسكر.",
 "story":"قاد ماجد فريق «سُم» في معسكر T5 بأكاديمية سدايا (أكتوبر 2024)، وهو مشروع لإدارة المرور والتسعير الديناميكي بـYOLOv8 حصد 78 من 100 في ترتيب المعسكر. وفي الشهر نفسه التحق ببرنامج تطوير الخريجين في البنك السعودي للاستثمار — وهذا متزامن مع الإتمام فلا يُحتسب — ثم رُقّي في أكتوبر 2025 إلى «أخصائي أول تحليلات متقدمة وذكاء اصطناعي»، يعمل على نماذج التجزئة والتصنيف والتنبؤ والتوصية وخطوط البيانات ولوحات المعلومات. النتيجة المحتسبة هي هذه الترقية إلى دور تحليلات وذكاء اصطناعي بعد اثني عشر شهرًا من الإتمام.",
 "achievements":["قائد فريق «سُم» في معسكر T5 — 78/100 (أكتوبر 2024)","الالتحاق ببرنامج تطوير الخريجين — البنك السعودي للاستثمار (أكتوبر 2024)","ترقية إلى أخصائي أول تحليلات متقدمة وذكاء اصطناعي (أكتوبر 2025)"],
 "links":[{"label":"LinkedIn","url":"https://www.linkedin.com/in/majidalmadani"}],
 "provenance":"صفحة الخبرة على LinkedIn بحساب مسجَّل، بتواريخ بمستوى الشهر (The Saudi Investment Bank — SGDP أكتوبر 2024 – أكتوبر 2025؛ Senior Specialist Advanced Analytics & AI منذ أكتوبر 2025) + سجل الأكاديمية #28 (قائد فريق «سُم»، T5 أكتوبر 2024). "+VER},
{"id":"meead-alshaibani","year":2026,"quote":{"text":"التدريب الاحترافي في النماذج اللغوية الكبيرة مع سدايا وNVIDIA منحني الأساس الذي أعمل به اليوم مهندسةَ ذكاء اصطناعي.","kind":"draft"},
 "name":"ميعاد الشيباني","nameEn":"Meead Alshaibani","photo":None,"role":"مهندسة ذكاء اصطناعي","org":"صندوق التنمية العقارية (REDF)","orgLogo":None,
 "program":"التدريب الاحترافي في النماذج اللغوية الكبيرة (سدايا × NVIDIA) + برنامج شهادات NVIDIA — أكاديمية سدايا","period":"نوفمبر 2025 – فبراير 2026","category":"employment","categories":["employment"],
 "impact":"تعيين بدوام كامل «مهندسة ذكاء اصطناعي» في صندوق التنمية العقارية في يونيو 2026 — بعد أربعة أشهر من إتمام البرنامج.",
 "story":"أتمّت ميعاد التدريب الاحترافي في النماذج اللغوية الكبيرة الذي تقدّمه أكاديمية سدايا بالشراكة مع NVIDIA (نوفمبر–ديسمبر 2025)، وتعلّمت فيه معماريات النماذج اللغوية وهندسة الأوامر وأساليب الضبط الدقيق، ثم أكملت برنامج شهادات NVIDIA (فبراير 2026). وبعد تدريب تعاوني في صندوق التنمية العقارية (يناير–يونيو 2026) عُيّنت فيه «مهندسة ذكاء اصطناعي» بدوام كامل في يونيو 2026. التدريب التعاوني لا يُحتسب؛ النتيجة المحتسبة هي التعيين بدوام كامل، بعد أربعة أشهر من الإتمام.",
 "achievements":["إتمام التدريب الاحترافي في النماذج اللغوية الكبيرة — سدايا × NVIDIA (ديسمبر 2025)","تدريب تعاوني — صندوق التنمية العقارية (يناير–يونيو 2026)","مهندسة ذكاء اصطناعي بدوام كامل — صندوق التنمية العقارية (يونيو 2026)"],
 "links":[{"label":"LinkedIn","url":"https://www.linkedin.com/in/meead-alshaibani/"}],
 "provenance":"صفحة الخبرة على LinkedIn بحساب مسجَّل، بتواريخ بمستوى الشهر (SDAIA — Professional Trainee, Generative AI & LLMs نوفمبر–ديسمبر 2025؛ REDF — Coop يناير–يونيو 2026 ثم AI Engineer · Full-time منذ يونيو 2026) + كشف رسمي لمسار NVIDIA وسجل الأكاديمية #381. "+VER},
{"id":"hamad-alrashid","year":2025,"quote":{"text":"برنامج سدايا وأكسفورد كان جسري من التدريبات الدولية إلى أول وظيفة بدوام كامل في علوم البيانات والذكاء الاصطناعي في المملكة.","kind":"draft"},
 "name":"حمد الرشيد","nameEn":"Hamad Alrashid","photo":None,"role":"عالم بيانات ← مهندس ذكاء اصطناعي","org":"جاهز (Jahez)","orgLogo":"assets/jahez.png",
 "program":"معسكر سدايا–أكسفورد للذكاء الاصطناعي (بالشراكة مع كاوست وجامعة أكسفورد)","period":"أغسطس–أكتوبر 2025","category":"employment","categories":["employment"],
 "impact":"توظيف بدوام كامل «عالم بيانات» في جاهز في نوفمبر 2025 — بعد شهر من إتمام البرنامج — ثم «مهندس ذكاء اصطناعي» في موج (فبراير 2026).",
 "story":"اختير حمد ضمن ثلاثين مرشحًا لبرنامج سدايا–أكسفورد التنافسي للذكاء الاصطناعي وتعلم الآلة (تسعة أسابيع، أغسطس–أكتوبر 2025، بالشراكة مع كاوست وجامعة أكسفورد) ونال شهادة إنجازه. وفي نوفمبر 2025 التحق بوظيفة «عالم بيانات» بدوام كامل في شركة جاهز العالمية، ثم انتقل في فبراير 2026 إلى «مهندس ذكاء اصطناعي» في موج. وكانت تجاربه السابقة تدريبات صيفية (Vectara 2023 وArio 2024) لا تُحتسب. النتيجة المحتسبة هي التوظيف الأول بدوام كامل، بعد شهر واحد من الإتمام.",
 "achievements":["إتمام برنامج سدايا–أكسفورد للذكاء الاصطناعي (أكتوبر 2025) — واحد من 30 مرشحًا","عالم بيانات بدوام كامل — جاهز (نوفمبر 2025)","مهندس ذكاء اصطناعي بدوام كامل — موج (فبراير 2026)"],
 "links":[{"label":"LinkedIn","url":"https://www.linkedin.com/in/hamad-alrashid-3a94bb142/"},{"label":"GitHub","url":"https://github.com/HamadAlrashid"}],
 "provenance":"صفحة الخبرة على LinkedIn بحساب مسجَّل، بتواريخ بمستوى الشهر (SDAIA – University of Oxford AI Bootcamp أغسطس–أكتوبر 2025 مع شهادة إنجاز؛ Jahez — Data Scientist · Full-time نوفمبر 2025 – يناير 2026؛ Mawj — AI Engineer · Full-time منذ فبراير 2026) + سجل الأكاديمية #2274. "+VER},
{"id":"nujud-senan","year":2024,"quote":{"text":"من معسكر T5 انطلقتُ إلى الذكاء الاصطناعي الهجين الكمّي، وفاز مشروعنا بجائزة في قمة الابتكار الكمّي بدبي.","kind":"draft"},
 "name":"نجود سنان","nameEn":"Nujud Senan","photo":None,"role":"قائدة فريق مشروع ذكاء اصطناعي هجين كمّي","org":"قمة الابتكار الكمّي — دبي (Quantum Innovation Summit)","orgLogo":None,
 "program":"معسكر T5 — أكاديمية سدايا (استضافة أكاديمية طويق)","period":"يوليو–أكتوبر 2024","category":"awards","categories":["awards"],
 "impact":"جائزة قمة الابتكار الكمّي في دبي (مارس 2025) عن مشروع «ذكاء اصطناعي هجين كمّي للتنبؤ بالشيخوخة البيولوجية» — بعد خمسة أشهر من إتمام المعسكر.",
 "story":"أتمّت نجود معسكر T5 لعلوم البيانات والذكاء الاصطناعي بأكاديمية سدايا (يوليو–أكتوبر 2024). ثم قادت فريق مشروع «Quantum-Hybrid AI for Predicting and Understanding Biological Aging» الذي يدمج نموذج انحدار هجينًا كمّيًا-كلاسيكيًا للتنبؤ بالعمر من بيانات RNA، وطوّرت مكوّنه الكمّي، وفاز المشروع بجائزة قمة الابتكار الكمّي في دبي (اختُتمت القمة في مارس 2025). ثم التحقت بوزارة الاتصالات وتقنية المعلومات مديرةَ مشروع (مايو 2025). النتيجة المحتسبة هي الجائزة، وتاريخها مثبَّت بتاريخ القمة داخل النافذة.",
 "achievements":["إتمام معسكر T5 — أكاديمية سدايا (أكتوبر 2024)","جائزة قمة الابتكار الكمّي — دبي (مارس 2025) عن مشروع ذكاء اصطناعي هجين كمّي","عضوة مجلس إدارة الجمعية السعودية لتقنية الكمّ (منذ نوفمبر 2024)"],
 "links":[{"label":"LinkedIn","url":"https://www.linkedin.com/in/nujud-senan-3623b51b5/"}],
 "provenance":"صفحة الخبرة على LinkedIn بحساب مسجَّل (T5 Bootcamp at Tuwaiq Academy — SDAIA يوليو–أكتوبر 2024؛ Quantum-Hybrid AI Developer — Quantum Innovation Summit سبتمبر 2024 – فبراير 2025 مع نص الفوز بالجائزة) + صفحة القمة الرسمية (quantuminnovationsummit.com: اختتام قمة 2025 في مارس 2025 ونهائيات تحدي QInnovision) + سجل الأكاديمية #2715. تنويه: الجائزة مذكورة في ملفها ولم يُعثر على اسمها في قائمة الفائزين المنشورة. "+VER},
]
IDS={'saleh-altuwaijri':49,'majid-almadani':28,'meead-alshaibani':381,'hamad-alrashid':2274,'nujud-senan':2715}
# ---- data.js
P=H+'SuccessStories/website/js/data.js'; bk(P); s=open(P,encoding='utf-8').read()
r0=s.index('"id": "randa-almohammadi"'); end=s.index('\n];',r0)+1
ins=''.join('  '+json.dumps(x,ensure_ascii=False)+',\n' for x in ST)
s=s[:end]+ins+s[end:]
s=rep(s,"{ value: 112,  label: 'قصة نجاح موثّقة'","{ value: 117,  label: 'قصة نجاح موثّقة'",1)
s=rep(s,"{ value: 69,   label: 'جهة عمل'","{ value: 72,   label: 'جهة عمل'",1)
s=rep(s,"'use strict';","/* 30 سبتمبر 2026 (ب): فحص قصص النجاح لقاعدة الخريجين — 5 قصص جديدة (صالح التويجري · ماجد المدني · ميعاد الشيباني · حمد الرشيد · نجود سنان) من صفحات الخبرة على LinkedIn؛ 112 ← 117 قصة، وجهات العمل 69 ← 72 (البنك السعودي للاستثمار · صندوق التنمية العقارية · جاهز؛ الجائزة لا تُحتسب جهة عمل). */\n'use strict';",1)
open(P,'w',encoding='utf-8').write(s)
subprocess.check_call(['node','--check',P])
# ---- stories index JSON-LD
P=H+'SuccessStories/website/index.html'; bk(P); s=open(P,encoding='utf-8').read()
s=rep(s,'"numberOfItems": 112','"numberOfItems": 117',1); open(P,'w',encoding='utf-8').write(s)
# ---- portal
P=H+'index.html'; bk(P); s=open(P,encoding='utf-8').read()
s=rep(s,'data-count="112"','data-count="117"',1); s=rep(s,'data-count="69"','data-count="72"',1)
s=rep(s,'(112 قصة عبر 69 جهة عمل)','(117 قصة عبر 72 جهة عمل)'); s=rep(s,'(112 stories across 69 employers)','(117 stories across 72 employers)')
s=rep(s,'في 69 جهة عمل','في 72 جهة عمل'); s=rep(s,'across 69 government','across 72 government')
s=rep(s,'# موقع قصص النجاح — 112 قصة','# موقع قصص النجاح — 117 قصة'); s=rep(s,'# success-stories site — 112 stories','# success-stories site — 117 stories')
s=rep(s,'3,180 سجلًا · 112 قصة','3,180 سجلًا · 117 قصة'); s=rep(s,'3,180 records · 112 stories','3,180 records · 117 stories')
open(P,'w',encoding='utf-8').write(s)
# ---- Graduates page counters + DATA notes
P=H+'Graduates/index.html'; bk(P); s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+13; j=s.index('\nconst SITE_STATS'); D=json.loads(s[i:j].rstrip()[:-1]); g=D['grads']; assert len(g)==3180
head,tail=s[:i],s[j:]
tail=rep(tail,"— عبر 69 جهة عمل'","— عبر 72 جهة عمل'",1); tail=rep(tail,"— across 69 employers'","— across 72 employers'",1)
tail=re.sub(r"\{ value: 112,(\s+)label: 'قصة نجاح موثّقة'",r"{ value: 117,\1label: 'قصة نجاح موثّقة'",tail)
assert "{ value: 117," in tail
for part in ('head','tail'):
    t=locals()[part]
    t=t.replace('للمجموعة الكاملة (112 قصة)','للمجموعة الكاملة (117 قصة)').replace('For the full collection (112 stories)','For the full collection (117 stories)')
    t=t.replace('112 قصة نجاح موثّقة (معيار','117 قصة نجاح موثّقة (معيار').replace('112 verified success stories (14-month','117 verified success stories (14-month')
    if part=='head': head=t
    else: tail=t
V=json.load(open('verdicts30.json'))
TAG='[فحص قصص النجاح — 30 سبتمبر 2026] '
for k,v in V.items():
    x=g[int(k)-1]; assert x['n']==v['n'],(k,x['n'],v['n'])
    x['d']=(x['d'].rstrip()+' '+TAG+v['t']).strip()
    for f in ('emp','role'):
        if v.get(f): x[f]=v[f]
    if v.get('job'): x['cats']=sorted(set(x['cats'])|{'job'}); x['score']=max(x['score'],90)
s=head+json.dumps(D,ensure_ascii=False)+';'+tail
open(P,'w',encoding='utf-8').write(s)
json.dump(g,open('grads_after2.json','w'),ensure_ascii=False)
rest=head+tail
print('grad leftovers 112:',len(re.findall(r'(?<!\d)112 (قصة|stor|verified)',rest)),'69 emp:',rest.count('69 جهة')+rest.count('69 employers'))
print('ok')
