/* =========================================================
   SDAIA Academy — Graduate Success Stories · Interactions
   (vanilla JS — stories grouped by graduation year; bilingual UI
   on top of the shared runtime in ../../assets/sdaia-ui.js)
   ========================================================= */
'use strict';

const $ = (sel, root = document) => root.querySelector(sel);
const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];
const T = (ar, en) => SDAIA.t(ar, en);
const N = v => SDAIA.n(v);
const I = (name, cls) => SDAIA.icon(name, cls);
const esc = s => SDAIA.esc(s);

const state = { query: '', year: 'all' };

/* ---------- Hero KPI tiles ---------- */
function renderStats() {
  $('#heroStats').innerHTML = SITE_STATS.map(s => `
    <div class="sd-kpi">
      <span class="sd-iconbox ${s.tint || 'tint-blue'}">${I(s.icon || 'star')}</span>
      <div class="sd-kpi__num" data-count="${s.value}">0</div>
      <div class="sd-kpi__label">${T(s.label, s.labelEn)}</div>
      <div class="sd-kpi__note">${T(s.note, s.noteEn)}</div>
    </div>`).join('');
  SDAIA.observeCounters($('#heroStats'));
}

/* ---------- Year navigation + chips ---------- */
function yearLabel(y) { return T(y.label, y.labelEn); }

function renderYearNav() {
  $('#yearNav').innerHTML = YEARS.map(y => `<a href="#year-${y.id}" data-year="${y.id}">${I('calendar-days')}<span>${yearLabel(y)}</span></a>`).join('');
}
function renderChips() {
  const wrap = $('#yearChips');
  wrap.innerHTML = [{ id: 'all', label: 'كل الدفعات', labelEn: 'All cohorts' }, ...YEARS].map(y => `
    <button type="button" class="sd-chip" data-year="${y.id}" aria-pressed="${String(y.id) === String(state.year)}">${yearLabel(y)}</button>`).join('');
}
function selectYear(year) {
  state.year = String(year);
  $$('.sd-chip', $('#yearChips')).forEach(ch => ch.setAttribute('aria-pressed', String(ch.dataset.year === state.year)));
  renderStories();
}
$('#yearChips').addEventListener('click', e => {
  const chip = e.target.closest('.sd-chip');
  if (chip) selectYear(chip.dataset.year);
});
/* the cohort sub-nav doubles as a selector, so its targets always exist after a click */
$('#yearNav').addEventListener('click', e => {
  const a = e.target.closest('a[data-year]');
  if (!a) return;
  const id = a.getAttribute('href').slice(1);
  if (a.getAttribute('aria-disabled') === 'true') { e.preventDefault(); return; }
  if (!document.getElementById(id)) {
    e.preventDefault();
    selectYear(a.dataset.year);
    const s = document.getElementById(id);
    if (s) s.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
});

/* ---------- Search ---------- */
let searchTimer;
$('#searchInput').addEventListener('input', e => {
  clearTimeout(searchTimer);
  searchTimer = setTimeout(() => { state.query = e.target.value.trim(); renderStories(); }, 160);
});

/* ---------- Stories grouped by year ---------- */
const storiesWrap = $('#storiesByYear');
const catLabel = id => { const c = CATEGORIES.find(x => x.id === id) || {}; return T(c.label, c.labelEn) || ''; };

function initialsOf(name) { return name.replace('د. ', '').trim().charAt(0); }

function countLabel(n) {
  if (SDAIA.lang === 'en') return n === 1 ? '1 story' : `${N(n)} stories`;
  if (n === 1) return 'قصة واحدة';
  if (n === 2) return 'قصتان';
  if (n <= 10) return `${N(n)} قصص`;
  return `${N(n)} قصة`;
}

function filteredStories() {
  const q = state.query.toLowerCase();
  return STORIES.filter(s => {
    const inYear = state.year === 'all' || s.year === +state.year;
    if (!inYear) return false;
    if (!q) return true;
    return [s.name, s.nameEn, s.org, s.role, s.program, s.impact].join(' ').toLowerCase().includes(q);
  });
}

/* Story content is Arabic-source; in the English layout it is rendered inside an RTL block (.ar)
   and the English name leads when available. */
function nameBlock(s, tag) {
  const en = SDAIA.lang === 'en';
  const primary = en && s.nameEn ? `<span class="en">${esc(s.nameEn)}</span>` : `<span class="ar">${esc(s.name)}</span>`;
  const alt = en && s.nameEn ? `<span class="ar">${esc(s.name)}</span>` : (s.nameEn ? `<span class="en">${esc(s.nameEn)}</span>` : '');
  return { primary, alt };
}

function cardHTML(s) {
  const media = s.photo
    ? `<img class="photo" src="${s.photo}" alt="${esc(T('صورة', 'Photo of') + ' ' + s.name)}" loading="lazy" decoding="async" width="560" height="385" onerror="this.outerHTML='<div class=&quot;avatar-fallback&quot; aria-hidden=&quot;true&quot;>${initialsOf(s.name)}</div>'">`
    : `<div class="avatar-fallback" aria-hidden="true">${initialsOf(s.name)}</div>`;
  const org = `<div class="card-org ar">${s.orgLogo ? `<img src="${s.orgLogo}" alt="" loading="lazy" decoding="async">` : I('building-2', 'i-sm muted')}<span>${esc(s.org)}</span></div>`;
  const links = s.links.slice(0, 1).map(l =>
    `<a class="ext-link" href="${l.url}" target="_blank" rel="noopener" aria-label="${esc(l.label)} — ${esc(s.name)} (${T('يفتح في نافذة جديدة', 'opens in a new window')})" title="${esc(l.label)}">${I('external-link')}</a>`).join('');
  const nm = nameBlock(s);
  return `
  <article class="sd-card story-card">
    <div class="card-media">
      ${media}
      <span class="rank-badge">${T('دفعة', 'Class of')} ${s.year}</span>
      <span class="cat-badge">${catLabel(s.category)}</span>
    </div>
    <div class="card-body">
      <h3>${nm.primary}</h3>
      ${nm.alt ? `<span class="card-name-alt">${nm.alt}</span>` : ''}
      <p class="card-role ar">${esc(s.role)}</p>
      ${org}
      <p class="card-impact ar">${esc(s.impact)}</p>
      <div class="card-meta"><span class="sd-tag ar">${I('calendar-days', 'i-sm')}${esc(s.period)}</span></div>
      <div class="card-actions">
        <button class="sd-btn sd-btn--primary sd-btn--sm btn-read" data-id="${s.id}" aria-haspopup="dialog">${I('book-open')}<span>${T('اقرأ القصة كاملة', 'Read the full story')}</span></button>
        ${links}
      </div>
    </div>
  </article>`;
}

function renderStories() {
  const list = filteredStories();
  const html = YEARS.map(y => {
    const items = list.filter(s => s.year === y.id);
    if (!items.length) return '';
    return `
    <section class="year-group" id="year-${y.id}" aria-label="${yearLabel(y)}">
      <div class="year-head">
        <div class="year-title-wrap">
          <h3 class="year-title"><span>${T('دفعة', 'Class of')}</span><span class="year-num">${y.id}</span></h3>
          <p class="year-desc">${T(y.desc, y.descEn)}</p>
        </div>
        <span class="sd-tag sd-tag--brand year-count">${countLabel(items.length)}</span>
      </div>
      <div class="cards-grid">${items.map(cardHTML).join('')}</div>
    </section>`;
  }).join('');
  storiesWrap.innerHTML = html;
  // a cohort emptied by the current search is unreachable — mark its sub-nav link disabled
  const q = state.query.toLowerCase();
  const hasAny = y => STORIES.some(s => s.year === y &&
    (!q || [s.name, s.nameEn, s.org, s.role, s.program, s.impact].join(' ').toLowerCase().includes(q)));
  $$('#yearNav a[data-year]').forEach(a => {
    const ok = hasAny(+a.dataset.year);
    a.classList.toggle('is-off', !ok);
    if (ok) a.removeAttribute('aria-disabled'); else a.setAttribute('aria-disabled', 'true');
  });
  if (SDAIA.refreshSubnav) SDAIA.refreshSubnav();
  $('#noResults').hidden = list.length > 0;
  $('#resultsCount').innerHTML = list.length === STORIES.length
    ? T(`عرض جميع القصص — <b>${N(list.length)}</b> قصة عبر <b>${N(YEARS.length)}</b> دفعات`, `Showing all stories — <b>${N(list.length)}</b> stories across <b>${N(YEARS.length)}</b> cohorts`)
    : T(`<b>${N(list.length)}</b> من <b>${N(STORIES.length)}</b> قصة`, `<b>${N(list.length)}</b> of <b>${N(STORIES.length)}</b> stories`);
}
storiesWrap.addEventListener('click', e => {
  const btn = e.target.closest('.btn-read');
  if (btn) openModal(btn.dataset.id);
});

/* ---------- Modal ---------- */
const modal = $('#storyModal');
const modalContent = $('#modalContent');
let lastFocused = null;

function openModal(id) {
  const s = STORIES.find(x => x.id === id);
  if (!s) return;
  lastFocused = document.activeElement;
  const photo = s.photo
    ? `<img class="m-photo" src="${s.photo}" alt="${esc(T('صورة', 'Photo of') + ' ' + s.name)}" onerror="this.outerHTML='<div class=&quot;m-avatar&quot; aria-hidden=&quot;true&quot;>${initialsOf(s.name)}</div>'">`
    : `<div class="m-avatar" aria-hidden="true">${initialsOf(s.name)}</div>`;
  const nm = nameBlock(s);
  modalContent.innerHTML = `
    <div class="modal-head">
      ${photo}
      <div class="m-head-txt">
        <span class="m-rank">${T('دفعة', 'Class of')} ${s.year} · ${catLabel(s.category)}</span>
        <h2 id="modalName">${nm.primary}</h2>
        ${nm.alt ? `<span class="m-name-alt">${nm.alt}</span>` : ''}
        <p class="m-role ar">${esc(s.role)}</p>
      </div>
    </div>
    <div class="modal-body">
      <div class="m-org ar">${s.orgLogo ? `<img src="${s.orgLogo}" alt="${esc(T('شعار', 'Logo of') + ' ' + s.org)}">` : ''}<span>${esc(s.org)}</span></div>
      <div class="sd-dl">
        <div><div class="k">${T('سنة التخرج', 'Graduation year')}</div><div class="v num">${s.year}</div></div>
        <div><div class="k">${T('البرنامج', 'Program')}</div><div class="v ar">${esc(s.program)}</div></div>
        <div><div class="k">${T('الفترة الزمنية', 'Period')}</div><div class="v ar">${esc(s.period)}</div></div>
      </div>
      <h3>${I('book-open')}${T('القصة', 'The story')}</h3>
      <p class="m-story ar">${esc(s.story)}</p>
      <h3>${I('trophy')}${T('أبرز الإنجازات', 'Highlights')}</h3>
      <ul class="m-achievements ar">${s.achievements.map(a => `<li>${I('circle-check')}<span>${esc(a)}</span></li>`).join('')}</ul>
      ${s.links.length ? `<h3>${I('link')}${T('روابط موثّقة', 'Verified sources')}</h3>
      <div class="m-links">${s.links.map(l => `<a class="sd-link-pill" href="${l.url}" target="_blank" rel="noopener">${I('external-link')}<span class="ar">${esc(l.label)}</span></a>`).join('')}</div>` : ''}
    </div>`;
  modal.hidden = false;
  document.body.classList.add('sd-lock');
  requestAnimationFrame(() => { $('.sd-modal__close', modal).focus(); });
}

function closeModal() {
  modal.hidden = true;
  document.body.classList.remove('sd-lock');
  if (lastFocused) lastFocused.focus();
}

modal.addEventListener('click', e => { if (e.target.closest('[data-close]')) closeModal(); });
document.addEventListener('keydown', e => {
  if (modal.hidden) return;
  if (e.key === 'Escape') closeModal();
  if (e.key === 'Tab') { // focus trap
    const focusables = $$('button, a[href], [tabindex]:not([tabindex="-1"])', modal).filter(el => !el.hidden);
    if (!focusables.length) return;
    const first = focusables[0], last = focusables[focusables.length - 1];
    if (e.shiftKey && document.activeElement === first) { last.focus(); e.preventDefault(); }
    else if (!e.shiftKey && document.activeElement === last) { first.focus(); e.preventDefault(); }
  }
});

/* ---------- Boot + re-render on language change ---------- */
function renderAll() { renderStats(); renderYearNav(); renderChips(); renderStories(); }
renderAll();
SDAIA.onLang(() => { renderAll(); if (!modal.hidden) closeModal(); });
