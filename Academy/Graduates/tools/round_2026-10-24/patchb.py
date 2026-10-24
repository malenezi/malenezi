import json
N=json.load(open('new24b.json',encoding='utf-8'))
for r in N:
    if r[1]=='Ali Al-Ghamdi' and '#3241' not in r[9]: r[9]+=' إشارة: ليس #3241 «Ali Alghamdi» (ملف LinkedIn مختلف ali-gmidi، معسكر أكسفورد 2025).'
json.dump(N,open('new24b.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
p='apply24b.py'; s=open(p,encoding='utf-8').read()
L=s.split('\n')
for i,l in enumerate(L):
    if l.startswith('s=rep(s,"\'use strict\';"'):
        L[i]='''s=rep(s,"'use strict';","/* %s (ب): ملف الأكاديمية «May–Oct 2026» + حكمان (رويدا الشهري ليست قصة؛ علي الغامدي متدرب تعاوني) — %s ← %s خريجًا (%d جديدًا · %d إثراء)؛ القصص %d؛ جهات العمل %d. */\\n'use strict';"%(DATE,OTOT,TOT,len(new_ids),LOG['enr'],S1,E1),1)'''
    if "'تحديث':" in l:
        L[i]='''   'تحديث':f'{DATE} (ب) — ملف الأكاديمية May–Oct 2026: {len(new_ids)} سجلات جديدة ({OTOT} → {TOT})؛ {LOG["enr"]} إثراء؛ القصص {S1}؛ جهات العمل {E1}'}'''
    if l.startswith("s=rep(s,'**الإصدار:**"):
        L[i]='''s=rep(s,'**الإصدار:** 24 أكتوبر 2026 — ','**الإصدار:** %s (ب) — ملف الأكاديمية «May–Oct 2026» وحكمان (%s → %s · القصص %d · جهات العمل %d). قبله: 24 أكتوبر 2026 — '%(DATE,OTOT,TOT,S1,E1),1)'''
s='\n'.join(L)
a=s.index("L=['## جولة مسح"); b=s.index("for k in new_ids:\n    G_=g[k-1]; L.append")
s=s[:a]+'''L=['## ملف الأكاديمية «May–Oct 2026» وحكمان — %s (ب)'%DATE,'',f'**الخريجون {OTOT} → {TOT} · القصص {S1} · جهات العمل {E1}.**','',
 '**1) الحكمان (أ. د. ممدوح العنزي، 24 أكتوبر 2026):** رويدا الشهري #3545 ليست قصة نجاح؛ علي الغامدي متدرب تدريب تعاوني (مارس – يونيو 2024) فأُضيف سجلًا في مسار التعاوني.','',
 f'**2) ملف الأكاديمية (21 اسمًا):** 10 موجودون برابطهم، و7 طابقوا سجلات قائمة فأُثريت (روابط وبرامج إضافية)، و4 جدد. مع علي الغامدي: {len(new_ids)} سجلات جديدة.','','| # | الاسم | الاسم الإنجليزي | البرنامج | الدفعة | المسار | المصدر |','|---|---|---|---|---|---|---|']
'''+s[b:]
a=s.index("L+=['',f\"**2) الإثراء"); b=s.index("k=re.search")
s=s[:a]+'''L+=['',f"**3) الإثراء ({LOG['enr']}):** "+' · '.join('#%d %s'%(e['k'],g[e['k']-1]['n']) for e in ENR)+'.','','---','']
'''+s[b:]
open(p,'w',encoding='utf-8').write(s)
