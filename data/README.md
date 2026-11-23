# Data

`source/` preserves supplied or source-extracted evidence. Do not edit its labels to match a desired result.

- `game_metrics.csv`: 90 main-study games and supplied pre/post counts.
- `auditor_notes_source.csv`: the supplied one-pass review of 96 auditing-related notes.
- `decision_contexts.json`: exact inputs and outputs for the 96 selected decisions, with state evidence and source hashes. These are extracts, not complete game logs.
- `game_inventory.csv` and `archive_manifest.json`: provenance for the 90 original exports.

`derived/surrogate_features.csv` contains the extracted pre-response features and tag-presence target for 29,147 decisions. It is the input to the surrogate analysis, not a collection of independent human truth labels.

Computed outputs belong in `../results/`. See `../docs/DATA_DICTIONARY.md` for definitions and limitations.
