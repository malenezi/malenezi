import json,re,openpyxl,collections,shutil,os
TAG='[إكمال الفجوات — 2 أكتوبر 2026] '
U={}  # id -> (co, note)
for i in range(168,180): U[i]=('أكتوبر 2024','شهر الإتمام من اسم الدفعة في حقل البرنامج نفسه («T5 أكتوبر 2024»، فرق مشاريع التخرج).')
C04=[2229,2230,2231,2232,2233,2234,2235,2236,2237,2239,2240,2241,2242,2243,2245]
for i in C04: U[i]=('سبتمبر–نوفمبر 2021','فصل C04 من معسكر T5 مؤرَّخ «سبتمبر–نوفمبر 2021» بكشف الفصل (#2240) وبحقل برنامج #2229، ويعضده تاريخ إصدار شهادة المعسكر «نوفمبر 2021» على LinkedIn لزميلَي الفصل محمد عسيلان ونورة الخليفة.')
U[2231]=(U[2231][0],U[2231][1]+' شهادته «Data Science (T5 Bootcamp) — SDAIA» صادرة نوفمبر 2021 (قسم الشهادات على LinkedIn).')
U[2232]=(U[2232][0],U[2232][1]+' شهادتها «SDAIA T5 Data Science Bootcamp — SDAIA Academy» صادرة نوفمبر 2021 (قسم الشهادات على LinkedIn).')
for i in (2246,2247): U[i]=('نوفمبر–ديسمبر 2021','فصل C06 من معسكر T5 مؤرَّخ «نوفمبر–ديسمبر 2021» في حقل برنامج #2246.')
U[2265]=('يوليو–أكتوبر 2024','تواريخ المعسكر مذكورة في حقل البرنامج نفسه (T5 Zeham يوليو–أكتوبر 2024)، ومستودعها أُنشئ 17 أكتوبر 2024.')
U[2698]=('يوليو–أكتوبر 2024','قيد «SDAIA T5 Bootcamp» يوليو–أكتوبر 2024 في صفحة خبرتها على LinkedIn (مذكور في الأدلة منذ 28 أغسطس).')
U[2268]=('يوليو–أكتوبر 2024','دفعة T5 2024 (يوليو–أكتوبر)، ومستودع مشروع التخرج SmartDashcam أُنشئ 27 أكتوبر 2024.')
U[13]=('ديسمبر 2025 – يناير 2026','شهادة NVIDIA ديسمبر 2025 واجتياز NCA-GENL ضمن برنامج الأكاديمية يناير 2026 (كلاهما في الأدلة القائمة).')
LI={17:('ديسمبر 2023','«LLMs Practitioner — SDAIA | سدايا» صادرة ديسمبر 2023'),
 19:('نوفمبر 2023','«ML practitioner — SDAIA | سدايا» صادرة نوفمبر 2023'),
 204:('يناير 2026','NCA-GENL صادرة يناير 2026'),
 220:('يوليو 2026','NCA-GENL صادرة يوليو 2026'),
 240:('مايو 2026','«Professional Training Program in Large Language Models (NVIDIA) — SDAIA» صادرة مايو 2026، ودورات NVIDIA DLI يناير 2026'),
 247:('يوليو 2026','«Professional Training Program In Large Language Models (NVIDIA) — SDAIA» صادرة يوليو 2026 مع NCA-GENL يوليو 2026'),
 248:('يوليو 2026','NCA-GENL صادرة يوليو 2026؛ وتحمل كذلك اعتماد «SDAIA Associate AI Engineer» (سبتمبر 2026)'),
 250:('مايو 2026','«برنامج التدريب الاحترافي للنماذج اللغوية الكبيرة (إنفيديا) — SDAIA» صادرة مايو 2026 ثم NCA-GENL يوليو 2026'),
 261:('أبريل–يوليو 2026','دورات NVIDIA DLI أبريل 2026 ثم NCA-GENL يوليو 2026'),
 279:('فبراير 2025','NCA-GENL وNCA Multimodal صادرتان فبراير 2025'),
 282:('يناير–فبراير 2025','دورة NVIDIA DLI يناير 2025 ثم NCA-GENL وNCA Multimodal فبراير 2025'),
 323:('يوليو 2025','NCA-GENL وNCA Multimodal صادرتان يوليو 2025'),
 334:('يوليو 2025','NCA Multimodal صادرة يوليو 2025؛ وتحمل كذلك «Quantum Computing Bootcamp — SDAIA» (يناير 2026) واعتماد «Expert AI Engineer — SDAIA» (سبتمبر 2026)'),
 376:('نوفمبر 2025','دورة NVIDIA DLI «Building Transformer-Based NLP Applications» نوفمبر 2025؛ وبرنامج ثانٍ: «SDAIA T5 Data Science Bootcamp — SDAIA» صادرة ديسمبر 2023'),
 384:('ديسمبر 2025','NCA-GENL صادرة ديسمبر 2025'),
 396:('ديسمبر 2025','«Professional Training in Large Language Models — SDAIA» صادرة ديسمبر 2025 مع NCA-GENL ديسمبر 2025'),
 401:('ديسمبر 2025','NCA-GENL صادرة ديسمبر 2025 مع «Professional Training in Large Language Models — SDAIA»')}
for i,(c,n) in LI.items(): U[i]=(c,'تاريخ الإتمام من قسم الشهادات على LinkedIn (حساب مسجَّل): '+n+'.')
AR=re.compile(r'[؀-ۿ]');LA=re.compile(r'^[A-Za-z]')
# --- xlsx
wb=openpyxl.load_workbook('Graduates_Database.xlsx'); ws=wb['قاعدة البيانات']
names={}; en_fixed=[]
for r in range(2,ws.max_row+1):
    i=ws.cell(r,1).value
    if i is None: continue
    assert r==i+1
    names[i]=ws.cell(r,2).value
    if i in U:
        old=ws.cell(r,6).value; ws.cell(r,6).value=U[i][0]
        ws.cell(r,21).value=(ws.cell(r,21).value or '')+' '+TAG+U[i][1]+f' (كانت الدفعة: «{old or "فارغة"}»).'
    n=ws.cell(r,2).value
    if n and LA.match(str(n)) and not AR.search(str(n)) and not ws.cell(r,3).value:
        ws.cell(r,3).value=str(n).strip(); en_fixed.append(i)
wb.save('Graduates_Database.xlsx')
# --- html
p='index.html'; s=open(p,encoding='utf-8').read()
i0=s.index('const DATA = {"grads"'); j=s.index('[',i0); d=0;k=j
while True:
    c=s[k]
    if c=='[': d+=1
    elif c==']':
        d-=1
        if d==0: break
    elif c=='"':
        k+=1
        while s[k]!='"':
            if s[k]=='\\': k+=1
            k+=1
    k+=1
g=json.loads(s[j:k+1])
for i,(co,note) in U.items():
    r=g[i-1]; assert r['n']==names[i],(i,r['n'],names[i])
    old=r.get('co'); r['co']=co; r['d']=(r.get('d') or '')+' '+TAG+note+f' (كانت الدفعة: «{old or "فارغة"}»).'
for i in en_fixed:
    r=g[i-1]; assert r['n']==names[i]
    if not r.get('en'): r['en']=r['n']
s=s[:j]+json.dumps(g,ensure_ascii=False)+s[k+1:]; open(p,'w',encoding='utf-8').write(s)
json.dump({'months':{str(i):v[0] for i,v in U.items()},'en_fixed':en_fixed},open('tools/round_2026-10-02/phase1_changes.json','w'),ensure_ascii=False)
print('months',len(U),'en fixed',len(en_fixed))
