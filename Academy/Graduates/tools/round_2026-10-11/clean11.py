# -*- coding: utf-8 -*-
# 11 Oct 2026 cleaning round: approved merges (2263→342, 2917→2212) + approved exclusions (194,195,197,198,199,404),
# k-alh fix, cross-notes, story provenance ids, data.js history comments; renumber + remap.
import json,re,os,sys,shutil,collections
import openpyxl
DRY='--apply' not in sys.argv
H=os.path.expanduser('~/mnt/Academy/'); B='backup-2026-10-11b'
DATE='11 أكتوبر 2026'; TAG='[تنظيف 11 أكتوبر 2026] '
PAIRS=[(342,2263),(2212,2917)]
EXCL={194:'موظف في سدايا — البرنامج مستنتج ولا دليل على إتمام برنامج تدريبي',195:'موظفة في سدايا — البرنامج مستنتج ولا دليل على إتمام برنامج تدريبي',197:'لا دليل على الانتساب لبرنامج في الأكاديمية — البرنامج مستنتج',198:'موظفة في سدايا — البرنامج مستنتج ولا دليل على إتمام برنامج تدريبي',199:'موظف في سدايا — البرنامج مستنتج ولا دليل على إتمام برنامج تدريبي',404:'مدرّب NVIDIA DLI معتمد وأستاذ مساعد — مدرّب لا متدرب'}
DEL=sorted([b for a,b in PAIRS]+list(EXCL))
MAP={b:a for a,b in PAIRS}
def nid(k):
    if k in MAP: k=MAP[k]
    if k in EXCL: return None
    return k-sum(1 for x in DEL if x<k)
def remap(t,N):
    def f(m):
        k=int(m.group(1))
        if not 1<=k<=N: return m.group(0)
        n=nid(k); return '#%d'%n if n else '#%d(مستبعد)'%k
    return re.sub(r'#(\d{1,4})(?![0-9A-Fa-f])',f,t)
FILES=['SuccessStories/website/js/data.js','index.html','Graduates/index.html','Graduates/Graduates_Database.xlsx','Graduates/Graduates_Database.md']
if not DRY:
    for f in FILES:
        a,b=os.path.splitext(H+f); t=f'{a}.{B}{b}'
        if not os.path.exists(t): shutil.copy2(H+f,t)
P=H+'Graduates/index.html'; s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+len('const DATA = '); j=s.index('\nconst SITE_STATS')
D=json.loads(s[i:j].rstrip()[:-1]); g=D['grads']; N0=len(g); assert N0==3360
head=s[:i]; tail=s[j:]
T0=collections.Counter(r['tr'] for r in g)
m=re.search(r"\{ value: (\d+),\s+label: 'سجلًا برابط تحقق علني', note: '([\d,]+) رابط مصدر فريد',",tail); wl0=int(m.group(1)); uu0s=m.group(2)
norm=lambda u:re.sub(r'^https?://(www\.|[a-z]{2}\.)?','',u).rstrip('/').lower()
X_=H+'Graduates/Graduates_Database.xlsx'; wb=openpyxl.load_workbook(X_); ws=wb['قاعدة البيانات']
assert ws.cell(N0+1,1).value==N0
def note(k,t):
    g[k-1]['d']+=' '+TAG+t; ws.cell(k+1,21).value=(ws.cell(k+1,21).value or '')+' '+TAG+t
# --- pre-renumber fixes (old ids) ---
G=g[3057-1]; before=len(G['links']); G['links']=[l for l in G['links'] if norm(l[1])!='github.com/k-alh']; assert len(G['links'])==before-1
v=ws.cell(3058,16).value or ''; ws.cell(3058,16).value=' · '.join(u for u in v.split(' · ') if norm(u)!='github.com/k-alh') or None
note(3057,'أُزيل رابط حساب GitHub «k-alh» من هذا السجل: الحساب يعود لزميله Khalid Alhaidary (#3335) وفق جدول فريق مشروع SDA-DSC-112؛ حسابه هو «Naxf1». أُبقي مستودع الفريق «k-alh/Capstone-Project».')
for a in (1686,2615,2836):
    note(a,'إشارة متبادلة: الاسم نفسه «محمد القحطاني» في #3352 (هندسة أنظمة الذكاء الاصطناعي الوكيلي المتقدمة، أكتوبر 2026) — اسم شائع بلا رابط مشترك؛ لا دمج.')
note(3352,'إشارة متبادلة: الاسم نفسه في #1686 و#2615 و#2836 — اسم شائع بلا رابط مشترك؛ لا دمج.')
# --- merges ---
SUM=[]
for a,b in PAIRS:
    A=g[a-1]; Bm=g[b-1]
    if Bm['prog'] and Bm['prog'] not in A['prog']: A['prog']=A['prog']+' + '+Bm['prog']
    if Bm['co'] and Bm['co'] not in A['co']: A['co']=(A['co']+' · ' if A['co'] else '')+Bm['co']
    for f in ('en','edu','emp','role'):
        if not A.get(f) and Bm.get(f): A[f]=Bm[f]
    if A['win']=='غير محدد' and Bm['win']!='غير محدد': A['win']=Bm['win']
    A['score']=max(A['score'],Bm['score']); A['cats']=A['cats']+[c for c in Bm['cats'] if c not in A['cats']]
    for l in Bm['links']:
        if not any(norm(x[1])==norm(l[1]) for x in A['links']): A['links'].append(l)
    names=[x for x in (Bm['n'],Bm.get('en')) if x and x not in (A['n'],A.get('en'))]
    if names:
        al=A.get('alias') or ''; A['alias']=' · '.join([x for x in [al]+names if x])
    if Bm['src'] and Bm['src'] not in (A['src'] or ''): A['src']=(A['src']+' · ' if A['src'] else '')+Bm['src']
    A['d']+=' '+TAG+f'دُمج فيه السجل #{b} (قبل إعادة الترقيم) «{Bm["n"]}» — {Bm["prog"]} ({Bm["co"]}) بقرار أ. د. ممدوح ({DATE})؛ أُبقي الرقم الأدنى. نص السجل المدموج: '+Bm['d']
    SUM.append((a,b,A['n'],Bm['prog']))
# --- exclusions: keep full copies ---
REMOVED=[dict(old_id=k,reason=EXCL[k],**g[k-1]) for k in sorted(EXCL)]
XROWS={k:[ws.cell(k+1,c).value for c in range(1,ws.max_column+1)] for k in sorted(EXCL)}
# --- stories: provenance ids for the 40 stories lacking one (old ids) ---
P3=H+'SuccessStories/website/js/data.js'; js=open(P3,encoding='utf-8').read()
a0=js.index('const STORIES = [')+len('const STORIES = '); b0=js.index('\n];',a0)+2; ST=json.loads(js[a0:b0])
idx=collections.defaultdict(set)
for k,r in enumerate(g,1):
    for l in r['links']: idx[norm(l[1])].add(k)
PROV=0
for x in ST:
    if re.search(r'#\d',x.get('provenance','')): continue
    c=set()
    for l in x.get('links',[]): c|=idx.get(norm(l['url']),set())
    c={nid(k) and k for k in c} - {None}
    c={MAP.get(k,k) for k in c}
    assert len(c)==1,(x['id'],c)
    k=c.pop(); x['provenance']=(x.get('provenance','').rstrip(' .')+' + ' if x.get('provenance') else '')+f'سجل الأكاديمية #{k}.'; PROV+=1
# --- delete + renumber ---
for b in sorted(DEL,reverse=True): del g[b-1]
for r in g: r['d']=remap(r['d'],N0)
for x in ST: x['provenance']=remap(x['provenance'],N0)
N=len(g); assert N==N0-len(DEL)
T=collections.Counter(r['tr'] for r in g)
wl=sum(1 for r in g if r.get('links')); uu=len({l[1].rstrip('/') for r in g for l in (r.get('links') or [])})
print('N',N0,'->',N,{k:(T0[k],T[k]) for k in T},'wl',wl0,'->',wl,'uu',uu0s,'->',uu,'prov',PROV,'new#3335->',nid(3335),'3352->',nid(3352))
if DRY: sys.exit(0)
TOT=format(N,','); OTOT=format(N0,',')
head=head.replace(OTOT,TOT); tail=tail.replace(OTOT,TOT)
tail=tail.replace("{ value: %d, label: 'سجلًا فرديًا',"%N0,"{ value: %d, label: 'سجلًا فرديًا',"%N)
EN={'ai':'AI Engineer','ds':'Data Scientist','dmg':'Data Management & Governance','other':'Other / Specialized','genai':'Gen AI Academy'}
for k,en in EN.items():
    if T[k]!=T0[k]: tail,n=re.subn(r"(en: '%s', value: )%d\b"%(re.escape(en),T0[k]),"\\g<1>%d"%T[k],tail); assert n==1,k
tail,n=re.subn(r"\{ value: %d,(\s+)label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(wl0,uu0s),"{ value: %d,\\1label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(wl,format(uu,',')),tail); assert n==1
tail=tail.replace("noteEn: '%s unique source links'"%uu0s,"noteEn: '%s unique source links'"%format(uu,','))
tail=tail.replace('(جولة الخريجين الجدد 2024–2026','(جولة الخريجين الجدد والتنظيف 2024–2026').replace('(new-graduates round, 2024–2026 focus','(new-graduates and cleaning round, 2024–2026 focus')
D['grads']=g; open(P,'w',encoding='utf-8').write(head+json.dumps(D,ensure_ascii=False)+';'+tail)
P2=H+'index.html'; s=open(P2,encoding='utf-8').read(); s=s.replace(OTOT,TOT)
s=s.replace('(جولة الخريجين الجدد 2024–2026','(جولة الخريجين الجدد والتنظيف 2024–2026').replace('(new-graduates round, 2024–2026 focus','(new-graduates and cleaning round, 2024–2026 focus')
assert s.count('data-count="%d"'%N0)==1; s=s.replace('data-count="%d"'%N0,'data-count="%d"'%N)
for k in ('ai','ds','dmg','other','genai','coop'):
    pc='%.1f'%(100*T[k]/N)
    pat=r'(data-count=")%d(">0</div>.*?--w:)[\d.]+(%%.*?data-ar=")[\d.]+(%% من السجل" data-en=")[\d.]+(%% of the registry")'%T0[k]
    s,n=re.subn(pat,lambda m:m.group(1)+str(T[k])+m.group(2)+pc+m.group(3)+pc+m.group(4)+pc+m.group(5),s,count=1,flags=re.S); assert n==1,k
open(P2,'w',encoding='utf-8').write(s)
# data.js: targeted edits only
js=js[:a0]+'[\n'+',\n'.join('  '+json.dumps(x,ensure_ascii=False) for x in ST)+'\n]'+js[b0:]
assert js.count("{ value: %d, label: 'خريجًا موثّقًا',"%N0)==1
js=js.replace("{ value: %d, label: 'خريجًا موثّقًا',"%N0,"{ value: %d, label: 'خريجًا موثّقًا',"%N)
for k,en in EN.items():
    if T[k]!=T0[k]: js,n=re.subn(r"(en: '%s',\s+value: )%d\b"%(re.escape(en),T0[k]),"\\g<1>%d"%T[k],js); assert n==1,k
js=js.replace('/* 7 أكتوبر 2026: جولة سد الفجوات — 3,360 خريجًا','/* 7 أكتوبر 2026: جولة سد الفجوات — 3,316 خريجًا')
js=js.replace('/* 10 أكتوبر 2026: جولة سد الفجوات والخريجين الجدد — 3,360 خريجًا','/* 10 أكتوبر 2026: جولة سد الفجوات والخريجين الجدد — 3,327 خريجًا (3,328 بعد سجل مزوّد)')
js=js.replace('/* 11 أكتوبر 2026: جولة الخريجين الجدد — 3,360 خريجًا (32 سجلًا جديدًا من GitHub وLinkedIn)؛ القصص 167 دون تغيير. */',
 f'/* 11 أكتوبر 2026: جولة الخريجين الجدد — 3,328 ← 3,360 خريجًا (32 سجلًا جديدًا من GitHub وLinkedIn)؛ ثم جولة التنظيف: دمج زوجين واستبعاد 6 موظفين/مدربين بقرار أ. د. ممدوح (3,360 ← {TOT})؛ ربط 40 قصة برقم سجلها؛ القصص 167 دون تغيير. */')
assert '3,360 خريجًا (7' not in js
open(P3,'w',encoding='utf-8').write(js)
# xlsx
for a,b in PAIRS:
    A=g[nid(a)-1]; r=a+1
    ws.cell(r,4).value=A['prog']; ws.cell(r,6).value=A['co']; ws.cell(r,3).value=A['en'] or ws.cell(r,3).value
    ws.cell(r,7).value=A['emp'] or ws.cell(r,7).value; ws.cell(r,12).value=A['score']; ws.cell(r,13).value=A['win']; ws.cell(r,22).value=A.get('alias') or ws.cell(r,22).value
    rb=b+1
    for c in (15,16,17,18,19,20):
        vb=ws.cell(rb,c).value
        if vb:
            va=ws.cell(r,c).value or ''; add=[u for u in str(vb).split(' · ') if u not in va]
            if add: ws.cell(r,c).value=(va+' · ' if va else '')+' · '.join(add)
    ws.cell(r,21).value=A['d']
for b in sorted(DEL,reverse=True): ws.delete_rows(b+1)
for r in range(2,N+2):
    ws.cell(r,1).value=r-1
    v=ws.cell(r,21).value
    if v: ws.cell(r,21).value=g[r-2]['d'] if r-1 in [nid(a) for a,_ in PAIRS] else remap(v,N0)
    assert (ws.cell(r,2).value or '').strip()==g[r-2]['n'].strip(),(r,ws.cell(r,2).value,g[r-2]['n'])
assert ws.cell(N+1,1).value==N and ws.cell(N+2,1).value in (None,'')
try: ws.auto_filter.ref='A1:%s%d'%(openpyxl.utils.get_column_letter(ws.max_column),N+1)
except Exception: pass
for name in ('جولة_11_أكتوبر_2026',):
    sh=wb[name]
    for row in sh.iter_rows(min_row=2):
        if isinstance(row[0].value,int): row[0].value=nid(row[0].value)
        if isinstance(row[3].value,str): row[3].value=remap(row[3].value,N0)
sm=wb.create_sheet('تنظيف_2026-10-11'); sm.append(['الإجراء','الرقم القديم','الرقم الجديد','الاسم','التفصيل'])
for a,b,n,p in SUM: sm.append(['دمج',b,nid(a),n,'دُمج في #%d (قديم) — %s'%(a,p)])
hdr=[ws.cell(1,c).value for c in range(1,ws.max_column+1)]
for k in sorted(EXCL): sm.append(['استبعاد',k,None,XROWS[k][1],EXCL[k]])
sm.append([]); sm.append(['إعادة الترقيم: كل رقم قديم يُطرح منه عدد المحذوفات الأصغر منه — المحذوفات (قديمة): '+', '.join(map(str,DEL))])
sx=wb.create_sheet('مستبعدون_2026-10-11'); sx.append(['سبب الاستبعاد']+hdr)
for k in sorted(EXCL): sx.append([EXCL[k]]+XROWS[k])
st=wb['إحصاءات']
hi=sum(1 for r in g if r.get('score',0)>=75); mid=sum(1 for r in g if 45<=r.get('score',0)<75); lo=N-hi-mid
emp=sum(1 for r in g if r.get('emp')); yc=collections.Counter()
for r in g:
    ys=set(re.findall(r'20(2[1-6])',r.get('co') or ''))
    if not ys: yc['none']+=1
    for y in ys: yc['20'+y]+=1
M={'الإجمالي':TOT,'مهندس ذكاء اصطناعي':T['ai'],'عالم بيانات':T['ds'],'أكاديمية الذكاء الاصطناعي التوليدي':T['genai'],'إدارة وحوكمة البيانات':T['dmg'],'التدريب التعاوني':T['coop'],'برامج متخصصة أخرى':T['other'],
   'ثقة مرتفعة (≥75)':hi,'ثقة متوسطة (45–74)':mid,'ثقة منخفضة (<45)':lo,'سجلات بجهة عمل موثّقة':emp,'سجلات بروابط تحقق علنية':wl,'روابط مصدر فريدة':uu,
   'سجلات بدفعة 2021':yc['2021'],'سجلات بدفعة 2022':yc['2022'],'سجلات بدفعة 2023':yc['2023'],'سجلات بدفعة 2024':yc['2024'],'سجلات بدفعة 2025':yc['2025'],'سجلات بدفعة 2026':yc['2026'],'سجلات بلا دفعة محددة':yc['none'],
   'تحديث':f'{DATE} — جولة الخريجين الجدد (3,328 → 3,360) ثم التنظيف والتدقيق: دمج زوجين واستبعاد 6 (3,360 → {TOT}) مع إعادة الترقيم؛ القصص 167'}
for row in st.iter_rows():
    if row[0].value in M: row[1].value=M[row[0].value]
wb.save(X_)
# md: remap today's section, add cleaning section
P5=H+'Graduates/Graduates_Database.md'; s=open(P5,encoding='utf-8').read()
a=s.index('## جولة الخريجين الجدد (تركيز 2024–2026) — 11 أكتوبر 2026'); b=s.index('## جولة سد الفجوات والخريجين الجدد والتدقيق والدمج — 10 أكتوبر 2026')
sec=remap(s[a:b],N0)
CL=['## جولة التنظيف والتدقيق — %s'%DATE,'',f'**الخريجون {OTOT} → {TOT} · القصص 167 · جهات العمل 89.** كل الأرقام بعد هذا القسم تتبع الترقيم السابق لهذه الجولة.','',
 '**1) دمج (بقرار أ. د. ممدوح):** '+' · '.join(f'#{b} القديم ← #{nid(a)} ({n})' for a,b,n,p in SUM)+'.',
 '**2) استبعاد (بقرار أ. د. ممدوح، قاعدة «الموظفون والمدربون ليسوا خريجين»):** '+' · '.join(f'#{k} {XROWS[k][1]} — {EXCL[k]}' for k in sorted(EXCL))+'. نُسخها الكاملة محفوظة في ورقة «مستبعدون_2026-10-11».',
 f'**3) تنظيف:** رابطان مكرران داخل سجلات أُزيلا؛ رابط GitHub «k-alh» نُقل من #3057 القديم (نايف الصماري) إلى صاحبه خالد الحيدري؛ إشارات متبادلة لاسم «محمد القحطاني»؛ ربط {PROV} قصة نجاح برقم سجلها في قاعدة البيانات (كل القصص الـ167 مربوطة الآن)؛ تصحيح تعليقات تاريخية في data.js أفسدها استبدال العدد الإجمالي في جولات سابقة.',
 '**4) تدقيق بلا ملاحظات:** لا معرّف LinkedIn ولا حساب GitHub مشترك بين سجلين؛ لا معرّف قصة مكرر؛ كل صور القصص وشعاراتها المشار إليها موجودة؛ تطابق صفوف xlsx مع قاعدة البيانات صفًا بصف؛ العدادات متسقة في البوابة وصفحة الخريجين وموقع القصص والـxlsx.','','---','']
s=s[:a]+'\n'.join(CL)+'\n'+sec+s[b:]
s=s.replace('**الإصدار:** %s — جولة الخريجين الجدد، تركيز 2024–2026 (3,328 → 3,360 · القصص 167).'%DATE,'**الإصدار:** %s — جولة الخريجين الجدد، تركيز 2024–2026 (3,328 → 3,360) ثم التنظيف والتدقيق (3,360 → %s · القصص 167).'%(DATE,TOT))
open(P5,'w',encoding='utf-8').write(s)
json.dump(dict(N=N,T=T,wl=wl,uu=uu,SUM=SUM,DEL=DEL,PROV=PROV,REMOVED=REMOVED),open(H+'Graduates/tools/round_2026-10-11/clean_stats.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
for f in ('index.html','Graduates/index.html','SuccessStories/website/js/data.js'):
    t=open(H+f,encoding='utf-8').read(); print(f,'old',t.count(OTOT),'new',t.count(TOT))
print('done')
