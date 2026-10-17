# -*- coding: utf-8 -*-
import json,re,os,openpyxl
H=os.path.expanduser('~/mnt/Academy/')
TAG='[جولة 17 أكتوبر 2026 (ب)] '
def rep(s,a,b,n=1):
    assert s.count(a)==n,(a[:80],s.count(a)); return s.replace(a,b)
P=H+'Graduates/index.html'; s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+len('const DATA = '); j=s.index('\nconst SITE_STATS')
D=json.loads(s[i:j].rstrip()[:-1]); g=D['grads']; G=g[197]; assert G['en']=='Yazeed Mohammed Ali Alobaidan'
ORG='بنك الجزيرة (Bank Aljazira)'; ROLE='مدير مساعد — تحليلات البيانات والذكاء الاصطناعي (AI & Data Analytics Assistant Manager) — أغسطس 2026'
NOTE='صفحتا الخبرة والشهادات على LinkedIn (حساب مسجَّل، قُرئتا 17 أكتوبر 2026): دورات NVIDIA الخمس وNVIDIA-Certified Associate: Generative AI LLMs صادرة في يناير 2026؛ Bank Aljazira — Data and AI GDP (أغسطس 2025 – أغسطس 2026) ثم AI & Data Analytics Assistant Manager (أغسطس 2026 – الآن). PASS_DATED (+7): ترقية إلى دور ذي صلة مباشرة — السياسة 1.0، البند 2 (ترقية أو انتقال داخلي إلى دور ذي صلة)، وبقرار المدير العام 17 أكتوبر 2026. مُرقّى إلى قصة نجاح «yazeed-alobaidan».'
G['emp']=ORG; G['role']=ROLE; G['co']='يناير 2026 (إصدار شهادات NVIDIA)'
if 'job' not in G['cats']: G['cats'].append('job')
G['d']+=' '+TAG+NOTE
s=s[:i]+json.dumps(D,ensure_ascii=False)+';'+s[j:]
s=rep(s,"value: 175,   label: 'قصة نجاح موثّقة',","value: 176,   label: 'قصة نجاح موثّقة',")
s=rep(s,"عبر 94 جهة عمل","عبر 95 جهة عمل"); s=rep(s,"across 94 employers","across 95 employers")
open(P,'w',encoding='utf-8').write(s)
X=H+'Graduates/Graduates_Database.xlsx'; wb=openpyxl.load_workbook(X); ws=wb['قاعدة البيانات']
assert ws.cell(199,1).value==198
ws.cell(199,6).value=G['co']; ws.cell(199,7).value=ORG; ws.cell(199,8).value=ROLE; ws.cell(199,21).value=(ws.cell(199,21).value or '')+' '+TAG+NOTE
sh=wb['جولة_17_أكتوبر_2026_ب']; sh.append([198,G['n'],'قصة جديدة',ORG+' — مدير مساعد، تحليلات البيانات والذكاء الاصطناعي'])
st=wb['إحصاءات']
for row in st.iter_rows():
    if row[0].value=='سجلات بجهة عمل موثّقة': row[1].value=sum(1 for r in g if r.get('emp'))
    if row[0].value=='تحديث' and isinstance(row[1].value,str): row[1].value=row[1].value.replace('القصص 173 → 175؛ جهات العمل 94','القصص 173 → 176؛ جهات العمل 95')
wb.save(X)
DJ=H+'SuccessStories/website/js/data.js'; js=open(DJ,encoding='utf-8').read()
def setfield(js,sid,field,val):
    k=js.index('"id": "%s"'%sid); e=js.index('\n',k); line=js[k:e]
    if ('"%s":'%field) in line: nl=re.sub(r'"%s": (null|"[^"]*")'%field,'"%s": "%s"'%(field,val),line,count=1)
    else: nl=line.replace('"program": ','"orgLogo": "%s", "program": '%val,1)
    assert nl!=line,(sid,field); return js[:k]+nl+js[e:]
js=setfield(js,'fayez-alhafta','photo','assets/fayez-alhafta.jpg'); js=setfield(js,'fayez-alhafta','orgLogo','assets/rushd-mark.png')
js=setfield(js,'waleed-alsirhani','photo','assets/waleed-alsirhani.jpg'); js=setfield(js,'waleed-alsirhani','orgLogo','assets/derayah.png')
st={"id":"yazeed-alobaidan","year":2026,"quote":{"text":"من برنامج NVIDIA الاحترافي في أكاديمية سدايا إلى قيادة تحليلات البيانات والذكاء الاصطناعي في بنك الجزيرة.","kind":"draft"},
 "name":"يزيد العبيدان","nameEn":"Yazeed Alobaidan","photo":"assets/yazeed-alobaidan.jpg",
 "role":"مدير مساعد — تحليلات البيانات والذكاء الاصطناعي","org":ORG,
 "program":"التدريب الاحترافي في الذكاء الاصطناعي التوليدي والنماذج اللغوية الكبيرة (سدايا × NVIDIA) — أكاديمية سدايا","period":"يناير 2026",
 "category":"employment","categories":["employment"],
 "impact":"ترقية إلى «مدير مساعد — تحليلات البيانات والذكاء الاصطناعي» في بنك الجزيرة في أغسطس 2026 — سبعة أشهر بعد إتمام البرنامج وشهادة NVIDIA.",
 "story":"أتمّ يزيد برنامج التدريب الاحترافي في الذكاء الاصطناعي التوليدي بأكاديمية سدايا بالشراكة مع NVIDIA، ونال في يناير 2026 شهادات دوراته الخمس وشهادة NVIDIA-Certified Associate: Generative AI LLMs، وهو حينها في برنامج تطوير الخريجين (Data and AI GDP) ببنك الجزيرة منذ أغسطس 2025. وفي أغسطس 2026 — بعد سبعة أشهر — رُقّي إلى «مدير مساعد — تحليلات البيانات والذكاء الاصطناعي» في البنك، ثم نال شارة سدايا «مهندس الذكاء الاصطناعي – خبير» وشهادة NVIDIA-Certified Professional: Agentic AI. النتيجة المحتسبة هي الترقية إلى دور قيادي في الذكاء الاصطناعي والبيانات، وهي ترقية إلى دور ذي صلة مباشرة بالبرنامج داخل نافذة الأربعة عشر شهرًا (السياسة 1.0، البند 2).",
 "achievements":["إتمام التدريب الاحترافي سدايا × NVIDIA وشهادة NCA-GENL (يناير 2026)","ترقية إلى مدير مساعد — تحليلات البيانات والذكاء الاصطناعي، بنك الجزيرة (أغسطس 2026)","شارة سدايا «مهندس الذكاء الاصطناعي – خبير» — الدفعة الأولى (يوليو 2026)","NVIDIA-Certified Professional: Agentic AI (يوليو 2026)"],
 "links":[{"label":"LinkedIn","url":"https://www.linkedin.com/in/yazeedalobaidan/"}],
 "provenance":"صفحتا الخبرة والشهادات على LinkedIn بحساب مسجَّل (قُرئتا 17 أكتوبر 2026)، بتواريخ بمستوى الشهر: شهادات NVIDIA يناير 2026؛ Bank Aljazira — Data and AI GDP (أغسطس 2025 – أغسطس 2026) ثم AI & Data Analytics Assistant Manager (أغسطس 2026 – الآن) + كشف شارات سدايا + سجل الأكاديمية #198. ترقية داخلية محتسبة بموجب السياسة 1.0، البند 2، وبقرار المدير العام (17 أكتوبر 2026)."}
k=js.index('const STORIES = ['); e=js.index('\n];',k)
pre=js[:e].rstrip(); pre+=('' if pre.endswith(',') else ',')
js=pre+'\n  '+json.dumps(st,ensure_ascii=False)+js[e:]
js=rep(js,"{ value: 175,  label: 'قصة نجاح موثّقة'","{ value: 176,  label: 'قصة نجاح موثّقة'")
js=rep(js,"{ value: 94,   label: 'جهة عمل'","{ value: 95,   label: 'جهة عمل'")
js=rep(js,"en: 'Cooperative Training (COOP)',   value: 11   }","en: 'Cooperative Training (COOP)',   value: 13   }")
js=rep(js,"'use strict';","/* 17 أكتوبر 2026 (تحديث الصور): صور فايز الهفتاء ووليد السرحاني ويزيد العبيدان وشعارا رشد للحلول ودراية المالية؛ قصة يزيد العبيدان (ترقية في بنك الجزيرة — السياسة 1.0 البند 2)؛ القصص 175 ← 176، جهات العمل 94 ← 95؛ مسار التدريب التعاوني 11 ← 13. */\n'use strict';")
open(DJ,'w',encoding='utf-8').write(js)
P4=H+'SuccessStories/website/index.html'; t=open(P4,encoding='utf-8').read(); t=rep(t,'"numberOfItems": 175','"numberOfItems": 176'); open(P4,'w',encoding='utf-8').write(t)
P2=H+'index.html'; t=open(P2,encoding='utf-8').read()
t=rep(t,'data-count="175"','data-count="176"'); t=rep(t,'data-count="94"','data-count="95"')
for a,b in (('175 قصة','176 قصة'),('175 stories','176 stories'),('175 verified','176 verified'),('94 جهة عمل','95 جهة عمل'),('94 employers','95 employers'),('across 94 government','across 95 government')): t=t.replace(a,b)
open(P2,'w',encoding='utf-8').write(t)
P5=H+'Graduates/Graduates_Database.md'; t=open(P5,encoding='utf-8').read()
t=rep(t,'القصص 173 → 175 · جهات العمل 94)','القصص 173 → 176 · جهات العمل 95)')
t=rep(t,'**3) قصص جديدة (2) — معيار الأربعة عشر شهرًا:** ','**3) قصص جديدة (3) — معيار الأربعة عشر شهرًا:** yazeed-alobaidan (#198، بنك الجزيرة — ترقية إلى مدير مساعد لتحليلات البيانات والذكاء الاصطناعي؛ السياسة 1.0 البند 2) · ')
open(P5,'w',encoding='utf-8').write(t)
for f in ('index.html','Graduates/index.html','SuccessStories/website/js/data.js'):
    t=open(H+f,encoding='utf-8').read(); print(f,'leftover175:',len(re.findall(r'\b175 (?:قصة|stories|verified)|value: 175\b|data-count="175"',t)),'94emp:',len(re.findall(r'\b94 (?:جهة|employers|government)',t)))
