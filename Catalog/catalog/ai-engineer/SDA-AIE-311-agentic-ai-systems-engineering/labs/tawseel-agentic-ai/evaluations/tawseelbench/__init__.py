"""TawseelBench — a reusable SDAIA Academy agent benchmark.

See `docs/TAWSEELBENCH.md` for the full spec and `README.md` in this
directory for how to run it and add a scenario. Every scenario under
`scenarios/` follows the tau-bench-inspired anatomy (SPEC §6): customer
request -> applicable policy -> environment state -> available tools ->
expected state transition -> pass/fail criteria, validated against
`schema.json`.
"""
