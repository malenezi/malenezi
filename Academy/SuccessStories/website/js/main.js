/* =========================================================
   SDAIA Academy — Graduate Success Stories · Interactions
   (vanilla JS — القصص مرتبة حسب سنة التخرج)
   ========================================================= */
'use strict';

const $ = (sel, root = document) => root.querySelector(sel);
const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];
const AR_NUM = new Intl.NumberFormat('ar-SA');

const state = { query: '', year: 'all' };

/* ---------- Header / nav ---------- */
const header = $('#siteHeader');
const navToggle = $('#navToggle');
const navMenu = $('#navMenu');

window.addEventListener('scroll', () => {
  header.classList.toggle('scrolled', window.scrollY > 40);
  $('#toTop').hidden = window.scrollY < 600;
}, { passive: true });

navToggle.addEventListener('click', () => {
  const open = navMenu.classList.toggle('open');
  navToggle.setAttribute('aria-expanded', String(open));
  navToggle.setAttribute('aria-label', open ? 'إغلاق القائمة' : 'فتح القائمة');
});
navMenu.addEventListener('click', e => {
  if (e.target.tagName === 'A') {
    navMenu.classList.remove('open');
    navToggle.setAttribute('aria-expanded', 'false');
  }
});

$('#toTop').addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

/* ---------- Reveal on scroll ---------- */
const revealIO = new IntersectionObserver(entries => {
  for (const en of entries) if (en.isIntersecting) { en.target.classList.add('visible'); revealIO.unobserve(en.target); }
}, { threshold: 0.12 });
$$('.reveal').forEach(el => revealIO.observe(el));

/* ---------- Animated counters ---------- */
function animateCount(el, target, dur = 1400) {
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduced) { el.textContent = AR_NUM.format(target); return; }
  const t0 = performance.now();
  const step = now => {
    const p = Math.min((now - t0) / dur, 1);
    el.textContent = AR_NUM.format(Math.round(target * (1 - Math.pow(1 - p, 3))));
    if (p < 1) requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
}

/* ---------- Hero stats ---------- */
const heroStats = $('#heroStats');
heroStats.innerHTML = SITE_STATS.map(s => `
  <div class="hero-stat">
    <dt>${s.label}<span class="stat-note">${s.note}</span></dt>
    <dd data-count="${s.value}">0</dd>
  </div>`).join('');

const statsIO = new IntersectionObserver(entries => {
  for (const en of entries) if (en.isIntersecting) {
    $$('[data-count]', en.target).forEach(el => animateCount(el, +el.dataset.count));
    statsIO.unobserve(en.target);
  }
}, { threshold: 0.4 });
statsIO.observe(heroStats);

/* ---------- Year chips ---------- */
const chipsWrap = $('#yearChips');
chipsWrap.innerHTML = [{ id: 'all', label: 'كل الدفعات' }, ...YEARS].map(y => `
  <button class="chip" role="tab" data-year="${y.id}" aria-selected="${y.id === 'all'}">${y.label}</button>`).join('');
chipsWrap.addEventListener('click', e => {
  const chip = e.target.closest('.chip');
  if (!chip) return;
  state.year = chip.dataset.year;
  $$('.chip', chipsWrap).forEach(ch => ch.setAttribute('aria-selected', String(ch === chip)));
  renderStories();
});

/* ---------- Search ---------- */
let searchTimer;
$('#searchInput').addEventListener('input', e => {
  clearTimeout(searchTimer);
  searchTimer = setTimeout(() => { state.query = e.target.value.trim(); renderStories(); }, 160);
});

/* ---------- Stories grouped by year ---------- */
const storiesWrap = $('#storiesByYear');
const catLabel = id => (CATEGORIES.find(c => c.id === id) || {}).label || '';
const EXT_ICON = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><path d="M15 3h6v6"/><path d="M10 14 21 3"/></svg>`;

function initialsOf(name) { return name.replace('د. ', '').trim().charAt(0); }

function countLabel(n) {
  if (n === 1) return 'قصة واحدة';
  if (n === 2) return 'قصتان';
  if (n <= 10) return `${AR_NUM.format(n)} قصص`;
  return `${AR_NUM.format(n)} قصة`;
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

function cardHTML(s, i) {
  const media = s.photo
    ? `<img class="photo" src="${s.photo}" alt="صورة ${s.name}" loading="lazy" decoding="async" width="560" height="385" onerror="this.outerHTML='<div class=&quot;avatar-fallback&quot; aria-hidden=&quot;true&quot;>${initialsOf(s.name)}</div>'">`
    : `<div class="avatar-fallback" aria-hidden="true">${initialsOf(s.name)}</div>`;
  const org = `<div class="card-org">${s.orgLogo ? `<img src="${s.orgLogo}" alt="" loading="lazy" decoding="async">` : ''}<span>${s.org}</span></div>`;
  const links = s.links.slice(0, 1).map(l =>
    `<a class="ext-link" href="${l.url}" target="_blank" rel="noopener" aria-label="${l.label} — ${s.name} (يفتح في نافذة جديدة)" title="${l.label}">${EXT_ICON}</a>`).join('');
  return `
  <article class="story-card" style="animation-delay:${Math.min(i * 60, 420)}ms">
    <div class="card-media">
      ${media}
      <span class="rank-badge">دفعة ${s.year}</span>
      <span class="cat-badge">${catLabel(s.category)}</span>
    </div>
    <div class="card-body">
      <h3>${s.name}</h3>
      <p class="card-role">${s.role}</p>
      ${org}
      <p class="card-impact">${s.impact}</p>
      <div class="card-meta">
        <span class="meta-pill">${s.period}</span>
      </div>
      <div class="card-actions">
        <button class="btn-read" data-id="${s.id}" aria-haspopup="dialog">اقرأ القصة كاملة</button>
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
    <section class="year-group" id="year-${y.id}" aria-label="${y.label}">
      <div class="year-head">
        <div class="year-title-wrap">
          <h3 class="year-title"><span class="year-num">${y.id}</span> ${y.label.replace(String(y.id), '').trim()}</h3>
          <p class="year-desc">${y.desc}</p>
        </div>
        <span class="year-count">${countLabel(items.length)}</span>
      </div>
      <div class="cards-grid">${items.map(cardHTML).join('')}</div>
    </section>`;
  }).join('');
  storiesWrap.innerHTML = html;
  $('#noResults').hidden = list.length > 0;
  $('#resultsCount').textContent = list.length === STORIES.length
    ? `عرض جميع القصص — ${AR_NUM.format(list.length)} قصة عبر ${AR_NUM.format(YEARS.length)} دفعات`
    : `${AR_NUM.format(list.length)} من ${AR_NUM.format(STORIES.length)} قصة`;
}
storiesWrap.addEventListener('click', e => {
  const btn = e.target.closest('.btn-read');
  if (btn) openModal(btn.dataset.id);
});
renderStories();

/* ---------- Modal ---------- */
const modal = $('#storyModal');
const modalContent = $('#modalContent');
let lastFocused = null;

function openModal(id) {
  const s = STORIES.find(x => x.id === id);
  if (!s) return;
  lastFocused = document.activeElement;
  const photo = s.photo
    ? `<img class="m-photo" src="${s.photo}" alt="صورة ${s.name}" onerror="this.outerHTML='<div class=&quot;m-avatar&quot; aria-hidden=&quot;true&quot;>${initialsOf(s.name)}</div>'">`
    : `<div class="m-avatar" aria-hidden="true">${initialsOf(s.name)}</div>`;
  modalContent.innerHTML = `
    <div class="modal-head">
      ${photo}
      <div class="m-head-txt">
        <span class="m-rank">دفعة ${s.year} · ${catLabel(s.category)}</span>
        <h2 id="modalName">${s.name}</h2>
        <span class="m-name-en">${s.nameEn}</span>
        <p class="m-role">${s.role}</p>
      </div>
    </div>
    <div class="modal-body">
      <div class="m-org">${s.orgLogo ? `<img src="${s.orgLogo}" alt="شعار ${s.org}">` : ''}<span>${s.org}</span></div>
      <div class="m-meta">
        <div class="m-meta-item"><div class="k">سنة التخرج</div><div class="v">${s.year}</div></div>
        <div class="m-meta-item"><div class="k">البرنامج</div><div class="v">${s.program}</div></div>
        <div class="m-meta-item"><div class="k">الفترة الزمنية</div><div class="v">${s.period}</div></div>
      </div>
      <h3>القصة</h3>
      <p class="m-story">${s.story}</p>
      <h3>أبرز الإنجازات</h3>
      <ul class="m-achievements">${s.achievements.map(a => `<li>${a}</li>`).join('')}</ul>
      ${s.links.length ? `<h3>روابط موثّقة</h3>
      <div class="m-links">${s.links.map(l => `<a href="${l.url}" target="_blank" rel="noopener">${EXT_ICON} ${l.label}</a>`).join('')}</div>` : ''}
    </div>`;
  modal.hidden = false;
  document.body.style.overflow = 'hidden';
  requestAnimationFrame(() => {
    $('.modal-close', modal).focus();
  });
}

function closeModal() {
  modal.hidden = true;
  document.body.style.overflow = '';
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
