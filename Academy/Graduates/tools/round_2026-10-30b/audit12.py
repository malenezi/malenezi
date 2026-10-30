import json,os,re,collections,sys
H=os.path.expanduser('~/mnt/Academy/')
sj=open(H+'SuccessStories/website/js/data.js',encoding='utf-8').read()
k=sj.index('const STORIES = [');e=sj.index('\n];',k)
ST=[json.loads(l.strip().rstrip(',')) for l in sj[k:e].split('\n')[1:] if l.strip().startswith('{')]
M={m:i+1 for i,m in enumerate('يناير فبراير مارس أبريل مايو يونيو يوليو أغسطس سبتمبر أكتوبر نوفمبر ديسمبر'.split())}
MR='|'.join(M)
def last_month(s):
    ms=re.findall(r'(%s)\s*[–-]?\s*(20\d\d)?'%MR,s); ys=re.findall(r'20\d\d',s)
    if not ys: return None
    y=int(ys[-1])
    found=[(mm,yy) for mm,yy in re.findall(r'(%s)\s+(20\d\d)'%MR,s)]
    if found: mm,yy=found[-1]; return (int(yy),M[mm],'m')
    ms2=re.findall(MR,s)
    if ms2: return (y,M[ms2[-1]],'m')
    return (y,1,'y')
def first_out(s):
    f=re.findall(r'(%s)\s+(20\d\d)'%MR,s)
    if f: return (int(f[0][1]),M[f[0][0]],'m')
    ys=re.findall(r'\b(20\d\d)\b',s)
    return (int(ys[0]),12,'y') if ys else None
rows=[]
for x in ST:
    c=last_month(x['period'] or '')
    o=first_out(x['achievements'][0]) if x['achievements'] else None
    gap=None
    if c and o: gap=(o[0]-c[0])*12+o[1]-c[1]
    emp=any(t in x.get('categories',[]) for t in ('employment','leadership'))
    rows.append((x['id'],x['category'],emp,x['period'],c,o,gap,x['achievements'][0][:110] if x['achievements'] else ''))
json.dump(rows,open('audit_rows.json','w'),ensure_ascii=False)
bad=[r for r in rows if r[6] is None or r[6]>12 or r[6]<1 or not r[2]]
print(len(rows),'flag',len(bad))
for r in bad: print(r[0],'|',r[1],'|',r[3],'|',r[4],r[5],'gap',r[6],'|',r[7])
