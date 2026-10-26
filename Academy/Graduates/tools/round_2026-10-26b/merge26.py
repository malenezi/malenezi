# -*- coding: utf-8 -*-
# 26 Oct 2026 (b): merge 3 confirmed internal duplicates (keep LOWER id), renumber, rewrite #N references, publish remap.
import json,re,os,sys,shutil,collections,openpyxl
DRY='--apply' not in sys.argv
H=os.path.expanduser('~/mnt/Academy/'); DATE='26 أكتوبر 2026'
PAIRS=[(202,399,'الاسم الأول واسم الأب وعائلة «آل مسعود/المسعود»، البرنامج نفسه (NVIDIA)، وتخصص الذكاء الاصطناعي'),
       (249,400,'اسم نادر «هتاف الخديدي/الخضيدي»؛ ملف LLM-Pro الرسمي يحمل الاسم العربي للسجل #249 والإنجليزي للسجل #400 معًا'),
       (212,704,'الاسم الرباعي متطابق «سكينة جعفر علي الرمضان»، ووصف #212 يذكر «Machine Learning Practitioner (SDAIA)»')]
REM=sorted(b for _,b,_ in PAIRS)
def rep(s,a,b,count=None):
    n=s.count(a); assert n>=1,('missing',a[:90])
    if count is not None: assert n==count,(a[:90],n)
    return s.replace(a,b)
def rrep(s,pat,b,count=1,flags=0):
    s2,n=re.subn(pat,b,s,flags=flags); assert n==count,(pat,n); return s2
FILES=['SuccessStories/website/js/data.js','SuccessStories/website/index.html','index.html','Graduates/index.html','Graduates/Graduates_Database.xlsx','Graduates/Graduates_Database.md']
BK=H+'_backups/2026-10-26c/'
if not DRY:
    os.makedirs(BK,exist_ok=True)
    for f in FILES:
        t=BK+f.replace('/','__')
        if not os.path.exists(t): shutil.copy2(H+f,t)
P=H+'Graduates/index.html'; s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+len('const DATA = '); j=s.index('\nconst SITE_STATS')
D=json.loads(s[i:j].rstrip()[:-1]); g=D['grads']; N0=len(g); assert N0==3883,N0
head=s[:i]; tail=s[j:]
T0=collections.Counter(r['tr'] for r in g); wl0=sum(1 for r in g if r.get('links')); uu0=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
X_=H+'Graduates/Graduates_Database.xlsx'; wb=openpyxl.load_workbook(X_); ws=wb['قاعدة البيانات']; assert ws.cell(N0+1,1).value==N0
norm=lambda u:re.sub(r'^https?://(www\.|[a-z]{2}\.)?','',u).rstrip('/').lower()
TAG='[دمج 26 أكتوبر 2026] '
for a,b,why in PAIRS:
    A=g[a-1]; B=g[b-1]; ra=a+1; rb=b+1
    for lab,u in B['links']:
        if not any(norm(u)==norm(x) for _,x in A['links']):
            A['links'].append([lab,u]); col=15 if 'linkedin.com' in u else 16
            cur=ws.cell(ra,col).value; ws.cell(ra,col).value=(cur+' · ' if cur else '')+u
    for c in B['cats']:
        if c not in A['cats']: A['cats'].append(c)
    bp=B['prog']
    for part in [p.strip() for p in bp.split(' + ')]:
        if part and part not in A['prog']: A['prog']+=' + '+part
    ws.cell(ra,4).value=A['prog']
    if not re.search(r'20\d\d',A.get('co') or '') and B.get('co'): A['co']=B['co']; ws.cell(ra,6).value=A['co']
    elif B.get('co') and B['co'] not in A['co'] and re.search(r'20\d\d',B['co']): A['co']+=' · '+B['co']; ws.cell(ra,6).value=A['co']
    for f,col in (('edu',10),('emp',7),('role',8)):
        if not (A.get(f) or '').strip() and (B.get(f) or '').strip(): A[f]=B[f]; ws.cell(ra,col).value=B[f]
    A['score']=max(A.get('score',0),B.get('score',0)); ws.cell(ra,12).value=A['score']
    al=[x for x in (A.get('alias') or '').split(' · ') if x]
    for x in (B['n'],B.get('en')):
        if x and x!=A['n'] and x!=A.get('en') and x not in al: al.append(x)
    A['alias']=' · '.join(al)
    t=f"{TAG}دُمج فيه السجل السابق #{b} «{B['n']}» / «{B.get('en','')}» (أساس الدمج: {why}). وصف السجل المدموج: {B['d']}"
    A['d']=(A['d']+' '+t).strip(); ws.cell(ra,21).value=((ws.cell(ra,21).value or '')+' '+t).strip()
    if B.get('src') and B['src'] not in (A.get('src') or ''): A['src']=((A.get('src') or '')+' · '+B['src']).strip(' ·'); ws.cell(ra,23).value=A['src']
remap=lambda n:n-sum(1 for x in REM if x<n)
MAP={old:remap(old) for old in range(1,N0+1) if old not in REM}
for b in REM: MAP[b]=dict((x,y) for x,y,_ in [(p[1],p[0],0) for p in PAIRS])[b]  # removed ids point to the kept record
def fix(text):
    if not text: return text
    return re.sub(r'#(\d{1,4})\b',lambda m:'#%d'%MAP[int(m.group(1))] if int(m.group(1)) in MAP and int(m.group(1))>=min(REM) else m.group(0),text)
nref=0
for r in g:
    nd=fix(r['d']); nref+=nd!=r['d']; r['d']=nd
g2=[r for k,r in enumerate(g,1) if k not in REM]
for b in sorted(REM,reverse=True): ws.delete_rows(b+1,1)
for k in range(1,len(g2)+1):
    ws.cell(k+1,1).value=k
    for col in (21,22):
        v=ws.cell(k+1,col).value
        if isinstance(v,str): ws.cell(k+1,col).value=fix(v)
assert ws.cell(len(g2)+1,1).value==len(g2) and ws.cell(len(g2)+2,1).value is None
for k,r in enumerate(g2,1): assert (ws.cell(k+1,2).value or '')==r['n'],(k,ws.cell(k+1,2).value,r['n'])
g=g2; N=len(g); T=collections.Counter(r['tr'] for r in g); wl=sum(1 for r in g if r.get('links')); uu=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
dj=H+'SuccessStories/website/js/data.js'; sj=open(dj,encoding='utf-8').read(); sj2=fix(sj); nrefs=sum(1 for a,b in zip(re.findall(r'#\d+',sj),re.findall(r'#\d+',sj2)) if a!=b)
print('N',N0,'->',N,{k:(T0[k],T[k]) for k in T},'wl',wl0,wl,'uu',uu0,uu,'d refs rewritten',nref,'data.js refs',nrefs)
if DRY: sys.exit(0)
TOT=format(N,','); OTOT=format(N0,',')
head=head.replace(OTOT,TOT); tail=tail.replace(OTOT,TOT)
tail=rep(tail,"{ value: %d, label: 'سجلًا فرديًا',"%N0,"{ value: %d, label: 'سجلًا فرديًا',"%N,1)
EN={'ai':'AI Engineer','ds':'Data Scientist','dmg':'Data Management & Governance','other':'Other / Specialized','genai':'Gen AI Academy','coop':'Cooperative Training (COOP)'}
for k,en in EN.items():
    if T[k]!=T0[k]:
        tail,n=re.subn(r"(en: '%s', value: )%d\b"%(re.escape(en),T0[k]),"\\g<1>%d"%T[k],tail); assert n>=1,k
if wl!=wl0 or uu!=uu0:
    tail=rrep(tail,r"\{ value: %d,(\s+)label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(wl0,format(uu0,',')),"{ value: %d,\\1label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(wl,format(uu,',')))
    tail=rep(tail,"noteEn: '%s unique source links'"%format(uu0,','),"noteEn: '%s unique source links'"%format(uu,','),1)
D['grads']=g; open(P,'w',encoding='utf-8').write(head+json.dumps(D,ensure_ascii=False)+';'+tail)
P2=H+'index.html'; s=open(P2,encoding='utf-8').read().replace(OTOT,TOT)
s=rep(s,'data-count="%d"'%N0,'data-count="%d"'%N,1)
for k in ('ai','ds','dmg','other','genai','coop'):
    pc='%.1f'%(100*T[k]/N)
    pat=r'(data-count=")%d(">0</div>.*?--w:)[\d.]+(%%.*?data-ar=")[\d.]+(%% من السجل" data-en=")[\d.]+(%% of the registry")'%T0[k]
    s,n=re.subn(pat,lambda mm:mm.group(1)+str(T[k])+mm.group(2)+pc+mm.group(3)+pc+mm.group(4)+pc+mm.group(5),s,count=1,flags=re.S); assert n==1,k
open(P2,'w',encoding='utf-8').write(s)
s=sj2
s=rep(s,"{ value: %d, label: 'خريجًا موثّقًا',"%N0,"{ value: %d, label: 'خريجًا موثّقًا',"%N,1)
for k,en in EN.items():
    if T[k]!=T0[k]: s=rrep(s,r"(en: '%s',\s+value: )%d\b"%(re.escape(en),T0[k]),"\\g<1>%d"%T[k])
s=rep(s,"'use strict';","/* %s (ج): دمج 3 تكرارات داخلية (#399→#202، #400→#249، #704→#212) وإعادة ترقيم ما بعد #399 — %s ← %s خريجًا. */\n'use strict';"%(DATE,OTOT,TOT),1)
open(dj,'w',encoding='utf-8').write(s)
hi=sum(1 for r in g if r.get('score',0)>=75); mid=sum(1 for r in g if 45<=r.get('score',0)<75); lo=N-hi-mid
yc=collections.Counter()
for r in g:
    ys=set(re.findall(r'20(2[1-6])',r.get('co') or ''))
    if not ys: yc['none']+=1
    for y in ys: yc['20'+y]+=1
st=wb['إحصاءات']
M={'الإجمالي':TOT,'مهندس ذكاء اصطناعي':T['ai'],'عالم بيانات':T['ds'],'أكاديمية الذكاء الاصطناعي التوليدي':T['genai'],'إدارة وحوكمة البيانات':T['dmg'],'التدريب التعاوني':T['coop'],'برامج متخصصة أخرى':T['other'],
   'ثقة مرتفعة (≥75)':hi,'ثقة متوسطة (45–74)':mid,'ثقة منخفضة (<45)':lo,'سجلات بجهة عمل موثّقة':sum(1 for r in g if r.get('emp')),'سجلات بروابط تحقق علنية':wl,'روابط مصدر فريدة':uu,
   'سجلات بدفعة 2021':yc['2021'],'سجلات بدفعة 2022':yc['2022'],'سجلات بدفعة 2023':yc['2023'],'سجلات بدفعة 2024':yc['2024'],'سجلات بدفعة 2025':yc['2025'],'سجلات بدفعة 2026':yc['2026'],'سجلات بلا دفعة محددة':yc['none'],
   'تحديث':f'{DATE} (ج) — دمج 3 تكرارات داخلية وإعادة الترقيم: {OTOT} → {TOT}'}
for row in st.iter_rows():
    if row[0].value in M: row[1].value=M[row[0].value]
sh=wb.create_sheet('دمج_2026-10-26'); sh.sheet_view.rightToLeft=True; sh.append(['الرقم القديم','الرقم الجديد','ملاحظة'])
for a,b,why in PAIRS: sh.append([b,a,'دُمج في السجل الأقدم — '+why])
sh.append(['400–3883','الرقم القديم − 1 (بين 400 و704) أو − 3 (بعد 704)','إزاحة الترقيم بعد حذف الخانات 399 و400 و704'])
wb.save(X_)
P5=H+'Graduates/Graduates_Database.md'; s=open(P5,encoding='utf-8').read()
s=rep(s,'**الإصدار:** %s (ب)'%DATE,'**الإصدار:** %s (ج) — دمج 3 تكرارات داخلية (%s → %s). قبله: %s (ب)'%(DATE,OTOT,TOT,DATE),1)
L=['## دمج التكرارات الداخلية — %s (ج)'%DATE,'',f'**{OTOT} → {TOT}.** أُبقي الرقم الأقدم في كل زوج ونُقلت إليه الروابط والبرامج والاسم البديل وجملة «[دمج]».','','| المحذوف | المُبقى | الأساس |','|---|---|---|']+[f'| #{b} | #{a} | {why} |' for a,b,why in PAIRS]+['',f'**إعادة الترقيم:** الأرقام 401–704 تنقص 1، و705 فما فوق تنقص 3 (القديم → الجديد). كل إشارات «#N» في الأوصاف وفي data.js أُعيدت كتابتها؛ الإشارات في تقارير الجولات المؤرخة قبل اليوم تبقى بالترقيم القديم.','','---','']
k=re.search(r'\n## ',s).start()+1; s=s[:k]+'\n'.join(L)+'\n'+s[k:]; open(P5,'w',encoding='utf-8').write(s)
print('done')
