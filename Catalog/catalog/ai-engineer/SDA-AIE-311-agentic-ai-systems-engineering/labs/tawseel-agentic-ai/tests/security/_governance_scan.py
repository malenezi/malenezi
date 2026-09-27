"""Module 8 — the AST-based scanner behind `test_no_prompt_only_rules.py`.

Not a test module itself (no `test_*`/`Test*` symbols) — a shared,
importable implementation so the pytest-style test file and the stdlib
`unittest` mirror (`tests/security/run_without_pytest.py`) run the EXACT
SAME scan rather than two hand-maintained copies that could quietly
diverge (the scan logic below is non-trivial; the existing repo
convention of re-typing assertions in both places is fine for simple
`assert x == y` checks, not for this).

WHAT THIS CATCHES: a monetary threshold (50 / 500 / 5,000 / 9,500 / 50,000
SAR) or an authorisation-rule phrase ("never refund more than", "only
if", "requires approval", their Arabic equivalents) living ONLY inside
text that is actually sent to a model — a `SystemMessage`/`HumanMessage`/
`AIMessage` call's content, or a string assigned to a name containing
`PROMPT` — anywhere under `src/rafeeq/` OTHER than the one deliberately
preserved anti-pattern foil, `reasoning/refund_prompt_only.py` (Module 7's
own teaching example, referenced by name in this repo's SPEC and never
imported by any production call path — see
`test_anti_pattern_file_is_inert` below).

WHAT THIS DELIBERATELY DOES NOT FLAG: docstrings/comments discussing the
limit in prose (documentation, not data sent to a model), and classroom-
table strings like `defence_layers.py`'s `DefenceLayer.catches` fields —
those are printed for humans via `explain_layers()`, never passed to an
LLM and never used to gate a decision, which is the actual distinction
this governance rule cares about. Narrowing to Message-call content and
PROMPT-named assignments is what keeps that distinction precise instead
of matching any string that happens to mention a number and "SAR".
"""
from __future__ import annotations

import ast
import re
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SRC_DIR = REPO_ROOT / "src" / "rafeeq"

# The one intentional anti-pattern foil (Module 7's own worked example,
# named in SPEC and in `flows/refund_flow.py`'s own docstring as the
# "compare every gate here to..." teaching pair). Whitelisted BY NAME,
# with its inertness independently asserted below — this is not a
# loophole, it is the one place this course explicitly wants the bug to
# still exist so participants can watch it fail.
WHITELISTED_ANTI_PATTERN_FILES: frozenset[str] = frozenset({
    "src/rafeeq/reasoning/refund_prompt_only.py",
})

# Files/paths that must NEVER import the whitelisted anti-pattern module —
# the actual guarantee that matters (the foil is inert, not wired into
# any real decision path).
PRODUCTION_PACKAGES: tuple[str, ...] = ("flows", "orchestration", "security", "service")

_MONEY_RE = re.compile(r"\b(50|500|5,?000|9,?500|50,?000)\s*(SAR|ريال)\b", re.IGNORECASE)
_AUTHZ_RULE_RE = re.compile(
    r"(never refund more than|only refund|requires? (human )?approval|"
    r"do not (need|require) approval|no approval needed|"
    r"لا يجوز|دون (الحاجة ل)?أي موافقة|يتطلب موافقة)",
    re.IGNORECASE,
)

_MESSAGE_CALL_NAMES = {"SystemMessage", "HumanMessage", "AIMessage"}
_PROMPT_NAME_RE = re.compile(r"(?i)(^|_)PROMPT(S)?($|_)")


@dataclass(frozen=True)
class Violation:
    file: str          # repo-relative path
    lineno: int
    kind: str           # "money" | "authz_rule"
    snippet: str


def _static_text_of(node: ast.AST) -> str | None:
    """Best-effort: the STATIC text of a string-shaped expression — a
    plain `Constant` string as-is, or a `JoinedStr` (f-string) with only
    its literal `Constant` pieces joined (interpolated `{amount}`-style
    `FormattedValue` pieces cannot contain a hardcoded literal, so they
    are correctly excluded, not just skipped for convenience)."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.JoinedStr):
        parts = [p.value for p in node.values if isinstance(p, ast.Constant) and isinstance(p.value, str)]
        return "".join(parts) if parts else None
    return None


def _docstring_node_ids(tree: ast.AST) -> set[int]:
    """id()s of every Constant node that IS a module/class/function
    docstring (the first statement of that body) — documentation, not
    data sent to a model, and explicitly out of scope for this scan."""
    ids: set[int] = set()
    candidates: list[ast.AST] = [tree]
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            candidates.append(node)
    for node in candidates:
        body = getattr(node, "body", None)
        if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) \
                and isinstance(body[0].value.value, str):
            ids.add(id(body[0].value))
    return ids


def _call_func_name(call: ast.Call) -> str | None:
    if isinstance(call.func, ast.Name):
        return call.func.id
    if isinstance(call.func, ast.Attribute):
        return call.func.attr
    return None


def scan_file(path: Path) -> list[Violation]:
    """Scan ONE .py file for money/authz-rule text living inside a
    Message-call's content or a PROMPT-named assignment. Returns an empty
    list for a file with none (the common case)."""
    try:
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source, filename=str(path))
    except (SyntaxError, UnicodeDecodeError):
        return []  # not this scanner's job to catch unrelated file problems

    docstring_ids = _docstring_node_ids(tree)
    rel = str(path.relative_to(REPO_ROOT))
    violations: list[Violation] = []

    def _check(text: str, lineno: int) -> None:
        if _MONEY_RE.search(text):
            violations.append(Violation(rel, lineno, "money", text.strip()[:160]))
        elif _AUTHZ_RULE_RE.search(text):
            violations.append(Violation(rel, lineno, "authz_rule", text.strip()[:160]))

    for node in ast.walk(tree):
        # Case 1: a SystemMessage/HumanMessage/AIMessage(...) call's
        # `content` kwarg, or its first positional argument.
        if isinstance(node, ast.Call) and _call_func_name(node) in _MESSAGE_CALL_NAMES:
            content_node = None
            for kw in node.keywords:
                if kw.arg == "content":
                    content_node = kw.value
                    break
            if content_node is None and node.args:
                content_node = node.args[0]
            if content_node is not None and id(content_node) not in docstring_ids:
                text = _static_text_of(content_node)
                if text:
                    _check(text, getattr(content_node, "lineno", node.lineno))

        # Case 2: `SOMETHING_PROMPT = "..."` / `f"..."` module- or
        # function-level assignment.
        if isinstance(node, ast.Assign):
            names = [t.id for t in node.targets if isinstance(t, ast.Name)]
            if any(_PROMPT_NAME_RE.search(n) for n in names) and id(node.value) not in docstring_ids:
                text = _static_text_of(node.value)
                if text:
                    _check(text, node.lineno)

    return violations


def scan_tree(root: Path = SRC_DIR, exclude: frozenset[str] = frozenset()) -> list[Violation]:
    """Scan every `.py` file under `root`, skipping any whose repo-
    relative path is in `exclude`."""
    violations: list[Violation] = []
    for path in sorted(root.rglob("*.py")):
        rel = str(path.relative_to(REPO_ROOT))
        if rel in exclude:
            continue
        violations.extend(scan_file(path))
    return violations


def _imports_refund_prompt_only(tree: ast.AST) -> bool:
    """True iff `tree` contains an ACTUAL import of
    `rafeeq.reasoning.refund_prompt_only` — an `import`/`from` statement,
    never a docstring or comment that merely NAMES the module (several
    files legitimately reference it by name as the anti-pattern this
    course contrasts real code against, e.g. `flows/refund_flow.py`'s own
    docstring; mentioning it in prose is not depending on it)."""
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            if any("refund_prompt_only" in alias.name for alias in node.names):
                return True
        if isinstance(node, ast.ImportFrom):
            module = node.module or ""
            if "refund_prompt_only" in module or any(
                "refund_prompt_only" in alias.name for alias in node.names
            ):
                return True
    return False


def anti_pattern_file_importers() -> list[str]:
    """Which files under the PRODUCTION_PACKAGES actually IMPORT
    `reasoning.refund_prompt_only` (a real `import`/`from` statement, not
    a docstring mention) — should always be empty; the whole point of
    whitelisting that file is that nothing real depends on it."""
    importers: list[str] = []
    for pkg in PRODUCTION_PACKAGES:
        pkg_dir = SRC_DIR / pkg
        if not pkg_dir.exists():
            continue
        for path in sorted(pkg_dir.rglob("*.py")):
            try:
                tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            except (SyntaxError, UnicodeDecodeError):
                continue
            if _imports_refund_prompt_only(tree):
                importers.append(str(path.relative_to(REPO_ROOT)))
    return importers
