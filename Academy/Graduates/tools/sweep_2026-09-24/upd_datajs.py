import os,json,re
from stories_new import S
st=json.load(open('stats24.json')); T=st['tracks']
P=os.path.expanduser('~/mnt/Academy/SuccessStories/website/js/data.js'); s=open(P,encoding='utf-8').read()
assert s.count('"id": "meshal-aldalbahi"')==0 and s.count('marwah-ali')==0
k=s.rindex('\n];'); lines=''.join('  '+json.dumps(x,ensure_ascii=False).replace(': null',': null')+',\n' for x in S)
s=s[:k+1]+lines+s[k+1:]
def rep(a,b):
    global s; assert s.count(a)==1,(a[:70],s.count(a)); s=s.replace(a,b)
rep("{ value: 2973, label: 'خريجًا موثّقًا',","{ value: %d, label: 'خريجًا موثّقًا',"%st['total'])
rep("{ value: 109,  label: 'قصة نجاح موثّقة',","{ value: 111,  label: 'قصة نجاح موثّقة',")
rep("{ value: 66,   label: 'جهة عمل',","{ value: 68,   label: 'جهة عمل',")
rep("en: 'AI Engineer',                   value: 1458 },","en: 'AI Engineer',                   value: %d },"%T['ai'])
rep("en: 'Data Scientist',                value: 805  },","en: 'Data Scientist',                value: %d  },"%T['ds'])
rep("en: 'Other / Specialized',           value: 124  },","en: 'Other / Specialized',           value: %d  },"%T['other'])
note='''   تحديث 24 سبتمبر 2026 (جولة مستودعات تسليم دفعات 2025–2026): 113 سجل خريج جديد (2,973 ← 3,086) من مستودعات التسليم
   التي تحيل إلى حساب الأكاديمية على GitHub (دفعات أغسطس–سبتمبر 2026 لبرامج SDA-AIE-113/211/212/213/311 وSDA-DSC-112/213
   والسلاسل الزمنية وL0-FAE وL0-FGP وهندسة البيانات الحديثة ووكلاء الذكاء الاصطناعي)، و21 إثراءً لسجلات قائمة بدل تكرارها.
   قصتان جديدتان بتواريخ من صفحات الخبرة على لينكدإن بحساب مسجَّل: مشعل الدلبحي (معسكر T5 لإدارة الحشود سبتمبر 2024 ←
   محلل بيانات في هيئة تنمية البحث والتطوير والابتكار، مايو 2025 — 8 أشهر) ومروة علي (المسارات المتقدمة — التعلم العميق
   نوفمبر 2024 ← مهندسة ذكاء اصطناعي في نبّه، مايو 2025 — 6 أشهر). 109 ← 111 قصة، وجهات العمل 66 ← 68.
*/'''
k=s.index('*/'); s=s[:k]+note.lstrip()[0:0]+note.replace('*/','').rstrip()+'\n*/'+s[k+2:]
open(P,'w',encoding='utf-8').write(s); print('ok')
