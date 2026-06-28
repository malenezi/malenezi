/* ============================================================
   أكاديمية سدايا · دورة حياة البرامج (النسخة الثالثة)
   شاشة مقدمة للمراحل · بطاقات قابلة للقلب · مسارات مكدّسة
   ============================================================ */
(function () {
  "use strict";
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Lucide icons ---------- */
  const LUCIDE = {
    "activity": '<path d="M22 12h-2.48a2 2 0 0 0-1.93 1.46l-2.35 8.36a.25.25 0 0 1-.48 0L9.24 2.18a.25.25 0 0 0-.48 0l-2.35 8.36A2 2 0 0 1 4.49 12H2"/>',
    "badge-check": '<path d="M3.85 8.62a4 4 0 0 1 4.78-4.77 4 4 0 0 1 6.74 0 4 4 0 0 1 4.78 4.78 4 4 0 0 1 0 6.74 4 4 0 0 1-4.77 4.78 4 4 0 0 1-6.75 0 4 4 0 0 1-4.78-4.77 4 4 0 0 1 0-6.76Z"/><path d="m9 12 2 2 4-4"/>',
    "bar-chart-3": '<path d="M3 3v18h18"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/>',
    "target": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    "list-checks": '<path d="m3 17 2 2 4-4"/><path d="m3 7 2 2 4-4"/><path d="M13 6h8"/><path d="M13 12h8"/><path d="M13 18h8"/>',
    "file-check": '<path d="M4 22h14a2 2 0 0 0 2-2V7l-5-5H6a2 2 0 0 0-2 2v4"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="m3 15 2 2 4-4"/>',
    "monitor-play": '<path d="M10 7.75a.75.75 0 0 1 1.142-.638l3.664 2.249a.75.75 0 0 1 0 1.278l-3.664 2.25a.75.75 0 0 1-1.142-.64z"/><path d="M12 17v4"/><path d="M8 21h8"/><rect x="2" y="3" width="20" height="14" rx="2"/>',
    "package-check": '<path d="m16 16 2 2 4-4"/><path d="M21 10V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l2-1.14"/><path d="M3.3 7 12 12l8.7-5"/><path d="M12 22V12"/>',
    "rocket": '<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/>',
    "book-open": '<path d="M12 7v14"/><path d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3Z"/>',
    "chevron-left": '<path d="m15 18-6-6 6-6"/>',
    "chevron-right": '<path d="m9 18 6-6-6-6"/>',
    "chevron-down": '<path d="m6 9 6 6 6-6"/>',
    "clipboard-check": '<rect width="8" height="4" x="8" y="2" rx="1" ry="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="m9 14 2 2 4-4"/>',
    "cpu": '<rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 2v2"/><path d="M9 20v2"/>',
    "database": '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14c0 1.66 4.03 3 9 3s9-1.34 9-3V5"/><path d="M3 12c0 1.66 4.03 3 9 3s9-1.34 9-3"/>',
    "graduation-cap": '<path d="M21.42 10.92a1 1 0 0 0-.02-1.84l-8.57-3.9a2 2 0 0 0-1.66 0l-8.57 3.9a1 1 0 0 0 0 1.84l8.57 3.9a2 2 0 0 0 1.66 0Z"/><path d="M22 10v6"/><path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5"/>',
    "inbox": '<polyline points="22 12 16 12 14 15 10 15 8 12 2 12"/><path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11Z"/>',
    "layers": '<path d="M12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.91a1 1 0 0 0 0-1.83Z"/><path d="m22 12.5-9.17 4.17a2 2 0 0 1-1.66 0L2 12.5"/><path d="m22 17.5-9.17 4.17a2 2 0 0 1-1.66 0L2 17.5"/>',
    "package": '<path d="m7.5 4.27 9 5.15"/><path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><path d="m3.3 7 8.7 5 8.7-5"/><path d="M12 22V12"/>',
    "pencil-ruler": '<path d="m15 5 4 4"/><path d="M13 7 8 2 2 8l5 5"/><path d="m14 6 6 6"/><path d="m4 16 4 4"/><path d="m17 11 5 5-6 6-5-5Z"/>',
    "radar": '<path d="M19.07 4.93A10 10 0 0 0 6.99 3.34"/><path d="M4 6h.01"/><path d="M2.29 9.62A10 10 0 1 0 21.31 8.35"/><path d="M16.24 7.76A6 6 0 1 1 8.23 7.75"/><path d="M12 18h.01"/><path d="M17.99 11.66A6 6 0 0 0 15.77 8.23"/><path d="M12 12h.01"/>',
    "refresh-cw": '<path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"/><path d="M8 16H3v5"/>',
    "route": '<circle cx="6" cy="19" r="3"/><path d="M9 19h8.5a3.5 3.5 0 0 0 0-7h-11a3.5 3.5 0 0 1 0-7H15"/><circle cx="18" cy="5" r="3"/>',
    "search-check": '<path d="m8 11 2 2 4-4"/><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    "settings": '<path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2Z"/><circle cx="12" cy="12" r="3"/>',
    "sparkles": '<path d="M9.94 15.5A2 2 0 0 0 8.5 14.06l-6.14-1.58a.5.5 0 0 1 0-.96L8.5 9.94A2 2 0 0 0 9.94 8.5l1.58-6.14a.5.5 0 0 1 .96 0l1.58 6.14a2 2 0 0 0 1.44 1.44l6.14 1.58a.5.5 0 0 1 0 .96l-6.14 1.58a2 2 0 0 0-1.44 1.44l-1.58 6.14a.5.5 0 0 1-.96 0Z"/><path d="M20 3v4"/><path d="M22 5h-4"/><path d="M4 17v2"/><path d="M5 18H3"/>',
    "trending-up": '<polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/>',
    "workflow": '<rect width="8" height="8" x="3" y="3" rx="2"/><path d="M7 11v4a2 2 0 0 0 2 2h4"/><rect width="8" height="8" x="13" y="13" rx="2"/>',
    "megaphone": '<path d="m3 11 18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/>',
    "briefcase": '<path d="M16 20V4a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/><rect width="20" height="14" x="2" y="6" rx="2"/>',
    "award": '<path d="m15.477 12.89 1.515 8.526a.5.5 0 0 1-.81.47l-3.58-2.687a1 1 0 0 0-1.197 0l-3.586 2.686a.5.5 0 0 1-.81-.469l1.514-8.526"/><circle cx="12" cy="8" r="6"/>',
    "blocks": '<rect width="7" height="7" x="14" y="3" rx="1"/><path d="M10 21V8a1 1 0 0 0-1-1H4a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-5a1 1 0 0 0-1-1H3"/>',
    "square-play": '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="m10 8 6 4-6 4Z"/>',
    "calendar-check": '<path d="M8 2v4"/><path d="M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/><path d="m9 16 2 2 4-4"/>',
    "x": '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>'
  };
  const P = {
    cycle:"refresh-cw", route:"route", grid:"layers",
    s1:"radar", s2:"search-check", s3:"pencil-ruler", s4:"square-play", s5:"clipboard-check", s6:"trending-up", s7:"refresh-cw",
    cap:"graduation-cap", cpu:"cpu", db:"database", book:"book-open", layers:"layers",
    gear:"settings", spark:"sparkles", bars:"bar-chart-3", flow:"workflow", badge:"badge-check",
    inbox:"inbox", act:"activity", box:"package", pkgok:"package-check",
    play:"monitor-play", rocket:"rocket",
    pencil:"pencil-ruler", target:"target", checks:"list-checks", filechk:"file-check",
    mega:"megaphone", brief:"briefcase",
    award:"award", blocks:"blocks", calc:"calendar-check",
    next:"chevron-left", prev:"chevron-right", down:"chevron-down"
  };
  const svg = (name, cls) => '<svg class="' + (cls || "ic") + '" viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' + (LUCIDE[name] || "") + '</svg>';
  const renderStaticIcons = (root) => {
    (root || document).querySelectorAll("[data-icon]").forEach(el => { el.innerHTML = svg(el.dataset.icon); });
  };

  /* ====== بيانات المراحل السبع ====== */
  const STEPS = [
    {
      ic:P.s1, ar:"رصد الاحتياج", en:"Need Sensing", color:"primary",
      desc:"ننطلق من إشارات الطلب الحقيقية الواردة من سدايا وأذرعها لتحديد الاحتياج التدريبي.",
      type:"proc",
      proc:{
        in:["الاحتياجات الحكومية والوطنية ذات الأولوية","احتياجات أذرع سدايا وأجهزتها","تقارير ودراسات مكتب الاستراتيجية","تقارير السوق والشركاء والاتجاهات العالمية"],
        act:["تحليل التوجهات العالمية والتقنيات الناشئة","ورش عمل ومقابلات منظمة مع الجهات","تحليل الوظائف والمهارات وفق الإطار الوطني (الجدارات والمهارات)","دراسة احتياجات السوق المستقبلية"],
        out:["وثيقة الاحتياج التدريبي المعتمدة","قائمة الوظائف والفئات المستهدفة","خريطة المهارات المطلوبة"]
      }
    },
    {
      ic:P.s2, ar:"دراسة الفجوة", en:"Gap Analysis", color:"primary",
      desc:"نحوّل الفجوة بين الواقع والمستهدف إلى تقرير ومصفوفة مهارات مرتّبة بالأولوية.",
      type:"proc",
      proc:{
        in:["مخرجات المرحلة الأولى (الاحتياج المعتمد)","خرائط المهارات الحالية للفئات المستهدفة","مرجعيات الإطار الوطني للمؤهلات"],
        act:["قياس الفجوة بين المهارات الحالية والمستهدفة","تحديد مستوى النضج الرقمي للفئة","جلسات عمل تشاركية مع الجهات المستفيدة","ترتيب الأولويات وفق معياري الأثر × الإلحاح"],
        out:["تقرير دراسة الفجوة الشامل","مصفوفة المهارات المستهدفة","قائمة الأولويات التدريبية المعتمدة"]
      }
    },
    {
      ic:P.s3, ar:"التصميم والتطوير", en:"Design & Develop", color:"teal",
      desc:"عملية ثلاثية: تصميم بالبيانات، تطوير بالذكاء الاصطناعي، وتهيئة للتطبيق حتى حقيبة جاهزة.",
      type:"tri",
      tri:[
        { ic:P.pencil, t:"التصميم", items:["أهداف تعلم وفق Bloom's Taxonomy","مسارات تدريبية مخصصة (Personalized Paths)","أساليب تعلم مبنية على البيانات","مواءمة مع الأطر المرجعية","أدوات تقييم واختبارات ذكية"] },
        { ic:P.spark, t:"التطوير", items:["إنتاج محتوى بالذكاء الاصطناعي (نص، عرض، فيديو)","محتوى تفاعلي ومحاكاة تعليمية","بنوك أسئلة متعددة المستويات","تدقيق آلي وبشري للجودة","حقائب تدريبية وفق المعايير الدولية"] },
        { ic:P.gear, t:"التهيئة للتطبيق", items:["تهيئة بيئات التعلم","اختيار أساليب التقديم (حضوري، عن بُعد، مدمج)","إعداد أدلة المدربين والمتدربين","تجهيز فرق الدعم الفني والأكاديمي"] }
      ],
      out:{ t:"حقيبة تدريبية متكاملة جاهزة للإطلاق التشغيلي", items:["دليل المدرب","مادة المتدرب","بنك التقييمات","المعامل التطبيقية","العرض التفاعلي","معايير الاعتماد"] }
    },
    {
      ic:P.s4, ar:"التقديم والتنفيذ", en:"Delivery", color:"branch",
      desc:"استقطاب المتدربين ثم التنفيذ التدريبي بجودة معتمدة عبر مسارين متوازيين.",
      type:"paths",
      paths:[
        { ic:P.mega, t:"مسار استقطاب المتدربين", steps:[
          { t:"الإعلان والتسويق", d:"عبر القنوات المعتمدة" },
          { t:"التسجيل", d:"عبر منصة أذكى X" },
          { t:"الفرز", d:"وفق المعايير المعتمدة" },
          { t:"اختيار المرشحين", d:"النهائيين للالتحاق" }
        ] },
        { ic:P.play, t:"مسار التنفيذ التدريبي", steps:[
          { t:"التنفيذ المباشر عبر مدربي سدايا", d:"اختبار واعتماد المدربين الداخليين" },
          { t:"التنفيذ عبر شركاء معتمدين", d:"اعتماد الشركاء والمواقع والمدربين الخارجيين" }
        ] }
      ]
    },
    {
      ic:P.s5, ar:"التقييم", en:"Evaluation", color:"primary",
      desc:"تقارير تقييم مباشرة تقيس الرضا والمعرفة وجودة التنفيذ وتُغذّي قياس الأثر والتحسين.",
      type:"proc",
      proc:{
        in:["بيانات التشغيل من المرحلة الرابعة","الاختبارات القبلية والبعدية","ملاحظات المدربين الفورية","بيانات سلوك المتدرب على المنصة"],
        act:["قياس رضا المتدربين عبر مؤشر NPS","قياس اكتساب المعرفة عبر الاختبارات القبلية والبعدية","تقييم جودة المدربين والمحتوى التدريبي","جمع التغذية الراجعة الفورية وتحليلها للتحسين المستمر"],
        out:["تقارير التقييم المباشر","إصدار الشهادات المهنية والتدريبية","تهيئة للشارة أو التوظيف","تغذية مرحلتي قياس الأثر والتحسين"]
      }
    },
    {
      ic:P.s6, ar:"قياس الأثر", en:"Impact", color:"teal",
      desc:"تقرير أثر شامل يقيس تطبيق المهارات والعائد المهني مع توصيات تطوير استراتيجية.",
      type:"proc",
      proc:{
        in:["تقارير التقييم الفوري","بيانات جهات عمل المتدربين","بيانات السوق والتوظيف","بيانات الأداء بعد التدريب"],
        act:["قياس تطبيق المهارات في بيئة العمل","استبيانات الأثر بعد 3 و6 و12 شهراً","مقابلات منظمة مع جهات العمل","تحليل المسار المهني للخريجين"],
        out:["تقرير الأثر الشامل","توصيات التطوير الاستراتيجية","قصص النجاح والحالات المرجعية"]
      }
    },
    {
      ic:P.s7, ar:"التحسين المستمر", en:"Continuous Imp.", color:"teal",
      desc:"إصدارات محسّنة وخارطة سنوية معتمدة تُغذّي المرحلة الأولى في دورة جديدة.",
      type:"proc",
      proc:{
        in:["مخرجات مرحلتي التقييم وقياس الأثر","اتجاهات السوق والتقنيات المستجدة","بيانات أداء المنصات الرقمية","ملاحظات الشركاء والمدربين"],
        act:["تطوير المحتوى وفق التغذية الراجعة","تحسين أساليب التدريب والتنفيذ","تحديث البرامج وفق المستجدات","مراجعة الأهداف والمسارات التدريبية"],
        out:["إصدارات محسّنة من البرامج","تغذية المرحلة الأولى لدورة جديدة","خارطة تطوير سنوية معتمدة"]
      }
    }
  ];

  const TRACKS = [
    { cls:"t1", ic:P.cpu, ar:"مسار تدريب مهندس الذكاء الاصطناعي", en:"AI Engineer Track",
      meta:["المدة: 12–16 أسبوعاً", "المستوى: متقدم", "5 وحدات تدريبية"],
      mods:[
        { ic:P.book,  t:"الأساسيات", d:"بايثون والرياضيات للذكاء الاصطناعي", u:4 },
        { ic:P.s2,    t:"تعلّم الآلة", d:"الخوارزميات الإشرافية وتقييمها", u:5 },
        { ic:P.layers,t:"التعلم العميق", d:"الشبكات العصبية والرؤية واللغة", u:5 },
        { ic:P.gear,  t:"التشغيل MLOps", d:"أتمتة ونشر النماذج في الإنتاج", u:4 },
        { ic:P.spark, t:"الذكاء التوليدي", d:"النماذج اللغوية وبناء الوكلاء", u:4 }
      ] },
    { cls:"t2", ic:P.db, ar:"مسار تدريب عالم البيانات", en:"Data Scientist Track",
      meta:["المدة: 12–16 أسبوعاً", "المستوى: متوسط–متقدم", "5 وحدات تدريبية"],
      mods:[
        { ic:P.db,   t:"أساسيات البيانات", d:"الجمع والتنظيف والتهيئة", u:4 },
        { ic:P.bars, t:"الإحصاء والتحليل", d:"التحليل الاستكشافي والاستدلالي", u:5 },
        { ic:P.cpu,  t:"التعلم الآلي", d:"النمذجة التنبؤية والتقييم", u:5 },
        { ic:P.flow, t:"هندسة البيانات", d:"خطوط البيانات والمستودعات", u:4 },
        { ic:P.s6,   t:"التصور ودعم القرار", d:"لوحات المعلومات ورواية البيانات", u:4 }
      ] }
  ];

  /* ====== إدارة الشاشات والنافذة ====== */
  function showScreen(id) {
    document.querySelectorAll(".screen").forEach(s => s.classList.remove("active", "anim"));
    const el = document.getElementById(id); el.classList.add("active");
    void el.offsetWidth; el.classList.add("anim");
    document.getElementById("backBtn").classList.toggle("show", id !== "home");
    window.scrollTo({ top: 0, behavior: "smooth" });
    if (id === "tracks") revealTracks();
  }
  function openOverlay() {
    const ov = document.getElementById("lcOverlay");
    ov.classList.add("open");
    document.body.classList.add("overlay-active");
    document.body.style.overflow = "hidden";
    showOverview();
  }
  function closeOverlay() {
    document.getElementById("lcOverlay").classList.remove("open");
    document.body.classList.remove("overlay-active");
    document.body.style.overflow = "";
  }

  function showOverview() {
    document.getElementById("lcOverview").classList.add("show");
    document.getElementById("lcDetail").classList.remove("show");
    document.getElementById("ovToOverview").classList.remove("show");
    const grid = document.querySelector("#lcOverview .lco-grid");
    grid.classList.remove("in"); void grid.offsetWidth; grid.classList.add("in");
  }
  function enterDetail(i) {
    document.getElementById("lcOverview").classList.remove("show");
    document.getElementById("lcDetail").classList.add("show");
    document.getElementById("ovToOverview").classList.add("show");
    setStep(i);
  }
  function buildOverview() {
    const grid = document.querySelector("#lcOverview .lco-grid");
    STEPS.forEach((s, i) => {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "lco-card c-" + s.color + (i === 0 ? " first" : "");
      b.innerHTML = '<span class="lco-card__num">' + (i + 1) + '</span>' +
        '<span class="lco-card__ic">' + svg(s.ic) + '</span>' +
        '<h4>' + s.ar + '</h4>' +
        '<span class="lco-card__en">' + s.en + '</span>';
      b.addEventListener("click", () => enterDetail(i));
      grid.appendChild(b);
    });
  }

  /* ====== عرض تفاصيل المرحلة ====== */
  let cur = 0, railEls = [];
  function buildRail() {
    const rail = document.getElementById("rail");
    STEPS.forEach((s, i) => {
      const b = document.createElement("button");
      b.type = "button"; b.className = "rstep c-" + s.color;
      b.innerHTML = '<span class="rstep__b">' + svg(s.ic) + '<span class="rstep__n">' + (i + 1) + '</span></span>' +
        '<span class="rstep__t">' + s.ar + '</span>';
      b.addEventListener("click", () => setStep(i));
      rail.appendChild(b); railEls.push(b);
    });
  }
  function nodeHTML(s, i) {
    return '<span class="node__ic">' + svg(s.ic) + '</span>' +
      '<div class="k">المرحلة ' + (i + 1) + ' من 7</div>' +
      '<h3>' + s.ar + '<span class="en">' + s.en + '</span></h3>' +
      '<p>' + s.desc + '</p>';
  }

  function procHTML(s) {
    const cards = [
      { ic:P.inbox, label:"المدخلات", sub:"مصادر الإدخال", items:s.proc.in, cls:"pc-in" },
      { ic:P.act,   label:"الأنشطة",  sub:"ما نقوم به",    items:s.proc.act, cls:"pc-act" },
      { ic:P.box,   label:"المخرجات", sub:"النتائج المعتمدة", items:s.proc.out, cls:"pc-out" }
    ];
    const el = c =>
      '<div class="flip ' + c.cls + '" tabindex="0" role="button" aria-label="' + c.label + '">' +
        '<div class="flip__in">' +
          '<div class="flip__face flip__front">' +
            '<span class="flip__ic">' + svg(c.ic) + '</span>' +
            '<h4>' + c.label + '</h4>' +
            '<span class="flip__sub">' + c.sub + '</span>' +
            '<span class="flip__count">' + c.items.length + ' عناصر</span>' +
            '<span class="flip__hint">' + svg(P.cycle) + ' مرّر للتفاصيل</span>' +
          '</div>' +
          '<div class="flip__face flip__back">' +
            '<div class="flip__bh">' + svg(c.ic) + ' ' + c.label + '</div>' +
            '<ul>' + c.items.map(it => '<li>' + it + '</li>').join("") + '</ul>' +
          '</div>' +
        '</div>' +
      '</div>';
    const arrow = '<span class="flow__arrow">' + svg(P.next) + '</span>';
    return '<div class="flow anim">' + cards.map(el).join(arrow) + '</div>';
  }

  function triHTML(s) {
    const arrow = '<span class="flow__arrow">' + svg(P.next) + '</span>';
    const cols = s.tri.map(c =>
      '<div class="tcol">' +
        '<div class="tcol__h"><span class="tcol__ic">' + svg(c.ic) + '</span><b>' + c.t + '</b></div>' +
        '<ul>' + c.items.map(it => '<li>' + it + '</li>').join("") + '</ul>' +
      '</div>').join(arrow);
    return '<div class="tri anim">' +
      '<div class="tri__row">' + cols + '</div>' +
      '<span class="tri__down">' + svg(P.down) + '</span>' +
      '<div class="tri-out">' +
        '<div class="tri-out__top">' +
          '<span class="tri-out__ic">' + svg(P.pkgok) + '</span>' +
          '<div><b>' + s.out.t + '</b><span class="ready">' + svg(P.rocket) + ' جاهزة للإطلاق التشغيلي</span></div>' +
        '</div>' +
        '<div class="tri-out__grid">' + s.out.items.map(i => '<span class="pkgi">' + svg(P.badge) + ' ' + i + '</span>').join("") + '</div>' +
      '</div>' +
    '</div>';
  }

  function pathsHTML(s) {
    return '<div class="paths anim">' + s.paths.map(p =>
      '<div class="pcard">' +
        '<div class="pcard__h"><span class="pcard__ic">' + svg(p.ic) + '</span><b>' + p.t + '</b></div>' +
        '<div class="pcard__flow">' +
          p.steps.map((st, k) =>
            '<div class="pstep">' +
              '<span class="pstep__n">' + (k + 1) + '</span>' +
              '<div class="pstep__b"><b>' + st.t + '</b><span>' + st.d + '</span></div>' +
            '</div>' +
            (k < p.steps.length - 1 ? '<span class="pstep__arrow">' + svg(P.down) + '</span>' : "")
          ).join("") +
        '</div>' +
      '</div>').join("") + '</div>';
  }

  function contentHTML(s) {
    if (s.type === "proc") return procHTML(s);
    if (s.type === "tri")  return triHTML(s);
    if (s.type === "paths") return pathsHTML(s);
    return "";
  }

  function setStep(i) {
    cur = i;
    railEls.forEach((el, k) => { el.classList.toggle("active", k === i); el.classList.toggle("done", k < i); });
    const s = STEPS[i];
    const stage = document.getElementById("lcStage");
    stage.setAttribute("data-color", s.color);
    stage.setAttribute("data-type", s.type);
    const node = document.getElementById("node");
    node.classList.remove("anim"); void node.offsetWidth; node.classList.add("anim");
    node.innerHTML = nodeHTML(s, i);
    document.getElementById("stageContent").innerHTML = contentHTML(s);
    document.getElementById("count").textContent = "المرحلة " + (i + 1) + " / 7";
    document.getElementById("ovCount").textContent = "المرحلة " + (i + 1) + " / 7";
    const prev = document.getElementById("prevBtn");
    prev.disabled = false;
    prev.innerHTML = (i === 0 ? svg(P.prev) + " كل المراحل" : svg(P.prev) + " السابق");
    const next = document.getElementById("nextBtn");
    next.innerHTML = (i === STEPS.length - 1) ? "مسارات التدريب " + svg(P.route) : "التالي " + svg(P.next);
  }

  /* ====== مسارات التدريب (وحدات مكدّسة) ====== */
  function buildTracks() {
    const wrap = document.getElementById("trackList");
    TRACKS.forEach(t => {
      const d = document.createElement("div"); d.className = "track " + t.cls;
      const mods = t.mods.map((m, k) =>
        '<div class="mod">' +
          '<span class="mod__n">' + (k + 1) + '</span>' +
          '<span class="mod__b">' + svg(m.ic) + '</span>' +
          '<div class="mod__t">' + m.t + '</div>' +
          '<div class="mod__d">' + m.d + '</div>' +
          '<span class="mod__u">' + svg(P.blocks) + ' ' + m.u + ' وحدات</span>' +
        '</div>').join('<span class="mod__plus">+</span>');
      d.innerHTML =
        '<div class="track__head">' +
          '<span class="track__ic">' + svg(t.ic) + '</span>' +
          '<div><h3>' + t.ar + '</h3><span class="en">' + t.en + '</span></div>' +
          '<div class="track__meta">' + t.meta.map(m => '<span class="m">' + m + '</span>').join("") + '</div>' +
        '</div>' +
        '<div class="stack">' +
          '<div class="stack__mods">' + mods + '</div>' +
          '<span class="stack__eq">' + svg(P.next) + '</span>' +
          '<div class="outcome">' +
            '<span class="outcome__lbl">' + svg(P.award) + ' المخرج النهائي</span>' +
            '<div class="outcome__row">' +
              '<span class="ob badge"><span class="ob__ic">' + svg(P.award) + '</span><b>شارة المحترف</b><span>اعتماد مهني معتمد</span></span>' +
              '<span class="ob__or">أو</span>' +
              '<span class="ob job"><span class="ob__ic">' + svg(P.brief) + '</span><b>فرصة توظيف</b><span>ربط مباشر بسوق العمل</span></span>' +
            '</div>' +
          '</div>' +
        '</div>';
      wrap.appendChild(d);
    });
  }
  function revealTracks() {
    const els = document.querySelectorAll("#tracks .track");
    if (reduce) { els.forEach(e => e.classList.add("in")); return; }
    els.forEach((e, i) => setTimeout(() => e.classList.add("in"), 120 + i * 160));
  }

  /* ====== التشغيل ====== */
  function boot() {
    renderStaticIcons();
    document.getElementById("lcIcon").innerHTML = svg(P.cycle);
    document.getElementById("trIcon").innerHTML = svg(P.route);
    buildOverview(); buildRail(); buildTracks();

    document.getElementById("goLifecycle").addEventListener("click", openOverlay);
    document.getElementById("goTracks").addEventListener("click", () => showScreen("tracks"));
    document.getElementById("backBtn").addEventListener("click", () => showScreen("home"));
    document.getElementById("ovClose").addEventListener("click", closeOverlay);
    document.getElementById("ovToOverview").addEventListener("click", showOverview);

    document.getElementById("prevBtn").addEventListener("click", () => {
      if (cur > 0) setStep(cur - 1); else showOverview();
    });
    document.getElementById("nextBtn").addEventListener("click", () => {
      if (cur < STEPS.length - 1) setStep(cur + 1);
      else { closeOverlay(); showScreen("tracks"); }
    });

    document.getElementById("stageContent").addEventListener("click", (e) => {
      const flip = e.target.closest(".flip");
      if (flip) flip.classList.toggle("flipped");
    });

    document.addEventListener("keydown", (e) => {
      const ov = document.getElementById("lcOverlay");
      if (!ov.classList.contains("open")) return;
      const inDetail = document.getElementById("lcDetail").classList.contains("show");
      if (e.key === "Escape") { if (inDetail) { showOverview(); } else { closeOverlay(); } return; }
      if (!inDetail) return;
      if (e.key === "ArrowLeft" && cur < STEPS.length - 1) setStep(cur + 1);
      else if (e.key === "ArrowRight" && cur > 0) setStep(cur - 1);
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
