# -*- coding: utf-8 -*-
"""Round 5 Sep 2026 (h) — logged-in LinkedIn sweep of the May-2026-onward programme portfolio. 15 new records."""
import json
P='index.html'; s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+13; j=s.index('\nconst SITE_STATS')
D=json.loads(s[i:j].strip()[:-1]); g=D['grads']; assert len(g)==2851, len(g)
C=json.load(open('tools/li_candidates_2026-09-05h.json',encoding='utf-8'))
SRC='مسح لينكدإن بحساب مسجَّل — البرامج المستحدثة (مايو–سبتمبر 2026) — 5 سبتمبر 2026 (ح)'
new=0
for c in C:
    rec={"n":c['ar'],"en":c['en'],"lv":"lisweep26h","score":c['score'],"prog":c['prog'],"co":c['co'],
         "win":"ضمن النطاق","edu":c.get('edu',''),"emp":c.get('emp',''),"role":c.get('role',''),
         "cats":["program"]+(["project"] if 'مشروع' in c['d'] else []),
         "d":c['d'],"links":([['LinkedIn',c['li']]] if c.get('li') else []),"src":SRC,"tr":c['tr']}
    g.append(rec); new+=1
# cross-note on #2604 (يارا الشويهي) — same NCA risk-assessment project, programme now probable
NOTE=' [مسح لينكدإن — 5 سبتمبر 2026 (ح)] تنويه تقاطعي: سجل جديد «ندى العنزي» يعلن قيادة فريق مشروع تقييم مخاطر الأمن السيبراني بمواءمة ضوابط الهيئة الوطنية للأمن السيبراني ضمن معسكر تطوير حلول الذكاء الاصطناعي التوليدي بأكاديمية سدايا (أغسطس 2026) — ترجّح المطابقة في الموضوع والشهر أن يكون هذا هو البرنامج غير المحدد لهذا السجل. تنويه لا إسناد؛ لم يُعدَّل حقل البرنامج.'
g[2603]['d']=g[2603]['d']+NOTE
print('new',new,'total',len(g))
from collections import Counter
cnt=Counter(r['tr'] for r in g); print(cnt,sum(cnt.values()))
hi=sum(1 for r in g if r['score']>=75); md=sum(1 for r in g if 45<=r['score']<75); lo=sum(1 for r in g if r['score']<45)
wl=sum(1 for r in g if r.get('links')); uu=len({u for r in g for l,u in r.get('links',[])}); we=sum(1 for r in g if r.get('emp'))
print('bands',hi,md,lo,'| withlinks',wl,'unique',uu,'| emp',we)
assert not any('**' in str(r.get(f,'')) for r in g for f in ('d','prog','role','edu','n','en')), 'literal **'
s=s[:i]+json.dumps(D,ensure_ascii=False,separators=(',',':'))+';'+s[j:]
def rep(a,b):
    global s; assert a in s, a[:80]; s=s.replace(a,b,1)
rep("{ key: 'ai', label: 'مهندس ذكاء اصطناعي', en: 'AI Engineer', value: 1381 },","{ key: 'ai', label: 'مهندس ذكاء اصطناعي', en: 'AI Engineer', value: %d },"%cnt['ai'])
rep("{ key: 'ds', label: 'عالم بيانات', en: 'Data Scientist', value: 766 },","{ key: 'ds', label: 'عالم بيانات', en: 'Data Scientist', value: %d },"%cnt['ds'])
rep("{ value: 2851, label: 'سجلًا فرديًا',","{ value: %d, label: 'سجلًا فرديًا',"%len(g))
s=s.replace('2,851','2,866')
s=s.replace('إصدار 5 سبتمبر 2026 (ز) (مسح البرامج المستحدثة مايو–سبتمبر 2026)','إصدار 5 سبتمبر 2026 (ح) (مسح لينكدإن للبرامج المستحدثة مايو–سبتمبر 2026)')
s=s.replace('version 5 September 2026 (g) (new-programme portfolio sweep, May–Sep 2026)','version 5 September 2026 (h) (LinkedIn sweep of the new-programme portfolio, May–Sep 2026)')
open(P,'w',encoding='utf-8').write(s)
json.dump({'total':len(g),'tracks':dict(cnt),'hi':hi,'md':md,'lo':lo,'wl':wl,'uu':uu,'we':we},open('tools/stats_h.json','w'))
print('written')
