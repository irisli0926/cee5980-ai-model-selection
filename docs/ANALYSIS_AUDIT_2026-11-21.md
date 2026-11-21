# Independent analysis audit

Auditor: XinruiXu729. Audit date: November 21, 2026, US Eastern time.

## Revisions and scope

The audit inspected `339b5b42fcb96194b1b49d3ebe744908879bbe68`, the requested review revision. Its baseline is the integrated main commit `f849e698b606497abbee91b60401aa744a31e55d`. The candidate-set extension was introduced in `30ef989aae22ec21000206a56986dc6b053fef7a` and is proposed in [PR #10](https://github.com/irisli0926/cee5980-ai-model-selection/pull/10). That PR was open and mergeable when checked; its extension is not part of the audited main baseline.

GitHub redirects the former `scenariofour/cee5980-ai-model-selection` location to `irisli0926/cee5980-ai-model-selection` (repository ID 1429108368). PR #9's merged status and merge commit were checked through GitHub. The existing canonical remote was retained.

This public note covers source integrity and computed evidence. The detailed course-report review, rubric crosswalk, participant arithmetic checks and submission actions are kept in ignored local deliverables. Original participant confirmations, author approvals, the Canvas template and submission receipts were not independently verified. Numerical agreement does not establish those approvals.

## Reproduction

The following commands completed in a disposable archive of the requested revision, using the existing requirements-compatible environment. The shared checkout was not used as the generators' output directory.

```sh
python analysis.py
python sensitivity.py
python -m scripts.decision_robustness_audit
python scripts/verify_baseline.py
python -m unittest discover -s tests -v
```

All seven sensitivity tests passed. All 27 files under `data/`, `results/` and `figures/` in that revision were byte-identical after regeneration. The frozen CSV's SHA256 was `ede5081a24bc5ac7f9b3b09a52af6bcfcd35aa0f1709239fed979db77a8159a6`. This audit did not execute the notebook again or run new model inference.

| Check | Verified evidence |
| --- | --- |
| Eligibility | 109 raw rows, 66 included; the independent verifier checked every eligibility flag and retained consequence. |
| Direction, scales and ties | Percentage values increase; resource values decrease over fixed anchors. The independent verifier checked every profile score, rank and optimum, duplicate policy and zero-weight ties. |
| Baseline Pareto and screen | Structured 30 / 14; clarification 22 / 0. All original profile and screened optima reproduced. |
| Grids | 1,771 preference vectors and 1,071 requirement pairs per workflow; Pareto-first allocations and all feasible counts reproduced. |
| Existing sensitivity | The saved scale, omission, reanchoring, switching-path and single-requirement outputs reproduced byte for byte. |
| Candidate-set extension | The four scenario sets and their outputs reproduced. Baseline / admit GLM / omit flagged / both give row counts 66 / 67 / 64 / 65, structured Pareto counts 30 / 31 / 29 / 30 and clarification Pareto counts 22 / 23 / 22 / 23. |
| Joint clarification boundary | The extension checks both sides of observed P95 boundaries. At 15 s the maximum clarification score is 58% in the baseline and 63% with GLM admitted. At a 60% floor, the first feasible ceiling is 17.66 s versus 13.50 s; thresholds are inclusive. |
| Weighted-sum limitation | The saved exact-decimal midpoint witness strictly improves all four GPT-4.1 consequences. The affine-value argument concerns unscreened scoring, not a deployable midpoint configuration. |

The independent baseline verifier supplies scalar checks for the baseline; the extension's boundary and midpoint checks are assertions in its own runner. Byte-identical regeneration is additional reproduction evidence, not independent proof of every implementation. Definitions and proxy limitations were cross-checked against the integrated [BFCL guide](BFCL_GUIDE.md), [worked methods](DECISION_METHODS_AND_EXAMPLES.md) and the saved source manifest. The BFCL release source was not re-audited in this session.

## Corrections and remaining decisions

The sensitivity guide still described A/B PRs as pending and participant review as wholly unresolved after the integrated handoff had advanced. The accompanying documentation change distinguishes historical task-start notes, the merged analysis, private individual records and unresolved eligibility policy. It preserves the historical generated verification records and all numerical artifacts.

No numerical correction to the audited results was identified. The baseline calculations are ready to support conditional shortlisting. They do not certify a deployment configuration, resolve the cause of zero-call rows, or approve GLM eligibility. The unmerged extension must remain identifiable by revision when used alongside main.

Before reporting a final group decision, the team must verify the original dated comparison records and each member's contribution statement privately. A maintainer should review the extension and the scope of its attached materials before merging it. Course submission readiness is a separate check; this note does not claim a final PDF approval or upload.
