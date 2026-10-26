# -*- coding: utf-8 -*-
# Round 26 Oct 2026 (b) — final sweep: Qafila capstone forks (Modern Data Engineering), LinkedIn content (past week), gaps, 5 stories, QA.
import json,re,os,sys,shutil,collections,openpyxl,urllib.request
DRY='--apply' not in sys.argv
H=os.path.expanduser('~/mnt/Academy/'); T=H+'Graduates/tools/round_2026-10-26b/'
DATE='26 أكتوبر 2026'; TAG='[جولة 26 أكتوبر 2026 (ب) — المسح الختامي] '
TL=' تنويه: الاسم العربي نقل حرفي عن الاسم اللاتيني المنشور — غير متحقق علنًا.'
TRN={'ai':'مهندس ذكاء اصطناعي — AI Engineer','ds':'عالم بيانات — Data Scientist','other':'برامج متخصصة أخرى — Other / Specialized','dmg':'إدارة وحوكمة البيانات — Data Management & Governance','genai':'أكاديمية الذكاء الاصطناعي التوليدي — Gen AI Academy','coop':'التدريب التعاوني — Cooperative Training (COOP)'}
def rep(s,a,b,count=None):
    n=s.count(a); assert n>=1,('missing',a[:90])
    if count is not None: assert n==count,(a[:90],n)
    return s.replace(a,b)
def rrep(s,pat,b,count=1,flags=0):
    s2,n=re.subn(pat,b,s,flags=flags); assert n==count,(pat,n); return s2
def get(u):
    try: return urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=20).read().decode('utf-8','ignore')
    except Exception: return ''
FILES=['SuccessStories/website/js/data.js','SuccessStories/website/index.html','index.html','Graduates/index.html','Graduates/Graduates_Database.xlsx','Graduates/Graduates_Database.md']
BK=H+'_backups/2026-10-26b/'
if not DRY:
    os.makedirs(BK,exist_ok=True)
    for f in FILES:
        t=BK+f.replace('/','__')
        if not os.path.exists(t): shutil.copy2(H+f,t)
X=json.load(open(T+'data26b.json',encoding='utf-8')); F={f['owner']:f for f in json.load(open(T+'forks.json'))}
P=H+'Graduates/index.html'; s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+len('const DATA = '); j=s.index('\nconst SITE_STATS')
D=json.loads(s[i:j].rstrip()[:-1]); g=D['grads']; N0=len(g); assert N0==3847,N0
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
    G['links'].append([label,url]); ALL.add(norm(url)); col=15 if 'linkedin.com' in url else 16
    cur=ws.cell(k+1,col).value; ws.cell(k+1,col).value=(cur+' · ' if cur else '')+url; return True
def progadd(k,pa):
    if pa in g[k-1]['prog']: return
    g[k-1]['prog']+=' + '+pa; ws.cell(k+1,4).value=g[k-1]['prog']
new_ids=[]; LOG=collections.Counter()
exist_en={(r.get('en') or '').lower().replace(' ','') for r in g}
def add(ar,en,prog,co,tr,score,lv,links,src,d,cats=('program','project')):
    assert en.lower().replace(' ','') not in exist_en or en in X['xnote'],('dup en',en)
    for l in links: assert norm(l[1]) not in ALL,(en,l)
    rid=len(g)+1; rr=rid+1
    rec={"n":ar,"en":en,"lv":lv,"score":score,"prog":prog,"co":co,"win":"ضمن النطاق","edu":"","emp":"","role":"","cats":list(cats),"d":TAG+d,"links":links,"src":src,"tr":tr}
    g.append(rec); new_ids.append(rid); exist_en.add(en.lower().replace(' ',''))
    for l in links: ALL.add(norm(l[1]))
    li=' · '.join(l[1] for l in links if 'linkedin.com' in l[1]) or None; gh=' · '.join(l[1] for l in links if 'github.com' in l[1]) or None
    catl={'program':'برنامج','project':'مشروع','cert':'شهادة'}
    vals=[rid,ar,en,prog,TRN[tr],co,None,None,None,None,lv,score,'ضمن النطاق',' · '.join(catl[c] for c in cats),li,gh,None,None,None,None,TAG+d,None,src]
    for ci,v in enumerate(vals,1): ws.cell(rr,ci).value=v
# ---- Qafila capstone forks ----
DE='هندسة البيانات الحديثة لأنظمة الذكاء الاصطناعي (Modern Data Engineering for AI Systems) — مشروع «قافلة» الختامي — أكاديمية سدايا'
for o,ar,en,li in X['qafila']:
    f=F[o]; links=[['GitHub (مشروع قافلة)','https://github.com/'+f['full']],['GitHub','https://github.com/'+o]]
    if li: links.append(['LinkedIn',li])
    sb=(f.get('submitted') or '').strip()
    ev=f"نسخة (fork) من مستودع الأكاديمية «SDAIAAcademy/qafila-margin-project» — المشروع الختامي لبرنامج هندسة البيانات الحديثة، أُنشئت {f['created']}"
    ev+=(f"، وسطر «Submitted by» في ملف README مملوء: «{re.sub(r'[*`<>]','',sb.split(' — ')[0].split(' – ')[0]).strip()}»" if '<your name>' not in sb else f"، والاسم من الاسم المعروض على GitHub «{f.get('pname')}»")
    ev+='، مع إيداعات من صاحب الحساب.' if o in ' '.join(f.get('commit_authors',[])) else '.'
    ev+=' '+X['xnote'].get(en,'')
    add(ar,en,DE,'أكتوبر 2026 (تسليم مشروع «قافلة»، 21–22 أكتوبر 2026)','ds',80 if li else 75,'gh1026',links,'GitHub — نسخ مستودع SDAIAAcademy/qafila-margin-project (جولة 26 أكتوبر 2026 ب)',ev.strip()+TL)
# ---- deep research late submitter ----
o,ar,en=X['deep']; f=F[o]
add(ar,en,'مشروع «وكيل البحث العميق» (Deep Research Agent — LangGraph) — أكاديمية سدايا','سبتمبر 2026 (إنشاء نسخة المشروع 15 سبتمبر 2026)','ai',72,'gh1026',[['GitHub (المشروع)','https://github.com/'+f['full']],['GitHub','https://github.com/'+o]],'GitHub — نسخ مستودع SDAIAAcademy/deep-research-agent-langgraph-project',f"نسخة من مستودع الأكاديمية أُنشئت {f['created']}، وسطر «Submitted by» مملوء: «Norah ALShahrani»، مع إيداعات من صاحب الحساب. "+X['xnote'][en]+TL)
# ---- LinkedIn posts ----
for ar,en,prog,co,tr,li,d,tl in X['li']:
    add(ar,en,prog,co,tr,80,'li1026',[['LinkedIn',li]],'LinkedIn (حساب مسجَّل) — بحث المنشورات «SDAIA Academy» / «SDAIA certificate»، آخر أسبوع (26 أكتوبر 2026)',d+(' '+X['xnote'][en] if en in X['xnote'] else '')+(TL if tl else ''),('program','cert'))
# ---- existing qafila forkers: add programme only with filled Submitted-by + owner commit ----
for o,k in (('Moashehri',3205),('NoufHar',3304),('dee2002al-c',3330),('Ahmed-Bah',3373)):
    f=F[o]; rd=get(f"https://raw.githubusercontent.com/{f['full']}/{f['branch']}/README.md"); m=re.search(r'Submitted by:?\s*(.+)',rd); sb=m.group(1).strip() if m else ''
    at=get(f"https://github.com/{f['full']}/commits/{f['branch']}.atom"); own=o.lower() in at.lower()
    assert any(('github.com/'+o.lower()) in u.lower() for _,u in g[k-1]['links']),(o,k)
    if sb and '<your name>' not in sb and own:
        progadd(k,'هندسة البيانات الحديثة — مشروع «قافلة» الختامي (أكتوبر 2026)'); addlink(k,'GitHub (مشروع قافلة)','https://github.com/'+f['full'])
        note(k,f"نسخة من مشروع «قافلة» (هندسة البيانات الحديثة) أُنشئت {f['created']}، و«Submitted by»: «{re.sub(r'[*`<>]','',sb.split(' — ')[0])[:60]}»، مع إيداعات من صاحب الحساب."); LOG['qafila_existing']+=1
    else: print('qafila existing not credited',o,k,bool(sb),own)
# ---- enrichments ----
for e in X['enr']:
    k=e['k']
    for lab,u in e.get('links',[]):
        if addlink(k,lab,u): LOG['link']+=1
    if e.get('prog_add'): progadd(k,e['prog_add']); LOG['prog_add']+=1
    if e.get('alias'):
        cur=g[k-1].get('alias') or ''
        if e['alias'] not in cur: g[k-1]['alias']=(cur+' · ' if cur else '')+e['alias']
    if e.get('co_append') and not re.search(r'20\d\d',g[k-1]['co']):
        g[k-1]['co']=(g[k-1]['co']+' · ' if g[k-1]['co'] else '')+e['co_append']; ws.cell(k+1,6).value=g[k-1]['co']; LOG['co']+=1
    note(k,e['t']); LOG['enr']+=1
# ---- gap: cohort year for official-file records whose cohort lacks a year but whose programme field carries the programme date ----
MON={'jan':'يناير','feb':'فبراير','mar':'مارس','apr':'أبريل','may':'مايو','jun':'يونيو','jul':'يوليو','aug':'أغسطس','sep':'سبتمبر','oct':'أكتوبر','nov':'نوفمبر','dec':'ديسمبر'}
GAPCO=[]
for k,r in enumerate(g,1):
    if k in new_ids or re.search(r'20(2\d)',r.get('co') or ''): continue
    m=re.findall(r'(?:practi\w*|bootcamps?|LLMs?|Cerificate|Certificates?)[^,;+]{0,30},?\s*(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s*(20(?:2[1-6]))',r['prog'],re.I)
    if not m: continue
    m23=[x for x in m if x[1]=='2023' and 'مجموعة' in (r.get('co') or '')]; mon,yr=(m23 or m)[0]; val=f"{MON[mon[:3].lower()]} {yr} (تاريخ البرنامج كما في حقل البرنامج)"
    r['co']=((r['co']+' · ') if (r.get('co') or '').strip() not in ('','—','غير معروفة') else '')+val; ws.cell(k+1,6).value=r['co']; GAPCO.append(k)
LOG['co_gap']=len(GAPCO)
# ---- stories ----
dj=H+'SuccessStories/website/js/data.js'; sj=open(dj,encoding='utf-8').read()
stories=[]; LI='https://www.linkedin.com/in/'
for p in X['stories']:
    G=g[p['i']-1]; assert G['en'].lower()==p['nameEn'].lower(),(p['i'],G['en']); assert ('"id": "%s"'%p['id']) not in sj
    st={"id":p['id'],"year":p['year'],"quote":{"text":p['quote'],"textEn":p['quoteEn'],"kind":"draft"},"name":p['name'],"nameEn":p['nameEn'],"photo":None,"role":p['role'],"org":p['org'],"orgLogo":p['orgLogo'],"program":p['program'],"period":p['period'],"category":"employment","categories":["employment"],"impact":p['impact'],"story":p['story'],"achievements":p['ach'],"links":[{"label":"LinkedIn","url":LI+p['slug']+'/'}],"provenance":f"صفحة الخبرة على LinkedIn بحساب مسجَّل (قُرئت {DATE})، بتواريخ بمستوى الشهر: {p['exp']} + سجل الأكاديمية #{p['i']}."}
    if st['orgLogo'] is None: del st['orgLogo']
    else: assert os.path.exists(H+'SuccessStories/website/'+st['orgLogo']),st['orgLogo']
    for t in (p['quote'],p['quoteEn']): assert len(t)<=100,t
    stories.append(st)
    if 'job' not in G['cats']: G['cats'].append('job')
    note(p['i'],p['note'])
orgs0=set(re.findall(r'"org": "([^"]+)"',sj)); newemp=sorted({p['org'] for p in X['stories']}-orgs0)
N=len(g); TT=collections.Counter(r['tr'] for r in g); wl=sum(1 for r in g if r.get('links')); uu=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
for t in [json.dumps(x,ensure_ascii=False) for x in stories]+[r['d'] for r in g]: assert '**' not in t
S0=199; S1=S0+len(stories); E0=108; E1=E0+len(newemp)
print('N',N0,'->',N,{k:(T0[k],TT[k]) for k in TT},'wl',wl0,wl,'uu',uu0,uu,dict(LOG),'new',new_ids[0],'-',new_ids[-1],'stories',S1,'emp',E1,newemp)
if DRY: sys.exit(0)
T=TT; TOT=format(N,','); OTOT=format(N0,',')
def stc(t):
    t=t.replace(OTOT,TOT)
    for a,b in (('%d قصة'%S0,'%d قصة'%S1),('%d stories'%S0,'%d stories'%S1),('%d verified success stories'%S0,'%d verified success stories'%S1),('%d جهة عمل'%E0,'%d جهة عمل'%E1),('%d employers'%E0,'%d employers'%E1)):
        t=t.replace(a,b)
    return t
head=stc(head); tail=stc(tail)
tail=rep(tail,"{ value: %d, label: 'سجلًا فرديًا',"%N0,"{ value: %d, label: 'سجلًا فرديًا',"%N,1)
EN={'ai':'AI Engineer','ds':'Data Scientist','dmg':'Data Management & Governance','other':'Other / Specialized','genai':'Gen AI Academy','coop':'Cooperative Training (COOP)'}
for k,en in EN.items():
    if T[k]!=T0[k]:
        tail,n=re.subn(r"(en: '%s', value: )%d\b"%(re.escape(en),T0[k]),"\\g<1>%d"%T[k],tail); assert n>=1,k
tail=rrep(tail,r"\{ value: %d,(\s+)label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(wl0,format(uu0,',')),"{ value: %d,\\1label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(wl,format(uu,',')))
tail=rep(tail,"noteEn: '%s unique source links'"%format(uu0,','),"noteEn: '%s unique source links'"%format(uu,','),1)
tail,n=re.subn(r"(\{ value: )%d(,\s+label: 'قصة نجاح)"%S0,r"\g<1>%d\2"%S1,tail); print('grad story kpi',n)
D['grads']=g; open(P,'w',encoding='utf-8').write(head+json.dumps(D,ensure_ascii=False)+';'+tail)
P2=H+'index.html'; s=stc(open(P2,encoding='utf-8').read())
s=rep(s,'data-count="%d"'%N0,'data-count="%d"'%N,1); s=rep(s,'data-count="%d"'%S0,'data-count="%d"'%S1,1)
if E1!=E0: s=rep(s,'data-count="%d"'%E0,'data-count="%d"'%E1,1)
for k in ('ai','ds','dmg','other','genai','coop'):
    pc='%.1f'%(100*T[k]/N)
    pat=r'(data-count=")%d(">0</div>.*?--w:)[\d.]+(%%.*?data-ar=")[\d.]+(%% من السجل" data-en=")[\d.]+(%% of the registry")'%T0[k]
    s,n=re.subn(pat,lambda mm:mm.group(1)+str(T[k])+mm.group(2)+pc+mm.group(3)+pc+mm.group(4)+pc+mm.group(5),s,count=1,flags=re.S); assert n==1,k
open(P2,'w',encoding='utf-8').write(s)
s=sj
s=rep(s,"{ value: %d, label: 'خريجًا موثّقًا',"%N0,"{ value: %d, label: 'خريجًا موثّقًا',"%N,1)
for k,en in EN.items():
    if T[k]!=T0[k]: s=rrep(s,r"(en: '%s',\s+value: )%d\b"%(re.escape(en),T0[k]),"\\g<1>%d"%T[k])
s=rrep(s,r"(\{ value: )%d(,\s+label: 'قصة نجاح)"%S0,r"\g<1>%d\2"%S1)
if E1!=E0: s=rrep(s,r"(\{ value: )%d(,\s+label: 'جهة عمل')"%E0,r"\g<1>%d\2"%E1)
k=s.index('const STORIES = ['); e=s.index('\n];',k); prev=s[:e].rstrip()
if not prev.endswith(','): prev+=','
s=prev+'\n'+',\n'.join('  '+json.dumps(x,ensure_ascii=False) for x in stories)+s[e:]
# gap: wire the Ministry of Commerce logo on the existing story that lacked it
m=re.search(r'\{"id": "[^"]+"[^\n]*"org": "وزارة التجارة"(?!, "orgLogo")[^\n]*',s)
if m and '"orgLogo"' not in m.group(0): s=s.replace(m.group(0),m.group(0).replace('"org": "وزارة التجارة"','"org": "وزارة التجارة", "orgLogo": "assets/moc.png"',1),1); LOG['moc_logo']=1
s=rep(s,"'use strict';","/* %s (ب): المسح الختامي — %s ← %s خريجًا (%d جديدًا · %d إثراء)؛ القصص %d؛ جهات العمل %d. */\n'use strict';"%(DATE,OTOT,TOT,len(new_ids),LOG['enr'],S1,E1),1)
open(dj,'w',encoding='utf-8').write(s)
P4=H+'SuccessStories/website/index.html'; t=open(P4,encoding='utf-8').read(); t=rep(t,'"numberOfItems": %d'%S0,'"numberOfItems": %d'%S1,1); open(P4,'w',encoding='utf-8').write(t)
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
   'تحديث':f'{DATE} (ب) — المسح الختامي: {len(new_ids)} سجلًا جديدًا ({OTOT} → {TOT})؛ {LOG["enr"]} إثراء؛ {len(GAPCO)} دفعة مكمَّلة؛ القصص {S1}؛ جهات العمل {E1}'}
for row in st.iter_rows():
    if row[0].value in M: row[1].value=M[row[0].value]
sh=wb.create_sheet('جولة_26_أكتوبر_2026_ب'); sh.sheet_view.rightToLeft=True; sh.append(['#','الاسم','النوع','التفصيل'])
for k in new_ids: sh.append([k,g[k-1]['n'],'سجل جديد ('+g[k-1]['lv']+')',g[k-1]['prog'][:90]+' — '+g[k-1]['co']])
for e in X['enr']: sh.append([e['k'],g[e['k']-1]['n'],'إثراء/فحص قصة',e['t'][:200]])
for p in X['stories']: sh.append([p['i'],p['name'],'قصة جديدة',p['org']+' — '+p['role']])
for k in GAPCO: sh.append([k,g[k-1]['n'],'سد فجوة الدفعة',g[k-1]['co']])
wb.save(X_)
P5=H+'Graduates/Graduates_Database.md'; s=open(P5,encoding='utf-8').read()
s=rep(s,'**الإصدار:** %s — '%DATE,'**الإصدار:** %s (ب) — المسح الختامي (%s → %s · القصص %d · جهات العمل %d). قبله: %s — '%(DATE,OTOT,TOT,S1,E1,DATE),1)
L=['## المسح الختامي — %s (ب)'%DATE,'',f'**الخريجون {OTOT} → {TOT} · القصص {S1} · جهات العمل {E1}.** السجلات الجديدة #{new_ids[0]}–#{new_ids[-1]}: 28 من مشروع «قافلة» الختامي لهندسة البيانات الحديثة، و1 من مشروع وكيل البحث العميق، و7 من منشورات LinkedIn. إثراء {LOG["enr"]} سجلًا، وتكميل سنة الدفعة لـ{len(GAPCO)} سجلًا من حقل البرنامج. القصص الجديدة: '+' · '.join(p['id'] for p in X['stories'])+'.','','---','']
k=re.search(r'\n## ',s).start()+1; s=s[:k]+'\n'.join(L)+'\n'+s[k:]; open(P5,'w',encoding='utf-8').write(s)
for f in ('index.html','Graduates/index.html'):
    t=open(H+f,encoding='utf-8').read(); print(f,'leftover',OTOT,t.count(OTOT),'new',t.count(TOT))
print('done',dict(LOG))
