"""AI Strategy executive reference: /ai-strategy/

A flagship long-form reference page. All reading content (evidence, frameworks, cases, sources ...)
lives in data/ai-strategy.json and is rendered to HTML here at build time, so it is indexable and
readable without JavaScript. assets/ai-strategy.js only adds behaviour (tabs, filters, the seven
working tools); assets/ai-strategy.css carries the page-specific styles on top of assets/site.css.

To update a figure, a source or a case: edit data/ai-strategy.json, bump UPDATED below, rebuild.
"""
import html, json, os, re
from datetime import datetime

SLUG = "ai-strategy/index.html"
PATH = "ai-strategy/"
PUBLISHED = "2026-11-22"
UPDATED = "2026-11-22"          # bump when the evidence or sources are re-checked
CHECKED = "November 2026"       # shown on the page: when the evidence was last checked
OG_IMAGE = "images/ai-strategy-card.png"

TITLE = "AI Strategy: Evidence, Frameworks and Working Tools — Prof. Mamdouh Alenezi"
HEADLINE = "AI Strategy, with evidence: an executive reference"
DESCRIPTION = ("An evidence-based executive reference on AI strategy: the research, nine frameworks compared, "
               "and tools for prioritization, business cases and governance.")
KEYWORDS = ["AI strategy", "enterprise AI strategy", "AI strategy framework", "AI governance",
            "AI transformation", "AI maturity model", "AI use case prioritization", "AI business case",
            "AI ROI", "agentic AI governance", "EU AI Act timeline", "NIST AI RMF", "ISO/IEC 42001",
            "AI roadmap", "national AI strategy"]

TOC = [("evidence", "Evidence"), ("terms", "Four terms"), ("frameworks", "Frameworks"),
       ("system", "Strategy system"), ("tools", "Tools"), ("roadmap", "Roadmap"), ("cases", "Cases"),
       ("priorities", "Priorities"), ("sources", "Sources")]

EV_THEMES = [("all", "All"), ("value", "Value captured"), ("failure", "Failure and abandonment"),
             ("scaling", "Scaling"), ("agents", "Agents"), ("adoption", "Adoption and cost")]

TOOLS = [("t-assess", "Maturity check"), ("t-prior", "Use-case prioritizer"), ("t-case", "Business case"),
         ("t-source", "Build, buy or partner"), ("t-govern", "Governance"), ("t-decide", "Board decisions"),
         ("t-canvas", "Strategy canvas")]


def h(s):
    """Author-written HTML fragment: keep its tags, escape only bare ampersands."""
    return re.sub(r"&(?!#?\w+;)", "&amp;", s)


def ext(url, text):
    return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (html.escape(url, quote=True), h(text))


def tablist(prefix, labels, aria, cls, vertical=False):
    """Tab buttons for pre-rendered panels <prefix>-<i>. Hidden until JS is confirmed (see CSS)."""
    return '<div class="%s" role="tablist" aria-label="%s"%s data-tabs>%s</div>' % (
        cls, aria, ' aria-orientation="vertical"' if vertical else "",
        "".join('<button type="button" role="tab" id="{p}-tab-{i}" aria-controls="{p}-{i}" '
                'aria-selected="{s}" tabindex="{t}">{l}</button>'.format(
                    p=prefix, i=i, l=l, s="true" if i == 0 else "false", t=0 if i == 0 else -1)
                for i, l in enumerate(labels)))


def panel_attrs(prefix, i, cls):
    return 'class="ax-panel %s%s" id="%s-%d" role="tabpanel" aria-labelledby="%s-tab-%d" tabindex="0"' % (
        cls, " on" if i == 0 else "", prefix, i, prefix, i)


def chips(group, items, aria):
    return '<ul class="chips ax-chips" data-filter="%s" role="group" aria-label="%s">%s</ul>' % (
        group, aria,
        "".join('<li><button type="button" class="chip" aria-pressed="%s" data-k="%s">%s</button></li>' % (
            "true" if i == 0 else "false", k, l) for i, (k, l) in enumerate(items)))


def build(B, insights):
    with open(os.path.join(B.ROOT, "data", "ai-strategy.json"), encoding="utf-8") as fh:
        D = json.load(fh)
    url = B.SITE + PATH
    arrow = B.ICONS["arrow"]

    # ---- hero chart ----
    gap = "".join(
        '<div class="ax-gap__row"><div class="ax-gap__lab"><span>{l}</span><b>{a}{p}%</b></div>'
        '<div class="ax-gap__track"><div class="ax-gap__fill" style="width:{p}%"></div></div></div>'.format(
            l=h(g["label"]), a="~" if g["approx"] else "", p=g["pct"]) for g in D["gap"])

    # ---- evidence ----
    evidence = "".join(
        '<article class="card ax-ev" data-k="{t}"><p class="ax-num">{n}</p><p class="ax-what">{w}</p>'
        '<p class="ax-src">{s}</p><details><summary>How to read this number</summary>'
        '<p><b>Method.</b> {m}</p><p><b>Caveat.</b> {c}</p></details></article>'.format(
            t=e["theme"], n=h(e["figure"]), w=h(e["finding"]), s=ext(e["url"], e["source"]),
            m=h(e["method"]), c=h(e["caveat"])) for e in D["evidence"])

    # ---- four terms ----
    terms = "".join(
        '<article {a}><div><h3>{t} answers</h3><p class="ax-q">{q}</p></div><dl class="ax-kv">{kv}</dl></article>'.format(
            a=panel_attrs("term", i, "ax-term"), t=h(t["term"]), q=h(t["question"]),
            kv="".join("<dt>%s</dt><dd>%s</dd>" % (h(k), h(v)) for k, v in t["facts"].items()))
        for i, t in enumerate(D["terms"]))

    # ---- frameworks ----
    fw_tabs = tablist("fw", ["%s<small>%s</small>" % (h(f["name"]), h(f["question"])) for f in D["frameworks"]],
                      "Frameworks", "ax-fw__list", vertical=True)
    frameworks = "".join(
        '<article {a}><h3>{n}</h3><p class="ax-fw__k">{k}</p><p>{d}</p><ol>{l}</ol><p>{x}</p>'
        '<div class="ax-two"><div><h4>Use it for</h4>{use}</div><div><h4>Its limit</h4>{lim}</div></div>'
        '<p class="ax-note ax-fw__src">{src}</p></article>'.format(
            a=panel_attrs("fw", i, "ax-fw__panel"), n=h(f["name"]), k=h(f["question"]), d=h(f["summary"]),
            l="".join("<li>%s</li>" % h(x) for x in f["elements"]), x=h(f["detail"]), use=h(f["use"]),
            lim=h(f["limit"]), src=" and ".join(ext(u, s) for s, u in f["sources"]))
        for i, f in enumerate(D["frameworks"]))

    # ---- twelve dimensions ----
    dim_tabs = '<div class="ax-dims" role="tablist" aria-label="The twelve dimensions" data-tabs id="dims">%s</div>' % "".join(
        '<button type="button" role="tab" id="dim-tab-{i}" aria-controls="dim-{i}" aria-selected="{s}" '
        'tabindex="{t}" data-name="{n}">{n}<span>{sc}</span></button>'.format(
            i=i, n=html.escape(d["name"]), sc=h(d["scope"]), s="true" if i == 0 else "false",
            t=0 if i == 0 else -1) for i, d in enumerate(D["dimensions"]))
    dims = "".join(
        '<article {a}><h3>{n}</h3><div><h4>The decision</h4><p>{d}</p></div>'
        '<div><h4>What it should produce</h4><p>{p}</p></div><div><h4>How it fails</h4><p>{f}</p></div></article>'.format(
            a=panel_attrs("dim", i, "ax-dim"), n=h(d["name"]), d=h(d["decision"]), p=h(d["produces"]),
            f=h(d["fails"])) for i, d in enumerate(D["dimensions"]))

    # ---- tools: static parts ----
    tool_tabs = '<div class="ax-tabs" role="tablist" aria-label="Tools" data-tabs>%s</div>' % "".join(
        '<button type="button" role="tab" id="{k}-tab" aria-controls="{k}" aria-selected="{s}" tabindex="{t}">{l}</button>'.format(
            k=k, l=l, s="true" if i == 0 else "false", t=0 if i == 0 else -1) for i, (k, l) in enumerate(TOOLS))
    eu = "".join('<li><time datetime="%s">%s</time>%s</li>' % (e["date"], e["label"], h(e["text"]))
                 for e in D["eu_timeline"])
    kpi = "".join('<tr><th scope="row">%s</th><td>%s</td><td>%s</td></tr>' % (
        h(k["dimension"]), h(k["measure"]), h(k["not"])) for k in D["scorecard"])

    # ---- roadmap ----
    ph_tabs = tablist("phase", ["%d. %s<small>%s</small>" % (i + 1, h(p["phase"]), h(p["months"]))
                                for i, p in enumerate(D["roadmap"])], "Roadmap phases", "ax-phases")
    phases = "".join(
        '<article {a}><div><h3>{n}. {p} <small>{m}</small></h3><ul>{s}</ul></div>'
        '<dl class="ax-kv"><dt>Deliverable</dt><dd>{d}</dd><dt>Gate to pass</dt><dd>{g}</dd></dl></article>'.format(
            a=panel_attrs("phase", i, "ax-phase"), n=i + 1, p=h(p["phase"]), m=h(p["months"]),
            s="".join("<li>%s</li>" % h(x) for x in p["steps"]), d=h(p["deliverable"]), g=h(p["gate"]))
        for i, p in enumerate(D["roadmap"]))

    # ---- cases, priorities, scope, sources ----
    cases = "".join(
        '<article class="ax-case" data-k="{k}"><span class="ax-tag {c}">{tag}</span><h3>{n}</h3><p>{s}</p>'
        '<p class="ax-lesson"><b>Lesson.</b> {l}</p><p class="ax-src">{src}</p></article>'.format(
            k=c["kind"], c="good" if c["kind"] == "scaled" else "caution", tag=h(c["tag"]), n=h(c["name"]),
            s=h(c["story"]), l=h(c["lesson"]), src=ext(c["url"], c["source"])) for c in D["cases"])
    priorities = "".join("<li><div><h3>%s</h3><p>%s</p></div></li>" % (h(p["title"]), h(p["text"]))
                         for p in D["priorities"])
    scope = "".join('<tr><th scope="row">%s</th><td>%s</td><td>%s</td></tr>' % (
        h(r["row"]), h(r["enterprise"]), h(r["national"])) for r in D["scope"])
    types = D["source_types"]
    sources = "".join(
        '<li data-k="{k}"><span><span class="ax-tag">{t}</span></span><div><b>{p}.</b> {a}<p>{n}</p></div></li>'.format(
            k=r["type"], t=types[r["type"]], p=h(r["publisher"]), a=ext(r["url"], r["title"]), n=h(r["note"]))
        for r in D["sources"])

    # ---- related writing: newest strategy-themed essays from data/insights.json ----
    def when(p):
        try:
            return datetime.strptime(p["date"], "%B %d, %Y")
        except Exception:
            return datetime(1900, 1, 1)
    related = sorted([p for p in insights if p.get("theme") == "strategy" and p.get("source") == "Medium"],
                     key=when, reverse=True)[:3]
    related_cards = "".join(
        '<a class="card" href="{u}" rel="noopener" target="_blank"><span class="card__num">{d} · {s}</span>'
        '<h3 dir="auto">{t}</h3><span class="card__link">Read {a}</span></a>'.format(
            u=html.escape(p["url"]), d=html.escape(p["date"]), s=html.escape(p["source"]),
            t=html.escape(p["title"]), a=arrow) for p in related)

    toc = "".join('<li><a href="#%s">%s</a></li>' % (k, l) for k, l in TOC)
    year = UPDATED[:4]
    _u = datetime.strptime(UPDATED, "%Y-%m-%d")
    updated_h = "%d %s" % (_u.day, _u.strftime("%B %Y"))

    body = """
<div class="aisx">
<section class="ax-hero" id="top">
  <div class="wrap">
    <div>
      <p class="crumbs"><a href="../index.html">Home</a> / AI Strategy</p>
      <h1><span class="ax-kicker">AI Strategy · an evidence-based executive reference</span>Most organizations use AI. Few can show what it earned.</h1>
      <p class="ax-sub">An executive reference for building, judging and running an AI strategy. It sets out what the research says, which frameworks are worth your time, and gives you working tools for the decisions that follow.</p>
      <div class="btn-row">
        <a class="btn btn--solid" href="#evidence">Read the evidence</a>
        <a class="btn btn--ghost" href="#tools">Open the tools</a>
      </div>
      <p class="ax-byline">By <a href="../about.html" rel="author">Prof. Mamdouh Alenezi</a> · Updated <time datetime="{updated}">{updated_h}</time></p>
    </div>
    <figure class="ax-gap" aria-label="Chart: the gap between AI use and AI value">
      {gap}
      <figcaption>Share of respondents, McKinsey Global Survey on the state of AI, 2026 (1,719 participants). The groups overlap and are not nested. <a href="https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai" target="_blank" rel="noopener">Source</a></figcaption>
    </figure>
  </div>
</section>

<nav class="ax-toc" aria-label="On this page">
  <div class="wrap"><ul id="ax-toc">{toc}</ul></div>
  <div class="ax-progress" id="ax-progress"></div>
</nav>

<section class="ax-band" id="evidence">
  <div class="wrap">
    <h2>What the research says about AI strategy</h2>
    <p class="ax-lede">Every figure here links to its publisher and states how it was produced. Surveys measure what leaders report, definitions of success differ, and none of these numbers is a law of nature. Read them as a pattern.</p>
    {ev_chips}
    <div class="ax-grid3" id="evGrid">{evidence}</div>
    <p class="ax-pull">The pattern across sources: access to models is no longer the constraint. Redesigned workflows, usable data, accountable owners and controls are.</p>
    <details class="ax-plain">
      <summary>Statistics in circulation that this page leaves out</summary>
      <ul>
        <li>A RAND “analysis of 2,400 enterprise AI initiatives” with an 80.3% failure rate and success rates by CEO involvement. RAND’s published study interviewed 65 practitioners and cites the 80% figure as an outside estimate. We could not trace the larger dataset or its percentages to a RAND publication.</li>
        <li>“42% of companies abandoned AI initiatives” credited to Deloitte, with an average sunk cost of $7.2 million. The 42% figure belongs to S&amp;P Global Market Intelligence. We found no primary source for the cost figure.</li>
        <li>MIT’s 95% finding credited to MIT Sloan. It comes from Project NANDA at the MIT Media Lab and is labelled preliminary by its authors.</li>
        <li>Quotations attributed to the Stanford AI Index or to consulting firms that do not appear in the documents they are credited to.</li>
      </ul>
    </details>
  </div>
</section>

<section class="ax-band tint" id="terms">
  <div class="wrap">
    <h2>AI strategy, transformation, governance, implementation: four terms that get used as one</h2>
    <p class="ax-lede">Strategy, transformation, governance and implementation answer different questions and belong to different owners. Programs stall when one is asked to do another’s job.</p>
    {term_tabs}
    {terms}
  </div>
</section>

<section class="ax-band" id="frameworks">
  <div class="wrap">
    <h2>AI strategy frameworks worth using, and what each is for</h2>
    <p class="ax-lede">No single framework is an AI strategy. Each of these does one job well. Pick by the question you need answered.</p>
    <div class="ax-fw">
      {fw_tabs}
      <div class="ax-fw__panels">{frameworks}</div>
    </div>
  </div>
</section>

<section class="ax-band night" id="system">
  <div class="wrap">
    <h2>An AI strategy is a system of twelve decisions</h2>
    <p class="ax-lede">These are not separate workstreams. A use case chosen without checking data, ownership and run cost looks good on a slide and fails in production. Select a dimension to see the decision it forces.</p>
    {dim_tabs}
    <div class="ax-dim-wrap">{dims}</div>
    <p class="ax-note" style="margin-top:16px">The twelve-dimension model is the author’s synthesis, not an external standard.</p>
  </div>
</section>

<section class="ax-band" id="tools">
  <div class="wrap">
    <h2>Working tools for AI strategy decisions</h2>
    <p class="ax-lede">Seven tools you can use in a workshop today. Your entries stay in this browser and are never sent anywhere. The scoring models are management aids to calibrate, not validated instruments.</p>
    <noscript><p class="ax-note">The interactive tools need JavaScript. The scorecard measures and EU AI Act dates below are readable without it.</p></noscript>
    {tool_tabs}

    <div class="ax-panel ax-tool on" id="t-assess" role="tabpanel" aria-labelledby="t-assess-tab" tabindex="0">
      <h3 class="ax-tool__h">AI strategy maturity check</h3>
      <p class="ax-how">Rate each dimension from 1 (ad hoc) to 5 (embedded and measured). Answer for the organization as it runs today.</p>
      <div class="ax-split">
        <div id="assessRows"></div>
        <div class="card ax-result">
          <div class="ax-big" id="assessScore">–</div>
          <p class="ax-note" id="assessBand"></p>
          <div id="radar"></div>
          <h4>Start with</h4>
          <ul id="assessWeak" class="ax-ul"></ul>
          <button class="btn btn--ghost btn--sm" id="assessReset" type="button">Reset ratings</button>
        </div>
      </div>
    </div>

    <div class="ax-panel ax-tool" id="t-prior" role="tabpanel" aria-labelledby="t-prior-tab" tabindex="0">
      <h3 class="ax-tool__h">AI use-case prioritizer</h3>
      <p class="ax-how">Score each use case from 1 to 5 on seven criteria. For complexity and risk, 5 means simple and low-risk. Change the weights to match your risk appetite. A use case scoring 2 or less on data or risk is held whatever its total.</p>
      <div class="ax-tbl"><table id="priorTable"><caption class="ax-vh">Use-case prioritization</caption></table></div>
      <div class="ax-actions">
        <button class="btn btn--solid btn--sm" id="priorAdd" type="button">Add use case</button>
        <button class="btn btn--ghost btn--sm" id="priorCsv" type="button">Download as CSV</button>
        <button class="btn btn--ghost btn--sm" id="priorReset" type="button">Restore examples</button>
        <span class="ax-note" id="priorWeightNote"></span>
      </div>
      <h4 class="ax-sub-h">Ranking</h4>
      <div id="priorRank" aria-live="polite"></div>
    </div>

    <div class="ax-panel ax-tool" id="t-case" role="tabpanel" aria-labelledby="t-case-tab" tabindex="0">
      <h3 class="ax-tool__h">Three-year AI business case</h3>
      <p class="ax-how">A three-year business case. Enter amounts in thousands of any currency. The realization rate discounts gross benefits to what actually reaches the accounts: time saved only counts when the capacity is redeployed or removed.</p>
      <div class="ax-fields">
        <label class="ax-field">Benefits realized (%)<input type="number" id="bcReal" min="0" max="100" step="5" value="60"></label>
        <label class="ax-field">Discount rate (%)<input type="number" id="bcRate" min="0" max="50" step="1" value="10"></label>
      </div>
      <div class="ax-tbl"><table id="bcTable"><caption class="ax-vh">Business case inputs</caption></table></div>
      <div class="ax-kpis" id="bcKpis" aria-live="polite"></div>
      <div id="bcChart"></div>
      <p class="ax-note">Net value = realized benefits − (build + run + change costs). Compare the result with the best non-AI alternative before approving.</p>
    </div>

    <div class="ax-panel ax-tool" id="t-source" role="tabpanel" aria-labelledby="t-source-tab" tabindex="0">
      <h3 class="ax-tool__h">Build, buy, partner or orchestrate</h3>
      <p class="ax-how">Five questions for one capability at a time. The answer is a starting position to test against total cost of ownership, lock-in and data portability.</p>
      <div class="ax-split">
        <div class="ax-qs" id="srcForm"></div>
        <div class="card ax-result" id="srcResult" aria-live="polite"></div>
      </div>
    </div>

    <div class="ax-panel ax-tool" id="t-govern" role="tabpanel" aria-labelledby="t-govern-tab" tabindex="0">
      <h3 class="ax-tool__h">AI governance: decision rights and agent controls</h3>
      <p class="ax-how">Governance is a set of named decision rights plus controls that run continuously. Name an owner for each question, then check the controls you have for agents that act on their own.</p>
      <div class="ax-split">
        <div>
          <h4 class="ax-sub-h" style="margin-top:0">Who decides</h4>
          <div class="ax-tbl" style="margin:12px 0 30px"><table id="govTable"><caption class="ax-vh">Decision rights</caption></table></div>
          <h4 class="ax-sub-h">Controls for agentic AI</h4>
          <div id="agentChecks"></div>
          <div class="ax-meter" aria-hidden="true"><i id="agentMeter"></i></div>
          <p class="ax-note" id="agentNote" role="status"></p>
        </div>
        <div class="card">
          <h4 class="ax-sub-h" style="margin-top:0">EU AI Act dates, as amended in July 2026</h4>
          <p class="ax-note" style="margin:8px 0 18px">The Digital Omnibus on AI (Regulation (EU) 2026/1744) moved the high-risk deadlines. Confirm obligations with counsel.</p>
          <ol class="ax-tl" id="euTl">{eu}</ol>
          <p class="ax-note"><a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj" target="_blank" rel="noopener">AI Act text</a> and <a href="https://www.whitecase.com/insight-alert/eu-ai-omnibus-enters-force-amending-ai-act" target="_blank" rel="noopener">summary of the 2026 amendments</a></p>
        </div>
      </div>
    </div>

    <div class="ax-panel ax-tool" id="t-decide" role="tabpanel" aria-labelledby="t-decide-tab" tabindex="0">
      <h3 class="ax-tool__h">Ten board decisions and the AI scorecard</h3>
      <p class="ax-how">Ten decisions a board should see settled before it funds a major AI program. Tick each one only when a named executive can answer it in writing.</p>
      <div class="ax-meter" aria-hidden="true"><i id="decMeter"></i></div>
      <p class="ax-note" id="decNote" role="status"></p>
      <div id="decList"></div>
      <h4 class="ax-sub-h">What to put on the scorecard</h4>
      <div class="ax-tbl"><table id="kpiTable"><caption class="ax-vh">Scorecard measures</caption><thead><tr><th scope="col">Dimension</th><th scope="col">Measure this</th><th scope="col">Not this</th></tr></thead><tbody>{kpi}</tbody></table></div>
    </div>

    <div class="ax-panel ax-tool" id="t-canvas" role="tabpanel" aria-labelledby="t-canvas-tab" tabindex="0">
      <h3 class="ax-tool__h">One-page AI strategy canvas</h3>
      <p class="ax-how">A one-page strategy canvas. Two or three lines per box is enough. If a box stays empty, that is the next conversation to have.</p>
      <div class="ax-canvas" id="canvas"></div>
      <div class="ax-actions">
        <button class="btn btn--solid btn--sm" id="cvCopy" type="button">Copy as text</button>
        <button class="btn btn--ghost btn--sm" id="cvPrint" type="button">Print this page</button>
        <button class="btn btn--ghost btn--sm" id="cvClear" type="button">Clear canvas</button>
        <span class="ax-status" id="cvStatus" role="status"></span>
      </div>
    </div>
  </div>
</section>

<section class="ax-band tint" id="roadmap">
  <div class="wrap">
    <h2>An AI strategy roadmap: twelve months from diagnosis to scaled value</h2>
    <p class="ax-lede">A sequence that holds for most large organizations. The durations are planning assumptions. The order matters more than the dates.</p>
    {ph_tabs}
    {phases}
  </div>
</section>

<section class="ax-band night" id="cases">
  <div class="wrap">
    <h2>Six documented cases</h2>
    <p class="ax-lede">Three organizations that scaled, three that paid for a gap in strategy or control. Each links to a primary or first-hand source.</p>
    {case_chips}
    <div class="ax-grid3" id="caseGrid">{cases}</div>
  </div>
</section>

<section class="ax-band" id="priorities">
  <div class="wrap">
    <h2>Six priorities, in order</h2>
    <p class="ax-lede">Where the evidence and the frameworks agree on what to do first.</p>
    <ol class="ax-prio">{priorities}</ol>
  </div>
</section>

<section class="ax-band tint" id="scope">
  <div class="wrap">
    <h2>Enterprise AI strategy and national AI strategy are different work</h2>
    <p class="ax-lede">The method overlaps. The stakeholders, instruments and measures of success do not.</p>
    <div class="ax-tbl"><table><caption class="ax-vh">Enterprise and national AI strategy compared</caption><thead><tr><th scope="col"><span class="ax-vh">Aspect</span></th><th scope="col">Enterprise AI strategy</th><th scope="col">National AI strategy</th></tr></thead><tbody>{scope}</tbody></table></div>
    <p class="ax-note" style="margin-top:14px">National strategies also carry choices an enterprise never faces: compute and data infrastructure, language coverage, public-sector adoption, and the regulatory regime itself. The OECD AI Principles are the common reference point for the policy side.</p>
  </div>
</section>

<section class="ax-band" id="sources">
  <div class="wrap">
    <h2>Sources</h2>
    <p class="ax-lede">Ordered roughly by evidentiary weight: independent research and standards first, practitioner surveys next. Consulting surveys are informed and useful, and they are also produced by firms that sell AI work.</p>
    <label class="ax-vh" for="refSearch">Search sources</label>
    <input class="ax-search" id="refSearch" type="search" placeholder="Search sources">
    {ref_chips}
    <ul class="ax-refs" id="refList">{sources}</ul>
    <p class="ax-note" id="refEmpty" hidden>No sources match. Clear the search or choose another type.</p>
  </div>
</section>

<section class="ax-band tint" id="about-this-reference">
  <div class="wrap">
    <div class="ax-about">
      <div>
        <span class="eyebrow">About this reference</span>
        <h2>Prepared by Prof. Mamdouh Alenezi</h2>
        <p class="ax-lede" style="margin-bottom:1rem">General Manager of the SDAIA Academy and Full Professor of Software Engineering. I build and govern national AI and technology capability institutions, and write on AI strategy, governance and agentic software engineering.</p>
        <p class="ax-note">Evidence last checked in {checked}. Figures are reported as published by their sources; survey results describe respondents, not all organizations. Frameworks marked as the author’s synthesis are professional judgment, not external standards. Nothing here is legal advice.</p>
        <div class="btn-row" style="margin-top:1.4rem">
          <a class="btn btn--solid" href="../contact.html">Discuss your AI strategy {arrow}</a>
          <a class="btn btn--ghost" href="../bio.html">Executive bio</a>
          <a class="btn btn--ghost" href="../projects.html#cases">Cases from my own work</a>
          <a class="btn btn--ghost" href="../speaking.html">Speaking topics</a>
        </div>
      </div>
      <div class="card ax-cite">
        <h3>Cite this page</h3>
        <p id="ax-cite-text">Alenezi, M. ({year}). <i>AI Strategy, with evidence: an executive reference.</i> {url}</p>
        <button class="btn btn--ghost btn--sm copy-btn" type="button" data-copy="#ax-cite-text">Copy citation</button>
      </div>
    </div>
    <h3 class="ax-related-h">Related essays on AI strategy</h3>
    <div class="grid grid--3">{related}</div>
    <div class="btn-row" style="margin-top:1.6rem">
      <a class="btn btn--ghost" href="../myblog/">All insights {arrow}</a>
      <a class="btn btn--ghost" href="../publications.html#programme">Research programme {arrow}</a>
      <a class="btn btn--ghost" href="#top">Back to top</a>
    </div>
  </div>
</section>
</div>
<script src="../assets/ai-strategy.js" defer></script>
""".format(gap=gap, toc=toc, evidence=evidence, ev_chips=chips("#evGrid", EV_THEMES, "Filter evidence by theme"),
           term_tabs=tablist("term", [h(t["term"]) for t in D["terms"]], "Terms", "ax-seg"), terms=terms,
           fw_tabs=fw_tabs, frameworks=frameworks, dim_tabs=dim_tabs, dims=dims, tool_tabs=tool_tabs,
           eu=eu, kpi=kpi, ph_tabs=ph_tabs, phases=phases,
           case_chips=chips("#caseGrid", [("all", "All six"), ("scaled", "Scaled"), ("caution", "Cautionary")],
                            "Filter cases"),
           cases=cases, priorities=priorities, scope=scope,
           ref_chips=chips("#refList", [("all", "All")] + list(types.items()), "Filter sources by type"),
           sources=sources, related=related_cards, arrow=arrow, checked=CHECKED, year=year, url=url,
           updated=UPDATED, updated_h=updated_h)

    article = {
        "@context": "https://schema.org",
        "@type": "Article",
        "@id": url + "#article",
        "headline": HEADLINE,
        "alternativeHeadline": "Most organizations use AI. Few can show what it earned.",
        "description": DESCRIPTION,
        "url": url,
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "inLanguage": "en",
        "isAccessibleForFree": True,
        "datePublished": PUBLISHED,
        "dateModified": UPDATED,
        "image": B.SITE + OG_IMAGE,
        "author": {"@type": "Person", "@id": B.SITE + "#person", "name": "Mamdouh Alenezi", "url": B.SITE},
        "publisher": {"@type": "Person", "@id": B.SITE + "#person", "name": "Mamdouh Alenezi", "url": B.SITE},
        "keywords": ", ".join(KEYWORDS),
        "about": [{"@type": "Thing", "name": n} for n in
                  ("AI strategy", "AI governance", "Enterprise AI adoption", "Agentic AI", "AI maturity models")],
        "articleSection": [l for _, l in TOC],
        "citation": [{"@type": "CreativeWork", "name": r["title"], "url": r["url"],
                      "publisher": {"@type": "Organization", "name": r["publisher"]}} for r in D["sources"]],
    }
    crumbs = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": B.SITE},
            {"@type": "ListItem", "position": 2, "name": "AI Strategy", "item": url}]}

    extra_head = (
        '<link rel="stylesheet" href="../assets/ai-strategy.css">\n'
        '<script>document.documentElement.classList.add("ax-js")</script>\n'
        '<meta property="article:published_time" content="%s">\n'
        '<meta property="article:modified_time" content="%s">\n'
        '<meta property="article:author" content="%sabout.html">\n'
        '<meta property="article:section" content="AI Strategy">' % (PUBLISHED, UPDATED, B.SITE))
    page = B.shell(SLUG, TITLE, DESCRIPTION, body, base="../", extra_head=extra_head,
                   extra_ld=[article, crumbs], og_image=OG_IMAGE)
    page = page.replace('<meta property="og:type" content="profile">', '<meta property="og:type" content="article">')
    page = page.replace('<meta property="og:image:alt" content="Portrait of Prof. Mamdouh Alenezi">',
                        '<meta property="og:image:alt" content="AI Strategy, with evidence: the gap between AI use and AI value">\n'
                        '<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">')
    return page
