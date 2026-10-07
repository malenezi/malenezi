import json,os
H=os.path.expanduser('~/mnt/Academy/')
def load():
    s=open(H+'Graduates/index.html',encoding='utf-8').read()
    i=s.index('const DATA = ')+len('const DATA = '); j=s.index('\nconst SITE_STATS')
    raw=s[i:j].rstrip(); return json.loads(raw[:-1])
def stories():
    import subprocess,json
    js=r"""
const fs=require('fs'),vm=require('vm');let s=fs.readFileSync(process.argv[1],'utf8').replace(/\bconst\b/g,'var').replace(/\blet\b/g,'var');
const c={};vm.createContext(c);vm.runInContext(s,c);process.stdout.write(JSON.stringify({S:c.STORIES,ST:c.SITE_STATS}));"""
    o=subprocess.run(['node','-e',js,H+'SuccessStories/website/js/data.js'],capture_output=True,text=True,encoding='utf-8')
    return json.loads(o.stdout)
