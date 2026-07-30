/* =========================================================
   SDAIA Academy — Success Stories · Interactions (vanilla JS)
   ========================================================= */
'use strict';

const $ = (sel, root = document) => root.querySelector(sel);
const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];
const AR_NUM = new Intl.NumberFormat('ar-SA');

const state = { query: '', category: 'all', sort: 'rank' };

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
    <dd data-count="${s.value}">0</dd>
    <dt>${s.label}<span class="stat-note">${s.note}</span></dt>
  </div>`).join('');

const statsIO = new IntersectionObserver(entries => {
  for (const en of entries) if (en.isIntersecting) {
    $$('[data-count]', en.target).forEach(el => animateCount(el, +el.dataset.count));
    statsIO.unobserve(en.target);
  }
}, { threshold: 0.4 });
statsIO.observe(heroStats);

/* ---------- Dashboard tiles ---------- */
const dashTiles = $('#dashTiles');
dashTiles.innerHTML = EXTRA_STATS.map(s => `
  <div class="dash-tile">
    <div class="val" data-count="${s.value}">0</div>
    <div class="lbl">${s.label}</div>
  </div>`).join('');
statsIO.observe(dashTiles);

/* ---------- Category bar chart ---------- */
const maxCat = Math.max(...CATEGORY_COUNTS.map(c => c.count));
$('#chartCategories').innerHTML = CATEGORY_COUNTS.map(c => `
  <div class="bar-row">
    <span class="bar-label">${c.label}</span>
    <div class="bar-track"><div class="bar-fill" data-w="${(c.count / maxCat) * 100}"></div></div>
    <span class="bar-val">${AR_NUM.format(c.count)}</span>
  </div>`).join('');

const barsIO = new IntersectionObserver(entries => {
  for (const en of entries) if (en.isIntersecting) {
    $$('.bar-fill', en.target).forEach(el => { el.style.width = el.dataset.w + '%'; });
    barsIO.unobserve(en.target);
  }
}, { threshold: 0.3 });
barsIO.observe($('#chartCategories'));

/* ---------- Verification donut (ordinal blue ramp — validated) ---------- */
(function buildDonut() {
  const data = [
    { key: 'أ', count: 9 }, { key: 'ب', count: 6 }, { key: 'ج', count: 5 },
  ];
  const colors = { 'أ': '#104281', 'ب': '#2a78d6', 'ج': '#6da7ec' };
  const total = data.reduce((a, d) => a + d.count, 0);
  const svg = $('#chartVerification');
  const R = 74, C = 100, SW = 30, GAP = 0.035; // gap in radians ≈ 2px spacer
  let angle = -Math.PI / 2;
  let paths = '';
  for (const d of data) {
    const frac = d.count / total;
    const a0 = angle + GAP / 2, a1 = angle + frac * 2 * Math.PI - GAP / 2;
    const large = (a1 - a0) > Math.PI ? 1 : 0;
    const x0 = C + R * Math.cos(a0), y0 = C + R * Math.sin(a0);
    const x1 = C + R * Math.cos(a1), y1 = C + R * Math.sin(a1);
    paths += `<path d="M ${x0} ${y0} A ${R} ${R} 0 ${large} 1 ${x1} ${y1}" fill="none" stroke="${colors[d.key]}" stroke-width="${SW}" stroke-linecap="butt"/>`;
    angle += frac * 2 * Math.PI;
  }
  svg.innerHTML = paths + `
    <text class="donut-center" x="100" y="94" text-anchor="middle" font-size="30" font-weight="700" fill="#0E1B2C">${AR_NUM.format(total)}</text>
    <text class="donut-center" x="100" y="118" text-anchor="middle" font-size="12.5" fill="#6E7F93">قصة موثّقة</text>`;
  $('#verifLegend').innerHTML = data.map(d => `
    <li><span class="swatch" style="background:${colors[d.key]}"></span>
    <span>${VERIFICATION[d.key].label} — <b>${AR_NUM.format(d.count)}</b> قصص</span></li>`).join('');
})();

/* ---------- Scores chart ---------- */
const scoresWrap = $('#chartScores');
const tip = document.createElement('div');
tip.className = 'chart-tip';
document.body.appendChild(tip);

scoresWrap.innerHTML = STORIES.map(s => `
  <button class="chart-score-col" data-id="${s.id}" aria-label="${s.name} — درجة الأثر ${s.score} من 100. اضغط لفتح القصة.">
    <span class="col-val">${AR_NUM.format(s.score)}</span>
    <div class="col-fill" style="height:${(s.score / 100) * 78}%"></div>
    <span class="col-name">${s.name.replace('د. ', '').split(' ')[0]}</span>
  </button>`).join('');

const scoresIO = new IntersectionObserver(entries => {
  for (const en of entries) if (en.isIntersecting) {
    $$('.col-fill', en.target).forEach((el, i) => {
      setTimeout(() => { el.style.transform = 'scaleY(1)'; }, i * 45);
    });
    scoresIO.unobserve(en.target);
  }
}, { threshold: 0.3 });
scoresIO.observe(scoresWrap);

scoresWrap.addEventListener('mousemove', e => {
  const col = e.target.closest('.chart-score-col');
  if (!col) { tip.classList.remove('show'); return; }
  const st = STORIES.find(s => s.id === col.dataset.id);
  tip.innerHTML = `<b>${st.name}</b> · ${AR_NUM.format(st.score)}/100<br><span style="opacity:.8">${st.role}</span>`;
  tip.style.top = (e.clientY - tip.offsetHeight - 14) + 'px';
  tip.style.left = Math.min(Math.max(e.clientX - tip.offsetWidth / 2, 8), innerWidth - tip.offsetWidth - 8) + 'px';
  tip.classList.add('show');
});
scoresWrap.addEventListener('mouseleave', () => tip.classList.remove('show'));
scoresWrap.addEventListener('click', e => {
  const col = e.target.closest('.chart-score-col');
  if (col) openModal(col.dataset.id);
});

/* ---------- Category chips ---------- */
const chipsWrap = $('#categoryChips');
chipsWrap.innerHTML = CATEGORIES.map(c => `
  <button class="chip" role="tab" data-cat="${c.id}" aria-selected="${c.id === 'all'}">${c.label}</button>`).join('');
chipsWrap.addEventListener('click', e => {
  const chip = e.target.closest('.chip');
  if (!chip) return;
  state.category = chip.dataset.cat;
  $$('.chip', chipsWrap).forEach(ch => ch.setAttribute('aria-selected', String(ch === chip)));
  renderCards();
});

/* ---------- Search + sort ---------- */
let searchTimer;
$('#searchInput').addEventListener('input', e => {
  clearTimeout(searchTimer);
  searchTimer = setTimeout(() => { state.query = e.target.value.trim(); renderCards(); }, 160);
});
$('#sortSelect').addEventListener('change', e => { state.sort = e.target.value; renderCards(); });

/* ---------- Cards ---------- */
const grid = $('#cardsGrid');
const catLabel = id => (CATEGORIES.find(c => c.id === id) || {}).label || '';
const EXT_ICON = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><path d="M15 3h6v6"/><path d="M10 14 21 3"/></svg>`;

function initialsOf(name) { return name.replace('د. ', '').trim().charAt(0); }

function filteredStories() {
  const q = state.query.toLowerCase();
  let list = STORIES.filter(s => {
    const inCat = state.category === 'all' || s.categories.includes(state.category);
    if (!inCat) return false;
    if (!q) return true;
    return [s.name, s.nameEn, s.org, s.role, s.program, s.impact].join(' ').toLowerCase().includes(q);
  });
  if (state.sort === 'score') list = [...list].sort((a, b) => b.score - a.score);
  else if (state.sort === 'name') list = [...list].sort((a, b) => a.name.localeCompare(b.name, 'ar'));
  else list = [...list].sort((a, b) => a.rank - b.rank);
  return list;
}

function cardHTML(s, i) {
  const media = s.photo
    ? `<img class="photo" src="${s.photo}" alt="صورة ${s.name}" loading="lazy" decoding="async" width="560" height="385">`
    : `<div class="avatar-fallback" aria-hidden="true">${initialsOf(s.name)}</div>`;
  const org = `<div class="card-org">${s.orgLogo ? `<img src="${s.orgLogo}" alt="" loading="lazy" decoding="async">` : ''}<span>${s.org}</span></div>`;
  const links = s.links.slice(0, 1).map(l =>
    `<a class="ext-link" href="${l.url}" target="_blank" rel="noopener" aria-label="${l.label} — ${s.name} (يفتح في نافذة جديدة)" title="${l.label}">${EXT_ICON}</a>`).join('');
  return `
  <article class="story-card" style="animation-delay:${Math.min(i * 60, 420)}ms">
    <div class="card-media">
      ${media}
      <span class="rank-badge">#${AR_NUM.format(s.rank)}</span>
      <span class="cat-badge">${catLabel(s.category)}</span>
    </div>
    <div class="card-body">
      <h3>${s.name}</h3>
      <p class="card-role">${s.role}</p>
      ${org}
      <p class="card-impact">${s.impact}</p>
      <div class="card-meta">
        <span class="meta-pill score">الأثر ${AR_NUM.format(s.score)}/١٠٠</span>
        <span class="meta-pill verif">تحقق ${s.verification}</span>
        <span class="meta-pill">${s.period}</span>
      </div>
      <div class="card-actions">
        <button class="btn-read" data-id="${s.id}" aria-haspopup="dialog">اقرأ القصة كاملة</button>
        ${links}
      </div>
    </div>
  </article>`;
}

function renderCards() {
  const list = filteredStories();
  grid.innerHTML = list.map(cardHTML).join('');
  $('#noResults').hidden = list.length > 0;
  $('#resultsCount').textContent = list.length === STORIES.length
    ? `عرض جميع القصص — ${AR_NUM.format(list.length)} قصة`
    : `${AR_NUM.format(list.length)} من ${AR_NUM.format(STORIES.length)} قصة`;
}
grid.addEventListener('click', e => {
  const btn = e.target.closest('.btn-read');
  if (btn) openModal(btn.dataset.id);
});
renderCards();

/* ---------- Timeline ---------- */
$('#timelineList').innerHTML = TIMELINE.map(t => `
  <li class="reveal">
    <span class="dot" aria-hidden="true"></span>
    <span class="t-year">${t.year}</span>
    <h3>${t.title}</h3>
    <p>${t.text}</p>
  </li>`).join('');
$$('#timelineList .reveal').forEach(el => revealIO.observe(el));

/* ---------- Verification layers (methodology) ---------- */
$('#verifLayers').innerHTML = Object.entries(VERIFICATION).map(([k, v]) => `
  <div class="verif-layer">
    <span class="verif-mark" style="background:${v.color}">${k}</span>
    <div><h3>${v.label}</h3><p>${v.desc}</p></div>
  </div>`).join('');

/* ---------- Modal ---------- */
const modal = $('#storyModal');
const modalContent = $('#modalContent');
let lastFocused = null;

function openModal(id) {
  const s = STORIES.find(x => x.id === id);
  if (!s) return;
  lastFocused = document.activeElement;
  const photo = s.photo
    ? `<img class="m-photo" src="${s.photo}" alt="صورة ${s.name}">`
    : `<div class="m-avatar" aria-hidden="true">${initialsOf(s.name)}</div>`;
  modalContent.innerHTML = `
    <div class="modal-head">
      ${photo}
      <div class="m-head-txt">
        <span class="m-rank">المرتبة ${AR_NUM.format(s.rank)} من ٢٠ · ${catLabel(s.category)}</span>
        <h2 id="modalName">${s.name}</h2>
        <span class="m-name-en">${s.nameEn}</span>
        <p class="m-role">${s.role}</p>
      </div>
    </div>
    <div class="modal-body">
      <div class="m-org">${s.orgLogo ? `<img src="${s.orgLogo}" alt="شعار ${s.org}">` : ''}<span>${s.org}</span></div>
      <div class="m-meta">
        <div class="m-meta-item"><div class="k">البرنامج</div><div class="v">${s.program}</div></div>
        <div class="m-meta-item"><div class="k">الفترة الزمنية</div><div class="v">${s.period}</div></div>
        <div class="m-meta-item"><div class="k">طبقة التحقق</div><div class="v">${s.verification} — ${VERIFICATION[s.verification].label}</div></div>
      </div>
      <div class="m-score-wrap">
        <div class="m-score-head"><span>درجة الأثر</span><b>${AR_NUM.format(s.score)} / ١٠٠</b></div>
        <div class="m-score-track"><div class="m-score-fill" data-w="${s.score}"></div></div>
      </div>
      <h3>القصة</h3>
      <p class="m-story">${s.story}</p>
      <h3>أبرز الإنجازات</h3>
      <ul class="m-achievements">${s.achievements.map(a => `<li>${a}</li>`).join('')}</ul>
      ${s.links.length ? `<h3>روابط موثّقة</h3>
      <div class="m-links">${s.links.map(l => `<a href="${l.url}" target="_blank" rel="noopener">${EXT_ICON} ${l.label}</a>`).join('')}</div>` : ''}
      <p class="m-verif-note"><b>عن التوثيق:</b> ${VERIFICATION[s.verification].desc}</p>
    </div>`;
  modal.hidden = false;
  document.body.style.overflow = 'hidden';
  requestAnimationFrame(() => {
    const fill = $('.m-score-fill', modalContent);
    if (fill) requestAnimationFrame(() => { fill.style.width = fill.dataset.w + '%'; });
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
