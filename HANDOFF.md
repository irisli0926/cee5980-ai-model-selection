# Shared project handoff

Canonical repository: https://github.com/scenariofour/cee5980-ai-model-selection
Read this with AGENTS.md and ONBOARDING.md before starting. Fetch canonical main to see integrated updates. Branch entries describe that branch until merged.

## Integrated baseline

The public analysis includes the frozen BFCL snapshot, eligibility audit, consequence matrices, exact Pareto sets, illustrative comparisons, sensitivity results, four figures and an executed baseline notebook. The [source guide](docs/BFCL_GUIDE.md), [decision methods](docs/DECISION_METHODS_AND_EXAMPLES.md) and [sensitivity extension](docs/SENSITIVITY_AND_REVIEW.md) document the integrated A/B/C work.

Source integrity, independent Pareto calculations, scoring checks, notebook execution and figure review were completed for the baseline; details are in results/verification_report.json. These are prior checks, not a claim that every future revision has been validated.

The public baseline uses illustrative profiles and thresholds. The design team completed individual preference comparisons and review in the private course materials. The candidate rule retains 66 configurations by suffix and numeric checks. Zero feasible clarification configurations applies to that set. An excluded row passes all four illustrative clarification thresholds, and a broader eligibility definition would need a verified mapping and recomputation.

## Next useful work

Cross-check the course report against the integrated public source audit, results and private review records. Any future eligibility or proxy-validity revision needs a documented rule and a fresh analysis of both workflows. Continue using the [ownership and review workflow](WORK_PLAN.md) for shared changes.

## Task entries

### 2026-10-21 — work/scenariofour/shared-handoff

- Files: HANDOFF.md, AGENTS.md, ONBOARDING.md, README.md, CHANGELOG.md.
- Completed: added a shared handoff, required future agents to maintain it, and documented setup from a ZIP without overwriting local work. Analytical code and numerical results were unchanged.
- Validation: checked documentation references, public-file exclusions and the distributable ZIP; checked that a ZIP copy can attach canonical Git history while preserving its files.
- Next: teammates open the extracted folder in Codex, read the three onboarding files, connect GitHub and select one of the bounded tasks above.
- Open: teammate task ownership and actual preference inputs remain to be decided.

### 2026-10-21 — work/scenariofour/canonical-workspace

- Files: AGENTS.md, .gitignore, HANDOFF.md, CHANGELOG.md; local filesystem organization.
- Completed: consolidated the owner's project into one designated desktop checkout, retaining Git history and private materials. Removed the identical starter-folder copy; retained chat deliverable access through links to the canonical files. Archived earlier drafting intermediates privately and retained the existing dependency environment.
- Validation: compared both starter folders byte-for-byte before removal; verified report identity before linking, repository history/remote continuity and deliverable links.
- Next: open the designated folder for future tasks; fetch integrated changes and select the next analysis task. Teammates continue with their own local copies and PRs.
- Analysis: no code, input data or numerical results changed.

### 2026-10-21 — work/scenariofour/update-readiness

- Files: README.md, HANDOFF.md, CHANGELOG.md; private status-report edits remain outside Git.
- Completed: clarified the decision, completed analyses, result-file links and remaining preference review in README. Revised the private one-page update to address amendments, resources, progress against the original plan and next milestones. Applied localized Humanizer prose editing while preserving analytical claims.
- Validation: independently rechecked source integrity, 109/66 configuration counts, Pareto counts of 30/22, 14/0 feasible configurations and 1,771/1,071 sensitivity-grid sizes. Verified report content against computed results; rendered both local and native document versions as one page. Public links and private exclusions checked. No analytical results changed.
- Next: finish participant preference review and the bounded sensitivity refinements listed above. The owner will complete remaining private submission identity fields; each member uses their own submission copy.

### 2026-11-03 — work/scenariofour/three-person-completion-plan

- Files: WORK_PLAN.md, README.md, ONBOARDING.md, HANDOFF.md, CHANGELOG.md.
- Completed: added a public three-role completion plan with technical deliverables, section writing, cross-review, acceptance checks, internal targets and Codex starter prompts. Roles are proposed and use neutral labels until teammates claim them; shared analysis editing passes from baseline verification to sensitivity work.
- Validation: checked baseline claims against saved results, local documentation links, file ownership/dependencies, privacy exclusions and the scoped diff. No analysis, notebook, source data or numerical outputs changed; experiments were not rerun for this documentation task.
- Open: teammate role claims and genuine preference responses remain pending. Private course requirements, response records and submission drafts remain excluded.
- Next: each teammate claims one role with their GitHub handle and starts its first bounded deliverable. A maintainer reviews this plan before merging; this branch entry is not integrated context until merged.
- PR: [#5](https://github.com/scenariofour/cee5980-ai-model-selection/pull/5).

### 2026-11-03 — work/zilingyan110-lang/member-a-bfcl-guide

- Owner: zilingyan110-lang. Role claimed: Member A.
- Files: docs/BFCL_GUIDE.md (new), DATA_SOURCES.md, CHANGELOG.md, HANDOFF.md. No edits to analysis.py, the notebook, raw data or results.
- Completed: source audit against the evaluation code the leaderboard names (`bfcl-eval==2025.12.17`); guide with plain-language definitions, real test entries, metric dictionary, Overall Acc/cost/latency formulas, worked row (xLAM-2-32b-fc-r) and eligibility/comparability audit with candidate-restriction options.
- Validation: raw SHA256 matches the manifest; Overall Acc reproduced for 109/109 rows with weights 10/10/10/30/40; worked balanced score 0.8731 matches the saved output; exclusion reasons (43, all from the suffix rule), FC-flag mismatches, cost types (27 API, 39 GPU estimate), licence and range counts recounted from the files. Live leaderboard and blog pages were read only through search-indexed text.
- Open for the active analysis editor (Member B now): decide the mode rule for the 7 rows in guide section 8.2 (GLM-4.6 (FC thinking) would make the clarification screen non-empty) and a validity rule for the two 0%/100% rows in section 8.3. Commercial-use and cost-type restrictions are left as labelled options for Member C, not applied.
- Next: Member B reviews sections 3 to 8 as cross-reviewer; Member A drafts the private context/data/limitations section and later reviews Member C's sensitivity assumptions.
- PR: [#6](https://github.com/scenariofour/cee5980-ai-model-selection/pull/6).

### 2026-11-04 — work/XinruiXu729/member-b-decision-verification

- Owner: XinruiXu729. Role claimed: Member B; initial active analysis editor for this task.
- Files: docs/DECISION_METHODS_AND_EXAMPLES.md, scripts/verify_baseline.py, results/member_b_verification.json, results/member_b_reproduction.json, CHANGELOG.md and this handoff entry.
- Starting state: clean main fast-forwarded to canonical 3acb4a3. Review Member A's unmerged source-audit branch separately; preserve its ownership and changes.
- Completed: reproduced the baseline; added an independent standard-library audit and methods/results prose with four worked selection cases, all-tie policies and three explicitly hypothetical task-call illustrations. Cross-reviewed Member A's PR #6 at b117bd4 against frozen rows and BFCL source checkpoint f7cf735, including seven mode-label disagreements and two all-zero call-score rows; recorded caveats without silently changing eligibility.
- Validation: python analysis.py completed in an isolated requirements-compatible environment; all 16 existing generated artifacts stayed byte-identical. All six notebook code cells executed without errors in an ignored copy. Independent audit verified every eligible consequence, score/rank/Pareto flag, all optima, 1,771 weight vectors and 1,071 requirement pairs per workflow; 30/22 Pareto and 14/0 feasible counts confirmed. Reviewed all three figures, ten documented consequence rows, local links and hypothetical schema/call validity. No analytical code, input, weights, requirements or prior generated outputs changed.
- Review findings: the zero clarification shortlist is conditional on the suffix-based baseline; excluded GLM-4.6 (FC thinking) passes the four frozen requirements. Do not infer failed-run causes solely from zero scores. Member A should refresh its present-tense leaderboard date claim (live page now says 2026-04-12). Pareto-first grid shares omit dominated configurations that would tie at two/four zero-weight boundary vectors; no current Pareto-grid or threshold-grid optimum is tied.
- Handoff to C: no arithmetic correction is needed before working from the existing baseline. After maintainer review of this PR, Member B releases the active shared-code editor role; Member C fetches the integrated handoff before editing shared code. Candidate/validity-rule changes still require an explicit reviewed decision; scale/extreme-row experiments must remain labelled and genuine preference inputs remain private/pending.
- Next: Member C cross-checks these examples, then performs the planned bounded robustness comparisons; Member A reviews the source comments and integrates its own guide via PR. This branch is not merged and does not claim group preference review is complete.
- PR: [#7](https://github.com/scenariofour/cee5980-ai-model-selection/pull/7).

### 2026-11-05 — work/scenariofour/member-c-sensitivity

- Owner: scenariofour. Role claimed: Member C, as assigned by the user. Started from clean canonical main at 3acb4a3 after fetching A/B's pending branches.
- Files: sensitivity.py, tests/test_sensitivity.py, docs/SENSITIVITY_AND_REVIEW.md, results/robustness_comparisons.csv, three results/sensitivity_*.csv tables, results/member_c_verification.json, figures/04_preference_paths.png, CHANGELOG.md and this entry. Private blank preference questions remain in ignored deliverables/member_c/.
- Completed: specified eight scenarios before computation; produced 48 scale/extreme-observation profile comparisons, analytic switching intervals with explicit tied boundaries, requirement-failure partitions and first-feasible boundaries. Added public robustness/review/theory prose and cross-reviewed B's examples at 6b5f761. Prepared identical private questions without inventing responses. Shared analysis.py/notebook and baseline artifacts are unchanged; B's shared-code handoff awaits review/integration of PR #7.
- Findings: fixed-anchor extreme omissions preserve all six profile/workflow winners. Log resource scales change four of six; cost/union omission with reanchoring changes the structured resource-focused winner. Clarification first becomes feasible at a performance floor of 58% or P95 ceiling of 17.66 s when varying that requirement alone; original requirements remain in force. All results are conditional on the existing suffix-based candidate rule.
- Validation: python analysis.py passed and all 18 pre-existing data/result/figure/preliminary artifacts stayed byte-identical. Seven synthetic numerical tests passed; independently checked 3,120 scalar scenario scores, baseline Pareto membership (30/22), all 1,771 preference vectors and 1,071 requirement pairs per workflow, 3,996 interior path points, boundary ties and requirement partitions. Reviewed the new figure. pip check, Python compilation, documentation links and diff whitespace checks passed.
- Open: actual participant responses/review, candidate/validity-rule decisions from A/B, and integration of their unmerged PRs. This extension does not release B's shared-code ownership or establish group consensus.
- Next: A/B review the sensitivity assumptions and outputs; collect three real private preference responses, freeze confirmed comparison inputs, then rerun only approved revisions. Maintainer integrates reviewed PRs and consolidates artifacts.
- PR: [#8](https://github.com/scenariofour/cee5980-ai-model-selection/pull/8); open for review, not merged.

### 2026-11-05 — work/scenariofour/member-c-sensitivity — preference research

- Owner: scenariofour, Member C. Files: docs/PREFERENCE_ELICITATION_PROTOCOL.md, a scoped link in docs/SENSITIVITY_AND_REVIEW.md, CHANGELOG.md and this entry. Live form links, instrument wording, empty input templates and research notes remain in ignored deliverables/member_c/.
- Completed: reviewed primary AAPOR/Pew/Census and government MCDA guidance; documented a question-to-analysis map, swing-weight and hard-cutoff procedure, confirmation gate and matched review. Added explicit separation of team decision participants from optional outside respondents. A separate 23-question English pilot is published; the eight-question form remains exploratory.
- Validation: instrument has five sections, nine short-answer fields, three paragraphs and eleven multiple-choice questions. Checked the saved form after reconnecting, traversed all five live pages using a labelled unsubmitted UI draft, checked NONE/DISCUSS/blank input paths, cleared that draft and observed zero submitted responses. Email collection and public response summaries are off. Checked English wording, anchors against summary.json, source/local links and diff scope. No experiments rerun for this documentation task; analytical inputs and outputs are unchanged.
- Open: actual human comprehension pilot and completion-time measurement, production wording freeze, actual responses and explicit individual input confirmation. Outside answers without follow-up remain exploratory. No scoring rubric was present among the available private references, so no claim of guaranteed grading compliance is made.
- Next: one comparable student explains the cost, P95, cutoff and swing-rating questions in their own words; revise/version the pilot if needed, then collect responses. Confirm full input cards before a designated comparison and document actual revisions after results are shown.
- PR: continues [#8](https://github.com/scenariofour/cee5980-ai-model-selection/pull/8); not merged.

### 2026-11-05 — work/scenariofour/member-c-sensitivity — general-audience survey revision

- Owner: scenariofour, Member C. Files: docs/PREFERENCE_ELICITATION_PROTOCOL.md, docs/SENSITIVITY_AND_REVIEW.md, CHANGELOG.md and this entry. Current/archived instrument copies, form links and empty response templates remain private in ignored deliverables/member_c/. Shared analysis.py, source data and generated numerical outputs were not edited.
- Completed: replaced the technical live pilot with a 14-question English survey for respondents with no project knowledge; 13 multiple-choice questions plus one optional paragraph, all skippable. Added a concrete scenario, definitions and four imaginary model comparisons with the other two features fixed. Public methods specify a question-to-analysis map, per-question denominators and separate missing/uncertain/no-choice categories. Quantitative swing-weight/cutoff elicitation is reserved for a facilitated team session rather than inferred from generic importance answers.
- Validation: observed zero submitted responses before and after editing; traversed all three live pages (5/3/6 questions) without answering or submitting and returned to blank page 1. Checked the saved title, glossary, all comparison choices, optional paragraph, email/sign-in settings and hidden public response summaries. Verified the English instrument structure, archived v1 preservation, headers-only response template, public documentation references, private exclusions and scoped whitespace diff. No experiments rerun; analysis inputs and outputs are unchanged.
- Open: human comprehension pilot and actual completion time; final production wording; real responses; separately confirmed team inputs and matched after-result review. Four scenario choices do not identify cardinal weights or real willingness to pay, and outside convenience responses do not establish team consensus or population preferences.
- Next: ask one person unfamiliar with the project to explain the scenario/terms and one paired choice in their own words; record confusing wording and elapsed time, then freeze the collection version. Analyse public responses descriptively; facilitate the team's quantitative inputs before recomputation.
- PR: continues [#8](https://github.com/scenariofour/cee5980-ai-model-selection/pull/8); not merged.

### 2026-11-12 — work/scenariofour/member-c-sensitivity — descriptive intake and team-review draft

- Owner: scenariofour, Member C. Files: docs/PREFERENCE_ELICITATION_PROTOCOL.md, docs/SENSITIVITY_AND_REVIEW.md, CHANGELOG.md and this entry. The item report and course draft are in ignored private deliverables.
- Completed: matched the descriptive survey export to the archived instrument, prepared the English item-level report and drafted the English robustness, preference and decision-theory sections for team review. Updated the public intake procedure and review status.
- Validation: checked the export checksum, question headers, all item denominators and answer categories, and four A/B mappings. Recalculated the 48 scenario optima and checked cited switches and ties, Pareto counts, screen boundaries, artifact hashes and document links. Checked private Git exclusions.
- Open: collection provenance, prior exposure, quantitative input confirmation and matched after-result review. A/B's PRs are pending and the shared-code handoff still depends on review of #7.
- Next: confirm each participant's dated input card for the designated comparison. Show the resulting consequences and trade-offs, then record any confirmed revisions privately. Resolve candidate and validity rules through the reviewed A/B handoff.
- PR: continues [#8](https://github.com/scenariofour/cee5980-ai-model-selection/pull/8).

### 2026-11-13 — work/scenariofour/member-c-sensitivity

- Owner: scenariofour, Member C. Files: docs/PREFERENCE_ELICITATION_PROTOCOL.md, docs/SENSITIVITY_AND_REVIEW.md, CHANGELOG.md and this entry.
- Completed: documented scoped confirmation for a ranking while cutoff decisions remain open, reporting for pending and empty feasible sets, and how to record exposure and interpretation during review. Participant-specific records and results are kept in ignored private deliverables.
- Validation: checked frozen input and sensitivity artifact hashes, the 48 illustrative cases, tied switch points, clarification boundaries, item-level counts, document links and private exclusions. Seven sensitivity unit tests passed.
- Open: group review is incomplete. A/B's candidate and measurement questions await reviewed integration, and PR #7 still holds the shared-code handoff.
- Next: confirm outstanding input cards privately, review the consequences with participants and record any dated revisions. Follow the reviewed A/B handoff before adopting candidate changes.
- PR: continues [#8](https://github.com/scenariofour/cee5980-ai-model-selection/pull/8).

### 2026-11-21 — work/scenariofour/member-c-sensitivity

- Owner: scenariofour, Member C. Public files: docs/PREFERENCE_ELICITATION_PROTOCOL.md, docs/SENSITIVITY_AND_REVIEW.md, CHANGELOG.md and this entry.
- Completed: clarified how review records represent retained settings, deferred decisions and requests for evidence, and how retrospective dates differ from an audit timestamp. Prepared the private comparison audit, English review synthesis and report handoff in ignored deliverables.
- Validation: baseline reproduction left existing data/result/figure files byte-identical. Checked all 48 saved scenario optima independently, private score calculations and source locators, document links and private exclusions. Seven existing sensitivity tests passed.
- Open: A/B candidate and measurement definitions still need reviewed integration. The shared-code editor handoff remains conditional on PR #7 review.
- Next: review A/B/C's PRs, settle the integrated specification and use the private report handoff for course-report assembly. Regenerate affected numerical outputs only after an integrated analytical change requires it.
- PR: continues [#8](https://github.com/scenariofour/cee5980-ai-model-selection/pull/8).

### 2026-11-21 — work/irisli0926/final-project-integration

- Owner: irisli0926. Integrated PRs [#6](https://github.com/irisli0926/cee5980-ai-model-selection/pull/6), [#7](https://github.com/irisli0926/cee5980-ai-model-selection/pull/7) and [#8](https://github.com/irisli0926/cee5980-ai-model-selection/pull/8) into the integration branch. Resolved the entry insertion conflicts in `CHANGELOG.md` and `HANDOFF.md` while preserving the three original histories.
- Files: integrated A/B/C's guides, scripts, verification records and sensitivity outputs. Updated `README.md`, `PRELIMINARY_RESULTS.md`, `docs/BFCL_GUIDE.md`, `CHANGELOG.md` and this handoff to describe the integrated baseline and its eligibility boundary.
- Validation: reproduced `analysis.py` and `sensitivity.py`, ran `scripts/verify_baseline.py`, passed all seven sensitivity unit tests and all six notebook cells, checked the frozen input and confirmed that all 25 analyzed data, result and figure files were byte-identical after the run. Counts remain 109 source rows, 66 included rows, 30 and 22 Pareto rows, and 14 and 0 rows passing the illustrative screens.
- Open and next: reconcile the report wording with the final reviewed draft and confirm individual contributions privately. The report should name the excluded GLM-4.6 counterexample and explain the unresolved zero-call score pattern. A broader eligibility rule would require an explicit follow-up decision and rerun.

### Entry template

Copy this template for your own branch; preserve existing entries.

- Date / branch / owner (GitHub handle):
- Task and files owned:
- Completed changes:
- Validation run and outcome:
- Open questions / blockers:
- Next concrete step:
- PR link (when available):
