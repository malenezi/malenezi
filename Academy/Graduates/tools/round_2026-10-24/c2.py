import sys,subprocess
rows=[l.strip().split('|') for l in open(sys.argv[1],encoding='utf-8') if l.strip()]
open('_t.txt','w',encoding='utf-8').write('\n'.join(r[1]+'|https://www.linkedin.com/in/'+r[0]+'/' for r in rows))
out=subprocess.run([sys.executable,'chk.py','_t.txt'],capture_output=True,text=True,encoding='utf-8').stdout.splitlines()[1:]
for r,o in zip(rows,out):
    if not o.startswith('LINK'): print(o[:150],'||',r[2])
