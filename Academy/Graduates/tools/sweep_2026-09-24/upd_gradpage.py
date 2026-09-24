import os,json
P=os.path.expanduser('~/mnt/Academy/Graduates/index.html'); s=open(P,encoding='utf-8').read()
st=json.load(open('stats24.json')); T=st['tracks']
i=s.index('const DATA = '); j=s.index('\nconst SITE_STATS')
head,data,tail=s[:i],s[i:j],s[j:]
def rep(txt,a,b,count=None):
    n=txt.count(a); assert n>=1,(a[:80]); 
    if count: assert n==count,(a[:60],n)
    return txt.replace(a,b)
tail=rep(tail,"{ value: 2973, label: 'سجلًا فرديًا',","{ value: %d, label: 'سجلًا فرديًا',"%st['total'],1)
tail=rep(tail,"{ value: 109,   label: 'قصة نجاح موثّقة',      note: 'مستوفية معيار الأربعة عشر شهرًا — عبر 66 جهة عمل',","{ value: 111,   label: 'قصة نجاح موثّقة',      note: 'مستوفية معيار الأربعة عشر شهرًا — عبر 68 جهة عمل',",1)
tail=rep(tail,"noteEn: 'Meeting the 14-month criterion — across 66 employers'","noteEn: 'Meeting the 14-month criterion — across 68 employers'",1)
tail=rep(tail,"{ value: 1025,  label: 'سجلًا برابط تحقق علني', note: '1,633 رابط مصدر فريد',","{ value: %d,  label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(st['wl'],format(st['uu'],',')),1)
tail=rep(tail,"noteEn: '1,633 unique source links'","noteEn: '%s unique source links'"%format(st['uu'],','),1)
tail=rep(tail,"{ key: 'ai', label: 'مهندس ذكاء اصطناعي', en: 'AI Engineer', value: 1458 },","{ key: 'ai', label: 'مهندس ذكاء اصطناعي', en: 'AI Engineer', value: %d },"%T['ai'],1)
tail=rep(tail,"{ key: 'ds', label: 'عالم بيانات', en: 'Data Scientist', value: 805 },","{ key: 'ds', label: 'عالم بيانات', en: 'Data Scientist', value: %d },"%T['ds'],1)
tail=rep(tail,"{ key: 'other', label: 'برامج متخصصة أخرى', en: 'Other / Specialized', value: 124 }","{ key: 'other', label: 'برامج متخصصة أخرى', en: 'Other / Specialized', value: %d }"%T['other'],1)
tot=format(st['total'],',')
for part in ('head','tail'):
    t=locals()[part]
    t=t.replace('2,973',tot)
    t=t.replace('للمجموعة الكاملة (109 قصة)','للمجموعة الكاملة (111 قصة)').replace('For the full collection (109 stories)','For the full collection (111 stories)')
    t=t.replace('إصدار 22 سبتمبر 2026 (جولة مسح دفعتَي 2023 و2026)','إصدار 24 سبتمبر 2026 (جولة مستودعات تسليم دفعات 2025–2026)')
    t=t.replace('version 22 September 2026 (2023 &amp; 2026 cohort sweep)','version 24 September 2026 (2025–2026 submission-repository sweep)')
    t=t.replace('109 قصة نجاح موثّقة (معيار','111 قصة نجاح موثّقة (معيار').replace('109 verified success stories (14-month','111 verified success stories (14-month')
    if part=='head': head=t
    else: tail=t
s=head+data+tail
open(P,'w',encoding='utf-8').write(s)
rest=head+tail
import re
for pat in ['2,973','2973','109 ','66 جهة','66 employers','1,633','22 سبتمبر 2026','cohort sweep']:
    print(pat, rest.count(pat))
print(tot, rest.count(tot))
