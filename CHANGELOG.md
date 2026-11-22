# Change log

## Technical report follow-up (2026-11-21)

Edited the report's Appendices A and B in response to the assignment on PR #12: pinned the robustness code/results and the local Qwen logs/protocol to their audited commits, distinguished the independent baseline verifier from the robustness runner's own checks, and added the sensitivity-test command. Clarified in Section 6 that individual unscreened rankings leave feasibility pending and do not revise the illustrative requirements. Preserved the retrospective timing qualifications and all reported scores.

Validation: independently recalculated all three Table 5 comparisons from the frozen CSV, checked all eight Pareto/feasible sets and the saved inclusive joint-boundary jumps, cross-checked all 18 Qwen trial transcripts/records and both described failures, inspected Figure 4, verified the four pinned files through GitHub, and confirmed all tracked data/results/figures unchanged. Private confirmations remain outside Git. Iris will consolidate the Markdown changes into the Word/PDF pair; this branch does not claim a new rendered report.

## Integrate the independent submission reviews (2026-11-21)

Combined the review record from PR #11 and the analysis audit and documentation corrections from PR #12 on the PR #10 branch. Updated the submission checklist with the report revisions each reviewer owns. Verified the merged documentation and preserved the audited report and analytical artifacts byte for byte.

## Add the final project review package (2026-11-21)

Added the final report in PDF, Word and Git-readable formats, the course rubric and assignment requirements, the original TA feedback transcribed from the proposal-revision discussion, the team's earlier response, and a read-only Claude audit. Linked the package from the repository README and included the synthetic Qwen run evidence that supports the report appendix. The baseline and sensitivity calculations are unchanged.

## Audit candidate eligibility and joint clarification requirements (2026-11-21)

Added a four-scenario candidate-set comparison, exact clarification–P95 feasibility boundary and a worked example of a Pareto configuration that cannot maximize the baseline linear additive score. The audit uses the frozen data, original anchors, profiles and screen. At the original 15 s ceiling, admitting the single excluded GLM-4.6 row changes maximum available clarification from 58% to 63%, while the original profiles keep their unscreened winners. Documented the two flagged-row removals as diagnostics. The baseline, prior sensitivity computations and frozen inputs remain intact. Reproduced all 27 data, result and figure files byte-for-byte in an isolated verification directory, ran the independent baseline audit and passed the seven sensitivity unit tests.

## Independent submission audit and current method status (2026-11-21)

Corrected stale pending-integration and review-status wording in the sensitivity guide while preserving its historical task-start and cross-review notes. Added a revision-specific public analysis audit that separates integrated main from the unmerged candidate-set extension. No raw data, code, value functions, weights, thresholds or numerical artifacts changed. Course-report findings and participant-specific calculations remain in ignored local materials.

Validation: reproduced all five requested audit commands at revision `339b5b42fcb96194b1b49d3ebe744908879bbe68` in an isolated archive; all seven sensitivity tests passed and all 27 data/result/figure files were byte-identical after regeneration. Checked the merged integration PR and the open extension PR, the documentation links and private exclusions. The public note distinguishes independent scalar baseline verification from the extension runner's internal assertions. Original participant confirmations, the course template and submission approvals remain team checks.

## Integrate the final project analyses (2026-11-21)

Combined the BFCL source audit, independent baseline verification and examples, and sensitivity and preference-review extension. Retained the frozen source, the 66-configuration suffix-based baseline, all value functions and illustrative thresholds. Clarified that the excluded GLM-4.6 (FC thinking) passes the clarification screen and that the completed individual preference review is documented privately. Reproduced the baseline and sensitivity outputs, ran the independent audit, passed all seven sensitivity tests and executed all six notebook cells. All 25 data, result and figure files in the verification run matched the integrated versions byte for byte.

## Review outcomes and evidence timing — 2026-11-21

The preference-review protocol now records retained settings, deferred choices and requests for further evidence alongside numerical revisions. Retrospective session summaries preserve the reported dates and their precision, with a separate audit date. The public sensitivity interpretation points to current private review records, and its generated verification record continues to describe the original sensitivity run.

Prepared the private Member C comparison audit, review synthesis and report handoff. Reproduced the baseline with all existing data/result/figure files byte-identical, checked the saved sensitivity optima independently, verified the private comparison scores and source locators, and passed the seven existing numerical tests. Shared analysis code, frozen inputs and published numerical artifacts retain their recorded specification.

## Confirmed comparison scope and review records — 2026-11-13

Clarified how to freeze a participant's input card for a ranking while cutoff decisions are still open. The protocol records pending feasibility distinctly from a completed screen with zero feasible configurations. It also records the material presented, the participant's reported exposure and questions about interpreting the results. Candidate eligibility, value functions and the illustrative scenarios retain their original specifications.

Verified the frozen snapshot and saved sensitivity hashes, cited scenario outcomes and tied switch points, clarification boundaries, survey item counts and documentation links. Seven existing sensitivity tests passed. Participant records and derived comparisons are kept in the ignored private deliverables.

## Descriptive survey intake and review status — 2026-11-12

Documented how to match an export to the archived survey, record unresolved collection provenance and interpret each paired choice using its own consequence values. Updated the public status of descriptive intake and the confirmation steps for the designated comparison. Item results and the Member C course draft are in the private deliverables. Quantitative input confirmation and matched after-result review remain open. The public diff is limited to documentation.

Checked the private export checksum and the full item tabulation against the archived wording and raw answers. Recalculated the 48 sensitivity optima from saved consequences and checked the cited switches, Pareto counts, screen boundaries and artifact hashes. Verified local links and private Git exclusions.

## General-audience survey revision — 2026-11-05

Revised the live English pilot for people with no project knowledge: one concrete task-assistant scenario, definitions before model comparisons, 13 multiple-choice questions and one optional comment, with all 14 questions skippable. Four hypothetical paired choices hold the other two features fixed and retain no-preference, neither and insufficient-information alternatives. The public protocol now maps every question to descriptive analysis and keeps ordinal ratings, waiting-time intervals and imagined prices separate from benchmark cutoffs and cardinal weights. Quantitative team elicitation remains a separate facilitated module; analytical assumptions and outputs are unchanged.

Observed zero submitted responses before and after the revision, traversed all three published pages without answering or submitting, and verified the saved wording, question options, optional navigation and privacy settings. Preserved the superseded 23-question pilot privately and added the current instrument and an empty response template in ignored deliverables/member_c/. Human comprehension testing and actual completion-time measurement remain pending. Documentation/link and scoped-diff checks were run; experiments were not rerun for these method-only edits.

## Research-backed preference-elicitation protocol — 2026-11-05

Added docs/PREFERENCE_ELICITATION_PROTOCOL.md and linked it from Member C's interpretation. The protocol distinguishes exploratory short-form responses from confirmed quantitative inputs, separates the three team members from optional outside convenience-sample respondents, specifies fixed-range swing ratings and inclusive hard cutoffs, and documents confirmation, missing/unresolved/zero handling and matched after-result review. Based on directly checked AAPOR, Pew, Census and government MCDA guidance, with the distinction between the 2024 public-appraisal cost policy and this course-study cost criterion made explicit.

Prepared and published a separate 23-question, five-section English research pilot; its form links, wording, empty input template and validation notes remain private in ignored deliverables/member_c/. Checked all five pages without submitting a test response, restored the blank draft, checked privacy/navigation settings, and verified question counts/types, fixed anchors, document references and the scoped diff. Actual human cognitive pretesting, confirmed participant inputs and after-result review remain pending. No analysis code, raw data, numerical results or existing short-form answers changed.

## Member C sensitivity extension — 2026-11-05

Added an independent sensitivity runner, numerical counterexample tests, four result tables, a preference-path figure and docs/SENSITIVITY_AND_REVIEW.md. Eight pre-specified scenarios compare linear/log resource values and extreme-row omissions with frozen versus recomputed anchors. All six fixed-anchor omission winners remain stable; log scales change four of six; reanchoring after maximum-cost/union omission changes the structured resource-focused choice. Analytic paths preserve switch-point ties. Requirement diagnostics explain the empty clarification set and raw first-feasible boundaries without adopting relaxed limits. Cross-checked Member B's examples and prepared private, unfilled preference questions; actual review remains incomplete.

Frozen inputs, baseline eligibility, profiles, requirements, shared code/notebook and prior artifacts remain unchanged. No narrower practical candidate rule is adopted while A/B's proposals are unmerged. Validation: baseline reproduction with 18 existing artifacts byte-identical, seven numerical tests, 3,120 independent scalar scenario scores, Pareto checks, complete baseline preference/requirement-grid checks, 3,996 path-point checks, requirement-boundary verification, new-figure review, dependency/compilation and documentation/diff checks. See results/member_c_verification.json and the dated handoff entry.

## Member B baseline verification and decision examples — 2026-11-04

Added docs/DECISION_METHODS_AND_EXAMPLES.md with Pareto/additive/satisficing methods, fixed value anchors, exact configuration consequences, four worked selection cases and three hypothetical create_task illustrations. Added scripts/verify_baseline.py and two verification/reproduction records. Independently checked all eligibility flags, scores/ranks, Pareto sets, optimum ties and both sensitivity grids. Reproduced python analysis.py and all six notebook code cells; existing outputs remained byte-identical and all three figures were inspected. Documented Pareto-first zero-weight tie handling, source-mapping/zero-score caveats and the Member A cross-review; retained illustrative assumptions and the original suffix-based baseline rather than silently applying candidate restrictions. No analytical code, raw data or baseline numerical outputs changed. Recorded Member B ownership and the conditional shared-code handoff to Member C.

## BFCL source audit and data guide (Member A)

Added docs/BFCL_GUIDE.md: version provenance, plain-language explanation of function calling, FC/Prompt and AST, the three test categories with real test entries, a metric dictionary, how Overall Acc, cost and P95 latency are computed, a worked row and an eligibility/comparability audit. Updated DATA_SOURCES.md with the evaluation-code source and corrected metric descriptions. Findings for the active analysis editor: the `(FC)` suffix rule disagrees with the source FC flag for 7 configurations, including GLM-4.6 (FC thinking), which would pass the illustrative clarification screen that currently has 0 feasible rows; two included configurations score 0% on every call-producing category and 100% on Irrelevance Detection, one of them in both Pareto sets and the other setting the P95 anchor; cost mixes API token pricing (27 rows) with a GPU-time estimate (39 rows). Validation: rechecked raw SHA256, reproduced Overall Acc for all 109 rows from the release weights, recomputed the worked balanced score, recounted exclusions, licence groups and resource ranges, and read definitions in the `bfcl-eval==2025.12.17` code and data. No code, raw data, thresholds or results changed; proposed corrections are left to the active analysis editor.

## Plan three-person project completion

Added WORK_PLAN.md with proposed roles for BFCL evidence, decision-model verification/practical examples, and robustness/preference review. Each role owns analytical writing and cross-review; shared analysis code has a sequential handoff. Linked the plan from README, onboarding and handoff. Checked saved-result claims, documentation links, dependencies and public/private boundaries. Assignments and feedback are not assumed confirmed. No analytical assumptions, code or numerical outputs changed.

## Clarify completed analysis and reporting

Updated README with the decision case, completed quantitative work, direct result links and remaining preference review. Independently checked the recorded numerical results. Reviewed the private progress update against its assignment prompt and verified one-page local and native layouts. No analysis code, data or numerical outputs changed.

## Single local workspace

Documented one designated working checkout per computer. Added exclusions for local notes, report exports and archived drafting materials. Consolidation retained source history and verified identical files before removing a redundant project copy. Analysis and numerical results are unchanged.

## Shared handoff and ZIP onboarding

Added HANDOFF.md and required agents to read and maintain it. Documented attaching canonical Git history to an extracted ZIP without overwriting local files, and clarified branch/PR synchronization. Checked referenced paths, ZIP contents and the Git-history attachment procedure. No analysis or numerical outputs changed.

## Initial public baseline

Published a frozen public-data screening analysis: data eligibility audit, two workflow consequence matrices, exact Pareto sets, illustrative weighted/threshold comparisons, sensitivity grids, figures and an executed notebook. Input integrity, dominance, scoring and notebook checks passed. Actual stakeholder preferences remain to be collected privately.
