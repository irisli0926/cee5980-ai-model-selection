# Claude final project submission audit

Review the final project from the repository checkout containing this file. The task is to identify corrections needed for CEE/ENGMT 5980 and to report evidence the team can verify. Work independently before comparing notes with another reviewer. Keep your audit read-only and return findings to the person who initiated it.

## Read the submission package

1. Read [Report.pdf](Report.pdf) for layout, page count and visual evidence. Use [Report.md](Report.md) as the searchable text and [Report.docx](Report.docx) for formatting checks when available.
2. Read [RUBRIC.md](RUBRIC.md), the [original rubric](Final_Project_Rubric.docx), [TA_FEEDBACK.md](TA_FEEDBACK.md), the [team response](Response_to_Proposal_Feedback.docx), and [SUBMISSION_REQUIREMENTS.md](SUBMISSION_REQUIREMENTS.md). Consult the [assignment overview](Assignment_Overview.pdf) for the exact requirements. The TA feedback is the previously supplied Assignment 2 text.
3. Read [data and field definitions](../BFCL_GUIDE.md), [decision methods and worked examples](../DECISION_METHODS_AND_EXAMPLES.md), [baseline outcomes](../../results/summary.json), [sensitivity methods](../SENSITIVITY_AND_REVIEW.md), [robustness audit](../DECISION_ROBUSTNESS_AUDIT.md) and [scenario outputs](../../results/decision_robustness_audit.json). For Appendix B, read the [scoring protocol](evidence/QWEN_SCORING_PROTOCOL.md) and [synthetic task logs](evidence/qwen_sandbox_v2.json). Check the repository revision and record it in your review.

## Audit the claims

- **Decision framing and feedback.** Check each Assignment 2 feedback item against the report and current results. Verify that the report motivates a concrete selection problem, explains the two task workflows and emphasizes the quantitative case. Trace how the analysis and the team's review affected a decision or follow-up. Treat the three participants as the design team. Their original individual records and any unresolved authorship questions require confirmation from the team.
- **Data and calculations.** Start with the frozen CSV and manifest. Verify the eligibility rule, metric directions, scope of benchmark cost and P95, candidate identifiers, and the counts and example values in the report. Check the Pareto and weighted rankings separately. Verify the midpoint argument, the scope of the weight-grid counts, the difference between illustrative thresholds and personal preferences, and every highlighted decision in the figures and tables. Check the GLM-4.6 and omitted-row scenarios separately from the baseline. Check the exact joint clarification boundary against the measurements and stated inclusive thresholds. Clarify what remains of the interpretation when an assumption changes.
- **Preference review and experiments.** Verify that the individual scores follow from their reported inputs and value functions. Check that the prose distinguishes recorded inputs, reactions, and final decisions. Check the local Qwen case counts and failure descriptions against the logs. Keep conclusions appropriate to those tested cases and configurations.
- **Presentation and submission.** Check the report against all five rubric categories, the course page-count and format requirements, references, figure and table numbering and readability, technical contributions, and readiness for the one group upload and three separate peer reviews. Treat teammate confirmations and submission receipts as actions still to be verified by the team.

## Reproduce the public analysis if you have a shell

Use a temporary copy of the current checkout with the Python dependencies in [requirements.txt](../../requirements.txt). The generators write output files. Run from that copy so the shared working files remain available for review.

```sh
python analysis.py
python sensitivity.py
python -m scripts.decision_robustness_audit
python scripts/verify_baseline.py
python -m unittest discover -s tests -v
```

Compare the regenerated data, result and figure files with the checked-out copies. The baseline generator also writes a preliminary summary during regeneration. Use the report and current methods documents for the status of team review. If you can only read the repository in a browser, label the checks you performed by inspection and any checks still unverified. Cite a source file, field, row or page for each verification claim.

## Return findings in this format

1. State the revision audited and the evidence you could access. Give separate readiness judgments for the repository analysis and the submission PDF.
2. List **Must fix** issues, then **Polish** suggestions. For each, include a page, figure, table or code location, the criterion or TA comment affected, the evidence, and the smallest proposed change. State when a change requires recomputation or team confirmation.
3. Give a compact five-row rubric crosswalk showing what supports each category and where evidence is incomplete. Include a check for each of the TA feedback concerns. Describe unverified items explicitly.
4. Finish with the remaining submission actions and their owners. After the factual fixes are resolved, suggest targeted Humanizer edits for repetition or awkward phrasing. Preserve numerical claims, units, method names, citations and the qualifying conditions on each result.
