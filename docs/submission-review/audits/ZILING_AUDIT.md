# Submission audit: Ziling

Reviewer focus from [BEFORE_SUBMISSION.md](../BEFORE_SUBMISSION.md): data sources, BFCL fields, eligibility, proxy limitations, framing and response to the TA feedback. The full report was also checked. This file only records findings. It does not edit the report, data or results; Iris applies accepted changes in the Word copy.

## 1. Revision and readiness

- Audited revision `339b5b4` on `work/irisli0926/robustness-audit` (PR #10), 2026-11-21.
- Evidence read: Report.pdf (11 pages, rendered and inspected), Report.md, Report.docx page setup, RUBRIC.md and the original rubric, TA_FEEDBACK.md, the team response, Assignment_Overview.pdf, SUBMISSION_REQUIREMENTS.md, BFCL_GUIDE.md, results/*.csv and *.json, the Qwen protocol and logs.
- Reproduction: ran the five commands in CLAUDE_AUDIT.md in a temporary copy (Python 3.13.18, numpy 2.3.5, pandas 2.2.3, matplotlib 3.11.2). All finished; verifier passed; 7/7 unit tests passed. Every result CSV and JSON matched byte for byte except `cross_configuration_correlations.csv` (last-digit float rounding) and `member_c_verification.json` (one figure hash). The five PNGs differ in bytes but have zero changed pixels above a small threshold. `PRELIMINARY_RESULTS.md` is rewritten by the generator, as CLAUDE_AUDIT.md warns.
- **Repository analysis: ready.** No calculation errors found.
- **Submission PDF: nearly ready.** Numbers are correct. Three framing/feedback fixes and one policy check are needed before sign-off.

Independently recomputed and matched: 109 rows × 36 fields; 66 retained; all 43 exclusions from the suffix rule; Table 2 winners, Pareto 30/22 and feasible 14/0; xLAM-2-32b balanced value 0.873132; Flash-Lite vs xLAM deltas (−9.50, +12.27, 1.67 s, +USD 1.55, lead 0.000168); Gemini-2.5-Flash values; 70B vs 32B deltas and its avoidance (79.11%) and P95 (91.21 s) failures; Opus overall 77.47% and clarification 58%; log-scale winners change in 4 of 6; Qwen3-0.6B values; Command A Reasoning after reanchoring; path switches 36.54% and 98.11%; boundaries 17.66 s and 58%; Table 4 counts and the Nemotron-Ultra/Falcon3-1B swap; 13/30 and 11/22 grid maximizers; GLM-4.6 values and the 58%→63% and 17.66→13.50 s boundary; midpoint 33.75 / 88.805 / 10.89 / 2.41; all Table 5 values from the swing ratings; Table 6 from the raw Qwen logs; 1-inch margins; 9 body pages.

## 2. Must fix

**M1. The title promises a normative vs constructive comparison, but the body never names it.**
- Where: title; Section 1 paragraph 2 ("two lenses"); Section 6 last paragraph.
- Criterion: Cogency; TA items "contribution beyond Assignment 1" and "specific methods".
- Evidence: "normative" appears only in the title. "Constructive" appears once (line 147 of Report.md).
- Smallest change: in Section 1 paragraph 2, name the first lens the normative step (Sections 3 to 5) and the second the constructive step (Section 6), one clause each. Optionally add one sentence in Section 8 saying what each lens contributed in this case. No recomputation.

**M2. The report does not say why this case was chosen.**
- Where: Section 1.
- Criterion: Cogency; TA item "spend significant time thinking about your case study along with clear justification for why this is chosen ... currently lacking".
- Evidence: Section 1 explains why the two workflows differ, but not why a task-management agent and public BFCL data were picked. The team response (October 21) already had this reasoning: a current, prospective design decision, reproducible with public data without building an app or buying model access.
- Smallest change: add two sentences to the end of Section 1 paragraph 3 using that reasoning. No recomputation.

**M3. No AI-use disclosure.**
- Where: whole report.
- Criterion: course AI policy, separate from the rubric.
- Evidence: the analysis, audits and planned Humanizer pass used AI tools. The course policy as Ziling understands it requires prior approval from Dr. Reed for AI use on graded work and, if approved, citing the service, access date, prompts and responses.
- Smallest change: team confirms approval status with Dr. Reed or the TA before upload, then adds the required disclosure (likely an appendix). **Needs team confirmation.**

## 3. Polish

**P1. The two lead clarification candidates are non-commercial models.** Section 7 "Avoidance and resource proxies" and Section 8. Criterion: limitations. Evidence: the snapshot `License` field is `cc-by-nc-4.0` for both xLAM-2-32b-fc-r and xLAM-2-70b-fc-r; Hammer2.1-3b is `qwen-research` and Command A Reasoning is CC-BY-NC. Change: one sentence naming this, since Section 8 recommends evaluating xLAM-2-32b next. The snapshot licence was not checked against the model pages.

**P2. The maximum-latency row is also a flagged row.** Section 5 paragraph 2. Criterion: limitations. Evidence: `robustness_comparisons.csv` removes Ministral-8B-Instruct-2410 in `omit_latency_*`; it is one of the two zero-score rows in Section 7. Change: add a clause linking the two, so readers see the latency anchor comes from a doubtful measurement.

**P3. "Published V4 dataset" should be "published V4 leaderboard results".** Section 2 paragraph 1. The CSV holds scores, not the test data. Wording only.

**P4. Appendix links.** Appendix A links the robustness code to the PR #10 page and Appendix B has no link to the Qwen logs. Change: after PR #10 is merged, link both to a fixed commit, including `docs/submission-review/evidence/qwen_sandbox_v2.json`.

**P5. Stale public status text.** `results/summary.json` and the regenerated `PRELIMINARY_RESULTS.md` say "no group elicitation has occurred"; `results/member_c_verification.json` says participant review is "incomplete". Section 6 of the report says the review was completed. These strings come from `analysis.py` and `sensitivity.py`, so fixing them changes shared code. Not needed for the PDF; optional repo cleanup by the code owners.

## 4. Rubric crosswalk

| Category | Support | Gaps |
| --- | --- | --- |
| Cogency (25) | Clear decision, two workflows, data-to-decision path (Sections 1, 2, 4) | M1, M2 |
| Technical content (25) | Pareto, additive value, screening, log scales, anchors, paths, exact boundaries, candidate-set scenarios, Qwen check; all reproduced | None found |
| Limitations (25) | Section 7, eligibility, zero-call rows, cost mix, conditional preferences | P1, P2 |
| Presentation (15) | Numbered tables 1 to 6, figures 1 to 4, equation, numbered citations, figures in body, 9 body pages, 1-inch margins | Course template use not verifiable from the files; P4 |
| Clarity (10) | Readable, consistent units | Heavy repetition of "illustrative" and "configuration"; Humanizer pass after fixes |

| TA concern | Status |
| --- | --- |
| Specific goals | Addressed in Abstract and Section 1 |
| Beyond Assignment 1 | Partly; M1 |
| More quantitative case work | Addressed; Sections 2 to 5 and Appendix A carry the argument |
| Realistic iterative feedback | Addressed with stated limits; Section 6 |
| Case choice and motivation | Partly; M2 |
| Specific course methods | Addressed in Section 3; the word "satisficing" from the course could label "requirement screening" |

Not verified: use of the Canvas template; whether Report.docx and Report.pdf are identical (HANDOFF says they match); the individual records behind Table 5; Gradescope receipt.

## 5. Remaining actions

| Action | Owner |
| --- | --- |
| Confirm Ziling's row in Table 5 and the contribution sentence in Section 8 | Ziling |
| Confirm AI-use approval and disclosure wording (M3) | All three |
| Apply M1, M2 and accepted Polish items in the Word copy | Iris |
| Cross-check Xinrui's numerical findings | Xinrui |
| Humanizer pass after factual fixes, keeping numbers, units, methods, citations and qualifiers | Iris, then both reviewers |
| PDF sign-off by November 24; Gradescope upload with all members; check receipt | Group submitter |
| Individual Peer Review Form on Gradescope | Each member |
