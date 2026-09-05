# -*- coding: utf-8 -*-
"""COOP round — 5 Sep 2026. Adds the التدريب التعاوني track + 9 new records,
retags #2711 and cross-tags six existing records."""
import json, io, sys

P='index.html'
s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+13
j=s.index('\nconst SITE_STATS')
raw=s[i:j].strip(); assert raw.endswith(';')
D=json.loads(raw[:-1])
g=D['grads']
assert len(g)==2811, len(g)

SRC='جولة التدريب التعاوني (COOP) — 5 سبتمبر 2026'
PROG='التدريب التعاوني — أكاديمية سدايا (SDAIA Academy Cooperative Training)'

def rec(n,en,score,co,d,links,role='',emp='',edu='',lv='coop26',cats=None,win='ضمن النطاق'):
    return {"n":n,"en":en,"lv":lv,"score":score,"prog":PROG,"co":co,"win":win,"edu":edu,
            "emp":emp,"role":role,"cats":cats or ["training"],"d":d,"links":links,"src":SRC,"tr":"coop"}

NEW=[
 rec("شذى المالكي","Shatha Almalki",85,"2025 (اختُتم — منشور إتمام ديسمبر 2025)",
   "متدربة التدريب التعاوني في سدايا — مكتب إدارة الاستراتيجية (Strategy Management Office). الدليل: منشور إتمام علني من الشخص نفسه: «Today, I proudly conclude my Coop training at SDAIA – Strategy Management Office»، ونبذة ملفها العلني: «Fresh E-commerce graduate with practical experience from my Coop training at SDAIA’s…»، وعنوان ملفها المفهرس علنًا «SDAIA Coop Trainee». التعليم: الجامعة السعودية الإلكترونية — التجارة الإلكترونية (2021–2025). عتبة الهوية: الاسم + البرنامج + الإدارة + الجامعة (أربع سمات).",
   [["LinkedIn","https://sa.linkedin.com/in/shatha-almalki-131619167"]],
   role="متدربة تدريب تعاوني — مكتب إدارة الاستراتيجية",
   edu="الجامعة السعودية الإلكترونية — التجارة الإلكترونية (2021–2025)"),

 rec("فريدة القفلي","Faridah Alqueflie",82,"2024 (اختُتم — منشور إتمام 18 يوليو 2024)",
   "متدربة التدريب التعاوني في سدايا. الدليل: منشور إتمام علني من الشخص نفسه (18 يوليو 2024، 16 تفاعلًا و7 تعليقات): «As my COOP internship at SDAIA | سدايا concludes, I find myself filled with excitement and gratitude… I would thank my supervisor Mohammed Alqahtani and my team». تاريخ المنشور مستخرج من معرّف النشاط 7219657201303384066.",
   [["منشور إتمام (LinkedIn)","https://www.linkedin.com/posts/faridah-alqueflie-339860289_as-my-coop-internship-at-sdaia-%D8%B3%D8%AF%D8%A7%D9%8A%D8%A7-concludes-activity-7219657201303384066-clnh"]],
   role="متدربة تدريب تعاوني"),

 rec("أروى السدران","Arwa Al-Sedran",74,"ديسمبر 2022 (بدء موثّق — الإتمام غير موثّق علنًا)",
   "متدربة التدريب التعاوني في سدايا — إدارة معمارية المؤسسة (Enterprise Architecture Department). الدليل: منشور علني من الشخص نفسه (12 ديسمبر 2022): «I’m glad to share that I’ve joined SDAIA | سدايا as a COOP Trainee in Enterprise Architecture Department». ⚠️ المنشور يوثّق بدء التدريب لا إتمامه — الإتمام يحتاج تأكيدًا (قائمة قيد التحقق).",
   [["منشور بدء (LinkedIn)","https://www.linkedin.com/posts/arwa-al-sedran-673472216_im-glad-to-share-that-ive-joined-sdaia-activity-7008059074659389440-fNSO"]],
   role="متدربة تدريب تعاوني — إدارة معمارية المؤسسة", win="غير محدد"),

 rec("أميرة التميمي","Ameerah Altamimi",84,"نوفمبر 2023 (اختُتم — منشور إتمام 28 نوفمبر 2023)",
   "متدربة التدريب التعاوني في سدايا — الإدارة العامة للدراسات. الدليل: منشور إتمام علني من الشخص نفسه (28 نوفمبر 2023، 45 تفاعلًا): «انتهت فترة تدريبي في الهيئة السعودية للبيانات والذكاء الاصطناعي… أود أن أعبّر عن شكري الجزيل إلى جميع الزملاء والزميلات في الإدارة العامة للدراسات» و«Thrilled to announce the successful completion of my co-op training at SDAIA». يذكر المنشور مشرفين من سدايا بالاسم (منهم د. منيرة العيسى).",
   [["منشور إتمام (LinkedIn)","https://ae.linkedin.com/posts/ameerah-altamimi-49341126a_sdaia-cooptraining-ai-activity-7135103240114692096-COeu"]],
   role="متدربة تدريب تعاوني — الإدارة العامة للدراسات"),

 rec("مهدي الزاير","Mahdi Alzayer",72,"سبتمبر 2023 (بدء موثّق — الإتمام غير موثّق علنًا)",
   "متدرب التدريب التعاوني في سدايا. الدليل: منشور علني من الشخص نفسه (13 سبتمبر 2023، 29 تفاعلًا): «I am happy to share that I have started my coop training program with SDAIA» بوسمي #SDAIA #CoopTraining. ⚠️ المنشور يوثّق بدء التدريب لا إتمامه — الإتمام يحتاج تأكيدًا (قائمة قيد التحقق).",
   [["منشور بدء (LinkedIn)","https://www.linkedin.com/posts/mahdi-alzayer-70_sdaia-cooptraining-activity-7107632120092618752-aPeX"]],
   role="متدرب تدريب تعاوني", win="غير محدد"),

 rec("عبدالملك الدوسري","Abdulmalek Aldossery",83,"أغسطس 2023 (اختُتم — منشور إتمام 29 أغسطس 2023)",
   "متدرب التدريب التعاوني في سدايا. الدليل: منشور إتمام علني من الشخص نفسه (29 أغسطس 2023، 35 تفاعلًا) عنوانه «CO-OP training certificate at SDAIA» ونصّه «Glad to share with you that I have completed my training at SDAIA, it was wonderful a experience»، ويسمّي مشرفه ومديره العام ومديره المباشر في سدايا بالاسم.",
   [["منشور إتمام (LinkedIn)","https://www.linkedin.com/posts/abdulmalek-aldossery-736464218_co-op-training-certificate-at-sdaia-activity-7102216244652646400-J-Vg"]],
   role="متدرب تدريب تعاوني"),

 rec("هديل الهندي","Hadeel Alhindi",70,"يوليو 2023 (بدء موثّق — الإتمام غير موثّق علنًا)",
   "متدربة التدريب التعاوني في سدايا. الدليل: منشور علني من الشخص نفسه (6 يوليو 2023): «First day with SDAIA | سدايا — It was a wonderful meeting for coop trainees with an informative background about SDAIA». ⚠️ المنشور يوثّق اليوم الأول لا الإتمام — الإتمام يحتاج تأكيدًا (قائمة قيد التحقق).",
   [["منشور بدء (LinkedIn)","https://www.linkedin.com/posts/hadeel-alhindi-832023209_first-day-with-sdaia-%D8%B3%D8%AF%D8%A7%D9%8A%D8%A7-it-was-a-wonderful-activity-7082690603708284928-LESP"]],
   role="متدربة تدريب تعاوني", win="غير محدد"),

 rec("شذى المستحي","Shatha Almustahi",84,"أغسطس 2023 (اختُتم — منشور إتمام 7 أغسطس 2023)",
   "متدربة التدريب التعاوني في سدايا — إدارة المبادرات الميدانية (المسؤولة عن القمة العالمية للذكاء الاصطناعي). الدليل: منشور إتمام علني من الشخص نفسه (7 أغسطس 2023، 67 تفاعلًا و14 تعليقًا): «اكملت فترة التدريب التعاوني في سدايا… صاحبني الشرف بالتدرب تحت إدارة المبادرات الميدانية المسؤولة بشكل رئيسي عن القمة العالمية للذكاء الاصطناعي، والعمل على تخطيط أحد المشاريع القادمة»، ويسمّي مشرفه في سدايا بالاسم. تحمل شهادتي CMMP® وCEM® على ملفها.",
   [["منشور إتمام (LinkedIn)","https://ae.linkedin.com/posts/shatha-almustahi-510269179_%D8%A7%D9%84%D8%AD%D9%85%D8%AF%D9%84%D9%84%D9%87-%D8%A7%D9%84%D8%B0%D9%8A-%D8%A8%D9%86%D8%B9%D9%85%D8%AA%D9%87-%D8%AA%D8%AA%D9%85-%D8%A7%D9%84%D8%B5%D8%A7%D9%84%D8%AD%D8%A7%D8%AA-%D8%A7%D9%83%D9%85%D9%84%D8%AA-activity-7094275222899437568-1hkX"]],
   role="متدربة تدريب تعاوني — إدارة المبادرات الميدانية"),

 rec("غدير الحربي","Ghadeer Alharbi",78,"مارس–يونيو 2024",
   "متدربة تدريب تعاوني/تدريب داخلي في علوم البيانات بسدايا. الدليل: إدخال خبرة علني «Data Science Intern — SDAIA | سدايا · Internship» (مارس–يونيو 2024) رُصد في جولة ستة البرامج (28 أغسطس 2026). ⚠️ أُجّل اعتمادها آنذاك بحجة «لا يوجد اسم برنامج؛ قد يكون تدريبًا تعاونيًا في الجهة لا معسكرًا أكاديميًا» — وباعتماد «التدريب التعاوني» برنامجًا مستقلًا في هذه الجولة زال سبب التأجيل واعتُمد السجل ضمن هذا البرنامج بعينه.",
   [["LinkedIn","https://www.linkedin.com/in/ghadeer-alharbi-531603288/"]],
   role="متدربة علوم بيانات (تدريب تعاوني)"),
]

g.extend(NEW)

NOTE_TAG=" [جولة التدريب التعاوني — 5 سبتمبر 2026] أُدرج هذا السجل ضمن برنامج «التدريب التعاوني — أكاديمية سدايا» المستحدث في هذه الجولة: "

# --- retag #2711 as the anchor COOP record
r=g[2710]
assert r['n']=='فرح البازعي', r['n']
r['tr']='coop'
r['prog']=PROG
r['d']+=NOTE_TAG+"سجله الأصل يسمّي «Cooperative Training Trainee – SDAIA Academy» صراحةً، فصار السجل المرجعي لهذا البرنامج."

# --- cross-tag: coop documented alongside another Academy program
CROSS={
 204:"منشور «Co-op Training at SDAIA» مسجَّل في حقل الأدلة، والملف الموثّق ينصّ على أنه نال NCA-GENL بعد تدريب تعاوني في سدايا على مشروعات ذكاء اصطناعي واقعية.",
 18:"يوثّق سجله تحوّلًا من متدربة تعاونية في سدايا (2023) إلى موظفة فيها (2024) — وهي قصة نجاح منشورة أصلًا (asma-alzahrani).",
 2679:"يوثّق سجله تدريبًا تعاونيًا في سدايا (مايو–أغسطس 2021) سابقًا لمعسكر T5 — وهو مذكور في قصتها المنشورة (ruba-alnashwan).",
 2412:"نبذة ملفها العلني تنصّ صراحةً: «Fresh graduate computer science and AI track at MU, Coop training at SDAIA».",
 2309:"يوثّق سجله «AI Intern at SDAIA (2023)» سابقًا لمعسكر T5 لتقنيات إدارة الزحام (2024).",
 2669:"يوثّق سجله تدريبًا تعاونيًا في تشغيل بنية الحوسبة السحابية بسدايا (يونيو–أغسطس 2024) — وهو مذكور في قصته المنشورة (rayan-alsuwat).",
}
NAMES={204:'فارس سلامه غثيمان الجهني',18:'أسماء الزهراني',2679:'ربى النشوان',
       2412:'Tahani Mudhhi Al-rashidi',2309:'رتاج المطيري',2669:'ريان سعد السواط'}
for k,why in CROSS.items():
    r=g[k-1]
    assert r['n']==NAMES[k], (k,r['n'])
    r['coop']=True
    r['d']+=" [جولة التدريب التعاوني — 5 سبتمبر 2026] وُسم هذا السجل بوسم «التدريب التعاوني» إضافةً إلى برنامجه الأصلي (المسار المعياري لم يتغيّر): "+why

# --- held duplicate-suspect cross-note on #2541
r=g[2540]
assert r['n']=='غيداء الزهراني', r['n']
r['d']+=" [جولة التدريب التعاوني — 5 سبتمبر 2026] ⚠️ مرشحة تدريب تعاوني بالاسم نفسه: «Ghaida Alzahrani» (linkedin.com/in/ghaidaalzahrani) نشرت في 25 سبتمبر 2024 إتمامها برنامج التدريب التعاوني في سدايا. طابق الاسمُ هذا السجلَ على طبقتَي المطابقة الثانية (الاسم) والرابعة (الهيكل الصوتي)، ولم يطابق على طبقة الرابط. وبحكم البند 7 من سياسة الاعتماد (لا يُنشأ سجل عند الاشتباه حتى يُحسم التطابق) عُلّقت الإضافة وأُدرجت في قائمة «قيد التحقق»، ولم تُسند شهادة التدريب التعاوني إلى هذا السجل."

out=json.dumps(D,ensure_ascii=False,separators=(',',':'))
s=s[:i]+out+';'+s[j:]

# ---- TRACKS + colours + icons + stats -------------------------------------
old_tracks="""const TRACKS = [
  { key: 'ai', label: 'مهندس ذكاء اصطناعي', en: 'AI Engineer', value: 1346 },
  { key: 'ds', label: 'عالم بيانات', en: 'Data Scientist', value: 765 },
  { key: 'genai', label: 'أكاديمية الذكاء الاصطناعي التوليدي', en: 'Gen AI Academy', value: 254 },
  { key: 'dmg', label: 'إدارة وحوكمة البيانات', en: 'Data Management & Governance', value: 324 },
  { key: 'other', label: 'برامج متخصصة أخرى', en: 'Other / Specialized', value: 122 },"""
new_tracks="""const TRACKS = [
  { key: 'ai', label: 'مهندس ذكاء اصطناعي', en: 'AI Engineer', value: 1346 },
  { key: 'ds', label: 'عالم بيانات', en: 'Data Scientist', value: 765 },
  { key: 'genai', label: 'أكاديمية الذكاء الاصطناعي التوليدي', en: 'Gen AI Academy', value: 254 },
  { key: 'dmg', label: 'إدارة وحوكمة البيانات', en: 'Data Management & Governance', value: 324 },
  { key: 'coop', label: 'التدريب التعاوني', en: 'Cooperative Training (COOP)', value: 10 },
  { key: 'other', label: 'برامج متخصصة أخرى', en: 'Other / Specialized', value: 121 },"""
assert old_tracks in s
s=s.replace(old_tracks,new_tracks,1)

s=s.replace("const TRACK_COLOR = { ai: '#1459A8', ds: '#0E7C86', genai: '#F07D3D', dmg: '#104281', other: '#7A8CA0' };",
            "const TRACK_COLOR = { ai: '#1459A8', ds: '#0E7C86', genai: '#F07D3D', dmg: '#104281', coop: '#6B4FA0', other: '#7A8CA0' };",1)
s=s.replace("const TRACK_TAG = { ai: '#1459A8', ds: '#0E7C86', genai: '#A84A10', dmg: '#104281', other: '#5F7389' };",
            "const TRACK_TAG = { ai: '#1459A8', ds: '#0E7C86', genai: '#A84A10', dmg: '#104281', coop: '#59408A', other: '#5F7389' };",1)
s=s.replace("const TRACK_ICON = { ai: 'brain-circuit', ds: 'chart-column', genai: 'sparkles', dmg: 'database', other: 'layers' };",
            "const TRACK_ICON = { ai: 'brain-circuit', ds: 'chart-column', genai: 'sparkles', dmg: 'database', coop: 'handshake', other: 'layers' };",1)

s=s.replace("{ value: 2811, label: 'سجلًا فرديًا',","{ value: 2820, label: 'سجلًا فرديًا',",1)

open(P,'w',encoding='utf-8').write(s)
print('records now:',len(g))
print('coop primary:',sum(1 for r in g if r.get('tr')=='coop'))
print('coop cross-tagged:',sum(1 for r in g if r.get('coop')))
from collections import Counter
c=Counter(r['tr'] for r in g); print(c, 'sum',sum(c.values()))
