/* ============================================================
   أكاديمية سدايا · دورة حياة البرامج (النسخة الثانية)
   نافذة منبثقة بملء الشاشة · تفرّع جانبي · مسارات بتفاصيل
   ============================================================ */
(function () {
  "use strict";
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- أيقونات SVG رسمية ---------- */
  const P = {
    cycle:'<path d="M20.5 12a8.5 8.5 0 1 1-2.4-5.9"/><path d="M20.5 4.5V11h-6.5"/>',
    route:'<circle cx="6" cy="18" r="2.4"/><circle cx="18" cy="6" r="2.4"/><path d="M8.2 16.8C14 15.5 15.5 13 15.6 8.2"/><path d="M6 15.6V9a3 3 0 0 1 3-3h2.8"/>',
    s1:'<circle cx="12" cy="12" r="2.2"/><path d="M12 9.8a4 4 0 0 1 4 4"/><path d="M12 5.8a8 8 0 0 1 8 8"/><path d="M12 12a4 4 0 0 0-4 4"/>',
    s2:'<circle cx="11" cy="11" r="6.2"/><path d="M20.5 20.5l-4.7-4.7"/><path d="M9 11h4M11 9v4"/>',
    s3:'<path d="M4 20l1-4 9-9 3 3-9 9-4 1z"/><path d="M13.5 6.5l3 3"/>',
    s4:'<rect x="3" y="4.5" width="18" height="13" rx="2"/><path d="M10.5 9l4 2.7-4 2.7z"/><path d="M8 21h8"/>',
    s5:'<rect x="6" y="4" width="12" height="16.5" rx="2"/><path d="M9 4.5h6V7H9z"/><path d="M9 13l2 2 4-4"/>',
    s6:'<path d="M3.5 17l6-6 4 4 7-7"/><path d="M16.5 8h4.5v4.5"/>',
    s7:'<path d="M20.5 12a8.5 8.5 0 1 1-2.4-5.9"/><path d="M20.5 4.5V11h-6.5"/>',
    cal:'<rect x="4" y="5" width="16" height="15.5" rx="2"/><path d="M4 9.5h16"/><path d="M9 3v4M15 3v4"/>',
    cap:'<path d="M3 9l9-4 9 4-9 4-9-4z"/><path d="M6.5 11v4.2c0 1.4 3 2.8 5.5 2.8s5.5-1.4 5.5-2.8V11"/>',
    net:'<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c3 2.6 3 14.4 0 17M12 3.5c-3 2.6-3 14.4 0 17"/>',
    cpu:'<rect x="7" y="7" width="10" height="10" rx="2"/><rect x="10" y="10" width="4" height="4" rx="1"/><path d="M10 3.5v3M14 3.5v3M10 17.5v3M14 17.5v3M3.5 10h3M3.5 14h3M17.5 10h3M17.5 14h3"/>',
    db:'<ellipse cx="12" cy="6" rx="7" ry="3"/><path d="M5 6v6c0 1.6 3.1 3 7 3s7-1.4 7-3V6"/><path d="M5 12v6c0 1.6 3.1 3 7 3s7-1.4 7-3v-6"/>',
    book:'<path d="M5 4.5h10.5a2 2 0 0 1 2 2V20H7a2 2 0 0 1-2-2z"/><path d="M8.5 4.5V20"/>',
    layers:'<path d="M12 3.5l8.5 4.7-8.5 4.7-8.5-4.7z"/><path d="M3.5 13l8.5 4.7 8.5-4.7"/>',
    gear:'<circle cx="12" cy="12" r="3.2"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2 2M16.4 16.4l2 2M18.4 5.6l-2 2M7.6 16.4l-2 2"/>',
    spark:'<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/>',
    bars:'<path d="M5 20v-7M11 20V5M17 20v-10"/><path d="M3.5 20h17"/>',
    flow:'<rect x="3" y="4" width="6" height="6" rx="1"/><rect x="15" y="14" width="6" height="6" rx="1"/><path d="M9 7h6a2 2 0 0 1 2 2v5"/>',
    badge:'<circle cx="12" cy="9" r="5.4"/><path d="M9 13.4L7.4 21l4.6-2.6L16.6 21 15 13.4"/><path d="M9.7 9l1.6 1.6 3-3.2"/>',
    // أيقونات التفاصيل
    inbox:'<path d="M4 13h4l1.5 3h5L16 13h4"/><path d="M4 13l2.4-8.2A1 1 0 0 1 7.4 4h9.2a1 1 0 0 1 1 .8L20 13v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1z"/>',
    act:'<path d="M3 12h4l2.4 7 4-15 2.3 8H21"/>',
    box:'<path d="M12 3l8 4.5v9L12 21l-8-4.5v-9z"/><path d="M4 7.5l8 4.5 8-4.5"/><path d="M12 12v9"/>',
    gauge:'<path d="M4 18a8 8 0 1 1 16 0"/><path d="M12 18l4.5-5.5"/><circle cx="12" cy="18" r="1.5"/>'
  };
  const svg = (p, cls) => `<svg class="${cls||'ic'}" viewBox="0 0 24 24">${p}</svg>`;

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
    ov.classList.add("open"); document.body.style.overflow = "hidden";
    setStep(0);
  }
  function closeOverlay() {
    document.getElementById("lcOverlay").classList.remove("open");
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
      ? `مسارات التدريب <svg class="ic" viewBox="0 0 24 24">${P.route}</svg>`
      : `التالي <svg class="ic" viewBox="0 0 24 24"><path d="M15 6l-6 6 6 6"/></svg>`;
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
