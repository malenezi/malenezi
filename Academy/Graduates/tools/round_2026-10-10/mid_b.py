LOG['fix']=[]
AML='أساليب تعلم الآلة المتقدمة (Advanced Machine Learning Methods) — أكاديمية سدايا'
DGA='تطوير حلول الذكاء الاصطناعي التوليدي (Developing Generative AI Solutions) — أكاديمية سدايا'
APL='تعلم الآلة التطبيقي للأنظمة الذكية (Applied Machine Learning) — أكاديمية سدايا'
for k,nm in ((3317,'نوف الحارثي'),(3318,'محمد الحجي'),(3320,'شذى السبيعي'),(3322,'أسماء مهدي نابه'),(3323,'فارس الشعشاع'),(3324,'عزام الزهراني')): assert g[k-1]['n']==nm,(k,g[k-1]['n'])
FIX={3318:(DGA,'ai'),3319:(APL,'ai'),3320:(AML,'ds'),3323:(None,'ai'),3324:(DGA,'ai')}
for k,(p,tr) in FIX.items():
    G=g[k-1]; r=k+1
    if p: G['prog']=p; ws.cell(r,4).value=p
    G['tr']=tr; ws.cell(r,5).value=TRN[tr]; LOG['fix'].append(k)
note(3320,'تصحيح: اسم البرنامج على التسمية القائمة ومساره «عالم البيانات» (المقرر SDA-DSC-211).')
ENR=[(3214,'GitHub','https://github.com/JanaAlkha',16,'حساب GitHub «JanaAlkha» فيه مستودع «Sdaia_Academy_Janaalkhalid» (16 سبتمبر 2026 — تاريخ منشورها نفسه) — يطابق الاسم والبرنامج والتاريخ.'),
 (3202,'GitHub','https://github.com/noufalohali-24',16,'حساب GitHub «noufalohali-24» فيه «Rafeeq-Agentic-AI-Systems-Nouf» (20 سبتمبر 2026) — مشروع «رفيق» لمقرر SDA-AIE-311 نفسه؛ يطابق الاسم والبرنامج والشهر.')]
for k,lab,url,col,txt in ENR:
    if addlink(k,lab,url,col): C['link_added']+=1
    note(k,txt); LOG['enrich'].append(k)
note(2869,'مرشح مطابقة غير محسوم: حساب GitHub «Dalonazi» فيه «Dana-TamweelLite-AdvancedMLMethods-DSC211» (7 أكتوبر 2026) — مسار عالم البيانات نفسه بعد مقرر السلاسل الزمنية (سبتمبر)، لكن بمعرّف مختلف عن danakhalif؛ لم يُربط ولم يُنشأ سجل جديد.'); LOG['enrich'].append(2869)
D1='أكتوبر 2026 (تاريخ مستودع مشروع المقرر)'
NEW=[
 ('ريم شايع','Reem Shaya',AML,D1,'ds',70,[['GitHub','https://github.com/ReemShaya'],['مستودع المشروع','https://github.com/ReemShaya/Reem_Shaya_Tamweel-Lite_AdvancedMachineLearning_SDA_DSC_211']],'مستودع «Reem_Shaya_Tamweel-Lite_AdvancedMachineLearning_SDA_DSC_211» (5 أكتوبر 2026) — رمز المقرر والاسم الكامل في اسم المستودع ويطابقان الحساب.'),
 ('اللولو البصري','Allolo Albasri',AML,D1,'ds',68,[['GitHub','https://github.com/Lulu634381'],['مستودع المشروع','https://github.com/Lulu634381/SDA-DSC-211-.-Tamweel-Project-.-Allolo-Albasri']],'مستودع «SDA-DSC-211 · Tamweel Project · Allolo Albasri» (4 أكتوبر 2026) — رمز المقرر والاسم الكامل في اسم المستودع.'),
 ('سارة القحطاني','Sarah Alqahtani',AML,D1,'ds',68,[['GitHub','https://github.com/sarahliic'],['مستودع المشروع','https://github.com/sarahliic/tamweel-project-lite-sda-dsc-211-sarah-alqahtani']],'مستودع «tamweel-project-lite-sda-dsc-211-sarah-alqahtani» (5 أكتوبر 2026). اسم شائع: لا يطابق #2828 «Sara Alqahtani» (حساب Sarai1i، معسكر AAI) ولا #392/#697 — برامج ومعرّفات مختلفة؛ لا دمج.'),
 ('سارة العنزي','Sarah Alanazi',AML,D1,'ds',68,[['GitHub','https://github.com/sara1xv'],['مستودع المشروع','https://github.com/sara1xv/Sarah-Alanazi-Tamweel-ML-211']],'مستودعا «Sarah-Alanazi-Tamweel-ML-211» و«tamweel-advanced-ml-sarah-alanazi» (4–7 أكتوبر 2026). لا يطابق #699 «Sarah Turki Alanazi» (ML 7، 2023)؛ لا دمج.'),
 ('داليا المعي','Dalia Almaai',AML,D1,'ds',68,[['GitHub','https://github.com/Daliaalmaai'],['مستودع المشروع','https://github.com/Daliaalmaai/tamweel-project-01-daliaalmaai-sda-dsc-211']],'مستودع «tamweel-project-01-daliaalmaai-sda-dsc-211» بوصف «SDA-DSC-211 — Advanced…» (4 أكتوبر 2026).'),
 ('فلوة العريفي','Fulwah Alarifi',AML,D1,'ds',68,[['GitHub','https://github.com/FelwaAl'],['مستودع المشروع','https://github.com/FelwaAl/FulwahAlarifi_Tamweel-Lite_AdvancedMachineLearning_211']],'مستودع «FulwahAlarifi_Tamweel-Lite_AdvancedMachineLearning_211» (6 أكتوبر 2026، «Final project»).'),
 ('عزوف العتيبي','Ozuf Alotaibi',AML,D1,'ds',66,[['GitHub','https://github.com/AzoofSA'],['مستودع المشروع','https://github.com/AzoofSA']],'مستودع «Ozuf-Alotaibi-Advanced-Machine-Learning-Methods-Tamweel-Lite» (أكتوبر 2026).'),
 ('فهد القحطاني','Fahad Alqahtani','ممارسات هندسة البرمجيات لأنظمة الذكاء الاصطناعي (SDA-AIE-113) — أكاديمية سدايا','سبتمبر 2026 (تاريخ مستودعات المقرر)','ai',70,[['GitHub','https://github.com/fahad33alqhtani'],['مستودع المشروع','https://github.com/fahad33alqhtani/nasih_credit_risk_service_SDA-AIE-113']],'مستودعا «nasih_credit_risk_service_SDA-AIE-113» و«Lab-5-SDAIA-Academy-» (22 سبتمبر 2026)؛ الاسم من اسم المستخدم على GitHub.'),
]
idx=TR.build_index(g); new_ids=[]
ghs={l[1].rstrip('/').lower() for r in g for l in r['links']}
SRC='بحث مستودعات GitHub برموز المقررات (SDA-DSC-211 · SDA-AIE-113) — جولة 10 أكتوبر 2026'
for ar,en,prog,co,tr,score,links,d in NEW:
    m=TR.match(ar,en,idx); print(en,'matches:',[(x[0],x[1]) for x in m])
    assert links[0][1].lower() not in ghs,en
    assert not any(('211' in g[x[0]-1]['prog'] or 'Advanced Machine Learning' in g[x[0]-1]['prog'] or 'AIE-113' in g[x[0]-1]['prog']) for x in m),(en,m)
    rid=len(g)+1; r=rid+1; dd=d+' '+TAG.strip()+TL
    g.append({"n":ar,"en":en,"lv":"gh1010","score":score,"prog":prog,"co":co,"win":"ضمن النطاق","edu":"","emp":"","role":"","cats":['program','project'],"d":dd,"links":links,"src":SRC,"tr":tr}); new_ids.append(rid)
    vals=[rid,ar,en,prog,TRN[tr],co,None,None,None,None,'gh1010',score,'ضمن النطاق','برنامج · مشروع',None,' · '.join(l[1] for l in links),None,None,None,None,dd,None,SRC]
    for ci,v in enumerate(vals,1): ws.cell(r,ci).value=v
