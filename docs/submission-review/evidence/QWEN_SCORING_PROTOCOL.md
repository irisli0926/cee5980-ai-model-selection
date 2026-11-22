# Local Qwen workflow check

Fixed before the revised run on November 21, 2026. Use the same six synthetic cases for each registered configuration, with two complete requests, two deadline clarification requests, and two general questions unrelated to task creation. Each task request explicitly labels its list ID. The date and time are known to the test harness.

A complete request passes if the model makes one valid call containing the requested title, list ID, and deadline, one exact task is saved to an in-memory SQLite store, and the model confirms the save without an extra tool call. Equivalent timestamps at the same absolute instant are accepted if they include a UTC offset. Title matching ignores case and surrounding space.

A clarification case additionally requires a request for the missing deadline before the fixture supplies it and no first-turn tool call. A request can be expressed as a question or a direct request for the information. Review the resulting exchanges for semantic correctness and flag redundant questions separately. An unrelated case passes the behavioral check if there is a visible relevant answer, no tool call or attempted imitation of a call, and no saved record. This check evaluates whether the model abstains from the task tool. Answer quality is outside the scoring rule.

Run the installed Qwen configurations sequentially with the same Ollama API, thinking-disabled request, temperature 0, seed 42, 4,096-token context, and output cap 768. Record registered digests, runner, and quantization. Retain pilot results and revised runs in separate files. Report case counts and failure mechanisms, without combining tests with BFCL or estimating model-size effects or deployment-wide success rates.

The pilot used ordinary list wording and gated the follow-up on a question mark. A valid request phrased as an instruction was blocked, and several models asked whether the supplied list was an ID. The revised run addresses both fixture issues across all configurations and keeps the workload and tool contract fixed.
