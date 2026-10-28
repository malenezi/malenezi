import json,re,os,sys,openpyxl,shutil
H=os.path.expanduser('~/mnt/Academy/'); TAG='[تدقيق ختامي 28 أكتوبر 2026] '
BK=H+'_backups/2026-10-28c/'; os.makedirs(BK,exist_ok=True)
for f in ('Graduates/index.html','Graduates/Graduates_Database.xlsx'): shutil.copy2(H+f,BK+f.replace('/','__'))
P=H+'Graduates/index.html'; s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+13;j=s.index('\nconst SITE_STATS');D=json.loads(s[i:j].rstrip()[:-1]);g=D['grads']
wb=openpyxl.load_workbook(H+'Graduates/Graduates_Database.xlsx'); ws=wb['قاعدة البيانات']
def note(k,t):
    g[k-1]['d']=(g[k-1]['d']+' '+TAG+t).strip(); ws.cell(k+1,21).value=((ws.cell(k+1,21).value or '')+' '+TAG+t).strip()
F={}
# 1 whitespace
n=0
for k,r in enumerate(g,1):
    for fld,col in (('n',2),('en',3),('prog',4),('co',6),('emp',7),('role',8),('d',21)):
        v=r.get(fld)
        if isinstance(v,str):
            nv=re.sub(r'[ \t ]{2,}',' ',v).strip()
            if nv!=v:
                r[fld]=nv; n+=1
                if ws.cell(k+1,col).value: ws.cell(k+1,col).value=re.sub(r'[ \t ]{2,}',' ',str(ws.cell(k+1,col).value)).strip()
F['ws']=n
# 2 story-linked records missing job category
for k,emp,role in ((2456,'تمكين للتقنيات','محللة أمن شبكات — ثم مهندسة أمن سحابي أولى (Senior Cloud Security Engineer)'),(452,None,None),(538,None,None)):
    r=g[k-1]
    if 'job' not in r['cats']: r['cats'].append('job')
    if emp and not r['emp']: r['emp']=emp; ws.cell(k+1,7).value=emp
    if role and r['role'] in ('','خريج / Trainee'): r['role']=role; ws.cell(k+1,8).value=role
    note(k,'مواءمة مع بطاقة قصة النجاح المنشورة: أُضيفت فئة «وظيفة»'+('، وجهة العمل والمسمى من البطاقة.' if emp else '.'))
F['job']=3
# 3 cross-notes for same-Latin-name pairs
CN=[(334,425,'مرشح دمج: الاسم الثلاثي نفسه «Ahad Awad Al Grais / Algrais» (لقب مميز) — برنامجان مختلفان (LLM 2023 وشهادات NVIDIA 2025). لم يُدمج دون تفويض.'),
    (358,541,'مرشح دمج: الاسم الثلاثي نفسه «Khawla Ahmed Al Matar / Almatar» (لقب مميز) — برنامجان مختلفان (ML 2023 وشهادات NVIDIA). لم يُدمج دون تفويض.'),
    (583,3044,'إشارة: الاسم نفسه «Mohammed Alsayed» — اسم شائع بلا تعزيز (ML 2023 مقابل هندسة البيانات 2026). لا يُدمج.'),
    (2106,2394,'لا يُدمج: الاسم نفسه «Shatha Alghamdi» لكن حسابا GitHub مختلفان (Shatha-CS / ShathaAlghamdi) وبرنامجان متباعدان (T5 2021 / AAI 2026).')]
for a,b,t in CN: note(a,t.replace('لم يُدمج','#%d — لم يُدمج'%b) if '#%d'%b not in t else t); note(b,'#%d — '%a+t)
F['crossnotes']=len(CN)*2
D['grads']=g; open(P,'w',encoding='utf-8').write(s[:i]+json.dumps(D,ensure_ascii=False)+';'+s[j:]); wb.save(H+'Graduates/Graduates_Database.xlsx'); print(F)
