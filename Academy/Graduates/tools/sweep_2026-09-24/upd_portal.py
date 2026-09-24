import os,json
st=json.load(open('stats24.json')); T=st['tracks']
P=os.path.expanduser('~/mnt/Academy/index.html'); s=open(P,encoding='utf-8').read()
def rep(a,b,n=1):
    global s; c=s.count(a); assert c==n,(a[:70],c); s=s.replace(a,b)
rep('data-count="2973"','data-count="%d"'%st['total'])
rep('<div class="sd-kpi__num" data-count="109">','<div class="sd-kpi__num" data-count="111">')
rep('<div class="sd-kpi__num" data-count="66">','<div class="sd-kpi__num" data-count="68">')
rep('<div class="v" data-count="1458">','<div class="v" data-count="%d">'%T['ai'])
rep('<div class="v" data-count="805">','<div class="v" data-count="%d">'%T['ds'])
rep('<div class="v" data-count="124">','<div class="v" data-count="%d">'%T['other'])
tot=format(st['total'],',')
n=s.count('2,973'); s=s.replace('2,973',tot); print('2,973 replaced',n)
rep('(109 قصة عبر 66 جهة عمل)','(111 قصة عبر 68 جهة عمل)')
rep('(109 stories across 66 employers)','(111 stories across 68 employers)')
rep('data-ar="109 قصة نجاح موثّقة لخريجي','data-ar="111 قصة نجاح موثّقة لخريجي')
rep('في 66 جهة عمل حكومية','في 68 جهة عمل حكومية')
rep('data-en="109 verified graduate success stories','data-en="111 verified graduate success stories')
rep('across 66 government, private','across 68 government, private')
rep('# موقع قصص النجاح — 109 قصة','# موقع قصص النجاح — 111 قصة')
rep('# success-stories site — 109 stories','# success-stories site — 111 stories')
rep('إصدار 22 سبتمبر 2026 (جولة مسح دفعتَي 2023 و2026 — %s سجلًا · 109 قصة · 6 مسارات)'%tot,'إصدار 24 سبتمبر 2026 (جولة مستودعات تسليم دفعات 2025–2026 — %s سجلًا · 111 قصة · 6 مسارات)'%tot)
rep('version 22 September 2026 (2023 &amp; 2026 cohort sweep — %s records · 109 st'%tot,'version 24 September 2026 (2025–2026 submission-repository sweep — %s records · 111 st'%tot)
link='<li><span class="ft md">MD</span><a href="Graduates/SDAIA_Stories_Round_2026-09-08.md" data-ar="جولة قصص النجاح — تواريخ الالتحاق عبر لينكدإن، 4 قصص (8 سبتمبر)" data-en="Success-story round — hire dates via LinkedIn, 4 stories (8 Sep)"></a></li>'
add=('<li><span class="ft md">MD</span><a href="Graduates/SDAIA_Cohort_Sweep_2026-09-22.md" data-ar="جولة مسح دفعتَي 2023 و2026 — 31 سجلًا وقصتان (22 سبتمبر)" data-en="2023 &amp; 2026 cohort sweep — 31 records, 2 stories (22 Sep)"></a></li>'
     '<li><span class="ft md">MD</span><a href="Graduates/SDAIA_Submission_Sweep_2026-09-24.md" data-ar="جولة مستودعات تسليم دفعات 2025–2026 — 113 سجلًا و21 إثراءً وقصتان (24 سبتمبر)" data-en="2025–2026 submission-repository sweep — 113 records, 21 enrichments, 2 stories (24 Sep)"></a></li>')
rep(link,link+add)
open(P,'w',encoding='utf-8').write(s)
for p in ['2,973','109 ','66 ','1458','"805"','22 سبتمبر 2026 (جولة']: print(p,s.count(p))
