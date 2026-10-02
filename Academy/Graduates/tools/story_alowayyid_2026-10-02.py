import json,re,shutil,os,openpyxl
B='backup-2026-10-02'
def bk(p):
    a,b=os.path.splitext(p); shutil.copy2(p,f'{a}.{B}{b}')
files=['SuccessStories/website/js/data.js','SuccessStories/website/index.html','index.html','Graduates/index.html','Graduates/Graduates_Database.xlsx','Graduates/Graduates_Database.md']
for f in files: bk(f)
def rw(p,fn):
    s=open(p,encoding='utf-8').read(); t=fn(s); assert t!=s,p; open(p,'w',encoding='utf-8').write(t)

CO='أكتوبر–ديسمبر 2023'
NOTE=(' [تحديد شهر الإتمام — 2 أكتوبر 2026] زوّدت الأكاديمية تواريخ إصدار شهادات البرامج الثلاث (من قسم الشهادات في ملفه على LinkedIn): '
 'معسكر تعلم الآلة 100 ساعة (أكتوبر 2023) · ممارس تعلم الآلة (نوفمبر 2023) · معسكر إدارة البيانات 100 ساعة (ديسمبر 2023). '
 'الإتمام = ديسمبر 2023، ونافذة الأربعة عشر شهرًا تمتد حتى فبراير 2025. التحاقه بالبنك العربي الوطني أخصائيَّ تجزئة/محلل بيانات '
 '(أغسطس 2024) يقع بعد ثمانية أشهر، ودور تحليل البيانات ذو صلة مباشرة بالتدريب؛ وتدريب سايت (فبراير–أغسطس 2024) لا يُحتسب. '
 'PASS_DATED — مُرقّى إلى قصة نجاح «abdullah-alowayyid»؛ أُغلقت حالة «قيد التحقق».')

story={"id":"abdullah-alowayyid","year":2023,
 "quote":{"text":"جمعتُ في أكاديمية سدايا بين تعلم الآلة وإدارة البيانات، ومنها انتقلت إلى أول دور لي في تحليل البيانات في القطاع المصرفي.","kind":"draft"},
 "name":"عبدالله العويد","nameEn":"Abdullah Alowayyid","photo":"assets/abdullah-alowayyid.jpg",
 "role":"أخصائي تجزئة / محلل بيانات","org":"البنك العربي الوطني (ANB)","orgLogo":None,
 "program":"معسكر تعلم الآلة + ممارس تعلم الآلة + معسكر إدارة البيانات — أكاديمية سدايا","period":CO,
 "category":"employment","categories":["employment"],
 "impact":"التحاق بالبنك العربي الوطني «أخصائي تجزئة / محلل بيانات» في أغسطس 2024 — بعد ثمانية أشهر من إتمام آخر برامجه في الأكاديمية.",
 "story":"أتمّ عبدالله ثلاثة برامج متتالية في أكاديمية سدايا: معسكر تعلم الآلة (100 ساعة، أكتوبر 2023)، وشهادة ممارس تعلم الآلة (نوفمبر 2023)، ومعسكر إدارة البيانات (100 ساعة، ديسمبر 2023)، وذلك بعد تخرّجه في تقنية المعلومات من جامعة القصيم (2023). وبعد تدريب في هندسة الشبكات والسحابة لدى سايت (فبراير–أغسطس 2024) — وهو تدريب لا يُحتسب — التحق في أغسطس 2024 بالبنك العربي الوطني أخصائيَّ تجزئة ومحللَ بيانات، ثم عاد إلى سايت مهندسَ عمليات سحابية في يناير 2025. النتيجة المحتسبة هي الالتحاق بدور تحليل البيانات في البنك العربي الوطني، بعد ثمانية أشهر من الإتمام.",
 "achievements":["معسكر تعلم الآلة 100 ساعة (أكتوبر 2023) وشهادة ممارس تعلم الآلة (نوفمبر 2023) — أكاديمية سدايا","معسكر إدارة البيانات 100 ساعة — أكاديمية سدايا (ديسمبر 2023)","أخصائي تجزئة / محلل بيانات — البنك العربي الوطني (أغسطس 2024)","مهندس عمليات سحابية — سايت (منذ يناير 2025)"],
 "links":[{"label":"LinkedIn","url":"https://www.linkedin.com/in/abdullah-alowayid/"}],
 "provenance":"تواريخ إصدار شهادات البرامج الثلاث بمستوى الشهر من قسم الشهادات في ملفه على LinkedIn (Machine Learning Bootcamp 100h — أكتوبر 2023؛ Machine Learning Practitioner — نوفمبر 2023؛ Data Management Bootcamp 100h — ديسمبر 2023)، مورّدة من الأكاديمية 2 أكتوبر 2026 + صفحة الخبرة على LinkedIn بحساب مسجَّل (سايت — متدرب فبراير–أغسطس 2024؛ البنك العربي الوطني أغسطس–ديسمبر 2024؛ سايت — مهندس عمليات سحابية منذ يناير 2025؛ قُرئت 22 سبتمبر 2026) + سجل الأكاديمية #2."}

# 1 data.js
def f_data(s):
    i=s.rindex('];'); s=s[:i]+'  '+json.dumps(story,ensure_ascii=False)+',\n'+s[i:]
    s=s.replace("'use strict';","/* 2 أكتوبر 2026: قصة عبدالله العويد — حُسمت حالة «قيد التحقق» بشهر الإتمام (ديسمبر 2023، من شهادات البرامج الثلاث) ← البنك العربي الوطني أغسطس 2024 (+8 أشهر). 117 ← 118 قصة، وجهات العمل 72 ← 73 (البنك العربي الوطني). */\n'use strict';",1)
    s,n1=re.subn(r"(\{ value: )117(,\s+label: 'قصة نجاح)",r"\g<1>118\2",s)
    s,n2=re.subn(r"(\{ value: )72(,\s+label: 'جهة عمل')",r"\g<1>73\2",s); assert n1==n2==1
    return s
rw('SuccessStories/website/js/data.js',f_data)
rw('SuccessStories/website/index.html',lambda s:s.replace('"numberOfItems": 117','"numberOfItems": 118'))
REP=[('data-count="117"','data-count="118"'),('data-count="72"','data-count="73"'),('117 قصة','118 قصة'),('117 stories','118 stories'),('117 verified','118 verified'),('72 جهة عمل','73 جهة عمل'),('72 employers','73 employers'),('across 72 government','across 73 government')]
def f_rep(s):
    for a,b in REP: s=s.replace(a,b)
    return s
rw('index.html',f_rep)
# Graduates page
def f_grads(s):
    s=f_rep(s); s,n=re.subn(r"(\{ value: )117(,\s+label: 'قصة نجاح)",r"\g<1>118\2",s); assert n==1
    i=s.index('const DATA = {"grads"'); j=s.index('[',i); d=0;k=j
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
    g=json.loads(s[j:k+1]); r=g[1]; assert r['en']=='Abdullah Alowayyid'
    r['co']=CO; r['d']+=NOTE
    if 'project' not in r['cats'] and 'job' not in r['cats']: r['cats'].append('job')
    return s[:j]+json.dumps(g,ensure_ascii=False)+s[k+1:]
rw('Graduates/index.html',f_grads)
# xlsx
wb=openpyxl.load_workbook('Graduates/Graduates_Database.xlsx'); ws=wb['قاعدة البيانات']
assert ws.cell(3,1).value==2 and ws.cell(3,3).value=='Abdullah Alowayyid'
ws.cell(3,6).value=CO; ws.cell(3,21).value=(ws.cell(3,21).value or '')+NOTE
st=wb['إحصاءات']
for row in st.iter_rows():
    if row[0].value=='قصص النجاح': row[1].value=118
    if row[0].value=='جهات العمل': row[1].value=73
    if row[0].value=='تحديث': row[1].value='2 أكتوبر 2026 — قصة عبدالله العويد (#2): شهر الإتمام ديسمبر 2023 من شهادات البرامج الثلاث ← البنك العربي الوطني أغسطس 2024 (+8). القصص 117 → 118 · جهات العمل 72 → 73'
wb.save('Graduates/Graduates_Database.xlsx')
# md
def f_md(s):
    lines=s.split('\n')
    for idx,l in enumerate(lines):
        if l.startswith('| 2 | عبدالله العويد | Abdullah Alowayyid |'):
            c=l.split(' | '); assert c[5]=='2023',c[5]; c[5]=CO; lines[idx]=' | '.join(c)
        elif l.startswith('| #2 | عبدالله العويد |'):
            lines[idx]='| #2 | عبدالله العويد | محلل بيانات/أخصائي تجزئة — البنك العربي الوطني (أغسطس 2024) | ✅ **حُسمت 2 أكتوبر 2026** — الإتمام ديسمبر 2023 (شهادات البرامج الثلاث) ← +8 أشهر؛ نُشرت قصة «abdullah-alowayyid». |'
    s='\n'.join(lines)
    sec=('\n## قصة عبدالله العويد — 2 أكتوبر 2026\n\n**قصص النجاح 117 → 118 · جهات العمل 72 → 73** (البنك العربي الوطني).\n\n'
         '- **#2 عبدالله العويد** — كانت الحالة «قيد التحقق» لأن الدفعة مسجّلة بالسنة فقط (2023). زوّدت الأكاديمية تواريخ إصدار الشهادات: معسكر تعلم الآلة (أكتوبر 2023) · ممارس تعلم الآلة (نوفمبر 2023) · معسكر إدارة البيانات (ديسمبر 2023).\n'
         '- الإتمام = ديسمبر 2023 · النافذة حتى فبراير 2025 · البنك العربي الوطني أخصائي تجزئة/محلل بيانات أغسطس 2024 = **+8 أشهر** · صلة مباشرة · تدريب سايت لا يُحتسب ← **PASS_DATED**.\n'
         '- الدفعة في السجل: «2023» ← «أكتوبر–ديسمبر 2023».\n\n---\n')
    i=s.index('\n---\n'); s=s[:i+5]+sec+s[i+5:]
    s=s.replace('**الإصدار:** ','**الإصدار:** 2 أكتوبر 2026 — قصة عبدالله العويد (117 → 118 · جهات العمل 72 → 73). قبله: ',1)
    return s
rw('Graduates/Graduates_Database.md',f_md)
print('ok')
