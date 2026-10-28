# -*- coding: utf-8 -*-
# Round 28 Oct 2026 (e) — supplied LinkedIn posts (9, all already in DB → enrichments), past-week post sweep (+2 new), photos/logos wiring.
import json,re,os,sys,shutil,collections,openpyxl
DRY='--apply' not in sys.argv
H=os.path.expanduser('~/mnt/Academy/')
DATE='28 أكتوبر 2026 (هـ)'; TAG='[جولة 28 أكتوبر 2026 (هـ)] '
TL=' تنويه: الاسم العربي نقل حرفي عن الاسم اللاتيني المنشور — غير متحقق علنًا.'
TRN={'ai':'مهندس ذكاء اصطناعي — AI Engineer','ds':'عالم بيانات — Data Scientist','other':'برامج متخصصة أخرى — Other / Specialized','dmg':'إدارة وحوكمة البيانات — Data Management & Governance','genai':'أكاديمية الذكاء الاصطناعي التوليدي — Gen AI Academy','coop':'التدريب التعاوني — Cooperative Training (COOP)'}
def rep(s,a,b,count=None):
    n=s.count(a); assert n>=1,('missing',a[:90])
    if count is not None: assert n==count,(a[:90],n)
    return s.replace(a,b)
def rrep(s,pat,b,count=1,flags=0):
    s2,n=re.subn(pat,b,s,flags=flags); assert n==count,(pat,n); return s2
FILES=['SuccessStories/website/js/data.js','SuccessStories/website/index.html','index.html','Graduates/index.html','Graduates/Graduates_Database.xlsx','Graduates/Graduates_Database.md','SuccessStories/website/assets/ammar-alsehli.jpeg']
BK=H+'_backups/2026-10-28e/'
if not DRY:
    os.makedirs(BK,exist_ok=True)
    for f in FILES:
        t=BK+f.replace('/','__')
        if not os.path.exists(t): shutil.copy2(H+f,t)
LI='https://www.linkedin.com/in/'; PO='https://www.linkedin.com/posts/'; P='منشور على LinkedIn '
new=[
('سعود الشباني','Saud Alshabani',[['LinkedIn',LI+'saud-alshabani-a99220391/']],'الذكاء الاصطناعي لرفع الإنتاجية — أتمتة سير العمل بالذكاء الاصطناعي (Workflow Automation using AI) — أكاديمية سدايا','أكتوبر 2026 (منشور الإتمام ~26 أكتوبر 2026)','other',78,
 P+'(~26 أكتوبر 2026): «I’m pleased to share that I have successfully completed the Workflow Automation using AI training program offered by SDAIA Academy». صفحة الخبرة (حساب مسجَّل): DevOps Engineer — مجموعة ثروة (Tharwah Group)، دوام كامل، أكتوبر 2026 – الآن · معسكر تطوير البرمجيات — الأكاديمية السعودية الرقمية، مايو – يونيو 2026. لا قصة نجاح: الوظيفة في شهر الإتمام نفسه (التزامن ليس تعاقبًا) وغير مرتبطة بالبرنامج (§5-و).',
 'مجموعة ثروة (Tharwah Group)','DevOps Engineer'),
('مها السويد','Maha Alsuwayid',[['LinkedIn',LI+'maha-alsuwayid-736835363/']],'التدريب التعاوني — أكاديمية سدايا (COOP)','أغسطس – أكتوبر 2026 (منشور الإتمام ~27 أكتوبر 2026)','coop',78,
 P+'(~27 أكتوبر 2026): «I have successfully completed my Cooperative Training Program at SDAIA… During my time at SDAIA Academy, I had the opportunity to work on process improvement, data analytics, and AI-driven solutions» — ومن إسهاماتها لوحة Power BI لتحليل مخرجات توظيف الخريجين. صفحة الخبرة: «Coop — SDAIA | سدايا، أغسطس 2026 – الآن». طالبة تقنية معلومات.',
 '',''),
]
enr=[
{'k':3909,'n':'لمى عبدالعزيز بن عسكر','en':'Lama Abdulaziz Bin Askar','co':'11–15 أكتوبر 2026 (شهادة حضور)','links':[['منشور الإتمام',PO+'lama-binaskar_aebaexaepaeyaep-aelaeraepaexaeyaetaeyaerabraebaexaepaeyaep-ugcPost-7520494135305265152-IWI8/']],
 't':'الاسم الكامل (من رابط زوّد به أ. د. ممدوح العنزي، ومن صورة الشهادة في المنشور): «Lama Abdulaziz Bin Askar — لمى عبدالعزيز بن عسكر»، شهادة حضور «هندسة الأوامر والاستخدام المسؤول للذكاء الاصطناعي» 11–15 أكتوبر 2026، والمدرّب عبدالله الشهراني. حُسمت الإشارة إلى #1388 «لمى سلطان عبدالله بن عسكر»: اسم الأب مختلف، فهما شخصان مختلفان.'},
{'k':3081,'links':[['منشور الإتمام',PO+'sama-alzahrani_%D8%B4%D9%87%D8%A7%D8%AF%D8%A9-%D8%A7%D8%AC%D8%AA%D9%8A%D8%A7%D8%B2-ugcPost-7513329522663096320-cqWU/']],
 't':'منشور إتمام على LinkedIn (~6 أكتوبر 2026، رابط زوّد به أ. د. ممدوح العنزي): «اختتمت مؤخرًا برنامج تصوير البيانات وسرد القصص… امتد لثلاثة أيام… مشروع Tayseer… وحصلت على شهادة اجتياز من SDAIA». يطابق الحساب ومستودع Tayseer المسجّلين.'},
{'k':1223,'links':[['منشور الإتمام',PO+'maryambuqrain_maryambuquraynadvanced-ml-techniques-ugcPost-7510309422103937024-Ud-2/']],
 't':'منشور على LinkedIn (~28 سبتمبر 2026، رابط زوّد به أ. د. ممدوح العنزي): «أنهيت الأسبوع الماضي البرنامج التدريبي "أساليب تعلم الآلة المتقدمة" المقدم من SDAIA Academy» مع شكر المدرّبة أسماء الزبيدي — يؤكد إتمام البرنامج الثاني في سبتمبر 2026. لا قصة: وظيفة NWC (سبتمبر 2025) سابقة للبرنامج الثاني.'},
{'k':3146,'links':[['منشور الإتمام',PO+'dareen-alshehri1_advanced-agentic-ai-systems-engineering-certificate-ugcPost-7510669701904142337-d33y/']],'emp':'Majorel','role':'Customer Service Specialist',
 't':'رابط منشور الإتمام (~29 سبتمبر 2026) زوّد به أ. د. ممدوح العنزي. صفحة الخبرة (حساب مسجَّل): Customer Service Specialist — Majorel، دوام كامل، سبتمبر 2026 – الآن (دعم برنامج حساب المواطن) · Data Processing & Quality Reviewer — SAMI Advanced Electronics (عمل حر، 2026). لا قصة: الوظيفة غير مرتبطة بالبرنامج (§5-و) وفي شهر الإتمام.'},
{'k':3875,'links':[['منشور الإتمام',PO+'aseel-alghamdi-6a1539353_aepaesaeyaeraepaejabraepaesaepaedaefaeuaepaehaey-ugcPost-7518655435202142208-RWbC/']],
 't':'منشور ثانٍ (~21 أكتوبر 2026، رابط زوّد به أ. د. ممدوح العنزي): مشروعها مساعد لموظفي الدعم يفهم رسائل العملاء باللهجة الخليجية، ورفعت دقته على اللهجة من 0.27 إلى 0.79. الحساب «Open to Work» — لا وظيفة لاحقة بعد.'},
{'k':2542,'links':[['منشور شهادة NVIDIA',PO+'sadeem-alharbi-740300377_nvidia-generativeai-llm-share-7511918519907667968-paGN/']],'prog_add':'التدريب الاحترافي في النماذج اللغوية الكبيرة (سدايا × NVIDIA) + شهادة NVIDIA NCA-GENL — أكاديمية سدايا (أكتوبر 2026)',
 't':'منشور على LinkedIn (~2 أكتوبر 2026، رابط زوّد به أ. د. ممدوح العنزي): شهادة NVIDIA في Generative AI & LLMs «بعد تجربة تدريبية ثرية ضمن برنامج SDAIA Academy × NVIDIA» — أُضيف البرنامج إلى حقل البرامج. صفحة الخبرة فارغة.'},
{'k':3172,'links':[['منشور الإتمام',PO+'abrar-alfrede-b42116314_share-7510612092505436160-Ey8y/']],
 't':'رابط منشور الإتمام (~29 سبتمبر 2026) زوّد به أ. د. ممدوح العنزي؛ المدرّبة هبة سليمان.'},
{'k':3173,'links':[['منشور الإتمام',PO+'raghad-almogbel-alqahtani_modern-data-engineering-for-ai-systems-ugcPost-7510585743808016384-i31v/']],'emp':'الشؤون الصحية بوزارة الحرس الوطني (MNGHA)','role':'Healthcare Service Engineer II',
 't':'رابط منشور الإتمام (~29 سبتمبر 2026) زوّد به أ. د. ممدوح العنزي. صفحة الخبرة (حساب مسجَّل): الشؤون الصحية بوزارة الحرس الوطني منذ نوفمبر 2023 (Healthcare Service Engineer II منذ مارس 2025) · AI Consultant — جامعة الفيصل (2025) · AI Research Affiliate — مركز الذكاء الاصطناعي بجامعة الفيصل (نوفمبر 2025). كلها سابقة للبرنامج — لا قصة.'},
{'k':3873,'links':[['منشور الإتمام',PO+'munirah-bin-dukhayn-951440282_aelaeraepaexaeyaetaeyaerabraebaexaepaeyaep-ugcPost-7520344958642581504-nHxz/']],
 't':'رابط منشور الإتمام (~26 أكتوبر 2026) زوّد به أ. د. ممدوح العنزي — يطابق المنشور المسجّل.'},
{'k':2800,'links':[['LinkedIn',LI+'ghala-a-670a62380/']],'prog_add':'تطوير حلول الذكاء الاصطناعي التوليدي (Developing Generative AI Solutions) — أكاديمية سدايا (أكتوبر 2026)',
 't':'منشور على LinkedIn (~27 أكتوبر 2026) من «Ghala Alshreef» (IT | Junior AI Engineer | Computer Vision & NLP): «completed the Developing Generative AI Solutions program by SDAIA Academy» ومشروعها «Ask My PDF» (مساعد RAG بإحالات للصفحات). المطابقة: الاسم الكامل النادر + اهتمام NLP الموافق لبرنامج «بيان» المسجّل. صفحة الخبرة: Project Manager (COOP) — موبايلي، يونيو – سبتمبر 2026 · AI Track Co-Lead — نادي طويق، جامعة الملك سعود، سبتمبر 2026. لا قصة (تدريب تعاوني ونشاط طلابي).'},
]
IMG={'abdulelah-khalaf':('assets/abdulelah-khalaf.jpeg','assets/nagarro_logo.jpeg'),'amjad-alnasser':('assets/amjad-alnasser.jpeg',None),'ammar-alsehli':('assets/ammar-alsehli.jpeg','assets/saisksa_logo.jpeg'),
     'bassam-alnefaie':('assets/bassam-alnefaie.jpeg','assets/pyxon-logo.png'),'hashem-almubarak':('assets/hashem-almubarak.jpeg','assets/sifiapp_logo.jpeg')}
P_=H+'Graduates/index.html'; s=open(P_,encoding='utf-8').read()
i=s.index('const DATA = ')+len('const DATA = '); j=s.index('\nconst SITE_STATS')
D=json.loads(s[i:j].rstrip()[:-1]); g=D['grads']; N0=len(g); assert N0==3913,N0
head=s[:i]; tail=s[j:]
T0=collections.Counter(r['tr'] for r in g); wl0=sum(1 for r in g if r.get('links')); uu0=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
X_=H+'Graduates/Graduates_Database.xlsx'; wb=openpyxl.load_workbook(X_); ws=wb['قاعدة البيانات']; assert ws.cell(N0+1,1).value==N0
norm=lambda u:re.sub(r'^https?://(www\.|[a-z]{2}\.)?','',u).rstrip('/').lower()
ALL={norm(l[1]) for r in g for l in r['links']}
def note(k,t):
    g[k-1]['d']=(g[k-1]['d']+' '+TAG+t).strip(); ws.cell(k+1,21).value=((ws.cell(k+1,21).value or '')+' '+TAG+t).strip()
def addlink(k,label,url):
    G=g[k-1]
    if any(norm(l[1])==norm(url) for l in G['links']): return False
    assert norm(url) not in ALL,('link on another record',k,url)
    G['links'].append([label,url]); ALL.add(norm(url)); col=15 if 'linkedin.com/in/' in url else 16
    cur=ws.cell(k+1,col).value; ws.cell(k+1,col).value=(cur+' · ' if cur else '')+url; return True
LOG=collections.Counter(); new_ids=[]
exist_en={(r.get('en') or '').lower().replace(' ','') for r in g}
for ar,en,links,prog,co,tr,score,d,emp,role in new:
    assert en.lower().replace(' ','') not in exist_en,('dup en',en)
    for l in links: assert norm(l[1]) not in ALL,(en,l)
    rid=len(g)+1; rr=rid+1; dd=TAG+d+TL
    rec={"n":ar,"en":en,"lv":"li1028b","score":score,"prog":prog,"co":co,"win":"ضمن النطاق","edu":"","emp":emp,"role":role,"cats":["program"],"d":dd,"links":links,"src":"LinkedIn (حساب مسجَّل) — بحث المنشورات «SDAIA Academy» + منشورات تذكر صفحة SDAIA Academy، آخر أسبوع — جولة 28 أكتوبر 2026 (هـ)","tr":tr}
    g.append(rec); new_ids.append(rid); exist_en.add(en.lower().replace(' ',''))
    for l in links: ALL.add(norm(l[1]))
    lic=' · '.join(u for _,u in links if 'linkedin.com/in/' in u) or None
    vals=[rid,ar,en,prog,TRN[tr],co,emp or None,role or None,None,None,'li1028b',score,'ضمن النطاق','برنامج',lic,None,None,None,None,None,dd,None,rec['src']]
    for ci,v in enumerate(vals,1): ws.cell(rr,ci).value=v
for e in enr:
    k=e['k']; G=g[k-1]
    for lab,u in e.get('links',[]):
        if addlink(k,lab,u): LOG['link']+=1
    if e.get('prog_add') and e['prog_add'] not in G['prog']: G['prog']+=' + '+e['prog_add']; ws.cell(k+1,4).value=G['prog']; LOG['prog_add']+=1
    if e.get('n'): G['n']=e['n']; ws.cell(k+1,2).value=e['n']; G['en']=e['en']; ws.cell(k+1,3).value=e['en']; LOG['name']+=1
    if e.get('co'): G['co']=e['co']; ws.cell(k+1,6).value=e['co']
    if e.get('emp') and not G.get('emp'): G['emp']=e['emp']; G['role']=e['role']; ws.cell(k+1,7).value=e['emp']; ws.cell(k+1,8).value=e['role']; LOG['emp']+=1
    note(k,e['t']); LOG['enr']+=1
for r in g: assert '**' not in r['d']
N=len(g); TT=collections.Counter(r['tr'] for r in g); wl=sum(1 for r in g if r.get('links')); uu=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
dj=H+'SuccessStories/website/js/data.js'; sj=open(dj,encoding='utf-8').read()
lines=sj.split('\n')
for sid,(ph,lg) in IMG.items():
    idx=[n for n,l in enumerate(lines) if l.startswith('  {"id": "%s"'%sid)]; assert len(idx)==1,sid; n=idx[0]; L=lines[n]
    assert os.path.exists(H+'SuccessStories/website/'+ph),ph
    L=L.replace('"photo": null','"photo": "%s"'%ph,1); assert ph in L
    if lg:
        assert os.path.exists(H+'SuccessStories/website/'+lg),lg; assert '"orgLogo"' not in L,sid
        L=re.sub(r'("org": "[^"]*")',r'\1, "orgLogo": "%s"'%lg,L,count=1)
    lines[n]=L; LOG['img']+=1
sj='\n'.join(lines)
print('N',N0,'->',N,{k:(T0[k],TT[k]) for k in TT if T0[k]!=TT[k]},'wl',wl0,wl,'uu',uu0,uu,dict(LOG),'new',new_ids)
if DRY: sys.exit(0)
from PIL import Image
ap=H+'SuccessStories/website/assets/ammar-alsehli.jpeg'; im=Image.open(ap).convert('RGB'); w,h=im.size
im.crop((5,10,w-5,h)).resize((w,w),Image.LANCZOS).save(ap,quality=92)
T=TT; TOT=format(N,','); OTOT=format(N0,',')
head=head.replace(OTOT,TOT); tail=tail.replace(OTOT,TOT)
tail=rep(tail,"{ value: %d, label: 'سجلًا فرديًا',"%N0,"{ value: %d, label: 'سجلًا فرديًا',"%N,1)
EN={'ai':'AI Engineer','ds':'Data Scientist','dmg':'Data Management & Governance','other':'Other / Specialized','genai':'Gen AI Academy','coop':'Cooperative Training (COOP)'}
for k,en in EN.items():
    if T[k]!=T0[k]:
        tail,n=re.subn(r"(en: '%s', value: )%d\b"%(re.escape(en),T0[k]),"\\g<1>%d"%T[k],tail); assert n>=1,k
tail=rrep(tail,r"\{ value: %d,(\s+)label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(wl0,format(uu0,',')),"{ value: %d,\\1label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(wl,format(uu,',')))
tail=rep(tail,"noteEn: '%s unique source links'"%format(uu0,','),"noteEn: '%s unique source links'"%format(uu,','),1)
D['grads']=g; open(P_,'w',encoding='utf-8').write(head+json.dumps(D,ensure_ascii=False)+';'+tail)
P2=H+'index.html'; s=open(P2,encoding='utf-8').read().replace(OTOT,TOT)
s=rep(s,'data-count="%d"'%N0,'data-count="%d"'%N,1)
for k in ('ai','ds','dmg','other','genai','coop'):
    pc='%.1f'%(100*T[k]/N)
    pat=r'(data-count=")%d(">0</div>.*?--w:)[\d.]+(%%.*?data-ar=")[\d.]+(%% من السجل" data-en=")[\d.]+(%% of the registry")'%T0[k]
    s,n=re.subn(pat,lambda mm:mm.group(1)+str(T[k])+mm.group(2)+pc+mm.group(3)+pc+mm.group(4)+pc+mm.group(5),s,count=1,flags=re.S); assert n==1,k
open(P2,'w',encoding='utf-8').write(s)
s=sj.replace(OTOT,TOT)
s=rep(s,"{ value: %d, label: 'خريجًا موثّقًا',"%N0,"{ value: %d, label: 'خريجًا موثّقًا',"%N,1)
for k,en in EN.items():
    if T[k]!=T0[k]: s=rrep(s,r"(en: '%s',\s+value: )%d\b"%(re.escape(en),T0[k]),"\\g<1>%d"%T[k])
s=rep(s,"'use strict';","/* %s: منشورات زوّد بها أ. د. ممدوح العنزي (9 — كلها قائمة فأُثريت) + مسح منشورات الأسبوع — %s ← %s خريجًا (%d جديدان · %d إثراءات)؛ صور 5 قصص وشعارات 4 جهات؛ القصص 212؛ جهات العمل 113. */\n'use strict';"%(DATE,OTOT,TOT,len(new_ids),LOG['enr']),1)
open(dj,'w',encoding='utf-8').write(s)
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
   'تحديث':f'{DATE} — منشورات مزوّدة + مسح الأسبوع: {len(new_ids)} سجلان جديدان ({OTOT} → {TOT})؛ {LOG["enr"]} إثراءات؛ القصص 212؛ جهات العمل 113'}
for row in st.iter_rows():
    if row[0].value in M: row[1].value=M[row[0].value]
sh=wb.create_sheet('جولة_28_أكتوبر_2026_هـ'); sh.sheet_view.rightToLeft=True; sh.append(['#','الاسم','النوع','التفصيل'])
for k in new_ids: sh.append([k,g[k-1]['n'],'سجل جديد (li1028b)',g[k-1]['prog'][:90]+' — '+g[k-1]['co']])
for e in enr: sh.append([e['k'],g[e['k']-1]['n'],'إثراء',e['t'][:200]])
wb.save(X_)
P5=H+'Graduates/Graduates_Database.md'; s=open(P5,encoding='utf-8').read()
s=rrep(s,r'\*\*الإصدار:\*\* ',f'**الإصدار:** {DATE} — منشورات مزوّدة ومسح الأسبوع ({OTOT} → {TOT} · القصص 212 · جهات العمل 113). قبله: ',1)
L=['## منشورات مزوّدة ومسح الأسبوع — %s'%DATE,'',f'**الخريجون {OTOT} → {TOT} · القصص 212 · جهات العمل 113.** المنشورات التسعة التي زوّد بها أ. د. ممدوح العنزي تعود كلها إلى سجلات قائمة فأُثريت (روابط المنشورات، جهات عمل، برامج إضافية)، وصُحّح اسم #3909 إلى «لمى عبدالعزيز بن عسكر» من صورة الشهادة. مسح منشورات الأسبوع أضاف سجلين: #{new_ids[0]} سعود الشباني (أتمتة سير العمل بالذكاء الاصطناعي) و#{new_ids[1]} مها السويد (التدريب التعاوني). إثراء {LOG["enr"]} سجلات، منها #2800 غلا الشريف (+تطوير حلول الذكاء الاصطناعي التوليدي). لا قصص جديدة.','','---','']
k=re.search(r'\n## ',s).start()+1; s=s[:k]+'\n'.join(L)+'\n'+s[k:]; open(P5,'w',encoding='utf-8').write(s)
for f in ('index.html','Graduates/index.html','SuccessStories/website/js/data.js'):
    t=open(H+f,encoding='utf-8').read(); print(f,'leftover',OTOT,t.count(OTOT),'new',t.count(TOT))
print('done',dict(LOG))
