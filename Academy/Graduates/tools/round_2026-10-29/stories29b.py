# -*- coding: utf-8 -*-
# 29 Oct 2026 (b): 5 stories published on Prof. Mamdouh's rulings; Duaa Khorsheed ruled not related.
import json,re,os,sys,openpyxl,shutil
DRY='--apply' not in sys.argv
H=os.path.expanduser('~/mnt/Academy/'); DATE='29 أكتوبر 2026'; TAG='[جولة 29 أكتوبر 2026 (ب)] '
BK=H+'_backups/2026-10-29b/'
FILES=['SuccessStories/website/js/data.js','SuccessStories/website/index.html','index.html','Graduates/index.html','Graduates/Graduates_Database.xlsx','Graduates/Graduates_Database.md']
if not DRY:
    os.makedirs(BK,exist_ok=True)
    for f in FILES: shutil.copy2(H+f,BK+f.replace('/','__'))
def rep(s,a,b,c=None):
    n=s.count(a); assert n>=1,('missing',a[:80])
    if c is not None: assert n==c,(a[:80],n)
    return s.replace(a,b)
P=H+'Graduates/index.html'; s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+13; j=s.index('\nconst SITE_STATS'); D=json.loads(s[i:j].rstrip()[:-1]); g=D['grads']; head=s[:i]; tail=s[j:]; assert len(g)==3929
X_=H+'Graduates/Graduates_Database.xlsx'; wb=openpyxl.load_workbook(X_); ws=wb['قاعدة البيانات']
RUL='بحكم أ. د. ممدوح العنزي (29 أكتوبر 2026)'
ST=[
 dict(k=3103,id='sultan-alanazi',year=2024,period='يوليو – أكتوبر 2024',role='متدرب عالم بيانات (Data Scientist Trainee) — دوام كامل',org='هيئة الزكاة والضريبة والجمارك (ZATCA)',logo='assets/zatca.png',
  q='من معسكر علوم البيانات في سدايا إلى علوم البيانات في هيئة الزكاة.',qe='From SDAIA’s data science bootcamp to data science at ZATCA.',
  impact='التحق بهيئة الزكاة والضريبة والجمارك متدربًا في علوم البيانات بدوام كامل في مارس 2025 — بعد خمسة أشهر من إتمام المعسكر.',
  story='أتمّ سلطان معسكر علوم البيانات والذكاء الاصطناعي في أكاديمية سدايا بين يوليو وأكتوبر 2024. وفي مارس 2025 التحق بهيئة الزكاة والضريبة والجمارك في برنامج «Data Scientist Trainee» بدوام كامل حتى سبتمبر 2025، ثم انضم في يونيو 2026 إلى Merkle MENA محللَ بيانات. يُعدّ برنامج المتدرب بدوام كامل نتيجة توظيفية '+RUL+'.',
  ach=['متدرب عالم بيانات — هيئة الزكاة والضريبة والجمارك، مارس – سبتمبر 2025 (+5 أشهر)','محلل بيانات — Merkle MENA، يونيو 2026','إتمام معسكر علوم البيانات والذكاء الاصطناعي — أكاديمية سدايا (أكتوبر 2024)'],
  exp='Data Scientist Trainee، Zakat, Tax and Customs Authority، دوام كامل: مارس – سبتمبر 2025 · Data Analyst، Merkle MENA: يونيو 2026 – الآن · Data Science and AI Bootcamp، SDAIA: يوليو – أكتوبر 2024'),
 dict(k=952,id='hassan-alshanqiti',year=2024,period='الربع الأول 2024',role='محلل بحث وتطوير (Research & Development Analyst)',org='ثقة (THIQAH)',logo=None,
  q='من معسكر تعلم الآلة في سدايا إلى البحث والتطوير في ثقة.',qe='From SDAIA’s ML bootcamp to research and development at THIQAH.',
  impact='التحق بشركة ثقة محللَ بحث وتطوير بدوام كامل في أبريل 2025 — ضمن نافذة الأربعة عشر شهرًا.',
  story='أتمّ حسن معسكر تعلم الآلة (ML) في أكاديمية سدايا ضمن دفعة الربع الأول من 2024، ثم تدرّب باحثًا في تعلم الآلة لدى معهد الابتكار التكنولوجي TII (مايو – نوفمبر 2024). وفي أبريل 2025 التحق بشركة ثقة محللَ بحث وتطوير بدوام كامل. أهليته ضمن النافذة '+RUL+'.',
  ach=['محلل بحث وتطوير — ثقة، أبريل – أغسطس 2025','متدرب باحث في تعلم الآلة — معهد الابتكار التكنولوجي TII، مايو – نوفمبر 2024','إتمام معسكر تعلم الآلة — أكاديمية سدايا (الربع الأول 2024)'],
  exp='Research & Development Analyst، THIQAH، دوام كامل: أبريل – أغسطس 2025 · Machine Learning Research Intern، Technology Innovation Institute: مايو – نوفمبر 2024؛ وفترة المعسكر من «الوثائق الداعمة للمؤشر الاستراتيجي» (الربع الأول 2024)'),
 dict(k=2095,id='refal-alzweaid',year=2026,period='ديسمبر 2025 – فبراير 2026',role='أخصائية هندسة تقنية المعلومات (IT Technology Engineering Specialist)',org='مصرف الإنماء',logo='assets/alinma.png',
  q='معسكر محترفي الذكاء الاصطناعي قادني إلى هندسة التقنية في مصرف الإنماء.',qe='The AI Professionals Bootcamp led me to technology engineering at Alinma Bank.',
  impact='التحقت بمصرف الإنماء أخصائيةً لهندسة تقنية المعلومات بدوام كامل في مايو 2026 — بعد ثلاثة أشهر من إتمام المعسكر.',
  story='أتمّت رفال معسكر أكاديمية سدايا لمحترفي الذكاء الاصطناعي بين ديسمبر 2025 وفبراير 2026، بالتوازي مع تلمذة مطوِّرةً للذكاء الاصطناعي وتعلم الآلة في نيوليب (أكتوبر 2025 – مايو 2026). وفي مايو 2026 التحقت بمصرف الإنماء أخصائيةً لهندسة تقنية المعلومات بدوام كامل. يُعدّ الدور مرتبطًا بالتدريب '+RUL+'.',
  ach=['أخصائية هندسة تقنية المعلومات — مصرف الإنماء، مايو 2026 (+3 أشهر)','مطوّرة ذكاء اصطناعي وتعلم آلة (تلمذة) — نيوليب، أكتوبر 2025 – مايو 2026','إتمام معسكر محترفي الذكاء الاصطناعي — أكاديمية سدايا (فبراير 2026)'],
  exp='IT Technology Engineering Specialist، Alinma Bank، دوام كامل: مايو 2026 – الآن · AI/ML Developer (Apprenticeship)، neoleap: أكتوبر 2025 – مايو 2026 · AI Professionals Bootcamp، SDAIA: ديسمبر 2025 – فبراير 2026'),
 dict(k=2253,id='sara-omairah',year=2024,period='يوليو – أكتوبر 2024',role='محللة أعمال (Business Analyst)',org='مصرف الإنماء',logo='assets/alinma.png',
  q='من معسكر علوم البيانات إلى برنامج «مصرفيو المستقبل» في مصرف الإنماء.',qe='From the data science bootcamp to Alinma Bank’s Future Bankers programme.',
  impact='التحقت ببرنامج تطوير الخريجين «Future Bankers» في مصرف الإنماء في فبراير 2025 — بعد أربعة أشهر من الإتمام — ثم ثُبّتت محللةَ أعمال في فبراير 2026.',
  story='أتمّت سارة معسكر T5 لعلوم البيانات والذكاء الاصطناعي في أكاديمية سدايا بين يوليو وأكتوبر 2024. وفي فبراير 2025 التحقت ببرنامج تطوير الخريجين «Future Bankers» في مصرف الإنماء متدربةً في تحليل الأعمال، ثم عُيّنت محللةَ أعمال بدوام كامل في فبراير 2026. يُعدّ الدور مرتبطًا بالتدريب '+RUL+'.',
  ach=['متدربة تحليل أعمال — برنامج Future Bankers، مصرف الإنماء، فبراير 2025 (+4 أشهر)','محللة أعمال بدوام كامل — مصرف الإنماء، فبراير 2026','إتمام معسكر T5 لعلوم البيانات والذكاء الاصطناعي (أكتوبر 2024)'],
  exp='Business Analyst، alinma، دوام كامل: فبراير 2026 – الآن · Business Analyst trainee | Future Bankers GDP، alinma: فبراير 2025 – فبراير 2026 · T5 Data Science & AI Bootcamp، SDAIA: يوليو – أكتوبر 2024'),
 dict(k=3458,id='abdulaziz-althobaiti',year=2025,period='2025',role='عالم بيانات (Data Scientist)',org='وازن (Wazen ERP)',logo=None,
  q='معسكر علوم البيانات في سدايا قادني إلى علوم البيانات في وازن.',qe='SDAIA’s data science bootcamp led me to data science at Wazen.',
  impact='التحق بوازن عالمَ بيانات بدوام كامل في يناير 2026 — ضمن نافذة الأربعة عشر شهرًا من إتمام المعسكر.',
  story='أتمّ عبدالعزيز معسكر T5 لعلوم البيانات (أكاديمية سدايا بالتعاون مع أكاديمية طويق، ثلاثة أشهر) ومعسكرًا للذكاء الاصطناعي لمدة شهرين. وفي يناير 2026 التحق بشركة وازن (Wazen ERP) عالمَ بيانات بدوام كامل. التوقيت ضمن النافذة '+RUL+'.',
  ach=['عالم بيانات — وازن، يناير 2026','إتمام معسكر T5 لعلوم البيانات — أكاديمية سدايا وأكاديمية طويق (2025)','إتمام معسكر الذكاء الاصطناعي — سدايا وطويق (شهران)'],
  exp='Data Scientist، Wazen ERP، دوام كامل: يناير 2026 – الآن؛ والمعسكران من ملفه على GitHub (abdu1z1z)'),
]
dj=H+'SuccessStories/website/js/data.js'; sj=open(dj,encoding='utf-8').read()
orgs0=set(re.findall(r'"org": "([^"]+)"',sj))
stories=[]
for p in ST:
    assert len(p['q'])<=100 and len(p['qe'])<=100,(p['id'],len(p['q']),len(p['qe']))
    assert ('"id": "%s"'%p['id']) not in sj,p['id']
    if p['logo']: assert os.path.exists(H+'SuccessStories/website/'+p['logo'])
    G=g[p['k']-1]; li=[l[1] for l in G['links'] if 'linkedin.com/in/' in l[1]][0]
    st={"id":p['id'],"year":p['year'],"quote":{"text":p['q'],"textEn":p['qe'],"kind":"draft"},"name":G['n'],"nameEn":G['en'],"photo":None,"role":p['role'],"org":p['org']}
    if p['logo']: st["orgLogo"]=p['logo']
    st.update({"program":G['prog'],"period":p['period'],"category":"employment","categories":["employment"],"impact":p['impact'],"story":p['story'],"achievements":p['ach'],"links":[{"label":"LinkedIn","url":li}],
       "provenance":f"صفحة الخبرة على LinkedIn بحساب مسجَّل (قُرئت {DATE})، بتواريخ بمستوى الشهر: {p['exp']} + سجل الأكاديمية #{p['k']}. {RUL} وفق السياسة v1.0."})
    stories.append(st)
    if 'job' not in G['cats']: G['cats'].append('job')
    G['emp']=p['org']; G['role']=p['role']; k=p['k']; ws.cell(k+1,7).value=p['org']; ws.cell(k+1,8).value=p['role']
    t=TAG+'%s: مستوفٍ — نُشرت قصة نجاح «%s»: %s'%(RUL,p['id'],p['ach'][0])
    G['d']=(G['d']+' '+t).strip(); ws.cell(k+1,21).value=((ws.cell(k+1,21).value or '')+' '+t).strip()
t=TAG+RUL+': الدور غير مرتبط بالتدريب (§5-و) — ليست قصة نجاح.'
g[3451]['d']+=' '+t; ws.cell(3453,21).value=(ws.cell(3453,21).value or '')+' '+t
for x in stories: assert '**' not in json.dumps(x,ensure_ascii=False)
newemp={p['org'] for p in ST}-orgs0
S0=216; S1=S0+len(ST); E0=115; E1=E0+len(newemp)
print('stories',S0,S1,'emp',E0,E1,newemp)
if DRY: sys.exit()
def stc(t):
    for a,b in (('%d قصة'%S0,'%d قصة'%S1),('%d stories'%S0,'%d stories'%S1),('%d verified success stories'%S0,'%d verified success stories'%S1),('%d جهة عمل'%E0,'%d جهة عمل'%E1),('%d employers'%E0,'%d employers'%E1)):
        t=t.replace(a,b)
    return t
head=stc(head); tail=stc(tail)
tail,n=re.subn(r"(\{ value: )%d(,\s+label: 'قصة نجاح)"%S0,r"\g<1>%d\2"%S1,tail); assert n==1
D['grads']=g; open(P,'w',encoding='utf-8').write(head+json.dumps(D,ensure_ascii=False)+';'+tail)
P2=H+'index.html'; s=stc(open(P2,encoding='utf-8').read()); s=rep(s,'data-count="%d"'%S0,'data-count="%d"'%S1,1); s=rep(s,'data-count="%d"'%E0,'data-count="%d"'%E1,1); open(P2,'w',encoding='utf-8').write(s)
s=sj
s,n=re.subn(r"(\{ value: )%d(,\s+label: 'قصة نجاح)"%S0,r"\g<1>%d\2"%S1,s,count=1); assert n==1
s,n=re.subn(r"(\{ value: )%d(,\s+label: 'جهة عمل')"%E0,r"\g<1>%d\2"%E1,s,count=1); assert n==1
k=s.index('const STORIES = ['); e=s.index('\n];',k); prev=s[:e].rstrip()
if not prev.endswith(','): prev+=','
s=prev+'\n'+',\n'.join('  '+json.dumps(x,ensure_ascii=False) for x in stories)+s[e:]
s=rep(s,"'use strict';","/* %s (ب): خمس قصص بأحكام أ. د. ممدوح العنزي (sultan-alanazi · hassan-alshanqiti · refal-alzweaid · sara-omairah · abdulaziz-althobaiti) — القصص %d؛ جهات العمل %d. دعاء خورشيد #3452: غير مرتبط. */\n'use strict';"%(DATE,S1,E1),1)
open(dj,'w',encoding='utf-8').write(s)
P4=H+'SuccessStories/website/index.html'; t=open(P4,encoding='utf-8').read(); t=rep(t,'"numberOfItems": %d'%S0,'"numberOfItems": %d'%S1,1); open(P4,'w',encoding='utf-8').write(t)
st=wb['إحصاءات']
for row in st.iter_rows():
    if row[0].value=='تحديث': row[1].value=str(row[1].value)+f' · (ب) خمس قصص بأحكام أ. د. ممدوح العنزي — القصص {S1}؛ جهات العمل {E1}'
sh=wb['جولة_29_أكتوبر_2026']
for p in ST: sh.append([p['k'],g[p['k']-1]['n'],'قصة جديدة (حكم 29 أكتوبر)',p['org']+' — '+p['ach'][0]])
sh.append([3452,g[3451]['n'],'حكم: غير مرتبط','ليست قصة'])
wb.save(X_)
P5=H+'Graduates/Graduates_Database.md'; s=open(P5,encoding='utf-8').read()
s=rep(s,'(3,915 → 3,929 · القصص 216 · جهات العمل 115)','(3,915 → 3,929 · القصص %d · جهات العمل %d)'%(S1,E1),1)
s=rep(s,'قيد الحكم: #3103 · #952 · #2095 · #2253 · #3452 · #3458.','(ب) بأحكام أ. د. ممدوح العنزي نُشرت خمس قصص: sultan-alanazi (هيئة الزكاة) · hassan-alshanqiti (ثقة) · refal-alzweaid (مصرف الإنماء) · sara-omairah (مصرف الإنماء) · abdulaziz-althobaiti (وازن) — القصص %d، وجهات العمل %d؛ و#3452 غير مرتبط.'%(S1,E1),1)
open(P5,'w',encoding='utf-8').write(s)
for f in ('index.html','Graduates/index.html'):
    t=open(H+f,encoding='utf-8').read(); t=t if f=='index.html' else t[:t.index('const DATA = ')]+t[t.index('\nconst SITE_STATS'):]
    print(f,'216 left',len(re.findall(r'\b216 (قصة|stories|verified)',t)),'115 left',len(re.findall(r'\b115 (جهة|employers)',t)))
print('done')
