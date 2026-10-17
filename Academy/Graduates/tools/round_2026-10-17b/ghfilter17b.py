# -*- coding: utf-8 -*-
import json,re,os,sys
sys.path[:0]=[os.path.expanduser('~/mnt/Academy/Graduates/tools/round_2026-10-07'),os.path.expanduser('~/mnt/Academy/Graduates/tools')]
import translit as TR
H=os.path.expanduser('~/mnt/Academy/'); T=H+'Graduates/tools/round_2026-10-17b/'
s=open(H+'Graduates/index.html',encoding='utf-8').read()
i=s.index('const DATA = ')+len('const DATA = '); j=s.index('\nconst SITE_STATS')
g=json.loads(s[i:j].rstrip()[:-1])['grads']; idx=TR.build_index(g)
V=json.load(open(T+'ver_gh.json',encoding='utf-8')); S=json.load(open(T+'harvest_state.json',encoding='utf-8'))['H']
SIG=re.compile(r'(sdaia academy|أكاديمية سدايا|SDAIAAcademy|SDA-[A-Z]{3}-\d{3}|bootcamp|boot camp|معسكر|capstone|tayseer|rafeeq|bayan|tamweel|airpassengers|workshop|course|program|training|trainee|academy)',re.I)
out=[]
for o,v in V.items():
    nm=(v['p'].get('name') or '').strip()
    toks=[t for t in re.split(r'\s+',nm) if len(t)>1 and not re.search(r'\d',t)]
    hits=[(r,l) for r,x in v['r'].items() for l in x['hits']]
    sig=[f'{r}: {l}' for r,l in hits if SIG.search(l) and re.search(r'sdaia|سدايا',l,re.I)]
    reposig=[r for r in v['r'] if re.search(r'sdaia|sda-|tayseer|rafeeq|bayan|tamweel|capstone|airpassengers',r,re.I)]
    if not sig and not reposig: continue
    if len(toks)<2: continue
    m=sorted({x[0] for x in TR.match(nm,nm,idx)})
    ex=[k+1 for k,r in enumerate(g) if (r.get('en') or '').lower()==nm.lower()]
    dates=sorted({S.get(o+'/'+r,{}).get('u','') for r in v['r']})
    out.append(f"{o} | {nm} | li:{','.join(x.split('/in/')[-1] for x in v['p'].get('li',[]))} | {','.join(v['r'])} | upd {dates[-1] if dates else ''} | match {m[:4]} exact {ex} || "+' ¦ '.join(x[:150] for x in (sig or [f'{r}: {l}' for r,l in hits])[:3]))
print(len(out)); print('\n'.join(out))
