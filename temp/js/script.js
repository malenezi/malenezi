/* =============================================================
   SDAIA ACADEMY — National Data & AI Competency Framework
   script.js  ·  Shared interactions for all pages
   ============================================================= */
(function () {
  'use strict';

  /* ---------- Mobile drawer ---------- */
  function initDrawer() {
    var openBtn = document.querySelector('[data-drawer-open]');
    var drawer = document.querySelector('[data-drawer]');
    if (!openBtn || !drawer) return;
    var closeBtn = drawer.querySelector('[data-drawer-close]');

    function open() {
      drawer.classList.add('open');
      drawer.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    }
    function close() {
      drawer.classList.remove('open');
      drawer.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }
    openBtn.addEventListener('click', open);
    if (closeBtn) closeBtn.addEventListener('click', close);
    drawer.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', close);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && drawer.classList.contains('open')) close();
    });
  }

  /* ---------- Scroll reveal ---------- */
  function initReveal() {
    var els = document.querySelectorAll('[data-reveal]');
    if (!els.length) return;
    if (!('IntersectionObserver' in window)) {
      els.forEach(function (el) { el.classList.add('in'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var el = entry.target;
          var delay = el.getAttribute('data-reveal-delay');
          if (delay) el.style.animationDelay = delay + 'ms';
          el.classList.add('in');
          io.unobserve(el);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    els.forEach(function (el) { io.observe(el); });

    /* failsafe: if anything is still hidden after 4s, reveal it */
    setTimeout(function () {
      document.querySelectorAll('[data-reveal]:not(.in)').forEach(function (el) {
        el.classList.add('in');
      });
    }, 4000);
  }

  /* ---------- Animated counters ---------- */
  function initCounters() {
    var nums = document.querySelectorAll('[data-count]');
    if (!nums.length) return;
    if (!('IntersectionObserver' in window)) {
      nums.forEach(function (n) { n.textContent = n.getAttribute('data-count'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        var target = parseFloat(el.getAttribute('data-count'));
        var suffix = el.getAttribute('data-suffix') || '';
        var dur = 1400;
        var start = null;
        function step(ts) {
          if (!start) start = ts;
          var p = Math.min((ts - start) / dur, 1);
          var eased = 1 - Math.pow(1 - p, 3);
          var val = Math.round(target * eased);
          el.textContent = val + suffix;
          if (p < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
        io.unobserve(el);
      });
    }, { threshold: 0.4 });
    nums.forEach(function (n) { io.observe(n); });
  }

  /* ---------- Accordions ---------- */
  function initAccordions() {
    document.querySelectorAll('.accordion').forEach(function (acc) {
      var items = acc.querySelectorAll('.acc-item');
      items.forEach(function (item) {
        var head = item.querySelector('.acc-head');
        var body = item.querySelector('.acc-body');
        if (!head || !body) return;
        head.setAttribute('aria-expanded', 'false');
        head.addEventListener('click', function () {
          var isOpen = item.classList.contains('open');
          // single-open accordion if data-single
          if (acc.hasAttribute('data-single')) {
            items.forEach(function (it) {
              it.classList.remove('open');
              var b = it.querySelector('.acc-body');
              var h = it.querySelector('.acc-head');
              if (b) b.style.maxHeight = null;
              if (h) h.setAttribute('aria-expanded', 'false');
            });
          }
          if (isOpen) {
            item.classList.remove('open');
            body.style.maxHeight = null;
            head.setAttribute('aria-expanded', 'false');
          } else {
            item.classList.add('open');
            body.style.maxHeight = body.scrollHeight + 'px';
            head.setAttribute('aria-expanded', 'true');
          }
        });
      });
    });
  }

  /* ---------- Tabs ---------- */
  function initTabs() {
    document.querySelectorAll('[data-tabs]').forEach(function (group) {
      var btns = group.querySelectorAll('.tab-btn');
      var panels = group.querySelectorAll('.tab-panel');
      btns.forEach(function (btn) {
        btn.addEventListener('click', function () {
          var target = btn.getAttribute('data-tab');
          btns.forEach(function (b) {
            b.classList.toggle('active', b === btn);
            b.setAttribute('aria-selected', b === btn ? 'true' : 'false');
          });
          panels.forEach(function (p) {
            p.classList.toggle('active', p.getAttribute('data-panel') === target);
          });
        });
      });
    });
  }

  /* ---------- Header shadow on scroll ---------- */
  function initHeaderScroll() {
    var header = document.querySelector('.header');
    if (!header) return;
    function update() {
      if (window.scrollY > 8) {
        header.style.boxShadow = '0 8px 24px -16px rgba(42,44,92,0.3)';
      } else {
        header.style.boxShadow = 'none';
      }
    }
    window.addEventListener('scroll', update, { passive: true });
    update();
  }

  /* ---------- Catalog filter engine ---------- */
  function initCatalog() {
    var root = document.querySelector('[data-catalog]');
    if (!root || !window.SDAIA_PROGRAMS) return;

    var grid = root.querySelector('[data-catalog-grid]');
    var empty = root.querySelector('[data-catalog-empty]');
    var countEl = root.querySelector('[data-catalog-count]');
    var totalEl = root.querySelector('[data-catalog-total]');
    var searchInput = root.querySelector('[data-catalog-search]');
    var clearBtn = root.querySelector('[data-catalog-clear]');
    var chips = root.querySelectorAll('[data-filter]');

    var programs = window.SDAIA_PROGRAMS;
    if (totalEl) totalEl.textContent = programs.length;

    var state = { q: '', persona: 'all', level: 'all', portfolio: 'all' };

    var personaLabel = { citizen: 'Citizen', worker: 'Worker', professional: 'Professional' };
    var levelLabel = { beginner: 'Beginner', practitioner: 'Practitioner', expert: 'Expert' };
    var portfolioLabel = {
      fluency: 'AI Fluency', foundations: 'Foundations', sectoral: 'Sectoral',
      leadership: 'Leadership', engineering: 'Engineering', science: 'Data Science',
      governance: 'Governance'
    };

    function arrow() {
      return '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M3 7h8m0 0L8 4m3 3L8 10" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    }
    function clockIcon() {
      return '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="7" cy="7" r="5.5"/><path d="M7 4v3l2 1.4" stroke-linecap="round"/></svg>';
    }

    function render() {
      var q = state.q.toLowerCase();
      var matches = programs.filter(function (p) {
        if (state.persona !== 'all' && p.persona !== state.persona) return false;
        if (state.level !== 'all' && p.level !== state.level) return false;
        if (state.portfolio !== 'all' && p.portfolio !== state.portfolio) return false;
        if (q) {
          var hay = (p.title + ' ' + p.desc + ' ' + p.code).toLowerCase();
          if (hay.indexOf(q) === -1) return false;
        }
        return true;
      });

      if (countEl) countEl.textContent = matches.length;
      if (empty) empty.classList.toggle('show', matches.length === 0);

      var anyFilter = state.q || state.persona !== 'all' || state.level !== 'all' || state.portfolio !== 'all';
      if (clearBtn) clearBtn.style.display = anyFilter ? 'inline-block' : 'none';

      grid.innerHTML = matches.map(function (p) {
        return (
          '<article class="card" data-persona="' + p.persona + '">' +
            '<div class="card-meta">' +
              '<span class="card-code">' + p.code + '</span>' +
              '<div class="card-badges">' +
                '<span class="badge badge-persona">' + (personaLabel[p.persona] || p.persona) + '</span>' +
                '<span class="badge badge-level">' + (levelLabel[p.level] || p.level) + '</span>' +
              '</div>' +
            '</div>' +
            '<h3>' + p.title + '</h3>' +
            '<p class="card-desc">' + p.desc + '</p>' +
            '<div class="card-foot">' +
              '<span class="card-duration"><span class="status-tag status-' + p.status + '"></span>' +
                clockIcon() + ' ' + p.duration + '</span>' +
              '<a class="card-link" href="contact.html">Enquire ' + arrow() + '</a>' +
            '</div>' +
          '</article>'
        );
      }).join('');
    }

    if (searchInput) {
      searchInput.addEventListener('input', function () {
        state.q = searchInput.value.trim();
        render();
      });
    }
    chips.forEach(function (chip) {
      chip.addEventListener('click', function () {
        var dim = chip.getAttribute('data-filter');
        var val = chip.getAttribute('data-value');
        state[dim] = val;
        root.querySelectorAll('[data-filter="' + dim + '"]').forEach(function (c) {
          c.classList.toggle('active', c === chip);
        });
        render();
      });
    });
    if (clearBtn) {
      clearBtn.addEventListener('click', function () {
        state = { q: '', persona: 'all', level: 'all', portfolio: 'all' };
        if (searchInput) searchInput.value = '';
        chips.forEach(function (c) {
          c.classList.toggle('active', c.getAttribute('data-value') === 'all');
        });
        render();
      });
    }

    // pre-select from URL hash (e.g. catalog.html#portfolio=engineering)
    var hash = window.location.hash.replace('#', '');
    if (hash.indexOf('=') > -1) {
      var parts = hash.split('=');
      if (state.hasOwnProperty(parts[0])) {
        state[parts[0]] = parts[1];
        chips.forEach(function (c) {
          if (c.getAttribute('data-filter') === parts[0]) {
            c.classList.toggle('active', c.getAttribute('data-value') === parts[1]);
          }
        });
      }
    }

    render();
  }

  /* ---------- Year stamp ---------- */
  function initYear() {
    document.querySelectorAll('[data-year]').forEach(function (el) {
      el.textContent = new Date().getFullYear();
    });
  }

  /* ---------- Init ---------- */
  document.addEventListener('DOMContentLoaded', function () {
    initDrawer();
    initReveal();
    initCounters();
    initAccordions();
    initTabs();
    initHeaderScroll();
    initCatalog();
    initYear();
  });
})();
