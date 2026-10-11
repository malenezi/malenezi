import json,os,sys
sys.path[:0]=[os.path.expanduser('~/mnt/Academy/Graduates/tools/round_2026-10-07'),os.path.expanduser('~/mnt/Academy/Graduates/tools')]
import translit as TR
H=os.path.expanduser('~/mnt/Academy/Graduates/index.html'); s=open(H,encoding='utf-8').read()
i=s.index('const DATA = ')+13;j=s.index('\nconst SITE_STATS'); g=json.loads(s[i:j].rstrip()[:-1])['grads']
idx=TR.build_index(g)
for n in sys.argv[1].split(';'):
    m=TR.match('',n,idx)
    ex=[k+1 for k,r in enumerate(g) if (r.get('en') or '').lower().replace('-','')==n.lower().replace('-','')]
    print(n,'| exact',ex,'| tr',[(x[0],g[x[0]-1]['en'] or g[x[0]-1]['n'],(g[x[0]-1]['prog'] or '')[:35],(g[x[0]-1]['co'] or '')[:20]) for x in m[:3]])
