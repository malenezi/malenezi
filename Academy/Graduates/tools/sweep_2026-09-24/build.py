import json,re
from final_list import ACCEPT
from arnames import AR,VERIFIED_AR
from cfg import *
S=json.load(open('sets.json')); P=json.load(open('prog.json'))
N=json.load(open('newowners.json')); F=json.load(open('fetched.json'))
g=json.load(open('data.json'))['grads']
def repo_of(o,name):
    for r in N[o]:
        if r['name']==name: return r
def pk(o): return OVR.get(o) or (P[o][0] if P.get(o) else None)
def prim(o):
    nm=REPO_OVR.get(o) or (P[o][1] if P.get(o) else None)
    return repo_of(o,nm)
def li_of(o):
    for u in F['prof'].get(o,{}).get('li',[]):
        m=re.search(r'linkedin\.com/in/([^/?#&]+)',u)
        if m: return 'https://www.linkedin.com/in/'+m.group(1).rstrip('/')
def fmt(dt):
    y,m,d=dt.split('-'); return int(d),MONTHS[int(m)-1],y
new=[];enr=[]
base=len(g)
newowners=[o for o in ACCEPT if o not in S['REM'] and o not in S['ENR']]
for o in newowners:
    en,_,b=ACCEPT[o]; k=pk(o); r=prim(o)
    assert k and r, (o,k,r)
    prog,tr,pen=PROGS[k]
    d_,mo,y=fmt(r['created'])
    co='%s %s (إنشاء مستودع التسليم: %d %s %s)'%(mo,y,d_,mo,y)
    links=[['GitHub','https://github.com/'+o],['مستودع التسليم','https://github.com/%s/%s'%(o,r['name'])]]
    if o in SECOND:
        prog+=' + '+PROGS[SECOND[o]][0]; r2=repo_of(o,SECOND_REPO[o]); links.append(['مستودع التسليم الثاني','https://github.com/%s/%s'%(o,r2['name'])])
    li=li_of(o)
    if li: links.append(['LinkedIn',li])
    if o=='Salmaralfehaid': links.append(['GitHub (حساب ثانٍ)','https://github.com/salmaalfehaid'])
    d='مستودع التسليم `%s` (أُنشئ %d %s %s) ينصّ صراحةً على برنامج «%s» في أكاديمية سدايا مع الإحالة إلى حساب الأكاديمية الرسمي على GitHub (SDAIAAcademy). عتبة الهوية: %s.'%(r['name'],d_,mo,y,pen,BASIS[b])
    if li: d+=' رابط LinkedIn منشور على ملف GitHub نفسه.'
    if o not in VERIFIED_AR: d+=' تنويه: الاسم العربي نقل حرفي عن الاسم اللاتيني المنشور — غير متحقق علنًا.'
    else: d+=' الاسم العربي مكتوب بالعربية في التسليم نفسه.'
    rec={'n':AR[o],'en':en,'lv':LV,'score':SCORE[b],'prog':prog,'co':co,'win':'ضمن النطاق','edu':'','emp':'','role':'','cats':['program','project'],'d':d,'links':links,'src':SRC,'tr':tr,'_o':o}
    new.append(rec)
json.dump(new,open('new_records.json','w'),ensure_ascii=False,indent=0)
print(len(new)); print(json.dumps(new[5],ensure_ascii=False)[:900])
import collections; print(collections.Counter(x['tr'] for x in new))
