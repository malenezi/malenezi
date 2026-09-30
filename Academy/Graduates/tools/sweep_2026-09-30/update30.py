import json,os,re,shutil,collections
H=os.path.expanduser('~/mnt/Academy/')
st=json.load(open('stats30.json')); T=st['tracks']; N=st['total']; g=json.load(open('grads_after.json'))
assert N==len(g)==3180
BK='backup-2026-09-30'
def bk(p):
    root,ext=os.path.splitext(p); b='%s.%s%s'%(root,BK,ext)
    if not os.path.exists(b): shutil.copy2(p,b)
def rep(s,a,b,count=None):
    n=s.count(a); assert n>=1,('missing',a[:80])
    if count is not None: assert n==count,(a[:80],n)
    return s.replace(a,b)
def rrep(s,pat,b,count=1):
    s2,n=re.subn(pat,b,s); assert n==count,(pat,n); return s2
TOT=format(N,',')
VER_AR_OLD='إصدار 28 سبتمبر 2026 (جولة مراجعة 2025–2026 والتدقيق)'
VER_AR_NEW='إصدار 30 سبتمبر 2026 (جولة الإثراء السريع لدفعات 2024–2026)'
VER_EN_OLD='version 28 September 2026 (2025–2026 review &amp; QA round)'
VER_EN_NEW='version 30 September 2026 (2024–2026 rapid enrichment round)'
pct=lambda k:'%.1f'%(100*T[k]/N)
# ---------- Graduates page
P=H+'Graduates/index.html'; bk(P); s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+len('const DATA = '); j=s.index('\nconst SITE_STATS')
raw=s[i:j].rstrip(); assert raw.endswith(';'); D=json.loads(raw[:-1]); assert len(D['grads'])==3085
D['grads']=g
head=s[:i]; tail=s[j:]
head=head.replace('3,085',TOT); tail=tail.replace('3,085',TOT)
tail=rep(tail,"{ value: 3085, label: 'سجلًا فرديًا',","{ value: %d, label: 'سجلًا فرديًا',"%N,1)
tail=rrep(tail,r"(key: 'ai', label: 'مهندس ذكاء اصطناعي', en: 'AI Engineer', value: )1507","\\g<1>%d"%T['ai'])
tail=rrep(tail,r"(key: 'ds', label: 'عالم بيانات', en: 'Data Scientist', value: )843","\\g<1>%d"%T['ds'])
tail=rrep(tail,r"(key: 'other', label: 'برامج متخصصة أخرى', en: 'Other / Specialized', value: )149","\\g<1>%d"%T['other'])
tail=rep(tail,"{ value: 1147,  label: 'سجلًا برابط تحقق علني', note: '1,924 رابط مصدر فريد',","{ value: %d,  label: 'سجلًا برابط تحقق علني', note: '%s رابط مصدر فريد',"%(st['wl'],format(st['uu'],',')),1)
tail=rep(tail,"noteEn: '1,924 unique source links'","noteEn: '%s unique source links'"%format(st['uu'],','),1)
for part in ('head','tail'):
    t=locals()[part]
    t=t.replace(VER_AR_OLD,VER_AR_NEW).replace(VER_EN_OLD,VER_EN_NEW).replace('version 28 September 2026 (2025–2026 review & QA round)',VER_EN_NEW)
    if part=='head': head=t
    else: tail=t
s=head+json.dumps(D,ensure_ascii=False)+';'+tail
open(P,'w',encoding='utf-8').write(s)
rest=head+tail
print('gradpage leftovers', {k:rest.count(k) for k in ['3,085','3085','1,924','28 سبتمبر 2026','28 September 2026']})
# ---------- Portal
P=H+'index.html'; bk(P); s=open(P,encoding='utf-8').read()
s=s.replace('3,085',TOT)
s=rep(s,'data-count="3085"','data-count="%d"'%N,1)
s=rep(s,'data-count="1507"','data-count="%d"'%T['ai'],1)
s=rep(s,'data-count="843"','data-count="%d"'%T['ds'],1)
s=rep(s,'data-count="149"','data-count="%d"'%T['other'],1)
for old,k in (('48.8','ai'),('27.3','ds'),('8.1','genai'),('10.6','dmg'),('4.8','other'),('0.4','coop')):
    s=rep(s,'--w:%s%%'%old,'--w:%s%%'%pct(k),1)
    s=rep(s,'data-ar="%s%% من السجل" data-en="%s%% of the registry"'%(old,old),'data-ar="%s%% من السجل" data-en="%s%% of the registry"'%(pct(k),pct(k)),1)
s=s.replace('إصدار 28 سبتمبر 2026 (جولة مراجعة 2025–2026 والتدقيق — ','إصدار 30 سبتمبر 2026 (جولة الإثراء السريع لدفعات 2024–2026 — ')
s=s.replace('version 28 September 2026 (2025–2026 review &amp; QA round — ','version 30 September 2026 (2024–2026 rapid enrichment round — ').replace('version 28 September 2026 (2025–2026 review & QA round — ','version 30 September 2026 (2024–2026 rapid enrichment round — ')
open(P,'w',encoding='utf-8').write(s)
print('portal leftovers',{k:s.count(k) for k in ['3,085','3085','28 سبتمبر 2026','28 September 2026']})
# ---------- data.js
P=H+'SuccessStories/website/js/data.js'; bk(P); s=open(P,encoding='utf-8').read()
s=rep(s,"{ value: 3085, label: 'خريجًا موثّقًا',","{ value: %d, label: 'خريجًا موثّقًا',"%N,1)
s=rrep(s,r"(en: 'AI Engineer',\s+value: )1507","\\g<1>%d"%T['ai'])
s=rrep(s,r"(en: 'Data Scientist',\s+value: )843 ","\\g<1>%d"%T['ds'])
s=rrep(s,r"(en: 'Other / Specialized',\s+value: )149 ","\\g<1>%d"%T['other'])
s=rep(s,"'use strict';","/* 30 سبتمبر 2026: جولة الإثراء السريع لدفعات 2024–2026 — 3,085 ← %s خريجًا (95 سجلًا جديدًا · 19 إثراءً)؛ مهندس ذكاء اصطناعي 1,507 ← %s · عالم بيانات 843 ← %s · برامج متخصصة أخرى 149 ← %s. القصص 112 وجهات العمل 69 دون تغيير. */\n'use strict';"%(TOT,format(T['ai'],','),T['ds'],T['other']),1)
open(P,'w',encoding='utf-8').write(s)
print('datajs ok')
