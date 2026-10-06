import load,re,collections,json,unicodedata
D=load.load(); g=D['grads']
def slug(u):
    m=re.search(r'linkedin\.com/in/([^/?#]+)',u)
    return m.group(1).lower().rstrip('/') if m else None
def gh(u):
    m=re.match(r'https?://github\.com/([^/?#]+)/?$',u); return m.group(1).lower() if m else None
cl=collections.defaultdict(set); gcl=collections.defaultdict(set)
for i,r in enumerate(g,1):
    for l in r['links']:
        s=slug(l[1]); 
        if s: cl[s].add(i)
        o=gh(l[1])
        if o: gcl[o].add(i)
dup=[(s,sorted(v)) for s,v in cl.items() if len(v)>1]
gdup=[(s,sorted(v)) for s,v in gcl.items() if len(v)>1]
print('slug-shared clusters',len(dup)); 
for s,v in dup: print(' LI',s,[(i,g[i-1]['n'],g[i-1]['prog'][:30],g[i-1]['co'][:20]) for i in v])
print('gh-shared clusters',len(gdup))
for s,v in gdup: print(' GH',s,[(i,g[i-1]['n'],g[i-1]['prog'][:30]) for i in v])
def norm(t):
    t=re.sub('[إأآا]','ا',t); t=t.replace('ة','ه').replace('ى','ي'); t=re.sub(r'[ً-ْ]','',t)
    return ' '.join(t.lower().split())
nm=collections.defaultdict(list)
for i,r in enumerate(g,1): nm[norm(r['n'])].append(i)
ex=[(k,v) for k,v in nm.items() if len(v)>1]
print('exact-name groups',len(ex))
# hygiene
print('** in d',sum('**' in r['d'] for r in g))
print('double space',sum('  ' in r['d'] for r in g))
print('lead/trail ws n/en',sum(r['n']!=r['n'].strip() or r['en']!=r['en'].strip() for r in g))
print('latin in n, empty en',sum(bool(re.fullmatch(r'[A-Za-z .\-\']+',r['n'])) and not r['en'] for r in g))
print('dup links in record',sum(len({l[1].rstrip('/') for l in r['links']})<len(r['links']) for r in g))
print('country-sub linkedin',sum(bool(re.match(r'https?://[a-z]{2}\.linkedin\.com/in/',l[1])) for r in g for l in r['links']))
print('http (not https)',sum(l[1].startswith('http://') for r in g for l in r['links']))
print('empty prog',sum(not r['prog'].strip() for r in g),'empty co',sum(not r['co'].strip() for r in g))
print('tr values',collections.Counter(r['tr'] for r in g))
print('cats',collections.Counter(c for r in g for c in r['cats']))
print('emp without job cat',sum(bool(r['emp']) and 'job' not in r['cats'] for r in g))
