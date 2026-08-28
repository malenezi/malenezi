#!/usr/bin/env python3
"""Static builder for malenezi.github.io/malenezi.

Assembles the site's pages from one shared shell (head, header, footer) plus
per-page content, so every page stays visually and structurally consistent.
Run from the repository root:  python3 _build/build.py
"""
import json, os, re, html
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://malenezi.github.io/malenezi/"
NAME = "Prof. Mamdouh Alenezi"
EMAIL = "enezi.mamdouh@gmail.com"

PROFILES = [
    ("Google Scholar", "https://scholar.google.com/citations?user=zH5wDBIAAAAJ", "scholar"),
    ("LinkedIn", "https://sa.linkedin.com/in/mamdouhalenezi", "linkedin"),
    ("ORCID", "https://orcid.org/0000-0001-6852-1206", "orcid"),
    ("ResearchGate", "https://www.researchgate.net/profile/Mamdouh_Alenezi", "dot"),
    ("Scopus", "https://www.scopus.com/authid/detail.uri?authorId=55854089000", "dot"),
    ("DBLP", "https://dblp.org/pers/hd/a/Alenezi:Mamdouh", "dot"),
    ("GitHub", "https://github.com/malenezi", "github"),
    ("Medium", "https://medium.com/@malenezi", "dot"),
    ("X", "https://x.com/MamdouhAlenezi", "x"),
]

ICONS = {
 "scholar": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 1 9l4 2.18v6L12 21l7-3.82v-6l2-1.09V17h2V9L12 3z"/></svg>',
 "linkedin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.32 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.79M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"/></svg>',
 "orcid": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zM7.9 7.4a.9.9 0 1 1 0 1.8.9.9 0 0 1 0-1.8zm.75 3h1.5v7h-1.5v-7zm3.35 0h2.9c2.75 0 3.96 1.97 3.96 3.5 0 1.8-1.4 3.5-3.94 3.5h-2.92v-7zm1.5 1.35v4.3h1.36c2.42 0 2.98-1.84 2.98-2.15 0-1.16-.74-2.15-3.03-2.15h-1.31z"/></svg>',
 "github": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2A10 10 0 0 0 8.84 21.5c.5.08.66-.23.66-.5v-1.7C6.73 19.91 6.14 18 6.14 18c-.45-1.15-1.1-1.46-1.1-1.46-.9-.62.07-.6.07-.6 1 .07 1.53 1.03 1.53 1.03.89 1.52 2.34 1.08 2.91.83.09-.65.35-1.09.63-1.34-2.22-.25-4.56-1.11-4.56-4.94 0-1.09.39-1.99 1.03-2.69-.1-.25-.45-1.27.1-2.65 0 0 .84-.27 2.75 1.03a9.5 9.5 0 0 1 5 0c1.91-1.3 2.75-1.03 2.75-1.03.55 1.38.2 2.4.1 2.65.64.7 1.03 1.6 1.03 2.69 0 3.84-2.34 4.68-4.57 4.93.36.31.68.92.68 1.85v2.74c0 .27.16.59.67.5A10 10 0 0 0 12 2z"/></svg>',
 "x": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.53 3H20.5l-6.49 7.42L21.75 21h-5.97l-4.68-6.12L5.74 21H2.77l6.94-7.93L2.25 3h6.12l4.23 5.59L17.53 3zm-1.04 16.2h1.65L7.6 4.72H5.83L16.49 19.2z"/></svg>',
 "dot": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4.24-8 4.76-8-4.76V6l8 4.75L20 6v2.24z"/></svg>',
 "download": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v10.6l3.3-3.3 1.4 1.4L12 17.4l-4.7-4.7 1.4-1.4 3.3 3.3V3h2zM5 19h14v2H5z"/></svg>',
 "arrow": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.2 5.6 11.8 7l4 4H4v2h11.8l-4 4 1.4 1.4L19.6 12z"/></svg>',
}

NAV = [
    ("about.html", "About"),
    ("leadership.html", "Leadership"),
    ("publications.html", "Research"),
    ("projects.html", "Projects"),
    ("speaking.html", "Speaking"),
]

PERSON_LD = {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Mamdouh Alenezi",
    "honorificPrefix": "Prof.",
    "honorificSuffix": "Ph.D.",
    "jobTitle": "General Manager, SDAIA Academy",
    "description": ("Executive leader in national AI and data capability development, technology "
                    "governance and digital transformation; Full Professor of Software Engineering."),
    "url": SITE,
    "image": SITE + "images/newprofile.png",
    "email": "mailto:" + EMAIL,
    "worksFor": {"@type": "Organization", "name": "SDAIA — Saudi Data & Artificial Intelligence Authority"},
    "alumniOf": [
        {"@type": "CollegeOrUniversity", "name": "North Dakota State University"},
        {"@type": "CollegeOrUniversity", "name": "DePaul University"},
        {"@type": "CollegeOrUniversity", "name": "Prince Sultan University"},
    ],
    "address": {"@type": "PostalAddress", "addressLocality": "Riyadh", "addressCountry": "SA"},
    "knowsAbout": ["Software Engineering", "Artificial Intelligence", "AI Governance",
                   "Technology Governance", "Digital Transformation", "Software Security",
                   "Capability Development", "Higher Education"],
    "sameAs": [u for _, u, _ in PROFILES],
}


def profile_links(keys=None, cls="profiles"):
    rows = [p for p in PROFILES if keys is None or p[0] in keys]
    lis = "".join(
        '<li><a href="{u}" rel="noopener me" target="_blank">{i}{n}</a></li>'.format(
            u=u, n=html.escape(n), i=ICONS[k]) for n, u, k in rows)
    return '<ul class="%s">%s</ul>' % (cls, lis)


def shell(slug, title, description, body, base="", extra_head="", extra_ld=None, og_image="images/newprofile.png"):
    canonical = SITE + ("" if slug == "index.html" else slug)
    nav = "".join(
        '<li><a href="{b}{h}"{cur}>{t}</a></li>'.format(
            b=base, h=h, t=t, cur=' aria-current="page"' if h == slug else "")
        for h, t in NAV)
    ld = [PERSON_LD] + (extra_ld or [])
    ld_tags = "\n".join(
        '<script type="application/ld+json">%s</script>' % json.dumps(x, ensure_ascii=False)
        for x in ld)
    foot_nav = "".join('<li><a href="{b}{h}">{t}</a></li>'.format(b=base, h=h, t=t)
                       for h, t in NAV + [("myblog/", "Insights"), ("contact.html", "Contact")])
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Mamdouh Alenezi">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#0f5646">
<link rel="canonical" href="{canonical}">
<link rel="icon" href="{base}images/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="{base}images/newprofile.png">

<meta property="og:type" content="profile">
<meta property="og:site_name" content="Prof. Mamdouh Alenezi">
<meta property="og:locale" content="en">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{site}{ogimg}">
<meta property="og:image:alt" content="Portrait of Prof. Mamdouh Alenezi">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@MamdouhAlenezi">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{site}{ogimg}">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="{base}assets/site.css">
<script>if(!window.matchMedia("(prefers-reduced-motion: reduce)").matches){{document.documentElement.className+=" js";}}</script>
{ld}
{extra_head}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<header class="site-head">
  <div class="site-head__in">
    <a class="brand" href="{base}index.html">Mamdouh <span>Alenezi</span></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="primary-nav" aria-label="Menu">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
    <ul class="nav" id="primary-nav">
      {nav}
      <li><a class="nav-cta" href="{base}contact.html">Contact</a></li>
    </ul>
  </div>
</header>

<main id="main">
{body}
</main>

<footer class="site-foot">
  <div class="site-foot__in">
    <ul class="foot-nav">{foot_nav}</ul>
    {profiles}
    <div class="foot-bottom">
      <p>&copy; {year} Mamdouh Alenezi · Riyadh, Saudi Arabia</p>
      <p><a href="mailto:{email}">{email}</a></p>
    </div>
  </div>
</footer>
<script src="{base}assets/site.js" defer></script>
</body>
</html>
""".format(title=html.escape(title), desc=html.escape(description), canonical=canonical,
           site=SITE, ogimg=og_image, base=base, ld=ld_tags, extra_head=extra_head, body=body,
           nav=nav, foot_nav=foot_nav, profiles=profile_links(),
           year=datetime.now().year, email=EMAIL)


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full) or ".", exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print("wrote %-28s %6d bytes" % (path, len(text.encode("utf-8"))))


def load(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf-8") as fh:
        return json.load(fh)


def bullets(items):
    return '<ul class="bullets">%s</ul>' % "".join("<li>%s</li>" % i for i in items)


def tags(items):
    return '<ul class="tags">%s</ul>' % "".join("<li>%s</li>" % html.escape(i) for i in items)


# ---------------------------------------------------------------- content ---

ROLES = [
    dict(date="Mar 2026 — Present", title="General Manager, SDAIA Academy",
         org="Saudi Data &amp; Artificial Intelligence Authority (SDAIA) · Riyadh",
         points=[
             "Direct Saudi Arabia's national data and AI capability-development arm, owning the strategy, portfolio and delivery of advanced training programmes, bootcamps and professional certifications.",
             "Translate Vision 2030 and Human Capability Development Program priorities into a measurable academy portfolio with defined KPIs and impact metrics.",
             "Structure and manage strategic partnerships with universities, research institutions and industry to co-develop curricula and scale accredited learning pathways.",
             "Govern academy-wide quality assurance, assessment and certification frameworks against international standards.",
         ],
         tags=["National programmes", "Vision 2030", "Certification frameworks", "Partnerships"]),
    dict(date="Aug 2024 — Mar 2026", title="Director, AI Academy &amp; Acting Director, Technology Governance",
         org="Tahakom · Riyadh",
         points=[
             "Held a dual mandate spanning enterprise-wide AI capability building and corporate technology governance for a national smart-mobility and public-safety technology company.",
             "Designed and institutionalised a PMO playbook governing the full project lifecycle; led governance audits, maturity assessments and remediation roadmaps.",
             "Raised enterprise-architecture maturity and clarified the governance operating model, aligning technology investment with corporate strategy.",
             "Overhauled policies, processes and the SDLC with CMMI-aligned quality controls, and modernised delivery with CI/CD-enabled DevOps.",
             "Built a sustained AI capability ecosystem through enterprise training, competency-based certifications, recurring AI townhalls and academia–industry partnerships.",
         ],
         tags=["Enterprise architecture", "PMO", "CMMI", "DevOps", "AI capability"]),
    dict(date="Apr 2024 — Aug 2024", title="Founding Dean, College of Space &amp; Aviation Sciences",
         org="Prince Sultan University · Riyadh",
         points=[
             "Established the college from inception — academic vision, governance structure and founding programme architecture — for one of the Kingdom's first dedicated space and aviation colleges.",
         ],
         tags=["Institution building"]),
    dict(date="Sep 2020 — Aug 2024", title="Dean, Quality Assurance &amp; Development",
         org="Prince Sultan University · Riyadh",
         points=[
             "Led institution-wide quality strategy, securing ISO certifications and national and international academic accreditations.",
             "Implemented a comprehensive Quality Management System and institution-wide assessment and evaluation frameworks.",
             "Elevated teaching practice through the Teaching &amp; Learning Center, expanding faculty development campus-wide.",
         ],
         tags=["ISO certification", "Accreditation", "Quality management"]),
    dict(date="Sep 2018 — Aug 2020", title="Dean, Educational Services",
         org="Prince Sultan University · Riyadh",
         points=[
             "Owned the end-to-end student journey and restructured the Preparatory Year Program into an independent department.",
             "Strengthened academic-support operations — placement testing, semester knowledge evaluations and advising.",
         ],
         tags=["Student experience", "Academic services"]),
    dict(date="Jan 2015 — Aug 2019", title="Chief Information &amp; Technology Officer",
         org="Prince Sultan University · Riyadh",
         points=[
             "Set and executed the university-wide technology vision, aligning IT services with institutional strategy.",
             "Delivered an institution-wide ERP implementation across finance, accounting and HR.",
             "Established a continuous IT planning process serving faculty, staff and students.",
         ],
         tags=["ERP", "IT strategy", "Digital transformation"]),
    dict(date="Sep 2015 — Aug 2016", title="Chairman, Department of Computer Science",
         org="Prince Sultan University · Riyadh",
         points=[
             "Redesigned the curriculum to IEEE, ACM and ABET standards, broadening course and degree offerings.",
             "Built structured employer feedback into programme design to keep the curriculum industry-relevant.",
         ],
         tags=["ABET", "Curriculum"]),
]

CONSULTING = [
    ("Strategic Planning Consultant", "CYBEX, Prince Sultan University", "Nov 2023 — Present",
     "Advise on strategy formulation end to end: methodology selection, multi-stakeholder workshops, and full documentation of vision, mission, goals and initiatives."),
    ("Software Engineering Consultant", "Prince Sultan Defense Studies &amp; Research Center (PSDSARC)", "Feb 2023 — Feb 2024",
     "Provided software-engineering expertise and technology recommendations that improved the efficiency of research and analysis workflows."),
    ("Principal Investigator, Funded Research", "King Abdulaziz City for Science &amp; Technology (KACST)", "Jan 2017 — Dec 2018",
     "Designed a dynamic capacity-provisioning system for cloud networks, applying machine learning to auto-scale resources against demand — improving network efficiency and reducing operational cost."),
    ("Software Engineering Consultant", "Software development company", "Jun 2018 — Oct 2018",
     "Ran a software process improvement initiative: analysed existing development processes and introduced tools and methods that improved delivery speed and quality."),
    ("Data Science Consultant", "Major Saudi telecom operator", "Jan 2016 — Sep 2016",
     "Led root-cause analysis of repeated customer-service tickets and implemented corrective measures, reducing ticket recurrence and lifting customer satisfaction."),
    ("Software Engineering Consultant", "NISC", "Jan 2013 — May 2013",
     "Led the migration of an enterprise billing-management system from client–server architecture to web services, reducing operational cost and improving the customer experience."),
    ("Software Engineering Consultant", "Wisconsin Falconers Association", "Aug 2010 — Feb 2011",
     "Designed and built a web-based reservation system with real-time availability, scheduling and integrated payment processing."),
]

EDUCATION = [
    ("Ph.D., Software Engineering", "North Dakota State University", "Fargo, ND · 2011–2014",
     "Thesis: <em>A New Coupling Metric: Combining Structural and Semantic Relationships.</em>"),
    ("M.S., Software Engineering", "DePaul University", "Chicago, IL · 2010–2011",
     "Requirements engineering, software design and architecture, project management, OO design patterns, testing and QA."),
    ("B.S., Computer Science", "Prince Sultan University", "Riyadh, KSA · 2005–2010",
     "Software engineering, advanced software engineering, internet security and firewalls."),
]

COMPETENCIES = [
    ("Strategic leadership",
     "Digital transformation strategy, national AI and data strategy execution, IT governance, Prosci/ADKAR change management, cross-sector stakeholder alignment."),
    ("Operational excellence",
     "Enterprise architecture, PMO and portfolio governance, programme design and delivery, KPI and performance measurement, budgeting, ISO- and CMMI-based quality management."),
    ("Technology",
     "Software engineering, DevOps and CI/CD, data governance and stewardship, cloud and distributed architecture, cybersecurity, high-performance computing foundations."),
    ("Capability building",
     "Curriculum and learning-programme design aligned to ABET and ACM, professional certification frameworks, talent-pipeline development, training evaluation, academia–industry partnerships."),
    ("Governance, ethics &amp; risk",
     "AI governance frameworks, responsible AI and ethics, privacy and data protection, regulatory compliance, governance audits and risk remediation."),
]

SELECTED_PUBS = [
    ("Healthcare Data Breaches: Insights and Implications", "Healthcare (MDPI)", "2020",
     "https://www.mdpi.com/2227-9032/8/2/133",
     "The most cited paper in my record — an analysis of healthcare breach trends and what they imply for security practice."),
    ("AI-Driven Innovations in Software Engineering: A Review of Current Practices and Future Directions",
     "Applied Sciences", "2025", "https://doi.org/10.3390/app15031344",
     "Where AI is genuinely changing engineering practice, and where the evidence is still thin."),
    ("A Unified Meta Model for Converting Architecture Decisions Into DevOps Pipelines",
     "Software: Practice and Experience (Wiley)", "2026",
     "https://onlinelibrary.wiley.com/doi/10.1002/spe.70077",
     "Closing the gap between architectural intent and what pipelines actually deploy."),
    ("Higher Education Future in the Era of Digital Transformation", "Education Sciences", "2022",
     "https://www.mdpi.com/2227-7102/12/11/784",
     "A roadmap for universities reinventing themselves as digital institutions."),
    ("Reducing Environmental Impact with Sustainable Serverless Computing", "Sustainability", "2025",
     "https://doi.org/10.3390/su17072999",
     "Quantifying how serverless architectures can shrink software's environmental footprint."),
    ("Evolving Microcredential Strategies for Enhancing Employability: Employer and Student Perspectives",
     "Education Sciences", "2024", "https://doi.org/10.3390/educsci14121307",
     "What employers and students actually value in microcredentials — and where the two diverge."),
]

METRICS = [
    ("8,000+", "Citations", "Google Scholar"),
    ("37", "h-index", "Career total"),
    ("98", "i10-index", "Career total"),
    ("140+", "Publications", "Peer-reviewed"),
    ("12+", "Years", "Executive leadership"),
]

COURSES = [
    ("SE 201", "Introduction to Software Engineering"),
    ("SE 211", "Software Construction"),
    ("SE 311", "Software Requirements Engineering"),
    ("SE 322", "Software Design and Architecture"),
    ("SE 353", "Building Secure Software Systems"),
    ("SE 401", "Software Quality Assurance and Testing"),
    ("SE 415", "Group Dynamics &amp; Professional Practice"),
    ("SE 423", "Software Project Management"),
    ("SE 489", "DevOps Engineering"),
    ("SE 492", "Cooperative Education"),
    ("SE 495", "Software Entrepreneurship"),
    ("SE 499", "Software Design &amp; Development Project"),
    ("CS 225", "Software Engineering: Design and Development"),
    ("CYS 402", "Secure Software Development"),
    ("DMS 426", "Game Development"),
]

SUPERVISION = [
    ("Hussain Alshehri", "Internet of Things — architecture of multiple-source data-acquisition sensors"),
    ("Sultan Alotaibi", "An exploratory study of DevOps awareness and adoption in Saudi Arabia"),
    ("Abdulrahman Asiri", "Cloud-based cross-enterprise imaging framework"),
    ("Thamer Alhamed", "Business continuity management and disaster recovery capability in Saudi ICT companies"),
    ("Turki Alshammary", "Software architecture understandability in object-oriented systems"),
    ("Hassan Al-Mousa", "Software architecture stability evolution in open-source object-oriented systems"),
    ("Laila Al-Rowais", "A framework for security testing of web applications"),
    ("Khawlah AlOmar", "Static analysis of open-source web applications"),
]

COMMITTEES = [
    "PSU Higher Strategic Planning Committee", "PSU Strategic Planning Committee",
    "PSU Higher Research Committee", "PSU Executive Research Committee",
    "PSU Institutional Policy Committee", "Institutional Effectiveness Committee",
    "Institutional Executive Quality and Planning Committee", "Institutional Quality Committee",
    "Institutional Technology and Quality Committee", "CCIS ABET Steering Committee",
    "MEGDAM Executive Committee", "CS Department Outreach Committee",
    "CS Department Research Committee", "PSU Strategic Transformation Project",
]

CONF_CHAIR = [
    ("5th International Symposium on Data Mining Applications", "SDMA 2018", "Riyadh, Saudi Arabia"),
    ("6th International Conference on Data Science and Machine Learning Applications", "CDMA 2020", "Riyadh, Saudi Arabia"),
    ("8th International Conference on Data Science and Machine Learning Applications", "CDMA 2024", "Riyadh, Saudi Arabia"),
]

PROGRAM_COMMITTEES = [
    "Workshop on Machine Learning for Predictive Models (MLPM 2014), 13th IEEE International Conference on Machine Learning and Applications (ICMLA 2014)",
    "International Conference on Computing and Informatics (ICOCI 2015)",
    "The Third Information Systems International Conference (ISICO 2015)",
    "The Tenth International Conference on Software Engineering Advances (ICSEA 2015)",
    "International Conference on Computing Education and Information Technology (ICCEIT 2015)",
    "Workshop on Machine Learning for Predictive Models in Engineering Applications (MLPMEA 2015), 14th IEEE ICMLA 2015",
    "The 7th International Conference on Information and Communication Systems (ICICS 2016)",
    "The 4th Symposium on Data Mining Applications (SDMA 2016)",
    "The 4th Saudi International Conference on Information Technology, Big Data Analysis (KACSTIT 2016)",
    "The Eleventh International Conference on Software Engineering Advances (ICSEA 2016)",
    "Special Session on Machine Learning for Predictive Models in Engineering Applications, 18th IEEE ICMLA 2019",
    "19th International Conference on Evaluation of Novel Approaches to Software Engineering (ENASE 2024)",
]

JOURNAL_REVIEWING = [
    "ACM Computing Surveys", "Information and Software Technology",
    "International Journal of Software Engineering and Knowledge Engineering",
    "International Journal of Cloud Applications and Computing (IJCAC)",
    "KSII Transactions on Internet and Information Systems",
    "Journal of Ambient Intelligence and Humanized Computing",
    "Journal of Information Security and Applications", "Applied Artificial Intelligence",
    "Cogent Business &amp; Management", "Education and Information Technologies",
    "Journal of Experimental &amp; Theoretical Artificial Intelligence",
]

TALKS = [
    ("CCIS Low Enrollment: Trends, Challenges and Solutions",
     "A data-led look at declining computing enrolment and what institutions can do about it.",
     "talks/CCIS_Low_Enrollment.pdf"),
    ("Strategies for Effective Proposal Writing",
     "A working session for researchers on building fundable, well-argued proposals.",
     "talks/Strategies%20for%20Effective%20Proposal%20Writing.pdf"),
    ("Data Mining using the R Programming Language",
     "A hands-on introduction to applied data mining for researchers and practitioners.",
     "talks/R.pdf"),
]

SPEAKING_TOPICS = [
    "Building national AI and data capability: from strategy to accredited learning pathways",
    "Technology governance that survives contact with delivery — EA, PMO and CMMI in practice",
    "Responsible AI adoption: governance frameworks, ethics and privacy as operational controls",
    "AI-driven software engineering: what changes for teams, architecture and quality",
    "Digital transformation in higher education and the future of the graduate–employer gap",
]


# ------------------------------------------------------------------ home ---

def metrics_block(note=True):
    cells = "".join(
        '<div class="metric"><b>{v}</b><span>{l}</span><small>{s}</small></div>'.format(v=v, l=l, s=s)
        for v, l, s in METRICS)
    out = '<div class="metrics">%s</div>' % cells
    if note:
        out += ('<p class="pub-count" style="margin-top:.9rem">Bibliometrics from '
                '<a href="https://scholar.google.com/citations?user=zH5wDBIAAAAJ" rel="noopener" target="_blank">Google Scholar</a>; '
                'the publication list below is maintained by hand.</p>')
    return out


def build_index(insights):
    recent = insights[:3]
    posts = "".join(
        '<a class="card" href="{u}" rel="noopener" target="_blank">'
        '<span class="card__num">{d} · {s}</span><h3 dir="auto">{t}</h3>'
        '<span class="card__link">Read {a}</span></a>'.format(
            u=html.escape(p["url"]), d=html.escape(p["date"]), s=html.escape(p["source"]),
            t=html.escape(p["title"]), a=ICONS["arrow"])
        for p in recent)

    pubs = "".join(
        '<li class="pub"><span class="pub__year">{y}</span><div>'
        '<h3 class="pub__title"><a href="{u}" rel="noopener" target="_blank">{t}</a></h3>'
        '<p class="pub__meta"><em>{v}</em></p><p class="pub__meta">{n}</p></div></li>'.format(
            y=y, u=u, t=html.escape(t), v=html.escape(v), n=html.escape(n))
        for t, v, y, u, n in SELECTED_PUBS[:4])

    focus = [
        ("01", "National AI &amp; data capability",
         "I lead the SDAIA Academy: the strategy, portfolio and delivery of advanced training programmes, bootcamps and professional certifications that prepare Saudi talent for data and AI careers — with quality, assessment and certification frameworks held to international standards.",
         "leadership.html", "See the leadership record"),
        ("02", "Technology governance &amp; delivery",
         "Enterprise architecture maturity, PMO playbooks, CMMI-aligned SDLC and CI/CD-enabled DevOps — the unglamorous machinery that decides whether a strategy ever ships. Paired with AI governance, ethics and privacy controls that work in operation, not only on paper.",
         "projects.html", "See projects &amp; impact"),
        ("03", "Research that travels back into practice",
         "More than 140 peer-reviewed publications on software security, AI-driven software engineering and digital transformation in education — an agenda deliberately pointed at problems institutions actually face.",
         "publications.html", "Browse the publications"),
    ]
    focus_cards = "".join(
        '<a class="card reveal" href="{h}"><span class="card__num">{n}</span><h3>{t}</h3><p>{b}</p>'
        '<span class="card__link">{c} {a}</span></a>'.format(n=n, t=t, b=b, h=h, c=c, a=ICONS["arrow"])
        for n, t, b, h, c in focus)

    impact = [
        ("Founded a college from zero", "Prince Sultan University · 2024",
         "Built the College of Space &amp; Aviation Sciences from inception — academic vision, governance structure and founding programme architecture."),
        ("ISO certification and institutional accreditation", "Prince Sultan University · 2020–2024",
         "Led the quality strategy and Quality Management System behind ISO certifications and national and international academic accreditation."),
        ("Three degree programmes and a new track designed", "Prince Sultan University",
         "B.S. in Software Engineering, M.S. in Software Engineering and M.S. in Cybersecurity Engineering, plus a Digital Transformation track and six new courses."),
        ("Delivery modernised at national scale", "Tahakom · 2024–2026",
         "PMO playbook institutionalised, enterprise-architecture maturity raised, SDLC rebuilt with CMMI-aligned controls and CI/CD-enabled DevOps."),
        ("University-wide ERP implementation", "Prince Sultan University · 2015–2019",
         "Delivered enterprise resource planning across finance, accounting and HR as CIO, alongside a continuous IT planning process."),
        ("Three international conferences chaired", "SDMA 2018 · CDMA 2020 · CDMA 2024",
         "Conference chair for three international conferences on data science and machine learning applications, hosted in Riyadh."),
    ]
    impact_rows = "".join(
        '<li><b>{t}</b><span>{m}</span><p>{d}</p></li>'.format(t=t, m=m, d=d)
        for t, m, d in impact)

    body = """
<section class="hero">
  <div class="wrap hero__grid">
    <div>
      <span class="eyebrow">Prof. Mamdouh Alenezi, Ph.D. · Riyadh, Saudi Arabia</span>
      <h1>Turning national AI ambition into <em>capability that lasts</em>.</h1>
      <p class="hero__role">General Manager, SDAIA Academy <span>Full Professor of Software Engineering&nbsp;· Prosci&reg; Certified Change Practitioner</span></p>
      <p class="lede">I lead Saudi Arabia's national data and AI capability development at the SDAIA Academy — the training programmes, certifications and partnerships that turn Vision&nbsp;2030 priorities into a workforce able to deliver them. Behind that sit twelve years of executive leadership in technology governance and digital transformation, three deanships and a CIO role, and a research record of more than 140 peer-reviewed publications.</p>
      <div class="btn-row">
        <a class="btn btn--solid" href="contact.html">Start a conversation</a>
        <a class="btn btn--ghost" href="myCV.pdf">{dl} Download CV</a>
      </div>
      {profiles}
    </div>
    <figure class="portrait">
      <img src="images/newprofile.png" width="512" height="512" alt="Portrait of Prof. Mamdouh Alenezi" fetchpriority="high" decoding="async">
    </figure>
  </div>
</section>

<section class="wrap" aria-label="Key metrics">
  {metrics}
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">What I do</span>
      <h2>Three arenas that rarely meet in one career.</h2>
      <p>Executive leadership of national programmes, hands-on technical governance, and an active research record — each one makes the other two more credible.</p>
    </div>
    <div class="grid grid--3">{focus}</div>
  </div>
</section>

<section class="sec sec--tint">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Selected impact</span>
      <h2>Things that existed afterwards that did not exist before.</h2>
    </div>
    <ul class="rows reveal">{impact}</ul>
    <div class="btn-row" style="margin-top:2rem">
      <a class="btn btn--ghost" href="projects.html">Projects &amp; impact {arrow}</a>
      <a class="btn btn--ghost" href="leadership.html">Full leadership record {arrow}</a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Research</span>
      <h2>Selected publications.</h2>
      <p>113 journal articles, 27 conference papers and three book chapters, cited more than 8,000 times. A few that represent the work:</p>
    </div>
    <ul class="pubs reveal">{pubs}</ul>
    <div class="btn-row" style="margin-top:2rem">
      <a class="btn btn--ghost" href="publications.html">All publications {arrow}</a>
      <a class="btn btn--ghost" href="https://scholar.google.com/citations?user=zH5wDBIAAAAJ" rel="noopener" target="_blank">Google Scholar</a>
    </div>
  </div>
</section>

<section class="sec sec--tint">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Insights</span>
      <h2>Writing, most recently.</h2>
      <p>Short essays on AI strategy, software engineering practice and technology leadership — {count} pieces so far, in English and Arabic.</p>
    </div>
    <div class="grid grid--3 reveal">{posts}</div>
    <div class="btn-row" style="margin-top:2rem"><a class="btn btn--ghost" href="myblog/">All insights {arrow}</a></div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="callout reveal">
      <h2>Let's build something with national impact.</h2>
      <p>I'm open to speaking engagements, advisory and board roles, research collaboration, and strategic partnerships in AI capability building and technology governance.</p>
      <div class="btn-row">
        <a class="btn btn--solid" href="mailto:{email}">{mail} {email}</a>
        <a class="btn btn--ghost" href="contact.html">More ways to reach me</a>
      </div>
    </div>
  </div>
</section>
""".format(profiles=profile_links(["Google Scholar", "LinkedIn", "ORCID", "X"]),
           metrics=metrics_block(note=False), focus=focus_cards, impact=impact_rows,
           pubs=pubs, posts=posts, count=len(insights), arrow=ICONS["arrow"],
           dl=ICONS["download"], mail=ICONS["mail"], email=EMAIL)

    return shell(
        "index.html",
        "Prof. Mamdouh Alenezi — AI Capability, Technology Governance & Software Engineering",
        "Prof. Mamdouh Alenezi, Ph.D. — General Manager of the SDAIA Academy and Full Professor of "
        "Software Engineering. National AI and data capability development, technology governance, "
        "and 140+ peer-reviewed publications with 8,000+ citations.",
        body)


# ----------------------------------------------------------------- about ---

def page_head(title, lede, eyebrow):
    return """
<section class="page-head">
  <div class="wrap">
    <span class="eyebrow">{e}</span>
    <h1>{t}</h1>
    <p>{l}</p>
  </div>
</section>""".format(e=eyebrow, t=title, l=lede)


def build_about():
    comps = "".join(
        '<article class="card reveal"><span class="card__num">{n:02d}</span><h3>{t}</h3><p>{d}</p></article>'.format(
            n=i + 1, t=t, d=d) for i, (t, d) in enumerate(COMPETENCIES))
    edu = "".join(
        '<article class="card reveal"><h3>{d}</h3><p><strong>{s}</strong><br>{p}</p><p>{n}</p></article>'.format(
            d=d, s=s, p=p, n=n) for d, s, p, n in EDUCATION)

    body = page_head(
        "I build the institutions that make strategy real.",
        "Executive leader in national AI and data capability development, technology governance and "
        "digital transformation — and a working software engineering researcher.",
        "About") + """
<section class="sec">
  <div class="wrap hero__grid hero__grid--top">
    <div class="reveal">
      <p class="lede">My career has run along three tracks that usually stay separate: executive leadership of national-scale programmes, hands-on practice in software engineering and AI, and a research record that now exceeds 140 peer-reviewed publications.</p>
      <p>Today I serve as <strong>General Manager of the SDAIA Academy</strong> at the Saudi Data &amp; Artificial Intelligence Authority, where I lead national capability development for data and AI. That means owning the strategy, portfolio and delivery of advanced training programmes, bootcamps and professional certifications; translating Vision&nbsp;2030 and the Human Capability Development Program into a measurable portfolio with real KPIs; and building the partnerships with universities, research institutions and industry that let accredited learning pathways scale.</p>
      <p>Before that, at <strong>Tahakom</strong>, I held a dual mandate as Director of the AI Academy and Acting Director of Technology Governance. I institutionalised a PMO playbook across the project lifecycle, raised enterprise-architecture maturity, rebuilt the SDLC with CMMI-aligned quality controls, and modernised delivery with CI/CD-enabled DevOps — while building a durable AI capability ecosystem through enterprise training, competency-based certifications and academia–industry partnerships.</p>
      <p>Across nearly a decade at <strong>Prince Sultan University</strong> I served as founding dean of a new college, Dean of Quality Assurance &amp; Development, Dean of Educational Services, Chief Information &amp; Technology Officer, and department chairman. The through-line was institutional plumbing: quality systems that earned ISO certification and accreditation, an ERP that replaced paper, curricula rebuilt to ABET and ACM standards, and degree programmes that did not exist before.</p>
      <p>I hold a Ph.D. in Software Engineering from North Dakota State University, an M.S. from DePaul University, and a B.S. in Computer Science from Prince Sultan University — where I am now a Full Professor. I am a Prosci&reg; Certified Change Practitioner and completed the strategy specialisation at Harvard Business School Online.</p>
      <p>What I care about, in one sentence: <strong>responsible, outcome-driven adoption of technology that leaves an institution more capable than it was.</strong></p>
    </div>
    <figure class="portrait reveal">
      <img src="images/newprofile.png" width="512" height="512" alt="Portrait of Prof. Mamdouh Alenezi" loading="lazy" decoding="async">
      <figcaption>Riyadh, Saudi Arabia</figcaption>
    </figure>
  </div>
</section>

<section class="sec sec--tint">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Core competencies</span>
      <h2>Five capabilities, one operating system.</h2>
      <p>Governance makes AI adoption responsible. Engineering rigour makes strategy executable. Capability building makes both sustainable.</p>
    </div>
    <div class="grid grid--3">{comps}</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Education</span>
      <h2>Academic foundations.</h2>
    </div>
    <div class="grid grid--3">{edu}</div>
    <div class="sec-head reveal" style="margin-top:3.2rem">
      <span class="eyebrow">Certifications &amp; executive education</span>
      <h2>Continuing practice.</h2>
    </div>
    <ul class="rows reveal">
      <li><b>Prosci&reg; Certified Change Practitioner</b><span>Prosci · 2025</span><p>Change management, the ADKAR model and organisational transformation.</p></li>
      <li><b>Learning Track: Specialization in Strategy</b><span>Harvard Business School Online · 2024</span><p>Strategy Execution, Sustainable Business Strategy and Disruptive Strategy.</p></li>
      <li><b>Full Professor of Software Engineering</b><span>Prince Sultan University · since 2022</span><p>Associate Professor 2018–2022; Assistant Professor 2014–2018.</p></li>
    </ul>
  </div>
</section>

<section class="sec sec--tint">
  <div class="wrap">
    <div class="callout reveal">
      <h2>Where to go next.</h2>
      <p>The leadership record has the full detail of roles and mandates; projects and impact covers what was built; the publication list is searchable by year, venue and type.</p>
      <div class="btn-row">
        <a class="btn btn--solid" href="leadership.html">Leadership &amp; experience</a>
        <a class="btn btn--ghost" href="publications.html">Research &amp; publications</a>
      </div>
    </div>
  </div>
</section>
""".format(comps=comps, edu=edu)

    return shell("about.html", "About — Prof. Mamdouh Alenezi",
                 "The career, competencies and academic foundations of Prof. Mamdouh Alenezi: "
                 "General Manager of the SDAIA Academy, Full Professor of Software Engineering, "
                 "and Prosci-certified change practitioner.", body)


# ------------------------------------------------------------ leadership ---

def build_leadership():
    tl = "".join(
        '<li class="tl reveal"><span class="tl__date">{d}</span><h3>{t}</h3>'
        '<p class="tl__org">{o}</p>{p}{g}</li>'.format(
            d=r["date"], t=r["title"], o=r["org"], p=bullets(r["points"]), g=tags(r["tags"]))
        for r in ROLES)

    cons = "".join(
        '<li><b>{t}</b><span>{d}</span><p><strong>{o}</strong> — {n}</p></li>'.format(t=t, o=o, d=d, n=n)
        for t, o, d, n in CONSULTING)

    courses = "".join(
        '<li><b>{c}</b><span></span><p>{t}</p></li>'.format(c=c, t=t) for c, t in COURSES)

    sup = "".join('<li><b>{n}</b><span></span><p>{t}</p></li>'.format(n=n, t=t) for n, t in SUPERVISION)

    comm = "".join("<li>%s</li>" % c for c in COMMITTEES)

    body = page_head(
        "From department chair to a national mandate.",
        "Twelve years of progressive executive and academic leadership across national AI capability "
        "building, technology governance and higher-education transformation.",
        "Leadership &amp; experience") + """
<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Executive &amp; academic roles</span>
      <h2>The record.</h2>
    </div>
    <ol class="timeline">{tl}</ol>
  </div>
</section>

<section class="sec sec--tint">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Consulting &amp; funded research</span>
      <h2>Advisory and applied work.</h2>
      <p>Engagements where the brief was to diagnose something concrete and leave a working answer behind.</p>
    </div>
    <ul class="rows reveal">{cons}</ul>
  </div>
</section>

<section class="sec" id="teaching">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Teaching</span>
      <h2>Courses taught, 2014–2024.</h2>
      <p>Fifteen courses across the software engineering, cybersecurity and computer science curricula at Prince Sultan University — several of which I designed from scratch.</p>
    </div>
    <ul class="rows reveal">{courses}</ul>
  </div>
</section>

<section class="sec sec--tint" id="supervision">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Graduate supervision</span>
      <h2>Master's students supervised.</h2>
    </div>
    <ul class="rows reveal">{sup}</ul>
    <div class="sec-head reveal" style="margin-top:3.2rem">
      <span class="eyebrow">Institutional governance</span>
      <h2>Committee service.</h2>
      <p>Fourteen university- and college-level committees spanning strategy, quality, research, policy and accreditation.</p>
    </div>
    <ul class="bullets reveal" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));display:grid">{comm}</ul>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="callout reveal">
      <h2>The detail behind the roles.</h2>
      <p>Projects and impact sets out what was actually built — programmes, systems, governance frameworks and funded research.</p>
      <div class="btn-row">
        <a class="btn btn--solid" href="projects.html">Projects &amp; impact</a>
        <a class="btn btn--ghost" href="myCV.pdf">Download CV</a>
      </div>
    </div>
  </div>
</section>
""".format(tl=tl, cons=cons, courses=courses, sup=sup, comm=comm)

    return shell("leadership.html", "Leadership & Experience — Prof. Mamdouh Alenezi",
                 "Executive and academic roles of Prof. Mamdouh Alenezi: SDAIA Academy, Tahakom, "
                 "and Prince Sultan University — plus consulting, funded research, teaching and "
                 "graduate supervision.", body)


# ---------------------------------------------------------- publications ---

def build_publications(pubs):
    counts = {"journal": 0, "conference": 0, "chapter": 0}
    years = []
    for p in pubs:
        counts[p["kind"]] = counts.get(p["kind"], 0) + 1
        if p.get("year"):
            years.append(p["year"])
    span = "%d–%d" % (min(years), max(years))

    chips = [("all", "All (%d)" % len(pubs)),
             ("journal", "Journal articles (%d)" % counts["journal"]),
             ("conference", "Conference papers (%d)" % counts["conference"]),
             ("chapter", "Book chapters (%d)" % counts["chapter"])]
    chip_html = "".join(
        '<li><button class="chip" type="button" data-kind="{k}" aria-pressed="{p}">{l}</button></li>'.format(
            k=k, l=l, p="true" if k == "all" else "false") for k, l in chips)

    data = json.dumps(pubs, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

    body = page_head(
        "Research &amp; publications.",
        "%d peer-reviewed works published between %s — software security and vulnerability prediction, "
        "AI for software engineering, mining software repositories, empirical software quality, and "
        "software engineering education." % (len(pubs), span),
        "Research") + """
<section class="sec">
  <div class="wrap">
    {metrics}

    <div class="pub-controls reveal" style="margin-top:2.6rem">
      <label class="field">
        <span class="skip">Search publications</span>
        <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
        <input id="pub-search" type="search" placeholder="Search by title, co-author, venue or year&hellip;" autocomplete="off">
      </label>
      <ul class="chips">{chips}</ul>
    </div>
    <p class="pub-count" id="pub-count" role="status"></p>

    <ol class="pubs" id="pub-list"></ol>
    <noscript><p class="empty">The searchable list needs JavaScript. The full record is also available on
      <a href="https://scholar.google.com/citations?user=zH5wDBIAAAAJ" rel="noopener" target="_blank">Google Scholar</a>,
      <a href="https://orcid.org/0000-0001-6852-1206" rel="noopener" target="_blank">ORCID</a> and
      <a href="https://www.scopus.com/authid/detail.uri?authorId=55854089000" rel="noopener" target="_blank">Scopus</a>.</p></noscript>
  </div>
</section>

<section class="sec sec--tint">
  <div class="wrap">
    <div class="callout reveal">
      <h2>Indexed profiles.</h2>
      <p>Citation counts, co-author networks and full-text versions are maintained on the indexing services.</p>
      <div class="btn-row">
        <a class="btn btn--solid" href="https://scholar.google.com/citations?user=zH5wDBIAAAAJ" rel="noopener" target="_blank">Google Scholar</a>
        <a class="btn btn--ghost" href="https://orcid.org/0000-0001-6852-1206" rel="noopener" target="_blank">ORCID</a>
        <a class="btn btn--ghost" href="https://www.scopus.com/authid/detail.uri?authorId=55854089000" rel="noopener" target="_blank">Scopus</a>
        <a class="btn btn--ghost" href="https://dblp.org/pers/hd/a/Alenezi:Mamdouh" rel="noopener" target="_blank">DBLP</a>
      </div>
    </div>
  </div>
</section>

<script type="application/json" id="pub-data">{data}</script>
""".format(metrics=metrics_block(), chips=chip_html, data=data)

    return shell("publications.html", "Research & Publications — Prof. Mamdouh Alenezi",
                 "Searchable list of %d peer-reviewed publications by Prof. Mamdouh Alenezi: journal "
                 "articles, conference papers and book chapters on software security, AI for software "
                 "engineering and engineering education." % len(pubs), body)


# -------------------------------------------------------------- projects ---

def build_projects(insights):
    def rows(items):
        return '<ul class="rows reveal">%s</ul>' % "".join(
            '<li><b>{t}</b><span>{m}</span><p>{d}</p></li>'.format(t=t, m=m, d=d) for t, m, d in items)

    programmes = [
        ("B.S. in Software Engineering", "Prince Sultan University",
         "Full undergraduate curriculum designed and taken through approval, aligned to IEEE, ACM and ABET standards."),
        ("M.S. in Software Engineering", "Prince Sultan University",
         "Graduate programme architecture, course sequence and learning outcomes."),
        ("M.S. in Cybersecurity Engineering", "Prince Sultan University",
         "Graduate programme built to serve national demand for security engineering talent."),
        ("Digital Transformation track", "Prince Sultan University",
         "A new specialisation track connecting software engineering education to institutional transformation practice."),
        ("Six new courses", "SE 411 · SE 311 · SE 415 · SE 489 · SE 495 · CYS 402",
         "Software construction, requirements engineering, group dynamics and professional practice, DevOps engineering, software entrepreneurship, and secure software engineering."),
        ("SDAIA Academy programme portfolio", "SDAIA · 2026–present",
         "Advanced training programmes, bootcamps and professional certifications, with quality assurance, assessment and certification frameworks held to international standards."),
    ]

    systems = [
        ("Quality Management System &amp; accreditation", "Prince Sultan University · 2020–2024",
         "Institution-wide QMS plus assessment and evaluation frameworks; the basis for ISO certifications and national and international academic accreditation."),
        ("Enterprise resource planning", "Prince Sultan University · 2015–2019",
         "ERP implemented across finance, accounting and human resources, with a continuous IT planning process serving faculty, staff and students."),
        ("Preparatory Year Program restructuring", "Prince Sultan University · 2018–2020",
         "Rebuilt the student journey end to end and established the PYP as an independent department."),
        ("College of Space &amp; Aviation Sciences", "Prince Sultan University · 2024",
         "Founded as its first dean: academic vision, governance structure and founding programme architecture."),
        ("Teaching &amp; Learning Center expansion", "Prince Sultan University",
         "Faculty development programmes extended campus-wide to lift teaching practice."),
    ]

    governance = [
        ("PMO playbook", "Tahakom · 2024–2026",
         "A governing playbook for the full project lifecycle, with governance audits, maturity assessments and remediation roadmaps to protect project value."),
        ("Enterprise architecture maturity", "Tahakom",
         "Raised EA maturity and clarified the governance operating model so technology investment tracked corporate strategy."),
        ("CMMI-aligned SDLC", "Tahakom",
         "Policies, processes and the software development lifecycle rebuilt with CMMI-aligned quality controls and measurable maturity gains."),
        ("CI/CD-enabled DevOps", "Tahakom",
         "Toolchain and delivery pipeline modernised, improving delivery speed, traceability and software quality."),
        ("Enterprise AI capability ecosystem", "Tahakom",
         "Enterprise training programmes, competency-based certifications, recurring AI townhalls and academia–industry partnerships embedding ISO-compliant standards into smart-mobility and public-safety solutions."),
    ]

    research_projects = [
        ("Dynamic capacity provisioning for cloud networks", "KACST-funded · 2017–2018",
         "As principal investigator: a scalable architecture that adjusts network resources to changing demand, using machine learning to optimise performance and cut resource waste."),
        ("Customer-service ticket root-cause analysis", "Major Saudi telecom operator · 2016",
         "Led the analysis of ticketing patterns behind a high rate of repeated tickets, then implemented corrective measures that reduced recurrence."),
        ("Billing platform migration", "NISC · 2013",
         "Led the migration of an enterprise billing-management system from client–server architecture to web services."),
        ("Strategy formulation", "CYBEX, Prince Sultan University · 2023–present",
         "Methodology selection, multi-stakeholder workshops and full documentation of vision, mission, goals and initiatives."),
        ("Software process improvement", "Software development company · 2018",
         "Process analysis and new tooling that improved development speed and quality."),
    ]

    body = page_head(
        "What was actually built.",
        "Programmes, institutional systems, governance frameworks and funded research — the work behind "
        "the job titles.",
        "Projects &amp; impact") + """
<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Programmes &amp; curricula</span>
      <h2>Learning that did not exist before.</h2>
      <p>Degree programmes, tracks and courses designed from scratch, plus the national training portfolio I lead today.</p>
    </div>
    {programmes}
  </div>
</section>

<section class="sec sec--tint">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Institutional systems</span>
      <h2>Quality, technology and structure.</h2>
    </div>
    {systems}
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Governance &amp; delivery</span>
      <h2>Making delivery predictable.</h2>
      <p>The operating machinery — architecture, portfolio governance, lifecycle controls and pipelines — that decides whether strategy ships.</p>
    </div>
    {governance}
  </div>
</section>

<section class="sec sec--tint">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Applied &amp; funded research</span>
      <h2>Problems with an owner.</h2>
    </div>
    {research}
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Insights</span>
      <h2>Writing in public.</h2>
      <p>{count} essays on AI strategy, software engineering practice, governance and higher education, published in English and Arabic on Medium and LinkedIn.</p>
    </div>
    <div class="grid grid--3 reveal">{posts}</div>
    <div class="btn-row" style="margin-top:2rem"><a class="btn btn--ghost" href="myblog/">All insights {arrow}</a></div>
  </div>
</section>

<section class="sec sec--tint">
  <div class="wrap">
    <div class="callout reveal">
      <h2>Looking for a partner on something similar?</h2>
      <p>Capability programmes, governance operating models, quality and accreditation systems, or research translation — happy to talk it through.</p>
      <div class="btn-row"><a class="btn btn--solid" href="contact.html">Get in touch</a></div>
    </div>
  </div>
</section>
""".format(programmes=rows(programmes), systems=rows(systems), governance=rows(governance),
           research=rows(research_projects), count=len(insights), arrow=ICONS["arrow"],
           posts="".join(
               '<a class="card" href="{u}" rel="noopener" target="_blank">'
               '<span class="card__num">{d} · {s}</span><h3 dir="auto">{t}</h3>'
               '<span class="card__link">Read {a}</span></a>'.format(
                   u=html.escape(p["url"]), d=html.escape(p["date"]), s=html.escape(p["source"]),
                   t=html.escape(p["title"]), a=ICONS["arrow"]) for p in insights[:3]))

    return shell("projects.html", "Projects & Impact — Prof. Mamdouh Alenezi",
                 "Degree programmes, institutional systems, governance frameworks and funded research "
                 "built by Prof. Mamdouh Alenezi across SDAIA, Tahakom and Prince Sultan University.", body)


# -------------------------------------------------------------- speaking ---

def build_speaking(insights):
    chairs = "".join(
        '<li><b>{t}</b><span>{a}</span><p>Conference chair · {l}</p></li>'.format(t=t, a=a, l=l)
        for t, a, l in CONF_CHAIR)
    talks = "".join(
        '<article class="card reveal"><h3>{t}</h3><p>{d}</p>'
        '<a class="card__link" href="{u}" rel="noopener" target="_blank">Slides (PDF) {a}</a></article>'.format(
            t=t, d=d, u=html.escape(u), a=ICONS["arrow"]) for t, d, u in TALKS)
    pcs = "".join("<li>%s</li>" % p for p in PROGRAM_COMMITTEES)
    revs = "".join("<li>%s</li>" % j for j in JOURNAL_REVIEWING)
    topics = "".join("<li>%s</li>" % t for t in SPEAKING_TOPICS)
    posts = "".join(
        '<li><b dir="auto"><a href="{u}" rel="noopener" target="_blank">{t}</a></b><span>{d} · {s}</span></li>'.format(
            u=html.escape(p["url"]), t=html.escape(p["title"]), d=html.escape(p["date"]),
            s=html.escape(p["source"])) for p in insights[:8])

    body = page_head(
        "Speaking, chairing and writing.",
        "Three international conferences chaired, programme committees for a dozen more, peer review "
        "for eleven indexed journals, and a steady stream of essays on AI and engineering leadership.",
        "Speaking &amp; media") + """
<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Topics</span>
      <h2>What I am usually asked to speak about.</h2>
    </div>
    <ul class="bullets reveal" style="font-size:1.05rem">{topics}</ul>
    <div class="btn-row" style="margin-top:2rem"><a class="btn btn--solid" href="contact.html">Invite me to speak</a></div>
  </div>
</section>

<section class="sec sec--tint">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Conference leadership</span>
      <h2>Chaired conferences.</h2>
      <p>International conferences on data science and machine learning applications, hosted in Riyadh.</p>
    </div>
    <ul class="rows reveal">{chairs}</ul>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Workshops &amp; presentations</span>
      <h2>Sessions and slides.</h2>
    </div>
    <div class="grid grid--3">{talks}</div>
  </div>
</section>

<section class="sec sec--tint">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Peer review &amp; committees</span>
      <h2>Service to the field.</h2>
    </div>
    <div class="grid grid--2">
      <div class="card reveal">
        <h3>Programme committees</h3>
        <p>Twelve international conferences and workshops, including IEEE ICMLA, ICSEA and ENASE.</p>
        <ul class="bullets" style="margin-top:1rem;font-size:.9rem">{pcs}</ul>
      </div>
      <div class="card reveal">
        <h3>Journal reviewing</h3>
        <p>Reviewer for eleven indexed journals.</p>
        <ul class="bullets" style="margin-top:1rem;font-size:.9rem">{revs}</ul>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Writing</span>
      <h2>Recent essays.</h2>
      <p>{count} pieces published on Medium and LinkedIn, in English and Arabic.</p>
    </div>
    <ul class="rows reveal">{posts}</ul>
    <div class="btn-row" style="margin-top:2rem"><a class="btn btn--ghost" href="myblog/">All insights {arrow}</a></div>
  </div>
</section>
""".format(topics=topics, chairs=chairs, talks=talks, pcs=pcs, revs=revs, posts=posts,
           count=len(insights), arrow=ICONS["arrow"])

    return shell("speaking.html", "Speaking & Media — Prof. Mamdouh Alenezi",
                 "Conference chairing, programme committees, journal peer review, workshops and public "
                 "writing by Prof. Mamdouh Alenezi on AI capability, governance and software engineering.",
                 body)


# --------------------------------------------------------------- contact ---

def build_contact():
    open_to = [
        ("Speaking &amp; keynotes", "Conferences, executive briefings and university events on AI capability, governance and software engineering."),
        ("Advisory &amp; board roles", "Technology governance, AI adoption strategy, quality and accreditation systems."),
        ("Research collaboration", "Empirical software engineering, software security, AI for SE, and engineering education."),
        ("Strategic partnerships", "Academia–industry programmes, curriculum co-development and accredited learning pathways."),
    ]
    cards = "".join(
        '<article class="card reveal"><h3>{t}</h3><p>{d}</p></article>'.format(t=t, d=d) for t, d in open_to)

    body = page_head(
        "Let's talk.",
        "Based in Riyadh, Saudi Arabia. Email is the most reliable way to reach me.",
        "Contact") + """
<section class="sec">
  <div class="wrap">
    <div class="grid grid--2">
      <div class="reveal">
        <h2>Get in touch</h2>
        <p class="lede" style="margin-top:1rem">Tell me what you are working on and what you need — a talk, an advisory conversation, a research collaboration or a partnership.</p>
        <div class="btn-row" style="margin-top:1.4rem">
          <a class="btn btn--solid" href="mailto:{email}">{mail} {email}</a>
        </div>
        <div class="btn-row" style="margin-top:.9rem">
          <a class="btn btn--ghost" href="myCV.pdf">{dl} CV (English)</a>
          <a class="btn btn--ghost" href="myCV-Arabic.pdf">{dl} CV (Arabic)</a>
        </div>
        <h3 style="margin-top:2.6rem">Profiles</h3>
        <div style="margin-top:1rem">{profiles}</div>
      </div>
      <div class="grid reveal">{cards}</div>
    </div>
  </div>
</section>
""".format(email=EMAIL, mail=ICONS["mail"], dl=ICONS["download"], profiles=profile_links(), cards=cards)

    return shell("contact.html", "Contact — Prof. Mamdouh Alenezi",
                 "Contact Prof. Mamdouh Alenezi in Riyadh, Saudi Arabia for speaking engagements, "
                 "advisory roles, research collaboration and strategic partnerships.", body)


# -------------------------------------------------------------- insights ---

def build_insights(insights):
    def key(p):
        try:
            return datetime.strptime(p["date"], "%B %d, %Y")
        except Exception:
            return datetime(1900, 1, 1)

    rows = sorted(insights, key=key, reverse=True)
    groups = {}
    for p in rows:
        groups.setdefault(key(p).year, []).append(p)

    sections = ""
    for year in sorted(groups, reverse=True):
        items = "".join(
            '<li><b dir="auto"><a href="{u}" rel="noopener" target="_blank">{t}</a></b>'
            '<span>{d} · {s}</span></li>'.format(
                u=html.escape(p["url"]), t=html.escape(p["title"]),
                d=html.escape(p["date"]), s=html.escape(p["source"])) for p in groups[year])
        sections += ('<div class="sec-head reveal" style="margin-top:2.8rem"><h2>{y}</h2></div>'
                     '<ul class="rows reveal">{i}</ul>').format(y=year, i=items)

    body = page_head(
        "Insights.",
        "Short essays on artificial intelligence, software engineering practice, governance and the "
        "future of technical work — published on Medium and LinkedIn, in English and Arabic.",
        "Writing") + """
<section class="sec">
  <div class="wrap">
    <p class="pub-count">{n} essays, {a}–{b}. Each title links to the published piece.</p>
    {sections}
  </div>
</section>

<section class="sec sec--tint">
  <div class="wrap">
    <div class="callout reveal">
      <h2>Follow the writing.</h2>
      <p>New essays appear first on Medium and LinkedIn.</p>
      <div class="btn-row">
        <a class="btn btn--solid" href="https://medium.com/@malenezi" rel="noopener" target="_blank">Medium</a>
        <a class="btn btn--ghost" href="https://sa.linkedin.com/in/mamdouhalenezi" rel="noopener" target="_blank">LinkedIn</a>
      </div>
    </div>
  </div>
</section>
""".format(n=len(rows), a=min(groups), b=max(groups), sections=sections)

    page = shell("myblog/index.html", "Insights — Prof. Mamdouh Alenezi",
                 "Essays by Prof. Mamdouh Alenezi on AI strategy, software engineering, technology "
                 "governance and higher education.", body, base="../")
    return page.replace('<link rel="canonical" href="%smyblog/index.html">' % SITE,
                        '<link rel="canonical" href="%smyblog/">' % SITE)


# --------------------------------------------------------------- redirect ---

def redirect(target, label):
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Moved — Prof. Mamdouh Alenezi</title>
<link rel="canonical" href="{site}{t}">
<meta name="robots" content="noindex, follow">
<meta http-equiv="refresh" content="0; url={t}">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<main id="main" class="wrap sec">
  <p class="eyebrow">Page moved</p>
  <h1>{l} now lives here.</h1>
  <p class="lede" style="margin-top:1rem">You are being redirected to <a href="{t}">{t}</a>.</p>
  <p class="btn-row" style="margin-top:1.5rem"><a class="btn btn--solid" href="{t}">Continue</a>
  <a class="btn btn--ghost" href="index.html">Home</a></p>
</main>
<script>location.replace("{t}");</script>
</body>
</html>
""".format(site=SITE, t=target, l=label)


def build_404():
    body = """
<section class="sec">
  <div class="wrap" style="max-width:44rem">
    <span class="eyebrow">404</span>
    <h1>That page has moved on.</h1>
    <p class="lede" style="margin-top:1rem">The link you followed does not exist on this site any more. These are the places worth trying:</p>
    <div class="btn-row" style="margin-top:1.6rem">
      <a class="btn btn--solid" href="/malenezi/">Home</a>
      <a class="btn btn--ghost" href="/malenezi/publications.html">Publications</a>
      <a class="btn btn--ghost" href="/malenezi/leadership.html">Leadership</a>
      <a class="btn btn--ghost" href="/malenezi/contact.html">Contact</a>
    </div>
  </div>
</section>
"""
    page = shell("404.html", "Page not found — Prof. Mamdouh Alenezi",
                 "The page you were looking for is not on this site.", body,
                 base="/malenezi/")
    return page.replace('<meta name="robots" content="index, follow, max-image-preview:large">',
                        '<meta name="robots" content="noindex, follow">')


def main():
    pubs = load("publications.json")
    insights = load("insights.json")
    write("index.html", build_index(insights))
    write("about.html", build_about())
    write("leadership.html", build_leadership())
    write("publications.html", build_publications(pubs))
    write("projects.html", build_projects(insights))
    write("speaking.html", build_speaking(insights))
    write("contact.html", build_contact())
    write("myblog/index.html", build_insights(insights))
    write("404.html", build_404())
    write("Research.html", redirect("publications.html", "Research"))
    write("Teaching.html", redirect("leadership.html#teaching", "Teaching"))
    write("Services.html", redirect("speaking.html", "Service and speaking"))
    write("Links.html", redirect("index.html", "Links"))

    pages = ["", "about.html", "leadership.html", "publications.html", "projects.html",
             "speaking.html", "contact.html", "myblog/"]
    today = datetime.now().strftime("%Y-%m-%d")
    urls = "".join(
        "  <url>\n    <loc>{s}{p}</loc>\n    <lastmod>{d}</lastmod>\n"
        "    <changefreq>{f}</changefreq>\n    <priority>{r}</priority>\n  </url>\n".format(
            s=SITE, p=p, d=today, f="weekly" if p in ("", "myblog/") else "monthly",
            r="1.0" if p == "" else "0.8")
        for p in pages)
    write("sitemap.xml",
          '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")
    write("robots.txt", "User-agent: *\nAllow: /\n\nSitemap: %ssitemap.xml\n" % SITE)


if __name__ == "__main__":
    main()
