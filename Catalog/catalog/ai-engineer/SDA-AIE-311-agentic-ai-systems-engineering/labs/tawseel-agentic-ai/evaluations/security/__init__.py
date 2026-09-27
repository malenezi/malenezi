"""Module 8 focused benchmark — guardrails and adversarial robustness.

Thin wrapper over `evaluations/tawseelbench/runner.py`: the `security`
family (TB-037..TB-050, the AgentDojo-style attack corpus) plus a
denial-of-wallet budget check, graded on attack-success rate and PII
egress. See `README.md` in this directory.
"""
