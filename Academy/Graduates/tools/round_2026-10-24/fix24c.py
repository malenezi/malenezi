import json,re,os,openpyxl
H=os.path.expanduser('~/mnt/Academy/')
# 1 Dona name
P=H+'Graduates/index.html'; s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+13; j=s.index('\nconst SITE_STATS'); D=json.loads(s[i:j].rstrip()[:-1]); g=D['grads']
k=[n for n,r in enumerate(g,1) if r['en']=='Dona Alsalhi']; assert len(k)==1; k=k[0]; r=g[k-1]
assert r['n']=='دانة الصالحي'; r['n']='دنا الصالحي'
TL=' تنويه: الاسم العربي نقل حرفي عن الاسم اللاتيني المنشور — غير متحقق علنًا.'
r['d']=r['d'].replace(TL,'')+' [24 أكتوبر 2026 (ج)] الاسم العربي «دنا الصالحي» مؤكَّد من أ. د. ممدوح العنزي.'
s=s[:i]+json.dumps(D,ensure_ascii=False)+';'+s[j:] if s[j-1]!=';' else s
# safer rebuild
s0=open(P,encoding='utf-8').read(); i0=s0.index('const DATA = ')+13; j0=s0.index('\nconst SITE_STATS')
open(P,'w',encoding='utf-8').write(s0[:i0]+json.dumps(D,ensure_ascii=False)+';'+s0[j0:])
X=H+'Graduates/Graduates_Database.xlsx'; wb=openpyxl.load_workbook(X); ws=wb['قاعدة البيانات']
assert ws.cell(k+1,1).value==k; ws.cell(k+1,2).value='دنا الصالحي'; ws.cell(k+1,21).value=r['d']
for sh in wb.worksheets:
    for row in sh.iter_rows():
        for c in row:
            if c.value=='دانة الصالحي': c.value='دنا الصالحي'
wb.save(X)
for f in ['Graduates/Graduates_Database.md']:
    t=open(H+f,encoding='utf-8').read(); print(f,t.count('دانة الصالحي')); open(H+f,'w',encoding='utf-8').write(t.replace('دانة الصالحي','دنا الصالحي'))
# 2 data.js
P3=H+'SuccessStories/website/js/data.js'; s=open(P3,encoding='utf-8').read()
print('datajs dana',s.count('دانة الصالحي')); s=s.replace('دانة الصالحي','دنا الصالحي')
for sid,fld,val in [('dona-alsalhi','orgLogo','assets/newera.jpg'),('shroog-alshamrani','photo','assets/shroog-alshamrani.jpg'),('norah-alobiwani','photo','assets/norah-alobiwani.jpg')]:
    assert os.path.exists(H+'SuccessStories/website/'+val)
    m=re.search(r'\{\s*"id": "%s"[^\n]*'%sid,s); line=m.group(0)
    m2=re.search(r'"%s": (?:"[^"]*"|null)'%fld,line)
    nl=line.replace(m2.group(0),'"%s": "%s"'%(fld,val),1) if m2 else line.replace('"photo":','"%s": "%s", "photo":'%(fld,val),1)
    assert nl!=line,sid; s=s.replace(line,nl,1)
open(P3,'w',encoding='utf-8').write(s)
print('ok',k)
