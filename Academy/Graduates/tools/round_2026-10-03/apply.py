# Round 3 Oct 2026 — LinkedIn post sweep (new graduates + enrichments) + story check (experience pages)
import json,re,os,shutil,sys,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import cands as C, verdicts as V
import openpyxl
H=os.path.expanduser('~/mnt/Academy/')
B='backup-2026-10-03'
def bk(p):
    a,b=os.path.splitext(p); t=f'{a}.{B}{b}'
    if not os.path.exists(t): shutil.copy2(p,t)
FILES=['SuccessStories/website/js/data.js','SuccessStories/website/index.html','index.html','Graduates/index.html','Graduates/Graduates_Database.xlsx','Graduates/Graduates_Database.md']
for f in FILES: bk(H+f)
def rep(s,a,b,count=None):
    n=s.count(a); assert n>=1,('missing',a[:90])
    if count is not None: assert n==count,(a[:90],n)
    return s.replace(a,b)
def rrep(s,pat,b,count=1):
    s2,n=re.subn(pat,b,s); assert n==count,(pat,n); return s2

DATE='3 أكتوبر 2026'
SRC='مسح منشورات LinkedIn (حساب مسجَّل) لإتمام برامج أكاديمية سدايا — 3 أكتوبر 2026'
TAG='[مسح منشورات LinkedIn — 3 أكتوبر 2026] '
STAG='[فحص القصص — 3 أكتوبر 2026] '
TL=' تنويه: الاسم العربي نقل حرفي عن الاسم اللاتيني المنشور — غير متحقق علنًا.'
TRN={'ai':'مهندس ذكاء اصطناعي — AI Engineer','ds':'عالم بيانات — Data Scientist','other':'برامج متخصصة أخرى — Other / Specialized','dmg':'إدارة وحوكمة البيانات — Data Management & Governance'}
LI=lambda s:'https://www.linkedin.com/in/'+s+'/'

# ---------------- Graduates page: load DATA
P=H+'Graduates/index.html'; s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+len('const DATA = '); j=s.index('\nconst SITE_STATS')
raw=s[i:j].rstrip(); assert raw.endswith(';'); D=json.loads(raw[:-1]); g=D['grads']; N0=len(g); assert N0==3189
head=s[:i]; tail=s[j:]

# ---------------- xlsx
X=H+'Graduates/Graduates_Database.xlsx'
wb=openpyxl.load_workbook(X); ws=wb['قاعدة البيانات']
last=ws.max_row
while ws.cell(last,1).value is None: last-=1
assert ws.cell(last,1).value==N0

# 2790 has a different LinkedIn slug -> new record, not enrichment
SAUD=C.ENR.pop(2790)
NEW=list(C.NEW)+[('سعود العجمي','Saud Alajmi','TS','saudalajmi','سبتمبر 2026 (منشور الإتمام 21 سبتمبر 2026)',0,
 '«سعيد بإتمامي دورة تحليل السلاسل الزمنية والتنبؤ (Time Series Analysis & Forecasting)، وهي أولى الدورات في مسار Data Science المقدم من مركز دايكو بالتعاون مع SDAIA Academy». العنوان المهني: Software Engineering Student at King Saud University.',
 'إشارة متبادلة غير مدموجة: #2790 «سعود العجمي» (AAASE، أغسطس 2026) يحمل رابط LinkedIn مختلفًا (saudalajmi1) — حسابان مختلفان، فلا يُدمجان.')]
new_ids=[]
for (ar,en,pk,slug,co,arv,ev,cross) in NEW:
    nid=len(g)+1; r=nid+1
    prog=C.P[pk]; tr=C.TRK[pk]
    d='منشور من الشخص نفسه على LinkedIn: '+ev+' عتبة الهوية مستوفاة بسمتين: الاسم على الملف الشخصي + منشور ذاتي يسمّي البرنامج والأكاديمية.'+(' '+cross if cross else '')+('' if arv else TL)
    score=84 if arv else 80
    vals=[nid,ar,en,prog,TRN[tr],co,None,None,None,None,'li1003',score,'ضمن النطاق','برنامج',LI(slug),None,None,None,None,None,d,None,SRC]
    for ci,v in enumerate(vals,1): ws.cell(r,ci).value=v
    g.append({"n":ar,"en":en,"lv":"li1003","score":score,"prog":prog,"co":co,"win":"ضمن النطاق","edu":"","emp":"","role":"","cats":["program"],"d":d,"links":[["LinkedIn",LI(slug)]],"src":SRC,"tr":tr})
    new_ids.append(nid)
# enrichments
NOLINK={3064}  # same profile under an older slug variant already linked
FLAG2={3026}   # second LinkedIn account
for i_,(slug,note,en) in C.ENR.items():
    r=i_+1; assert ws.cell(r,1).value==i_; G=g[i_-1]; assert G['n']==ws.cell(r,2).value,(i_,G['n'])
    txt=' '+TAG+note
    if i_ in FLAG2: txt+=' رابط LinkedIn ثانٍ (abdulelahalkhathami) إلى جانب الرابط القائم — يبدو حسابًا ثانيًا للشخص نفسه (البرنامج والشهر متطابقان).'
    if en and not G.get('en'): G['en']=en; ws.cell(r,3).value=en
    if i_ not in NOLINK:
        cur=ws.cell(r,15).value; ws.cell(r,15).value=(cur+' · ' if cur else '')+LI(slug)
        G['links']=(G.get('links') or [])+[["LinkedIn",LI(slug)]]
    G['d']=(G.get('d') or '')+txt; ws.cell(r,21).value=(ws.cell(r,21).value or '')+txt
# second programme / months from experience pages
EXTRA={1052:('شهر الإتمام من صفحة الخبرة: يناير–فبراير 2024.','يناير–فبراير 2024'),
       1238:('شهر الإتمام من صفحة الخبرة: يناير–فبراير 2024.','يناير–فبراير 2024'),
       1224:('صفحة الخبرة تُظهر «Data science & AI — SDAIA» (معسكر T5 بالتعاون مع أكاديمية طويق) يوليو–أكتوبر 2024 — برنامج ثانٍ.',None),
       2450:('صفحة الخبرة تُظهر «SDAIA T5 Data Science Bootcamp» (مارس–يونيو 2024) — برنامج ثانٍ؛ ثم AI Engineer — Confidential Government منذ أبريل 2025 (قصته المنشورة قائمة على جائزة KSAA-2026).',None)}
for i_,(note,co) in EXTRA.items():
    r=i_+1; G=g[i_-1]; assert ws.cell(r,1).value==i_
    t=' '+STAG+note
    if co: t+=f' (كانت الدفعة: «{G["co"]}»).'; G['co']=co; ws.cell(r,6).value=co
    G['d']+=t; ws.cell(r,21).value=(ws.cell(r,21).value or '')+t
# verdicts into d
for i_,why in list(V.FAIL.items())+[(k,'HOLD — قيد التحقق: '+v) for k,v in V.HOLD.items()]:
    r=i_+1; G=g[i_-1]; t=' '+STAG+'صفحة الخبرة (حساب مسجَّل): '+why
    G['d']+=t; ws.cell(r,21).value=(ws.cell(r,21).value or '')+t
# PASS -> stories
stories=[]
IDS={531:'hassan-abid',626:'noura-alghonaim',2398:'dina-bokhamseen',2475:'maha-aladwani',2495:'elaf-talal',2633:'wejdan-mangl',2638:'abdulrahman-alghofaily'}
LOGO={'Devoteam':'assets/devoteam.png','شركة علم':'assets/elm.png','صندوق الاستثمارات العامة (PIF)':'assets/pif.png','أكسنتشر':'assets/accenture.webp'}
ORGMAP={'Accenture':'أكسنتشر','علم (Elm)':'شركة علم'}
QUOTE={531:'من شهادة النماذج اللغوية الكبيرة إلى معسكر T5، بنيت في أكاديمية سدايا الأساس الذي أعمل به اليوم مستشارًا للبيانات.',
 626:'معسكر تعلم الآلة في أكاديمية سدايا كان بوابتي إلى أول دور لي مهندسةً للذكاء الاصطناعي.',
 2398:'معسكر T5 في أكاديمية سدايا نقلني مباشرة إلى العمل محللةً للبيانات والذكاء الاصطناعي في أكسنتشر.',
 2475:'من معسكر T5 في أكاديمية سدايا انتقلت إلى تحليل البيانات في صندوق الاستثمارات العامة.',
 2495:'بدأت رحلتي مهندسةً للذكاء الاصطناعي في معسكر أكاديمية سدايا، ومنه انتقلت إلى استشارات الذكاء الاصطناعي وحوكمته.',
 2633:'برنامج أبطال صيف الذكاء الاصطناعي عمّق مهاراتي في البيانات، ومنه انتقلت إلى تحليل البيانات في علم.',
 2638:'معسكر T5 في أكاديمية سدايا قادني إلى أول وظيفة عالمَ بيانات، ثم إلى هندسة الذكاء الاصطناعي.'}
TXT={
 531:('التحاق بشركة Devoteam «استشاري بيانات» بدوام كامل في نوفمبر 2024 — بعد شهر واحد من إتمام معسكر T5.',
      'نال حسن شهادة ممارس النماذج اللغوية الكبيرة (LLM Practitioner) من أكاديمية سدايا في نوفمبر 2023، وعمل بعدها محلل بيانات في مشروع مالك لدى شركة كدانة للتنمية والتطوير (أبريل–يوليو 2024)، ثم التحق بمعسكر T5 لعلوم البيانات والذكاء الاصطناعي (يوليو–أكتوبر 2024، بتنفيذ أكاديمية طويق). وفي نوفمبر 2024 — بعد شهر واحد من إتمام المعسكر — التحق بشركة Devoteam استشاريًّا للبيانات بدوام كامل، وما زال فيها. النتيجة المحتسبة هي الالتحاق بـDevoteam؛ وتقع أيضًا ضمن نافذة الأربعة عشر شهرًا من شهادة LLM Practitioner (+12 شهرًا).'),
 626:('التحاق بشركة Netways «مهندسة ذكاء اصطناعي» في ديسمبر 2023 — بعد شهر واحد من إتمام برنامجها في الأكاديمية.',
      'أتمّت نورة معسكر تعلم الآلة في أكاديمية سدايا (سبتمبر–أكتوبر 2023) ونالت شهادة ممارس تعلم الآلة (ML Practitioner) في نوفمبر 2023. وفي ديسمبر 2023 التحقت بشركة Netways مهندسةً للذكاء الاصطناعي (ديسمبر 2023 – أكتوبر 2024)، ثم انتقلت داخل الشركة إلى دور محللة أعمال بدوام كامل (أكتوبر 2024 – ديسمبر 2025). النتيجة المحتسبة هي دور مهندسة الذكاء الاصطناعي، بعد شهر واحد من الإتمام.'),
 2398:('التحاق بأكسنتشر الشرق الأوسط «محللة بيانات وذكاء اصطناعي» بدوام كامل في أبريل 2024 — بعد أربعة أشهر من إتمام معسكر T5.',
      'أتمّت دينا معسكر T5 لعلوم البيانات والذكاء الاصطناعي في أكاديمية سدايا (ديسمبر 2023). وفي أبريل 2024 التحقت بأكسنتشر الشرق الأوسط محللةً للبيانات والذكاء الاصطناعي بدوام كامل (أبريل 2024 – فبراير 2026)، وعملت على تجهيز البيانات للتحليل وسياسات حوكمة البيانات، ثم انتقلت محللة أعمال إلى شركة حمد محمد الرقيب وأولاده (أبريل 2026). النتيجة المحتسبة هي الالتحاق بأكسنتشر، بعد أربعة أشهر من الإتمام.'),
 2475:('عقد «محللة بيانات» مع صندوق الاستثمارات العامة في مارس 2022 — بعد شهرين من إتمام معسكر T5.',
      'أتمّت مها معسكر T5 لعلوم البيانات في أكاديمية سدايا (نوفمبر 2021 – يناير 2022). وفي مارس 2022 عملت محللةً للبيانات لدى صندوق الاستثمارات العامة بعقد (مارس–أبريل 2022)، ثم التحقت ببرنامج «بناء الكفاءات» لتطوير الخريجين في هيئة الزكاة والضريبة والجمارك (فبراير 2023) وتعمل فيها اليوم أخصائية أولى. النتيجة المحتسبة هي عقد تحليل البيانات مع صندوق الاستثمارات العامة، بعد شهرين من الإتمام؛ وهو عقد قصير (شهران).'),
 2495:('التحاق بشركة Devoteam «مستشارة ذكاء اصطناعي» بدوام كامل في أغسطس 2022 — بعد سبعة أشهر من إتمام معسكر T5.',
      'أتمّت إيلاف معسكر T5 لعلوم البيانات والذكاء الاصطناعي في أكاديمية سدايا (أكتوبر 2021 – يناير 2022). وفي أغسطس 2022 التحقت بشركة Devoteam مستشارةً للذكاء الاصطناعي بدوام كامل، وبقيت في الدور أربع سنوات، ثم صارت مستشارة حوكمة الذكاء الاصطناعي (يناير–سبتمبر 2026). النتيجة المحتسبة هي الالتحاق بـDevoteam، بعد سبعة أشهر من الإتمام.'),
 2633:('التحاق بشركة علم «محللة بيانات» بدوام كامل في أغسطس 2023 — بعد ثلاثة عشر شهرًا من إتمام البرنامج — ثم ترقية إلى محللة بيانات أولى (يونيو 2025).',
      'شاركت وجدان في برنامج «أبطال صيف الذكاء الاصطناعي» في أكاديمية سدايا (يوليو 2022) وهي تعمل مطوّرة ذكاء أعمال في بنده للتجزئة (مايو 2022 – أبريل 2023؛ دور سابق للإتمام لا يُحتسب). وفي أغسطس 2023 التحقت بشركة علم محللةً للبيانات بدوام كامل، ثم رُقّيت إلى محللة بيانات أولى في يونيو 2025. النتيجة المحتسبة هي الالتحاق بشركة علم، بعد ثلاثة عشر شهرًا من الإتمام — ضمن نافذة الأربعة عشر شهرًا.'),
 2638:('التحاق بشركة GeoTech «عالم بيانات» بدوام كامل في يناير 2024 — بعد شهر واحد من إتمام معسكر T5 — ثم مهندس ذكاء اصطناعي (يناير 2026).',
      'أتمّ عبدالرحمن معسكر T5 لعلوم البيانات والذكاء الاصطناعي في أكاديمية سدايا (سبتمبر–ديسمبر 2023). وفي يناير 2024 التحق بشركة GeoTech عالمَ بيانات بدوام كامل (يناير 2024 – ديسمبر 2025)، ثم صار مهندس ذكاء اصطناعي فيها منذ يناير 2026، وبنى نظامًا وكيليًّا للتقارير باستخدام LangGraph. النتيجة المحتسبة هي الالتحاق بـGeoTech، بعد شهر واحد من الإتمام.'),
}
for i_,p in V.PASS.items():
    if i_ not in IDS: continue   # 2450 already a published story
    G=g[i_-1]; org=ORGMAP.get(p['org'],p['org'])
    name=G['n'] if re.search('[؀-ۿ]',G['n']) else p['ar']
    nameEn=G.get('en') or p['en']
    impact,story_txt=TXT[i_]
    st={"id":IDS[i_],"year":p['year'],"quote":{"text":QUOTE[i_],"kind":"draft"},"name":name,"nameEn":nameEn,"photo":None,
        "role":p['role'],"org":org,"orgLogo":LOGO.get(org),"program":p['program'],"period":p['period'],
        "category":"employment","categories":["employment"],"impact":impact,"story":story_txt,
        "achievements":[p['program'],f"{p['role']} — {org} ({p['hire']})"],
        "links":[{"label":"LinkedIn","url":LI(p['slug'])}],
        "provenance":f"صفحة الخبرة على LinkedIn بحساب مسجَّل (قُرئت 3 أكتوبر 2026): {p['exp']} + سجل الأكاديمية #{i_}."}
    stories.append(st)
    t=' '+STAG+f"صفحة الخبرة (حساب مسجَّل): {p['exp']}. PASS_DATED ({p['gap']}) — مُرقّى إلى قصة نجاح «{IDS[i_]}»."
    G['d']+=t; G['emp']=org; G['role']=p['role']
    if 'job' not in G['cats']: G['cats'].append('job')
    r=i_+1; ws.cell(r,7).value=org; ws.cell(r,8).value=p['role']; ws.cell(r,21).value=(ws.cell(r,21).value or '')+t
NS=len(stories)
# ---------------- stats
N=len(g)
T=collections.Counter(r['tr'] for r in g)
wl=sum(1 for r in g if r.get('links'))
uu=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
emp=sum(1 for r in g if r.get('emp'))
hi=sum(1 for r in g if r.get('score',0)>=75); mid=sum(1 for r in g if 45<=r.get('score',0)<75); lo=N-hi-mid
yc=collections.Counter()
for r in g:
    ys=set(re.findall(r'20(2[1-6])',r.get('co') or ''))
    if not ys: yc['none']+=1
    for y in ys: yc['20'+y]+=1
S0=118; E0=73; S1=S0+NS; E1=E0+2   # new employers: Netways, GeoTech
TOT=format(N,',')
print('N',N,dict(T),'wl',wl,'uu',uu,'emp',emp,'stories',S1,'employers',E1,'years',dict(yc),'conf',hi,mid,lo)
json.dump(dict(N=N,T=T,wl=wl,uu=uu,new=new_ids,stories=[x['id'] for x in stories]),open(os.path.dirname(os.path.abspath(__file__))+'/stats.json','w'),ensure_ascii=False)

VER_AR_OLD='إصدار 2 أكتوبر 2026 (جولة إكمال الفجوات ومسح منشورات LinkedIn'
VER_AR_NEW='إصدار 3 أكتوبر 2026 (جولة مسح منشورات LinkedIn وفحص القصص'
VER_EN_OLD='version 2 October 2026 (gap-closing and LinkedIn post sweep round'
VER_EN_NEW='version 3 October 2026 (LinkedIn post sweep and story-check round'
# ---------------- Graduates page counters
for part in ('head','tail'):
    t=locals()[part]
    t=t.replace('3,189',TOT).replace(VER_AR_OLD,VER_AR_NEW).replace(VER_EN_OLD,VER_EN_NEW)
    t=t.replace('(118 قصة)','(%d قصة)'%S1).replace('(118 stories)','(%d stories)'%S1).replace('118 قصة نجاح موثّقة','%d قصة نجاح موثّقة'%S1).replace('118 verified success stories','%d verified success stories'%S1)
    t=t.replace('عبر 73 جهة عمل','عبر %d جهة عمل'%E1).replace('across 73 employers','across %d employers'%E1)
    if part=='head': head=t
    else: tail=t
tail=rep(tail,"{ value: 3189, label: 'سجلًا فرديًا',","{ value: %d, label: 'سجلًا فرديًا',"%N,1)
for k,en,old in (('ai','AI Engineer',1544),('ds','Data Scientist',872),('dmg','Data Management & Governance',326),('other','Other / Specialized',187)):
    tail=rrep(tail,r"(en: '%s', value: )%d\b"%(re.escape(en),old),"\\g<1>%d"%T[k])
tail=rrep(tail,r"\{ value: 1239,(\s+)label: 'سجلًا برابط تحقق علني', note: '2,113 رابط مصدر فريد',","{ value: %d,\\1label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(wl,format(uu,',')))
tail=rep(tail,"noteEn: '2,113 unique source links'","noteEn: '%s unique source links'"%format(uu,','),1)
tail=rrep(tail,r"\{ value: 118,(\s+)label: 'قصة نجاح موثّقة'","{ value: %d,\\1label: 'قصة نجاح موثّقة'"%S1)
D['grads']=g
open(P,'w',encoding='utf-8').write(head+json.dumps(D,ensure_ascii=False)+';'+tail)
rest=head+tail; print('grad leftovers',{k:rest.count(k) for k in ['3,189','3189','2,113','118 قصة','2 أكتوبر 2026 (جولة إكمال']})
# ---------------- portal
P=H+'index.html'; s=open(P,encoding='utf-8').read()
s=s.replace('3,189',TOT).replace(VER_AR_OLD,VER_AR_NEW).replace(VER_EN_OLD,VER_EN_NEW)
s=rep(s,'data-count="3189"','data-count="%d"'%N,1)
s=rep(s,'data-count="118"','data-count="%d"'%S1,1); s=rep(s,'data-count="73"','data-count="%d"'%E1,1)
s=s.replace('118 قصة','%d قصة'%S1).replace('118 stories','%d stories'%S1).replace('73 جهة عمل','%d جهة عمل'%E1).replace('73 employers','%d employers'%E1).replace('across 73 government','across %d government'%E1)
for k,old in (('ai',1544),('ds',872),('dmg',326),('other',187),('genai',249),('coop',11)):
    pc='%.1f'%(100*T[k]/N)
    pat=r'(data-count=")%d(">0</div>.*?--w:)[\d.]+(%%.*?data-ar=")[\d.]+(%% من السجل" data-en=")[\d.]+(%% of the registry")'%old
    s,n=re.subn(pat,lambda m:m.group(1)+str(T[k])+m.group(2)+pc+m.group(3)+pc+m.group(4)+pc+m.group(5),s,count=1,flags=re.S); assert n==1,k
open(P,'w',encoding='utf-8').write(s)
print('portal leftovers',{k:s.count(k) for k in ['3,189','3189','118 قصة','73 جهة']})
# ---------------- data.js
P=H+'SuccessStories/website/js/data.js'; s=open(P,encoding='utf-8').read()
s=rep(s,"{ value: 3189, label: 'خريجًا موثّقًا',","{ value: %d, label: 'خريجًا موثّقًا',"%N,1)
for k,en,old in (('ai','AI Engineer',1544),('ds','Data Scientist',872),('dmg','Data Management & Governance',326),('other','Other / Specialized',187)):
    s=rrep(s,r"(en: '%s',\s+value: )%d\b"%(re.escape(en),old),"\\g<1>%d"%T[k])
s=rrep(s,r"(\{ value: )118(,\s+label: 'قصة نجاح)",r"\g<1>%d\2"%S1)
s=rrep(s,r"(\{ value: )73(,\s+label: 'جهة عمل')",r"\g<1>%d\2"%E1)
k=s.index('const STORIES = ['); e=s.index('\n];',k)
s=s[:e]+'\n'+',\n'.join('  '+json.dumps(x,ensure_ascii=False) for x in stories)+','+s[e:]
s=rep(s,"'use strict';","/* %s: مسح منشورات LinkedIn وفحص القصص — 3,189 ← %s خريجًا (%d سجلًا جديدًا · %d إثراءً)؛ %d قصص جديدة من صفحات الخبرة (118 ← %d)، وجهات العمل 73 ← %d (Netways · GeoTech). */\n'use strict';"%(DATE,TOT,len(new_ids),len(C.ENR),NS,S1,E1),1)
open(P,'w',encoding='utf-8').write(s)
P=H+'SuccessStories/website/index.html'; s=open(P,encoding='utf-8').read(); s=rep(s,'"numberOfItems": 118','"numberOfItems": %d'%S1,1); open(P,'w',encoding='utf-8').write(s)
# ---------------- xlsx stats + sheet
st=wb['إحصاءات']
M={'الإجمالي':TOT,'مهندس ذكاء اصطناعي':T['ai'],'عالم بيانات':T['ds'],'أكاديمية الذكاء الاصطناعي التوليدي':T['genai'],'إدارة وحوكمة البيانات':T['dmg'],'التدريب التعاوني':T['coop'],'برامج متخصصة أخرى':T['other'],
   'ثقة مرتفعة (≥75)':hi,'ثقة متوسطة (45–74)':mid,'ثقة منخفضة (<45)':lo,'سجلات بجهة عمل موثّقة':emp,'سجلات بروابط تحقق علنية':wl,'روابط مصدر فريدة':uu,
   'سجلات بدفعة 2021':yc['2021'],'سجلات بدفعة 2022':yc['2022'],'سجلات بدفعة 2023':yc['2023'],'سجلات بدفعة 2024':yc['2024'],'سجلات بدفعة 2025':yc['2025'],'سجلات بدفعة 2026':yc['2026'],'سجلات بلا دفعة محددة':yc['none'],
   'قصص النجاح':S1,'جهات العمل':E1,
   'تحديث':f'{DATE} — مسح منشورات LinkedIn وفحص القصص: {len(new_ids)} سجلًا جديدًا (3,189 → {TOT})، {len(C.ENR)} إثراءً؛ {NS} قصص نجاح جديدة من صفحات الخبرة (118 → {S1})، وجهات العمل 73 → {E1}'}
for row in st.iter_rows():
    if row[0].value in M: row[1].value=M[row[0].value]
sh=wb.create_sheet('جولة_منشورات_وقصص_2026-10-03')
sh.append(['#','الاسم','النوع','البرنامج / الحكم','الدليل'])
for nid in new_ids: G=g[nid-1]; sh.append([nid,G['n'],'سجل جديد',G['prog'],G['links'][0][1]])
for i_ in C.ENR: sh.append([i_,g[i_-1]['n'],'إثراء','',C.ENR[i_][0]])
for x,i_ in zip(stories,[k for k in V.PASS if k in IDS]): sh.append([i_,x['name'],'قصة جديدة',x['org']+' — '+x['role'],x['links'][0]['url']])
for i_,v in V.HOLD.items(): sh.append([i_,g[i_-1]['n'],'قيد التحقق',v,''])
for i_,v in V.FAIL.items(): sh.append([i_,g[i_-1]['n'],'مرفوض',v.split(' — ')[0],''])
for sl,v in C.REFUSED.items(): sh.append(['',sl,'لم يُقبل',v,LI(sl)])
wb.save(X)
# ---------------- md
P=H+'Graduates/Graduates_Database.md'; s=open(P,encoding='utf-8').read()
s=rep(s,'**الإصدار:** 2 أكتوبر 2026 (ب) — جولة إكمال الفجوات ومسح منشورات LinkedIn (3,180 → 3,189).','**الإصدار:** %s — جولة مسح منشورات LinkedIn وفحص القصص (3,189 → %s · القصص 118 → %d · جهات العمل 73 → %d). قبله: 2 أكتوبر 2026 (ب) — جولة إكمال الفجوات ومسح منشورات LinkedIn (3,180 → 3,189).'%(DATE,TOT,S1,E1),1)
L=['## جولة مسح منشورات LinkedIn وفحص القصص — %s'%DATE,'',f'**الخريجون 3,189 → {TOT} · القصص 118 → {S1} · جهات العمل 73 → {E1}.**','',
   f'**1) سجلات جديدة ({len(new_ids)})** — من منشورات إتمام ذاتية على LinkedIn (بحث المحتوى بحساب مسجَّل، الأحدث، آخر شهر):','',
   '| # | الاسم | الاسم الإنجليزي | البرنامج | الدفعة | الرابط |','|---|---|---|---|---|---|']
for nid in new_ids:
    G=g[nid-1]; L.append(f"| {nid} | {G['n']} | {G['en']} | {G['prog']} | {G['co']} | {G['links'][0][1]} |")
L+=['',f'**2) إثراءات ({len(C.ENR)})** — روابط LinkedIn ومنشورات إتمام مطابقة: '+' · '.join('#%d'%k for k in C.ENR)+'.','',
    f'**3) قصص نجاح جديدة ({NS})** — من صفحات الخبرة (حساب مسجَّل) لـ101 سجل مؤرخ 2022–2025 لم تُفحص سابقًا:','',
    '| القصة | # | النتيجة | الفارق |','|---|---|---|---|']
for i_ in IDS:
    p=V.PASS[i_]; L.append(f"| {IDS[i_]} | {i_} | {p['role']} — {ORGMAP.get(p['org'],p['org'])} ({p['hire']}) | {p['gap']} |")
L+=['','**قيد التحقق (%d):** '%len(V.HOLD)+' · '.join('#%d'%k for k in V.HOLD)+' — التفاصيل في حقل الوصف لكل سجل.','',
    '**مرفوض/بلا نتيجة (%d):** موثّق برمز السبب في حقل الوصف.'%len(V.FAIL),'',
    '**لم يُقبل من المنشورات (%d):** '%len(C.REFUSED)+' · '.join(v for v in C.REFUSED.values())+'.','','---','']
k=s.index('## جولة إكمال الفجوات ومسح منشورات LinkedIn — 2 أكتوبر 2026 (ب)')
s=s[:k]+'\n'.join(L)+'\n'+s[k:]
open(P,'w',encoding='utf-8').write(s)
print('done',len(new_ids),'new',NS,'stories')
