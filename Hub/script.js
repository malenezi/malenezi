/* ============================================================
   أكاديمية سدايا · دورة حياة البرامج (النسخة الثانية)
   نافذة منبثقة بملء الشاشة · تفرّع جانبي · مسارات بتفاصيل
   ============================================================ */
(function () {
  "use strict";
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Lucide icons ---------- */
  const LUCIDE = {
    "activity": '<path d="M22 12h-2.48a2 2 0 0 0-1.93 1.46l-2.35 8.36a.25.25 0 0 1-.48 0L9.24 2.18a.25.25 0 0 0-.48 0l-2.35 8.36A2 2 0 0 1 4.49 12H2"/>',
    "badge-check": '<path d="M3.85 8.62a4 4 0 0 1 4.78-4.77 4 4 0 0 1 6.74 0 4 4 0 0 1 4.78 4.78 4 4 0 0 1 0 6.74 4 4 0 0 1-4.77 4.78 4 4 0 0 1-6.75 0 4 4 0 0 1-4.78-4.77 4 4 0 0 1 0-6.76Z"/><path d="m9 12 2 2 4-4"/>',
    "bar-chart-3": '<path d="M3 3v18h18"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/>',
    "book-open": '<path d="M12 7v14"/><path d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3Z"/>',
    "calendar-days": '<path d="M8 2v4"/><path d="M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/><path d="M8 14h.01"/><path d="M12 14h.01"/><path d="M16 14h.01"/><path d="M8 18h.01"/><path d="M12 18h.01"/><path d="M16 18h.01"/>',
    "chevron-left": '<path d="m15 18-6-6 6-6"/>',
    "chevron-right": '<path d="m9 18 6-6-6-6"/>',
    "clipboard-check": '<rect width="8" height="4" x="8" y="2" rx="1" ry="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="m9 14 2 2 4-4"/>',
    "cpu": '<rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 2v2"/><path d="M9 20v2"/>',
    "database": '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14c0 1.66 4.03 3 9 3s9-1.34 9-3V5"/><path d="M3 12c0 1.66 4.03 3 9 3s9-1.34 9-3"/>',
    "gauge": '<path d="m12 14 4-4"/><path d="M3.34 19a10 10 0 1 1 17.32 0"/>',
    "graduation-cap": '<path d="M21.42 10.92a1 1 0 0 0-.02-1.84l-8.57-3.9a2 2 0 0 0-1.66 0l-8.57 3.9a1 1 0 0 0 0 1.84l8.57 3.9a2 2 0 0 0 1.66 0Z"/><path d="M22 10v6"/><path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5"/>',
    "inbox": '<polyline points="22 12 16 12 14 15 10 15 8 12 2 12"/><path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11Z"/>',
    "layers": '<path d="m12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.91a1 1 0 0 0 0-1.83Z"/><path d="m22 12.5-9.17 4.17a2 2 0 0 1-1.66 0L2 12.5"/><path d="m22 17.5-9.17 4.17a2 2 0 0 1-1.66 0L2 17.5"/>',
    "network": '<rect x="16" y="16" width="6" height="6" rx="1"/><rect x="2" y="16" width="6" height="6" rx="1"/><rect x="9" y="2" width="6" height="6" rx="1"/><path d="M5 16v-3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3"/><path d="M12 12V8"/>',
    "package": '<path d="m7.5 4.27 9 5.15"/><path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><path d="m3.3 7 8.7 5 8.7-5"/><path d="M12 22V12"/>',
    "pencil-ruler": '<path d="m15 5 4 4"/><path d="M13 7 8 2 2 8l5 5"/><path d="m14 6 6 6"/><path d="m4 16 4 4"/><path d="m17 11 5 5-6 6-5-5Z"/>',
    "radar": '<path d="M19.07 4.93A10 10 0 0 0 6.99 3.34"/><path d="M4 6h.01"/><path d="M2.29 9.62A10 10 0 1 0 21.31 8.35"/><path d="M16.24 7.76A6 6 0 1 1 8.23 7.75"/><path d="M12 18h.01"/><path d="M17.99 11.66A6 6 0 0 0 15.77 8.23"/><path d="M12 12h.01"/>',
    "refresh-cw": '<path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"/><path d="M8 16H3v5"/>',
    "route": '<circle cx="6" cy="19" r="3"/><path d="M9 19h8.5a3.5 3.5 0 0 0 0-7h-11a3.5 3.5 0 0 1 0-7H15"/><circle cx="18" cy="5" r="3"/>',
    "search-check": '<path d="m8 11 2 2 4-4"/><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    "settings": '<path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2Z"/><circle cx="12" cy="12" r="3"/>',
    "sparkles": '<path d="M9.94 15.5A2 2 0 0 0 8.5 14.06l-6.14-1.58a.5.5 0 0 1 0-.96L8.5 9.94A2 2 0 0 0 9.94 8.5l1.58-6.14a.5.5 0 0 1 .96 0l1.58 6.14a2 2 0 0 0 1.44 1.44l6.14 1.58a.5.5 0 0 1 0 .96l-6.14 1.58a2 2 0 0 0-1.44 1.44l-1.58 6.14a.5.5 0 0 1-.96 0Z"/><path d="M20 3v4"/><path d="M22 5h-4"/><path d="M4 17v2"/><path d="M5 18H3"/>',
    "square-play": '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="m10 8 6 4-6 4Z"/>',
    "trending-up": '<polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/>',
    "workflow": '<rect width="8" height="8" x="3" y="3" rx="2"/><path d="M7 11v4a2 2 0 0 0 2 2h4"/><rect width="8" height="8" x="13" y="13" rx="2"/>',
    "x": '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>'
  };
  const P = {
    cycle:"refresh-cw", route:"route",
    s1:"radar", s2:"search-check", s3:"pencil-ruler", s4:"square-play", s5:"clipboard-check", s6:"trending-up", s7:"refresh-cw",
    cal:"calendar-days", cap:"graduation-cap", net:"network", cpu:"cpu", db:"database", book:"book-open", layers:"layers",
    gear:"settings", spark:"sparkles", bars:"bar-chart-3", flow:"workflow", badge:"badge-check",
    inbox:"inbox", act:"activity", box:"package", gauge:"gauge",
    prev:"chevron-right", next:"chevron-left"
  };
  const svg = (name, cls) => `<svg class="${cls || "ic"}" viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">${LUCIDE[name] || ""}</svg>`;
  const renderStaticIcons = (root = document) => {
    root.querySelectorAll("[data-icon]").forEach(el => {
      el.innerHTML = svg(el.dataset.icon);
    });
  };

  /* ---------- المراحل السبع (تفاصيل بأيقونات ونص قليل) ---------- */
  const D = (inv, dov, outv, kpiv) => ([
    { ic:P.inbox, l:"المدخلات", v:inv },
    { ic:P.act,   l:"النشاط",   v:dov },
    { ic:P.box,   l:"المخرج",   v:outv },
    { ic:P.gauge, l:"المؤشر",   v:kpiv }
  ]);
  const STEPS = [
    { ic:P.s1, ar:"رصد الاحتياج", en:"Need Sensing", desc:"ننطلق من إشارات الطلب الحقيقية.", items:D("إشارات الطلب","تحليل واستطلاع","وثيقة الاحتياج","تغطية القطاعات") },
    { ic:P.s2, ar:"دراسة الفجوة", en:"Gap Analysis", desc:"نحدّد الفجوة بين الواقع والمستهدف.", items:D("الاحتياج المعتمد","تحليل الفجوة","تقرير الفجوة","المهارات الحرجة") },
    { ic:P.s3, ar:"التصميم والتطوير", en:"Design & Develop", desc:"تصميم بالبيانات وتطوير بالذكاء الاصطناعي.", items:D("مواصفات البرنامج","تصميم + تطوير","حقيبة تدريبية","زمن التطوير") },
    { ic:P.s4, ar:"التقديم والتنفيذ", en:"Delivery", desc:"استقطاب وتنفيذ بجودة معتمدة — ومنها يتفرّع المسار.", items:D("الحقيبة الجاهزة","استقطاب وتنفيذ","برامج منفّذة","معدل الإكمال") },
    { ic:P.s5, ar:"التقييم", en:"Evaluation", desc:"بوابة الجودة عبر الاختبارات والرضا.", items:D("بيانات التشغيل","اختبارات ورضا","شهادات معتمدة","NPS > 70") },
    { ic:P.s6, ar:"قياس الأثر", en:"Impact", desc:"نقيس تطبيق المهارات وأثرها المهني.", items:D("تقارير التقييم","قياس بعد التدريب","تقرير الأثر","تطبيق المهارات") },
    { ic:P.s7, ar:"التحسين المستمر", en:"Continuous Imp.", desc:"حلقة تغذية راجعة تُحسّن النموذج.", items:D("الدروس المستفادة","تحديث وتحسين","نسخ محدّثة","تحسّن المؤشرات") }
  ];

  /* ---------- التفرّع بعد المرحلة الرابعة ---------- */
  const ENABLERS = [
    { ic:P.cal, ar:"الجدولة المستمرة", desc:"تقويم سنوي ونموذج «مضمون الانعقاد».", chip:"365 يوماً" },
    { ic:P.cap, ar:"المدربون المتميزون", desc:"ممارسون معتمدون عبر تأهيل دقيق.", chip:"4 مراحل اعتماد" },
    { ic:P.net, ar:"التوسع المنضبط", desc:"ممكّن وطني عبر جامعات شريكة.", chip:"16 جامعة" }
  ];

  /* ---------- مسارات التدريب (محطات بتفاصيل) ---------- */
  const TRACKS = [
    { cls:"t1", ic:P.cpu, ar:"مسار تدريب مهندس الذكاء الاصطناعي", en:"AI Engineer Track",
      meta:["المدة: 12–16 أسبوعاً", "المستوى: متقدم", "المخرج: شارة محترف + توظيف"],
      miles:[
        { ic:P.book,  t:"الأساسيات", d:"بايثون والرياضيات للذكاء الاصطناعي" },
        { ic:P.s2,    t:"تعلّم الآلة", d:"الخوارزميات الإشرافية وتقييمها" },
        { ic:P.layers,t:"التعلم العميق", d:"الشبكات العصبية والرؤية واللغة" },
        { ic:P.gear,  t:"التشغيل MLOps", d:"أتمتة ونشر النماذج في الإنتاج" },
        { ic:P.spark, t:"الذكاء التوليدي", d:"النماذج اللغوية وبناء الوكلاء" },
        { ic:P.badge, t:"شارة المحترف", d:"اعتماد مهني + مشروع تطبيقي", end:true }
      ] },
    { cls:"t2", ic:P.db, ar:"مسار تدريب عالم البيانات", en:"Data Scientist Track",
      meta:["المدة: 12–16 أسبوعاً", "المستوى: متوسط–متقدم", "المخرج: شارة محترف + توظيف"],
      miles:[
        { ic:P.db,   t:"أساسيات البيانات", d:"الجمع والتنظيف والتهيئة" },
        { ic:P.bars, t:"الإحصاء والتحليل", d:"التحليل الاستكشافي والاستدلالي" },
        { ic:P.cpu,  t:"التعلم الآلي", d:"النمذجة التنبؤية والتقييم" },
        { ic:P.flow, t:"هندسة البيانات", d:"خطوط البيانات والمستودعات" },
        { ic:P.s6,   t:"التصور ودعم القرار", d:"لوحات المعلومات ورواية البيانات" },
        { ic:P.badge,t:"شارة المحترف", d:"اعتماد مهني + مشروع تطبيقي", end:true }
      ] }
  ];

  /* ---------- إدارة الشاشات والنافذة ---------- */
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
    setStep(0);
  }
  function closeOverlay() {
    document.getElementById("lcOverlay").classList.remove("open");
    document.body.classList.remove("overlay-active");
    document.body.style.overflow = "";
  }

  /* ---------- دورة الحياة ---------- */
  let cur = 0, railEls = [];
  function buildRail() {
    const rail = document.getElementById("rail");
    STEPS.forEach((s, i) => {
      const b = document.createElement("button");
      b.type = "button"; b.className = "rstep" + (i === 3 ? " branch4" : "");
      b.innerHTML = `<span class="rstep__b">${svg(s.ic)}<span class="rstep__n">${i+1}</span></span><span class="rstep__t">${s.ar}</span>`;
      b.addEventListener("click", () => setStep(i));
      rail.appendChild(b); railEls.push(b);
    });
  }

  function nodeHTML(s, i) {
    return `
      <span class="node__ic">${svg(s.ic)}</span>
      <div class="k">المرحلة ${i+1} من 7</div>
      <h3>${s.ar}<span class="en">${s.en}</span></h3>
      <p>${s.desc}</p>`;
  }
  function detailHTML(s) {
    return `<div class="dgrid anim">` + s.items.map(it =>
      `<div class="dcard"><span class="dcard__ic">${svg(it.ic)}</span><div class="l">${it.l}</div><div class="v">${it.v}</div></div>`
    ).join("") + `</div>`;
  }
  function branchHTML() {
    return `<div class="branch-out" id="branchOut">
      <span class="branch-out__tag">${svg(P.s4)} يتفرّع من التنفيذ</span>` +
      ENABLERS.map(e => `<div class="enabler">
        <span class="enabler__ic">${svg(e.ic)}</span>
        <div><h4>${e.ar}</h4><p>${e.desc}</p><span class="chip">${e.chip}</span></div>
      </div>`).join("") + `</div>`;
  }

  function setStep(i) {
    cur = i;
    railEls.forEach((el, k) => { el.classList.toggle("active", k === i); el.classList.toggle("done", k < i); });

    const s = STEPS[i];
    const node = document.getElementById("node");
    node.classList.remove("anim"); void node.offsetWidth; node.classList.add("anim");
    node.innerHTML = nodeHTML(s, i);

    const content = document.getElementById("stageContent");
    if (i === 3) {
      content.innerHTML = branchHTML();
      requestAnimationFrame(() => document.getElementById("branchOut").classList.add("show"));
    } else {
      content.innerHTML = detailHTML(s);
    }

    document.getElementById("count").textContent = `المرحلة ${i+1} / 7`;
    document.getElementById("ovCount").textContent = `المرحلة ${i+1} / 7`;
    document.getElementById("prevBtn").disabled = i === 0;
    const next = document.getElementById("nextBtn");
    next.innerHTML = i === STEPS.length - 1
      ? `مسارات التدريب ${svg(P.route)}`
      : `التالي ${svg(P.next)}`;
  }

  /* ---------- مسارات التدريب ---------- */
  function buildTracks() {
    const wrap = document.getElementById("trackList");
    TRACKS.forEach(t => {
      const d = document.createElement("div"); d.className = "track " + t.cls;
      const miles = t.miles.map((m, k) => `
        <div class="mile ${m.end ? "end" : ""}">
          <span class="mile__b">${svg(m.ic)}</span>
          <div class="mile__n">المحطة ${k+1}</div>
          <div class="mile__t">${m.t}</div>
          <div class="mile__d">${m.d}</div>
        </div>`).join("");
      d.innerHTML = `
        <div class="track__head">
          <span class="track__ic">${svg(t.ic)}</span>
          <div><h3>${t.ar}</h3><span class="en">${t.en}</span></div>
          <div class="track__meta">${t.meta.map(m => `<span class="m">${m}</span>`).join("")}</div>
        </div>
        <div class="path">${miles}</div>`;
      wrap.appendChild(d);
    });
  }
  function revealTracks() {
    const els = document.querySelectorAll("#tracks .track");
    if (reduce) { els.forEach(e => e.classList.add("in")); return; }
    els.forEach((e, i) => setTimeout(() => e.classList.add("in"), 120 + i * 160));
  }

  /* ---------- التشغيل ---------- */
  function boot() {
    renderStaticIcons();
    document.getElementById("lcIcon").innerHTML = svg(P.cycle);
    document.getElementById("trIcon").innerHTML = svg(P.route);
    buildRail(); buildTracks();

    document.getElementById("goLifecycle").addEventListener("click", openOverlay);
    document.getElementById("goTracks").addEventListener("click", () => showScreen("tracks"));
    document.getElementById("backBtn").addEventListener("click", () => showScreen("home"));
    document.getElementById("ovClose").addEventListener("click", closeOverlay);

    document.getElementById("prevBtn").addEventListener("click", () => { if (cur > 0) setStep(cur - 1); });
    document.getElementById("nextBtn").addEventListener("click", () => {
      if (cur < STEPS.length - 1) setStep(cur + 1);
      else { closeOverlay(); showScreen("tracks"); }
    });
    document.addEventListener("keydown", (e) => {
      const ov = document.getElementById("lcOverlay");
      if (e.key === "Escape" && ov.classList.contains("open")) return closeOverlay();
      if (!ov.classList.contains("open")) return;
      if (e.key === "ArrowLeft" && cur < STEPS.length - 1) setStep(cur + 1);
      else if (e.key === "ArrowRight" && cur > 0) setStep(cur - 1);
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
