import json,os,re
H=os.path.expanduser('~/mnt/Academy/')
sj=open(H+'SuccessStories/website/js/data.js',encoding='utf-8').read()
k=sj.index('const STORIES = [');e=sj.index('\n];',k)
ST=[json.loads(l.strip().rstrip(',')) for l in sj[k:e].split('\n')[1:] if l.strip().startswith('{')]
W={'شهر واحد':1,'شهرين':2,'شهران':2,'ثلاثة أشهر':3,'أربعة أشهر':4,'خمسة أشهر':5,'ستة أشهر':6,'سبعة أشهر':7,'ثمانية أشهر':8,'تسعة أشهر':9,'عشرة أشهر':10,'أحد عشر شهرًا':11,'اثني عشر شهرًا':12,'اثنا عشر شهرًا':12,'ثلاثة عشر شهرًا':13,'أربعة عشر شهرًا':14,'الشهر الرابع عشر':14,'الشهر التالي':1,'صفر شهر':0,'شهر التخرّج نفسه':0,'شهر إتمام':0}
res={}
for x in ST:
    t=' '.join([x['impact'],x['story']]+x['achievements'])
    t2=re.sub(r'(نافذة|معيار|حد|حدّ) ?(ال)?أربعة عشر شهرًا','',t)
    g=[int(m) for m in re.findall(r'\+~?(\d{1,2}) ?(?:أشهر|شهر|شهرًا|\))',t2)]+[int(m) for m in re.findall(r'(\d{1,2}) شهرًا',t2)]
    for w,v in W.items():
        if w in t2: g.append(v)
    res[x['id']]=g
json.dump(res,open('gaps.json','w'),ensure_ascii=False)
none=[i for i,g in res.items() if not g]; over=[(i,g) for i,g in res.items() if g and min(g)>12]; mixed=[(i,g) for i,g in res.items() if g and min(g)<=12 and max(g)>12]
print('none',len(none)); print('over',over); print('mixed',mixed)
import sys
if '--none' in sys.argv:
    S={x['id']:x for x in ST}
    for i in none: x=S[i]; print('##',i,'|',x['category'],'|',x['period'],'|',x['role'][:40],'|',x['org'][:30],'|',re.sub(r'\s+',' ',x['provenance'])[:260])
