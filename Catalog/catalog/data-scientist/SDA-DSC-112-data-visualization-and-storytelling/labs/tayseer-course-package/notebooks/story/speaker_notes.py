
"""story/speaker_notes.py — timed speaker notes generated from the Module 5 storyboard.

Delivery is a plan too. Every scene gets a time box and a one-line narration cue, and
the ask is stated twice: once at 0:00 (BLUF) and once at the close.

The generator also produces the HALVED-SLOT version, because a committee chair cutting
your seven minutes to three on the spot is a normal event, not an emergency.
"""
from __future__ import annotations

from story.tayseer_storyboard import BIG_IDEA, STORYBOARD

# seconds per arc role; the sum must fit the slot with headroom for Q&A hand-off
TIME_BOX = {
    "BLUF": 30,
    "situation": 45,
    "complication": 60,
    "evidence": 75,
    "options": 90,
    "resolution": 60,
    "ask": 30,
}

SLOT_SECONDS = 7 * 60
THE_ASK = "Approve the reallocation of SAR 40M to OPT-A; first checkpoint in 90 days."


def build_notes(storyboard=STORYBOARD, time_box=None, slot=SLOT_SECONDS,
                echo: bool = True) -> list[dict]:
    """Return timed notes, one entry per scene. Raises if the plan overruns the slot."""
    time_box = time_box or TIME_BOX
    total = 0
    notes = []
    if echo:
        print(f"OPEN 0:00 — say the ask: {THE_ASK}")
        print(f"          (the Big Idea behind it: {BIG_IDEA})\n")
    for s in storyboard:
        secs = time_box.get(s.arc_role, 45)
        start = total
        total += secs
        note = {
            "n": s.n,
            "arc_role": s.arc_role,
            "starts_at": f"{start // 60}:{start % 60:02d}",
            "ends_at": f"{total // 60}:{total % 60:02d}",
            "seconds": secs,
            "orient": "One line on what the axes are, then the takeaway.",
            "assert": s.message,
            "point_at": "the highlighted mark only — do NOT read the chart",
            "evidence_if_challenged": s.evidence,
        }
        notes.append(note)
        if echo:
            print(f"[{note['starts_at']}–{note['ends_at']}] Slide {s.n} "
                  f"({s.arc_role}, {secs}s)")
            print(f"   Orient : {note['orient']}")
            print(f"   Assert : \"{s.message}\"")
            print(f"   Point  : {note['point_at']}")
            print(f"   If challenged: {s.evidence[:96]}...\n")
    assert total <= slot, f"Over slot by {total - slot}s — cut a scene, do not rush."
    if echo:
        print(f"CLOSE — say the ask AGAIN: {THE_ASK}")
        print(f"Total: {total // 60}:{total % 60:02d} / {slot // 60}:{slot % 60:02d}  "
              f"({slot - total}s headroom for the hand-off)")
    return notes


def halved_slot(storyboard=STORYBOARD, keep=("BLUF", "complication", "ask"),
                echo: bool = True) -> list[dict]:
    """The chair just halved your slot. What survives: the ask, the single strongest
    evidence scene, the ask again."""
    cut = [s for s in storyboard if s.arc_role in keep]
    if echo:
        print("HALVED SLOT (3:00) — what survives:")
    return build_notes(cut, slot=3 * 60, echo=echo)
