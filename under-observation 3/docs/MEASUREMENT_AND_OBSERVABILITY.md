# Measurement and observability

Updated 24 November 2026. The printed poster is unchanged; this document clarifies the website's analyses.

## Three evidence channels

1. The live auditor uses the instrument's tagged-statement machinery. Exported instrument documentation includes eligible false own-hand claims and broken promises among publicly reportable violations. Absence of promise posts does not establish that promises are unsupported by the implementation.
2. The supplied game-level false-own-resource metrics use a narrower post-game word-based statement measure. The supplied briefing recommends that scorer for hand-claim counts and records known tagging and reading errors. It has not undergone a blind validation established by these exports.
3. The surrogate target is simply whether a response's `speech.acts` list is nonempty. It is model-supplied tag presence, not claim truth, valid-tag count, judged-claim count or natural-language checkability recall.

Original documentation: [instrument briefing](../data/source/INSTRUMENT_BRIEFING.md) and [exported metrics definitions](../data/source/METRICS_INSTRUMENT_2_2.md). These documents are source evidence, not an independent rerun or verification of every engine rule.

## Sparse outcomes

The source metrics contain 75 false classifications among 5,650 checked own-resource claims (about 1.33%). They occur in 46 games; 44 games have none and the maximum is five per game. Splitting the positives by arm and period limits precision. Repeated statements share a game, and the 90 games cover 20 starting-board seeds with repetitions. The matched-seed bootstrap preserves that grouping. The count is not a census of all false or deceptive speech.

Reassessment should review the flags and sample scored-true and unscored statements. A flag-only review cannot measure false negatives. Broader categories need separate definitions for own-hand facts, other-player claims, conditional commitments, plans, ambiguous statements and unresolved outcomes. Changed measurement should be reported alongside the original results, with explicit denominators and no inference of intent solely from contradiction.

## What AUROC evaluates here

Each of 29,147 included response rows receives a probability from a tree trained on other board seeds. The pooled out-of-fold AUROC is 0.5817308483. A full-data tree supplies the displayed rules only. Positive rows are 8,746 (30.0065%). The target differs from the 5,650 own-resource claims; exact claim-to-response overlap has not been reconstructed.

AUROC measures ranking across thresholds, not classification accuracy, truthfulness or monitoring effectiveness. Average precision is 0.34866935 against a tagged share of 0.30006519. Brier score is 0.20640983 against 0.21005679 for training-fold prevalence. The restricted depth-three model has modest predictive fidelity. It omits much of the history Qwen saw; 6,554 of 35,701 prompted post-setup records lack required extraction fields. Listed-action count can partly mark prompt or turn format. Low feature importance in this surrogate cannot establish causal irrelevance to Qwen.

## Existing Qwen evidence

The six archive hashes are verified by `analysis/observability.py`. Across 90 games, all 35,701 prompted post-setup records retain prompt, raw, private, public, stamp, speech and usage fields. This is field presence, not certification of successful parsing or substantive completeness. Usage records consistently name Qwen/Qwen3.8-27B; the provider's actual served weights are not independently verified.

The generated `private_reasoning` field is part of the application response format. Five raw strings contain a closing `</think>` delimiter, with run/event references in the saved inventory. A generated `reasoning` key occurs once. These do not establish a consistent native reasoning channel or a verified thinking-mode configuration. No activation tensors, attention traces, separate token-log-probability channel or explicit generation-mode settings were found in the checked fields and run configurations. Do not infer thinking mode from the mere presence or absence of a delimiter.

These records support content and trajectory analysis now. Token-probability scoring, controlled replays, latent probes and activation interventions require appropriate additional access or inference; none is claimed here. Open weights offer future instrumentation, subject to matching the checkpoint and configuration, rather than retrospective access to internals.

## Manual evaluation and source coding

The bounded manual evaluation reported by Maitreyee checks factual grounding, expressed monitoring capabilities and correspondence with the public response. The 96-note category counts remain the supplied exploratory source review, not outcome counts for that evaluation. Source provenance is retained. No sample size, pass rate or independent-review agreement is invented.


## Reminder salience as a future question

The turn context includes the current audit-status block; this was not a one-time-only exposure. Context accumulation, cue habituation and failures to use recurring reminders remain possible explanations to investigate, not demonstrated mechanisms or established inflation of the continuing-auditor rate. Trace cue presence, position, context length, truncation and public feedback before designing reminder-frequency or placement interventions. The initial condition imbalance also precedes any proposed later fading.
