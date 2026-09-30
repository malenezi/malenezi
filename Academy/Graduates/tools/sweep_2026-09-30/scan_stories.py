import json,re,os,subprocess,collections
H=os.path.expanduser('~/mnt/Academy/')
s=open(H+'Graduates/index.html',encoding='utf-8').read()
i=s.index('const DATA = ')+13; j=s.index('\nconst SITE_STATS'); g=json.loads(s[i:j].rstrip()[:-1])['grads']
js=r"""
const fs=require('fs'),vm=require('vm');let src=fs.readFileSync(process.argv[1],'utf8').replace(/^const /mg,'var ');
const c={};vm.createContext(c);vm.runInContext(src,c);
console.log(JSON.stringify(c.STORIES.map(s=>({id:s.id,name:s.name,nameEn:s.nameEn||s.name_en||'',org:s.org,year:s.year,links:(s.links||[]).map(l=>l.url||l[1]||''),prov:s.provenance||''}))));
"""
open('/tmp/st.js','w').write(js)
ST=json.loads(subprocess.check_output(['node','/tmp/st.js',H+'SuccessStories/website/js/data.js']))
print('stories',len(ST))
def norm(n):
    n=re.sub('[أإآ]','ا',n or ''); n=n.replace('ة','ه').replace('ى','ي'); return re.sub(r'\s+',' ',n).strip()
slug=lambda u:(re.search(r'linkedin\.com/in/([^/?#]+)',u or '') or [None,None])[1]
story_ids=set(); unmatched=[]
for st in ST:
    hit=None
    m=re.findall(r'#(\d{1,4})',st['prov'])
    sl={slug(u).lower() for u in st['links'] if slug(u)}
    for k,x in enumerate(g,1):
        xs={slug(u).lower() for l,u in x['links'] if slug(u)}
        if (sl & xs) or norm(x['n'])==norm(st['name']) or (x.get('alias') and norm(st['name']) in norm(x.get('alias',''))):
            hit=k; story_ids.add(k)
    if not hit: unmatched.append(st['id'])
print('story-mapped records',len(story_ids),'unmatched stories',unmatched)
AR={'يناير':1,'فبراير':2,'مارس':3,'أبريل':4,'ابريل':4,'مايو':5,'يونيو':6,'يوليو':7,'أغسطس':8,'اغسطس':8,'سبتمبر':9,'أكتوبر':10,'اكتوبر':10,'نوفمبر':11,'ديسمبر':12}
EN={m:i for i,m in enumerate(['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'],1)}
MRX=r'(%s|%s)[a-z]*\.?'%('|'.join(AR),'|'.join(k.capitalize() for k in EN)+'|'+'|'.join(EN))
def dates(t):
    out=[]
    for m in re.finditer(r'(?:(\S+)\s+)?(20[12]\d)',t or ''):
        w=(m.group(1) or '').strip('(«»,.').lower()
        mo=AR.get(m.group(1).strip('(«»,.') if m.group(1) else '',None) or EN.get(w[:3]) if w else None
        out.append((int(m.group(2)),mo))
    return out
def completion(co):
    ds=dates(co)
    if not ds: return None
    y,mo=ds[-1]
    if mo is None:
        # range like "يوليو–أكتوبر 2024"
        mm=[AR[w] for w in re.findall('|'.join(AR),co)]
        mo=mm[-1] if mm else None
    return (y,mo)
DONE=re.compile(r'FAIL_|CERT_ONLY|HELD_|PASS_|§5|لا قصة|لا نتيجة مؤهلة|مُرقّ[اى] إلى قصة|قصة نجاح \(|غير مؤهل|قيد التحقق')
rows=[]
for k,x in enumerate(g,1):
    if k in story_ids: continue
    emp=(x.get('emp') or '').strip(); role=(x.get('role') or '').strip()
    cats=set(x.get('cats') or [])
    if not emp and not (cats & {'award','promo','startup','research','job'}): continue
    c=completion(x.get('co') or '')
    od=dates(role)+dates(emp)
    prior=bool(DONE.search(x.get('d') or ''))
    rows.append(dict(id=k,n=x['n'],en=x.get('en',''),co=x.get('co',''),emp=emp,role=role,cats=sorted(cats),comp=c,od=od,prior=prior,li=[u for l,u in x['links'] if 'linkedin.com/in/' in u][:1],tr=x['tr'],score=x['score']))
def window(c,o):
    if not c or not o: return 'nodate'
    cy,cm=c; oy,om=o
    cm_eff=cm or 1
    end=cy*12+cm_eff-1+14
    if om is None:
        last=oy*12+11
        if last>end: return 'out'
        first=oy*12
        if oy*12+11 <= cy*12+cm_eff-1: return 'before'
        return 'pass?'
    t=oy*12+om-1
    if t<=cy*12+cm_eff-1: return 'before/sim'
    return 'pass' if t<=end else 'out'
cand=[]
for r in rows:
    vs=[window(r['comp'],o) for o in r['od']] or ['nodate']
    r['win']=vs
    if any(v in ('pass','pass?') for v in vs): cand.append(r)
print('records with employer/outcome (non-story):',len(rows),' prior-adjudicated:',sum(r['prior'] for r in rows))
print('timing candidates:',len(cand),' of which not previously adjudicated:',sum(not r['prior'] for r in cand))
json.dump({'rows':rows,'cand':cand,'story_ids':sorted(story_ids)},open('scan_out.json','w'),ensure_ascii=False)
for r in cand:
    print(('NEW ' if not r['prior'] else 'adj ')+'#%d %s | co=%s | emp=%s | role=%s | %s'%(r['id'],r['n'],r['co'][:40],r['emp'][:40],r['role'][:50],r['win']))
