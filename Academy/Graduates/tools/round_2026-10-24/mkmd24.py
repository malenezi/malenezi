# -*- coding: utf-8 -*-
# Builds the two comprehensive MD files from the live data (15 Oct 2026).
import json,re,os,collections
H=os.path.expanduser('~/mnt/Academy/')
s=open(H+'Graduates/index.html',encoding='utf-8').read()
i=s.index('const DATA = ')+13;j=s.index('\nconst SITE_STATS'); g=json.loads(s[i:j].rstrip()[:-1])['grads']; N=len(g)
js=open(H+'SuccessStories/website/js/data.js',encoding='utf-8').read()
a=js.index('const STORIES = [')+len('const STORIES = '); b=js.index('\n];',a)+2; ST=json.loads(js[a:b])
DATE='24 أكتوبر 2026'
TRK=[('ai','مهندس ذكاء اصطناعي','AI Engineer'),('ds','عالم بيانات','Data Scientist'),('genai','أكاديمية الذكاء الاصطناعي التوليدي','Gen AI Academy'),('dmg','إدارة وحوكمة البيانات','Data Management & Governance'),('coop','التدريب التعاوني','Cooperative Training (COOP)'),('other','برامج متخصصة أخرى','Other / Specialized')]
TL={k:a for k,a,_ in TRK}
def c(x): return re.sub(r'\s+',' ',str(x or '')).replace('|','¦').strip()
def pct(x,n): return '%.1f%%'%(100*x/n) if n else '—'
def fmt(n): return format(n,',')
def years(co):
    return sorted(set('20'+y for y in re.findall(r'20(2[1-6])',co or '')))
def first_year(co):
    y=years(co); return y[0] if y else None
def plink(r):
    L=r['links']
    for lab,u in L:
        if 'linkedin.com/in/' in u: return u
    for lab,u in L:
        if re.match(r'https://github\.com/[^/]+/?$',u): return u
    return L[0][1] if L else ''
# ----------------------------- GRADUATES -----------------------------
T=collections.Counter(r['tr'] for r in g)
fy=collections.Counter(first_year(r['co']) or 'غير محددة' for r in g)
anyy=collections.Counter(y for r in g for y in years(r['co']))
mat=collections.defaultdict(collections.Counter)
for r in g: mat[first_year(r['co']) or 'غير محددة'][r['tr']]+=1
hi=sum(1 for r in g if r['score']>=75); mid=sum(1 for r in g if 45<=r['score']<75); lo=N-hi-mid
wl=sum(1 for r in g if r['links']); uu=len({l[1].rstrip('/') for r in g for l in r['links']})
li=sum(1 for r in g if any('linkedin.com/in/' in l[1] for l in r['links']))
gh=sum(1 for r in g if any('github.com' in l[1] for l in r['links']))
emp=sum(1 for r in g if r.get('emp')); en=sum(1 for r in g if r.get('en')); noco=sum(1 for r in g if not years(r['co']))
win=collections.Counter(r.get('win') or '—' for r in g)
story_by_rec={}
for x in ST:
    for m in re.findall(r'#(\d{1,4})\b',x['provenance']):
        k=int(m)
        if k<=N: story_by_rec.setdefault(k,x['id'])
def pnorm(p):
    p=re.sub(r'\s*[\(（][^)]*[\)）]','',p); p=re.sub(r'\s*[—–-]\s*أكاديمية سدايا.*$','',p); p=re.sub(r'\s+',' ',p).strip(' —-')
    return p
progs=collections.Counter()
for r in g:
    for part in re.split(r'\s\+\s',r['prog'] or ''):
        if part.strip(): progs[pnorm(part)]+=1
O=[]
O+=['# قاعدة بيانات خريجي أكاديمية سدايا — الإصدار الشامل','# SDAIA Academy Graduates Database — Comprehensive Edition','',
 f'**الإصدار:** {DATE} · **المصدر:** `Graduates/index.html` (DATA.grads) مطابق صفًا بصف لـ `Graduates_Database.xlsx` · **الترقيم:** «#N» = السجل رقم N في هذا الإصدار (بعد دمج واستبعاد 11 أكتوبر 2026؛ جولات 13 و15 و17 أكتوبر و17 أكتوبر (ب) و18 و19 و21 و24 أكتوبر أضافت #3353–#3566 دون إعادة ترقيم).','',
 '> هذا الملف لقطة موحّدة ونظيفة للقاعدة كما هي اليوم. سجلّ الجولات التاريخي (بترقيمه المحلي) باقٍ في `Graduates_Database.md`.','',
 '## 1. الملخص التنفيذي — Executive summary','','| المؤشر | القيمة |','|---|---|',
 f'| إجمالي الخريجين الموثّقين (سجلات فردية) | **{fmt(N)}** |',
 f'| قصص نجاح مرتبطة بسجلات القاعدة | **{len(ST)}** |',
 f'| المسارات المعيارية | 6 |',
 f'| الدفعات | 2021 – 2026 |',
 f'| سجلات بجهة عمل موثّقة | {fmt(emp)} ({pct(emp,N)}) |',
 f'| سجلات برابط تحقق علني | {fmt(wl)} ({pct(wl,N)}) — {fmt(uu)} رابطًا فريدًا |',
 f'| منها بحساب LinkedIn / GitHub | {fmt(li)} / {fmt(gh)} |',
 f'| سجلات بالاسم الإنجليزي | {fmt(en)} ({pct(en,N)}) |',
 f'| ثقة مرتفعة (≥75) · متوسطة (45–74) · منخفضة (<45) | {fmt(hi)} · {fmt(mid)} · {fmt(lo)} |','',
 '## 2. التوزيع حسب المسار — By standard track','','| المسار | Track | السجلات | النسبة |','|---|---|---:|---:|']
for k,ar,e in TRK: O.append(f'| {ar} | {e} | {fmt(T[k])} | {pct(T[k],N)} |')
O+=[f'| **الإجمالي** | **Total** | **{fmt(N)}** | 100% |','',
 '## 3. التوزيع حسب سنة الدفعة — By cohort year','',
 'السنة الأولى المذكورة في حقل الدفعة لكل سجل (لكل سجل سنة واحدة). العمود الأخير يعدّ السجل في كل سنة يذكرها (من درس في أكثر من سنة يُعدّ أكثر من مرة).','',
 '| السنة | '+' | '.join(e for _,_,e in TRK)+' | الإجمالي | ذِكر السنة في أي برنامج |','|---|'+'---:|'*len(TRK)+'---:|---:|']
for y in ['2021','2022','2023','2024','2025','2026','غير محددة']:
    O.append(f'| {y} | '+' | '.join(str(mat[y][k]) for k,_,_ in TRK)+f' | **{fmt(sum(mat[y].values()))}** | {fmt(anyy.get(y,0)) if y!="غير محددة" else "—"} |')
O+=['','## 4. تركيز 2024 – 2026 — Focus on recent cohorts','',
 f'سجلات سنتها الأولى 2024: **{fmt(sum(mat["2024"].values()))}** · 2025: **{fmt(sum(mat["2025"].values()))}** · 2026: **{fmt(sum(mat["2026"].values()))}** — أي **{fmt(sum(sum(mat[y].values()) for y in ("2024","2025","2026")))}** سجلًا ({pct(sum(sum(mat[y].values()) for y in ("2024","2025","2026")),N)} من القاعدة).','',
 '**جولة 24 أكتوبر 2026 (ج):** 3 قصص جديدة (SASO · أكسنتشر · الرائدة) و11 إثراءً بتواريخ شهرية؛ تصحيح الاسم «دنا الصالحي». **جولة 24 أكتوبر 2026 (ب):** ملف الأكاديمية «May–Oct 2026» (21 اسمًا): 4 سجلات جديدة و7 إثراءات، وعلي الغامدي متدربًا تعاونيًا (#3562–#3566)؛ ورويدا الشهري ليست قصة نجاح. **جولة 24 أكتوبر 2026 — مسح خريجي يناير 2023 – أبريل 2026:** 24 سجلًا جديدًا (#3538–#3561) من صفحات الخبرة على LinkedIn لملفات ظهرت في بحث الأشخاص «Bootcamp at SDAIA» و«Trainee at SDAIA» و«Coop Trainee SDAIA» (معسكر T5 للدفعات 2023–2024، معسكر زحام 2024، ممارس تعلم الآلة، معسكر LLM، معسكر سدايا–أكسفورد، ServiceNow، إدارة الأنظمة السحابية، بناء تطبيقات الذكاء الاصطناعي، المسارات المتقدمة، و5 من التدريب التعاوني 2025–2026، و3 سجلات 2021–2022)؛ و19 إثراءً بروابط LinkedIn؛ و3 قصص جديدة (Newera.ai · شركة علم · جهة حكومية غير معلنة). **جولة 21 أكتوبر 2026:** 17 سجلًا جديدًا (#3521–#3537): 14 من منشورات إتمام على LinkedIn (هندسة أنظمة الذكاء الاصطناعي الوكيلي المتقدمة، هندسة تطبيقات النماذج اللغوية الكبيرة، أساليب تعلم الآلة المتقدمة، التجريب واختبارات A/B، برنامج مبرمجي الذكاء الاصطناعي، ورشة صناعة المحتوى بالذكاء الاصطناعي) و2 من قسم الشهادات (SDAIA T5) و1 من GitHub (SDA-AIE-113)؛ وإثراء واحد؛ ولا قصص جديدة؛ وصور GitHub محلية لـ11 قصة وشعارات 8 جهات عمل. **جولة 19 أكتوبر 2026:** 6 سجلات من مستودعات GitHub (#3515–#3520) وشعارات SNB وSAMI وMNGHA. **جولة 18 أكتوبر 2026 — خريجو 2021–2024:** 48 سجلًا جديدًا (#3467–#3514) من صفحات الخبرة على LinkedIn لملفات ظهرت في بحث الأشخاص «T5 bootcamp SDAIA» وبحث المحتوى (معسكر T5 للدفعات 2021 و2023 و2024، ومعسكر تقنيات إدارة الزحام 2024، والتدريب التعاوني)، كلها بمدخل خبرة مؤرخ بالشهر؛ و28 إثراءً (روابط LinkedIn وتواريخ بمستوى الشهر لسجلات قائمة، وحسم انتساب #2249 لمعسكر T5)؛ و13 قصة جديدة (وزارة العدل · وزارة التجارة · أداء · المركز الوطني للتأمين الصحي · دراهم · الشؤون الصحية بالحرس الوطني · مركز الملك عبدالعزيز للتواصل الحضاري · القرارات الذكية · علم · SDM · سدايا · جهتان حكوميتان غير معلنتين). **جولة 17 أكتوبر 2026 (ب) — خريجو 2024–2026:** 58 سجلًا جديدًا (#3409–#3466): 54 من منشورات إتمام/شهادات على LinkedIn (البرمجة التوليدية، هندسة الأوامر، الذكاء الاصطناعي التوليدي للإنتاجية، رفع الإنتاجية، تطوير حلول الذكاء الاصطناعي التوليدي، الأنظمة التوكيلية، هندسة البيانات الحديثة، NVIDIA، CDMP وحوكمة البيانات وغيرها) و4 من ملفات GitHub؛ و44 إثراءً (منها 28 سجلًا داخليًا بلا رابط حصلت على رابط LinkedIn واسم لاتيني)؛ وثلاث قصص جديدة (رشد للحلول · دراية المالية · بنك الجزيرة — ترقية). **جولة 17 أكتوبر 2026:** 32 سجلًا جديدًا (#3377–#3408): 21 من مستودعات المشاريع الختامية على GitHub (هندسة البيانات الحديثة، هندسة أنظمة الذكاء الاصطناعي الوكيلي المتقدمة، الرؤية الحاسوبية، البرمجة التوليدية، تطوير حلول الذكاء الاصطناعي التوليدي، السلاسل الزمنية، أساسيات الذكاء الاصطناعي لبيئة العمل) و11 من منشورات إتمام/شهادات على LinkedIn؛ و13 إثراءً؛ و3 قصص نجاح جديدة (الشركة القابضة للصحة · مصرف الإنماء · KACST/MIT). **جولة 15 أكتوبر 2026:** 13 سجلًا جديدًا (#3363–#3375): 12 من دفعة أكتوبر 2026 لدورة السلاسل الزمنية (تفريعات مشروع «المسافرون الدوليون» مع إيداعات المالكين) و1 من منشورات LinkedIn (هندسة أنظمة الذكاء الاصطناعي الوكيلي المتقدمة)؛ و11 إثراءً (منها سجل فرح الربح #3308 بدل تكرار)؛ وقصة جديدة لخريجة معسكر إدارة البيانات 2023 (ماستر ووركس)، وروابط LinkedIn لأربع بطاقات قصص. **جولة 13 أكتوبر 2026:** 10 سجلات جديدة (#3353–#3362): 3 من GitHub (مشروع نهائي لمقرر الرؤية الحاسوبية SDA-AIE-212 وتسليمان لمشروع «وكيل البحث العميق») و7 من منشورات LinkedIn وشهاداتها (دفعات أكتوبر 2026، إضافة إلى خريج معسكر LLM يناير 2024)؛ و8 إثراءات ضبطت الدفعات من شهادات بتواريخ يومية؛ وقصتان جديدتان لخريجي دفعة 2024 (ويدو سوليوشنز · وتد الطبية). جولة 11 أكتوبر سبقتها بـ32 سجلًا من دفعات سبتمبر–أكتوبر 2026.','',
 '## 5. البرامج الأكثر تمثيلًا — Top programmes (normalized names)','','| # | البرنامج | السجلات |','|---:|---|---:|']
for n_,(p,cnt) in enumerate(progs.most_common(40),1): O.append(f'| {n_} | {c(p)} | {cnt} |')
O+=['',f'إجمالي صيغ البرامج المختلفة بعد التوحيد: {len(progs)}.','',
 '## 6. جودة البيانات والنطاق الزمني — Data quality','','| النطاق الزمني (معيار الأربعة عشر شهرًا) | السجلات |','|---|---:|']
for k,v in win.most_common(): O.append(f'| {c(k)} | {fmt(v)} |')
O+=['',f'سجلات بلا سنة دفعة محددة: **{fmt(noco)}** (أغلبها قائمة NVIDIA الرسمية بلا تواريخ). سجلات بلا اسم إنجليزي: **{fmt(N-en)}** (قوائم رسمية بلا روابط).','',
 '**تدقيق 18 أكتوبر 2026 (بلا ملاحظات مفتوحة):** لا معرّف LinkedIn ولا حساب GitHub مشترك بين سجلين · لا روابط مكررة داخل السجل · المسارات والدرجات ضمن القيم المسموحة · صفوف xlsx مطابقة لقاعدة البيانات صفًا بصف · العدادات متسقة في البوابة وصفحة الخريجين وموقع القصص والـxlsx · كل مراجع الصور والملفات المحلية تعمل · لا نص `**` في الحقول المعروضة.','',
 '## 7. المنهجية والمصادر — Methodology','',
 '- **وحدة القاعدة:** شخص واحد = سجل واحد؛ من أتمّ أكثر من برنامج تُضمّ برامجه بـ « + » ودفعاته بـ « · ».',
 '- **من يُعدّ خريجًا:** من أتمّ برنامجًا تدريبيًا في الأكاديمية بدليل (قائمة رسمية، شهادة، منشور إتمام، مستودع تسليم أو مشروع ختامي مؤرخ). **الموظفون والمدربون ليسوا خريجين**، ومن نشر قبولًا أو بداية برنامج فقط لا يُضاف حتى يُثبت الإتمام.',
 '- **الهوية:** سمتان مستقلتان على الأقل (الاسم + البرنامج/الدفعة/الحساب)؛ اسم المستخدم وحده لا يكفي. الأسماء العربية المنقولة حرفيًا موسومة بتنويه في وصف السجل.',
 '- **كشف التكرار:** تجميع بالرابط الشخصي (LinkedIn/GitHub)، ثم الاسم المطبّع عربيًا ولاتينيًا، ثم المطابق الصوتي `translit.py`، ثم ثلاثية (البرنامج، السنة، الجهة). الدمج بقرار أ. د. ممدوح فقط: يُبقى الرقم الأدنى وتُضمّ الحقول والروابط ويُحفظ الاسم الآخر في alias. الأسماء الشائعة بلا رابط مشترك تُربط بإشارة متبادلة ولا تُدمج.',
 '- **درجة الثقة:** 0–100 بحسب قوة المصدر (قائمة رسمية/شهادة > منشور إتمام موثّق > مستودع تسليم يسمّي المقرر > استنتاج).',
 '- **المصادر:** قوائم الأكاديمية الرسمية وسجلات الشهادات وقوائم الإشراف؛ LinkedIn (صفحات الخبرة والشهادات والمنشورات بحساب مسجَّل)؛ GitHub (مستودعات المقررات والمشاريع الختامية وجداول الفرق)؛ ملفات مزوّدة من أ. د. ممدوح العنزي. **المواقع الوسيطة (brokers) ممنوعة مصدرًا ورابطًا.**','',
 '## 8. بنود مفتوحة — Open items','',
 '- **مرشحون معلّقون (أسماء ناقصة أو تطابق غير محسوم):** Shatha Alghamdi (سجلان بالاسم نفسه) · Layan Al-Shehri (مطابق محتمل #1977) · Abdulaziz B. · Raghad1015 · nfsh46655-jpg · Naif-aln · Afnan633 · Lalnefaie · arwam-m · sfom30 · Reema D. Alanazi.',
 '- **قبول/بداية فقط (يُضافون بعد الإتمام):** Hassan Almakinah · Essa Almaymuni · Hamad Al-Mutairi · Rana Almohethef · Alhanouf Aldossary.',
 f'- **فجوات بيانات لا تُغلق من مصادر علنية:** {fmt(N-en)} سجلًا بلا اسم إنجليزي، و{fmt(noco)} بلا دفعة محددة.','',
 '## 9. السجل الكامل — Full registry','',
 f'{fmt(N)} سجلًا مرتبة بالرقم. «الرابط» هو الرابط الأساسي (LinkedIn أولًا ثم GitHub)؛ الروابط كلها في `Graduates_Database.xlsx`. ⭐ = للخريج قصة نجاح منشورة.','',
 '| # | الاسم | Name | البرنامج | المسار | الدفعة | جهة العمل | الثقة | الرابط |','|---:|---|---|---|---|---|---|---:|---|']
for k,r in enumerate(g,1):
    star=' ⭐' if k in story_by_rec else ''
    O.append(f"| {k} | {c(r['n'])}{star} | {c(r.get('en'))} | {c(r['prog'])} | {TL[r['tr']]} | {c(r['co'])} | {c(r.get('emp'))} | {r['score']} | {plink(r)} |")
O+=['',f'— نهاية الملف · {fmt(N)} سجلًا · أُنتج آليًا من البيانات الحية في {DATE} —','']
GP=H+'Graduates/SDAIA_Graduates_Comprehensive_2026-10-24.md'; open(GP,'w',encoding='utf-8').write('\n'.join(O))
# ----------------------------- STORIES -----------------------------
CAT={'employment':'التوظيف والتقدم المهني','leadership':'القيادة والمواقع الرفيعة','research':'البحث والنشر العلمي','opensource':'المصادر المفتوحة','awards':'الجوائز والزمالات'}
UN={'جهة حكومية','جهة حكومية (غير معلنة)','غير معلنة',''}
yc=collections.Counter(x['year'] for x in ST); cc=collections.Counter(x['category'] for x in ST)
qk=collections.Counter(x['quote'].get('kind') for x in ST)
orgs=collections.Counter(x['org'] for x in ST)
named_emp={x['org'] for x in ST if x['category'] in ('employment','leadership') and x['org'] not in UN}
ph=sum(1 for x in ST if x.get('photo')); lg=sum(1 for x in ST if x.get('orgLogo'))
def rec_of(x):
    m=re.findall(r'#(\d{1,4})\b',x['provenance']); return [int(v) for v in m if int(v)<=N]
Ys=sorted(yc)
S=['# قصص نجاح خريجي أكاديمية سدايا — الإصدار الشامل','# SDAIA Academy Graduate Success Stories — Comprehensive Edition','',
 f'**الإصدار:** {DATE} · **المصدر:** `SuccessStories/website/js/data.js` (STORIES) · كل قصة مربوطة برقم سجل الخريج في `SDAIA_Graduates_Comprehensive_2026-10-24.md`.','',
 '## 1. الملخص — Summary','','| المؤشر | القيمة |','|---|---|',
 f'| قصص نجاح موثّقة | **{len(ST)}** |',
 f'| جهات العمل المسمّاة (قاعدة العدّ الرسمية المنشورة) | **91** |',
 f'| جهات مسمّاة في قصص التوظيف والقيادة (عدّ آلي بلا توحيد صيغ) | {len(named_emp)} |',
 f'| خريجون في قاعدة البيانات | {fmt(N)} — نسبة القصص {pct(len(ST),N)} |',
 f'| اقتباسات معتمدة / مسودات | {qk.get("verified",0)} / {qk.get("draft",0)} |',
 f'| صور شخصية / شعارات جهات | {ph} / {lg} من {len(ST)} |','',
 '### حسب سنة التخرج','','| السنة | القصص |','|---|---:|']+[f'| {y} | {yc[y]} |' for y in Ys]+['',
 '### حسب الفئة','','| الفئة | القصص |','|---|---:|']+[f'| {CAT.get(k,k)} | {v} |' for k,v in cc.most_common()]+['',
 '## 2. المعيار — The 14-month criterion (Policy v1.0)','',
 '- **إثبات مؤرّخ داخل النافذة:** إنجاز (توظيف، ترقية، جائزة، نشر، مساهمة مفتوحة المصدر) مؤرّخ بالشهر ضمن أربعة عشر شهرًا من إتمام البرنامج.',
 '- **مصدر موثوق غير وسيط:** صفحة الخبرة على LinkedIn، صفحات مؤسسية، منشورات، سجلات الأكاديمية. المواقع الوسيطة ممنوعة.',
 '- **الصلة بالتدريب (البند 5-و):** يجب أن يكون الإنجاز في مجال البرنامج؛ وظيفة دعم فني أو تسويق بعد برنامج علوم بيانات لا تُحتسب — وهو أكثر أسباب الرفض شيوعًا.',
 '- **الإنجاز يتبع التدريب:** شهادة البرنامج نفسها ومشروعه الختامي مخرجات تدريب لا إنجاز لاحق؛ والإنجاز في شهر الإتمام نفسه يُرجأ.',
 '- **الاقتباس:** «verified» إذا صدر عن الخريج أو أقرّته الأكاديمية، و«draft» إذا صيغ من الأدلة بانتظار الاعتماد.','',
 '## 3. جهات العمل — Employers and organisations','','| الجهة | القصص |','|---|---:|']+[f'| {c(o) or "—"} | {v} |' for o,v in sorted(orgs.items(),key=lambda t:(-t[1],t[0]))]+['',
 '## 4. فهرس القصص — Index','','| # | الاسم | Name | السنة | الجهة | الفئة | سجل الخريج |','|---:|---|---|---:|---|---|---|']
ordered=sorted(ST,key=lambda x:(x['year'],x['name']))
for n_,x in enumerate(ordered,1):
    S.append(f"| {n_} | {c(x['name'])} | {c(x['nameEn'])} | {x['year']} | {c(x['org'])} | {CAT.get(x['category'],x['category'])} | {' · '.join('#%d'%k for k in rec_of(x)) or '—'} |")
S+=['','## 5. القصص بالتفصيل — Full stories','']
cur=None; n_=0
for x in ordered:
    if x['year']!=cur:
        cur=x['year']; S+=[f'### دفعة {cur} — Class of {cur} ({yc[cur]} قصة)','']
    n_+=1
    flag=' · ⚠ مراجعة: '+c(x['reviewFlag']) if x.get('reviewFlag') else ''
    S+=[f"#### {n_}. {c(x['name'])} — {c(x['nameEn'])}",'',
        f"- **الجهة والدور:** {c(x['org'])} — {c(x['role'])}",
        f"- **البرنامج:** {c(x['program'])} · **الفترة:** {c(x['period'])}",
        f"- **الفئة:** {', '.join(CAT.get(k,k) for k in x.get('categories') or [x['category']])}{flag}",
        f"- **سجل الخريج:** {' · '.join('#%d'%k for k in rec_of(x)) or '—'} · **المعرّف:** `{x['id']}`",
        f"- **الأثر:** {c(x['impact'])}",'',
        c(x['story']),'']
    if x.get('achievements'): S+=['**الإنجازات:**','']+[f'- {c(t)}' for t in x['achievements']]+['']
    q=x.get('quote') or {}
    if q.get('text'): S+=[f"> «{c(q['text'])}» — *{'اقتباس معتمد' if q.get('kind')=='verified' else 'مسودة بانتظار الاعتماد'}*",'']
    if x.get('links'): S+=['**الروابط:** '+' · '.join(f"[{c(l['label'])}]({l['url']})" for l in x['links']),'']
    S+=[f"**التوثيق:** {c(x['provenance'])}",'','---','']
S+=[f'— نهاية الملف · {len(ST)} قصة · أُنتج آليًا من البيانات الحية في {DATE} —','']
SP=H+'SuccessStories/SDAIA_Success_Stories_Comprehensive_2026-10-24.md'; open(SP,'w',encoding='utf-8').write('\n'.join(S))
print(GP,os.path.getsize(GP)); print(SP,os.path.getsize(SP)); print('stories w/o record',[x['id'] for x in ST if not rec_of(x)]); print('top progs',progs.most_common(3))
print({y:sum(mat[y].values()) for y in mat})
