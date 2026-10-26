# -*- coding: utf-8 -*-
# Round 26 Oct 2026 — four Academy files (COOP 1446/1447 acceptance lists, LLM-Pro NVIDIA Apr–May 2026, NVIDIA cert cohort 4).
# Input: plan26.json (no personal IDs/phones/emails/DOB/GPA). Dry run by default; --apply writes.
import json,re,os,sys,shutil,collections,openpyxl
DRY='--apply' not in sys.argv
H=os.path.expanduser('~/mnt/Academy/'); T=H+'Graduates/tools/round_2026-10-26/'
DATE='26 أكتوبر 2026'; TAG='[جولة 26 أكتوبر 2026 — ملفات الأكاديمية] '
TRN={'ai':'مهندس ذكاء اصطناعي — AI Engineer','ds':'عالم بيانات — Data Scientist','other':'برامج متخصصة أخرى — Other / Specialized','dmg':'إدارة وحوكمة البيانات — Data Management & Governance','genai':'أكاديمية الذكاء الاصطناعي التوليدي — Gen AI Academy','coop':'التدريب التعاوني — Cooperative Training (COOP)'}
def rep(s,a,b,count=None):
    n=s.count(a); assert n>=1,('missing',a[:90])
    if count is not None: assert n==count,(a[:90],n)
    return s.replace(a,b)
def rrep(s,pat,b,count=1,flags=0):
    s2,n=re.subn(pat,b,s,flags=flags); assert n==count,(pat,n); return s2
FILES=['SuccessStories/website/js/data.js','SuccessStories/website/index.html','index.html','Graduates/index.html','Graduates/Graduates_Database.xlsx','Graduates/Graduates_Database.md']
BK=H+'_backups/2026-10-26/'
if not DRY:
    os.makedirs(BK,exist_ok=True)
    for f in FILES:
        t=BK+f.replace('/','__')
        if not os.path.exists(t): shutil.copy2(H+f,t)
P=H+'Graduates/index.html'; s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+len('const DATA = '); j=s.index('\nconst SITE_STATS')
D=json.loads(s[i:j].rstrip()[:-1]); g=D['grads']; N0=len(g); assert N0==3566,N0
head=s[:i]; tail=s[j:]
T0=collections.Counter(r['tr'] for r in g); wl0=sum(1 for r in g if r.get('links')); uu0=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
X_=H+'Graduates/Graduates_Database.xlsx'; wb=openpyxl.load_workbook(X_); ws=wb['قاعدة البيانات']
assert ws.cell(N0+1,1).value==N0
PL=json.load(open(T+'plan26.json',encoding='utf-8'))
# ---- enrichment (never overwrite non-empty fields) ----
LOG=collections.Counter()
for ks,e in PL['enr'].items():
    k=int(ks); G=g[k-1]; rr=k+1
    t=TAG+' '.join(e['notes'])
    G['d']=(G['d']+' '+t).strip(); ws.cell(rr,21).value=((ws.cell(rr,21).value or '')+' '+t).strip()
    for pa in e['prog_add']:
        G['prog']+=' + '+pa; ws.cell(rr,4).value=G['prog']; LOG['prog_add']+=1
    if e.get('edu') and not (G.get('edu') or '').strip():
        G['edu']=e['edu']; ws.cell(rr,10).value=e['edu']; LOG['edu']+=1
    if e.get('co') and not (G.get('co') or '').strip() in ('',):
        pass
    if e.get('co') and (G.get('co') or '').strip() in ('','—','غير معروفة'):
        G['co']=e['co']; ws.cell(rr,6).value=e['co']; LOG['co']+=1
    if e.get('alias'):
        cur=G.get('alias') or ''
        if e['alias'] not in cur: G['alias']=(cur+' · ' if cur else '')+e['alias']; LOG['alias']+=1
    for sc in e.get('srcs',[]):
        if sc not in (G.get('src') or ''):
            G['src']=((G.get('src') or '')+' · '+sc).strip(' ·'); ws.cell(rr,23).value=G['src']
    LOG['enr']+=1
# ---- new records ----
new_ids=[]
exist={(r['n'] or '').replace(' ','') for r in g}
for x in PL['new']:
    assert x['tr'] in TRN
    assert x['ar'].replace(' ','') not in exist,('exact dup',x['ar'])
    rid=len(g)+1; rr=rid+1; dd=TAG+x['d']
    rec={"n":x['ar'],"en":x['en'],"lv":x['lv'],"score":x['score'],"prog":x['prog'],"co":x['co'],"win":"ضمن النطاق","edu":x['edu'],"emp":"","role":"","cats":["program"],"d":dd,"links":[],"src":x['src'],"tr":x['tr']}
    g.append(rec); new_ids.append(rid); exist.add(x['ar'].replace(' ',''))
    vals=[rid,x['ar'],x['en'] or None,x['prog'],TRN[x['tr']],x['co'],None,None,None,x['edu'] or None,x['lv'],x['score'],'ضمن النطاق','برنامج',None,None,None,None,None,None,dd,None,x['src']]
    for ci,v in enumerate(vals,1): ws.cell(rr,ci).value=v
N=len(g); TT=collections.Counter(r['tr'] for r in g)
wl=sum(1 for r in g if r.get('links')); uu=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
blob=json.dumps(g,ensure_ascii=False)
assert '**' not in ''.join(r['d'] for r in g[-len(new_ids):])
assert not re.search(r'\b[12]\d{9}\b',json.dumps([g[k-1] for k in new_ids]+[g[int(k)-1] for k in PL['enr']],ensure_ascii=False)),'ID-like number'
print('N',N0,'->',N,{k:(T0[k],TT[k]) for k in TT},'wl',wl0,wl,'uu',uu0,uu,dict(LOG),'new ids',new_ids[0],'-',new_ids[-1])
if DRY: sys.exit(0)
T=TT; S0=S1=199; TOT=format(N,','); OTOT=format(N0,',')
def stc(t): return t.replace(OTOT,TOT)
head=stc(head); tail=stc(tail)
tail=rep(tail,"{ value: %d, label: 'سجلًا فرديًا',"%N0,"{ value: %d, label: 'سجلًا فرديًا',"%N,1)
EN={'ai':'AI Engineer','ds':'Data Scientist','dmg':'Data Management & Governance','other':'Other / Specialized','genai':'Gen AI Academy','coop':'Cooperative Training (COOP)'}
for k,en in EN.items():
    if T[k]!=T0[k]:
        tail,n=re.subn(r"(en: '%s', value: )%d\b"%(re.escape(en),T0[k]),"\\g<1>%d"%T[k],tail); print('tail',k,n); assert n>=1
D['grads']=g; open(P,'w',encoding='utf-8').write(head+json.dumps(D,ensure_ascii=False)+';'+tail)
P2=H+'index.html'; s=stc(open(P2,encoding='utf-8').read())
s=rep(s,'data-count="%d"'%N0,'data-count="%d"'%N,1)
for k in ('ai','ds','dmg','other','genai','coop'):
    pc='%.1f'%(100*T[k]/N)
    pat=r'(data-count=")%d(">0</div>.*?--w:)[\d.]+(%%.*?data-ar=")[\d.]+(%% من السجل" data-en=")[\d.]+(%% of the registry")'%T0[k]
    s,n=re.subn(pat,lambda mm:mm.group(1)+str(T[k])+mm.group(2)+pc+mm.group(3)+pc+mm.group(4)+pc+mm.group(5),s,count=1,flags=re.S); assert n==1,k
open(P2,'w',encoding='utf-8').write(s)
P3=H+'SuccessStories/website/js/data.js'; s=open(P3,encoding='utf-8').read()
s=rep(s,"{ value: %d, label: 'خريجًا موثّقًا',"%N0,"{ value: %d, label: 'خريجًا موثّقًا',"%N,1)
for k,en in EN.items():
    if T[k]!=T0[k]: s=rrep(s,r"(en: '%s',\s+value: )%d\b"%(re.escape(en),T0[k]),"\\g<1>%d"%T[k])
s=rep(s,"'use strict';","/* %s: ملفات الأكاديمية الأربعة (التعاوني 1446/1447 · LLM-Pro إنفيديا أبريل–مايو 2026 · شهادات NVIDIA الدفعة 4) — %s ← %s خريجًا (%d جديدًا · %d إثراء)؛ القصص %d. */\n'use strict';"%(DATE,OTOT,TOT,len(new_ids),LOG['enr'],S1),1)
open(P3,'w',encoding='utf-8').write(s)
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
   'تحديث':f'{DATE} — ملفات الأكاديمية الأربعة: {len(new_ids)} سجلًا جديدًا ({OTOT} → {TOT})؛ {LOG["enr"]} إثراء؛ القصص {S1}'}
for row in st.iter_rows():
    if row[0].value in M: row[1].value=M[row[0].value]
sh=wb.create_sheet('جولة_26_أكتوبر_2026'); sh.append(['#','الاسم','النوع','التفصيل'])
for k in new_ids: sh.append([k,g[k-1]['n'],'سجل جديد ('+g[k-1]['tr']+')',g[k-1]['prog']+' — '+g[k-1]['co']])
for ks in PL['enr']: sh.append([int(ks),g[int(ks)-1]['n'],'إثراء',' '.join(PL['enr'][ks]['notes'])[:160]])
for r in PL['review']: sh.append([r.get('k'),r['name'],'للمراجعة — '+r['cat'],r['detail'][:200]])
for r in PL['excluded']: sh.append([None,r['name'],'مستبعد — '+r['reason'],r['src']])
wb.save(X_)
P5=H+'Graduates/Graduates_Database.md'; s=open(P5,encoding='utf-8').read()
s=rep(s,'**الإصدار:** 24 أكتوبر 2026','**الإصدار:** %s — ملفات الأكاديمية الأربعة (%s → %s · القصص %d). قبله: 24 أكتوبر 2026'%(DATE,OTOT,TOT,S1),1)
san=lambda x:(x or '').replace('|','/')
L=['## ملفات الأكاديمية الأربعة — %s'%DATE,'',f'**الخريجون {OTOT} → {TOT} · القصص {S1}.** المصادر: قائمتا قبول التدريب التعاوني 1446هـ و1447هـ، وملف «التدريب الاحترافي للنماذج اللغوية الكبيرة (إنفيديا)» 19 أبريل – 7 مايو 2026، وقائمة «برنامج شهادات NVIDIA — الدفعة 4». لم تُنقل أي هوية وطنية أو جوال أو بريد أو تاريخ ميلاد أو معدل.','',
 f'**سجلات جديدة ({len(new_ids)}):** #{new_ids[0]}–#{new_ids[-1]} — {sum(1 for k in new_ids if g[k-1]["tr"]=="coop")} في مسار التعاوني (مؤكَّدو الالتحاق؛ الإتمام غير مسجّل في الملفات) و{sum(1 for k in new_ids if g[k-1]["tr"]=="genai")} في مسار NVIDIA.','',
 f'**إثراء ({LOG["enr"]} سجلًا):** '+' · '.join('#%s %s'%(k,g[int(k)-1]['n']) for k in PL['enr'])+'.','',
 '**للمراجعة:** %d حالة · **مستبعدون:** %d (اعتذار/غير مقبول/منسحب). التفاصيل في ورقة «جولة_26_أكتوبر_2026» وفي تقرير المطابقة.'%(len(PL['review']),len(PL['excluded'])),'','---','']
k=re.search(r'\n## ',s).start()+1
s=s[:k]+'\n'.join(L)+'\n'+s[k:]
open(P5,'w',encoding='utf-8').write(s)
for f in ('index.html','Graduates/index.html'):
    t=open(H+f,encoding='utf-8').read(); print(f,'leftover',OTOT,t.count(OTOT),'new',t.count(TOT))
print('done')
