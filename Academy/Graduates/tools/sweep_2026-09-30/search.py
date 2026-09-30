import json,time,urllib.request,urllib.parse,calendar,sys,os
out='search.json'
R=json.load(open(out)) if os.path.exists(out) else {}
Q=[]
for m in range(1,13):
    e=calendar.monthrange(2024,m)[1]
    for a,b in ((1,15),(16,e)):
        Q.append('sdaia in:name,description,readme created:2024-%02d-%02d..2024-%02d-%02d'%(m,a,m,b))
Q.append('sdaia in:name,description,readme created:2026-09-23..2026-09-30')
Q.append('"SDA-AIE" OR "SDA-DSC" created:2026-09-20..2026-09-30')
Q.append('SDAIAAcademy in:readme created:2026-09-20..2026-09-30')
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
