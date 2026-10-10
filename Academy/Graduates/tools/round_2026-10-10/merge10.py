# -*- coding: utf-8 -*-
import json,re,os,sys,shutil,collections
sys.path[:0]=[os.path.expanduser('~/mnt/Academy/Graduates/tools/round_2026-10-07')]
import load,openpyxl
DRY='--apply' not in sys.argv
H=os.path.expanduser('~/mnt/Academy/'); B='backup-2026-10-10c'
DATE='10 أكتوبر 2026'; TAG='[دمج 10 أكتوبر 2026] '
PAIRS=[(2126,2400),(294,469),(301,676),(348,504),(357,520)]
DEL=sorted(b for a,b in PAIRS)
def nid(k):
    if k in DEL: return dict((b,a) for a,b in PAIRS)[k] - sum(1 for x in DEL if x<dict((b,a) for a,b in PAIRS)[k])
    return k-sum(1 for x in DEL if x<k)
def remap(t,N):
    return re.sub(r'#(\d{1,4})(?![0-9A-Fa-f])',lambda m:'#%d'%nid(int(m.group(1))) if 1<=int(m.group(1))<=N else m.group(0),t)
FILES=['SuccessStories/website/js/data.js','index.html','Graduates/index.html','Graduates/Graduates_Database.xlsx','Graduates/Graduates_Database.md','Graduates/SDAIA_Round_2026-10-10.md']
if not DRY:
    for f in FILES:
        a,b=os.path.splitext(H+f); t=f'{a}.{B}{b}'
        if not os.path.exists(t): shutil.copy2(H+f,t)
P=H+'Graduates/index.html'; s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+len('const DATA = '); j=s.index('\nconst SITE_STATS')
D=json.loads(s[i:j].rstrip()[:-1]); g=D['grads']; N0=len(g); assert N0==3332
head=s[:i]; tail=s[j:]
T0=collections.Counter(r['tr'] for r in g); wl0=sum(1 for r in g if r.get('links')); uu0=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
norm=lambda u:re.sub(r'^https?://(www\.|[a-z]{2}\.)?','',u).rstrip('/').lower()
SUM=[]
for a,b in PAIRS:
    A=g[a-1]; Bm=g[b-1]
    assert (A['en'] or A['n']).lower().replace(' ','')[:8]==(Bm['en'] or Bm['n']).lower().replace(' ','')[:8],(a,b)
    old=dict(A)
    if Bm['prog'] and Bm['prog'] not in A['prog']: A['prog']=A['prog']+' + '+Bm['prog']
    if Bm['co'] and Bm['co'] not in A['co']: A['co']=(A['co']+' · ' if A['co'] else '')+Bm['co']
    for f in ('en','edu','emp','role'):
        if not A.get(f) and Bm.get(f): A[f]=Bm[f]
    if A['win']=='غير محدد' and Bm['win']!='غير محدد': A['win']=Bm['win']
    A['score']=max(A['score'],Bm['score'])
    A['cats']=A['cats']+[c for c in Bm['cats'] if c not in A['cats']]
    for l in Bm['links']:
        if not any(norm(x[1])==norm(l[1]) for x in A['links']): A['links'].append(l)
    if Bm['n']!=A['n']:
        al=A.get('alias') or ''; A['alias']=(al+' · ' if al else '')+Bm['n']
    if Bm['src'] and Bm['src'] not in (A['src'] or ''): A['src']=(A['src']+' · ' if A['src'] else '')+Bm['src']
    A['d']=(A['d']+' ' if A['d'] else '')+TAG+f'دُمج فيه السجل #{b} (قبل إعادة الترقيم) «{Bm["n"]}» — {Bm["prog"]} ({Bm["co"]}) بقرار أ. د. ممدوح؛ أُبقي الرقم الأدنى. نص السجل المدموج: '+Bm['d']
    SUM.append((a,b,A['n'],Bm['prog']))
# remove and remap
for b in sorted(DEL,reverse=True): del g[b-1]
for G in g: G['d']=remap(G['d'],N0)
N=len(g); T=collections.Counter(r['tr'] for r in g)
wl=sum(1 for r in g if r.get('links')); uu=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
print('N',N,dict(T),'from',dict(T0),wl0,wl,uu0,uu, 'new ids of 3312..3332:',nid(3317),nid(3332), 'sample remap 2401->',nid(2401))
if DRY: sys.exit(0)
TOT=format(N,','); OTOT=format(N0,',')
head=head.replace(OTOT,TOT); tail=tail.replace(OTOT,TOT)
tail=tail.replace("{ value: %d, label: 'سجلًا فرديًا',"%N0,"{ value: %d, label: 'سجلًا فرديًا',"%N)
for k,en in (('ai','AI Engineer'),('ds','Data Scientist'),('dmg','Data Management & Governance'),('other','Other / Specialized'),('genai','Gen AI Academy')):
    if T[k]!=T0[k]:
        tail,n=re.subn(r"(en: '%s', value: )%d\b"%(re.escape(en),T0[k]),"\\g<1>%d"%T[k],tail); assert n==1,k
tail,n=re.subn(r"\{ value: %d,(\s+)label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(wl0,format(uu0,',')),"{ value: %d,\\1label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(wl,format(uu,',')),tail); assert n==1
tail=tail.replace("noteEn: '%s unique source links'"%format(uu0,','),"noteEn: '%s unique source links'"%format(uu,','))
D['grads']=g; open(P,'w',encoding='utf-8').write(head+json.dumps(D,ensure_ascii=False)+';'+tail)
P2=H+'index.html'; s=open(P2,encoding='utf-8').read(); s=s.replace(OTOT,TOT)
s=s.replace('data-count="%d"'%N0,'data-count="%d"'%N)
for k in ('ai','ds','dmg','other','genai','coop'):
    pc='%.1f'%(100*T[k]/N)
    pat=r'(data-count=")%d(">0</div>.*?--w:)[\d.]+(%%.*?data-ar=")[\d.]+(%% من السجل" data-en=")[\d.]+(%% of the registry")'%T0[k]
    s,n=re.subn(pat,lambda m:m.group(1)+str(T[k])+m.group(2)+pc+m.group(3)+pc+m.group(4)+pc+m.group(5),s,count=1,flags=re.S); assert n==1,k
open(P2,'w',encoding='utf-8').write(s)
P3=H+'SuccessStories/website/js/data.js'; s=open(P3,encoding='utf-8').read()
s=s.replace("{ value: %d, label: 'خريجًا موثّقًا',"%N0,"{ value: %d, label: 'خريجًا موثّقًا',"%N).replace(OTOT,TOT)
for k,en in (('ai','AI Engineer'),('ds','Data Scientist'),('dmg','Data Management & Governance'),('other','Other / Specialized'),('genai','Gen AI Academy')):
    if T[k]!=T0[k]: s,n=re.subn(r"(en: '%s',\s+value: )%d\b"%(re.escape(en),T0[k]),"\\g<1>%d"%T[k],s); assert n==1,k
k0=s.index('const STORIES = ['); e=s.index('\n];',k0); s=s[:k0]+remap(s[k0:e],N0)+s[e:]
s=s.replace('(16 سجلًا جديدًا من GitHub)','(16 سجلًا جديدًا من GitHub؛ ثم دمج 5 أزواج مكررة)')
open(P3,'w',encoding='utf-8').write(s)
# xlsx
X_=H+'Graduates/Graduates_Database.xlsx'; wb=openpyxl.load_workbook(X_); ws=wb['قاعدة البيانات']
assert ws.cell(N0+1,1).value==N0
cols=ws.max_column
for a,b in PAIRS:
    A=g[nid(a)-1]; r=a+1
    ws.cell(r,4).value=A['prog']; ws.cell(r,6).value=A['co']; ws.cell(r,3).value=A['en'] or ws.cell(r,3).value
    ws.cell(r,7).value=A['emp'] or ws.cell(r,7).value; ws.cell(r,12).value=A['score']; ws.cell(r,13).value=A['win']
    rb=b+1
    for c in (15,16):
        vb=ws.cell(rb,c).value
        if vb:
            va=ws.cell(r,c).value or ''
            add=[u for u in vb.split(' · ') if u not in va]
            if add: ws.cell(r,c).value=(va+' · ' if va else '')+' · '.join(add)
    ws.cell(r,21).value=A['d']
for b in sorted(DEL,reverse=True): ws.delete_rows(b+1)
for r in range(2,N+2):
    ws.cell(r,1).value=r-1
    v=ws.cell(r,21).value
    if v and r-1 not in [nid(a) for a,_ in PAIRS]: ws.cell(r,21).value=remap(v,N0)
assert ws.cell(N+1,1).value==N and ws.cell(N+2,1).value in (None,'')
try: ws.auto_filter.ref='A1:%s%d'%(openpyxl.utils.get_column_letter(cols),N+1)
except Exception: pass
sh=wb['جولة_10_أكتوبر_2026']
for row in sh.iter_rows(min_row=2):
    if isinstance(row[0].value,int): row[0].value=nid(row[0].value)
    if isinstance(row[2].value,str): row[2].value=remap(row[2].value,N0)
sm=wb.create_sheet('دمج_2026-10-10'); sm.append(['الرقم الباقي (جديد)','الرقم المدموج (قديم)','الاسم','البرنامج المدموج'])
for a,b,n,p in SUM: sm.append([nid(a),b,n,p])
sm.append([]); sm.append(['جدول إعادة الترقيم: كل رقم قديم أكبر من الرقم المحذوف يُطرح منه عدد المحذوفات الأصغر منه — المحذوفات (قديمة): '+', '.join(map(str,DEL))])
st=wb['إحصاءات']
M={'الإجمالي':TOT,'مهندس ذكاء اصطناعي':T['ai'],'عالم بيانات':T['ds'],'أكاديمية الذكاء الاصطناعي التوليدي':T['genai'],'إدارة وحوكمة البيانات':T['dmg'],'التدريب التعاوني':T['coop'],'برامج متخصصة أخرى':T['other'],'سجلات بروابط تحقق علنية':wl,'روابط مصدر فريدة':uu}
for row in st.iter_rows():
    if row[0].value in M: row[1].value=M[row[0].value]
    if row[0].value=='تحديث': row[1].value=str(row[1].value).replace(OTOT,TOT)+f'؛ ثم دمج 5 أزواج مكررة ({OTOT} → {TOT}) مع إعادة الترقيم'
wb.save(X_)
# md + report: remap today's section only
P5=H+'Graduates/Graduates_Database.md'; s=open(P5,encoding='utf-8').read()
a=s.index('## جولة سد الفجوات والخريجين الجدد والتدقيق — 10 أكتوبر 2026'); b=s.index('## جولة سد الفجوات واستكمال البيانات — 7 أكتوبر 2026')
sec=remap(s[a:b],N0).replace(OTOT,TOT)
k=sec.rindex('---')
SEC=f'**7) الدمج (بقرار أ. د. ممدوح، {DATE}):** دُمجت 5 أزواج وحُذفت مقاعدها وأُعيد ترقيم ما بعدها ({OTOT} → {TOT}): '+' · '.join(f'#{b} القديم ← #{nid(a)} ({n})' for a,b,n,p in SUM)+'. القاعدة: الإبقاء على الرقم الأدنى، ونقل الحقول غير الفارغة، وضم الروابط والفئات، ووضع الاسم الآخر في alias. أُعيدت كتابة إشارات #N في حقول d وحقل provenance في القصص وفي هذا القسم؛ **كل رقم في وثيقة سابقة لهذا الدمج يتبع الترقيم القديم.** صفوف الأقسام التاريخية في هذا الملف لم تُحذف (ترقيمها محلي).\n\n'
sec=sec[:k]+SEC+sec[k:]
s=s[:a]+sec+s[b:]
s=s.replace('(3,316 → %s · القصص 167)'%OTOT,'(3,316 → %s · القصص 167)'%TOT)
open(P5,'w',encoding='utf-8').write(s)
P6=H+'Graduates/SDAIA_Round_2026-10-10.md'; s=open(P6,encoding='utf-8').read()
s=remap(s,N0).replace(OTOT,TOT)+'\n## 5) الدمج (بعد قرارك)\n'+SEC.replace('**7) الدمج','**الدمج')
open(P6,'w',encoding='utf-8').write(s)
json.dump(dict(N=N,T=T,wl=wl,uu=uu,SUM=SUM,DEL=DEL),open('merge_stats.json','w'),ensure_ascii=False)
print('written')
