import json,re,os,collections,shutil
from cfg import *
from enr import *
from final_list import ACCEPT
H=os.path.expanduser('~/mnt/Academy/Graduates/')
P=H+'index.html'; s=open(P,encoding='utf-8').read()
DI=s.index("const DATA = ")+len("const DATA = "); DJ=s.index("\nconst SITE_STATS")
raw=s[DI:DJ].rstrip(); assert raw.endswith(';'); D=json.loads(raw[:-1]); g=D['grads']; assert len(g)==2973,len(g)
S=json.load(open('sets.json'));PR=json.load(open('prog.json'));NW=json.load(open('newowners.json'))
new=json.load(open('new_records.json'))
TAG='[جولة 24 سبتمبر 2026] '
def add(i,txt): g[i-1]['d']=(g[i-1]['d'].rstrip()+' '+TAG+txt).strip()
def addlink(i,l,u):
    if u not in [x[1] for x in g[i-1]['links']]: g[i-1]['links'].append([l,u])
# --- Meshal override
for x in new:
    if x['_o']=='Meshal-Css':
        x.update({'co':'يوليو–سبتمبر 2024','emp':'هيئة تنمية البحث والتطوير والابتكار (RDI)','role':'محلل بيانات (مايو 2025) ← مهندس ذكاء اصطناعي، NHC Innovation (يناير 2026)','edu':'علوم الحاسب — جامعة شقراء','cats':['job','program'],'score':88,
        'd':'قيد الخبرة في LinkedIn (حساب مسجَّل): «SDAIA | سدايا · Internship» يوليو–سبتمبر 2024 مع شهادة «Crowd Management Technologies Bootcamp — SDAIA» (أغسطس 2024)، ويصف في ملفه على GitHub تدرّبه «عبر معسكرات متقدمة مثل SDAIA T5». النتيجة المؤرخة: محلل بيانات بدوام كامل في هيئة تنمية البحث والتطوير والابتكار (RDI) من مايو 2025 (+8 أشهر، داخل نافذة الأربعة عشر شهرًا) ثم مهندس ذكاء اصطناعي في NHC Innovation من يناير 2026. عتبة الهوية: الاسم الكامل على GitHub وLinkedIn المتبادلين + البرنامج + الجامعة. تنويه: الاسم العربي نقل حرفي — غير متحقق علنًا. مُرقّى إلى قصة نجاح (meshal-aldalbahi).'})
        x['links']=[['LinkedIn','https://www.linkedin.com/in/meshalaldalbahi'],['GitHub','https://github.com/Meshal-Css']]
    if x['_o'] in ('dxi7','LamisAlamrah'):
        x['d']=x['d'].replace('ينصّ صراحةً على برنامج','يسمّي في عنوانه برنامج').replace('مع الإحالة إلى حساب الأكاديمية الرسمي على GitHub (SDAIAAcademy)','(أُنشئ يوم تسليمات دفعة SDA-DSC-112 نفسها)')
base=len(g); idmap={}
for x in new:
    o=x.pop('_o'); g.append(x); idmap[o]=len(g)
# --- cross-notes
for o,ids in XNOTE.items():
    ni=idmap[o]
    for oi in ids:
        g[ni-1]['d']+=' ⚠️ تنويه مطابقة: #%d «%s» (%s) — الاسم شائع وبلا تعزيز بالبرنامج أو التاريخ أو جهة العمل، فلم يُدمج واكتُفي بالإشارة المتبادلة.'%(oi,g[oi-1]['n'],g[oi-1]['prog'][:60])
        add(oi,'⚠️ تنويه مطابقة: السجل الجديد #%d «%s» (%s) يحمل الاسم نفسه — لم يُدمج لغياب التعزيز؛ إشارة متبادلة فقط.'%(ni,g[ni-1]['n'],g[ni-1]['prog'][:60]))
# --- enrichments
for o,i in S['ENR'].items():
    k=OVR.get(o) or PR[o][0]; nm=REPO_OVR.get(o) or PR[o][1]
    addlink(i,'GitHub','https://github.com/'+o); addlink(i,'مستودع التسليم','https://github.com/%s/%s'%(o,nm))
    x=g[i-1]
    if not x.get('en'): x['en']=ACCEPT[o][0]
    txt='إثراء بدل تكرار: حساب GitHub `%s` ومستودع التسليم `%s` يطابقان هذا السجل (الاسم + البرنامج/الدفعة).'%(o,nm)
    if o not in NOPROG and not re.search(FAM.get(k,'@@'),x['prog']):
        x['prog']+=' + '+PROGS[k][0]; txt+=' أُضيف برنامج ثانٍ مسمّى في التسليم: «%s».'%PROGS[k][2]
    if o in EXTRA: txt+=' '+EXTRA[o]
    add(i,txt); x['score']=max(x['score'],80)
# --- LinkedIn adjudication corrections
x=g[2735-1]; assert x['n']=='مروة علي'
x['co']='نوفمبر 2024 (قيد الخبرة: SDAIA Advanced Pathways in AI — DL)'; x['role']='مهندسة ذكاء اصطناعي (مايو 2025)'; x['emp']='نبّه (Nabeh)'
x['cats']=sorted(set(x['cats'])|{'job'}); x['score']=max(x['score'],90)
add(2735,'صفحة الخبرة (حساب مسجَّل): «SDAIA Advanced Pathways in Artificial Intelligence program - DL» نوفمبر 2024 مع شهادة DeepLearning.AI (نوفمبر 2024)، ثم «AI Engineer — Nabeh · Full-time» من مايو 2025 (+6 أشهر). صُحّحت الدفعة من «2025» (سنة منشور الإتمام) إلى نوفمبر 2024 بالدليل المؤرخ. مُرقّاة إلى قصة نجاح (marwah-ali).')
x=g[2832-1]; assert x['n'].startswith('أفراح')
x['co']='يوليو–أكتوبر 2024 (قيد الخبرة: Zeham Management Technologies BootCamp T5)'; x['prog']=PROGS['zeham'][0]
add(2832,'صفحة الخبرة: «Zeham Managment Technologies BootCamp (T5) — SDAIA · Internship» يوليو–أكتوبر 2024؛ صُحّحت الدفعة من «2025» والبرنامج إلى معسكر T5 لتقنيات إدارة الزحام. لا وظيفة لاحقة مسجلة (CERT_ONLY).')
x=g[2750-1]; assert 'Tharaa' in x['en']
x['n']='ثراء الشريف'; x['co']='نوفمبر 2024 – مارس 2025'; x['emp']=''; x['prog']+=' + معسكر T5 لعلوم البيانات — أكاديمية سدايا (سبتمبر–نوفمبر 2023)'
add(2750,'صفحة الخبرة: معسكر هندسة البيانات (سدايا × مايكروسوفت) «Apprenticeship» نوفمبر 2024 – مارس 2025، ومعسكر T5 لعلوم البيانات سبتمبر–نوفمبر 2023 (برنامج ثانٍ). حُذفت جهة العمل «SDAIA | سدايا» لأنها قيد المعسكر نفسه لا وظيفة (§5-هـ). الاسم العربي نقل حرفي (كان الحقل العربي لاتينيًا). لا نتيجة لاحقة (CERT_ONLY).')
add(2734,'صفحة الخبرة لا تعرض أي وظيفة في سدايا (آخر قيد: تدريب دعم شبكات، وزارة التعليم، يوليو–سبتمبر 2023)؛ جهة العمل المسجلة مصدرها عنوان الملف — ثقة منخفضة، ولا تُعد نتيجة مؤرخة.')
add(2714,'صفحة الخبرة: التحقت بالتنفيذي في يونيو 2024 أثناء المعسكر (مارس 2024 – فبراير 2025) ثم رُقّيت إلى «Senior Software Engineer | Application Support & CRM | ITSM» في سبتمبر 2025 — الدور دعم تطبيقات وCRM لا صلة له بعلوم البيانات (§5-و) ⇒ FAIL_RELATEDNESS.')
add(362,'صفحة الخبرة: «AI Engineer — Masdr» منذ يونيو 2024، قبل إتمام البرنامج (أغسطس 2025) ⇒ FAIL_TIMING (§5-أ)؛ لا إنجاز جديد مؤرخ داخل النافذة.')
add(303,'صفحة الخبرة: محللة أنظمة أعمال في أرامكو منذ فبراير 2022 (قبل البرنامج)؛ دور «خبيرة موضوع لاستراتيجية الحلول الرقمية والذكاء الاصطناعي» غير مؤرخ ⇒ HELD_ONE_DATUM (تاريخ بدء ذلك الدور).')
add(2700,'صفحة الخبرة: قيد التدريب التعاوني وحده (يونيو–أغسطس 2025) ولا وظيفة لاحقة ⇒ CERT_ONLY.')
add(2736,'صفحة الخبرة: «Information Technology Specialist» منذ أغسطس 2023 بلا جهة مسمّاة (قبل البرنامج) ⇒ لا نتيجة مؤهلة.')
add(2561,'صفحة الخبرة: آخر قيد تدريب دعم تطبيقات (سبتمبر 2023 – فبراير 2024) قبل البرنامج؛ لا وظيفة لاحقة ⇒ CERT_ONLY.')
cnt=collections.Counter(r['tr'] for r in g)
yrs={y:sum(1 for r in g if str(y) in (r.get('co') or '')) for y in range(2021,2027)}
none=sum(1 for r in g if not re.search(r'202[1-6]',r.get('co') or ''))
st={'total':len(g),'base':base,'new':len(new),'tracks':dict(cnt),'hi':sum(1 for r in g if r['score']>=75),'md':sum(1 for r in g if 45<=r['score']<75),'lo':sum(1 for r in g if r['score']<45),
'wl':sum(1 for r in g if r.get('links')),'uu':len({u for r in g for l,u in r.get('links',[])}),'we':sum(1 for r in g if r.get('emp')),'yrs':yrs,'none':none,'idmap':idmap}
json.dump(st,open('stats24.json','w'),ensure_ascii=False)
json.dump(g,open('grads_after.json','w'),ensure_ascii=False)
print(json.dumps({k:v for k,v in st.items() if k!='idmap'},ensure_ascii=False))
if os.environ.get('WRITE')=='1':
    s=s[:DI]+json.dumps(D,ensure_ascii=False)+";"+s[DJ:]
    open(P,'w',encoding='utf-8').write(s); print('WRITTEN')
