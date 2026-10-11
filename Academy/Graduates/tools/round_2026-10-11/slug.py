import json,os,sys
H=os.path.expanduser('~/mnt/Academy/Graduates/index.html'); s=open(H,encoding='utf-8').read()
i=s.index('const DATA = ')+13;j=s.index('\nconst SITE_STATS'); g=json.loads(s[i:j].rstrip()[:-1])['grads']
for sl in sys.argv[1].split(','):
    h=[k+1 for k,r in enumerate(g) if any(('/in/'+sl.lower()) in l[1].lower() for l in r['links'])]
    print(sl,h)
