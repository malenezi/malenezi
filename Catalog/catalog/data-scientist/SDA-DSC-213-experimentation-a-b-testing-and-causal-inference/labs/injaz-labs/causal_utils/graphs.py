"""
Causal graphs: junctions, d-separation, the backdoor criterion.
Module 6 — Causal Graphs and Confounding.

A DAG is not decoration. It is the set of assumptions you are willing to
defend, written down where a colleague can attack them. The payoff is
mechanical: once the graph is drawn, the adjustment set is derived rather
than argued about.
"""
from __future__ import annotations

from itertools import combinations

import networkx as nx
import numpy as np

__all__ = ["InjazDAG", "backdoor_adjustment_sets", "classify_triple",
           "is_valid_adjustment_set", "draw_dag", "injaz_uploader_dag"]


def injaz_uploader_dag() -> nx.DiGraph:
    """The defended graph for 'does the guided uploader raise completion?'

    Note two deliberate traps:
      * support_calls is a MEDIATOR (uploader -> support_calls -> completed).
        Controlling for it removes part of the very effect being measured.
      * completed is a COLLIDER for digital_literacy and service_complexity.
        Analysing only completed sessions conditions on it and manufactures
        a spurious association.
    """
    g = nx.DiGraph()
    g.add_edges_from([
        ("digital_literacy", "uses_uploader"),
        ("digital_literacy", "completed"),
        ("device_age", "uses_uploader"),
        ("device_age", "completed"),
        ("age", "digital_literacy"),
        ("age", "device_age"),
        ("region", "completed"),
        ("uses_uploader", "support_calls"),   # MEDIATOR
        ("support_calls", "completed"),
        ("uses_uploader", "completed"),       # the effect of interest
        ("service_complexity", "completed"),
    ])
    return g


class InjazDAG:
    """A thin, teachable wrapper over networkx for causal queries."""

    def __init__(self, graph: nx.DiGraph | None = None,
                 treatment: str = "uses_uploader", outcome: str = "completed"):
        self.g = graph if graph is not None else injaz_uploader_dag()
        if not nx.is_directed_acyclic_graph(self.g):
            raise ValueError("Graph contains a cycle — it is not a DAG.")
        self.treatment = treatment
        self.outcome = outcome

    # ---------------------------------------------------------------- paths
    def backdoor_paths(self) -> list[list[str]]:
        """Non-causal paths from T to Y that start with an arrow INTO T.
        Each one is a route for confounding and must be blocked."""
        und = self.g.to_undirected()
        out = []
        for path in nx.all_simple_paths(und, self.treatment, self.outcome):
            if self.g.has_edge(path[1], path[0]):     # arrow into T
                out.append(path)
        return out

    def causal_paths(self) -> list[list[str]]:
        """Directed T -> ... -> Y paths. These carry the effect; never block them."""
        return list(nx.all_simple_paths(self.g, self.treatment, self.outcome))

    def mediators(self) -> set[str]:
        return {n for p in self.causal_paths() for n in p[1:-1]}

    def descendants_of_treatment(self) -> set[str]:
        return set(nx.descendants(self.g, self.treatment))

    def colliders(self, on_paths_only: bool = True) -> list[tuple[str, str, str]]:
        """Collider triples a->b<-c. With `on_paths_only`, restrict to
        colliders that actually sit on a treatment-outcome path and are not
        the outcome itself -- those are the ones that can trap an analyst."""
        out = [t for t in _triples(self.g) if classify_triple(self.g, *t) == "collider"]
        if not on_paths_only:
            return out
        und = self.g.to_undirected()
        mids = {n for p in nx.all_simple_paths(und, self.treatment, self.outcome)
                for n in p[1:-1]}
        return [(a, b, c) for a, b, c in out if b in mids and b != self.outcome]

    # --------------------------------------------------------- adjustment
    def valid_adjustment_sets(self, max_size: int = 3) -> list[set[str]]:
        return backdoor_adjustment_sets(self.g, self.treatment, self.outcome,
                                        max_size=max_size)

    def minimal_adjustment_set(self) -> set[str]:
        sets = self.valid_adjustment_sets()
        if not sets:
            raise RuntimeError(
                "No valid backdoor adjustment set exists in this graph. "
                "The honest answer is 'not identifiable from these variables' "
                "— look for an instrument, a frontdoor path, or a design change.")
        return min(sets, key=len)

    def explain(self) -> str:
        lines = [f"Causal query: effect of '{self.treatment}' on '{self.outcome}'", ""]
        lines.append(f"Causal (directed) paths — DO NOT BLOCK:")
        for p in self.causal_paths():
            lines.append("   " + " -> ".join(p))
        lines.append("")
        lines.append("Backdoor paths — MUST BE BLOCKED:")
        for p in self.backdoor_paths():
            lines.append("   " + " - ".join(p))
        lines.append("")
        med = self.mediators()
        if med:
            lines.append(f"Mediators (NEVER adjust for these): {sorted(med)}")
        col = self.colliders()
        if col:
            lines.append("Colliders (adjusting OPENS a path): "
                         + ", ".join(f"{a}->{b}<-{c}" for a, b, c in col))
        lines.append("")
        try:
            lines.append(f"Minimal valid adjustment set: {sorted(self.minimal_adjustment_set())}")
        except RuntimeError as e:
            lines.append(f"NOT IDENTIFIABLE: {e}")
        return "\n".join(lines)


def _triples(g: nx.DiGraph):
    und = g.to_undirected()
    for b in g.nodes:
        for a, c in combinations(list(und.neighbors(b)), 2):
            yield a, b, c


def classify_triple(g: nx.DiGraph, a: str, b: str, c: str) -> str:
    """chain (a->b->c), fork (a<-b->c), or collider (a->b<-c)."""
    ab, ba = g.has_edge(a, b), g.has_edge(b, a)
    cb, bc = g.has_edge(c, b), g.has_edge(b, c)
    if ab and cb:
        return "collider"
    if ba and bc:
        return "fork"
    if (ab and bc) or (cb and ba):
        return "chain"
    return "unconnected"


def is_valid_adjustment_set(g: nx.DiGraph, treatment: str, outcome: str,
                            adj: set[str]) -> bool:
    """Backdoor criterion: (1) no member is a descendant of the treatment,
    and (2) the set blocks every backdoor path."""
    if adj & (set(nx.descendants(g, treatment)) | {treatment, outcome}):
        return False
    und = g.to_undirected()
    for path in nx.all_simple_paths(und, treatment, outcome):
        if not g.has_edge(path[1], path[0]):
            continue                        # not a backdoor path
        if not _path_blocked(g, path, adj):
            return False
    return True


def _path_blocked(g: nx.DiGraph, path: list[str], adj: set[str]) -> bool:
    for i in range(1, len(path) - 1):
        a, b, c = path[i - 1], path[i], path[i + 1]
        kind = classify_triple(g, a, b, c)
        if kind == "collider":
            desc = {b} | set(nx.descendants(g, b))
            if not (adj & desc):
                return True                 # collider blocks unless conditioned
        else:
            if b in adj:
                return True                 # chain/fork blocked by conditioning
    return False


def backdoor_adjustment_sets(g: nx.DiGraph, treatment: str, outcome: str,
                             max_size: int = 3) -> list[set[str]]:
    """All valid adjustment sets up to `max_size`, smallest first.

    More controls is NOT more rigour: a set containing a mediator or a
    collider will be rejected here, and would have silently biased the
    estimate had you added it by instinct.
    """
    candidates = set(g.nodes) - {treatment, outcome} - set(nx.descendants(g, treatment))
    out = []
    for k in range(0, max_size + 1):
        for combo in combinations(sorted(candidates), k):
            if is_valid_adjustment_set(g, treatment, outcome, set(combo)):
                out.append(set(combo))
    return sorted(out, key=lambda s: (len(s), sorted(s)))


def draw_dag(g: nx.DiGraph, ax=None, treatment=None, outcome=None,
             adjust=(), pos=None, title=None):
    """Render a DAG in the SDAIA palette: treatment blue, outcome orange,
    adjustment set teal, everything else slate."""
    import matplotlib.pyplot as plt
    from .style import NAVY, BLUE, ORANGE, TEAL, SLATE, MUTED
    if ax is None:
        _, ax = plt.subplots(figsize=(8, 5))
    pos = pos or nx.spring_layout(g, seed=7)
    colors = []
    for n in g.nodes:
        if n == treatment: colors.append(BLUE)
        elif n == outcome: colors.append(ORANGE)
        elif n in adjust:  colors.append(TEAL)
        else:              colors.append(SLATE)
    nx.draw_networkx_edges(g, pos, ax=ax, edge_color=MUTED, width=1.6,
                           arrowsize=16, node_size=2600)
    nx.draw_networkx_nodes(g, pos, ax=ax, node_color=colors, node_size=2600,
                           edgecolors="white", linewidths=2)
    nx.draw_networkx_labels(g, pos, ax=ax, font_size=8, font_color="white",
                            font_family="sans-serif")
    if title:
        ax.set_title(title)
    ax.axis("off")
    return ax
