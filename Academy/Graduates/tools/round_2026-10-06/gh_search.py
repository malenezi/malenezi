import json,urllib.request,urllib.parse,time,sys,re,load
D=load.load(); g=D['grads']
own=set()
for r in g:
    for l in r['links']:
        m=re.match(r'https?://github\.com/([^/?#]+)',l[1]); 
        if m: own.add(m.group(1).lower())
print('db owners',len(own))
Q=[('2022','sdaia in:name,description,readme created:2022-01-01..2022-12-31'),
   ('2023a','sdaia in:name,description,readme created:2023-01-01..2023-06-30'),
   ('2023b','sdaia in:name,description,readme created:2023-07-01..2023-12-31'),
   ('2024a','sdaia in:name,description,readme created:2024-01-01..2024-04-30'),
   ('2024b','sdaia in:name,description,readme created:2024-05-01..2024-08-31'),
   ('2024c','sdaia in:name,description,readme created:2024-09-01..2024-12-31'),
   ('2026a','sdaia in:name,description,readme created:2026-01-01..2026-05-31'),
   ('2026b','sdaia in:name,description,readme created:2026-06-01..2026-10-06'),
   ('t5','"T5" bootcamp in:name,description,readme created:2022-01-01..2024-12-31'),
   ('ar','سدايا in:readme,description created:2022-01-01..2026-10-06')]
import os
out=json.load(open('gh_raw.json')) if os.path.exists('gh_raw.json') else {}
sel=sys.argv[1].split(',')
for tag,q in Q:
    if tag not in sel or tag in out: continue
    items=[]
    for p in range(1,11):
        u='https://api.github.com/search/repositories?per_page=100&page=%d&q=%s'%(p,urllib.parse.quote(q))
        for attempt in range(3):
            try:
                d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'x'}),timeout=30)); break
            except Exception as e:
                print('err',e); time.sleep(15); d=None
        if not d: break
        it=d.get('items',[]); items+=it
        if p==1: print(tag,'total',d.get('total_count'))
        if len(it)<100: break
        time.sleep(7)
    out[tag]=[dict(o=i['owner']['login'],t=i['owner']['type'],n=i['name'],c=i['created_at'],p=i['pushed_at'],d=(i['description'] or '')[:120],f=i['fork']) for i in items]
    time.sleep(7)
    json.dump(out,open('gh_raw.json','w'),ensure_ascii=False)
for tag,v in out.items():
    new={x['o'] for x in v if x['o'].lower() not in own and x['t']=='User'}
    print(tag,len(v),'new owners',len(new))
