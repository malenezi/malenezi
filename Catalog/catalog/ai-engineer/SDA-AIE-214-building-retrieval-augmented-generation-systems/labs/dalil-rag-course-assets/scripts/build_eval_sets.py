#!/usr/bin/env python3
"""
build_eval_sets.py -- derive every evaluation set from the corpus that was
actually generated, so answer keys can never drift from the documents.

SDA-AIE-214, SDAIA Academy.

Outputs
-------
  data/probes/easy.jsonl              5   friendly probes (Lab 1 step 2)
  data/probes/failure_gallery.jsonl   12  adversarial probes, F1-F8 (Lab 1)
  data/retrieval_labels.jsonl         200 labelled queries (Lab 3/4 recall@k)
  data/golden/golden_qa_v1.jsonl      120 golden Q&A with ground truth (Lab 6)
  data/redteam/unanswerable.jsonl     20  must-refuse questions
  data/redteam/staleness.jsonl        12  supersession pairs (Day 4 drill)
  data/redteam/conflict.jsonl         8   two documents disagree
  data/keys/*.json                    instructor answer keys

Design rule: every ground-truth value is READ FROM layer_b_index.json (the
`facts` recorded at generation time) or from the Layer A manifest. Nothing is
typed by hand twice. Regenerate the corpus with a different seed and every
answer key regenerates with it.

Layer A questions are marked `verify: true` and carry `evidence_hint` instead
of a literal answer, because the real SDAIA PDFs are fetched at delivery time
and their pagination/wording is not knowable here. `scripts/verify_golden.py`
resolves them against the fetched corpus and reports any that do not ground.
"""
from __future__ import annotations

import argparse
import json
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_index(p: Path) -> dict:
    return json.loads(p.read_text(encoding="utf-8"))


def w(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"  {len(rows):4d} -> {path.relative_to(ROOT)}")


# --------------------------------------------------------------------------
class Builder:
    def __init__(self, index: dict, seed: int = 4214):
        self.docs = index["documents"]
        self.by_id = {d["doc_id"]: d for d in self.docs}
        self.rng = random.Random(seed)
        self.fam = {}
        for d in self.docs:
            self.fam.setdefault(d["family"], []).append(d)

    # -- helpers -----------------------------------------------------------
    def circulars(self, superseded_only=False):
        out = []
        for d in self.fam.get("circulars", []):
            lbc = d.get("lifecycle_by_corpus") or {}
            if superseded_only and lbc.get("v2") != "superseded":
                continue
            out.append(d)
        return out

    # -- Lab 1 probes ------------------------------------------------------
    def easy(self) -> list[dict]:
        rows = []
        for d in self.fam["hr_policy_digital_en"][:3]:
            rows.append({
                "id": f"easy-{len(rows)+1}", "language": "en",
                "question": f"What does the {d['title_en']} say about the maximum entitlement?",
                "expected_doc_ids": [d["doc_id"]],
                "expected_answer_contains": [f"{d['facts']['max_entitlement_pct']}%"],
                "query_class": "factoid",
                "why": "single document, digital text, English, unambiguous — the baseline "
                       "answers these well, which is exactly why Lab 1 asks them first.",
            })
        it = self.fam["it_procedures"][0]
        rows.append({
            "id": "easy-4", "language": "en",
            "question": f"What is the triage window in the {it['title_en']}?",
            "expected_doc_ids": [it["doc_id"]],
            "expected_answer_contains": [str(it["facts"]["triage_hours"])],
            "query_class": "factoid",
            "why": "DOCX, clean structure, one fact.",
        })
        web = self.fam["intranet_pages"][0]
        rows.append({
            "id": "easy-5", "language": "en",
            "question": f"Which extension do I call for the service desk?",
            "expected_doc_ids": [web["doc_id"]],
            "expected_answer_contains": ["4400"],
            "query_class": "factoid",
            "why": "HTML page, trivially retrievable — establishes the 'it works!' feeling "
                   "that the failure gallery is about to demolish.",
        })
        return rows

    def failure_gallery(self) -> list[dict]:
        """12 probes, one or two per failure class F1-F8."""
        rows: list[dict] = []
        add = rows.append

        # F1 parsing loss -- a figure that lives in a table (XLSX)
        tbl = self.fam["allowance_tables"][0]
        key = [k for k in tbl["facts"] if k.endswith("grade11")][0]
        add({"id": "fg-01", "failure_class": "F1", "language": "en",
             "question": "What is the monthly housing allowance for Grade 11?",
             "expected_doc_ids": [tbl["doc_id"]],
             "expected_answer_contains": [f"{tbl['facts'][key]:,}"],
             "query_class": "tabular",
             "why": "The answer is a cell in an XLSX. A loader that flattens tables with "
                    "' '.join(cells) destroys the Grade-11-to-amount adjacency and the fact "
                    "stops being retrievable at all. Fixed in Module 2."})

        # F1 parsing loss -- scanned Arabic, no text layer
        scan = self.fam["hr_policy_scanned_ar"][0]
        add({"id": "fg-02", "failure_class": "F1", "language": "ar",
             "question": f"ما الحد الأقصى للاستحقاق في {scan['title_ar']}؟",
             "expected_doc_ids": [scan["doc_id"]],
             "expected_answer_contains": [str(scan["facts"]["max_entitlement_pct"])],
             "query_class": "factoid",
             "why": "Image-only Arabic PDF. The naive loader returns an empty string and "
                    "reports success. Fixed in Module 2 (detect-then-OCR)."})

        # F2 chunk boundary damage
        hr_en = self.fam["hr_policy_digital_en"][1]
        add({"id": "fg-03", "failure_class": "F2", "language": "en",
             "question": f"Under the {hr_en['title_en']}, how many working days' notice "
                         f"is required and who approves it?",
             "expected_doc_ids": [hr_en["doc_id"]],
             "expected_answer_contains": [str(hr_en["facts"]["notice_days"]),
                                          "line manager"],
             "query_class": "conditional",
             "why": "Two facts one clause apart. 500-char blind splitting cuts between them, "
                    "so each chunk answers half. Fixed by structure-aware chunking."})

        # F3 semantic miss across languages
        pair_en = self.fam["hr_policy_digital_en"][2]
        add({"id": "fg-04", "failure_class": "F3", "language": "ar",
             "question": f"ما هي شروط {pair_en['title_ar']}؟",
             "expected_doc_ids": [pair_en["doc_id"]],
             "expected_answer_contains": [str(pair_en["facts"]["max_entitlement_pct"])],
             "query_class": "factoid",
             "why": "Arabic query, English document. An English-only embedding model puts "
                    "them in different regions of the vector space. Fixed in Module 3 (bge-m3 "
                    "+ normalisation on BOTH paths)."})

        add({"id": "fg-05", "failure_class": "F3", "language": "ar",
             "question": "ما إجراءات إتلاف البيانات الشخصية بعد انتهاء مدة الاحتفاظ؟",
             "expected_doc_ids": ["data-destruction-guideline"],
             "layer": "A", "verify": True,
             "evidence_hint": "SDAIA Personal Data Destruction Guideline — retention "
                              "expiry and destruction evidence section",
             "query_class": "procedural",
             "why": "Arabic query against the real SDAIA guideline. Tests Arabic "
                    "normalisation on a document nobody in the room wrote."})

        # F4 exact identifier
        circ = self.circulars(superseded_only=True)[0]
        add({"id": "fg-06", "failure_class": "F4", "language": "en",
             "question": f"What figure does Circular {circ['circular_id']} set?",
             "expected_doc_ids": [circ["doc_id"]],
             "expected_answer_contains": [str(circ["facts"]["applicable_figure"])],
             "query_class": "identifier",
             "why": "Dense retrieval blurs exact tokens by design: '10/2024' and '11/2024' "
                    "are near-identical vectors. Only sparse/hybrid fixes this (Module 4)."})

        circ2 = self.circulars()[5]
        add({"id": "fg-07", "failure_class": "F4", "language": "ar",
             "question": f"ما مضمون التعميم رقم {circ2['circular_id']}؟",
             "expected_doc_ids": [circ2["doc_id"]],
             "expected_answer_contains": [str(circ2["facts"]["applicable_figure"])],
             "query_class": "identifier",
             "why": "Same failure, Arabic-Indic digits. Also tests digit normalisation: "
                    "'٤٤/٢٠٢٥' and '44/2025' must reach the same postings."})

        # F5 precision collapse -- near-duplicate policies
        add({"id": "fg-08", "failure_class": "F5", "language": "en",
             "question": "What conditions apply before an entity may publish a dataset as "
                         "open data?",
             "expected_doc_ids": ["open-data-policy"],
             "distractor_doc_ids": ["data-sharing-policy"],
             "layer": "A", "verify": True,
             "evidence_hint": "SDAIA/NDMO Open Data Policy — publication conditions",
             "query_class": "conditional",
             "why": "The Data Sharing Policy is semantically adjacent and will crowd the "
                    "top-k. The reranker's job, and the cleanest live demo of why it earns "
                    "its latency (Module 4)."})

        # F6 context construction / lost in the middle
        add({"id": "fg-09", "failure_class": "F6", "language": "en",
             "question": "List every responsibility assigned to Data Governance across our "
                         "HR policies.",
             "expected_doc_ids": [d["doc_id"] for d in self.fam["hr_policy_digital_en"][:4]],
             "query_class": "multi_hop",
             "why": "Evidence is spread across several chunks; stuffing 16 chunks buries the "
                    "middle ones. Fixed by budgeting + edge ordering (Module 5)."})

        # F7 unanswerable answered confidently
        add({"id": "fg-10", "failure_class": "F7", "language": "en",
             "question": "What is the parental leave entitlement for contractors on "
                         "secondment to a foreign mission?",
             "expected_doc_ids": [], "must_refuse": True,
             "query_class": "unanswerable",
             "why": "Plausible, adjacent to real policies, and absent from the corpus. The "
                    "naive baseline answers it fluently and inventively. This is the probe "
                    "to read aloud."})

        add({"id": "fg-11", "failure_class": "F7", "language": "ar",
             "question": "كم عدد أيام الإجازة المرضية المدفوعة للمتعاقدين بدوام جزئي؟",
             "expected_doc_ids": [], "must_refuse": True,
             "query_class": "unanswerable",
             "why": "Arabic twin of fg-10. Refusal must work identically in both languages; "
                    "systems that refuse in English and confabulate in Arabic are common."})

        # F8 staleness
        add({"id": "fg-12", "failure_class": "F8", "language": "en",
             "question": f"What is the currently applicable figure under Circular "
                         f"{circ['circular_id']}?",
             "expected_doc_ids": [f"{circ['doc_id'].replace('-v1','')}-v2"],
             "stale_doc_ids": [circ["doc_id"]],
             "corpus": "v2",
             "expected_answer_contains": [str(circ["facts"]["applicable_figure"] + 10)],
             "query_class": "identifier",
             "why": "Two editions of the same circular exist in corpus_v2. Without lifecycle "
                    "metadata and filtering, the superseded one wins on lexical overlap. "
                    "This is the Day-4 drill in one probe."})
        return rows

    # -- Lab 3/4 labelled retrieval set ------------------------------------
    # Queries are PARAPHRASES, not restatements of document titles. A labelled
    # set whose queries copy the title measures string overlap and reports
    # recall@10 = 1.00 for BM25 alone -- which teaches participants that their
    # retriever is perfect and that Modules 3 and 4 were a waste of a day.
    # Every query below is written the way a colleague would ask it.
    NATURAL = {
        "remote-work": ("Can I work from home, and what do I have to do to get it approved?",
                        "هل يمكنني العمل من المنزل وما الإجراءات المطلوبة للموافقة؟"),
        "housing-allowance": ("How much do I get towards rent each month?",
                              "كم المبلغ الشهري المخصص للإيجار؟"),
        "travel-allowance": ("What am I paid per day when I travel for work?",
                             "كم يُصرف لي يومياً عند السفر في مهمة عمل؟"),
        "annual-leave": ("How many leave days can I carry into next year?",
                         "كم يوم إجازة يمكن ترحيله إلى السنة القادمة؟"),
        "training-sponsorship": ("If the organisation pays for my course and I leave early, "
                                 "do I owe money back?",
                                 "إذا تحملت الجهة تكاليف دراستي وتركت العمل مبكراً هل أعيد المبلغ؟"),
        "performance-review": ("How does my rating affect my annual increment?",
                               "كيف يؤثر تقديري السنوي على العلاوة؟"),
        "secondment": ("Can I be loaned to another entity and keep my job here?",
                       "هل يمكن إعارتي لجهة أخرى مع الاحتفاظ بوظيفتي؟"),
        "grievance": ("Someone treated me unfairly — how long do I have to complain?",
                      "تعرضت لإجراء غير عادل، كم المدة المتاحة لتقديم تظلم؟"),
        "recruitment-data": ("How long do we keep the CVs of people we did not hire?",
                             "كم مدة الاحتفاظ بالسير الذاتية لمن لم يتم توظيفهم؟"),
        "employee-records": ("When can old staff files be destroyed?",
                             "متى يمكن إتلاف ملفات الموظفين القديمة؟"),
        "disciplinary": ("How long does a written warning stay on my record?",
                         "كم تبقى العقوبة الكتابية مقيدة في ملفي؟"),
    }
    IT_NATURAL = {
        "access-provisioning": "Someone joined my team last week and still cannot log in — "
                               "whose job is it to grant access?",
        "incident-response": "We think customer data may have leaked. Who do we tell and "
                             "how fast?",
        "backup-restore": "How often are backups tested, and what recovery time are we "
                          "committed to?",
        "change-management": "Do I need a committee to approve a config change tonight?",
        "data-export": "A partner abroad wants a copy of our dataset. What has to happen "
                       "first?",
        "llm-gateway": "Am I allowed to paste an internal document into ChatGPT?",
        "vendor-onboarding": "What do we check before signing a supplier who will process "
                             "our data?",
        "device-hardening": "What is the baseline configuration required on laptops?",
        "log-retention": "Who can read the audit trail and how long is it kept?",
        "data-deletion": "A citizen asked us to erase their data — what is the process and "
                         "the deadline?",
    }

    def _topic(self, doc_id: str, prefix: str) -> str:
        rest = doc_id[len(prefix):]
        return re.sub(r"-(en|ar)?-?\d+$", "", rest)

    def retrieval_labels(self, n: int = 200) -> list[dict]:
        rows: list[dict] = []

        # HR: one natural question per topic, answerable from EITHER language
        # edition -- which is the point. An Arabic question whose only answer is
        # in an English PDF is the F3 case, and it must be scored as correct.
        hr_by_topic: dict[str, list[str]] = {}
        for d in self.fam["hr_policy_digital_en"] + self.fam["hr_policy_scanned_ar"]:
            t = self._topic(d["doc_id"], "ndsa-hr-")
            hr_by_topic.setdefault(t, []).append(d["doc_id"])
        for topic, docs in hr_by_topic.items():
            q_en, q_ar = self.NATURAL.get(topic, (topic.replace("-", " "), topic))
            rows.append({"query": q_en, "language": "en", "query_class": "factoid",
                         "relevant_doc_ids": docs, "topic": topic})
            rows.append({"query": q_ar, "language": "ar", "query_class": "factoid",
                         "relevant_doc_ids": docs, "topic": topic,
                         "cross_lingual": True})

        # IT procedures: one natural question each, plus an Arabic mirror for a
        # third of them (the documents are English-only -> pure F3 territory)
        for i, d in enumerate(self.fam["it_procedures"]):
            t = self._topic(d["doc_id"], "ndsa-it-")
            q = self.IT_NATURAL.get(t)
            if not q:
                continue
            rows.append({"query": q, "language": "en", "query_class": "procedural",
                         "relevant_doc_ids": [d["doc_id"]], "topic": t})

        # Identifier queries: bare and embedded, both digit sets
        for d in self.fam["circulars"]:
            corp = d.get("corpus", ["v1", "v2"])
            cid = d["circular_id"]
            ar_cid = cid.translate(str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩"))
            rows.append({"query": f"circular {cid}", "language": "en",
                         "query_class": "identifier",
                         "relevant_doc_ids": [d["doc_id"]], "corpus": corp})
            rows.append({"query": f"ما مضمون التعميم {ar_cid}؟", "language": "ar",
                         "query_class": "identifier",
                         "relevant_doc_ids": [d["doc_id"]], "corpus": corp,
                         "note": "Arabic-Indic digits: fails without digit normalisation"})

        # Tabular: ask for the number, never name the sheet
        for d in self.fam["allowance_tables"]:
            t = d["doc_id"].replace("ndsa-fin-allowance-", "")
            for grade in ("9", "11", "13"):
                rows.append({"query": f"{t.replace('-', ' ')} amount for grade {grade}",
                             "language": "en", "query_class": "tabular",
                             "relevant_doc_ids": [d["doc_id"]]})

        # Intranet: short, under-specified queries -> the AMBIGUOUS class
        for d in self.fam["intranet_pages"][:12]:
            t = self._topic(d["doc_id"], "ndsa-web-")
            rows.append({"query": t.replace("-", " "), "language": "en",
                         "query_class": "ambiguous", "relevant_doc_ids": [d["doc_id"]]})

        for r in rows:
            r.setdefault("corpus", ["v1", "v2"])
        self.rng.shuffle(rows)
        for i, r in enumerate(rows[:n], 1):
            r["qid"] = f"rl-{i:03d}"
        return rows[:n]

    # -- Lab 6 golden set ---------------------------------------------------
    def golden(self, n: int = 120) -> list[dict]:
        rows: list[dict] = []

        def add(q, gt, docs, cls, lang, **kw):
            rows.append({"id": f"g-{len(rows)+1:03d}", "question": q, "ground_truth": gt,
                         "relevant_doc_ids": docs, "query_class": cls, "language": lang,
                         **kw})

        for d in self.fam["hr_policy_digital_en"]:
            f = d["facts"]
            add(f"What is the maximum entitlement under the {d['title_en']}?",
                f"The maximum entitlement is {f['max_entitlement_pct']}% of basic salary.",
                [d["doc_id"]], "factoid", "en")
            add(f"How many working days before the start date must a request under the "
                f"{d['title_en']} be submitted, and who approves it?",
                f"At least {f['notice_days']} working days before the intended start date; "
                f"approval requires the line manager and then Human Resources, and may not "
                f"be sub-delegated below grade {f['min_approval_grade']}.",
                [d["doc_id"]], "conditional", "en")
        for d in self.fam["hr_policy_scanned_ar"]:
            f = d["facts"]
            add(f"ما الحد الأقصى للاستحقاق وفق {d['title_ar']}؟",
                f"الحد الأقصى للاستحقاق هو {f['max_entitlement_pct']} بالمئة من الراتب الأساسي.",
                [d["doc_id"]], "factoid", "ar")
        for d in self.fam["allowance_tables"]:
            for g, label in (("grade9", "Grade 9"), ("grade11", "Grade 11"),
                             ("grade13", "Grade 13")):
                k = [x for x in d["facts"] if x.endswith(g)]
                if not k:
                    continue
                add(f"What is the {d['title_en'].lower()} amount for {label}?",
                    f"{d['facts'][k[0]]:,}", [d["doc_id"]], "tabular", "en")
        for d in self.fam["it_procedures"]:
            add(f"What is the triage window in the {d['title_en']}?",
                f"Assessed within {d['facts']['triage_hours']} hours by the duty engineer "
                f"against the severity matrix.", [d["doc_id"]], "factoid", "en")
        for d in self.circulars():
            add(f"What figure does Circular {d['circular_id']} set?",
                str(d["facts"]["applicable_figure"]), [d["doc_id"]], "identifier", "en")
            add(f"ما القيمة المحددة في التعميم رقم {d['circular_id']}؟",
                str(d["facts"]["applicable_figure"]), [d["doc_id"]], "identifier", "ar")

        # Layer A: real SDAIA regulation. Ground truth is deliberately absent --
        # verify_golden.py fills and checks these against the fetched PDFs.
        layer_a = [
            ("What are the SDAIA AI Ethics Principles?", "ai-ethics-principles",
             "enumeration", "en"),
            ("ما هي مبادئ أخلاقيات الذكاء الاصطناعي الصادرة عن سدايا؟",
             "ai-ethics-principles", "enumeration", "ar"),
            ("Which data classification levels does the national Data Classification "
             "Policy define?", "data-classification-policy", "tabular", "en"),
            ("ما مستويات تصنيف البيانات وفق سياسة تصنيف البيانات؟",
             "data-classification-policy", "tabular", "ar"),
            ("Under the PDPL, what rights does a data subject have?", "pdpl-law",
             "enumeration", "en"),
            ("ما حقوق صاحب البيانات الشخصية بموجب نظام حماية البيانات الشخصية؟",
             "pdpl-law", "enumeration", "ar"),
            ("What conditions must be met before personal data is transferred outside "
             "the Kingdom?", "pdpl-data-transfer-regulation", "conditional", "en"),
            ("What must a transfer risk assessment cover?",
             "pdpl-risk-assessment-guideline", "procedural", "en"),
            ("What does the Generative AI Guideline require government entities to do "
             "before using a public generative AI service?", "genai-guideline-government",
             "conditional", "en"),
            ("ما الضوابط الواجبة قبل استخدام أدوات الذكاء الاصطناعي التوليدي العامة في "
             "الجهات الحكومية؟", "genai-guideline-government", "conditional", "ar"),
            ("What is the difference between the Data Sharing Policy and the Open Data "
             "Policy?", "data-sharing-policy", "comparative", "en"),
            ("Which techniques does the anonymisation guideline describe?",
             "data-anonymization-guideline", "enumeration", "en"),
        ]
        for q, doc, cls, lang in layer_a:
            add(q, "", [doc], cls, lang, layer="A", verify=True,
                evidence_hint=f"resolve against {doc} once corpus/fetch_corpus.py has run")

        # cross-layer multi-hop: internal procedure -> the SDAIA instrument it implements
        for d in self.fam["it_procedures"][:6]:
            ref = (d.get("cites") or ["pdpl-law"])[0]
            add(f"Our {d['title_en']} requires an approval step before execution — which "
                f"SDAIA instrument does it implement, and what does that instrument require?",
                "", [d["doc_id"], ref], "multi_hop", "en", layer="A+B", verify=True,
                evidence_hint="hop 1: the internal procedure; hop 2: the cited SDAIA document")

        self.rng.shuffle(rows)
        return rows[:n]

    # -- red-team sets ------------------------------------------------------
    def unanswerable(self) -> list[dict]:
        qs = [
            ("What is the parental leave entitlement for contractors on secondment?", "en"),
            ("How much is the overseas education allowance for dependants?", "en"),
            ("Which vendor supplies the organisation's payroll system?", "en"),
            ("What is the CEO's mobile number?", "en"),
            ("How many employees resigned last quarter?", "en"),
            ("What is the budget for the data platform programme?", "en"),
            ("Which candidates were rejected in the last recruitment round?", "en"),
            ("What penalties apply under the Labour Law for late salary payment?", "en"),
            ("Does the organisation offer a share option scheme?", "en"),
            ("What is the retirement age set by the pension authority?", "en"),
            ("كم عدد أيام الإجازة المرضية المدفوعة للمتعاقدين بدوام جزئي؟", "ar"),
            ("ما قيمة بدل التعليم لأبناء الموظفين في الخارج؟", "ar"),
            ("من هو مزود خدمة الحوسبة السحابية للهيئة؟", "ar"),
            ("ما ميزانية برنامج التحول الرقمي لهذا العام؟", "ar"),
            ("كم عدد الموظفين في إدارة الشؤون القانونية؟", "ar"),
            ("ما هي أسماء أعضاء لجنة التظلمات؟", "ar"),
            ("ما موعد صرف الرواتب في شهر رمضان؟", "ar"),
            ("What is the weather forecast for Riyadh tomorrow?", "en"),
            ("Recommend a restaurant near the head office.", "en"),
            ("ما نتيجة مباراة الهلال أمس؟", "ar"),
        ]
        return [{"id": f"un-{i:02d}", "question": q, "language": lang,
                 "must_refuse": True,
                 "trap": ("out-of-scope" if i > 17 else "plausible-but-absent")}
                for i, (q, lang) in enumerate(qs, 1)]

    def staleness(self) -> list[dict]:
        rows = []
        for i, d in enumerate(self.circulars(superseded_only=True), 1):
            base = d["doc_id"].replace("-v1", "")
            rows.append({
                "id": f"st-{i:02d}",
                "question": f"What is the currently applicable figure under Circular "
                            f"{d['circular_id']}?",
                "question_ar": f"ما القيمة المطبقة حالياً بموجب التعميم رقم "
                               f"{d['circular_id']}؟",
                "language": "en",
                "stale_doc_id": d["doc_id"], "current_doc_id": f"{base}-v2",
                "stale_value": str(d["facts"]["applicable_figure"]),
                "current_value": str(d["facts"]["applicable_figure"] + 10),
                "corpus": "v2",
            })
        return rows

    def conflict(self) -> list[dict]:
        rows = []
        for i, d in enumerate(self.circulars(superseded_only=True)[:8], 1):
            base = d["doc_id"].replace("-v1", "")
            rows.append({
                "id": f"cf-{i:02d}",
                "question": f"Two versions of Circular {d['circular_id']} exist. What "
                            f"should we apply, and what changed?",
                "language": "en",
                "doc_ids": [d["doc_id"], f"{base}-v2"],
                "expected_behaviour": "surface both, name the supersession, apply the later",
                "grading": "full credit only if BOTH documents are cited AND the answer "
                           "states which is superseded",
            })
        return rows


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--index", type=Path, default=ROOT / "data/corpus/layer_b_index.json")
    ap.add_argument("--out", type=Path, default=ROOT / "data")
    ap.add_argument("--seed", type=int, default=4214)
    a = ap.parse_args()

    b = Builder(load_index(a.index), seed=a.seed)
    print("Building evaluation sets from the generated corpus:")
    w(a.out / "probes/easy.jsonl", b.easy())
    w(a.out / "probes/failure_gallery.jsonl", b.failure_gallery())
    w(a.out / "retrieval_labels.jsonl", b.retrieval_labels())
    w(a.out / "golden/golden_qa_v1.jsonl", b.golden())
    w(a.out / "redteam/unanswerable.jsonl", b.unanswerable())
    w(a.out / "redteam/staleness.jsonl", b.staleness())
    w(a.out / "redteam/conflict.jsonl", b.conflict())

    key = {
        "note": "INSTRUCTOR KEY — do not distribute before the lab.",
        "failure_gallery_reference": {
            r["id"]: {"class": r["failure_class"], "why": r["why"]}
            for r in b.failure_gallery()},
        "expected_lab1_distribution": {"F1": 2, "F2": 1, "F3": 2, "F4": 2,
                                       "F5": 1, "F6": 1, "F7": 2, "F8": 1},
    }
    (a.out / "keys").mkdir(parents=True, exist_ok=True)
    (a.out / "keys/failure_gallery_key.json").write_text(
        json.dumps(key, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"     -> {(a.out / 'keys/failure_gallery_key.json').relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
