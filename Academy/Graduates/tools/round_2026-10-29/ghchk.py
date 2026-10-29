import json,re,sys,os
H=os.path.expanduser('~/mnt/Academy/')
s=open(H+'Graduates/index.html',encoding='utf-8').read()
i=s.index('const DATA = ')+13; j=s.index('\nconst SITE_STATS'); g=json.loads(s[i:j].rstrip()[:-1])['grads']
OW={};RP={}
for k,r in enumerate(g,1):
    for l in r['links']:
        m=re.search(r'github\.com/([^/?#]+)(?:/([^/?#]+))?',l[1])
        if m: OW.setdefault(m.group(1).lower(),k); 
        if m and m.group(2): RP.setdefault((m.group(1)+'/'+m.group(2)).lower(),k)
# also check notes text for owners
TXT=' '.join((r.get('d') or '') for r in g).lower()
known_ex=open('ghseen.txt').read().split() if os.path.exists('ghseen.txt') else []
for nm in sys.stdin.read().split():
    o=nm.split('/')[0].lower()
    if o in OW: continue
    tag='MENTIONED' if o in TXT else 'NEW'
    print(tag,nm)
