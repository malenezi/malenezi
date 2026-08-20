/* =====================================================================
   SDAIA Academy — shared UI runtime  (assets/sdaia-ui.js)
   Load (non-deferred) in the document head, after assets/sdaia-icons.js:
     script src="…/assets/sdaia-icons.js"  then  script src="…/assets/sdaia-ui.js"
   (the file is also inlined verbatim into the single-file Success Stories bundle, so it must
   never contain a literal closing script tag)
   Provides: window.SDAIA = { lang, theme, t(ar,en), n(num), icon(name),
     translate(root), setLang(l), setTheme(d), onLang(fn), countUp(el,v) }
   Builds the shared header/drawer/footer/back-to-top, applies the saved
   language + theme before first paint, and translates [data-ar]/[data-en].
   ===================================================================== */
(function(){
  'use strict';
  var doc = document, root = doc.documentElement;

  /* ---- locate the Academy root folder from this script's own URL ---- */
  var ROOT = '';
  try{
    var src = (doc.currentScript && doc.currentScript.src) || '';
    var m = src.match(/^(.*?)assets\/sdaia-ui\.js/);
    if (m) ROOT = m[1];
  }catch(e){}
  if (!ROOT){ var rootAttr = root.getAttribute('data-root'); if (rootAttr !== null) ROOT = rootAttr; }

  /* ---- persisted preferences ---- */
  function get(k){ try{ return localStorage.getItem(k); }catch(e){ return null; } }
  function set(k,v){ try{ localStorage.setItem(k,v); }catch(e){} }
  var lang = get('sdaia_lang') === 'en' ? 'en' : 'ar';
  var dark = get('sdaia_theme') === 'd';
  /* optional URL overrides — ?lang=en|ar  ?theme=dark|light — persisted so shared links open in the intended language */
  try{
    var q = new URLSearchParams(location.search);
    if (q.get('lang') === 'en' || q.get('lang') === 'ar'){ lang = q.get('lang'); set('sdaia_lang', lang); }
    if (q.get('theme') === 'dark' || q.get('theme') === 'light'){ dark = q.get('theme') === 'dark'; set('sdaia_theme', dark ? 'd' : 'l'); }
  }catch(e){}
  var listeners = [];

  function applyLangAttrs(){
    root.setAttribute('lang', lang);
    root.setAttribute('dir', lang === 'ar' ? 'rtl' : 'ltr');
  }
  function applyTheme(){
    if (dark) root.setAttribute('data-theme','dark'); else root.removeAttribute('data-theme');
    var meta = doc.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', dark ? '#0A1628' : '#0B2A4E');
  }
  applyLangAttrs(); applyTheme();

  /* ---- helpers ---- */
  var NF = new Intl.NumberFormat('en-US');
  function t(ar,en){ return lang === 'ar' ? ar : en; }
  function n(v){ return NF.format(v); }
  function icon(name, cls){ return '<svg class="i' + (cls ? ' ' + cls : '') + '" aria-hidden="true" focusable="false"><use href="#i-' + name + '"/></svg>'; }
  function esc(s){ return String(s == null ? '' : s).replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }

  function translate(scope){
    scope = scope || doc;
    var isAr = lang === 'ar';
    var nodes = scope.querySelectorAll('[data-ar][data-en]');
    for (var i = 0; i < nodes.length; i++){
      var el = nodes[i], v = isAr ? el.getAttribute('data-ar') : el.getAttribute('data-en');
      if (el.tagName === 'TITLE') { el.textContent = v; continue; }
      el.innerHTML = v;
    }
    var ph = scope.querySelectorAll('[data-ar-placeholder]');
    for (i = 0; i < ph.length; i++) ph[i].setAttribute('placeholder', isAr ? ph[i].getAttribute('data-ar-placeholder') : ph[i].getAttribute('data-en-placeholder'));
    var al = scope.querySelectorAll('[data-ar-label]');
    for (i = 0; i < al.length; i++) al[i].setAttribute('aria-label', isAr ? al[i].getAttribute('data-ar-label') : al[i].getAttribute('data-en-label'));
    var ti = scope.querySelectorAll('[data-ar-title]');
    for (i = 0; i < ti.length; i++) ti[i].setAttribute('title', isAr ? ti[i].getAttribute('data-ar-title') : ti[i].getAttribute('data-en-title'));
    var langBtns = doc.querySelectorAll('.sd-lang');
    for (i = 0; i < langBtns.length; i++){
      langBtns[i].innerHTML = icon('languages','i-sm') + '<span>' + (isAr ? 'English' : 'العربية') + '</span>';
      langBtns[i].setAttribute('aria-label', isAr ? 'Switch to English' : 'التبديل إلى العربية');
      langBtns[i].setAttribute('lang', isAr ? 'en' : 'ar');
    }
    var themeBtns = doc.querySelectorAll('.sd-theme');
    for (i = 0; i < themeBtns.length; i++) themeBtns[i].setAttribute('aria-label', isAr ? 'تبديل الوضع الليلي' : 'Toggle dark mode');
    var menuBtns = doc.querySelectorAll('.sd-menu-btn');
    for (i = 0; i < menuBtns.length; i++) menuBtns[i].setAttribute('aria-label', isAr ? 'القائمة' : 'Menu');
  }

  /* keep shared links honest: reflect an explicit choice back into the URL if that param is present */
  function syncUrlParam(name, value){
    try{
      var u = new URL(location.href);
      if (u.searchParams.has(name)){ u.searchParams.set(name, value); history.replaceState(null, '', u); }
    }catch(e){}
  }
  function syncThemeButtons(){
    var btns = doc.querySelectorAll('.sd-theme');
    for (var i = 0; i < btns.length; i++) btns[i].setAttribute('aria-pressed', String(dark));
  }
  function setLang(l){
    lang = l === 'en' ? 'en' : 'ar';
    set('sdaia_lang', lang); syncUrlParam('lang', lang);
    applyLangAttrs(); translate(); tagLangParts();
    for (var i = 0; i < listeners.length; i++){ try{ listeners[i](lang); }catch(e){ console.error(e); } }
    initSubnav();
    doc.dispatchEvent(new CustomEvent('sdaia:lang', { detail: { lang: lang } }));
  }
  function setTheme(d){ dark = !!d; set('sdaia_theme', dark ? 'd' : 'l'); syncUrlParam('theme', dark ? 'dark' : 'light'); applyTheme(); syncThemeButtons(); doc.dispatchEvent(new CustomEvent('sdaia:theme', { detail: { dark: dark } })); }

  /* language-of-parts: content rendered in the opposite language is marked with .ar/.en —
     mirror that as a lang attribute so screen readers switch voices correctly */
  function tagLangParts(scope){
    var els = (scope || doc).querySelectorAll('.ar:not([lang])');
    for (var i = 0; i < els.length; i++) els[i].setAttribute('lang', 'ar');
    els = (scope || doc).querySelectorAll('.en:not([lang])');
    for (i = 0; i < els.length; i++) els[i].setAttribute('lang', 'en');
  }

  /* animated counter (respects reduced motion) */
  function countUp(el, target, dur){
    dur = dur || 1300;
    var fmt = el.getAttribute('data-raw') === '1' ? function(v){ return String(v); } : n;
    if (matchMedia('(prefers-reduced-motion: reduce)').matches){ el.textContent = fmt(target); return; }
    var t0 = performance.now();
    (function step(now){
      var p = Math.min((now - t0) / dur, 1);
      el.textContent = fmt(Math.round(target * (1 - Math.pow(1 - p, 3))));
      if (p < 1) requestAnimationFrame(step);
    })(t0);
  }
  function observeCounters(scope){
    var els = [].slice.call((scope || doc).querySelectorAll('[data-count]:not([data-counted])'));
    if (!els.length) return;
    els.forEach(function(el){ el.setAttribute('data-counted','1'); });
    if (!('IntersectionObserver' in window)){ els.forEach(function(el){ el.textContent = n(+el.getAttribute('data-count')); }); return; }
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(en){ if (en.isIntersecting){ countUp(en.target, +en.target.getAttribute('data-count')); io.unobserve(en.target); } });
    }, { threshold: .35 });
    els.forEach(function(el){ io.observe(el); });
  }

  /* ---- site map (one source of truth for the global navigation) ---- */
  var SITES = [
    { id:'portal',    ar:'البوابة',           en:'Portal',           href:'index.html',                          icon:'layout-grid' },
    { id:'about',     ar:'عن الأكاديمية',     en:'About',            href:'about.html',                          icon:'landmark' },
    { id:'catalog',   ar:'الكاتالوج التدريبي', en:'Training Catalog', href:'Catalog/index.html',                  icon:'book-open' },
    { id:'graduates', ar:'الخريجون',          en:'Graduates',        href:'Graduates/index.html',                icon:'graduation-cap' },
    { id:'stories',   ar:'قصص النجاح',        en:'Success Stories',  href:'SuccessStories/website/index.html',   icon:'award' }
  ];
  var RESOURCES = [
    { ar:'كاتالوج المسارات التعليمية (Excel)', en:'Learning Paths Catalog (Excel)', href:'Catalog/SDAIA_Learning_Paths_Catalog.xlsx' },
    { ar:'كاتالوج التعلم v2 (PDF)',            en:'Learning Catalog v2 (PDF)',      href:'Catalog/TrainingMaterials/Programs%20Details%20and%20Paths/SDAIA_Learning_Catalog_v2.pdf' },
    { ar:'قاعدة بيانات الخريجين (Excel)',      en:'Graduates Database (Excel)',     href:'Graduates/Graduates_Database.xlsx' },
    { ar:'الحقائب التدريبية للمدرّبين',         en:'Instructor training materials',  href:'Catalog/TrainingMaterials/' },
    { ar:'ملف تعريف الأكاديمية',               en:'Academy profile',                href:'Academy_Profile.md' }
  ];

  function buildHeader(){
    var hd = doc.querySelector('.sd-header');
    if (!hd || hd.getAttribute('data-built')) return;
    hd.setAttribute('data-built','1');
    var active = hd.getAttribute('data-active') || '';
    var subAr = hd.getAttribute('data-sub-ar') || '', subEn = hd.getAttribute('data-sub-en') || '';
    var links = SITES.map(function(s){
      return '<a href="' + ROOT + s.href + '" class="' + (s.id === active ? 'is-active' : '') + '"' + (s.id === active ? ' aria-current="page"' : '') + ' data-ar="' + s.ar + '" data-en="' + s.en + '"></a>';
    }).join('');
    hd.innerHTML =
      '<div class="sd-container sd-header__inner">' +
        '<a class="sd-brand" href="' + ROOT + 'index.html" data-ar-label="أكاديمية سدايا — البوابة الرئيسية" data-en-label="SDAIA Academy — home">' +
          '<img class="sd-brand__logo" src="' + ROOT + 'assets/academy-logo.png" alt="" width="660" height="162">' +
          '<span class="sd-brand__text"><span class="sd-brand__name" data-ar="أكاديمية سدايا" data-en="SDAIA Academy"></span>' +
          (subAr ? '<span class="sd-brand__sub" data-ar="' + esc(subAr) + '" data-en="' + esc(subEn) + '"></span>' : '') + '</span>' +
        '</a>' +
        '<nav class="sd-nav" data-ar-label="التنقل الرئيسي" data-en-label="Main navigation">' + links + '</nav>' +
        '<div class="sd-header__tools">' +
          '<button type="button" class="sd-tool sd-lang"></button>' +
          '<button type="button" class="sd-tool sd-tool--icon sd-theme">' + icon('moon','i-sm i-moon') + icon('sun','i-sm i-sun') + '</button>' +
          '<button type="button" class="sd-tool sd-tool--icon sd-menu-btn" aria-expanded="false" aria-controls="sdDrawer">' + icon('menu','i-sm') + '</button>' +
        '</div>' +
      '</div>';
    var drawer = doc.createElement('div');
    drawer.className = 'sd-drawer'; drawer.id = 'sdDrawer';
    drawer.innerHTML = SITES.map(function(s){
      return '<a href="' + ROOT + s.href + '" class="' + (s.id === active ? 'is-active' : '') + '">' + icon(s.icon,'i-sm') + '<span data-ar="' + s.ar + '" data-en="' + s.en + '"></span></a>';
    }).join('') +
      '<div class="sd-drawer__sep"></div><div class="sd-drawer__row"><button type="button" class="sd-tool sd-lang"></button>' +
      '<button type="button" class="sd-tool sd-tool--icon sd-theme">' + icon('moon','i-sm i-moon') + icon('sun','i-sm i-sun') + '</button></div>';
    hd.insertAdjacentElement('afterend', drawer);

    if (hd.getAttribute('data-solid') === '1') hd.classList.add('is-solid');
    var menuBtn = hd.querySelector('.sd-menu-btn');
    menuBtn.addEventListener('click', function(){
      var open = drawer.classList.toggle('is-open');
      menuBtn.setAttribute('aria-expanded', String(open));
      menuBtn.innerHTML = icon(open ? 'x' : 'menu','i-sm');
      if (open) hd.classList.add('is-solid'); else if (hd.getAttribute('data-solid') !== '1') hd.classList.remove('is-solid');
    });
    drawer.addEventListener('click', function(e){ if (e.target.closest('a')) { drawer.classList.remove('is-open'); menuBtn.setAttribute('aria-expanded','false'); menuBtn.innerHTML = icon('menu','i-sm'); if (hd.getAttribute('data-solid') !== '1') hd.classList.remove('is-solid'); } });
    doc.addEventListener('click', function(e){ if (!e.target.closest('.sd-drawer') && !e.target.closest('.sd-menu-btn') && drawer.classList.contains('is-open')){ drawer.classList.remove('is-open'); menuBtn.setAttribute('aria-expanded','false'); menuBtn.innerHTML = icon('menu','i-sm'); if (hd.getAttribute('data-solid') !== '1') hd.classList.remove('is-solid'); } });
    doc.addEventListener('keydown', function(e){ if (e.key === 'Escape' && drawer.classList.contains('is-open')){ menuBtn.click(); menuBtn.focus(); } });

    function onScroll(){ hd.classList.toggle('is-scrolled', window.scrollY > 24); }
    window.addEventListener('scroll', onScroll, { passive:true }); onScroll();
  }

  function buildFooter(){
    var ft = doc.querySelector('.sd-footer');
    if (!ft || ft.getAttribute('data-built')) return;
    ft.setAttribute('data-built','1');
    var noteAr = ft.getAttribute('data-note-ar') || '', noteEn = ft.getAttribute('data-note-en') || '';
    var extra = ft.innerHTML; // page-provided bottom-right slot (optional)
    ft.innerHTML =
      '<div class="sd-container">' +
        '<div class="sd-footer__top">' +
          '<div class="sd-footer__brand"><img src="' + ROOT + 'assets/academy-logo.png" alt="SDAIA Academy" width="660" height="162">' +
            '<p data-ar="أكاديمية سدايا — الأكاديمية الوطنية لبناء القدرات في مجالي البيانات والذكاء الاصطناعي، إحدى مبادرات الهيئة السعودية للبيانات والذكاء الاصطناعي (سدايا)." data-en="SDAIA Academy — the national academy for building capability in data and artificial intelligence, an initiative of the Saudi Data &amp; AI Authority (SDAIA)."></p></div>' +
          '<div><h2 class="sd-footer__h" data-ar="المنصات" data-en="Platforms"></h2><ul>' + SITES.map(function(s){ return '<li><a href="' + ROOT + s.href + '" data-ar="' + s.ar + '" data-en="' + s.en + '"></a></li>'; }).join('') + '</ul></div>' +
          '<div><h2 class="sd-footer__h" data-ar="الموارد" data-en="Resources"></h2><ul>' + RESOURCES.map(function(r){ return '<li><a href="' + ROOT + r.href + '" data-ar="' + r.ar + '" data-en="' + r.en + '"></a></li>'; }).join('') + '</ul></div>' +
        '</div>' +
        '<div class="sd-footer__bottom"><span' + (noteAr ? ' data-ar="' + esc(noteAr) + '" data-en="' + esc(noteEn) + '"' : '') + '></span>' +
          '<span>' + (extra || '<a href="#top" data-ar="العودة إلى الأعلى" data-en="Back to top"></a>') + '</span></div>' +
      '</div>';
  }

  function buildToTop(){
    if (doc.querySelector('.sd-totop')) return;
    var b = doc.createElement('button');
    b.type = 'button'; b.className = 'sd-totop'; b.innerHTML = icon('arrow-up');
    b.setAttribute('data-ar-label','العودة إلى الأعلى'); b.setAttribute('data-en-label','Back to top');
    doc.body.appendChild(b);
    b.addEventListener('click', function(){ window.scrollTo({ top:0, behavior:'smooth' }); });
    function onScroll(){ b.classList.toggle('is-visible', window.scrollY > 560); }
    window.addEventListener('scroll', onScroll, { passive:true }); onScroll();
  }

  /* scroll-spy for in-page sub navigation */
  var spyIO = null;
  function initSubnav(){
    var nav = doc.querySelector('.sd-subnav[data-spy]');
    if (!nav || !('IntersectionObserver' in window)) return;
    if (spyIO){ spyIO.disconnect(); spyIO = null; }
    var links = [].slice.call(nav.querySelectorAll('a[href^="#"]'));
    var map = {}; links.forEach(function(a){ var id = a.getAttribute('href').slice(1); var s = doc.getElementById(id); if (s) map[id] = a; });
    var current = null;
    function activate(id){ if (current === id) return; current = id; links.forEach(function(a){ a.classList.toggle('is-active', a.getAttribute('href') === '#' + id); }); var a = map[id]; if (a && a.scrollIntoView){ try{ a.scrollIntoView({ block:'nearest', inline:'center', behavior:'smooth' }); }catch(e){} } }
    spyIO = new IntersectionObserver(function(entries){
      entries.forEach(function(en){ if (en.isIntersecting) activate(en.target.id); });
    }, { rootMargin: '-' + (parseInt(getComputedStyle(root).getPropertyValue('--header-h')) + 70) + 'px 0px -55% 0px', threshold: 0 });
    Object.keys(map).forEach(function(id){ spyIO.observe(doc.getElementById(id)); });
  }

  function wireTools(){
    doc.addEventListener('click', function(e){
      var lb = e.target.closest('.sd-lang'); if (lb){ setLang(lang === 'ar' ? 'en' : 'ar'); return; }
      var tb = e.target.closest('.sd-theme'); if (tb){ setTheme(!dark); return; }
    });
  }

  function init(){
    if (window.SDAIA_ICONS && !doc.querySelector('.sd-sprite')){ var d = doc.createElement('div'); d.innerHTML = window.SDAIA_ICONS; doc.body.insertBefore(d.firstChild, doc.body.firstChild); }
    buildHeader(); buildFooter(); buildToTop(); wireTools(); translate(); syncThemeButtons(); tagLangParts(); initSubnav(); observeCounters();
    /* keep lang-of-parts tags current for content rendered later (registry pages, filters, modals) */
    if ('MutationObserver' in window){
      var mo = new MutationObserver(function(muts){
        for (var i = 0; i < muts.length; i++) if (muts[i].addedNodes.length){ tagLangParts(); return; }
      });
      mo.observe(doc.body, { childList: true, subtree: true });
    }
  }
  if (doc.readyState === 'loading') doc.addEventListener('DOMContentLoaded', init); else init();

  window.SDAIA = {
    get lang(){ return lang; }, get dark(){ return dark; }, root: ROOT,
    t: t, n: n, icon: icon, esc: esc, translate: translate, setLang: setLang, setTheme: setTheme,
    onLang: function(fn){ listeners.push(fn); }, countUp: countUp, observeCounters: observeCounters,
    tagLangParts: tagLangParts, refreshSubnav: initSubnav
  };
})();
