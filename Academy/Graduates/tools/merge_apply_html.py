# -*- coding: utf-8 -*-
import json, re, collections, sys
BASE=sys.argv[1]; FINAL=sys.argv[2]; DRY=len(sys.argv)>3 and sys.argv[3]=='dry'
F=json.load(open(FINAL,encoding='utf-8')); NEW=F['new']; ENR=F['enrich']
TAG='[دمج ملف القاعدة النوعية — 28 أغسطس 2026]'
gp=(BASE+'/grad.html') if DRY else (BASE+'/Graduates/index.html')
pp=(BASE+'/portal.html') if DRY else (BASE+'/index.html')
def prec(p):
    if re.search(r'NVIDIA|NCA-GENL|انفيديا|إنفيديا|الذكاء الاصطناعي التوليدي|Gen ?AI',p,re.I): return 'genai'
    if re.search(r'علوم البيانات|هندسة البيانات|نمذجة|مستودعات البيانات|ذكاء الأعمال|\bT5\b|Data Scien|Data Engineer|زحام|مستقبل سدايا|GDP',p,re.I): return 'ds'
    if re.search(r'تعلم الآلة|التعلم الآلي|النماذج اللغوية|LLM|وكلاء|التوكيلي|الوكيلي|Agentic|رؤية الحاسب|معالجة اللغة|البرمجة التوليدية|محترفي الذكاء|بناء تطبيقات|المسارات المتقدمة|أكسفورد|Oxford|ML|Machine Learning',p,re.I): return 'ai'
    if re.search(r'إدارة البيانات|حوكمة|الجودة|البيانات الوصفية|Data Management|Governance',p): return 'dmg'
    return 'other'
s=open(gp,encoding='utf-8').read()
i=s.find('const DATA = '); j=i+len('const DATA = '); depth=0; k=j
while True:
    c=s[k]
    if c=='{': depth+=1
    elif c=='}':
        depth-=1
        if depth==0: break
    k+=1
raw=s[j:k+1]; data=json.loads(raw)
assert json.dumps(data,ensure_ascii=False,separators=(',',':'))==raw,'ROUND-TRIP FAILED'
g=data['grads']; n0=len(g); assert n0==2740,n0
AR='يناير|فبراير|مارس|أبريل|مايو|يونيو|يوليو|أغسطس|سبتمبر|أكتوبر|نوفمبر|ديسمبر'
trchg=[]
for e in ENR:
    rec=g[e['id']-1]; have=[u for _,u in rec.get('links',[])]
    for lab,u in e['add_links']:
        if u not in have: rec.setdefault('links',[]).append([lab,u]); have.append(u)
    if e['add_progs']:
        rec['prog']=rec['prog']+' + '+' + '.join(e['add_progs'])
        nt=prec(rec['prog'])
        if nt!=rec['tr']: trchg.append((e['id'],rec['tr'],nt)); rec['tr']=nt
    if e['file_emp'] and not (rec.get('emp') or '').strip(): rec['emp']=e['file_emp']
    if e['file_role'] and not (rec.get('role') or '').strip(): rec['role']=e['file_role']
    co=(rec.get('co') or '').strip(); fd=e['file_dates'][0] if e['file_dates'] else ''
    if fd and re.search(AR,fd) and (re.match(r'^\s*20\d\d\s*$',co) or re.match(r'^\s*20\d\d-\d\d-\d\d',co) or co==''):
        rec['co']=fd
    rec['d']=((rec.get('d','') or '').strip()+' '+TAG+' '+e['d']).strip()
    if rec['score']<80: rec['score']=min(88,rec['score']+8)
for r in NEW:
    g.append({kk:r[kk] for kk in ('n','en','lv','score','prog','co','win','edu','emp','role','cats','d','links','src','tr')})
assert len(g)==n0+len(NEW)
N=len(g); tr=collections.Counter(x['tr'] for x in g)
wl=sum(1 for x in g if x.get('links')); uq=len({l[1] for x in g for l in x.get('links',[])})
emp=sum(1 for x in g if (x.get('emp') or '').strip())
hi=sum(1 for x in g if x['score']>=75); mid=sum(1 for x in g if 45<=x['score']<75); lo=sum(1 for x in g if x['score']<45)
NVPAT=re.compile(r'NVIDIA|NCA-GENL|انفيديا|إنفيديا',re.I)
named={i2 for i2,x in enumerate(g,1) if NVPAT.search(x['prog'])}
tier={i2 for i2,x in enumerate(g,1) if x['lv']=='nvidia'}
nv=len(named|tier)
st={'N':N,'tr':dict(tr),'withlink':wl,'uniq':uq,'emp':emp,'hi':hi,'mid':mid,'lo':lo,
    'nv_named':len(named),'nv_tier':len(tier),'nv_union':nv,'trchg':trchg}
print(json.dumps(st,ensure_ascii=False))
new_raw=json.dumps(data,ensure_ascii=False,separators=(',',':'))
s2=s[:j]+new_raw+s[k+1:]
fm=lambda x: format(x,',')
def rep(t,old,new,exp=1):
    c=t.count(old); assert c==exp,'count %r=%d exp %d'%(old[:60],c,exp); return t.replace(old,new)
s2=rep(s2,"value: 2740, label: 'سجلًا فرديًا'","value: %d, label: 'سجلًا فرديًا'"%N)
s2=rep(s2,"en: 'AI Engineer', value: 1317","en: 'AI Engineer', value: %d"%tr['ai'])
s2=rep(s2,"en: 'Data Scientist', value: 731","en: 'Data Scientist', value: %d"%tr['ds'])
s2=rep(s2,"en: 'Data Management & Governance', value: 324","en: 'Data Management & Governance', value: %d"%tr['dmg'])
s2=rep(s2,"en: 'Gen AI Academy', value: 245","en: 'Gen AI Academy', value: %d"%tr['genai'])
s2=rep(s2,"en: 'Other / Specialized', value: 123","en: 'Other / Specialized', value: %d"%tr['other'])
s2=rep(s2,"{ value: 733,  label: 'سجلًا برابط تحقق علني', note: '1,148 رابط مصدر فريد',",
          "{ value: %d,  label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(wl,fm(uq)))
s2=rep(s2,"noteEn: '1,148 unique source links'","noteEn: '%s unique source links'"%fm(uq))
s2=rep(s2,"{ value: 245,  label: 'خريج مسار NVIDIA',      note: '240 مُسمّى ∪ 215 في الطبقة الرسمية',",
          "{ value: %d,  label: 'خريج مسار NVIDIA',      note: '%d مُسمّى ∪ %d في الطبقة الرسمية',"%(nv,len(named),len(tier)))
s2=rep(s2,"noteEn: '240 named ∪ 215 in the official tier'","noteEn: '%d named ∪ %d in the official tier'"%(len(named),len(tier)))
s2=rep(s2,'240 سجلًا يذكر NVIDIA صراحةً في حقل البرنامج، اتحادًا مع 215 سجلًا في طبقة «برامج NVIDIA» الرسمية — والمجموع غير المكرَّر 245.',
          '%d سجلًا يذكر NVIDIA صراحةً في حقل البرنامج، اتحادًا مع %d سجلًا في طبقة «برامج NVIDIA» الرسمية — والمجموع غير المكرَّر %d.'%(len(named),len(tier),nv))
s2=rep(s2,'240 records name NVIDIA explicitly in the program field, unioned with the 215 records in the official NVIDIA tier — 245 distinct in total.',
          '%d records name NVIDIA explicitly in the program field, unioned with the %d records in the official NVIDIA tier — %d distinct in total.'%(len(named),len(tier),nv))
for a,b in [('لخريجي أكاديمية سدايا: 2,740 سجلًا','لخريجي أكاديمية سدايا: %s سجلًا'%fm(N)),
            ('قاعدة بيانات موثّقة لـ2,740 خريجًا','قاعدة بيانات موثّقة لـ%s خريجًا'%fm(N)),
            ('(2,740 اليوم)','(%s اليوم)'%fm(N)),('(2,740 today)','(%s today)'%fm(N)),
            ('إصدار 28 أغسطس 2026 (جولة مسح LinkedIn للبرامج الستة) · 2,740 سجلًا فرديًا',
             'إصدار 28 أغسطس 2026 (جولة دمج ملف القاعدة النوعية) · %s سجلًا فرديًا'%fm(N)),
            ('version 28 August 2026 (six-programme LinkedIn scan) · 2,740 individual records',
             'version 28 August 2026 (specialised-database merge) · %s individual records'%fm(N))]:
    s2=s2.replace(a,b)
assert '2,740' not in s2
open(gp,'w',encoding='utf-8').write(s2); print('graduates html ok')
ps=open(pp,encoding='utf-8').read()
ps=ps.replace('data-count="2740"','data-count="%d"'%N)
ps=ps.replace('data-count="1317"','data-count="%d"'%tr['ai']).replace('data-count="731"','data-count="%d"'%tr['ds'])
ps=ps.replace('data-count="324"','data-count="%d"'%tr['dmg']).replace('data-count="245"','data-count="%d"'%tr['genai'])
ps=ps.replace('data-count="123"','data-count="%d"'%tr['other'])
ps=ps.replace('240 سجلًا يذكر NVIDIA صراحةً في حقل البرنامج، اتحادًا مع 215 سجلًا في طبقة «برامج NVIDIA» الرسمية — والمجموع غير المكرَّر 245.',
              '%d سجلًا يذكر NVIDIA صراحةً في حقل البرنامج، اتحادًا مع %d سجلًا في طبقة «برامج NVIDIA» الرسمية — والمجموع غير المكرَّر %d.'%(len(named),len(tier),nv))
ps=ps.replace('240 records name NVIDIA explicitly in the program field, unioned with the 215 records in the official NVIDIA tier — 245 distinct in total.',
              '%d records name NVIDIA explicitly in the program field, unioned with the %d records in the official NVIDIA tier — %d distinct in total.'%(len(named),len(tier),nv))
for a,b in [('2,740 أفراد منذ 2021','%s أفراد منذ 2021'%fm(N)),('2,740 individuals since 2021','%s individuals since 2021'%fm(N)),
            ('سجلات قاعدة الخريجين الـ2,740','سجلات قاعدة الخريجين الـ%s'%fm(N)),
            ('Each of the 2,740 graduate records','Each of the %s graduate records'%fm(N)),
            ('موثّقة لـ 2,740 خريجين منذ 2021','موثّقة لـ %s خريجين منذ 2021'%fm(N)),
            ('database of 2,740 graduates since 2021','database of %s graduates since 2021'%fm(N)),
            ('# بوابة الخريجين — 2,740 سجلًا موثّقًا','# بوابة الخريجين — %s سجلًا موثّقًا'%fm(N)),
            ('# graduates portal — 2,740 verified records','# graduates portal — %s verified records'%fm(N))]:
    ps=ps.replace(a,b)
assert '2,740' not in ps and '2740' not in ps
open(pp,'w',encoding='utf-8').write(ps); print('portal ok')
json.dump(st,open('/tmp/merge/stats2.json','w'))
