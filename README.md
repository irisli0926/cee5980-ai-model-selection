# Selecting AI Agent Models Through Normative and Constructive Decision Analysis

A reproducible case study of multiobjective model screening: how task requirements, preferences and constraints change a shortlist drawn from public Berkeley Function-Calling Leaderboard (BFCL) measurements.

Canonical repository: https://github.com/scenariofour/cee5980-ai-model-selection

**Final project review.** Open the [review package](docs/submission-review/README.md) for the report, rubric, TA feedback and submission requirements. Start an independent [Claude submission audit](docs/submission-review/CLAUDE_AUDIT.md) from this checkout.

## Start with Codex

Clone this repository or open its folder in Codex, then ask:

> Read AGENTS.md, ONBOARDING.md and HANDOFF.md. If this is an extracted ZIP without .git, connect it to the canonical repository using the documented ZIP setup without overwriting local files. Fetch the latest integrated progress, preserve existing changes, and explain the next task. Work on your own branch; when verified, update HANDOFF.md, commit, push and open a PR.

A public repository allows anyone to clone and inspect the project. Pushing to it requires collaborator write access; otherwise use a personal fork and PR. Each teammate signs in to their own GitHub account once. AGENTS.md delegates routine Git operations to Codex; it cannot guarantee conflict-free concurrent edits.

For the proposed three-person work split, deliverables, acceptance checks and role-specific Codex prompts, read [WORK_PLAN.md](WORK_PLAN.md). Each role includes analytical work, writing and cross-review; teammates claim roles with their GitHub handles before starting.

## Reproduce

Use Python 3 with requirements.txt, then run `python analysis.py` and `python sensitivity.py` from this directory. The notebook reproduces the baseline and expects analysis.py and data/ alongside it. Run `python scripts/verify_baseline.py` for an independent audit and `python -m unittest discover -s tests` for the sensitivity tests. No API key or paid inference is required. environment_used.json records versions used for the baseline run.

Run `python -m scripts.decision_robustness_audit` for the [candidate-set scenarios, exact clarification boundary, and comparison of Pareto and weighted optima](docs/DECISION_ROBUSTNESS_AUDIT.md).

## Decision and current stage

The decision is which model configurations to shortlist for a proposed task-management agent under two workflows: structured single-turn calls and missing-parameter clarification. We evaluate workflow score, irrelevant-call avoidance, full-benchmark cost and P95 latency. The outputs show trade-offs and conditional recommendations under specified preferences and requirements.

The project includes a [BFCL source audit](docs/BFCL_GUIDE.md), [independently verified decision methods and worked examples](docs/DECISION_METHODS_AND_EXAMPLES.md), and [sensitivity analysis and review interpretation](docs/SENSITIVITY_AND_REVIEW.md). The public computations use illustrative weights and thresholds. The design team also completed individually specified comparisons and reviewed the trade-offs. The [review report](docs/submission-review/Report.md) summarizes that process.

## Completed data analysis

- Frozen source snapshot and SHA256 manifest: 109 configurations, 66 retained under the recorded `(FC)` suffix and numeric validity rules.
- Consequence matrices for structured single-turn and missing-parameter multi-turn workflows.
- Four-objective Pareto sets: 30 and 22 configurations in the initial run.
- Three illustrative preference profiles, weighted rankings, and an illustrative requirement screen.
- Sensitivity over 1,771 weight vectors and 1,071 requirement pairs per workflow.
- Four figures, descriptive summaries, machine-readable results, sensitivity checks and an executed baseline notebook.

The illustrative requirement screen leaves 14 structured-call configurations feasible and zero clarification configurations feasible within the 66-row baseline. The [eligibility audit](docs/BFCL_GUIDE.md#8-eligibility-and-comparability-audit) identifies GLM-4.6 (FC thinking), an excluded row that would satisfy all four clarification requirements.

Inspect the [preliminary findings](PRELIMINARY_RESULTS.md), [numerical summary](results/summary.json), [eligibility audit](results/eligibility_audit.csv), [weight sensitivity](results/preference_grid_selection_shares.csv) and [requirement sensitivity](results/threshold_grid.csv). The [trade-off figure](figures/01_pareto_tradeoffs.png), [weight-sensitivity figure](figures/02_preference_sensitivity.png) and [requirement-sensitivity figure](figures/03_requirement_sensitivity.png) visualize the computed results. Counts are initial results, not invariants to preserve after justified model changes.

## Files

- analysis.py and analysis.ipynb: reproducible computations and checks.
- data/: public source snapshot, manifest and selected configuration fields.
- results/: eligibility audit, descriptive summaries, Pareto sets, rankings and sensitivity tables.
- figures/: trade-off and sensitivity plots.
- DATA_SOURCES.md: provenance and metric boundaries.
- AGENTS.md: task ownership, checks, branch/push/PR and privacy rules.
- ONBOARDING.md: project framing and remaining analysis tasks.
- HANDOFF.md: current shared context, task handoffs, open issues and next steps.
- CHANGELOG.md: substantive changes and validation.

The designated report and course review materials are versioned under `docs/submission-review/`. Raw participant records and private shared-document links are maintained separately.

## Interpretation boundaries

The application is a prospective design case. Public weights and thresholds are illustrative. Accuracy values are benchmark proxies for the workflows. Reported cost covers the entire benchmark, and latency is environment-dependent. The suffix and numeric screening rules establish eligibility for this analysis. Endpoint availability and evaluation comparability require separate checks.

The same illustrative profiles apply to both workflows. Cost and latency use observed eligible-set minimum and maximum anchors. The sensitivity extension tests alternative resource value scales, extreme observations, and changing anchors. Practical candidate restrictions and deployment-specific requirements would need an explicit decision and further evidence.

Data and source measurements retain their original authorship and applicable terms; this project does not relicense third-party material. See DATA_SOURCES.md.
