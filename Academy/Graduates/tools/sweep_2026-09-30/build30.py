import json,re,os,collections,copy
from cfg24 import PROGS as P24, BASIS, SCORE, MONTHS
exec(open('accept_gh.py').read()); A1=A
exec(open('accept_gh2.py').read()); A2=A
exec(open('accept_li.py').read())
F={}
for f in ('fetched.json','fetched2.json'): F.update(json.load(open(f)))
C={}
for f in ('cand_gh.json','cand_gh2k.json'): C.update(json.load(open(f)))
D=json.load(open('data.json')); g=D['grads']; base=len(g); assert base==3085
PR={k:(v[0],v[1],v[2]) for k,v in P24.items()}
PR.update({
'ml':('معسكر تعلم الآلة (ML)','ai','SDAIA ML Bootcamp'),
'llm':('معسكر النماذج اللغوية الكبيرة (LLM)','ai','SDAIA LLM Bootcamp'),
't5':('معسكر T5 لعلوم البيانات والذكاء الاصطناعي — أكاديمية سدايا','ds','T5 Data Science & AI Bootcamp'),
'bc24':('معسكر سدايا 2024 — T5 لعلوم البيانات والذكاء الاصطناعي على الأرجح (مستنتج من مستودع «SDAIA Bootcamp»)','ds','SDAIA Bootcamp 2024 (likely T5)'),
'java':('دورة سدايا للبرمجة بلغة جافا (SDAIA Java Course)','other','SDAIA Java Course'),
'cv26':('الرؤية الحاسوبية — أكاديمية سدايا (برنامج رؤية حاسوبية سبتمبر 2026؛ رمز البرنامج غير مذكور في التسليم)','ai','Computer Vision programme (Sep 2026)'),
'creat':('معسكر الإبداع بالذكاء الاصطناعي — أكاديمية سدايا (ثلاثة أيام)','other','AI Creativity Bootcamp'),
'vibe':('البرمجة التوليدية (Vibe Coding) — أكاديمية سدايا','ai','Vibe Coding (Generative Programming)'),
'prod':('رفع الإنتاجية وتحسين العمليات — أكاديمية سدايا','other','Productivity Enhancement & Process Improvement'),
})
BASIS.update({'dn+li':'الاسم الكامل معروض على ملف GitHub الشخصي ومعه رابط LinkedIn يحمل الاسم نفسه، والبرنامج مسمّى في المستودع',
 'dn+h':'الاسم الكامل معروض على ملف GitHub الشخصي ويطابق اسم الحساب، والبرنامج مسمّى في المستودع',
 'li+repo':'رابط LinkedIn على ملف GitHub الشخصي يحمل الاسم الكامل، والاسم الأول في اسم مستودع التسليم، والبرنامج مسمّى في التسليم',
 'dn':'الاسم الكامل معروض على ملف GitHub الشخصي، والبرنامج مسمّى في المستودع'})
SCORE.update({'dn+li':76,'dn+h':72,'li+repo':74,'dn':72})
LV_G='ghsweep30'; LV_L='lisweep30'; LV_T='team30'
SRC_G='مسح GitHub لمستودعات 2024 ومستودعات تسليم سبتمبر 2026 (إشارة صريحة لأكاديمية سدايا أو برنامجها) — 30 سبتمبر 2026'
SRC_L='مسح منشورات LinkedIn (حساب مسجَّل) لإتمام برامج أكاديمية سدايا — 30 سبتمبر 2026'
SRC_T='قائمة أعضاء الفريق في README مستودع مشروع تخرج يحيل إلى حساب الأكاديمية الرسمي — 30 سبتمبر 2026'
DUP_G={'iHaneenHMD':528,'Janaalgh':1018,'devAfnan':1100,'Wajdals':1092,'manal-sa':815,'maram-a22':2723,'Noufsaleh46':177,'MaryamBuqrain':1238,'Joud-77':1224,'Haya-Almalki':180}
SECOND_PROG={'MaryamBuqrain':'advml','Joud-77':'t5'}
DUP_L={'rawanaldossari11':2862,'shrouq-alzah':3048,'layan-alhamad-3b8387230':3072,'layanalrouji':3033,'aalbujayr':3003,'raghad-alenezi---':3080,'anwar-saad-alotaibi-':2865,'emad-alaskar-6308b73a9':2042}
SECOND_L={'aalbujayr':'dsc213','raghad-alenezi---':'advml','emad-alaskar-6308b73a9':'mde'}
HOLD={'saudalajmi':'#2790'}
XN={'shuruq2':[1830],'Thew7007':[1999],'shomookhAlharbi1900':[2120],'yalmutairi72-cpu':[2992],'smqhtani-20':[1467],'saraahamd1444-spec':[695],'khaled-al-qahtani-997b2433a':[1476],'vabdull':[1591],
 ('T','نوف الجهني'):[1822],('T','خالد المطيري'):[1824]}
TEAM_SKIP={'نجد عبيد القحطاني','رغد الدوسري','عبدالوهاب الناصر'}
MERGE_LI={('SULTAN702kSA','العنود الكناني'):('alanoud-alkanani-736887323','منشورها على LinkedIn: رحلتها مع أكاديمية سدايا في برنامج Vibe Coding ومشروع «مُدار» مع شكر المرشدة حنين المعيوف'),
 ('Reema11H','هاجر عائض الشهراني'):('hajar-al-shahrani','منشورها على LinkedIn: إتمام شهادة «رفع الإنتاجية وتحسين العمليات» من أكاديمية سدايا (قبل ~18 ساعة من المسح)')}
GH_LI_MERGE={'nalrshoud0':('norah-alrshoud-811621350','منشورها على LinkedIn يؤكد إتمام «Generative AI for Productivity» من أكاديمية سدايا')}
TEAMNOTE=' عضو الفريق مسمّى نصًّا لا بوسم حساب، فلا يُرفق رابط شخصي (قاعدة زميل الفريق). يحتاج تأكيدًا من كشوف حضور الأكاديمية.'
def fmt(dt):
    y,m,d=dt[:10].split('-'); return int(d),MONTHS[int(m)-1],y
def li_of(o):
    for u in F.get(o,{}).get('li',[]):
        m=re.search(r'linkedin\.com/in/([^/?#&"]+)',u)
        if m and m.group(1) not in ('https:','http:'): return 'https://www.linkedin.com/in/'+m.group(1).rstrip('/')
def created(o,repo):
    for r in C[o]:
        if r[0]==repo: return r[1]
    return C[o][0][1]
idmap={}
def push(rec,key):
    g.append(rec); idmap[key]=len(g)
# --- GitHub new records
for A in (A1,A2):
    for o,(en,ar,k,b,repo,arv) in A.items():
        if o in DUP_G: continue
        prog,tr,pen=PR[k]
        dt=created(o,repo); d_,mo,y=fmt(dt)
        if k in ('ml','llm','t5','bc24','java','zeham'):
            co='%s %s (إنشاء مستودع المعسكر/الدورة: %d %s %s)'%(mo,y,d_,mo,y)
        else:
            co='%s %s (إنشاء مستودع التسليم: %d %s %s)'%(mo,y,d_,mo,y)
        links=[['GitHub','https://github.com/'+o],['مستودع التسليم' if y=='2026' else 'مستودع البرنامج','https://github.com/%s/%s'%(o,repo)]]
        li=li_of(o)
        if o in GH_LI_MERGE: li='https://www.linkedin.com/in/'+GH_LI_MERGE[o][0]
        if li: links.append(['LinkedIn',li])
        if o=='DAleid': links.append(['مستودع التسليم الثاني','https://github.com/DAleid/sdaia-data-engineering-capstone']); prog+=' + '+PR['mde'][0]
        what='مستودع التسليم' if y=='2026' else 'مستودع'
        d='%s `%s` (أُنشئ %d %s %s) يسمّي برنامج «%s» في أكاديمية سدايا%s. عتبة الهوية: %s.'%(what,repo,d_,mo,y,pen,' مع الإحالة إلى حساب الأكاديمية الرسمي على GitHub (SDAIAAcademy)' if y=='2026' else '',BASIS[b])
        if k=='bc24': d+=' البرنامج مستنتج: المستودع يسمّي «SDAIA Bootcamp» دون ذكر T5 صراحةً، وتوقيته (يوليو–أغسطس 2024) يطابق دفعة T5 2024.'
        if k=='java': d+=' تنويه برنامج: «دورة سدايا للجافا» (مايو–يوليو 2024) مسجّلة في القاعدة سابقًا بسجلين؛ تبعيتها للأكاديمية تستحق تأكيدًا من سجلاتها.'
        if k in ('ml','llm'): d+=' تنبيه دفعة: مستودع أُنشئ مطلع 2024 قد يؤرّخ دفعة أواخر 2023.'
        if o in GH_LI_MERGE: d+=' '+GH_LI_MERGE[o][1]+'.'
        if o=='DAleid': d+=' ولها مستودع ثانٍ لمشروع «Modern Data Engineering» (سبتمبر 2026) يسمّي أكاديمية سدايا.'
        if li and o not in GH_LI_MERGE: d+=' رابط LinkedIn منشور على ملف GitHub نفسه.'
        d+=(' الاسم العربي مكتوب بالعربية في التسليم نفسه.' if arv else ' تنويه: الاسم العربي نقل حرفي عن الاسم اللاتيني المنشور — غير متحقق علنًا.')
        sc=SCORE[b]+(9 if o in GH_LI_MERGE else 0)
        rec={'n':ar,'en':en,'lv':LV_G,'score':sc,'prog':prog,'co':co,'win':'ضمن النطاق','edu':'','emp':'','role':'','cats':['program','project'],'d':d,'links':links,'src':SRC_G+(' · '+SRC_L if o in GH_LI_MERGE else ''),'tr':tr}
        push(rec,o)
# --- teammates
for o,Lt in T.items():
    own=A2[o]; k=own[2]; prog,tr,pen=PR[k]; repo=own[4]; dt=created(o,repo); d_,mo,y=fmt(dt)
    for en,ar in Lt:
        if ar in TEAM_SKIP: continue
        rec={'n':ar,'en':en,'lv':LV_T,'score':65,'prog':prog,'co':'%s %s (إنشاء مستودع مشروع الفريق: %d %s %s)'%(mo,y,d_,mo,y),'win':'ضمن النطاق','edu':'','emp':'','role':'','cats':['program','project'],
             'd':'مسمّى/ة بالاسم في قائمة أعضاء الفريق داخل README مستودع مشروع التخرج `%s/%s` (أُنشئ %d %s %s)، الذي يسمّي برنامج «%s» ويحيل إلى حساب أكاديمية سدايا الرسمي.'%(o,repo,d_,mo,y,pen)+TEAMNOTE,
             'links':[],'src':SRC_T,'tr':tr}
        if (o,ar) in MERGE_LI:
            slug,txt=MERGE_LI[(o,ar)]
            rec['links']=[['LinkedIn','https://www.linkedin.com/in/'+slug]]; rec['score']=85; rec['lv']=LV_L
            rec['d']=rec['d'].replace(TEAMNOTE,' '+txt+' — مصدران مستقلان متطابقان (الاسم + البرنامج + الشهر)، فرُفعت الثقة وأُرفق رابطها الشخصي.')
            rec['src']=SRC_T+' · '+SRC_L
            rec['en']={'العنود الكناني':'Alanoud Alkanani','هاجر عائض الشهراني':'Hajar Alshahrani'}[ar]
        push(rec,('T',ar))
# --- LinkedIn new
AGO={'18h':'قبل ~18 ساعة','19h':'قبل ~19 ساعة','1d':'قبل يوم','2d':'قبل يومين','3d':'قبل 3 أيام','5d':'قبل 5 أيام','1w':'قبل أسبوع','2w':'قبل أسبوعين','3w':'قبل 3 أسابيع','1mo':'قبل شهر تقريبًا'}
for s,(en,ar,k,ago,ev) in L.items():
    if s in DUP_L or s in HOLD or s=='hajar-al-shahrani': continue
    prog,tr,pen=PR[k]
    co=('أغسطس–سبتمبر 2026' if ago=='1mo' else 'سبتمبر 2026')+' (منشور الإتمام %s من 30 سبتمبر 2026)'%AGO[ago]
    d='%s — منشور ذاتي من صاحب/ة الحساب على LinkedIn يسمّي البرنامج والأكاديمية. عتبة الهوية: الاسم الكامل + رابط الملف الشخصي + البرنامج المسمّى.'%ev
    d+=' تنويه: الاسم العربي نقل حرفي عن الاسم اللاتيني المنشور — غير متحقق علنًا.'
    rec={'n':ar,'en':en,'lv':LV_L,'score':85,'prog':prog,'co':co,'win':'ضمن النطاق','edu':'','emp':'','role':'','cats':['program','cert'],'d':d,'links':[['LinkedIn','https://www.linkedin.com/in/'+s]],'src':SRC_L,'tr':tr}
    push(rec,s)
push({'n':'سارة الشبيب','en':'Sarah Alshabib','lv':LV_T,'score':60,'prog':PR['cvu'][0],'co':'سبتمبر 2026 (منشور زميلتها قبل 5 أيام من 30 سبتمبر 2026)','win':'ضمن النطاق','edu':'','emp':'','role':'','cats':['program','project'],
 'd':'مسمّاة نصًّا شريكةً في مشروع «Privacy Guard» ضمن منشور تالين العمار عن إتمام «Computer Vision for Developers» في أكاديمية سدايا. مسمّاة لا موسومة، فلا يُرفق رابط (قاعدة زميل الفريق). يحتاج تحققًا. تنويه: الاسم العربي نقل حرفي.','links':[],'src':SRC_L,'tr':'ai'},('T','سارة الشبيب'))
TAG='[جولة 30 سبتمبر 2026] '
def add(i,txt): g[i-1]['d']=(g[i-1]['d'].rstrip()+' '+TAG+txt).strip()
def addlink(i,l,u):
    if u.rstrip('/').lower() not in [x[1].rstrip('/').lower() for x in g[i-1]['links']]:
        g[i-1]['links'].append([l,u]); return True
# --- cross notes
for key,ids in XN.items():
    ni=idmap[key]
    for oi in ids:
        g[ni-1]['d']+=' ⚠️ تنويه مطابقة: #%d «%s» (%s) — الاسم شائع وبلا تعزيز بالبرنامج أو التاريخ، فلم يُدمج واكتُفي بالإشارة المتبادلة.'%(oi,g[oi-1]['n'],g[oi-1]['prog'][:60])
        add(oi,'⚠️ تنويه مطابقة: السجل الجديد #%d «%s» (%s) يحمل اسمًا مطابقًا/قريبًا — لم يُدمج لغياب التعزيز؛ إشارة متبادلة فقط.'%(ni,g[ni-1]['n'],g[ni-1]['prog'][:60]))
# --- enrichments
enr=[]
allA={**A1,**A2}
for o,i in DUP_G.items():
    en,ar,k,b,repo,arv=allA[o]; x=g[i-1]
    addlink(i,'GitHub','https://github.com/'+o); addlink(i,'مستودع البرنامج','https://github.com/%s/%s'%(o,repo))
    li=li_of(o)
    if li: addlink(i,'LinkedIn',li)
    if not x.get('en'): x['en']=en
    txt='إثراء بدل تكرار: حساب GitHub `%s` ومستودع `%s` يطابقان هذا السجل (الاسم + البرنامج/الفترة).'%(o,repo)
    if li: txt+=' وأُضيف رابط LinkedIn المنشور على ملف GitHub.'
    if o in SECOND_PROG:
        k2=SECOND_PROG[o]; x['prog']+=' + '+PR[k2][0]+(' (2024)' if k2=='t5' else ' (سبتمبر 2026)'); txt+=' أُضيف برنامج ثانٍ مسمّى في المستودع: «%s». المطابقة بالاسم الكامل النادر مع رابط LinkedIn.'%PR[k2][2]
    add(i,txt); x['score']=max(x['score'],78); enr.append((i,o,txt))
for s,i in DUP_L.items():
    en,ar,k,ago,ev=L[s]; x=g[i-1]
    addlink(i,'LinkedIn','https://www.linkedin.com/in/'+s)
    if not x.get('en'): x['en']=en
    txt='منشور LinkedIn (%s): %s.'%(AGO[ago],ev)
    if s in SECOND_L:
        k2=SECOND_L[s]; x['prog']+=' + '+PR[k2][0]; txt+=' أُضيف برنامج ثانٍ: «%s».'%PR[k2][2]
    x['score']=max(x['score'],85); add(i,txt); enr.append((i,s,txt))
x=g[2624-1]; assert x['n']=='عبدالوهاب النصار'
x['prog']+=' + '+PR['ts'][0]; addlink(2624,'مستودع فريق السلاسل الزمنية','https://github.com/yalmutairi72-cpu/Data-science-Project1')
t='مسمّى «Abdulwahab Al-Nassar» في قائمة فريق مشروع التخرج لبرنامج «Time Series Forecasting for AI Systems» (مستودع yalmutairi72-cpu/Data-science-Project1، سبتمبر 2026) — برنامج ثانٍ.'
add(2624,t); enr.append((2624,'yalmutairi72-cpu',t))
cnt=collections.Counter(r['tr'] for r in g)
yrs={y:sum(1 for r in g if str(y) in (r.get('co') or '')) for y in range(2021,2027)}
none=sum(1 for r in g if not re.search(r'202[1-6]',r.get('co') or ''))
st={'total':len(g),'base':base,'new':len(g)-base,'tracks':dict(cnt),'hi':sum(1 for r in g if r['score']>=75),'md':sum(1 for r in g if 45<=r['score']<75),'lo':sum(1 for r in g if r['score']<45),
'wl':sum(1 for r in g if r.get('links')),'uu':len({u for r in g for l,u in r.get('links',[])}),'we':sum(1 for r in g if r.get('emp')),'yrs':yrs,'none':none,'enr':[e[0] for e in enr],'idmap':{str(k):v for k,v in idmap.items()}}
json.dump(st,open('stats30.json','w'),ensure_ascii=False)
json.dump(g,open('grads_after.json','w'),ensure_ascii=False)
json.dump(enr,open('enr30.json','w'),ensure_ascii=False)
print(json.dumps({k:v for k,v in st.items() if k not in('idmap',)},ensure_ascii=False))
nw=g[base:]
print(collections.Counter(r['lv'] for r in nw), collections.Counter(r['tr'] for r in nw))
print(collections.Counter(re.search(r'202\d',r['co']).group(0) for r in nw))
