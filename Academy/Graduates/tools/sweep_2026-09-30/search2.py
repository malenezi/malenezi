import json,time,urllib.request,urllib.parse,calendar,sys,os
out='search2.json'
R=json.load(open(out)) if os.path.exists(out) else {}
Q=[]
QX=True
for m in range(1,13):
    e=calendar.monthrange(2024,m)[1]
    for a,b in ((1,15),(16,e)):
        Q.append('sdaia in:name,description,readme created:2024-%02d-%02d..2024-%02d-%02d'%(m,a,m,b))
Q.append('sdaia in:name,description,readme created:2026-09-23..2026-09-30')
Q.append('"SDA-AIE" OR "SDA-DSC" created:2026-09-20..2026-09-30')
Q.append('SDAIAAcademy in:readme created:2026-09-20..2026-09-30')
Q=['T5 bootcamp created:2024-01-01..2024-06-30','T5 bootcamp created:2024-07-01..2024-12-31','zeham created:2024-01-01..2025-06-30','"crowd management" created:2024-06-01..2024-12-31','tuwaiq T5 created:2024-01-01..2024-12-31','"T5" "data science" bootcamp created:2024-01-01..2024-12-31','"SDAIA" java created:2024-04-01..2024-08-31','sdaia in:name,description,readme created:2025-01-01..2025-12-31 fork:false','"SDAIA Academy" created:2026-08-01..2026-09-30','sdaia capstone created:2026-09-01..2026-09-30','SDAIAAcademy in:readme created:2026-08-15..2026-09-19']
for q in Q:
    if q in R: continue
    items=[];tot=None
    for p in range(1,11):
        u='https://api.github.com/search/repositories?q=%s&per_page=100&page=%d'%(urllib.parse.quote(q),p)
        for att in range(5):
            try:
                with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'x','Accept':'application/vnd.github+json'}),timeout=30) as r:
                    d=json.load(r);break
            except Exception as ex:
                print('err',ex,flush=True);time.sleep(65)
        else: d={'items':[],'total_count':0}
        tot=d.get('total_count');it=d.get('items',[])
        items+= [{'o':i['owner']['login'],'n':i['name'],'c':i['created_at'],'desc':i.get('description'),'fork':i['fork']} for i in it]
        time.sleep(7)
        if len(it)<100: break
    R[q]={'total':tot,'items':items}
    json.dump(R,open(out,'w'))
    print(q,tot,len(items),flush=True)
print('DONE',flush=True)
