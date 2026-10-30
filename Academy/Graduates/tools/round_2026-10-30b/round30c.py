# -*- coding: utf-8 -*-
# 30 Oct 2026 (c): keep Hassan Alshanqiti (ruling), Alaa Aljadani completion = Nov–Dec 2021, drop the quote tag,
# wire supplied photos (7) + logos (9), counters.
import json,re,os,sys,shutil,openpyxl
DRY='--apply' not in sys.argv
H=os.path.expanduser('~/mnt/Academy/'); W=H+'SuccessStories/website/'
TAG='[جولة 30 أكتوبر 2026 (ج)] '
def rep(s,a,b,c=None):
    n=s.count(a); assert n>=1,('missing',a[:90])
    if c is not None: assert n==c,(a[:90],n)
    return s.replace(a,b)
EXCL={'جهة حكومية','جهة حكومية (غير معلنة)','غير معلنة','قمة الابتكار الكمّي — دبي (Quantum Innovation Summit)','مركز «ذكاء» — منشآت','مهمة OSACT7 المشتركة — LREC 2026','Private Data Department'}
emp_count=lambda st:len({x['org'].strip() for x in st}-EXCL)
dj=W+'js/data.js'; sj=open(dj,encoding='utf-8').read()
k=sj.index('const STORIES = [');e=sj.index('\n];',k)
ST=[json.loads(l.strip().rstrip(',')) for l in sj[k:e].split('\n')[1:] if l.strip().startswith('{')]
S0=len(ST);E0=emp_count(ST); assert (S0,E0)==(208,119),(S0,E0)
S={x['id']:x for x in ST}
# 1. restore Hassan Alshanqiti
arc=H+'SuccessStories/audit/removed_stories_policy_v2_2026-10-30.json'; A=json.load(open(arc,encoding='utf-8'))
h=[x for x in A if x['id']=='hassan-alshanqiti'][0]; A=[x for x in A if x['id']!='hassan-alshanqiti']
for kk in ('removedReason','record'): h.pop(kk,None)
RUL='استثناء بحكم أ. د. ممدوح العنزي (30 أكتوبر 2026) — يُبقى رغم أن التوظيف يقع بعد نحو 13 شهرًا من إتمام المعسكر'
h['impact']='التحق بشركة ثقة محللَ بحث وتطوير بدوام كامل في أبريل 2025.'
h['story']=re.sub(r'أهليته ضمن النافذة[^.]*\.',RUL+'.',h['story'])
if RUL not in h['story']: h['story']=h['story'].rstrip()+' '+RUL+'.'
h['provenance']=h['provenance']+' '+RUL+'.'
h['policyException']=RUL
h['category']='employment'; h['categories']=['employment']
q=h['quote']; q['kind']='verified'; assert len(q['text'])<=97 and len(q['textEn'])<=97
assert os.path.exists(W+h['photo']) and os.path.exists(W+h['orgLogo'])
ST.append(h)
# 2. Alaa Aljadani completion
a=S['alaa-aljadani']; a['period']='نوفمبر – ديسمبر 2021'
a['story']=a['story'].replace('وأرّخ مستودع مشروعها الختامي بين 29 نوفمبر و16 ديسمبر 2021.','بين نوفمبر وديسمبر 2021 (Data Science Bootcamp، شهران).').replace('؛ شهر الإتمام مأخوذ من تاريخ المستودع','')
a['achievements']=[x.replace('(ديسمبر 2021)','(نوفمبر – ديسمبر 2021)') for x in a['achievements']]
a['provenance']=a['provenance'].replace('؛ وشهر الإتمام من مستودع المشروع الختامي','؛ وفترة المعسكر من صفحة الخبرة: Data Science Bootcamp، نوفمبر – ديسمبر 2021 (شهران)')
a['impact']=a['impact'].replace('بعد عشرة أشهر من مشروعها الختامي في المعسكر','بعد عشرة أشهر من إتمام المعسكر')
# 3. photos & logos
PH={'alaa-aljadani':'alaa-aljadani-lb.jpg','fatima-alsaeed':'fatima-alsaeed-lb.jpg','jinan-alghutaymil':'jinan-alghutaymil-lb.jpg','nada-rambu':'nada-rambu-lb.jpg',
    'ali-altamimi':'ali-altamimi-photo.jpg','mohammad-alown':'mohammad-alown-photo.jpg','saud-alballaa':'saud-alballaa-photo.jpg'}
LG={'نada':None}
LG={'أفون العربية (Avon Beauty Arabia)':'logo-avon.png','بنك البلاد':'logo-albilad.png','إعمار المدينة الاقتصادية':'logo-kaec.png','إكسيكرا (Execra)':'logo-execra.png',
    'هواوي (Huawei)':'logo-huawei.png','وزارة الاتصالات وتقنية المعلومات':'logo-mcit.png','NHC Innovation':'logo-nhc.png','القدية (Qiddiya)':'logo-qiddiya.png','روشن (ROSHN)':'logo-roshn.png'}
nph=nlg=0
for x in ST:
    if x['id'] in PH:
        f='assets/'+PH[x['id']]; assert os.path.exists(W+f),f; x['photo']=f; x.pop('photoPlaceholder',None); nph+=1
    if x['org'] in LG:
        f='assets/'+LG[x['org']]; assert os.path.exists(W+f),f; x['orgLogo']=f; nlg+=1
assert nph==7 and nlg==9,(nph,nlg)
# 4. blanket-approval source not shown
for x in ST:
    if x['quote'].get('source','').startswith('اعتماد أ. د. ممدوح العنزي لجميع'): x['quote'].pop('source')
order={x['id']:i for i,x in enumerate(json.loads('['+','.join(l.strip().rstrip(',') for l in sj[k:e].split('\n')[1:] if l.strip().startswith('{'))+']'))}
S1=len(ST); E1=emp_count(ST)
print('stories',S0,S1,'emp',E0,E1)
if DRY: sys.exit(0)
BK=H+'_backups/2026-10-30c/'; os.makedirs(BK,exist_ok=True)
for f in ['SuccessStories/website/js/data.js','SuccessStories/website/js/main.js','SuccessStories/website/index.html','index.html','Graduates/index.html','Graduates/Graduates_Database.xlsx','Graduates/Graduates_Database.md']: shutil.copy2(H+f,BK+f.replace('/','__'))
json.dump(A,open(arc,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
sj2=sj[:k]+'const STORIES = [\n'+',\n'.join('  '+json.dumps(x,ensure_ascii=False) for x in ST)+sj[e:]
sj2=re.sub(r"(\{ value: )%d(,\s+label: 'قصة نجاح)"%S0,r"\g<1>%d\2"%S1,sj2,count=1)
sj2=re.sub(r"(\{ value: )%d(,\s+label: 'جهة عمل')"%E0,r"\g<1>%d\2"%E1,sj2,count=1)
sj2=rep(sj2,"'use strict';","/* 30 أكتوبر 2026 (ج): إبقاء قصة حسن الشنقيطي استثناءً بحكم أ. د. ممدوح العنزي؛ فترة معسكر آلاء الجداني نوفمبر – ديسمبر 2021؛ حذف وسم «اقتباس معتمد للنشر»؛ ربط 7 صور و9 شعارات زوّد بها أ. د. ممدوح العنزي — القصص %d ← %d، جهات العمل %d ← %d. */\n'use strict';"%(S0,S1,E0,E1),1)
open(dj,'w',encoding='utf-8').write(sj2)
m=open(W+'js/main.js',encoding='utf-8').read()
m=rep(m,"    : `<span class=\"q-tag q-tag--verified\">${I('badge-check', 'i-sm')}${T('اقتباس معتمد للنشر', 'Approved for publication')}</span>`;","    : '';",1)
m=rep(m,'      <div class="q-foot">${tag}</div>','      ${tag ? `<div class="q-foot">${tag}</div>` : \'\'}',1)
open(W+'js/main.js','w',encoding='utf-8').write(m)
# DB
P_=H+'Graduates/index.html'; s=open(P_,encoding='utf-8').read(); i=s.index('const DATA = ')+13; j=s.index('\nconst SITE_STATS')
D=json.loads(s[i:j].rstrip()[:-1]); g=D['grads']; head=s[:i]; tail=s[j:]
X_=H+'Graduates/Graduates_Database.xlsx'; wb=openpyxl.load_workbook(X_); ws=wb['قاعدة البيانات']
def note(kk,t): g[kk-1]['d']+=' '+TAG+t; ws.cell(kk+1,21).value=(ws.cell(kk+1,21).value or '')+' '+TAG+t
note(952,'أُعيدت قصة «hassan-alshanqiti» إلى المنشور: '+RUL+'.')
g[2234]['co']='نوفمبر – ديسمبر 2021 (Data Science Bootcamp — صفحة الخبرة على LinkedIn)'; ws.cell(2236,6).value=g[2234]['co']
note(2235,'فترة المعسكر من صفحة الخبرة: Data Science Bootcamp، نوفمبر – ديسمبر 2021 (شهران) — زوّد بها أ. د. ممدوح العنزي.')
def counts(t):
    for a_,b_ in (('%d قصة'%S0,'%d قصة'%S1),('%d stories'%S0,'%d stories'%S1),('%d verified'%S0,'%d verified'%S1),('%d جهة عمل'%E0,'%d جهة عمل'%E1),('%d employers'%E0,'%d employers'%E1),('across %d government'%E0,'across %d government'%E1)):
        t=t.replace(a_,b_)
    return t
tail=counts(tail); head=counts(head)
tail=re.sub(r"(\{ value: )%d(,\s+label: 'قصة نجاح)"%S0,r"\g<1>%d\2"%S1,tail,count=1)
D['grads']=g; open(P_,'w',encoding='utf-8').write(head+json.dumps(D,ensure_ascii=False)+';'+tail)
P2=H+'index.html'; t=counts(open(P2,encoding='utf-8').read()); t=rep(t,'data-count="%d"'%S0,'data-count="%d"'%S1,1); t=rep(t,'data-count="%d"'%E0,'data-count="%d"'%E1,1); open(P2,'w',encoding='utf-8').write(t)
P4=W+'index.html'; t=counts(open(P4,encoding='utf-8').read()); t=rep(t,'"numberOfItems": %d'%S0,'"numberOfItems": %d'%S1,1); open(P4,'w',encoding='utf-8').write(t)
sh=wb['السياسة_v2_30_أكتوبر_2026']; sh.append(['hassan-alshanqiti',952,'أُعيدت (استثناء)',RUL]); sh.append(['alaa-aljadani',2235,'تصحيح فترة المعسكر','نوفمبر – ديسمبر 2021'])
wb.save(X_)
P5=H+'Graduates/Graduates_Database.md'; md=open(P5,encoding='utf-8').read()
md=rep(md,'— السياسة v2.0 لقصص النجاح (القصص %d · جهات العمل %d).'%(S0,E0),'— السياسة v2.0 لقصص النجاح (القصص %d · جهات العمل %d بعد الجولة ج).'%(S1,E1),1)
md=rep(md,'## السياسة v2.0 لقصص النجاح — 30 أكتوبر 2026\n','## السياسة v2.0 لقصص النجاح — 30 أكتوبر 2026\n\n**الجولة (ج):** أُعيدت قصة حسن الشنقيطي #952 استثناءً بحكم أ. د. ممدوح العنزي (القصص %d ← %d، جهات العمل %d ← %d)؛ فترة معسكر آلاء الجداني #2235 نوفمبر – ديسمبر 2021؛ حُذف وسم «اقتباس معتمد للنشر»؛ رُبطت 7 صور و9 شعارات.\n'%(S0,S1,E0,E1),1)
open(P5,'w',encoding='utf-8').write(md)
print('done')
