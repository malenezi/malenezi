# -*- coding: utf-8 -*-
# 30 Oct 2026 (b): Success-Story Policy v2.0 (12 months; employment / promotion / founder; programme-related),
# 5 rulings published, re-audit of all stories, placeholder photos, all quotes approved (<=97 chars), bigger logos.
import json,re,os,sys,shutil,collections,openpyxl
DRY='--apply' not in sys.argv
H=os.path.expanduser('~/mnt/Academy/'); W=H+'SuccessStories/website/'
DATE='30 أكتوبر 2026'; TAG='[السياسة v2.0 — 30 أكتوبر 2026] '
BK=H+'_backups/2026-10-30b/'
FILES=['SuccessStories/website/js/data.js','SuccessStories/website/index.html','SuccessStories/website/css/style.css','index.html','Graduates/index.html','Graduates/Graduates_Database.xlsx','Graduates/Graduates_Database.md']
def rep(s,a,b,c=None):
    n=s.count(a); assert n>=1,('missing',a[:90])
    if c is not None: assert n==c,(a[:90],n)
    return s.replace(a,b)
EXCL={'جهة حكومية','جهة حكومية (غير معلنة)','غير معلنة','قمة الابتكار الكمّي — دبي (Quantum Innovation Summit)','مركز «ذكاء» — منشآت','مهمة OSACT7 المشتركة — LREC 2026','Private Data Department'}
def emp_count(st): return len({x['org'].strip() for x in st if x.get('org')}-EXCL)
# ---------------- load ----------------
dj=W+'js/data.js'; sj=open(dj,encoding='utf-8').read()
k=sj.index('const STORIES = [');e=sj.index('\n];',k)
ST=[json.loads(l.strip().rstrip(',')) for l in sj[k:e].split('\n')[1:] if l.strip().startswith('{')]
S0=len(ST); E0=emp_count(ST); assert (S0,E0)==(226,122),(S0,E0)
P_=H+'Graduates/index.html'; s=open(P_,encoding='utf-8').read()
i=s.index('const DATA = ')+13; j=s.index('\nconst SITE_STATS'); D=json.loads(s[i:j].rstrip()[:-1]); g=D['grads']; head=s[:i]; tail=s[j:]; assert len(g)==3952
X_=H+'Graduates/Graduates_Database.xlsx'; wb=openpyxl.load_workbook(X_); ws=wb['قاعدة البيانات']
def note(kk,t):
    g[kk-1]['d']=(g[kk-1]['d']+' '+TAG+t).strip(); ws.cell(kk+1,21).value=((ws.cell(kk+1,21).value or '')+' '+TAG+t).strip()
nrm=lambda u:re.sub(r'^https?://(www\.|[a-z]{2}\.)?','',u).rstrip('/').lower()
LIDX=collections.defaultdict(set)
for kk,r in enumerate(g,1):
    for _,u in r['links']: LIDX[nrm(u)].add(kk)
def rec_of(x):
    c=collections.Counter()
    for l in x.get('links',[]):
        for kk in LIDX.get(nrm(l['url']),()): c[kk]+=1
    for m in re.findall(r'https?://[^\s·)،]+',x.get('provenance','')):
        for kk in LIDX.get(nrm(m.rstrip('.')),()): c[kk]+=1
    if c: return c.most_common(1)[0][0]
    nm=x['name'].strip(); hits=[kk for kk,r in enumerate(g,1) if r['n'].strip()==nm]
    return hits[0] if len(hits)==1 else None
# ---------------- 1. removals under v2.0 ----------------
RM={
 'shroaq-allwiahaq':'FAIL_TIMING — التوظيف بعد 14 شهرًا من الإتمام (> 12)',
 'rawabi-allihyani':'FAIL_TIMING — التوظيف بعد 13 شهرًا من الإتمام (> 12)؛ كانت استثناء تخويل (gap)',
 'etab-alotaibi':'FAIL_TIMING — التوظيف بعد 14 شهرًا من الإتمام الثاني (> 12)',
 'rand-alsaleh':'FAIL_TIMING — بالقراءة الصارمة لإتمام سنوي (يناير 2024) يقع التوظيف (فبراير 2025) بعد 13 شهرًا',
 'randa-almohammadi':'FAIL_TIMING — التوظيف في الشهر الرابع عشر بعد الإتمام (> 12)',
 'wejdan-mangl':'FAIL_TIMING — التوظيف بعد 13 شهرًا من الإتمام (> 12)',
 'layan-alorayyidh':'FAIL_TIMING — التوظيف بعد 14 شهرًا من الإتمام (> 12)',
 'ruqaiah-tehaifah':'FAIL_TIMING — التوظيف بعد 13 شهرًا من الإتمام (> 12)',
 'hassan-alshanqiti':'FAIL_TIMING — الإتمام الربع الأول 2024 والتوظيف أبريل 2025 (13 شهرًا على الأقل من مارس 2024)',
 'rayan-alsuwat':'FAIL_TIMING — بالقراءة الصارمة لإتمام سنوي (يناير 2025) يقع التوظيف (فبراير 2026) بعد 13 شهرًا',
 'meshal-alamr':'FAIL_OUTCOME_TYPE — النتيجة مستودع مفتوح المصدر لا توظيف/ترقية/تأسيس',
 'fares-altoukhi':'FAIL_OUTCOME_TYPE — النتيجة نماذج مفتوحة المصدر لا توظيف/ترقية/تأسيس',
 'mohammed-almalki':'FAIL_OUTCOME_TYPE — النتيجة مشروع تخرج منشور لا توظيف/ترقية/تأسيس',
 'alanoud-alotaibi':'FAIL_OUTCOME_TYPE — النتيجة موقع منشور لا توظيف/ترقية/تأسيس',
 'lena-alenazi':'FAIL_OUTCOME_TYPE — النتيجة جائزة مشروع لا توظيف/ترقية/تأسيس',
 'maysam-almalah':'FAIL_OUTCOME_TYPE — النتيجة مركز في مسابقة لا توظيف/ترقية/تأسيس',
 'rayah-aldawsari':'FAIL_OUTCOME_TYPE — النتيجة مركز في مسابقة لا توظيف/ترقية/تأسيس',
 'shahad-altamimi':'FAIL_OUTCOME_TYPE — النتيجة ورقة بحثية/درجة مسابقة؛ والتوظيف في شهر الإتمام نفسه (متزامن)',
 'hassn-alqaeri':'FAIL_OUTCOME_TYPE — النتيجة جائزة بحثية؛ والتوظيف (أبريل 2025) بعد 16 شهرًا من برنامج الأكاديمية (ديسمبر 2023)',
 'hoor-alshihi':'FAIL_OUTCOME_TYPE — النتيجة مركز في مسابقة؛ والتوظيف في SITE غير مؤرخ',
 'hind-aljuaid':'FAIL_OUTCOME_TYPE — النتائج اعتماد وجوائز؛ والدور في سدايا غير مؤرخ بعد الإتمام',
 'rana-alharsan':'FAIL_OUTCOME_TYPE — النتيجة مشروع مميز؛ والتوظيف في فضاء أجا غير مؤرخ',
 'rana-alshehri':'FAIL_OUTCOME_TYPE — النتيجة اعتماد ومشروع؛ والتوظيف في كاكست سابق للإتمام (يناير 2026)',
}
removed=[x for x in ST if x['id'] in RM]; assert len(removed)==len(RM),len(removed)
ST=[x for x in ST if x['id'] not in RM]
LOG=collections.Counter(); rmrec={}
for x in removed:
    kk=rec_of(x); rmrec[x['id']]=kk
    if kk: note(kk,'أُزيلت قصة «%s» من المنشور عند تطبيق السياسة v2.0 (12 شهرًا؛ توظيف أو ترقية أو تأسيس): %s. القصة مؤرشفة في SuccessStories/audit/.'%(x['id'],RM[x['id']])); LOG['rm_note']+=1
# ---------------- 2. converted stories ----------------
S={x['id']:x for x in ST}
nj=S['nujud-senan']; nj.update(role='مديرة مشروع (Project Manager)',org='وزارة الاتصالات وتقنية المعلومات')
nj['impact']='التحقت بوزارة الاتصالات وتقنية المعلومات مديرةَ مشروع بدوام كامل في مايو 2025 — بعد سبعة أشهر من إتمام المعسكر — بعد فوز مشروعها بجائزة قمة الابتكار الكمّي في دبي.'
nj['achievements']=['مديرة مشروع — وزارة الاتصالات وتقنية المعلومات، بدوام كامل منذ مايو 2025 (+7 أشهر)']+[a for a in nj['achievements'] if 'وزارة الاتصالات' not in a]
nj['story']=nj['story'].rstrip()+' والنتيجة المحتسبة وفق السياسة v2.0 هي التحاقها بوزارة الاتصالات وتقنية المعلومات مديرةَ مشروع بدوام كامل (مايو 2025، بعد سبعة أشهر من الإتمام).'
if os.path.exists(W+'assets/mcit.png'): nj['orgLogo']='assets/mcit.png'
else: nj.pop('orgLogo',None)
rq=S['raghad-alqobali']; rq['achievements']=['باحثة ومهندسة ذكاء اصطناعي — سدايا، بانتساب مطبوع في ورقة Sensors (أكتوبر 2024، خلال 10 أشهر من الإتمام)']+rq['achievements']
# ---------------- 3. five rulings (Prof. Mamdouh, 30 Oct 2026) ----------------
RUL='بحكم أ. د. ممدوح العنزي (30 أكتوبر 2026)'; POL='وفق السياسة v2.0 (معيار 12 شهرًا)'
NEWS=[
 dict(k=2228,id='raghad-alarifi',year=2021,role='محللة أعمال لعمليات المبيعات (Business Analyst — Sales Operations)',org='روشن (ROSHN)',logo=None,cat='employment',gender='f',
  q='من معسكر علوم البيانات في سدايا إلى تحليل الأعمال في روشن.',qe='From SDAIA’s data science bootcamp to business analysis at ROSHN.',
  impact='التحقت بروشن محللةَ أعمال لعمليات المبيعات في فبراير 2022 — بعد ثلاثة أشهر من إتمام المعسكر.',
  story='أتمّت رغد معسكر T5 لعلوم البيانات في أكاديمية سدايا ضمن فصل C04 (سبتمبر – نوفمبر 2021). وفي فبراير 2022 التحقت بروشن محللةَ أعمال لعمليات المبيعات، ثم انتقلت إلى جهة حكومية أخصائيةً للأمن السيبراني فمحللةَ أعمال تقنية (نوفمبر 2022 – الآن). يُعدّ الدور مرتبطًا بالتدريب '+RUL+'، '+POL+'.',
  ach=['محللة أعمال لعمليات المبيعات — روشن، فبراير – مايو 2022 (+3 أشهر)','محللة أعمال تقنية — جهة حكومية، نوفمبر 2022 – الآن','إتمام معسكر T5 لعلوم البيانات — فصل C04 (نوفمبر 2021)'],
  exp='Business Analyst for Sales Operation، ROSHN، دوام كامل: فبراير – مايو 2022 · Cyber Security Specialist ثم Junior IT Business Analyst، Confidential Government: مايو 2022 – الآن · Data Science Bootcamp Trainee، SDAIA Academy: سبتمبر – نوفمبر 2021'),
 dict(k=38,id='elham-alzahrani',year=2022,role='محللة أعمال تقنية (IT Business Analyst)',org='هيئة الزكاة والضريبة والجمارك (ZATCA)',logo='assets/zatca.png',cat='employment',gender='f',
  q='معسكر علوم البيانات في سدايا قادني إلى تحليل الأعمال التقنية في هيئة الزكاة.',qe='SDAIA’s data science bootcamp led me to IT business analysis at ZATCA.',
  impact='التحقت بهيئة الزكاة والضريبة والجمارك محللةَ أعمال تقنية بدوام كامل في يناير 2023 — بعد اثني عشر شهرًا من إتمام المعسكر.',
  story='أتمّت إلهام معسكر T5 لعلوم البيانات في أكاديمية سدايا (نوفمبر 2021 – يناير 2022)، ومن مشاريعها كشف إشارات المرور بالشبكات الالتفافية على مجموعة GTSRB. وفي يناير 2023 التحقت بهيئة الزكاة والضريبة والجمارك محللةَ أعمال تقنية بدوام كامل. يُعدّ الدور مرتبطًا بالتدريب '+RUL+'، '+POL+'.',
  ach=['محللة أعمال تقنية — هيئة الزكاة والضريبة والجمارك، يناير 2023 (+12 شهرًا)','إتمام معسكر T5 لعلوم البيانات (يناير 2022)','مشروع كشف إشارات المرور بشبكات CNN (أكثر من 50,000 صورة)'],
  exp='IT Business Analyst، Zakat, Tax and Customs Authority، دوام كامل: يناير 2023 – الآن · Junior Data Scientist، SDAIA (تدريب): أكتوبر 2021 – يناير 2022'),
 dict(k=2226,id='fatima-alsaeed',year=2021,role='مهندسة برمجيات (Software Engineer II)',org='شركة TAM للتطوير',logo='assets/tam.png',cat='employment',gender='f',
  q='من معسكر علوم البيانات في سدايا إلى هندسة البرمجيات ثم الذكاء الاصطناعي.',qe='From SDAIA’s data science bootcamp to software engineering, then AI.',
  impact='التحقت بشركة تام مهندسةَ برمجيات في أبريل 2022 — بعد خمسة أشهر من إتمام المعسكر — وصولًا إلى مهندسة ذكاء اصطناعي في «عمق».',
  story='أتمّت فاطمة معسكر T5 لعلوم البيانات في أكاديمية سدايا ضمن فصل C04 (سبتمبر – نوفمبر 2021). وفي أبريل 2022 التحقت بشركة تام مهندسةَ برمجيات، ثم ترقّت إلى مهندسة برمجيات أولى (يناير 2024)، وانتقلت في مايو 2025 إلى «عمق» (DEEP.SA) مهندسةً للذكاء الاصطناعي. يُعدّ الدور مرتبطًا بالتدريب '+RUL+'، '+POL+'.',
  ach=['مهندسة برمجيات — تام، أبريل 2022 (+5 أشهر)','مهندسة برمجيات أولى — تام، يناير 2024','AI Staff Engineer — عمق (DEEP.SA)، مايو 2025'],
  exp='Software Engineer II، TAM، دوام كامل: أبريل 2022 – يناير 2024 · Senior Software Engineer: يناير 2024 – يناير 2025 · Ai Staff Engineer، DEEP.SA: مايو 2025 – الآن'),
 dict(k=3950,id='mohammad-alown',year=2026,role='مهندس أتمتة (Automation Engineer)',org='هواوي (Huawei)',logo=None,cat='employment',gender='m',
  q='بعد برنامج رؤية الحاسب في سدايا انتقلت إلى هندسة الأتمتة في هواوي.',qe='After SDAIA’s computer vision programme I moved into automation engineering at Huawei.',
  impact='انتقل إلى دور مهندس أتمتة في هواوي في سبتمبر 2026 — بعد نحو خمسة أشهر من إتمام البرنامج.',
  story='أتمّ محمد برنامج رؤية الحاسب للمطورين في أكاديمية سدايا (نحو أبريل 2026)، واكتسب فيه خبرة عملية في معالجة الصور واكتشاف الأجسام. وكان قد التحق بهواوي أخصائيًا في هندسة البرمجيات في يناير 2026، ثم انتقل في سبتمبر 2026 إلى دور مهندس أتمتة منتدبًا لدى «سلام» لبناء حلول أتمتة لعمليات الشبكات. يُعدّ الدور مرتبطًا بالتدريب '+RUL+'، '+POL+'.',
  ach=['مهندس أتمتة — هواوي (منتدب لدى سلام)، سبتمبر 2026 (+~5 أشهر)','أخصائي هندسة برمجيات — هواوي، يناير – أغسطس 2026','إتمام برنامج رؤية الحاسب للمطورين — أكاديمية سدايا (~أبريل 2026)'],
  exp='Automation Engineer، Huawei، دوام كامل: سبتمبر 2026 – الآن · Software Engineering Specialist، Huawei: يناير – أغسطس 2026'),
 dict(k=2032,id='wael-almutairi',year=2026,role='المؤسس والرئيس التنفيذي (Founder & CEO)',org='إكسيكرا (Execra)',logo=None,cat='founder',gender='m',
  q='بعد برنامج رفع الإنتاجية في سدايا أسّست شركة لحلول الذكاء الاصطناعي.',qe='After SDAIA’s productivity programme I founded an AI solutions company.',
  impact='أسّس شركة Execra لحلول الذكاء الاصطناعي وتولّى رئاستها التنفيذية في مايو 2026 — بعد شهر من إتمام البرنامج.',
  story='أتمّ وائل برنامج رفع الإنتاجية وتحسين العمليات في أكاديمية سدايا (أبريل 2026)، ثم برنامج بناء أنظمة وكلاء الذكاء الاصطناعي (نحو يوليو 2026) الذي يوثّقه مستودعه building-agentic-ai-systems. وفي مايو 2026 أسّس شركة Execra لحلول الذكاء الاصطناعي في الرياض وتولّى رئاستها التنفيذية، وقاد الشراكات في جمعية الذكاء الاصطناعي (يونيو – سبتمبر 2026). يُعتمد التأسيس نتيجةً '+RUL+'، '+POL+'.',
  ach=['المؤسس والرئيس التنفيذي — Execra، مايو 2026 (+1 شهر)','قائد الشراكات والرعايات — جمعية الذكاء الاصطناعي، يونيو – سبتمبر 2026','برنامجان بالأكاديمية: رفع الإنتاجية (أبريل 2026) وبناء أنظمة وكلاء الذكاء الاصطناعي (~يوليو 2026)'],
  exp='Chief Executive Officer، Execra: مايو 2026 – الآن · Partnerships and Sponsors Leader، AI Association: يونيو – سبتمبر 2026'),
]
for p in NEWS:
    assert p['id'] not in S
    G=g[p['k']-1]; li=[l[1] for l in G['links'] if 'linkedin.com/in/' in l[1]]; assert li,p['id']
    st={"id":p['id'],"year":p['year'],"quote":{"text":p['q'],"textEn":p['qe'],"kind":"verified"},"name":G['n'],"nameEn":G.get('en') or '',"photo":None,"role":p['role'],"org":p['org']}
    if p['logo']: assert os.path.exists(W+p['logo']); st['orgLogo']=p['logo']
    st.update({"program":G['prog'],"period":G['co'],"category":p['cat'],"categories":[p['cat']],"impact":p['impact'],"story":p['story'],"achievements":p['ach'],"links":[{"label":"LinkedIn","url":li[0]}],
       "provenance":f"صفحة الخبرة على LinkedIn بحساب مسجَّل (قُرئت 30 أكتوبر 2026)، بتواريخ بمستوى الشهر: {p['exp']} + سجل الأكاديمية #{p['k']}. {POL}؛ {RUL}."})
    ST.append(st)
    if 'job' not in G['cats']: G['cats'].append('job')
    G['emp']=p['org']; G['role']=p['role']; ws.cell(p['k']+1,7).value=p['org']; ws.cell(p['k']+1,8).value=p['role']
    note(p['k'],'نُشرت قصة نجاح «%s» %s، %s: %s'%(p['id'],RUL,POL,p['ach'][0])); LOG['new_story']+=1
note(310,'حكم أ. د. ممدوح العنزي (30 أكتوبر 2026): لا تُنسب الترقية الأكاديمية (أستاذ مشارك، أغسطس 2026) إلى برنامج بناء أنظمة الذكاء الاصطناعي التوكيلي — لا قصة.')
# ---------------- 4. categories ----------------
PROMO={'wadha-almattar','jinan-alghutaymil','yazeed-alobaidan'}
for x in ST:
    if x['id']=='wael-almutairi': cat='founder'
    elif x['id'] in PROMO: cat='promotion'
    else: cat='employment'
    cats=[cat]
    if cat=='employment' and re.search(r'ترق[ّيت]|ترقية|رُقّي',x['impact']+' '.join(x['achievements'])): cats.append('promotion')
    x['category']=cat; x['categories']=cats
# ---------------- 5. text: 14 -> 12 months, v1.0 -> v2.0 ----------------
TR=[('نافذة الأربعة عشر شهرًا','نافذة الاثني عشر شهرًا'),('معيار الأربعة عشر شهرًا','معيار الاثني عشر شهرًا'),('معيار 14 شهرًا','معيار 12 شهرًا'),
    ('ضمن 14 شهرًا','ضمن 12 شهرًا'),('داخل 14 شهرًا','داخل 12 شهرًا'),('السياسة v1.0','السياسة v2.0'),('Policy v1.0','Policy v2.0'),('14-month','12-month'),('14 months','12 months')]
def fix(v):
    if isinstance(v,str):
        for a,b in TR: v=v.replace(a,b)
        return v
    if isinstance(v,list): return [fix(t) for t in v]
    if isinstance(v,dict): return {kk:fix(t) for kk,t in v.items()}
    return v
for n,x in enumerate(ST): ST[n]=fix(x)
left=[(x['id'],m.group(0)) for x in ST for m in re.finditer(r'.{40}(أربعة عشر|14 شهر|الرابع عشر).{20}',json.dumps(x,ensure_ascii=False))]
# ---------------- 6. quotes: all approved, <= 97 chars ----------------
QE={'noura-alfouzan':'After the Advanced Tracks I trained 100+ learners, then became a senior data analyst at SWA.',
 'osama-alfawzan':'From outside the field into the ML bootcamp; within a year I was a database officer at SDAIA.',
 'majd-alziyadi':'My ServiceNow bootcamp CAD and CSA certifications opened the door to app development at IBM.',
 'amal-almuarik':'SDAIA Academy’s Data Engineering Bootcamp … strengthened my professional readiness to work in AI',
 'najd-alqahtani':'One month after T5 I was a data analyst; four years on, a senior analyst at a government entity.',
 'rana-alturki':'T5 gave me the language of data: from business analyst to senior solutions engineer.',
 'ohoud-albabtain':'Two months after T5, I became a project manager at the National Information Center.',
 'anas-almana':'It helped me move quickly into the job market … working at SDAIA, promoted to senior AI engineer',
 'tasneem-alrajih':'Two Academy programs in a row built my readiness; three months on I joined SDAIA as a developer.',
 'sultan-alsubaie':'Three months after the data governance program, I became a GRC analyst at resilience.',
 'hanan-aljaid':'SDAIA Academy’s Data Engineering Bootcamp was a key step in building my technical skills',
 'aljohara-alhogail':'SDAIA Academy’s AI Agents program deepened my grasp of intelligent automation applications',
 'dhiyaa-alsalem':'I left T5 with a computer vision project, and my co-op became a data scientist role at Wakeb.',
 'noura-aldawsari':'The Zeham bootcamp opened the door to data science at Tawuniya, then a senior specialist role.',
 'maram-alshehri-zeham':'The vision models I built in the Zeham bootcamp now underpin my work as an ML engineer.',
 'munirah-alhazzani':'I safeguard data integrity in a national government resources system, on a foundation from T5.',
 'mazen-alkhodairi':'The Advanced AI Tracks led me to an AI engineering internship at SAMI, then a permanent role.',
 'joud-alghamdi':'A month after the LLM Practitioner bootcamp I became an AI engineer, and I’m still on that path.',
 'khaled-almutairy':'A month after two NVIDIA certifications, I moved from project management to AI research at Elm.',
 'rayan-dahlawi':'Five months after the LLM Practitioner certificate, I became a data scientist at ALJ Finance.',
 'meead-alshaibani':'From SDAIA x NVIDIA LLM training to AI engineer at the Real Estate Development Fund in 4 months.',
 'abdullah-alowayyid':'Combining ML and data management at SDAIA Academy led me to data analysis at Arab National Bank.',
 'faisal-alharbi':'I turned what I learned in T5 into daily work as a recruitment data analyst at ANB.',
 'sultan-almgablh':'The data management bootcamp led me to a specialist role at the National Palms and Dates Center.',
 'fatimah-alsoger':'The ML bootcamp was my turning point; within six months I was a data analyst at Lean.',
 'amal-alsulami':'I started T5 data science in 2021; a year later I was an AI developer at TAHAKOM.',
 'yazeed-alobaidan':'After SDAIA x NVIDIA training I was promoted to assistant manager, data and AI, at Bank Aljazira.',
 'ritaj-almutairi':'From computer vision in the crowd-management bootcamp to health-insurance analytics in 2 months.'}
QA={'lama-alzahrani':'عززت مهاراتي في الذكاء الاصطناعي وأسهمت في توظيف المعرفة التقنية بفاعلية أكبر في عملي الهندسي',
 'mazen-alkhodairi':'قادني برنامج المسارات المتقدمة إلى تدريب في هندسة الذكاء الاصطناعي بشركة SAMI، ثم وظيفة دائمة.',
 'meshal-aldalbahi':'معسكر إدارة الحشود قادني إلى تحليل البيانات في هيئة البحث والتطوير، ثم هندسة الذكاء الاصطناعي.',
 'majid-almadani':'قدت فريق سُم في T5، وبعد عام صرت أخصائيًا أول للتحليلات المتقدمة في البنك السعودي للاستثمار.',
 'yazeed-alobaidan':'بعد برنامج سدايا وNVIDIA ترقّيت مديرًا مساعدًا لتحليلات البيانات والذكاء الاصطناعي ببنك الجزيرة.'}
for x in ST:
    q=x['quote']
    if x['id'] in QE:
        if q.get('kind')=='verified' and 'originalEn' not in q and q['textEn']!=QE[x['id']]: q['originalEn']=q['textEn']
        q['textEn']=QE[x['id']]; LOG['q_en']+=1
    if x['id'] in QA:
        if q.get('kind')=='verified' and 'original' not in q: q['original']=q['text']
        q['text']=QA[x['id']]; LOG['q_ar']+=1
    if q.get('kind')!='verified': q['kind']='verified'; q.setdefault('source','اعتماد أ. د. ممدوح العنزي لجميع الاقتباسات (30 أكتوبر 2026)'); LOG['q_approved']+=1
    assert len(q['text'])<=97 and len(q['textEn'])<=97,(x['id'],len(q['text']),len(q['textEn']))
# ---------------- 7. placeholder photos ----------------
GEN={'reem-albalawi':'f','najd-alqahtani':'f','jennan-sowayan':'f','joud-alghamdi':'f','maria-a-alghamdi':'f','lamia-alasmari':'f','dona-alsalhi':'f','nada-rambu':'f','alaa-aljadani':'f','jinan-alghutaymil':'f','raghad-alarifi':'f','elham-alzahrani':'f','fatima-alsaeed':'f',
     'jehad-aljazi':'m','sultan-alsubaie':'m','faisal-almufarrih':'m','ali-altamimi':'m','saud-alballaa':'m','mohammad-alown':'m','wael-almutairi':'m'}
noph=[x['id'] for x in ST if not x.get('photo')]
miss=[i for i in noph if i not in GEN]; assert not miss,miss
for x in ST:
    if not x.get('photo'): x['photo']='assets/placeholder-%s.jpg'%('female' if GEN[x['id']]=='f' else 'male'); x['photoPlaceholder']=True; LOG['ph']+=1
# ---------------- 8. ordering & checks ----------------
for x in ST: assert '**' not in json.dumps(x,ensure_ascii=False)
S1=len(ST); E1=emp_count(ST)
print('stories',S0,'->',S1,'employers',E0,'->',E1,dict(LOG),'rm recs',{k:v for k,v in rmrec.items()})
print('leftover 14-month text',left)
print('cats',collections.Counter(x['category'] for x in ST))
if DRY: sys.exit(0)
os.makedirs(BK,exist_ok=True)
for f in FILES: shutil.copy2(H+f,BK+f.replace('/','__'))
for nm in ('male','female'): assert os.path.exists(W+'assets/placeholder-%s.jpg'%nm)
# archive
os.makedirs(H+'SuccessStories/audit',exist_ok=True)
json.dump([dict(x,removedReason=RM[x['id']],record=rmrec[x['id']]) for x in removed],open(H+'SuccessStories/audit/removed_stories_policy_v2_2026-10-30.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
# ---------------- 9. write data.js ----------------
sj2=sj[:k]+'const STORIES = [\n'+',\n'.join('  '+json.dumps(x,ensure_ascii=False) for x in ST)+sj[e:]
sj2=rep(sj2,"{ value: %d,  label: 'قصة نجاح موثّقة', note: 'مستوفية معيار الأربعة عشر شهرًا — مرتبة حسب سنة التخرج',"%S0,"{ value: %d,  label: 'قصة نجاح موثّقة', note: 'مستوفية معيار الاثني عشر شهرًا (السياسة v2.0) — مرتبة حسب سنة التخرج',"%S1,1)
sj2=rep(sj2,"noteEn: 'Meeting the 14-month criterion — by graduation year'","noteEn: 'Meeting the 12-month criterion (Policy v2.0) — by graduation year'",1)
sj2=re.sub(r"(\{ value: )%d(,\s+label: 'جهة عمل')"%E0,r"\g<1>%d\2"%E1,sj2,count=1)
a=sj2.index('const CATEGORIES = ['); b=sj2.index('];',a)+2
sj2=sj2[:a]+"""const CATEGORIES = [
  { id: 'all',        label: 'الكل',                    labelEn: 'All' },
  { id: 'employment', label: 'التوظيف',                 labelEn: 'Employment' },
  { id: 'promotion',  label: 'الترقية',                 labelEn: 'Promotion' },
  { id: 'founder',    label: 'تأسيس شركة ناشئة',         labelEn: 'Startup founder' },
];"""+sj2[b:]
sj2=rep(sj2,"'use strict';","/* %s (ب): السياسة v2.0 لقصص النجاح بقرار أ. د. ممدوح العنزي — نافذة 12 شهرًا، ونتيجة توظيف أو ترقية أو تأسيس، وارتباط البرنامج بها. إعادة تدقيق كل القصص: أُزيلت %d قصة (أرشيف SuccessStories/audit/removed_stories_policy_v2_2026-10-30.json) ونُشرت 5 قصص بأحكام 30 أكتوبر (raghad-alarifi · elham-alzahrani · fatima-alsaeed · mohammad-alown · wael-almutairi) — القصص %d ← %d، جهات العمل %d ← %d. اعتماد جميع الاقتباسات (≤97 حرفًا)، وصور بديلة للقصص بلا صورة، وتكبير شعارات جهات العمل. */\n'use strict';"%(DATE,len(removed),S0,S1,E0,E1),1)
open(dj,'w',encoding='utf-8').write(sj2)
# CSS: bigger logos
c=open(W+'css/style.css',encoding='utf-8').read()
c=rep(c,'.card-org img { height: 22px; width: auto; max-width: 88px;','.card-org img { height: 34px; width: auto; max-width: 140px;',1)
c=rep(c,'.m-org img { height: 30px; width: auto; max-width: 120px;','.m-org img { height: 46px; width: auto; max-width: 190px;',1)
open(W+'css/style.css','w',encoding='utf-8').write(c)
# ---------------- 10. counters & wording across pages ----------------
VA_old='30 أكتوبر 2026 (منشورات مزوّدة ومسح 2021 – أغسطس 2026 والتدقيق'; VA_new='30 أكتوبر 2026 (السياسة v2.0 لقصص النجاح — معيار 12 شهرًا — والتدقيق'
VE_old='30 October 2026 (supplied posts + 2021 – Aug 2026 sweep and QA round'; VE_new='30 October 2026 (success-story Policy v2.0 — 12-month criterion — and QA round'
def counts(t):
    for a_,b_ in (('%d قصة'%S0,'%d قصة'%S1),('%d stories'%S0,'%d stories'%S1),('%d verified success stories'%S0,'%d verified success stories'%S1),
                  ('%d جهة عمل'%E0,'%d جهة عمل'%E1),('%d employers'%E0,'%d employers'%E1),(VA_old,VA_new),(VE_old,VE_new),
                  ('معيار الأربعة عشر شهرًا','معيار الاثني عشر شهرًا'),('14-month criterion','12-month criterion')):
        t=t.replace(a_,b_)
    return t
tail=counts(tail); head=counts(head)
tail=re.sub(r"(\{ value: )%d(,\s+label: 'قصة نجاح)"%S0,r"\g<1>%d\2"%S1,tail,count=1)
head=rep(head,'داخل نافذة الأربعة عشر شهرًا بتاريخ شهري موثّق','داخل نافذة الاثني عشر شهرًا بتاريخ شهري موثّق',1)
# showcase card: rana-alharsan (removed) -> ali-altamimi
a=head.index('<h3>رنا الحرصان</h3>'); a=head.rfind('<div class="sd-card story-card ar">',0,a); b=head.index('<div class="sd-card story-card ar">',a+10)
head=head[:a]+'''<div class="sd-card story-card ar">
          <div class="story-badges"><span class="sd-tag sd-tag--accent">توظيف خلال 4 أشهر</span></div>
          <div class="story-name"><h3>علي التميمي</h3><div class="en">Ali Al-Tamimi</div></div>
          <div class="story-role">مهندس بيانات مشارك — القدية (Qiddiya)</div>
          <p class="story-txt">خريج معسكر T5 لعلوم البيانات (فصل C06، ديسمبر 2021). التحق بالقدية مهندسَ بيانات مشاركًا في أبريل 2022، ثم ترقّى إلى مهندس بيانات أول فأخصائي أول في علوم البيانات.</p>
          <div class="story-links"><a class="sd-link-pill" href="https://www.linkedin.com/in/ali-al-tamimi/" target="_blank" rel="noopener">LinkedIn</a></div>
        </div>
        '''+head[b:]
D['grads']=g; open(P_,'w',encoding='utf-8').write(head+json.dumps(D,ensure_ascii=False)+';'+tail)
P2=H+'index.html'; t=counts(open(P2,encoding='utf-8').read())
t=rep(t,'data-count="%d"'%S0,'data-count="%d"'%S1,1); t=rep(t,'data-count="%d"'%E0,'data-count="%d"'%E1,1)
t=rep(t,'data-en="204 verified graduate success stories meeting the 12-month criterion, across 109 government','data-en="%d verified graduate success stories meeting the 12-month criterion, across %d government'%(S1,E1),1)
t=rep(t,'href="SuccessStories/SDAIA_Success_Story_Policy_2026-08-30.md" data-ar="سياسة اعتماد قصص النجاح — الإصدار 1.0 (30 أغسطس)" data-en="Success-story adoption policy — v1.0 (30 Aug)"',
        'href="SuccessStories/SDAIA_Success_Story_Policy_v2_2026-10-30.md" data-ar="سياسة اعتماد قصص النجاح — الإصدار 2.0 (30 أكتوبر)" data-en="Success-story adoption policy — v2.0 (30 Oct)"',1)
t=t.replace('data-ar="تقرير تدقيق القصص — معيار الاثني عشر شهرًا (21 أغسطس)" data-en="Story audit — the 12-month criterion (21 Aug)"','data-ar="تقرير تدقيق القصص — معيار الأربعة عشر شهرًا (21 أغسطس، تاريخي)" data-en="Story audit — the 14-month criterion (21 Aug, historical)"')
t=t.replace('data-ar="# تدقيق معيار الاثني عشر شهرًا — تقرير + أرشيف المستبعدين" data-en="# 12-month-criterion audit — report + excluded-story archive"','data-ar="# تدقيقات المعيار — تقارير + أرشيف القصص المستبعدة (آخرها السياسة v2.0)" data-en="# criterion audits — reports + excluded-story archives (latest: Policy v2.0)"')
open(P2,'w',encoding='utf-8').write(t)
P4=W+'index.html'; t=counts(open(P4,encoding='utf-8').read()); t=rep(t,'"numberOfItems": %d'%S0,'"numberOfItems": %d'%S1,1)
t=rep(t,'من قاعات التدريب إلى مواقع العمل والقيادة والبحث في قلب المنظومة الوطنية','من قاعات التدريب إلى التوظيف والترقية وتأسيس الشركات في قلب المنظومة الوطنية',1)
t=rep(t,'from the training room to employment, leadership and research at the heart','from the training room to employment, promotion and startup founding at the heart',1)
open(P4,'w',encoding='utf-8').write(t)
# xlsx round sheet + md
sh=wb.create_sheet('السياسة_v2_30_أكتوبر_2026'); sh.sheet_view.rightToLeft=True; sh.append(['القصة','السجل #','الإجراء','السبب'])
for x in removed: sh.append([x['id'],rmrec[x['id']],'أُزيلت (مؤرشفة)',RM[x['id']]])
for p in NEWS: sh.append([p['id'],p['k'],'نُشرت (حكم 30 أكتوبر)',p['ach'][0]])
sh.append(['nujud-senan',None,'أعيد تصنيفها توظيفًا','وزارة الاتصالات وتقنية المعلومات — مايو 2025 (+7)'])
wb.save(X_)
P5=H+'Graduates/Graduates_Database.md'; m=open(P5,encoding='utf-8').read()
m=re.sub(r'\*\*الإصدار:\*\* ',f'**الإصدار:** {DATE} (ب) — السياسة v2.0 لقصص النجاح (القصص {S1} · جهات العمل {E1}). قبله: ',m,count=1)
L=['## السياسة v2.0 لقصص النجاح — %s'%DATE,'',f'**القصص {S0} → {S1} · جهات العمل {E0} → {E1}.** بقرار أ. د. ممدوح العنزي: نافذة 12 شهرًا (بدل 14)، والنتيجة توظيف أو ترقية أو تأسيس/رئاسة تنفيذية لشركة، مع ارتباط البرنامج بها. أُزيلت {len(removed)} قصة ({sum(1 for v in RM.values() if v.startswith("FAIL_TIMING"))} لتجاوز النافذة و{sum(1 for v in RM.values() if v.startswith("FAIL_OUTCOME"))} لأن نتيجتها جائزة أو مشروع أو بحث) وأُرشفت في SuccessStories/audit/. نُشرت 5 قصص بأحكام 30 أكتوبر: '+' · '.join(p['id'] for p in NEWS)+'. أعيد تصنيف nujud-senan توظيفًا. حكم: لا تُنسب الترقية الأكاديمية للسجل #310 إلى البرنامج.','','---','']
kk=re.search(r'\n## ',m).start()+1; m=m[:kk]+'\n'.join(L)+'\n'+m[kk:]; open(P5,'w',encoding='utf-8').write(m)
print('done')
