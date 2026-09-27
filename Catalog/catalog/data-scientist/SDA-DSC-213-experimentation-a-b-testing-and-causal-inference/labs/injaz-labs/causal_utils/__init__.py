"""
causal_utils — the SDA-DSC-213 experimentation toolkit.

Built across Labs 1-7 and reused in the capstone. Import what you need:

    from causal_utils import (hash_assign, srm_check, balance_table,
                              sample_size_proportions, run_length, cuped_adjust,
                              two_proportion_test, regression_effect,
                              peeking_simulation, correct_pvalues,
                              match_nearest, did_twfe, event_study, iv_2sls,
                              decision_plot, decision_memo)

Design rule for everything here: a function returns an ESTIMATE, an
UNCERTAINTY, and enough diagnostic output to argue about it. A function that
returns a bare number invites a bare number in the memo, and that is the
habit this course exists to break.
"""
from .style import use_sdaia_style, NAVY, BLUE, ORANGE, PURPLE, TEAL, SLATE, MUTED, PANEL
from .assignment import (hash_assign, srm_check, SRMResult,
                         standardised_mean_difference, balance_table)
from .power import (sample_size_proportions, sample_size_means, power_for_n,
                    mde_for_n, run_length, RunLengthPlan, cuped_adjust, CupedResult)
from .analysis import (EffectEstimate, two_proportion_test, regression_effect,
                       delta_method_ratio, peeking_simulation, correct_pvalues,
                       always_valid_bound, practical_significance_verdict)
from .quasi import (estimate_propensity, match_nearest, MatchResult, ipw_ate,
                    did_twfe, DiDResult, event_study, iv_2sls, IVResult,
                    rosenbaum_bounds, placebo_outcome_test,
                    random_common_cause_test, subset_refutation)
from .graphs import (InjazDAG, backdoor_adjustment_sets, classify_triple,
                     is_valid_adjustment_set, draw_dag)
from .reporting import (decision_plot, forest_plot, decision_memo,
                        AnalysisPlan, freeze_plan)

__version__ = "1.0.0"
__course__ = "SDA-DSC-213 · Experimentation, A/B Testing and Causal Inference"
