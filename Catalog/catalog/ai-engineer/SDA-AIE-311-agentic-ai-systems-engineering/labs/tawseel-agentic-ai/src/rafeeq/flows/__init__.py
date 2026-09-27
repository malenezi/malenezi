"""Module 7 — flow engineering: business rules as typed state and
deterministic graph branches, never as prompt sentences. Every gate
function in this package (`refund_flow.py`, `reschedule_flow.py`) is a
PURE function of typed state — importable and table-testable with no
langgraph installed (`tests/unit/test_refund_flow.py`,
`test_reschedule_flow.py`); only the `build_*_flow()` graph wiring needs
`langgraph` and is import-guarded.
"""
