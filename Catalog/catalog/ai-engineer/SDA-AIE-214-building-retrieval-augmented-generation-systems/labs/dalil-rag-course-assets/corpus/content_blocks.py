"""
content_blocks.py -- the writing that Layer B is assembled from.

Kept separate from the generator so a course team can localise or re-theme the
synthetic overlay (different fictional entity, different domain) without
touching generation logic. Every block is fictional; every block cites a real
Layer A instrument by title so that cross-layer multi-hop questions work.
"""

ORG_EN = "National Digital Services Authority"
ORG_AR = "الهيئة الوطنية للخدمات الرقمية"

# --------------------------------------------------------------------------
# Layer A instruments that Layer B documents cite (title only -- the article
# text lives in the real PDFs fetched by fetch_corpus.py)
# --------------------------------------------------------------------------
LAYER_A_REFS = [
    ("pdpl-law", "Personal Data Protection Law", "نظام حماية البيانات الشخصية"),
    ("pdpl-implementing-regulation", "Implementing Regulation of the PDPL",
     "اللائحة التنفيذية لنظام حماية البيانات الشخصية"),
    ("pdpl-data-transfer-regulation", "Regulation on Personal Data Transfer outside the Kingdom",
     "ضوابط نقل البيانات الشخصية خارج المملكة"),
    ("data-classification-policy", "Data Classification Policy", "سياسة تصنيف البيانات"),
    ("data-sharing-policy", "Data Sharing Policy", "سياسة مشاركة البيانات"),
    ("open-data-policy", "Open Data Policy", "سياسة البيانات المفتوحة"),
    ("ai-ethics-principles", "AI Ethics Principles", "مبادئ أخلاقيات الذكاء الاصطناعي"),
    ("genai-guideline-government", "Generative AI Guidelines for Government",
     "أدلة الذكاء الاصطناعي التوليدي للجهات الحكومية"),
    ("data-anonymization-guideline", "Personal Data Anonymization Guideline",
     "دليل إخفاء هوية البيانات الشخصية"),
    ("data-destruction-guideline", "Personal Data Destruction Guideline",
     "دليل إتلاف البيانات الشخصية"),
]

# --------------------------------------------------------------------------
# HR policy topics -- Arabic (scanned) and English (digital) editions
# --------------------------------------------------------------------------
HR_TOPICS = [
    ("remote-work", "Remote Work Policy", "سياسة العمل عن بُعد",
     "eligibility, approval workflow, equipment, and information-security duties for remote work",
     "شروط الاستحقاق وإجراءات الموافقة والأجهزة والتزامات أمن المعلومات للعمل عن بُعد"),
    ("housing-allowance", "Housing Allowance Policy", "سياسة بدل السكن",
     "entitlement bands, proration on joining and leaving, and payment cycle for housing allowance",
     "شرائح الاستحقاق والاحتساب النسبي عند المباشرة والانتهاء ودورة الصرف لبدل السكن"),
    ("travel-allowance", "Business Travel and Per-Diem Policy", "سياسة السفر في مهمة عمل والبدلات",
     "per-diem bands by destination class, ticket class entitlement, and expense evidence rules",
     "شرائح البدل اليومي حسب فئة الوجهة ودرجة التذكرة وقواعد إثبات المصروفات"),
    ("annual-leave", "Annual Leave Policy", "سياسة الإجازة السنوية",
     "accrual rate, carry-over ceiling, and encashment on separation",
     "معدل الاستحقاق وحد الترحيل والتعويض النقدي عند انتهاء الخدمة"),
    ("training-sponsorship", "Training and Sponsorship Policy", "سياسة التدريب والابتعاث",
     "sponsorship tiers, service-bond duration, and reimbursement on early exit",
     "فئات الابتعاث ومدة الالتزام الوظيفي واسترداد التكاليف عند الانفكاك المبكر"),
    ("performance-review", "Performance Management Policy", "سياسة إدارة الأداء",
     "rating scale, calibration, and the link between rating and the annual increment",
     "مقياس التقييم وجلسات المعايرة وارتباط التقدير بالعلاوة السنوية"),
    ("secondment", "Secondment and Assignment Policy", "سياسة الإعارة والانتداب",
     "internal and external secondment terms, duration caps, and return rights",
     "أحكام الإعارة الداخلية والخارجية وحدود المدة وحقوق العودة"),
    ("grievance", "Grievance and Appeals Policy", "سياسة التظلمات",
     "filing window, committee composition, and confidentiality of grievance records",
     "مدة تقديم التظلم وتشكيل اللجنة وسرية سجلات التظلم"),
    ("recruitment-data", "Candidate Data Handling Policy", "سياسة معالجة بيانات المرشحين",
     "retention of unsuccessful-candidate records and the lawful basis for CV processing",
     "مدة الاحتفاظ بسجلات المرشحين غير المقبولين والأساس النظامي لمعالجة السير الذاتية"),
    ("employee-records", "Employee Records Retention Policy", "سياسة الاحتفاظ بسجلات الموظفين",
     "retention periods per record class and destruction evidence requirements",
     "مدد الاحتفاظ حسب فئة السجل ومتطلبات إثبات الإتلاف"),
    ("disciplinary", "Disciplinary Procedure", "لائحة الجزاءات",
     "graduated sanctions, investigation timelines, and record expiry",
     "تدرج الجزاءات ومدد التحقيق وسقوط القيد"),
]

# --------------------------------------------------------------------------
# IT procedures (DOCX)
# --------------------------------------------------------------------------
IT_TOPICS = [
    ("access-provisioning", "Identity and Access Provisioning Procedure",
     "joiner/mover/leaver access changes and quarterly recertification"),
    ("incident-response", "Information Security Incident Response Procedure",
     "severity matrix, escalation clock, and personal-data breach notification path"),
    ("backup-restore", "Backup and Restore Procedure", "backup tiers, RPO/RTO targets, and restore testing"),
    ("change-management", "Change Management Procedure", "change classes, CAB thresholds, and emergency changes"),
    ("data-export", "Data Export and Cross-Border Transfer Procedure",
     "approval chain and transfer risk assessment before any export outside the Kingdom"),
    ("llm-gateway", "Approved LLM Gateway Usage Procedure",
     "which data classes may be sent to which model tier, logging, and prohibited inputs"),
    ("vendor-onboarding", "Third-Party and Processor Onboarding Procedure",
     "due diligence, processing agreement clauses, and sub-processor notification"),
    ("device-hardening", "Endpoint Hardening Standard", "baseline configuration and exception handling"),
    ("log-retention", "Logging and Monitoring Standard", "log classes, retention, and access to audit trails"),
    ("data-deletion", "Data Deletion Request Handling Procedure",
     "intake, verification, execution window, and evidence of destruction"),
]

# --------------------------------------------------------------------------
# Circular subjects -- identifier-heavy, some superseded (F4 + F8)
# --------------------------------------------------------------------------
CIRCULAR_SUBJECTS = [
    ("Updated housing allowance bands", "تحديث شرائح بدل السكن"),
    ("Remote work approval delegation", "تفويض اعتماد العمل عن بُعد"),
    ("Mandatory data classification refresher", "التدريب التنشيطي الإلزامي لتصنيف البيانات"),
    ("Restrictions on public generative AI tools", "ضوابط استخدام أدوات الذكاء الاصطناعي التوليدي العامة"),
    ("Cross-border transfer pre-approval", "الموافقة المسبقة لنقل البيانات خارج المملكة"),
    ("Per-diem rate revision for Gulf destinations", "تعديل البدل اليومي لوجهات الخليج"),
    ("Annual leave carry-over ceiling change", "تعديل حد ترحيل الإجازة السنوية"),
    ("Personal data breach reporting channel", "قناة الإبلاغ عن حوادث البيانات الشخصية"),
    ("Records retention schedule update", "تحديث جدول الاحتفاظ بالسجلات"),
    ("Training bond recalculation method", "طريقة إعادة احتساب الالتزام التدريبي"),
    ("Contractor access recertification", "إعادة اعتماد صلاحيات المتعاقدين"),
    ("Anonymisation standard for analytics datasets", "معيار إخفاء الهوية لمجموعات بيانات التحليلات"),
    ("Data sharing request intake form", "نموذج طلب مشاركة البيانات"),
    ("Open data publication checklist", "قائمة التحقق لنشر البيانات المفتوحة"),
    ("Secondment allowance clarification", "إيضاح بدل الإعارة"),
    ("Performance calibration calendar", "تقويم معايرة الأداء"),
    ("Emergency change approval quorum", "نصاب اعتماد التغيير الطارئ"),
    ("Processor sub-contracting notice period", "مدة الإشعار للتعاقد من الباطن"),
]

# --------------------------------------------------------------------------
# Intranet page subjects (HTML, boilerplate-heavy on purpose)
# --------------------------------------------------------------------------
INTRANET_TOPICS = [
    ("how-to-request-leave", "How to request leave", "كيفية طلب إجازة"),
    ("who-to-contact-hr", "Who to contact in HR", "جهات التواصل في الموارد البشرية"),
    ("data-classification-quickref", "Data classification quick reference", "مرجع سريع لتصنيف البيانات"),
    ("expense-claim-steps", "Submitting an expense claim", "تقديم مطالبة مصروفات"),
    ("new-joiner-checklist", "New joiner checklist", "قائمة تحقق الموظف الجديد"),
    ("security-awareness", "Security awareness essentials", "أساسيات التوعية الأمنية"),
    ("using-the-llm-gateway", "Using the approved LLM gateway", "استخدام بوابة النماذج اللغوية المعتمدة"),
    ("reporting-a-breach", "Reporting a suspected data breach", "الإبلاغ عن اشتباه بحادثة بيانات"),
    ("requesting-a-dataset", "Requesting an internal dataset", "طلب مجموعة بيانات داخلية"),
    ("travel-booking", "Booking business travel", "حجز السفر في مهمة عمل"),
    ("it-service-desk", "Contacting the IT service desk", "التواصل مع مكتب خدمات تقنية المعلومات"),
    ("policy-index", "Policy index", "فهرس السياسات"),
]

BOILERPLATE_HTML_NAV = """
<nav class="site-nav"><ul>
<li><a href="/home">Home</a></li><li><a href="/hr">HR</a></li>
<li><a href="/it">IT</a></li><li><a href="/finance">Finance</a></li>
<li><a href="/policies">Policies</a></li><li><a href="/contact">Contact</a></li>
</ul></nav>
<div class="breadcrumb">Home &rsaquo; Intranet &rsaquo; {crumb}</div>
"""

BOILERPLATE_HTML_FOOTER = """
<footer><p>© National Digital Services Authority — internal intranet.
This page is generated for SDAIA Academy course SDA-AIE-214 and is fictional.</p>
<p class="links"><a href="/privacy">Privacy</a> · <a href="/terms">Terms</a> ·
<a href="/accessibility">Accessibility</a> · <a href="/sitemap">Sitemap</a></p></footer>
"""
