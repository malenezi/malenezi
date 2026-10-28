# 28 Oct 2026 (b): 3 stories published on Prof. Mamdouh's relatedness ruling + GenAI note rewrite
import json,re,os,sys,collections,openpyxl,shutil
DRY='--apply' not in sys.argv
H=os.path.expanduser('~/mnt/Academy/'); DATE='28 أكتوبر 2026'; TAG='[جولة 28 أكتوبر 2026 (ب)] '
BK=H+'_backups/2026-10-28b/'
FILES=['SuccessStories/website/js/data.js','SuccessStories/website/index.html','index.html','Graduates/index.html','Graduates/Graduates_Database.xlsx','Graduates/Graduates_Database.md']
if not DRY:
    os.makedirs(BK,exist_ok=True)
    for f in FILES: shutil.copy2(H+f,BK+f.replace('/','__'))
def rep(s,a,b,c=None):
    n=s.count(a); assert n>=1,('missing',a[:80])
    if c is not None: assert n==c,(a[:80],n)
    return s.replace(a,b)
P=H+'Graduates/index.html'; s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+13; j=s.index('\nconst SITE_STATS'); D=json.loads(s[i:j].rstrip()[:-1]); g=D['grads']; head=s[:i]; tail=s[j:]
X_=H+'Graduates/Graduates_Database.xlsx'; wb=openpyxl.load_workbook(X_); ws=wb['قاعدة البيانات']
RUL='بحكم البروفيسور ممدوح العنزي (28 أكتوبر 2026) يُعدّ الدور مرتبطًا بالتدريب (البند 5-و).'
ST=[
 dict(k=3883,id='wedyan-almushaddag',year=2025,role='محللة أنظمة هندسة البترول (Associate Petroleum Engineering Systems Analyst) — المركز الرقمي للتنقيب والإنتاج',org='أرامكو السعودية',logo='assets/aramco.png',
  q='من معسكر سدايا × أكسفورد إلى المركز الرقمي للتنقيب والإنتاج في أرامكو.',qe='From the SDAIA × Oxford bootcamp to Aramco’s Upstream Digital Center.',
  impact='التحقت بأرامكو السعودية في مارس 2026 محللةَ أنظمة في المركز الرقمي للتنقيب والإنتاج — بعد خمسة أشهر من الإتمام.',
  story='أتمّت وديان معسكر هندسة تطبيقات الذكاء الاصطناعي (سدايا × جامعة أكسفورد) بين أغسطس وأكتوبر 2025. ثم تدربت مهندسةَ ذكاء اصطناعي لدى Beam Data (أغسطس – نوفمبر 2025)، وعملت مساعدةَ تدريس في الذكاء الاصطناعي بأكاديمية كاوست (يناير 2026)، وفي مارس 2026 التحقت بأرامكو السعودية في دور «Associate Petroleum Engineering Systems Analyst» بالمركز الرقمي للتنقيب والإنتاج. '+RUL,
  ach=['محللة أنظمة هندسة البترول — أرامكو السعودية، مارس 2026 (+5 أشهر)','مساعدة تدريس في الذكاء الاصطناعي — أكاديمية كاوست، يناير 2026','مهندسة ذكاء اصطناعي متدربة — Beam Data، أغسطس – نوفمبر 2025','إتمام معسكر سدايا × أكسفورد (أكتوبر 2025)'],
  exp='Artificial Intelligence Application Engineering Bootcamp، University of Oxford: أغسطس – أكتوبر 2025 · AI Engineer (Internship)، Beam Data: أغسطس – نوفمبر 2025 · AI Teaching Assistant، KAUST Academy: يناير 2026 · Associate Petroleum Engineering Systems Analyst، aramco: مارس 2026 – الآن'),
 dict(k=3895,id='reema-jubran-alqahtani',year=2025,role='محللة أنظمة تقنية المعلومات (Associate IT Systems Analyst)',org='أرامكو السعودية',logo='assets/aramco.png',
  q='معسكر سدايا × أكسفورد كان جسري إلى تحليل أنظمة التقنية في أرامكو.',qe='The SDAIA × Oxford bootcamp was my bridge to IT systems analysis at Aramco.',
  impact='التحقت بأرامكو السعودية في يونيو 2026 محللةَ أنظمة تقنية المعلومات — بعد ثمانية أشهر من الإتمام.',
  story='أتمّت ريما معسكر هندسة تطبيقات الذكاء الاصطناعي (سدايا × جامعة أكسفورد) متدربةً في الذكاء الاصطناعي بين أغسطس وأكتوبر 2025، ونالت شهادة إنجاز. وفي يونيو 2026 التحقت بأرامكو السعودية بدوام كامل في الظهران في دور «Associate IT Systems Analyst». '+RUL,
  ach=['محللة أنظمة تقنية المعلومات — أرامكو السعودية، يونيو 2026 (+8 أشهر)','عضوة في Mawhiba MetaMinds (M3)، منذ سبتمبر 2025','إتمام معسكر سدايا × أكسفورد بشهادة إنجاز (أكتوبر 2025)'],
  exp='(AI Intern) Artificial Intelligence in Application Software Engineering Bootcamp، SDAIA: أغسطس – أكتوبر 2025 · Associate IT Systems Analyst، aramco: يونيو 2026 – الآن'),
 dict(k=3890,id='samar-kilfaden',year=2025,role='برنامج تطوير الخريجين (GDP)',org='صندوق الاستثمارات العامة (PIF)',logo='assets/pif.png',
  q='بعد سدايا × أكسفورد، بدأت مسيرتي في صندوق الاستثمارات العامة.',qe='After SDAIA × Oxford, my career began at the Public Investment Fund.',
  impact='التحقت ببرنامج تطوير الخريجين في صندوق الاستثمارات العامة في نوفمبر 2025 — في الشهر التالي للإتمام.',
  story='أتمّت سمر برنامج سدايا × أكسفورد للذكاء الاصطناعي في جامعة أكسفورد (وحدات في كلية مجدلين وكلية سعيد للأعمال)، وتعلمت فيه الرؤية الحاسوبية ومعالجة اللغة الطبيعية والنماذج التوليدية. وفي نوفمبر 2025 التحقت ببرنامج تطوير الخريجين (GDP) في صندوق الاستثمارات العامة. '+RUL,
  ach=['برنامج تطوير الخريجين — صندوق الاستثمارات العامة، نوفمبر 2025 (+1 شهر)','إتمام برنامج سدايا × أكسفورد للذكاء الاصطناعي (2025)'],
  exp='GDP، Public Investment Fund (PIF): نوفمبر 2025 – الآن؛ ومنشور الإتمام قبل سنة أو أكثر من 28 أكتوبر 2026 (أي في أغسطس – أكتوبر 2025، ضمن نافذة الدفعة)'),
]
dj=H+'SuccessStories/website/js/data.js'; sj=open(dj,encoding='utf-8').read()
for p in ST:
    assert len(p['q'])<=100 and len(p['qe'])<=100,(p['id'],len(p['q']),len(p['qe']))
    assert ('"id": "%s"'%p['id']) not in sj
    assert os.path.exists(H+'SuccessStories/website/'+p['logo'])
G=None; stories=[]
for p in ST:
    G=g[p['k']-1]
    st={"id":p['id'],"year":p['year'],"quote":{"text":p['q'],"textEn":p['qe'],"kind":"draft"},"name":G['n'],"nameEn":G['en'],"photo":None,"role":p['role'],"org":p['org'],"orgLogo":p['logo'],"program":G['prog'],"period":G['co'],"category":"employment","categories":["employment"],"impact":p['impact'],"story":p['story'],"achievements":p['ach'],"links":[{"label":"LinkedIn","url":G['links'][0][1]}],"provenance":f"صفحة الخبرة على LinkedIn بحساب مسجَّل (قُرئت {DATE})، بتواريخ بمستوى الشهر: {p['exp']} + سجل الأكاديمية #{p['k']}."}
    stories.append(st)
    if 'job' not in G['cats']: G['cats'].append('job')
    G['emp']=p['org']; G['role']=p['role']; k=p['k']; assert ws.cell(k+1,1).value==k
    ws.cell(k+1,7).value=p['org']; ws.cell(k+1,8).value=p['role']
    t=TAG+'نُشرت قصة نجاح «%s» وفق السياسة v1.0 (معيار 14 شهرًا) بعد حكم الارتباط: %s'%(p['id'],p['ach'][0])
    G['d']=(G['d']+' '+t).strip(); ws.cell(k+1,21).value=((ws.cell(k+1,21).value or '')+' '+t).strip()
if p['id']=='samar-kilfaden':
    G=g[3890-1]; G['co']='أغسطس – أكتوبر 2025 (منشور الإتمام قبل سنة أو أكثر من 28 أكتوبر 2026)'; ws.cell(3891,6).value=G['co']; stories[-1]['period']=G['co']
for t in [json.dumps(x,ensure_ascii=False) for x in stories]: assert '**' not in t
orgs0=set(re.findall(r'"org": "([^"]+)"',sj)); newemp={p['org'] for p in ST}-orgs0; assert not newemp,newemp
S0=209; S1=212
print('stories',S0,'->',S1,[p['id'] for p in ST])
# GenAI note
nv=lambda r:bool(re.search(r'NVIDIA',r['prog']))
A={k for k,r in enumerate(g,1) if nv(r)}; B={k for k,r in enumerate(g,1) if r['lv']=='nvidia'}; GT=sum(r['tr']=='genai' for r in g)
U=len(A|B); oth=len({k for k in A|B if g[k-1]['tr']!='genai'})
print('note',len(A),len(B),U,GT,oth)
if DRY: sys.exit()
def stc(t):
    for a,b in (('%d قصة'%S0,'%d قصة'%S1),('%d stories'%S0,'%d stories'%S1),('%d verified success stories'%S0,'%d verified success stories'%S1),('%d قصة نجاح'%S0,'%d قصة نجاح'%S1)):
        t=t.replace(a,b)
    return t
head=stc(head); tail=stc(tail)
tail,n=re.subn(r"(\{ value: )%d(,\s+label: 'قصة نجاح)"%S0,r"\g<1>%d\2"%S1,tail); assert n==1
old=re.search(r'<p class="sd-note" data-ar="تُحسب «أكاديمية الذكاء الاصطناعي التوليدي»[^"]*" data-en="[^"]*"></p>',head+tail)
NOTE=(f'<p class="sd-note" data-ar="تعرض بطاقة «أكاديمية الذكاء الاصطناعي التوليدي» {GT} سجلًا مسارها الأساسي هذه الأكاديمية. وعبر كل الطبقات يحمل {U} سجلًا غير مكرَّر برنامجًا من برامج NVIDIA ({len(A)} يذكر NVIDIA صراحةً في حقل البرنامج، و{len(B)} من طبقة «برامج NVIDIA» الرسمية)، منها {oth} سجلًا يُحتسب في مسار آخر وفق ترتيب أولوية المسارات. الرقم الرسمي 232 حدّ أدنى وليس سقفًا." '
      f'data-en="The “Gen AI Academy” card shows the {GT} records whose primary track is this academy. Across all tiers, {U} distinct records hold an NVIDIA program ({len(A)} name NVIDIA in the program field; {len(B)} come from the official NVIDIA tier), and {oth} of them count under another track by track precedence. The official figure of 232 is a floor, not a ceiling."></p>')
assert old
if old.group(0) in head: head=head.replace(old.group(0),NOTE)
else: tail=tail.replace(old.group(0),NOTE)
D['grads']=g; open(P,'w',encoding='utf-8').write(head+json.dumps(D,ensure_ascii=False)+';'+tail)
P2=H+'index.html'; s=stc(open(P2,encoding='utf-8').read()); s=rep(s,'data-count="%d"'%S0,'data-count="%d"'%S1,1); open(P2,'w',encoding='utf-8').write(s)
s=sj; s=re.sub(r"(\{ value: )%d(,\s+label: 'قصة نجاح)"%S0,r"\g<1>%d\2"%S1,s,count=1)
k=s.index('const STORIES = ['); e=s.index('\n];',k); prev=s[:e].rstrip()
if not prev.endswith(','): prev+=','
s=prev+'\n'+',\n'.join('  '+json.dumps(x,ensure_ascii=False) for x in stories)+s[e:]
s=rep(s,'"id": "amjad-alnasser", "year": 2025,','"id": "amjad-alnasser", "year": 2025,',1)
s=s.replace('"name": "أمجاد الناصر", "nameEn": "Amjad Alnasser", "photo": null, "role": "محللة أنظمة — الأمن السيبراني بالذكاء الاصطناعي (AI Cybersecurity – IT System Analyst)", "org": "أرامكو السعودية", "program"','"name": "أمجاد الناصر", "nameEn": "Amjad Alnasser", "photo": null, "role": "محللة أنظمة — الأمن السيبراني بالذكاء الاصطناعي (AI Cybersecurity – IT System Analyst)", "org": "أرامكو السعودية", "orgLogo": "assets/aramco.png", "program"',1)
s=rep(s,"'use strict';","/* %s (ب): ثلاث قصص بعد حكم الارتباط — القصص %d. */\n'use strict';"%(DATE,S1),1)
open(dj,'w',encoding='utf-8').write(s)
P4=H+'SuccessStories/website/index.html'; t=open(P4,encoding='utf-8').read(); t=rep(t,'"numberOfItems": %d'%S0,'"numberOfItems": %d'%S1,1); open(P4,'w',encoding='utf-8').write(t)
st=wb['إحصاءات']
for row in st.iter_rows():
    if row[0].value=='تحديث': row[1].value=str(row[1].value)+f' · (ب) ثلاث قصص بعد حكم الارتباط — القصص {S1}'
sh=wb['جولة_28_أكتوبر_2026']
for p in ST: sh.append([p['k'],g[p['k']-1]['n'],'قصة جديدة (حكم الارتباط)',p['org']+' — '+p['role']])
wb.save(X_)
P5=H+'Graduates/Graduates_Database.md'; s=open(P5,encoding='utf-8').read()
s=rep(s,'(3,904 → 3,915 · القصص 209 · جهات العمل 113)','(3,904 → 3,915 · القصص 212 · جهات العمل 113)',1)
s=rep(s,'إثراء 9 سجلات، منها أول خريجة NCA-ADS (#3076). لا قصص جديدة.','إثراء 9 سجلات، منها أول خريجة NCA-ADS (#3076). (ب) بعد حكم الارتباط نُشرت ثلاث قصص: wedyan-almushaddag · reema-jubran-alqahtani · samar-kilfaden (القصص 209 → 212).',1)
open(P5,'w',encoding='utf-8').write(s)
for f in ('index.html','Graduates/index.html'):
    t=open(H+f,encoding='utf-8').read(); print(f,'209 left',len(re.findall(r'\b209 (قصة|stories|verified)',t)),'212',t.count('212'))
print('done')
