# -*- coding: utf-8 -*-
"""Sweep round 5 Sep 2026 (b) — GitHub-capstone vector, all programmes. 19 new records, 4 enrichments."""
import json
P='index.html'; s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+13; j=s.index('\nconst SITE_STATS')
raw=s[i:j].strip(); D=json.loads(raw[:-1]); g=D['grads']; assert len(g)==2820
C=json.load(open('tools/sweep_candidates_2026-09-05b.json',encoding='utf-8'))
SRC='مسح GitHub لمشاريع التخرج — 5 سبتمبر 2026 (ب)'
PROG={'nlp':'معالجة اللغة الطبيعية بالمحوّلات (SDA-AIE-211 «بيان») — أكاديمية سدايا',
      'agents':'بناء أنظمة وكلاء الذكاء الاصطناعي — أكاديمية سدايا (Building AI Agent Systems)',
      'cv':'الرؤية الحاسوبية للمطوّرين مع Ultralytics — أكاديمية سدايا (Computer Vision for Developers with Ultralytics)',
      'viz':'تصوّر البيانات وسرد القصص (SDA-DSC-112) — أكاديمية سدايا (Data Visualization & Storytelling)'}
TR={'nlp':'ai','agents':'ai','cv':'ai','viz':'ds'}
DUP={'G18':2211,'G16':2466,'G20':190,'G22':2061}
NOTE=' [مسح GitHub — 5 سبتمبر 2026 (ب)] '
new=0
for c in C:
    if c['k'] in DUP:
        r=g[DUP[c['k']]-1]
        r['prog']=r['prog']+' + '+PROG[c['prog']]
        r['d']+=NOTE+'برنامج إضافي موثّق: '+PROG[c['prog']]+' ('+c['co']+'). '+c['d']
        links=[u for l,u in r['links']]
        if c['gh'] not in links: r['links'].append(['مشروع التخرج (GitHub)',c['gh']])
        if c.get('li') and c['li'] not in links: r['links'].append(['LinkedIn',c['li']])
        if not r.get('en'): r['en']=c['en']
        continue
    rec={"n":c['ar'],"en":c['en'],"lv":"gh26b","score":c['score'],"prog":PROG[c['prog']],"co":c['co'],
         "win":"ضمن النطاق","edu":c.get('edu',''),"emp":c.get('emp',''),"role":c.get('role',''),
         "cats":["project","program"],"d":c['d'],"links":[["مشروع التخرج (GitHub)",c['gh']]],"src":SRC,"tr":TR[c['prog']]}
    if c.get('li'): rec['links'].append(['LinkedIn',c['li']])
    if c['k']=='G10':
        rec['d']+=' تنويه: سجل قائم بالاسم نفسه #735 «نوف علي عايض القرني» (قوائم معسكرات 2023 الرسمية، بلا رابط) — ببرنامج ودفعة مختلفين ولا سمة مشتركة سوى الاسم؛ لم يُدمج (المعرّفات موضعية).'
        g[734]['d']+=NOTE+'تنويه تقاطعي: سجل جديد #2839 «نوف القرني» (بناء أنظمة وكلاء الذكاء الاصطناعي، 23–27 أغسطس 2026، GitHub) بالاسم نفسه — لم يُدمج لغياب أي سمة مشتركة غير الاسم.'
    g.append(rec); new+=1
print('new',new,'total',len(g))
s=s[:i]+json.dumps(D,ensure_ascii=False,separators=(',',':'))+';'+s[j:]
def rep(a,b):
    global s; assert a in s, a[:60]; s=s.replace(a,b,1)
rep("{ key: 'ai', label: 'مهندس ذكاء اصطناعي', en: 'AI Engineer', value: 1346 },","{ key: 'ai', label: 'مهندس ذكاء اصطناعي', en: 'AI Engineer', value: 1363 },")
rep("{ key: 'ds', label: 'عالم بيانات', en: 'Data Scientist', value: 765 },","{ key: 'ds', label: 'عالم بيانات', en: 'Data Scientist', value: 767 },")
rep("{ value: 2820, label: 'سجلًا فرديًا',","{ value: 2839, label: 'سجلًا فرديًا',")
s=s.replace('2,820','2,839')
rep("إصدار 5 سبتمبر 2026 (جولة التدريب التعاوني COOP)","إصدار 5 سبتمبر 2026 (ب) (جولة التدريب التعاوني COOP + مسح مشاريع التخرج)")
rep("version 5 September 2026 (Cooperative Training / COOP round)","version 5 September 2026 (b) (COOP round + capstone sweep)")
open(P,'w',encoding='utf-8').write(s)
from collections import Counter; c=Counter(r['tr'] for r in g); print(c,sum(c.values()))
hi=sum(1 for r in g if r['score']>=75); md=sum(1 for r in g if 45<=r['score']<75); lo=sum(1 for r in g if r['score']<45)
wl=sum(1 for r in g if r.get('links')); uu=len({u for r in g for l,u in r.get('links',[])}); we=sum(1 for r in g if r.get('emp'))
print('bands',hi,md,lo,'| links',wl,'unique',uu,'| emp',we)
