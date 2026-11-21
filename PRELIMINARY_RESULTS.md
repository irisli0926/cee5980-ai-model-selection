# Preliminary results

The frozen input contains 109 configurations. The baseline retains 66 under the `(FC)` suffix and numeric validity rules.
These are completed screening computations, not final deployment recommendations.

**All preference profiles and screening thresholds are illustrative, not stakeholder-elicited.**

## Structured single-turn
- Four-objective Pareto set: 30 configurations.
- balanced: xLAM-2-32b-fc-r (FC)
- quality focused: Hammer2.1-3b (FC)
- resource focused: Gemini-2.5-Flash-Lite (FC)
- Illustrative requirement screen: 14 feasible configurations.
- Best balanced-value feasible candidate(s): Gemini-2.5-Flash (FC)

## Missing-parameter multi-turn
- Four-objective Pareto set: 22 configurations.
- balanced: xLAM-2-32b-fc-r (FC)
- quality focused: xLAM-2-70b-fc-r (FC)
- resource focused: xLAM-2-32b-fc-r (FC)
- Illustrative requirement screen: 0 feasible configurations.
- Best balanced-value feasible candidate(s): none

The zero count applies to the 66-row baseline. The [source audit](docs/BFCL_GUIDE.md#8-eligibility-and-comparability-audit) documents an excluded configuration, GLM-4.6 (FC thinking), that clears the four clarification thresholds.

## Completed checks
- input_hash: passed
- pareto_direction_and_duplicate_checks: passed
- positive_weight_winners_nondominated: passed
- selection_shares_sum_to_one: passed
- manual_score_spot_check: passed

## Boundaries
- Snapshot screening, not confirmation of current endpoint availability.
- Weights and thresholds in these reproduced baseline outputs are illustrative. The later individual review is documented in the private course materials.
- Benchmark-wide cost and P95 latency are not workflow-specific operating metrics.
- Benchmark accuracy is not deployment success probability or output determinism.
- Selection share depends on the specified preference grid and tie handling; it is not empirical probability.
- Linear resource scales use observed eligible-set anchors and are sensitive to range/outliers.
