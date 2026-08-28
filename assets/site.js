/* Site behaviour: mobile nav, gentle reveal, publication filtering. */
(function () {
  "use strict";

  /* ---- mobile navigation ---- */
  var btn = document.querySelector(".menu-btn");
  var nav = document.getElementById("primary-nav");
  if (btn && nav) {
    btn.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      btn.setAttribute("aria-expanded", String(open));
    });
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        nav.classList.remove("open");
        btn.setAttribute("aria-expanded", "false");
      }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("open")) {
        nav.classList.remove("open");
        btn.setAttribute("aria-expanded", "false");
        btn.focus();
      }
    });
  }

  /* ---- reveal on scroll (skipped when reduced motion is requested) ---- */
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var targets = document.querySelectorAll(".reveal");
  if (!reduce && "IntersectionObserver" in window) {
    /* failsafe: never leave content hidden if the observer never fires */
    setTimeout(function () {
      targets.forEach(function (el) { el.classList.add("is-in"); });
    }, 3000);
  }
  if (reduce || !("IntersectionObserver" in window)) {
    targets.forEach(function (el) { el.classList.add("is-in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-in");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });
    targets.forEach(function (el) { io.observe(el); });
  }

  /* ---- publications: search + filter ---- */
  var list = document.getElementById("pub-list");
  var dataEl = document.getElementById("pub-data");
  if (!list || !dataEl) return;

  var items = [];
  try { items = JSON.parse(dataEl.textContent); } catch (err) { items = []; }

  var LABEL = { journal: "Journal article", conference: "Conference paper", chapter: "Book chapter" };
  var search = document.getElementById("pub-search");
  var chips = Array.prototype.slice.call(document.querySelectorAll(".chip[data-kind]"));
  var countEl = document.getElementById("pub-count");
  var kind = "all";

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function authorMarkup(a) {
    if (!a) return "";
    return esc(a).replace(/Mamdouh Alenezi/g, "<em>Mamdouh Alenezi</em>");
  }

  function render(rows) {
    if (!rows.length) {
      list.innerHTML = '<li class="empty">No publications match that search.</li>';
    } else {
      list.innerHTML = rows.map(function (p) {
        var links = [];
        if (p.doi) links.push('<a href="' + esc(p.doi) + '" rel="noopener" target="_blank">DOI</a>');
        else if (p.url) links.push('<a href="' + esc(p.url) + '" rel="noopener" target="_blank">Publisher</a>');
        if (p.pdf) links.push('<a href="' + esc(p.pdf) + '" rel="noopener" target="_blank">PDF</a>');
        var head = p.doi || p.url
          ? '<a href="' + esc(p.doi || p.url) + '" rel="noopener" target="_blank">' + esc(p.title) + "</a>"
          : esc(p.title);
        return '<li class="pub">' +
          '<span class="pub__year">' + (p.year ? esc(p.year) : "&mdash;") + "</span>" +
          "<div><h3 class=\"pub__title\">" + head +
            '<span class="pub__kind">' + esc(LABEL[p.kind] || p.kind) + "</span></h3>" +
            (p.authors ? '<p class="pub__meta">' + authorMarkup(p.authors) + "</p>" : "") +
            (p.venue ? '<p class="pub__meta">' + esc(p.venue) + "</p>" : "") +
            (links.length ? '<p class="pub__links">' + links.join("") + "</p>" : "") +
          "</div></li>";
      }).join("");
    }
    if (countEl) {
      countEl.textContent = rows.length + (rows.length === 1 ? " publication" : " publications") +
        (kind === "all" ? "" : " · " + (LABEL[kind] || kind) + "s");
    }
  }

  function apply() {
    var q = (search && search.value || "").trim().toLowerCase();
    var rows = items.filter(function (p) {
      if (kind !== "all" && p.kind !== kind) return false;
      if (!q) return true;
      return (p.title + " " + p.authors + " " + p.venue + " " + (p.year || "")).toLowerCase().indexOf(q) > -1;
    });
    rows.sort(function (a, b) { return (b.year || 0) - (a.year || 0); });
    render(rows);
  }

  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      kind = chip.getAttribute("data-kind");
      chips.forEach(function (c) { c.setAttribute("aria-pressed", String(c === chip)); });
      apply();
    });
  });
  if (search) {
    var t;
    search.addEventListener("input", function () {
      clearTimeout(t);
      t = setTimeout(apply, 120);
    });
  }
  apply();
})();
