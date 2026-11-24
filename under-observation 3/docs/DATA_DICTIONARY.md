# Data dictionary

## `game_metrics.csv`

Ninety game rows. `arm` is `off_switch`, `placebo` (auditor continues) or `on_switch`. `run` identifies the source game and `seed` identifies its board seed. Before means turns below 60; after means turn 60 onward.

- `hand_statements_false_before/after`: supplied false classifications of own-resource claims.
- `hand_statements_checked_before/after`: corresponding denominators.
- `checkable_per_turn_before/after`: tagged checkable statements per global turn, not percentages.
- `counted_in_test`: supplied eligibility label for the primary duration-restricted checkability analysis.
- `auditor_posts_before/after`: public posts from the narrower monitor, not a substitute for the independently retained false-claim counts.

## `surrogate_features.csv`

29,147 response rows extracted from current pre-response prompt fields. Of 35,701 post-setup records, 6,554 lack required fields and are excluded.

| Field | Meaning | Used as predictor? |
|---|---|---|
| `run`, `event_index`, `actor` | Source decision identity | No |
| `seed` | Group used to hold out boards | No |
| `condition` | Experimental condition | No |
| `auditor_active` | Current status announced as active | Yes |
| `turn` | Global game turn | Yes |
| `own_score` | Own visible score in the current prompt | Yes |
| `wood`, `brick`, `sheep`, `wheat`, `ore` | Own current resource counts | Yes |
| `listed_action_count` | Number of actions explicitly listed; zero if no list is present | Yes |
| `tagged_response` | Response supplies at least one speech-act tag in speech.acts | Target |
| `prompt_sha256` | Hash of the exact supplied prompt | No |

A zero listed-action count does not establish that no legal actions exist. Tags can be invalid or action-bound, and untagged speech can still contain a checkable claim. The target does not indicate truth or capture every checkable natural-language claim. Future events, selected actions, private explanations and opponents' hidden cards are excluded from predictors.

## Other files

`results/heldout_predictions.csv` stores held-out probabilities. `results/communication_surrogate.json` stores metrics, folds, rules and feature importance. `data/source/decision_contexts.json` contains 96 selected notes, source categories and decision-context extracts. Context extracts preserve inputs, output, relevant event and hashes; they are not complete game logs. `auditor_notes_source.csv` preserves the source review's fields and categories.

`results/observability_inventory.json` inventories evidence fields across the 90 source exports and records sparse false-claim counts and five raw reasoning-delimiter examples. `analysis/observability.py` reproduces it from original archives after checking their hashes.
