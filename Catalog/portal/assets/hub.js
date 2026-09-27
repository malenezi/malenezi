/* SDAIA Academy Trainer Portal — catalog filtering and sortable tables (no external dependencies). */
(function () {
  function textOf(cell) { return (cell && cell.textContent || "").trim(); }

  function makeSortable(table) {
    var head = table.tHead; if (!head) return;
    Array.prototype.forEach.call(head.rows[0].cells, function (th, idx) {
      if (!textOf(th)) return;
      th.classList.add("hub-sortable");
      th.addEventListener("click", function () {
        var asc = !th.classList.contains("hub-sort-asc");
        Array.prototype.forEach.call(head.rows[0].cells, function (h) { h.classList.remove("hub-sort-asc", "hub-sort-desc"); });
        th.classList.add(asc ? "hub-sort-asc" : "hub-sort-desc");
        var body = table.tBodies[0];
        var rows = Array.prototype.slice.call(body.rows);
        rows.sort(function (a, b) {
          var x = textOf(a.cells[idx]), y = textOf(b.cells[idx]);
          var nx = parseFloat(x), ny = parseFloat(y);
          var c = (!isNaN(nx) && !isNaN(ny) && /^[\d.]+/.test(x) && /^[\d.]+/.test(y)) ? nx - ny : x.localeCompare(y);
          return asc ? c : -c;
        });
        rows.forEach(function (r) { body.appendChild(r); });
      });
    });
  }

  function setupFilter(bar) {
    var wrap = document.getElementById(bar.getAttribute("data-target"));
    var table = wrap && wrap.querySelector("table");
    if (!table) return;
    var rows = Array.prototype.slice.call(table.tBodies[0].rows);
    var input = bar.querySelector("input");
    var selects = Array.prototype.slice.call(bar.querySelectorAll("select"));
    var count = bar.querySelector(".hub-count");

    selects.forEach(function (sel) {
      var col = parseInt(sel.getAttribute("data-col"), 10), seen = {};
      rows.forEach(function (r) { var v = textOf(r.cells[col]); if (v) seen[v] = true; });
      Object.keys(seen).sort().forEach(function (v) {
        var o = document.createElement("option"); o.value = v; o.textContent = v; sel.appendChild(o);
      });
    });

    var params = new URLSearchParams(window.location.search);
    if (params.get("q")) input.value = params.get("q");

    function apply() {
      var q = (input.value || "").toLowerCase().split(/\s+/).filter(Boolean), shown = 0;
      rows.forEach(function (r) {
        var text = r.textContent.toLowerCase();
        var ok = q.every(function (t) { return text.indexOf(t) !== -1; });
        selects.forEach(function (sel) {
          if (sel.value && textOf(r.cells[parseInt(sel.getAttribute("data-col"), 10)]) !== sel.value) ok = false;
        });
        r.style.display = ok ? "" : "none";
        if (ok) shown++;
      });
      if (count) count.textContent = shown + " of " + rows.length + " courses";
    }
    input.addEventListener("input", apply);
    selects.forEach(function (s) { s.addEventListener("change", apply); });
    apply();
  }

  function init() {
    document.querySelectorAll(".hub-filter").forEach(setupFilter);
    document.querySelectorAll(".md-typeset table:not(.hub-no-sort)").forEach(makeSortable);
  }
  if (window.document$ && window.document$.subscribe) { window.document$.subscribe(init); }
  else if (document.readyState !== "loading") { init(); } else { document.addEventListener("DOMContentLoaded", init); }
})();
