---
name: sep12-linkedin-round
description: The 12 Sep 2026 round — logged-in LinkedIn came back and is the ONLY channel for hire dates; 4 new 2026 programmes swept via the SDAIA certificate image; 65 records + 20 enrichments + 2 stories. CURRENT TOTAL 2,941 graduates · 106 stories · 62 employers.
type: project
---

> NOTE: project memory was unavailable at the end of the 12 Sep session (the bridge
> reconnected mid-round and the binding was lost). Fold this file into project memory
> as `sep12_linkedin_round.md` and add its index line to MEMORY.md.

**12 September 2026.** Supersedes `sep11-github-sweep` on all counts.

## RULING COUNTS

**2,941 graduates · 106 stories · 62 employers · 6 tracks** — ai **1,439** · ds **795** · genai 249 · dmg 324 · coop 11 · other 123.

## The channel came back — and it is two capabilities, not one

Logged-in LinkedIn was live for the first time in weeks. It is the only channel that yields **hire dates** (`/in/<slug>/details/experience/`), *and* it was the best discovery channel this round. Check `list_connected_browsers` first (the sep07 rule). **Do not trust a `.global-nav` selector to test login — it returned false while the session was fine; read `document.body.innerText` instead.**

`device_bash` was down all round (the Windows-8-Sep mount bug) — the container-only pipeline (stage → edit → commit) ran the whole round. **Mid-round the Chrome extension AND the remote-devices bridge both dropped for ~10 minutes and came back.** Nothing was lost because all work lives in `/home/claude/work`; keep going offline and commit when it returns.

## THE SEARCH LESSON (the reusable one)

**Generic Academy-name queries are worthless; the PROGRAMME NAME in quotes is everything.**
- `"أكاديمية سدايا" معسكر T5` → **1 irrelevant result.**
- `أكاديمية سدايا تخرج` → 17 results, almost all noise.
- `"هندسة البيانات الحديثة لأنظمة الذكاء الاصطناعي"` → **43 profiles, 40 absent from the DB.**

Run ONE noisy generic search — it is what surfaced the programme name that unlocked the other four. Then pivot immediately.

**Mechanics that work on today's LinkedIn:**
- Search DOM has no stable class names and no `data-urn`; `div[class]` matching `/update|result/` returns **zero**. Collect `a[href*="/in/"]` and climb to the nearest ancestor with `textContent.length > 250`.
- Use `textContent`, never `innerText`, in the climb — `innerText` forces layout per ancestor and hangs the 45 s CDP timeout.
- **In-page `setTimeout` loops never finish: the tab is backgrounded and Chrome throttles timers to ~1/min.** Drive scrolling from outside with `computer{action:'scroll'}` + `javascript_tool` pairs; keep `browser_batch` to ~6 actions (11 timed out).
- Never return `location.href` from `javascript_tool` on a search page — the whole result is redacted as query-string data.
- Tool output truncates at ~1.5 KB: return compact `{slug,name,flags}` rows in slices, and inject the DB's known slugs into the page to get back only the new ones.
- **The tabId changes after navigations/disconnects** — re-call `tabs_context_mcp` when a call says the tab is not in the group.

## The evidence that made this round strong: the SDAIA certificate image

Graduates post the **«شهادة اجتياز» / Certificate of Achievement** as an image carrying the **three-part name in Arabic AND English** plus **exact start/end dates**. That is why 14 records have a *verified* Arabic name rather than a transliteration (score 80 vs 75). Dated batches: 17–21 May · 12–16 Jul · 19–23 Jul · 2–6 Aug · 9–13 Aug · 16–20 Aug 2026.

**Distinguish «شهادة اجتياز» (achievement) from «شهادة حضور» (attendance)** — attendance is participation, not completion; score 70 and say so in `d`.

**Certificate templates carry a bilingual title conflict**: several show EN "Developing Generative AI Solutions" with AR «هندسة البيانات الحديثة لأنظمة الذكاء الاصطناعي» **on the same document**, confirmed by a graduate describing her programme as "Developing Generative AI Solutions, focused on Modern Data Engineering for AI". Record as they appear and keep the note — otherwise a later round reads them as duplicates.

## Four 2026 programmes, all hosted at KSU's DAICO

هندسة البيانات الحديثة لأنظمة الذكاء الاصطناعي (23 new) · تطوير حلول الذكاء الاصطناعي التوليدي (20) · هندسة أنظمة الذكاء الاصطناعي الوكيلي المتقدمة (10) · بناء أنظمة وكلاء الذكاء الاصطناعي (12). All with **مركز دايكو، جامعة الملك سعود**.

## Two new rejection rules, both high-yield

1. **THE TRAINER IS NOT A GRADUATE — detect by cross-programme ubiquity.** `mosefbeladi` (Mohammad Albeladi) and `sultan-alsarra` appeared in **all four** programme searches; a graduate's post named them as "guided by". **Count distinct programme searches a slug appears in: 3+ is the staff signature.** (2 is normal — serial graduates are common; several posted two certificates.)
2. **A REACTOR OR A MENTIONED PERSON IS NOT EVIDENCE OF THEMSELVES.** The `a[href*="/in/"]` sweep catches likers ("X and 33 others"), commenters and mentioned team-mates. Require completion language **in that person's own post block**; 11 refused on this. Check block author vs slug with **substring** matching — concatenated vanity slugs (`adelsaqralotaibi`, `mosefbeladi`) defeat token matching.

Match **English completion language too** (`complet|have earned|successfully|Certificate of Achievement`): an Arabic-only regex flagged 13 genuine English posts as evidence-free.

## 20 enrichments instead of 20 duplicates

Twenty candidates matched existing records on the (programme, completion year, window) triple — found earlier via GitHub/supervision links **with no LinkedIn URL**. Added the link + a dated `[إثراء]` sentence, floored score at 80, changed no programme or date. **Slug variants matter: `sarah-alsaed-2706973a7` vs the DB's `sarah-al-saed-2706973a7` are the same profile — dedupe on the numeric suffix too.**

Cross-noted, NOT merged: **#2200 ↔ #2770** «عايدة السويد» — reinforcement exists but a merge needs explicit authorisation.

## Stories: 10 experience pages → 2 published

- **محمد البريح #155** → SDAIA AI Engineer **Dec 2024**; LLM professional training **Sep 2024** — in-window. Host-org exclusion cleared by his own month-dated entry (أسامة الفوزان precedent). His posted job description *is* the LLM stack, so attribution is direct.
- **ريان دحلوي #52** → Abdul Latif Jameel United Finance, Data Science Specialist (AI/BI) **May 2024**; LLM bootcamp **Dec 2023**. New employer → 62.

Refusals cluster: **timing** (شهد الخليفة Dec-2023→Oct-2025; ماهد الجهني year-only 2023→Apr-2025), **pre-program** (الجوهرة البهلال hired Jun 2023 vs Dec 2023 programme), **relatedness** (محمد الثنيان J.P. Morgan infra support; أبرار غندورة IBM application development — both in-window, both refused), **course output** (كميل البصري's "AI & ML Engineer **Trainee** at SDAIA" IS the bootcamp). Deferred: **يزن الكمال #2546**, hired the month the programme ended.

**`emp` is a snapshot and is wrong often enough to check**: #2139 records a traineeship as employment; #2546 names Lucidya while his live experience shows a MawHub internship.

## Counter locations — now SEVEN, and three were already stale

1. `Graduates/index.html` SITE_STATS + TRACKS + prose
2. `SuccessStories/website/js/data.js` SITE_STATS + TRACKS
3. `SuccessStories/website/index.html` **JSON-LD `numberOfItems` — was 100 against 104 stories**
4. portal `index.html` KPIs (**employers KPI was 59 against a ruling 61**), track cards, **derived percentages AND bar widths**, prose, footer
5. `Graduates_Database.md` header (**claimed "100 قصة نجاح عبر 59 جهة عمل"**)
6. xlsx `قاعدة البيانات` sheet
7. xlsx **«إحصاءات»** sheet

**The ar/en footer drift recurred**: Arabic said 11 Sep, English said 8 Sep. Grep the English footer separately.

## Traps hit this round

- **A trailing comma in the STORIES array + a leading comma on insert = an array elision.** Length went 104 → **107** with only 2 objects added; one slot was a hole, and `new Set(ids).size === length` still passed. **Test `arr.length - arr.filter(Boolean).length === 0`**, and check whether the array already ends with a comma before prepending one.
- `data.js` TRACKS lines are **column-aligned** (`value: 772  }`); exact-string replacement fails — anchor with a regex on `en: 'AI Engineer',\s*value:\s*`.
- A dup-detector appending ids to a list reports `[3,3]` for one record carrying the same URL twice — **collect ids into a set** or you get 30 false positives.
- A lazily-loaded `<img>` reports `naturalWidth === 0` until scrolled into view; `await img.decode()` after `scroll_into_view_if_needed` is the real test.

## Mechanics

Container-only pipeline; backups committed first, live files second, standalone last. **The standalone was PATCHED, not rebuilt** — only one new image is referenced and a rebuild needs ~250 asset files staged. The patch reuses the `sdaia.svg` data URI already embedded for the أسامة الفوزان story and inlines `rayan-dahlawi.jpg` fresh: 17.18 → 17.75 MB. Headless-verified directly: **106 cards · 176 imgs · 0 broken · 0 console errors · 0 literal asterisk pairs**.

`~/work/verify.py` recomputes every published figure across all seven locations and asserts ar/en parity, derived percentages, xlsx `row = id + 1` alignment, and cross-record LinkedIn-slug uniqueness. **All checks passed.**

## Next slice

- **The story queue is 172 records** (employer + LinkedIn link + no hire date). Only 10 read. The channel is open — highest-yield work available.
- حمد الباقي **#70** — experience page failed twice; retry.
- Fix `emp`/`role` on **#2139** and **#2546**; re-evaluate #2546 after Aug 2026.
- **#2200 ↔ #2770** merge decision needs authorisation.
- Backup retention: 19 files / 63.7 MB over policy. `device_bash` down so nothing moved — **`Academy/Cleanup_Backups_2026-09-12.ps1`** written for the user to run; it moves, never deletes.
