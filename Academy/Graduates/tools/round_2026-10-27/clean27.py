import json,re,os,sys,openpyxl
DRY='--apply' not in sys.argv
P='Graduates/index.html'; s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+13; j=s.index('\nconst SITE_STATS')
D=json.loads(s[i:j].rstrip()[:-1]); g=D['grads']
sj=open('SuccessStories/website/js/data.js',encoding='utf-8').read()
k=sj.index('const STORIES = ['); e=sj.index('\n];',k)
ST=[json.loads(l.strip().rstrip(',')) for l in sj[k:e].split('\n')[1:] if l.strip().startswith('{')]
print('stories parsed',len(ST))
ar=lambda t:bool(re.search('[؀-ۿ]',t or ''))
fix=[]
for x in ST:
    refs=[int(m) for m in re.findall(r'#(\d{1,4})\b',x.get('provenance',''))]
    for ref in refs[-1:]:
        r=g[ref-1]
        if not ar(r['n']) and ar(x['name']) and (r.get('en') or r['n']).split()[0].lower()[:4] in (x.get('nameEn') or '').lower():
            fix.append((ref,r['n'],x['name']))
for f in fix: print(f)
if DRY: sys.exit()
wb=openpyxl.load_workbook('Graduates/Graduates_Database.xlsx'); ws=wb['قاعدة البيانات']
for ref,old,new in fix:
    r=g[ref-1]; 
    if not r.get('en'): r['en']=old; ws.cell(ref+1,3).value=old
    r['n']=new; assert ws.cell(ref+1,1).value==ref; ws.cell(ref+1,2).value=new
    r['d']=(r['d']+' [جولة 27 أكتوبر 2026 — تنظيف] أُكمل الاسم العربي من بطاقة قصة النجاح المنشورة (كان السجل لاتيني الاسم فقط).').strip()
    ws.cell(ref+1,21).value=r['d']
D['grads']=g; open(P,'w',encoding='utf-8').write(s[:i]+json.dumps(D,ensure_ascii=False)+';'+s[j:]); wb.save('Graduates/Graduates_Database.xlsx'); print('applied',len(fix))
