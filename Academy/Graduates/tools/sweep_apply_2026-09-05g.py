# -*- coding: utf-8 -*-
"""Round 5 Sep 2026 (g) — May-2026-onward programme portfolio sweep (GitHub + LinkedIn). 6 new records."""
import json
P='index.html'; s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+13; j=s.index('\nconst SITE_STATS')
raw=s[i:j].strip(); D=json.loads(raw[:-1]); g=D['grads']; assert len(g)==2845, len(g)
C=json.load(open('tools/sweep_candidates_2026-09-05g.json',encoding='utf-8'))
SRC='مسح البرامج المستحدثة (مايو 2026 – سبتمبر 2026) عبر GitHub ولينكدإن — 5 سبتمبر 2026 (ز)'
PROG={'cv':'الرؤية الحاسوبية للمطوّرين مع Ultralytics — أكاديمية سدايا (Computer Vision for Developers with Ultralytics)',
      'ts':'تحليل السلاسل الزمنية — أكاديمية سدايا (SDAIA Academy Time Series Course)'}
new=0
for c in C:
    rec={"n":c['ar'],"en":c['en'],"lv":"ghsweep26g","score":c['score'],"prog":PROG[c['prog']],"co":c['co'],
         "win":"ضمن النطاق","edu":c.get('edu',''),"emp":c.get('emp',''),"role":c.get('role',''),
         "cats":["project","program"],"d":c['d'],
         "links":[["مشروع التخرج (GitHub)",c['gh']]],"src":SRC,"tr":c['tr']}
    if c.get('li'): rec['links'].append(['LinkedIn',c['li']])
    g.append(rec); new+=1
print('new',new,'total',len(g))
from collections import Counter
cnt=Counter(r['tr'] for r in g); print(cnt, sum(cnt.values()))
hi=sum(1 for r in g if r['score']>=75); md=sum(1 for r in g if 45<=r['score']<75); lo=sum(1 for r in g if r['score']<45)
wl=sum(1 for r in g if r.get('links')); uu=len({u for r in g for l,u in r.get('links',[])}); we=sum(1 for r in g if r.get('emp'))
print('bands',hi,md,lo,'| withlinks',wl,'unique',uu,'| emp',we)
s=s[:i]+json.dumps(D,ensure_ascii=False,separators=(',',':'))+';'+s[j:]
def rep(a,b):
    global s; assert a in s, a[:80]; s=s.replace(a,b,1)
rep("{ key: 'ai', label: 'مهندس ذكاء اصطناعي', en: 'AI Engineer', value: 1379 },","{ key: 'ai', label: 'مهندس ذكاء اصطناعي', en: 'AI Engineer', value: %d },"%cnt['ai'])
rep("{ key: 'ds', label: 'عالم بيانات', en: 'Data Scientist', value: 762 },","{ key: 'ds', label: 'عالم بيانات', en: 'Data Scientist', value: %d },"%cnt['ds'])
rep("{ value: 2845, label: 'سجلًا فرديًا',","{ value: %d, label: 'سجلًا فرديًا',"%len(g))
s=s.replace('2,845','2,851')
s=s.replace('إصدار 5 سبتمبر 2026 (و) (مسح المسارات + حسم قائمة قيد التحقق بمعطيات الأكاديمية)','إصدار 5 سبتمبر 2026 (ز) (مسح البرامج المستحدثة مايو–سبتمبر 2026)')
s=s.replace('version 5 September 2026 (f) (track sweep + pending list resolved from Academy records)','version 5 September 2026 (g) (new-programme portfolio sweep, May–Sep 2026)')
open(P,'w',encoding='utf-8').write(s)
json.dump({'total':len(g),'tracks':dict(cnt),'hi':hi,'md':md,'lo':lo,'wl':wl,'uu':uu,'we':we},open('tools/stats_g.json','w'))
print('written')
