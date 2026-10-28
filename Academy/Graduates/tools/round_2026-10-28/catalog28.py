import json,re,os
H=os.path.expanduser('~/mnt/Academy/'); P=H+'Catalog/index.html'; s=open(P,encoding='utf-8').read()
def R(a,b,c=1):
    global s; n=s.count(a); assert n==c,(a[:80],n); s=s.replace(a,b)
# 1) data
m=re.search(r'(<script id="catalog-data"[^>]*>)(.*?)(</script>)',s,re.S); D=json.loads(m.group(2))
assert 'certifications' not in D
D['certifications']=[
 {"code":"NCA-ADS","new":True,"name_en":"NVIDIA-Certified Associate: Accelerated Data Science","name_ar":"شهادة NVIDIA المعتمدة المشاركة: علم البيانات المسرَّع",
  "format_en":"Self-paced NVIDIA DLI courses + proctored exam","format_ar":"دورات NVIDIA DLI ذاتية التعلّم + اختبار مراقَب",
  "exam_en":"60 min · 50–60 questions · English · valid 2 years","exam_ar":"60 دقيقة · 50–60 سؤالًا · بالإنجليزية · صالحة سنتين",
  "desc_en":"The GenAI Academy's newest certification track. Learners work through NVIDIA's recommended self-paced courses on GPU-accelerated data science (RAPIDS, cuDF, cuML) and then sit NVIDIA's associate-level exam. It suits data scientists, analysts and data or ML engineers who already process large datasets.",
  "desc_ar":"أحدث مسارات الاعتماد في أكاديمية الذكاء الاصطناعي التوليدي. يُتمّ المتدرب دورات NVIDIA الموصى بها ذاتية التعلّم في علم البيانات المسرَّع بوحدات المعالجة الرسومية (RAPIDS وcuDF وcuML)، ثم يجتاز اختبار NVIDIA بمستوى «مشارك». يناسب علماء البيانات ومحلليها ومهندسي البيانات وتعلم الآلة الذين يعالجون مجموعات بيانات كبيرة.",
  "domains_en":["Data manipulation and preparation 23%","Machine learning with RAPIDS 16%","Pipelines and workflow automation 13%","Descriptive analysis and visualization 13%","Foundations of accelerated data science 12%","Introductory MLOps 10%","Advanced data structures 7%","Software and environment management 6%"],
  "domains_ar":["معالجة البيانات وتهيئتها 23%","تعلم الآلة باستخدام RAPIDS 16%","خطوط المعالجة وأتمتة سير العمل 13%","التحليل الوصفي والتصوّر 13%","أساسيات علم البيانات المسرَّع 12%","مبادئ MLOps 10%","هياكل البيانات المتقدمة 7%","إدارة البرمجيات والبيئات 6%"],
  "courses_en":["Accelerating End-to-End Data Science Workflows","Accelerated Machine Learning for Time Series Forecasting","Best Practices in Feature Engineering for Tabular Data with GPU Acceleration"],
  "pathway_en":"Complements the Data Scientist Track.","pathway_ar":"مكمّل لمسار عالم البيانات."},
 {"code":"NCA-GENL","new":False,"name_en":"NVIDIA-Certified Associate: Generative AI LLMs","name_ar":"شهادة NVIDIA المعتمدة المشاركة: الذكاء الاصطناعي التوليدي والنماذج اللغوية الكبيرة",
  "format_en":"Professional Training Program in LLMs (5 NVIDIA DLI courses) + proctored exam","format_ar":"التدريب الاحترافي في النماذج اللغوية الكبيرة (5 دورات NVIDIA DLI) + اختبار مراقَب",
  "exam_en":"60 min · 50–60 questions · English · valid 2 years","exam_ar":"60 دقيقة · 50–60 سؤالًا · بالإنجليزية · صالحة سنتين",
  "desc_en":"The GenAI Academy's established track, delivered in partnership with NVIDIA. Learners complete five specialised NVIDIA courses on large language models and then sit NVIDIA's associate-level exam in generative AI and LLMs.",
  "desc_ar":"المسار الراسخ في أكاديمية الذكاء الاصطناعي التوليدي بالشراكة مع NVIDIA. يُتمّ المتدرب خمس دورات متخصصة من NVIDIA في النماذج اللغوية الكبيرة، ثم يجتاز اختبار NVIDIA بمستوى «مشارك» في الذكاء الاصطناعي التوليدي والنماذج اللغوية الكبيرة.",
  "domains_en":["Core machine learning and AI knowledge 30%","Software development 24%","Experimentation 22%","Data analysis 14%","Trustworthy AI 10%"],
  "domains_ar":["أساسيات تعلم الآلة والذكاء الاصطناعي 30%","تطوير البرمجيات 24%","التجريب 22%","تحليل البيانات 14%","الذكاء الاصطناعي الجدير بالثقة 10%"],
  "courses_en":[],
  "pathway_en":"Complements the AI Engineer Track.","pathway_ar":"مكمّل لمسار مهندس الذكاء الاصطناعي."}]
s=s[:m.start(2)]+json.dumps(D,ensure_ascii=False)+s[m.end(2):]
# 2) section numbers after catalog
R('<span class="sec-num">05</span><span data-ar="الجدارات"','<span class="sec-num">06</span><span data-ar="الجدارات"')
R('<span class="sec-num">06</span><span data-ar="اصطلاح التسمية"','<span class="sec-num">07</span><span data-ar="اصطلاح التسمية"')
R('<span class="sec-num">07</span><span data-ar="التحسين المستقبلي"','<span class="sec-num">08</span><span data-ar="التحسين المستقبلي"')
# 3) new section
SEC='''
<!-- GENAI ACADEMY CERTIFICATIONS -->
<section class="sd-section" id="certs">
  <div class="sd-container">
    <div class="sd-section__head">
      <div class="sd-eyebrow"><span class="sec-num">05</span><span data-ar="أكاديمية الذكاء الاصطناعي التوليدي" data-en="GenAI Academy"></span></div>
      <h2 data-ar="شهادات NVIDIA المعتمدة" data-en="NVIDIA certifications"></h2>
      <p data-ar="مسارات اعتماد بالشراكة مع NVIDIA تُقدَّم إلى جانب المسارات الأربعة: دورات تحضيرية ثم اختبار NVIDIA الرسمي. لا تدخل ضمن البرامج السبعة والثلاثين ولا في حساب الأيام التدريبية." data-en="Partner certification tracks offered alongside the four pathways: preparatory courses, then NVIDIA's official exam. They sit outside the 37 programs and the training-day count."></p>
    </div>
    <div id="certgrid" class="sd-grid sd-grid--2"></div>
  </div>
</section>
'''
R('\n<!-- SKILLS MATRIX -->',SEC+'\n<!-- SKILLS MATRIX -->')
# 4) css
R('\n@media(max-width:640px){.step-card','''
.cert-card{padding:1.5rem 1.6rem;display:flex;flex-direction:column;gap:.85rem}
.cert-card .top{display:flex;align-items:center;justify-content:space-between;gap:10px}
.cert-card .code{font-family:var(--font-mono);font-weight:700;color:var(--brand);direction:ltr}
.cert-card h3{font-size:1.08rem;line-height:1.5}
.cert-card .lbl{font-size:12px;font-weight:700;color:var(--ink-3);margin-bottom:.35rem}
.cert-card ul{margin:0;padding-inline-start:1.1rem;display:grid;gap:.2rem;font-size:13.5px;color:var(--ink-2)}
.cert-card .meta{display:grid;gap:.35rem;font-size:13.5px;color:var(--ink-2)}
.cert-card .meta div{display:flex;gap:8px;align-items:flex-start}
@media(max-width:640px){.step-card''')
# 5) js
R('''/* ---------- in-page nav ---------- */''','''/* ---------- GenAI Academy certifications ---------- */
function renderCerts() {
  $('#certgrid').innerHTML = (CATALOG.certifications || []).map(c => `<article class="sd-card sd-card--flat cert-card">
      <div class="top"><span class="sd-iconbox sd-iconbox--sm tint-blue">${I('award', 'i-sm')}</span><span class="code">${esc(c.code)}</span>${c.new ? `<span class="sd-tag sd-tag--brand">${T('مسار جديد', 'New track')}</span>` : ''}</div>
      <h3>${L(c.name_en, c.name_ar)}</h3>
      <p class="desc">${L(c.desc_en, c.desc_ar)}</p>
      <div class="meta">
        <div>${I('book-open', 'i-sm')}<span>${L(c.format_en, c.format_ar)}</span></div>
        <div>${I('badge-check', 'i-sm')}<span>${L(c.exam_en, c.exam_ar)}</span></div>
        <div>${I('route', 'i-sm')}<span>${L(c.pathway_en, c.pathway_ar)}</span></div>
      </div>
      <div><div class="lbl">${T('مجالات الاختبار', 'Exam domains')}</div><ul>${L(c.domains_en, c.domains_ar).map(x => `<li>${esc(x)}</li>`).join('')}</ul></div>
      ${c.courses_en.length ? `<div><div class="lbl">${T('دورات NVIDIA الموصى بها', 'Recommended NVIDIA courses')}</div><ul>${c.courses_en.map(x => `<li dir="ltr">${esc(x)}</li>`).join('')}</ul></div>` : ''}
    </article>`).join('');
}

/* ---------- in-page nav ---------- */''')
R("['catalog', 'Catalog', 'الكاتالوج', 'layout-grid'], ","['catalog', 'Catalog', 'الكاتالوج', 'layout-grid'], ['certs', 'NVIDIA', 'شهادات NVIDIA', 'award'], ")
R("renderCatalog(); renderMatrix();","renderCatalog(); renderCerts(); renderMatrix();")
open(P,'w',encoding='utf-8').write(s); print('ok')
