"""Arabic pages for malenezi.github.io/malenezi.

Called from build.py's main(); never run on its own. Everything numeric (publication count,
Scholar figures) is read from the build module that is passed in, so the Arabic pages always
show the same numbers as the English ones.
"""
import json, html
from datetime import datetime

HOME, LEAD, PROJ = "index_arabic.html", "leadership_arabic.html", "projects_arabic.html"

RTL_CSS = """<style>
/* Arabic / RTL layer over the shared design system (assets/site.css).
   Same palette and components; only typography and direction change. */
:root{
  --display:"Noto Naskh Arabic","IBM Plex Sans Arabic",serif;
  --sans:"IBM Plex Sans Arabic","Inter",Tahoma,"Segoe UI",sans-serif;
}
body{line-height:1.85}
h1,h2,h3,h4,.brand,.eyebrow,.card__num,.tl__date,.case__dl dt{letter-spacing:0}
h1,h2{line-height:1.5}
h3{line-height:1.6}
h1{font-size:clamp(2.1rem,1.4rem + 3vw,3.3rem)}
.eyebrow{font-size:.8rem;text-transform:none}
.hero::before{background:radial-gradient(60% 60% at 30% 20%,rgba(15,86,70,.06),transparent 70%)}
.hero__role{font-size:1.05rem}
.lede{line-height:1.95}
.nav a::after{transform-origin:right}
.nav a.nav-lang{font-family:"Inter",sans-serif}
.metric{border-left:0;border-right:1px solid var(--line-2)}
.metric:first-child{border-right:0}
.metric b{font-family:"Inter",var(--sans);font-weight:600;direction:ltr;unicode-bidi:isolate;text-align:right}
@media (max-width:700px){.metric{border-right:0}}
.card p,.rows p,.case__dl dd,.bullets li{line-height:1.95}
.rows b{font-size:1.04rem}
.btn svg.flip,.card__link svg{transform:scaleX(-1)}
.ltr{direction:ltr;unicode-bidi:isolate}
.skip{left:auto;right:-9999px}
.skip:focus{left:auto;right:0}
.bullets li{padding-left:0;padding-right:1.35rem}
.bullets li::before{left:auto;right:0}
.timeline{margin-left:0;margin-right:2px}
.timeline::before{left:auto;right:5px}
.tl{padding:0 2.1rem 2.6rem 0}
.tl:last-child{padding-bottom:0}
.tl::before{left:auto;right:0}
.tl__date{font-size:.85rem;text-transform:none}
.case__dl dt{font-size:.82rem;text-transform:none}
.page-head h1{max-width:none}
@media (max-width:860px){.portrait figcaption{text-align:right}}
</style>"""

DL_ICON = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v10.6l3.3-3.3 1.4 1.4L12 '
           '17.4l-4.7-4.7 1.4-1.4 3.3 3.3V3h2zM5 19h14v2H5z"/></svg>')

# ------------------------------------------------------------- leadership ---

ROLES = [
    ("مارس 2026 — حتى الآن", "المدير العام لأكاديمية سدايا",
     "الهيئة السعودية للبيانات والذكاء الاصطناعي (سدايا) · الرياض",
     ["قيادة الذراع الوطنية لبناء القدرات في البيانات والذكاء الاصطناعي، والمسؤولية عن الاستراتيجية والمحفظة وتنفيذ البرامج التدريبية المتقدمة والمعسكرات والشهادات المهنية.",
      "ترجمة أولويات رؤية السعودية 2030 وبرنامج تنمية القدرات البشرية إلى محفظة قابلة للقياس بمؤشرات أداء ومقاييس أثر محددة.",
      "بناء وإدارة الشراكات الاستراتيجية مع الجامعات والمؤسسات البحثية والقطاع الخاص لتطوير المناهج المشتركة وتوسيع المسارات التعليمية المعتمدة.",
      "حوكمة أطر ضمان الجودة والتقييم ومنح الشهادات على مستوى الأكاديمية وفق المعايير الدولية، ومنها خارطة طريق مرحلية نحو شهادة الأيزو 21001 للمؤسسات التعليمية.",
      "استحداث منظومة تقييم واعتماد المدربين والخبراء، ونموذج مؤشرات الأداء وبطاقة الأداء التنفيذية المستخدم في توجيه المحفظة.",
      "توسيع المحفظة المتقدمة لتشمل مسارات الذكاء الاصطناعي الوكيلي، وهندسة البيانات والذكاء الاصطناعي، والإنتاجية بالذكاء الاصطناعي التوليدي، بما يتوافق مع الإطار الوطني للمؤهلات والمعايير المهنية."],
     ["البرامج الوطنية", "رؤية 2030", "أطر الشهادات", "الأيزو 21001", "الشراكات"]),
    ("أغسطس 2024 — مارس 2026", "مدير أكاديمية الذكاء الاصطناعي والمدير المكلّف لحوكمة التقنية",
     "شركة تحكم · الرياض",
     ["تولّي مهمة مزدوجة تجمع بناء قدرات الذكاء الاصطناعي على مستوى الشركة وحوكمة التقنية المؤسسية في شركة وطنية لتقنيات التنقل الذكي والسلامة العامة.",
      "تصميم دليل مكتب إدارة المشاريع الحاكم لدورة حياة المشروع كاملة وترسيخه، وقيادة مراجعات الحوكمة وتقييمات النضج وخرائط المعالجة.",
      "رفع نضج البنية المؤسسية وتوضيح النموذج التشغيلي للحوكمة، بما يربط الاستثمار التقني باستراتيجية الشركة.",
      "إعادة بناء السياسات والإجراءات ودورة حياة تطوير البرمجيات بضوابط جودة متوافقة مع <span class=\"ltr\">CMMI</span>، وتحديث التسليم بممارسات <span class=\"ltr\">DevOps</span> والتكامل والتسليم المستمرين.",
      "بناء منظومة مستدامة لقدرات الذكاء الاصطناعي عبر التدريب المؤسسي والشهادات المبنية على الجدارات ولقاءات الذكاء الاصطناعي الدورية والشراكات بين الأوساط الأكاديمية والقطاع الخاص."],
     ["البنية المؤسسية", "مكتب إدارة المشاريع", "CMMI", "DevOps", "قدرات الذكاء الاصطناعي"]),
    ("أبريل 2024 — أغسطس 2024", "العميد المؤسس لكلية علوم الفضاء والطيران",
     "جامعة الأمير سلطان · الرياض",
     ["تأسيس الكلية من الصفر — الرؤية الأكاديمية والهيكل التنظيمي وبنية البرامج التأسيسية — لتكون من أوائل الكليات المتخصصة في الفضاء والطيران في المملكة."],
     ["البناء المؤسسي"]),
    ("سبتمبر 2020 — أغسطس 2024", "عميد ضمان الجودة والتطوير",
     "جامعة الأمير سلطان · الرياض",
     ["قيادة استراتيجية الجودة على مستوى الجامعة، والحصول على شهادات الأيزو والاعتمادات الأكاديمية الوطنية والدولية.",
      "تطبيق نظام شامل لإدارة الجودة وأطر للتقييم والقياس على مستوى الجامعة.",
      "الارتقاء بالممارسة التدريسية عبر مركز التعليم والتعلّم وتوسيع برامج تطوير أعضاء هيئة التدريس."],
     ["شهادات الأيزو", "الاعتماد الأكاديمي", "إدارة الجودة"]),
    ("سبتمبر 2018 — أغسطس 2020", "عميد الخدمات التعليمية",
     "جامعة الأمير سلطان · الرياض",
     ["المسؤولية عن رحلة الطالب كاملة، وإعادة هيكلة برنامج السنة التحضيرية ليصبح قسماً مستقلاً.",
      "تعزيز عمليات الدعم الأكاديمي: اختبارات تحديد المستوى، والتقييمات المعرفية الفصلية، والإرشاد."],
     ["تجربة الطالب", "الخدمات الأكاديمية"]),
    ("يناير 2015 — أغسطس 2019", "الرئيس التنفيذي لتقنية المعلومات",
     "جامعة الأمير سلطان · الرياض",
     ["وضع الرؤية التقنية للجامعة وتنفيذها، ومواءمة خدمات تقنية المعلومات مع الاستراتيجية المؤسسية.",
      "تنفيذ نظام تخطيط الموارد المؤسسية على مستوى الجامعة في المالية والمحاسبة والموارد البشرية.",
      "تأسيس عملية تخطيط مستمرة لتقنية المعلومات تخدم أعضاء هيئة التدريس والموظفين والطلاب."],
     ["تخطيط الموارد المؤسسية", "استراتيجية التقنية", "التحول الرقمي"]),
    ("سبتمبر 2015 — أغسطس 2016", "رئيس قسم علوم الحاسب",
     "جامعة الأمير سلطان · الرياض",
     ["إعادة تصميم المنهج وفق معايير <span class=\"ltr\">IEEE</span> و<span class=\"ltr\">ACM</span> و<span class=\"ltr\">ABET</span>، وتوسيع المقررات والبرامج.",
      "إدخال آراء جهات التوظيف بصورة منظمة في تصميم البرامج لإبقاء المنهج مواكباً لاحتياج السوق."],
     ["ABET", "المناهج"]),
]

REGIONAL = [
    ("رئيس فريق بناء القدرات والشراكات",
     "اللجنة العربية الدائمة للذكاء الاصطناعي والتقنيات الناشئة · 2026 — حتى الآن",
     "رئاسة أحد الفرق الفنية الستة للجنة العربية الدائمة للذكاء الاصطناعي والتقنيات الناشئة المنبثقة عن مجلس الوزراء العرب للاتصالات والمعلومات. تشمل خطة عمل الفريق 2026–2029 خريطة عربية لقدرات الذكاء الاصطناعي، وإطاراً إقليمياً لمهارات الذكاء الاصطناعي، ومنصة مشتركة للمعرفة والتعلّم، وبرنامج شراكات للتميّز، وبرنامجاً للقيادات والمواهب، وترفع تقاريرها إلى اللجنة والمجلس الوزاري."),
    ("نائب رئيس فريق حوكمة الذكاء الاصطناعي",
     "اللجنة العربية الدائمة للذكاء الاصطناعي والتقنيات الناشئة · 2026 — حتى الآن",
     "نيابة رئاسة الفريق الفني لحوكمة الذكاء الاصطناعي في اللجنة، والعمل على ممارسات حوكمة إقليمية مشتركة لتبنّي الذكاء الاصطناعي في الدول العربية."),
]

CONSULTING = [
    ("مستشار التخطيط الاستراتيجي", "<span class=\"ltr\">CYBEX</span>، جامعة الأمير سلطان", "نوفمبر 2023 — حتى الآن",
     "تقديم المشورة في صياغة الاستراتيجية من البداية إلى النهاية: اختيار المنهجية، وورش العمل مع أصحاب المصلحة، والتوثيق الكامل للرؤية والرسالة والأهداف والمبادرات."),
    ("مستشار هندسة البرمجيات", "مركز الأمير سلطان للدراسات والبحوث الدفاعية", "فبراير 2023 — فبراير 2024",
     "تقديم خبرة هندسة البرمجيات وتوصيات تقنية رفعت كفاءة إجراءات البحث والتحليل."),
    ("الباحث الرئيس، بحث مموّل", "مدينة الملك عبدالعزيز للعلوم والتقنية", "يناير 2017 — ديسمبر 2018",
     "تصميم نظام ديناميكي لتوفير السعة في الشبكات السحابية يستخدم تعلّم الآلة لتوسيع الموارد آلياً بحسب الطلب، بما يرفع كفاءة الشبكة ويخفض التكلفة التشغيلية."),
    ("مستشار هندسة البرمجيات", "شركة تطوير برمجيات", "يونيو 2018 — أكتوبر 2018",
     "تنفيذ مبادرة لتحسين إجراءات تطوير البرمجيات: تحليل الإجراءات القائمة وإدخال أدوات وأساليب حسّنت سرعة التسليم وجودته."),
    ("مستشار علم البيانات", "أحد كبار مشغلي الاتصالات في المملكة", "يناير 2016 — سبتمبر 2016",
     "قيادة تحليل الأسباب الجذرية لتكرار بلاغات خدمة العملاء وتطبيق إجراءات تصحيحية خفّضت التكرار ورفعت رضا العملاء."),
    ("مستشار هندسة البرمجيات", "<span class=\"ltr\">NISC</span>", "يناير 2013 — مايو 2013",
     "قيادة ترحيل نظام مؤسسي لإدارة الفوترة من بنية الخادم والعميل إلى خدمات الويب، بما خفّض التكلفة التشغيلية وحسّن تجربة العميل."),
    ("مستشار هندسة البرمجيات", "<span class=\"ltr\">Wisconsin Falconers Association</span>", "أغسطس 2010 — فبراير 2011",
     "تصميم وبناء نظام حجز عبر الويب يتضمن التوافر الفوري والجدولة والدفع الإلكتروني."),
]

# --------------------------------------------------------------- projects ---

CASE_LABELS = ("التكليف", "ما قمت به", "ما الذي تغيّر")
CASES = [
    ("منظومة جودة وأداء لأكاديمية وطنية", "أكاديمية سدايا · 2026",
     "قيادة الذراع الوطنية لبناء القدرات في البيانات والذكاء الاصطناعي، وإثبات أن محفظتها تُنفَّذ بمستوى ثابت قابل للقياس.",
     "استحداث منظومة لتقييم واعتماد المدربين والخبراء، ومجموعة مؤشرات أداء أساسية مع بطاقة أداء تنفيذية، وخارطة طريق مرحلية نحو شهادة الأيزو 21001.",
     "صارت جودة التنفيذ تُقيَّم وفق معايير منشورة لا وفق السمعة، وتُوجَّه المحفظة وتُرفع تقاريرها إلى القيادة العليا عبر بطاقة أداء واحدة، وأصبح للأكاديمية مسار محدد نحو الاعتماد الدولي."),
    ("حوكمة تقنية تستخدمها فرق التنفيذ فعلاً", "شركة تحكم · 2024–2026",
     "بصفتي المدير المكلّف لحوكمة التقنية في شركة وطنية لتقنيات التنقل الذكي والسلامة العامة: مواءمة الاستثمار التقني والتنفيذ مع استراتيجية الشركة.",
     "تصميم دليل مكتب إدارة المشاريع لدورة حياة المشروع كاملة وترسيخه، وقيادة مراجعات الحوكمة وتقييمات النضج، وإعادة بناء دورة حياة تطوير البرمجيات بضوابط جودة متوافقة مع <span class=\"ltr\">CMMI</span>، وتحديث التسليم بممارسات <span class=\"ltr\">DevOps</span>.",
     "ارتفع نضج البنية المؤسسية، واتضح النموذج التشغيلي للحوكمة، واكتسب التسليم سرعة وقابلية تتبع ونضجاً إجرائياً قابلاً للقياس."),
    ("جودة أثمرت شهادات واعتمادات", "جامعة الأمير سلطان · 2020–2024",
     "بصفتي عميد ضمان الجودة والتطوير: المسؤولية عن استراتيجية الجودة على مستوى الجامعة.",
     "تطبيق نظام شامل لإدارة الجودة مع أطر للتقييم والقياس على مستوى الجامعة، وتوسيع تطوير أعضاء هيئة التدريس عبر مركز التعليم والتعلّم.",
     "حصلت الجامعة على شهادات الأيزو والاعتمادات الأكاديمية الوطنية والدولية."),
    ("نظام واحد لموارد الجامعة", "جامعة الأمير سلطان · 2015–2019",
     "بصفتي الرئيس التنفيذي لتقنية المعلومات: وضع الرؤية التقنية للجامعة ومواءمة خدمات التقنية مع الاستراتيجية المؤسسية.",
     "تنفيذ نظام تخطيط الموارد المؤسسية على مستوى الجامعة في المالية والمحاسبة والموارد البشرية، وتأسيس عملية تخطيط مستمرة لتقنية المعلومات.",
     "أصبحت الوظائف الإدارية الأساسية تعمل على نظام واحد، وصار تخطيط التقنية عملية دائمة تخدم أعضاء هيئة التدريس والموظفين والطلاب."),
]

PROGRAMMES = [
    ("بكالوريوس هندسة البرمجيات", "جامعة الأمير سلطان",
     "تصميم المنهج الجامعي كاملاً ومتابعته حتى الاعتماد، وفق معايير <span class=\"ltr\">IEEE</span> و<span class=\"ltr\">ACM</span> و<span class=\"ltr\">ABET</span>."),
    ("ماجستير هندسة البرمجيات", "جامعة الأمير سلطان",
     "بنية برنامج الدراسات العليا وتسلسل المقررات ومخرجات التعلّم."),
    ("ماجستير هندسة الأمن السيبراني", "جامعة الأمير سلطان",
     "برنامج دراسات عليا يلبّي الطلب الوطني على كفاءات هندسة الأمن."),
    ("مسار التحول الرقمي", "جامعة الأمير سلطان",
     "مسار تخصصي جديد يربط تعليم هندسة البرمجيات بممارسة التحول المؤسسي."),
    ("ستة مقررات جديدة", "<span class=\"ltr\">SE 411 · SE 311 · SE 415 · SE 489 · SE 495 · CYS 402</span>",
     "بناء البرمجيات، وهندسة المتطلبات، وديناميكيات الفرق والممارسة المهنية، وهندسة <span class=\"ltr\">DevOps</span>، وريادة الأعمال البرمجية، وهندسة البرمجيات الآمنة."),
    ("محفظة برامج أكاديمية سدايا", "سدايا · 2026 — حتى الآن",
     "برامج تدريبية متقدمة ومعسكرات وشهادات مهنية، مع أطر لضمان الجودة والتقييم ومنح الشهادات وفق المعايير الدولية."),
    ("مسارات الذكاء الاصطناعي الوكيلي وهندسة البيانات", "أكاديمية سدايا · 2026",
     "مسارات متقدمة جديدة في بناء أنظمة الذكاء الاصطناعي الوكيلي، وهندسة النماذج اللغوية والبيانات، والإنتاجية بالذكاء الاصطناعي التوليدي، مرتبطة بالإطار الوطني للمؤهلات والمعايير المهنية."),
]

SYSTEMS = [
    ("نظام إدارة الجودة والاعتماد", "جامعة الأمير سلطان · 2020–2024",
     "نظام لإدارة الجودة على مستوى الجامعة مع أطر للتقييم والقياس؛ وهو الأساس الذي قامت عليه شهادات الأيزو والاعتمادات الأكاديمية الوطنية والدولية."),
    ("تخطيط الموارد المؤسسية", "جامعة الأمير سلطان · 2015–2019",
     "تطبيق النظام في المالية والمحاسبة والموارد البشرية، مع عملية تخطيط مستمرة لتقنية المعلومات."),
    ("إعادة هيكلة برنامج السنة التحضيرية", "جامعة الأمير سلطان · 2018–2020",
     "إعادة بناء رحلة الطالب كاملة وتأسيس السنة التحضيرية قسماً مستقلاً."),
    ("كلية علوم الفضاء والطيران", "جامعة الأمير سلطان · 2024",
     "تأسيسها بصفتي أول عميد لها: الرؤية الأكاديمية والهيكل التنظيمي وبنية البرامج التأسيسية."),
    ("توسعة مركز التعليم والتعلّم", "جامعة الأمير سلطان",
     "تعميم برامج تطوير أعضاء هيئة التدريس على مستوى الجامعة للارتقاء بالممارسة التدريسية."),
    ("منظومة اعتماد المدربين", "أكاديمية سدايا · 2026",
     "منظومة لتقييم واعتماد المدربين والخبراء، لتُقيَّم جودة التنفيذ وفق معايير منشورة لا وفق السمعة."),
    ("خارطة طريق الأيزو 21001", "أكاديمية سدايا · 2026",
     "خطة تنفيذ مرحلية تنقل نظام إدارة الأكاديمية نحو شهادة الأيزو 21001 للمؤسسات التعليمية."),
    ("منظومة قياس الأداء", "أكاديمية سدايا · 2026",
     "مجموعة مؤشرات أداء أساسية وبطاقة أداء تنفيذية تغطي وحدات الأكاديمية، تُستخدم في توجيه المحفظة ورفع تقارير الأثر إلى القيادة العليا."),
]

GOVERNANCE = [
    ("دليل مكتب إدارة المشاريع", "شركة تحكم · 2024–2026",
     "دليل حاكم لدورة حياة المشروع كاملة، مع مراجعات حوكمة وتقييمات نضج وخرائط معالجة لحماية قيمة المشاريع."),
    ("نضج البنية المؤسسية", "شركة تحكم",
     "رفع نضج البنية المؤسسية وتوضيح النموذج التشغيلي للحوكمة ليتبع الاستثمار التقني استراتيجية الشركة."),
    ("دورة حياة تطوير متوافقة مع <span class=\"ltr\">CMMI</span>", "شركة تحكم",
     "إعادة بناء السياسات والإجراءات ودورة حياة تطوير البرمجيات بضوابط جودة متوافقة مع <span class=\"ltr\">CMMI</span> ومكاسب نضج قابلة للقياس."),
    ("ممارسات <span class=\"ltr\">DevOps</span> والتسليم المستمر", "شركة تحكم",
     "تحديث سلسلة الأدوات ومسار التسليم، بما حسّن سرعة التسليم وقابلية التتبع وجودة البرمجيات."),
    ("منظومة قدرات الذكاء الاصطناعي المؤسسية", "شركة تحكم",
     "برامج تدريب مؤسسية وشهادات مبنية على الجدارات ولقاءات دورية للذكاء الاصطناعي وشراكات بين الأوساط الأكاديمية والقطاع الخاص."),
]

RESEARCH = [
    ("توفير السعة الديناميكي في الشبكات السحابية", "بتمويل من مدينة الملك عبدالعزيز للعلوم والتقنية · 2017–2018",
     "بصفتي الباحث الرئيس: بنية قابلة للتوسع تضبط موارد الشبكة بحسب تغيّر الطلب، وتستخدم تعلّم الآلة لتحسين الأداء وتقليل هدر الموارد."),
    ("تحليل الأسباب الجذرية لبلاغات خدمة العملاء", "أحد كبار مشغلي الاتصالات في المملكة · 2016",
     "قيادة تحليل أنماط البلاغات وراء ارتفاع نسبة التكرار، ثم تطبيق إجراءات تصحيحية خفّضته."),
    ("ترحيل منصة الفوترة", "<span class=\"ltr\">NISC</span> · 2013",
     "قيادة ترحيل نظام مؤسسي لإدارة الفوترة من بنية الخادم والعميل إلى خدمات الويب."),
    ("صياغة الاستراتيجية", "<span class=\"ltr\">CYBEX</span>، جامعة الأمير سلطان · 2023 — حتى الآن",
     "اختيار المنهجية وورش العمل مع أصحاب المصلحة والتوثيق الكامل للرؤية والرسالة والأهداف والمبادرات."),
    ("تحسين إجراءات تطوير البرمجيات", "شركة تطوير برمجيات · 2018",
     "تحليل الإجراءات وإدخال أدوات جديدة حسّنت سرعة التطوير وجودته."),
]


# ------------------------------------------------------------------ shell ---

def shell(B, slug, en_slug, title, desc, og_title, body):
    site = B.SITE
    en_url = site + ("" if en_slug == "index.html" else en_slug)
    ld = {"@context": "https://schema.org", "@type": "Person", "name": "Mamdouh Alenezi",
          "alternateName": "ممدوح العنزي", "honorificPrefix": "Prof.", "honorificSuffix": "Ph.D.",
          "jobTitle": "المدير العام لأكاديمية سدايا",
          "description": "قيادي تنفيذي في بناء القدرات الوطنية في البيانات والذكاء الاصطناعي وحوكمة التقنية والتحول الرقمي، وأستاذ هندسة البرمجيات.",
          "url": site + HOME, "image": site + "images/newprofile.png",
          "worksFor": {"@type": "Organization", "name": "الهيئة السعودية للبيانات والذكاء الاصطناعي (سدايا)",
                       "alternateName": "SDAIA — Saudi Data & Artificial Intelligence Authority"},
          "address": {"@type": "PostalAddress", "addressLocality": "Riyadh", "addressCountry": "SA"},
          "knowsLanguage": ["ar", "en"],
          "sameAs": [site] + [u for n, u, _ in B.PROFILES if n in ("Google Scholar", "LinkedIn", "ORCID", "X")]}
    nav = [(LEAD, "القيادة والخبرات", ""), (PROJ, "المشاريع والأثر", ""),
           ("publications.html", "الأبحاث", ' hreflang="en"'), ("myCV-Arabic.pdf", "السيرة الذاتية", "")]
    nav_html = "".join('<li><a href="{h}"{x}{cur}>{t}</a></li>'.format(
        h=h, t=t, x=x, cur=' aria-current="page"' if h == slug else "") for h, t, x in nav)
    foot = [(HOME, "الرئيسية", ""), (LEAD, "القيادة والخبرات", ""), (PROJ, "المشاريع والأثر", ""),
            ("publications.html", "الأبحاث", ' hreflang="en"'), ("speaking.html", "المشاركات", ' hreflang="en"'),
            ("myblog/", "المقالات", ""), ("contact.html", "تواصل", ' hreflang="en"'),
            (en_slug, "English", ' hreflang="en" lang="en"')]
    foot_html = "".join('<li><a href="{h}"{x}>{t}</a></li>'.format(h=h, t=t, x=x) for h, t, x in foot)
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Mamdouh Alenezi">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#0f5646">
<link rel="canonical" href="{site}{slug}">
<link rel="alternate" hreflang="ar" href="{site}{slug}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">
<link rel="icon" href="images/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="images/newprofile.png">

<meta property="og:type" content="profile">
<meta property="og:site_name" content="Prof. Mamdouh Alenezi">
<meta property="og:locale" content="ar_SA">
<meta property="og:locale:alternate" content="en">
<meta property="og:title" content="{og}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{site}{slug}">
<meta property="og:image" content="{site}images/newprofile.png">
<meta property="og:image:alt" content="الصورة الشخصية للأستاذ الدكتور ممدوح العنزي">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@MamdouhAlenezi">
<meta name="twitter:title" content="{og}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{site}images/newprofile.png">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&family=Noto+Naskh+Arabic:wght@600;700&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="assets/site.css">
{css}
<script>if(!window.matchMedia("(prefers-reduced-motion: reduce)").matches){{document.documentElement.className+=" js";}}</script>
<script type="application/ld+json">{ld}</script>
</head>
<body>
<a class="skip" href="#main">تخطَّ إلى المحتوى</a>

<header class="site-head">
  <div class="site-head__in">
    <a class="brand" href="{home}">ممدوح <span>العنزي</span></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="primary-nav" aria-label="القائمة">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
    <ul class="nav" id="primary-nav">
      {nav}
      <li><a class="nav-lang" href="{en_slug}" hreflang="en" lang="en">English</a></li>
      <li><a class="nav-cta" href="contact.html" hreflang="en">تواصل</a></li>
    </ul>
  </div>
</header>

<main id="main">
{body}
</main>

<footer class="site-foot">
  <div class="site-foot__in">
    <ul class="foot-nav">{foot}</ul>
    <div class="foot-bottom">
      <p>&copy; {year} ممدوح العنزي · الرياض، المملكة العربية السعودية</p>
      <p><a href="mailto:{email}" class="ltr">{email}</a></p>
    </div>
  </div>
</footer>
<script src="assets/site.js" defer></script>
{analytics}</body>
</html>
""".format(title=html.escape(title), desc=html.escape(desc), og=html.escape(og_title), site=site, slug=slug,
           en_url=en_url, en_slug=en_slug, css=RTL_CSS, ld=json.dumps(ld, ensure_ascii=False),
           home=HOME, nav=nav_html, foot=foot_html, body=B.alternate(body), year=datetime.now().year,
           email=B.EMAIL, analytics=B.analytics_tag())


def page_head(eyebrow, title, lede):
    return """
<section class="page-head">
  <div class="wrap">
    <span class="eyebrow">{e}</span>
    <h1>{t}</h1>
    <p>{l}</p>
  </div>
</section>""".format(e=eyebrow, t=title, l=lede)


def rows(items):
    return '<ul class="rows reveal">%s</ul>' % "".join(
        "<li><b>{t}</b><span>{m}</span><p>{d}</p></li>".format(t=t, m=m, d=d) for t, m, d in items)


# ------------------------------------------------------------------ pages ---

def build_home(B, pubs):
    reviewed = B.peer_reviewed(pubs)["reviewed"]
    profiles = B.profile_links(["Google Scholar", "LinkedIn", "ORCID", "X"])
    body = """
<section class="hero">
  <div class="wrap hero__grid">
    <div>
      <span class="eyebrow">أ.د. ممدوح العنزي · الرياض، المملكة العربية السعودية</span>
      <h1>تحويل الطموح الوطني في الذكاء الاصطناعي إلى <em>قدرات مستدامة</em>.</h1>
      <p class="hero__role">المدير العام لأكاديمية سدايا <span>أستاذ هندسة البرمجيات · ممارس معتمد في إدارة التغيير من <span class="ltr">Prosci®</span></span></p>
      <p class="lede">أعمل على تحويل الطموحات الوطنية في البيانات والذكاء الاصطناعي إلى قدرات مؤسسية وبشرية مستدامة، عبر قيادة البرامج الوطنية، وتطوير حوكمة التقنية، وربط البحث العلمي بالتطبيق العملي.</p>
      <div class="btn-row">
        <a class="btn btn--solid" href="{lead}">القيادة والخبرات</a>
        <a class="btn btn--ghost" href="{proj}">المشاريع والأثر</a>
        <a class="btn btn--ghost" href="myCV-Arabic.pdf">{dl} تحميل السيرة الذاتية</a>
      </div>
      {profiles}
    </div>
    <figure class="portrait">
      <img src="images/newprofile.png" width="512" height="512" alt="الصورة الشخصية للأستاذ الدكتور ممدوح العنزي" fetchpriority="high" decoding="async">
    </figure>
  </div>
</section>

<section class="wrap" aria-label="أبرز المؤشرات">
  <div class="metrics">
    <div class="metric"><b>{reviewed}</b><span>منشوراً علمياً</span><small>محكّماً</small></div>
    <div class="metric"><b>{cit}</b><span>استشهاد بحثي</span><small>Google Scholar</small></div>
    <div class="metric"><b>{h}</b><span>مؤشر هيرش</span><small class="ltr">h-index</small></div>
    <div class="metric"><b>{i10}</b><span>مؤشر i10</span><small>إجمالي المسيرة</small></div>
    <div class="metric"><b>2015</b><span>في المناصب التنفيذية منذ</span><small>رئيس تقنية · عميد · مدير · مدير عام</small></div>
  </div>
</section>

<section class="sec" id="areas">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">مجالات التركيز</span>
      <h2>ثلاثة مسارات يجمعها أثر واحد.</h2>
      <p>من الاستراتيجية إلى التنفيذ، ومن المعرفة إلى الممارسة.</p>
    </div>
    <div class="grid grid--3">
      <article class="card reveal"><span class="card__num">01</span><h3>بناء القدرات الوطنية في البيانات والذكاء الاصطناعي</h3><p>قيادة أكاديمية سدايا وتطوير منظومة البرامج المتقدمة والمعسكرات والشهادات المهنية والشراكات، بما يخدم الاحتياجات الوطنية وأولويات رؤية السعودية 2030.</p></article>
      <article class="card reveal"><span class="card__num">02</span><h3>حوكمة التقنية والتحول المؤسسي</h3><p>تطوير الحوكمة المؤسسية والبنية المؤسسية وإدارة المشاريع ودورة حياة البرمجيات، وتعزيز جودة التنفيذ عبر الممارسات الهندسية والتحسين المستمر.</p></article>
      <article class="card reveal"><span class="card__num">03</span><h3>البحث العلمي وهندسة البرمجيات</h3><p>أبحاث في الذكاء الاصطناعي وهندسة البرمجيات وأمن الأنظمة والتحول الرقمي، مع تركيز حديث على الأنظمة الوكيلة وهندسة البرمجيات المدعومة بالذكاء الاصطناعي.</p></article>
    </div>
  </div>
</section>

<section class="sec" id="achievements">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">محطات مختارة</span>
      <h2>أبرز الإنجازات والأدوار.</h2>
    </div>
    <ul class="rows reveal">
      <li><b>قيادة أكاديمية سدايا</b><span>سدايا · منذ 2026</span><p>الإشراف على الاستراتيجية والمحفظة التدريبية والشهادات المهنية وأطر الجودة والتقييم وقياس الأثر.</p></li>
      <li><b>أدوار قيادية إقليمية</b><span>اللجنة العربية للذكاء الاصطناعي · 2026</span><p>رئاسة فريق بناء القدرات والشراكات، ونيابة رئاسة فريق حوكمة الذكاء الاصطناعي ضمن اللجنة العربية الدائمة للذكاء الاصطناعي والتقنيات الناشئة.</p></li>
      <li><b>تطوير حوكمة التقنية ومنظومة الذكاء الاصطناعي</b><span>شركة تحكم · 2024 – 2026</span><p>قيادة أكاديمية الذكاء الاصطناعي، وتطوير حوكمة المشاريع والبنية المؤسسية وممارسات تطوير وتسليم البرمجيات.</p></li>
      <li><b>العميد المؤسس لكلية علوم الفضاء والطيران</b><span>جامعة الأمير سلطان · 2024</span><p>تأسيس الرؤية الأكاديمية والهيكل التنظيمي والبرامج الأولية للكلية.</p></li>
      <li><b>قيادة الجودة والاعتماد الأكاديمي</b><span>جامعة الأمير سلطان · 2020 – 2024</span><p>تطوير منظومة إدارة الجودة ودعم الاعتمادات الأكاديمية وشهادات الأيزو على مستوى الجامعة.</p></li>
      <li><b>التحول الرقمي وتطوير البرامج الأكاديمية</b><span>جامعة الأمير سلطان · 2015 – 2024</span><p>قيادة تنفيذ نظام تخطيط الموارد المؤسسية، وتصميم برامج وتخصصات في هندسة البرمجيات والأمن السيبراني.</p></li>
    </ul>
    <div class="btn-row" style="margin-top:2rem">
      <a class="btn btn--solid" href="{proj}#cases">أربع حالات بالتفصيل</a>
      <a class="btn btn--ghost" href="{lead}">السجل القيادي الكامل</a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="callout reveal">
      <h2>المزيد عن المسيرة والأبحاث.</h2>
      <p>السجل القيادي والمشاريع متاحة بالعربية، وقائمة الأبحاث العلمية والمقالات متاحة على الموقع باللغة الإنجليزية.</p>
      <div class="btn-row">
        <a class="btn btn--solid" href="publications.html" hreflang="en">الأبحاث العلمية</a>
        <a class="btn btn--ghost" href="myCV-Arabic.pdf">السيرة الذاتية بالعربية</a>
        <a class="btn btn--ghost" href="mailto:{email}"><span class="ltr">{email}</span></a>
      </div>
    </div>
  </div>
</section>
""".format(lead=LEAD, proj=PROJ, dl=DL_ICON, profiles=profiles, reviewed=reviewed, cit=B.CITATIONS,
           h=B.H_INDEX, i10=B.I10_INDEX, email=B.EMAIL)
    return shell(B, HOME, "index.html",
                 "أ.د. ممدوح العنزي — بناء القدرات في الذكاء الاصطناعي وحوكمة التقنية وهندسة البرمجيات",
                 "الأستاذ الدكتور ممدوح العنزي، المدير العام لأكاديمية سدايا وأستاذ هندسة البرمجيات: بناء القدرات "
                 "الوطنية في البيانات والذكاء الاصطناعي، وحوكمة التقنية، و%d منشوراً علمياً محكّماً بأكثر من %s استشهاد."
                 % (reviewed, B.CITATIONS.rstrip("+")),
                 "أ.د. ممدوح العنزي — المدير العام لأكاديمية سدايا", body)


def build_leadership(B):
    tl = "".join(
        '<li class="tl reveal"><span class="tl__date">{d}</span><h3>{t}</h3><p class="tl__org">{o}</p>{p}{g}</li>'.format(
            d=d, t=t, o=o, p=B.bullets(pts), g=B.tags(tg)) for d, t, o, pts, tg in ROLES)
    cons = "".join("<li><b>{t}</b><span>{d}</span><p><strong>{o}</strong> — {n}</p></li>".format(t=t, o=o, d=d, n=n)
                   for t, o, d, n in CONSULTING)
    body = page_head("القيادة والخبرات", "من رئاسة قسم إلى تكليف وطني.",
                     "أكثر من عقد من القيادة التنفيذية والأكاديمية المتدرجة في بناء قدرات الذكاء الاصطناعي "
                     "وطنياً وإقليمياً، وحوكمة التقنية، وتحويل التعليم العالي.") + """
<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">المناصب التنفيذية والأكاديمية</span>
      <h2>السجل.</h2>
    </div>
    <ol class="timeline">{tl}</ol>
  </div>
</section>

<section class="sec" id="regional">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">التكليف الإقليمي</span>
      <h2>اللجنة العربية الدائمة للذكاء الاصطناعي.</h2>
      <p>موقعان قياديان في الفرق الفنية الستة المنبثقة عن مجلس الوزراء العرب للاتصالات والمعلومات.</p>
    </div>
    {regional}
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">الاستشارات والبحوث المموّلة</span>
      <h2>أعمال استشارية وتطبيقية.</h2>
      <p>تكليفات كان المطلوب فيها تشخيص مشكلة محددة وترك حل يعمل.</p>
    </div>
    <ul class="rows reveal">{cons}</ul>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="callout reveal">
      <h2>التفاصيل وراء المناصب.</h2>
      <p>صفحة المشاريع والأثر تعرض ما بُني فعلاً. أما المقررات التي درّستها والإشراف على طلاب الدراسات العليا وعضوية اللجان فمتاحة في النسخة الإنجليزية.</p>
      <div class="btn-row">
        <a class="btn btn--solid" href="{proj}">المشاريع والأثر</a>
        <a class="btn btn--ghost" href="myCV-Arabic.pdf">السيرة الذاتية بالعربية</a>
        <a class="btn btn--ghost" href="leadership.html#teaching" hreflang="en">التدريس والإشراف (بالإنجليزية)</a>
      </div>
    </div>
  </div>
</section>
""".format(tl=tl, regional=rows(REGIONAL), cons=cons, proj=PROJ)
    return shell(B, LEAD, "leadership.html", "القيادة والخبرات — أ.د. ممدوح العنزي",
                 "المناصب التنفيذية والأكاديمية للأستاذ الدكتور ممدوح العنزي: أكاديمية سدايا، واللجنة العربية "
                 "الدائمة للذكاء الاصطناعي، وشركة تحكم، وجامعة الأمير سلطان، مع الاستشارات والبحوث المموّلة.",
                 "القيادة والخبرات — أ.د. ممدوح العنزي", body)


def build_projects(B):
    body = page_head("المشاريع والأثر", "ما الذي بُني فعلاً.",
                     "برامج وأنظمة مؤسسية وأطر حوكمة وبحوث مموّلة — العمل الذي يقف وراء المسميات الوظيفية.") + """
<section class="sec" id="cases">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">حالات مختارة</span>
      <h2>أربعة تكليفات، وما الذي تغيّر.</h2>
      <p>النسخة المختصرة لمن يريد النتائج قبل التفاصيل: ما الذي كُلّفت به، وما الذي قمت به، وما الذي اختلف بعده.</p>
    </div>
    {cases}
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">البرامج والمناهج</span>
      <h2>تعليم لم يكن موجوداً من قبل.</h2>
      <p>برامج أكاديمية ومسارات ومقررات صُممت من الصفر، إضافة إلى المحفظة التدريبية الوطنية التي أقودها اليوم.</p>
    </div>
    {programmes}
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">الأنظمة المؤسسية</span>
      <h2>الجودة والتقنية والهيكلة.</h2>
    </div>
    {systems}
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">الحوكمة والتنفيذ</span>
      <h2>تنفيذ يمكن التنبؤ به.</h2>
      <p>الآليات التشغيلية — البنية المؤسسية وحوكمة المحافظ وضوابط دورة الحياة ومسارات التسليم — التي تحدد هل تتحول الاستراتيجية إلى واقع.</p>
    </div>
    {governance}
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">البحوث التطبيقية والمموّلة</span>
      <h2>مشكلات لها صاحب.</h2>
    </div>
    {research}
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="callout reveal">
      <h2>هل تبحثون عن شريك في عمل مشابه؟</h2>
      <p>برامج بناء القدرات، والنماذج التشغيلية للحوكمة، وأنظمة الجودة والاعتماد، أو نقل البحث إلى التطبيق.</p>
      <div class="btn-row">
        <a class="btn btn--solid" href="mailto:{email}"><span class="ltr">{email}</span></a>
        <a class="btn btn--ghost" href="{lead}">القيادة والخبرات</a>
      </div>
    </div>
  </div>
</section>
""".format(cases=B.cases_block(CASES, CASE_LABELS), programmes=rows(PROGRAMMES), systems=rows(SYSTEMS),
           governance=rows(GOVERNANCE), research=rows(RESEARCH), email=B.EMAIL, lead=LEAD)
    return shell(B, PROJ, "projects.html", "المشاريع والأثر — أ.د. ممدوح العنزي",
                 "برامج أكاديمية وأنظمة مؤسسية وأطر حوكمة وبحوث مموّلة بناها الأستاذ الدكتور ممدوح العنزي في "
                 "سدايا وشركة تحكم وجامعة الأمير سلطان، مع أربع حالات مختارة.",
                 "المشاريع والأثر — أ.د. ممدوح العنزي", body)


def build_all(B, pubs, insights):
    return [(HOME, build_home(B, pubs)), (LEAD, build_leadership(B)), (PROJ, build_projects(B))]
