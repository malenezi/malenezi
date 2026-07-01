/* ============================================================
   أكاديمية سدايا · النموذج التشغيلي — العرض التنفيذي
   منطق العرض التفاعلي (بدون أي اعتماد خارجي)
   ============================================================ */
(function () {
  "use strict";
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const $  = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const AR = n => Number(n).toLocaleString("ar-EG");

  /* ---------------- مكتبة الأيقونات (Lucide inline) ---------------- */
  const LUCIDE = {
    "activity": '<path d="M22 12h-2.48a2 2 0 0 0-1.93 1.46l-2.35 8.36a.25.25 0 0 1-.48 0L9.24 2.18a.25.25 0 0 0-.48 0l-2.35 8.36A2 2 0 0 1 4.49 12H2"/>',
    "arrow-left": '<path d="m12 19-7-7 7-7"/><path d="M19 12H5"/>',
    "arrow-up": '<path d="m5 12 7-7 7 7"/><path d="M12 19V5"/>',
    "award": '<path d="m15.477 12.89 1.515 8.526a.5.5 0 0 1-.81.47l-3.58-2.687a1 1 0 0 0-1.197 0l-3.586 2.686a.5.5 0 0 1-.81-.469l1.514-8.526"/><circle cx="12" cy="8" r="6"/>',
    "badge-check": '<path d="M3.85 8.62a4 4 0 0 1 4.78-4.77 4 4 0 0 1 6.74 0 4 4 0 0 1 4.78 4.78 4 4 0 0 1 0 6.74 4 4 0 0 1-4.77 4.78 4 4 0 0 1-6.75 0 4 4 0 0 1-4.78-4.77 4 4 0 0 1 0-6.76Z"/><path d="m9 12 2 2 4-4"/>',
    "bar-chart-3": '<path d="M3 3v18h18"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/>',
    "blocks": '<rect width="7" height="7" x="14" y="3" rx="1"/><path d="M10 21V8a1 1 0 0 0-1-1H4a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-5a1 1 0 0 0-1-1H3"/>',
    "book-open": '<path d="M12 7v14"/><path d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3Z"/>',
    "calendar-check": '<path d="M8 2v4"/><path d="M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/><path d="m9 16 2 2 4-4"/>',
    "chevron-left": '<path d="m15 18-6-6 6-6"/>',
    "chevron-right": '<path d="m9 18 6-6-6-6"/>',
    "chevron-down": '<path d="m6 9 6 6 6-6"/>',
    "clipboard-check": '<rect width="8" height="4" x="8" y="2" rx="1" ry="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="m9 14 2 2 4-4"/>',
    "cpu": '<rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 2v2"/><path d="M9 20v2"/>',
    "database": '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14c0 1.66 4.03 3 9 3s9-1.34 9-3V5"/><path d="M3 12c0 1.66 4.03 3 9 3s9-1.34 9-3"/>',
    "git-branch": '<line x1="6" x2="6" y1="3" y2="15"/><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M18 9a9 9 0 0 1-9 9"/>',
    "graduation-cap": '<path d="M21.42 10.92a1 1 0 0 0-.02-1.84l-8.57-3.9a2 2 0 0 0-1.66 0l-8.57 3.9a1 1 0 0 0 0 1.84l8.57 3.9a2 2 0 0 0 1.66 0Z"/><path d="M22 10v6"/><path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5"/>',
    "inbox": '<polyline points="22 12 16 12 14 15 10 15 8 12 2 12"/><path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11Z"/>',
    "landmark": '<line x1="3" x2="21" y1="22" y2="22"/><line x1="6" x2="6" y1="18" y2="11"/><line x1="10" x2="10" y1="18" y2="11"/><line x1="14" x2="14" y1="18" y2="11"/><line x1="18" x2="18" y1="18" y2="11"/><polygon points="12 2 20 7 4 7"/>',
    "layers": '<path d="M12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.91a1 1 0 0 0 0-1.83Z"/><path d="m22 12.5-9.17 4.17a2 2 0 0 1-1.66 0L2 12.5"/><path d="m22 17.5-9.17 4.17a2 2 0 0 1-1.66 0L2 17.5"/>',
    "list-checks": '<path d="m3 17 2 2 4-4"/><path d="m3 7 2 2 4-4"/><path d="M13 6h8"/><path d="M13 12h8"/><path d="M13 18h8"/>',
    "megaphone": '<path d="m3 11 18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/>',
    "monitor-play": '<path d="M10 7.75a.75.75 0 0 1 1.142-.638l3.664 2.249a.75.75 0 0 1 0 1.278l-3.664 2.25a.75.75 0 0 1-1.142-.64z"/><path d="M12 17v4"/><path d="M8 21h8"/><rect x="2" y="3" width="20" height="14" rx="2"/>',
    "moon": '<path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/>',
    "package": '<path d="m7.5 4.27 9 5.15"/><path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><path d="m3.3 7 8.7 5 8.7-5"/><path d="M12 22V12"/>',
    "package-check": '<path d="m16 16 2 2 4-4"/><path d="M21 10V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l2-1.14"/><path d="M3.3 7 12 12l8.7-5"/><path d="M12 22V12"/>',
    "pencil-ruler": '<path d="m15 5 4 4"/><path d="M13 7 8 2 2 8l5 5"/><path d="m14 6 6 6"/><path d="m4 16 4 4"/><path d="m17 11 5 5-6 6-5-5Z"/>',
    "radar": '<path d="M19.07 4.93A10 10 0 0 0 6.99 3.34"/><path d="M4 6h.01"/><path d="M2.29 9.62A10 10 0 1 0 21.31 8.35"/><path d="M16.24 7.76A6 6 0 1 1 8.23 7.75"/><path d="M12 18h.01"/><path d="M17.99 11.66A6 6 0 0 0 15.77 8.23"/><path d="M12 12h.01"/>',
    "refresh-cw": '<path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"/><path d="M8 16H3v5"/>',
    "rocket": '<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/>',
    "route": '<circle cx="6" cy="19" r="3"/><path d="M9 19h8.5a3.5 3.5 0 0 0 0-7h-11a3.5 3.5 0 0 1 0-7H15"/><circle cx="18" cy="5" r="3"/>',
    "search-check": '<path d="m8 11 2 2 4-4"/><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    "settings": '<path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2Z"/><circle cx="12" cy="12" r="3"/>',
    "shield": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/>',
    "sparkles": '<path d="M9.94 15.5A2 2 0 0 0 8.5 14.06l-6.14-1.58a.5.5 0 0 1 0-.96L8.5 9.94A2 2 0 0 0 9.94 8.5l1.58-6.14a.5.5 0 0 1 .96 0l1.58 6.14a2 2 0 0 0 1.44 1.44l6.14 1.58a.5.5 0 0 1 0 .96l-6.14 1.58a2 2 0 0 0-1.44 1.44l-1.58 6.14a.5.5 0 0 1-.96 0Z"/><path d="M20 3v4"/><path d="M22 5h-4"/><path d="M4 17v2"/><path d="M5 18H3"/>',
    "square-play": '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="m10 8 6 4-6 4Z"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/>',
    "target": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    "trending-up": '<polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/>',
    "user-check": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><polyline points="16 11 18 13 22 9"/>',
    "workflow": '<rect width="8" height="8" x="3" y="3" rx="2"/><path d="M7 11v4a2 2 0 0 0 2 2h4"/><rect width="8" height="8" x="13" y="13" rx="2"/>'
  };
  const svg = (name, cls) => '<svg class="' + (cls || "ic") + '" viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' + (LUCIDE[name] || "") + '</svg>';
  const renderStaticIcons = (root) => (root || document).querySelectorAll("[data-icon]").forEach(el => { el.innerHTML = svg(el.dataset.icon); });

  /* ============================================================
     البيانات
     ============================================================ */
  const STEPS = [
    { ic:"radar", ar:"رصد الاحتياج", en:"Needs Sensing", color:"primary",
      desc:"نرصد إشارات الطلب الحقيقية من سدايا وأذرعها والسوق، ونحوّلها إلى احتياج تدريبي معتمد.",
      in:"الأولويات الحكومية والوطنية، واحتياجات أذرع سدايا، وتقارير السوق والشركاء.",
      act:"تحليل الاتجاهات العالمية، وورش ومقابلات منظّمة، وتحليل الوظائف وفق الجدارات.",
      out:"وثيقة احتياج معتمدة، وقائمة الفئات المستهدفة، وخريطة المهارات.",
      timeline:"٢–٤ أسابيع", outcome:"احتياج تدريبي معتمد وقابل للقياس" },
    { ic:"search-check", ar:"دراسة الفجوة", en:"Gap Analysis", color:"teal",
      desc:"نحوّل الفجوة بين الواقع والمستهدف إلى تقرير ومصفوفة مهارات مرتّبة بالأولوية.",
      in:"وثيقة الاحتياج، وخرائط المهارات الحالية، ومرجعيات الإطار الوطني.",
      act:"قياس الفجوة، وتحديد النضج الرقمي، وترتيب الأولويات بالأثر والإلحاح.",
      out:"تقرير الفجوة، ومصفوفة المهارات المستهدفة، وقائمة الأولويات.",
      timeline:"٢–٣ أسابيع", outcome:"خارطة أولويات مبنية على الأدلة" },
    { ic:"pencil-ruler", ar:"التصميم والتطوير", en:"Design & Development", color:"gold",
      desc:"نصمم التجربة بالبيانات، ونطوّر المحتوى بالذكاء الاصطناعي، حتى نصل إلى حقيبة تدريبية متكاملة.",
      model:{ name:"ADDIE", steps:["تحليل","تصميم","تطوير","تطبيق","تقويم"] },
      in:"تقرير الفجوة والمصفوفة، والأولويات المعتمدة، ومعايير الجودة (ADDIE).",
      act:"تصميم أهداف بلوم، وإنتاج محتوى بالذكاء الاصطناعي ومحاكاة، وتهيئة البيئة.",
      out:"حقيبة تدريبية متكاملة جاهزة للإطلاق، ومعايير الاعتماد.",
      timeline:"٦–١٠ أسابيع", outcome:"حقيبة معتمدة جاهزة للإطلاق" },
    { ic:"square-play", ar:"التقديم والتنفيذ", en:"Delivery & Execution", color:"violet",
      desc:"نستقطب المتدربين وننفّذ التدريب بجودة معتمدة عبر ثلاثة مسارات متكاملة.",
      in:"الحقيبة الجاهزة، والمدربون والشركاء المعتمدون، ومنصات التعلّم المهيأة.",
      act:"الاستقطاب والتسجيل عبر منصة أذكى، والتنفيذ عبر المدربين والشركاء، والعمليات المشتركة.",
      out:"برنامج منفّذ، وبيانات الأداء، وسجلات الحضور والإنجاز.",
      timeline:"حسب البرنامج", outcome:"تنفيذ عالي الجودة موثّق بالبيانات" },
    { ic:"clipboard-check", ar:"التقييم", en:"Evaluation", color:"primary",
      desc:"نقيس الرضا والمعرفة وجودة التنفيذ عبر تقارير مباشرة تُغذّي قياس الأثر والتحسين.",
      in:"البرنامج المنفّذ وبياناته، والاختبارات القبلية والبعدية، وملاحظات المدربين.",
      act:"قياس الرضا NPS، وقياس اكتساب المعرفة، وتقييم جودة المدرب والمحتوى.",
      out:"تقارير تقييم مباشر، وإصدار الشهادات، والتهيئة للشارة أو التوظيف.",
      timeline:"١–٢ أسبوع", outcome:"شهادات صادرة ومؤشرات موثّقة" },
    { ic:"trending-up", ar:"قياس الأثر", en:"Impact Measurement", color:"teal",
      desc:"نقيس تطبيق المهارات في بيئة العمل والعائد المهني عبر تقرير أثر شامل وتوصيات تطوير.",
      in:"تقارير التقييم والشهادات، وبيانات جهات العمل، وبيانات السوق والتوظيف.",
      act:"قياس تطبيق المهارات، واستبيانات بعد ٣ و٦ و١٢ شهراً، وتحليل المسار المهني.",
      out:"تقرير أثر شامل، وتوصيات تطوير، وتوثيق نماذج النجاح.",
      timeline:"٣–١٢ شهراً", outcome:"دليل أثر مهني قابل للتنفيذ" },
    { ic:"refresh-cw", ar:"التحسين المستمر", en:"Continuous Improvement", color:"gold",
      desc:"نطوّر إصدارات محسّنة وخارطة سنوية معتمدة تُغذّي مرحلة رصد الاحتياج في دورة جديدة.",
      in:"مخرجات التقييم والأثر، واتجاهات السوق، وبيانات المنصات وملاحظات الشركاء.",
      act:"تطوير المحتوى، وتحسين أساليب التنفيذ، وتحديث البرامج ومراجعة الأهداف.",
      out:"إصدارات محسّنة، وخارطة تطوير سنوية معتمدة، وتغذية دورة جديدة.",
      timeline:"دورة سنوية", outcome:"حلقة تحسين مغلقة ومستدامة" }
  ];

  /* بطاقات الإطار الوطني للمؤهلات */
  const NQF = [
    { ic:"layers", t:"مستويات المؤهلات", d:"تصنيف وطني موحّد لمستويات التعلّم يحدّد عمق كل برنامج ومخرجاته." },
    { ic:"badge-check", t:"جدارات مرجعية", d:"جدارات وطنية تُشتقّ منها أهداف التعلّم ومعايير التقييم لكل وحدة." },
    { ic:"shield", t:"اعتراف ومواءمة", d:"اعتراف وطني بالشارات والشهادات ومواءمتها لاحتياجات سوق العمل." }
  ];

  /* عناصر داعمة (ندوات وفعاليات) — عناصر عامة دون أسماء شركات */
  const SUPPORT = [
    { ic:"megaphone", t:"ندوات الخبراء", d:"لقاءات دورية مع خبراء من الجهات الحكومية وأذرع سدايا حول أحدث التطبيقات.", tag:"حضوري" },
    { ic:"monitor-play", t:"ويبينار مع شركات محلية", d:"بثّ مباشر مع ممارسين من الشركات التقنية المحلية لنقل خبرات السوق.", tag:"عن بُعد" },
    { ic:"pencil-ruler", t:"ورش تطبيقية", d:"ورش عملية قصيرة على أدوات وحالات استخدام واقعية من الميدان.", tag:"تطبيقي" },
    { ic:"rocket", t:"تحدّيات وهاكاثون", d:"تحدّيات تنافسية مبنية على مشكلات فعلية من السوق السعودي.", tag:"تنافسي" }
  ];

  /* الوحدات التدريبية (من مصفوفة التتبّع الرسمية) — lv: S أخصائي · E خبير · topics: أبرز المحاور */
  const SHARED = [
    { ref:"SF-1", code:"P2.1.01", ic:"database",    t:"أساسيات البيانات للذكاء الاصطناعي والتحليلات", en:"Data Foundations", h:15, lv:"S", topics:["أنواع البيانات وجودتها","خطوط معالجة البيانات","التهيئة للنمذجة"] },
    { ref:"SF-2", code:"P2.1.02", ic:"cpu",         t:"أساسيات تعلّم الآلة التطبيقي", en:"Applied ML Essentials", h:15, lv:"S", topics:["خوارزميات التعلّم الأساسية","التدريب وضبط النماذج","المقايضات العملية"] },
    { ref:"SF-3", code:"P2.1.03", ic:"list-checks", t:"تقييم النماذج والتحقّق منها", en:"Model Evaluation", h:12, lv:"S", topics:["مقاييس الأداء","التحقّق المتقاطع","كشف الانحياز"] },
    { ref:"SF-4", code:"P7.1.01", ic:"badge-check", t:"الذكاء الاصطناعي المسؤول وحوكمة البيانات", en:"Responsible AI", h:12, lv:"S", topics:["أخلاقيات الذكاء الاصطناعي","حوكمة البيانات الوطنية","الخصوصية والامتثال"] },
    { ref:"SF-5", code:"P2.1.04", ic:"megaphone",   t:"تأطير المشكلات والتواصل", en:"Problem Framing", h:10, lv:"S", topics:["صياغة المشكلة","التواصل مع الأطراف","سرد النتائج"] }
  ];
  const AE_TRACK = [
    { ref:"AE-1", code:"P5.1.01", ic:"layers",       t:"التعلّم العميق والنماذج الأساسية", h:15, lv:"S", topics:["الشبكات العصبية","المحوّلات Transformers","النماذج الأساسية"] },
    { ref:"AE-2", code:"P5.1.02", ic:"search-check", t:"أنظمة التوليد المعزّز بالاسترجاع RAG", h:15, lv:"S", topics:["قواعد المتجهات","الاسترجاع الدلالي","تحسين السياق"] },
    { ref:"AE-3", code:"P5.1.03", ic:"sparkles",     t:"الذكاء الوكيلي وهندسة تطبيقات LLM", h:15, lv:"E", topics:["الوكلاء والأدوات","هندسة التلقين","تنسيق المهام"] },
    { ref:"AE-4", code:"P5.1.04", ic:"workflow",     t:"هندسة برمجيات الذكاء الاصطناعي والتكامل", h:15, lv:"S", topics:["واجهات البرمجة APIs","التكامل والنشر","معمارية الخدمات"] },
    { ref:"AE-5", code:"P5.1.05", ic:"settings",     t:"MLOps وLLMOps: النشر ودورة حياة النموذج", h:14, lv:"E", topics:["خطوط CI/CD","إدارة الإصدارات","أتمتة دورة النموذج"] },
    { ref:"AE-6", code:"P5.1.06", ic:"radar",        t:"المراقبة والموثوقية والاستجابة للحوادث", h:10, lv:"E", topics:["المراقبة والتنبيه","الموثوقية","الاستجابة للحوادث"] },
    { ref:"AE-7", code:"P5.1.07", ic:"trending-up",  t:"الأداء وقابلية التوسّع وتحسين التكلفة", h:12, lv:"E", topics:["زمن الاستجابة","قابلية التوسّع","تحسين التكلفة"] },
    { ref:"AE-8", code:"P5.1.08", ic:"shield",       t:"أمن الذكاء الاصطناعي والنماذج اللغوية", h:13, lv:"E", topics:["هجمات النماذج","الحقن التلقيني","تحصين الأنظمة"] }
  ];
  const AE_CAP = { ref:"AE-Cap", code:"P5.1.09", ic:"graduation-cap", t:"مشروع التخرّج: أنظمة توليدية إنتاجية", h:15, lv:"E", cap:true, topics:["نظام توليدي إنتاجي متكامل","معايير جودة واعتماد","تطبيق واقعي للجدارات"] };
  const DS_TRACK = [
    { ref:"DS-1", code:"P6.1.01", ic:"bar-chart-3", t:"الأسس الإحصائية والاستدلال لعلم البيانات", h:15, lv:"S", topics:["الاحتمالات والتوزيعات","الاستدلال الإحصائي","اختبار الفرضيات"] },
    { ref:"DS-2", code:"P6.1.02", ic:"workflow",    t:"هندسة البيانات للتحليلات واسعة النطاق", h:14, lv:"S", topics:["خطوط ETL/ELT","المعالجة واسعة النطاق","مستودعات البيانات"] },
    { ref:"DS-3", code:"P6.1.03", ic:"cpu",         t:"تعلّم الآلة التطبيقي للأنظمة الذكية", h:15, lv:"S", topics:["نمذجة تنبؤية","هندسة الخصائص","تحسين النماذج"] },
    { ref:"DS-4", code:"P6.1.04", ic:"target",      t:"التجريب والاستدلال السببي", h:15, lv:"E", topics:["التصميم التجريبي","اختبارات A/B","الاستدلال السببي"] },
    { ref:"DS-5", code:"P6.1.05", ic:"trending-up", t:"تصوير البيانات والرؤى ورواية البيانات", h:15, lv:"S", topics:["لوحات المعلومات","التصوير الفعّال","رواية البيانات"] },
    { ref:"DS-6", code:"P6.1.06", ic:"refresh-cw",  t:"علم البيانات القابل للتكرار والمعزّز بالذكاء التوليدي", h:12, lv:"E", topics:["بيئات قابلة للتكرار","مساعدة الذكاء التوليدي","توثيق التجارب"] }
  ];
  const DS_CAP = { ref:"DS-Cap", code:"P6.1.07", ic:"graduation-cap", t:"مشروع التخرّج: من السؤال إلى القرار", h:15, lv:"E", cap:true, topics:["من السؤال إلى القرار","تحليل شامل موجّه بالأثر","تطبيق واقعي للجدارات"] };

  const TRACKS = [
    { cls:"t1", ic:"cpu", ar:"مهندس الذكاء الاصطناعي", en:"AI Engineer Track",
      cert:"شهادة مهندس الذكاء الاصطناعي المهنية", certH:"١٨٨ ساعة · مستوى خبير", mods:AE_TRACK, cap:AE_CAP },
    { cls:"t2", ic:"database", ar:"عالِم البيانات", en:"Data Scientist Track",
      cert:"شهادة عالِم البيانات المهنية", certH:"١٦٥ ساعة · مستوى خبير", mods:DS_TRACK, cap:DS_CAP }
  ];

  /* ============================================================
     دورة الحياة — لوحة تفاصيل المرحلة المحددة
     ============================================================ */
  const rail = $("#stepperRail");
  const seen = new Set();
  let active = 0;
  const CIRC = 113;

  STEPS.forEach((s, i) => {
    const b = document.createElement("button");
    b.type = "button"; b.className = "snode"; b.dataset.i = i;
    b.setAttribute("aria-label", "المرحلة " + AR(i + 1) + ": " + s.ar);
    b.innerHTML =
      '<span class="snode__line"></span>' +
      '<span class="snode__b">' + svg(s.ic) + '<span class="snode__n">' + AR(i + 1) + '</span></span>' +
      '<span class="snode__t">' + s.ar + '</span>';
    b.addEventListener("click", () => setStage(i));
    rail.appendChild(b);
  });
  const snodes = $$(".snode", rail);
  const nodeEl = $("#stageNode"), flowEl = $("#stageFlow"), metaEl = $("#stageMeta"), panelEl = $("#stagePanel");

  function nodeHTML(s, i) {
    return '<span class="stage-node__ic">' + svg(s.ic) + '</span>' +
      '<div class="stage-node__k">المرحلة ' + AR(i + 1) + ' من ٧</div>' +
      '<h3>' + s.ar + '<span class="en">' + s.en + '</span></h3>' +
      '<p>' + s.desc + '</p>' +
      (s.model ?
        '<div class="stage-model"><span class="stage-model__lbl">' + svg("layers") + ' نموذج ' + s.model.name + '</span>' +
        '<div class="stage-model__row">' + s.model.steps.map((x, k) =>
          '<span class="sms">' + x + '</span>' + (k < s.model.steps.length - 1 ? '<span class="sms-sep">' + svg("chevron-left") + '</span>' : "")
        ).join("") + '</div></div>' : "");
  }
  function flowHTML(s) {
    const cards = [
      { cls:"in",  ic:"inbox",         label:"المدخلات", sub:"مصادر الإدخال",   txt:s.in },
      { cls:"act", ic:"activity",      label:"الأنشطة",  sub:"ما نقوم به",       txt:s.act },
      { cls:"out", ic:"package-check", label:"المخرجات", sub:"النتائج المعتمدة", txt:s.out }
    ];
    const arrow = '<span class="stage-flow__arrow">' + svg("chevron-left") + '</span>';
    return cards.map(c =>
      '<div class="proc ' + c.cls + '">' +
        '<span class="proc__ic">' + svg(c.ic) + '</span>' +
        '<div class="proc__b"><span class="proc__lbl">' + c.label + '</span>' +
        '<span class="proc__sub">' + c.sub + '</span><p>' + c.txt + '</p></div>' +
      '</div>').join(arrow);
  }
  function metaHTML(s) {
    return '<div class="smeta"><span class="smeta__ic">' + svg("calendar-check") + '</span>' +
        '<div><span class="k">المدة التقديرية</span><span class="v">' + s.timeline + '</span></div></div>' +
      '<div class="smeta"><span class="smeta__ic">' + svg("target") + '</span>' +
        '<div><span class="k">المحصّلة</span><span class="v">' + s.outcome + '</span></div></div>';
  }
  function updateRing() {
    const pct = Math.round(seen.size / STEPS.length * 100);
    $("#ringProg").style.strokeDashoffset = CIRC * (1 - pct / 100);
    $("#ringPct").textContent = AR(pct) + "٪";
  }
  function setStage(i) {
    active = i;
    const s = STEPS[i];
    snodes.forEach((n, k) => { n.classList.toggle("active", k === i); n.classList.toggle("done", k < i); });
    panelEl.setAttribute("data-color", s.color);
    nodeEl.classList.remove("anim"); void nodeEl.offsetWidth; nodeEl.classList.add("anim");
    flowEl.classList.remove("anim"); void flowEl.offsetWidth; flowEl.classList.add("anim");
    nodeEl.innerHTML = nodeHTML(s, i);
    flowEl.innerHTML = flowHTML(s);
    metaEl.innerHTML = metaHTML(s);
    $("#stageCounter").textContent = "المرحلة " + AR(i + 1) + " من ٧";
    $("#prevStage").disabled = i <= 0;
    $("#nextStage").disabled = i >= STEPS.length - 1;
    seen.add(i); updateRing();
  }
  $("#prevStage").addEventListener("click", () => { if (active > 0) setStage(active - 1); });
  $("#nextStage").addEventListener("click", () => { if (active < STEPS.length - 1) setStage(active + 1); });
  setStage(0);

  /* ============================================================
     المسارات — بطاقات وحدات قابلة للقلب
     ============================================================ */
  const lvName = lv => lv === "E" ? "خبير" : "أخصائي";
  function chip(m, n, extra) {
    const topics = (m.topics || []).map(t => '<li>' + t + '</li>').join("");
    const marketTag = m.cap ? '<span class="umod__market">' + svg("target") + ' مستمدّ من احتياج السوق</span>' : '';
    return '<div class="umod ' + (extra || "") + '" data-lv="' + m.lv + '" tabindex="0" ' +
      'title="' + m.code + ' · ' + lvName(m.lv) + ' · ' + m.h + ' ساعة">' +
      '<div class="umod__in">' +
        '<div class="umod__face umod__front">' +
          (n ? '<span class="umod__n">' + n + '</span>' : '') +
          '<span class="umod__lv">' + lvName(m.lv) + '</span>' +
          '<span class="umod__ic">' + svg(m.ic) + '</span>' +
          '<div class="umod__t">' + m.t + '</div>' +
          marketTag +
          '<div class="umod__foot"><span class="umod__ref">' + m.ref + '</span>' +
            '<span class="umod__h">' + svg("calendar-check") + ' ' + AR(m.h) + ' ساعة</span></div>' +
          '<span class="umod__hint">' + svg("layers") + ' مرّر لعرض المحاور</span>' +
        '</div>' +
        '<div class="umod__face umod__back">' +
          '<div class="umod__back-h">' + svg(m.ic) + '<b>أبرز المحاور</b></div>' +
          '<ul class="umod__topics">' + topics + '</ul>' +
        '</div>' +
      '</div>' +
    '</div>';
  }

  $("#nqfGrid").innerHTML = NQF.map(c =>
    '<div class="nqf-card"><span class="nqf-card__ic">' + svg(c.ic) + '</span>' +
    '<b>' + c.t + '</b><p>' + c.d + '</p></div>').join("");

  $("#sharedMods").innerHTML = SHARED.map((m, i) => chip(m, AR(i + 1))).join("");

  $("#trackList").innerHTML = TRACKS.map(t => {
    const seq = t.mods.map((m, i) => chip(m, AR(i + 1))).join("");
    return '<div class="track ' + t.cls + '">' +
      '<div class="track__head">' +
        '<span class="track__ic">' + svg(t.ic) + '</span>' +
        '<div><h3>' + t.ar + '<span class="en">' + t.en + '</span></h3></div>' +
        '<span class="track__tag">الطبقة ٢ · ' + AR(t.mods.length) + ' وحدات</span>' +
      '</div>' +
      '<div class="mods">' + seq + '</div>' +
      '<div class="track__foot">' +
        '<div class="cap">' + chip(t.cap, "★", "is-cap") + '</div>' +
        '<div class="cert"><span class="cert__ic">' + svg("award") + '</span>' +
          '<div><b>' + t.cert + '</b><span>' + t.certH + '</span></div></div>' +
      '</div>' +
    '</div>';
  }).join("");

  $("#supportGrid").innerHTML = SUPPORT.map(c =>
    '<div class="scard"><span class="scard__ic">' + svg(c.ic) + '</span>' +
    '<h4>' + c.t + '</h4><p>' + c.d + '</p>' +
    '<span class="scard__tag">' + svg("badge-check") + ' ' + c.tag + '</span></div>').join("");

  /* ============================================================
     المظهر (فاتح / داكن)
     ============================================================ */
  const root = document.documentElement;
  function setTheme(d) {
    root.classList.toggle("dark", d);
    $("#themeToggle").innerHTML = svg(d ? "sun" : "moon");
  }
  let dark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
  setTheme(dark);
  $("#themeToggle").addEventListener("click", () => { dark = !dark; setTheme(dark); });

  /* ============================================================
     الظهور عند التمرير + العدّادات
     ============================================================ */
  renderStaticIcons();

  if (reduce) {
    $$(".reveal").forEach(el => el.classList.add("show"));
    $$("[data-count]").forEach(el => { el.textContent = AR(el.dataset.count) + (el.dataset.suffix || ""); });
  } else {
    const io = new IntersectionObserver((es) => {
      es.forEach(e => { if (e.isIntersecting) { e.target.classList.add("show"); io.unobserve(e.target); } });
    }, { threshold: .12 });
    $$(".reveal").forEach(el => io.observe(el));

    const cio = new IntersectionObserver((es) => {
      es.forEach(e => {
        if (!e.isIntersecting) return;
        const el = e.target, to = +el.dataset.count, suf = el.dataset.suffix || "";
        let n = 0; const step = Math.max(1, Math.round(to / 40));
        const t = setInterval(() => { n += step; if (n >= to) { n = to; clearInterval(t); } el.textContent = AR(n) + suf; }, 26);
        cio.unobserve(el);
      });
    }, { threshold: .6 });
    $$("[data-count]").forEach(el => cio.observe(el));
  }

  /* ============================================================
     التمرير: المؤشر + التنقل النشط + زر الأعلى
     ============================================================ */
  const prog = $("#scrollProg"), toTop = $("#toTop");
  const navlinks = $$(".nav__links a");
  const secs = ["hero", "lifecycle", "tracks", "support", "impact"];
  window.addEventListener("scroll", () => {
    const h = document.documentElement;
    const sc = h.scrollTop / (h.scrollHeight - h.clientHeight || 1);
    prog.style.width = (sc * 100) + "%";
    toTop.classList.toggle("show", h.scrollTop > 500);
    let cur = secs[0];
    for (const id of secs) { const el = document.getElementById(id); if (el && el.getBoundingClientRect().top <= 160) cur = id; }
    navlinks.forEach(a => a.classList.toggle("active", a.getAttribute("href") === "#" + cur));
  }, { passive: true });
  toTop.addEventListener("click", () => window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" }));

  /* التنقل بالأسهم بين المراحل عندما يكون القسم ظاهراً */
  document.addEventListener("keydown", (e) => {
    const lc = document.getElementById("lifecycle").getBoundingClientRect();
    const visible = lc.top < window.innerHeight * .6 && lc.bottom > window.innerHeight * .4;
    if (!visible) return;
    if (e.key === "ArrowLeft" && active < STEPS.length - 1) setStage(active + 1);
    else if (e.key === "ArrowRight" && active > 0) setStage(active - 1);
  });
})();
