
"""story/tayseer_storyboard.py — the seven-slide executive arc as a checkable spec.

Each scene declares its message, its arc role, the asset that carries it, and WHY it
earns its place. A slide that does not advance the decision is a candidate for the
appendix, and `audit()` will say so.

The Big Idea is the sentence every scene must be defensible against. If a scene cannot
be justified as "this builds toward that sentence", it is cut.
"""
from __future__ import annotations

from dataclasses import dataclass, field


BIG_IDEA = (
    "Five stalled regions hold national digital adoption 1.2 points below the 65% "
    "target; directing the next SAR 40 million to targeted regional activation there "
    "- rather than to the channel rebuild - is the only option that closes the gap "
    "by December."
)

ARC = "Situation - Complication - Resolution (Minto / SCR)"


@dataclass
class Scene:
    n: int
    arc_role: str            # BLUF | situation | complication | evidence |
                             # options | resolution | ask
    message: str             # the ONE sentence the audience should think (= the title)
    asset: str               # the rendered scene file
    advances_decision: bool
    evidence: str = ""       # the number that makes the message defensible
    sets_up_next: str = ""   # sequence is argument: what question does this raise?


STORYBOARD = [
    Scene(1, "BLUF",
          "Direct the next SAR 40M to the five stalled regions to reach 65% by December",
          "lab5_scene1_bluf.png", True,
          "OPT-A lifts 4 of 5 stalled regions past 65%; OPT-B and OPT-C lift none.",
          "raises: what is the situation that makes this necessary?"),
    Scene(2, "situation",
          "Digital adoption nearly doubled in five years, to 63.8% against a 65% target",
          "lab5_scene2_situation.png", True,
          "34.2% -> 63.8% national, cost per transaction -34%, CSAT +12%.",
          "raises: so why are we not there yet?"),
    Scene(3, "complication",
          "Nine regions sit below target, and five of them have stopped moving",
          "lab5_scene3_complication.png", True,
          "Five Tier-1 regions add under 0.08pp per month; unaided they finish "
          "December about 8.7pp short.",
          "raises: are those regions just small, and is this even fixable?"),
    Scene(4, "evidence",
          "They are not small, and the cause is specific: authentication failures",
          "lab5_scene4_evidence.png", True,
          "15.8% of the population, 12.1% below the national digital-transactions-per-"
          "capita rate, highest unit cost in the country (24.6 vs 14.6 SAR); "
          "authentication is 27% of their tickets versus 17% elsewhere.",
          "raises: what are our options for spending the money?"),
    Scene(5, "options",
          "Three uses of SAR 40M, compared on gap closed per riyal and delivery timing",
          "lab5_scene5_options.png", True,
          "OPT-A 0.0532 pp per SAR m, 6 months to impact; OPT-B 0.0333 and 14 months; "
          "OPT-C 0.0475 and 3 months but no stalled region reaches target.",
          "raises: which one do you recommend?"),
    Scene(6, "resolution",
          "Only targeted regional activation lifts the stalled regions past 65%",
          "lab5_scene6_recommendation.png", True,
          "Projected December: OPT-A 66.0% national and 4 of 5 stalled regions at "
          "target; OPT-B 65.2% and none; OPT-C 65.7% and none.",
          "raises: what exactly are you asking us to approve?"),
    Scene(7, "ask",
          "Approve the reallocation to OPT-A, with a first checkpoint in 90 days",
          "lab5_scene7_ask.png", True,
          "SAR 40M reallocated; 90-day checkpoint on adoption slope in the five regions.",
          "closes the arc by restating the BLUF."),
]

APPENDIX = [
    ("Methodology and measure definitions",
     "Needed only if the adoption number is challenged (QA-02); the recommendation "
     "does not depend on it."),
    ("Per-service breakdown, all 36 services",
     "Interesting, but the decision is regional, not per-service."),
    ("Data-quality note on the raw extract",
     "Governance hygiene; no bearing on the allocation choice."),
    ("The full Module 4 dashboard",
     "Exploratory artefact. Showing it live invites filter-by-filter narration and "
     "loses the arc."),
    ("Per-region allocation table for OPT-A",
     "Detail behind scene 6; produce it only if the committee asks how the SAR 40M "
     "splits across the five regions."),
    ("Do-nothing December projection by region",
     "Supports scene 3; keep in reserve for QA-04 'what happens if we do nothing?'."),
]


def audit(storyboard=STORYBOARD, appendix=APPENDIX, verbose: bool = True) -> dict:
    """Fail the storyboard if it breaks the executive-arc contract."""
    assert storyboard[0].arc_role == "BLUF", "Recommendation must lead (BLUF)."
    assert storyboard[-1].arc_role == "ask", "The arc closes on an explicit ask."
    weak = [s.n for s in storyboard if not s.advances_decision]
    assert not weak, f"Slides not advancing the decision -> appendix: {weak}"
    assert len(storyboard) <= 7, "Executive arc is 7 scenes; the rest is appendix."
    assert len({s.arc_role for s in storyboard}) == len(storyboard), \
        "Each scene plays a distinct arc role."
    missing = [s.n for s in storyboard if not s.evidence]
    assert not missing, f"Every scene needs a defensible number: {missing}"
    objection = any("not small" in s.message.lower() or "per-capita" in s.evidence.lower()
                    or "per-\ncapita" in s.evidence.lower() or
                    "capita" in s.evidence.lower() for s in storyboard)
    assert objection, "Seat the 'aren't those regions just small?' rebuttal in the arc."
    result = {"scenes": len(storyboard), "appendix": len(appendix),
              "arc": ARC, "big_idea": BIG_IDEA, "pass": True}
    if verbose:
        print(f"Storyboard audit: PASS  ({len(storyboard)} scenes, "
              f"{len(appendix)} moved to appendix, 0 non-advancing)")
        print(f"Arc: {ARC}")
        print("Big Idea:")
        print("  " + BIG_IDEA)
    return result


if __name__ == "__main__":
    audit()
