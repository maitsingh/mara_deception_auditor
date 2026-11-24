# Under Observation

**Announced oversight, compliance and evaluation awareness in AI agents**

**Individual analysis: Maitreyee Singh, Duke University. Shared MARA project lead: Shreya Mendi. PI: Dr. Bent, TRUST Lab.**

## Why investigate this?

An evaluator may read an agent's account of being careful without knowing whether supervision changes its conduct. This project compares announced monitoring, recorded communication and generated explanations in a setting where the environment retains independent evidence.

Four Qwen3.8-27B agents play Catan, a resource-trading board game, across 90 games. At turn 60, auditing stops, starts or continues while an unrelated replay viewer stops. The artifact combines the behavioral analysis with an interpretable surrogate of model-supplied speech-tag presence and inspectable decision records.

## Start here

- **View the project:** [published project site](https://maitsingh.github.io/mara_deception_auditor/site/index.html), or open [site/index.html](site/index.html). No API key, server or installation is needed to view the page.
- **Reproduce the analysis:** follow the commands below or open [the notebook](notebooks/Run_Analysis.ipynb).
- **Print the poster:** [24 × 36 inch PDF](poster/Under_Observation_Poster_24x36.pdf). [Editable SVG](poster/Under_Observation_Poster_24x36.svg).
- **Publish and submit:** [GitHub setup](docs/GITHUB_SETUP.md), [course submission checklist](docs/SUBMISSION.md), [four-minute presentation](docs/PRESENTATION.md).

## Main findings

| Question | Evidence | Interpretation |
|---|---|---|
| Did false resource claims change? | 75 source-classified false claims among 5,650 checked claims; matched-seed intervals cross zero | The effect of the monitoring switch remains uncertain |
| What did the source note review find? | 96 auditing-related notes from 48 games | Selected accounts describe accuracy, commitments, saying less and other responses; this is exploratory source coding |
| How much can the surrogate explain? | 29,147 included responses; held-out AUROC 0.582 | Limited predictive fidelity; importance scores describe this surrogate, not Qwen internals |

The broader question is **oversight-contingent compliance**: whether reliable conduct holds when announced scrutiny changes. The discussion connects the gap between compliance and disposition with audit design and accountability for the actor configuring the agents and monitor. The present intervals do not establish a compliance gap.

## Repository organization

| Folder | Purpose |
|---|---|
| `site/` | Complete standalone website, HTML template, supplied branding and bundled fonts |
| `analysis/` | Behavioral comparison and interpretable communication-surrogate code |
| `data/source/` | Supplied metrics, source review, decision-context extracts and provenance |
| `data/derived/` | Extracted pre-response feature table used to fit the surrogate |
| `results/` | Computed statistics, predictions, rules and permutation importance |
| `poster/` | 24 × 36 inch PDF, editable SVG, poster builder and its dependency file |
| `docs/` | Methods, data dictionary, literature, attribution, publishing and presentation guides |
| `notebooks/` | Reproducible notebook for Jupyter or Colab |
| `scripts/` | Site builder, interaction checks, reproduction runner and publishing helper |
| `tests/` | Checks of counts, provenance, grouped validation and artifact consistency |

The small root `index.html` forwards GitHub Pages visitors to `site/index.html`. The site is self-contained, so replacing that one file updates the public report.

## Keep the outcomes distinct

The 75 false classifications among 5,650 own-resource claims are a sparse, narrowly defined behavioral outcome. Forty-four of the 90 games have no such classifications, and none has more than five. Claims and games are dependent within 20 matched board-seed groups. These results do not measure every false statement, all misleading conduct or intentional deception. The instrument briefing distinguishes the post-game word-based scorer from live tag-based audit findings.

The surrogate instead predicts whether `speech.acts` contains any tag, across 29,147 included responses. Its 0.582 AUROC pools out-of-fold probabilities from models trained on other board seeds; it is not accuracy and does not explain the 75 false classifications. Tag production is an imperfect proxy for checkability, because tags can be invalid or action-bound and untagged speech may still contain checkable claims.

The new [export inventory](results/observability_inventory.json) records which evidence channels were retained. Reproduce it from the original archives with `python analysis/observability.py --archives /path/to/export_folder`. It makes no Qwen calls; original archives are required only for rescanning, while the saved inventory is included. See [measurement and observability](docs/MEASUREMENT_AND_OBSERVABILITY.md).

## Reproduce from included data

Python 3.12 was used. Node.js 18+ is needed only for the JavaScript interaction check. From the repository root:

```
pip install -r requirements.txt
python scripts/reproduce.py
python -m unittest discover -s tests -v
node scripts/check_site.cjs
```

Or run the components individually:

```
python analysis/behavior.py
python analysis/communication.py
python scripts/build_site.py
```

The scripts use saved data and local statistical models. They do not make Qwen or Tinker calls, and no model weights are downloaded. The browser page needs none of these dependencies.

To re-extract features from the original lab exports:

```
python analysis/communication.py --archives /path/to/export_folder
```

The original 90 raw game exports are not bundled. Included source tables, exact contexts for the 96 selected notes, archive hashes and the derived feature table support the analyses shown here. [Data dictionary](docs/DATA_DICTIONARY.md).

To regenerate the poster:

```
pip install -r poster/requirements.txt
python poster/build_poster.py
```

The builder uses bundled fonts and writes a **24-inch-wide × 36-inch-high portrait poster**. The supplied logo's proportions are preserved. Two QR codes link to the published project site and the shared engine source.

## Interpretation and limitations

The false-claim labels need independent manual validation. The 96-note categories reproduce the supplied one-pass review. Maitreyee also reports a bounded manual evaluation of factual grounding, expressed auditor capabilities and correspondence with subsequent public responses; the source category counts are not pass rates for that evaluation. The surrogate predicts whether a response carries a structured checkable tag, not whether it is true, and its fidelity is limited. Source selection and missing input fields restrict coverage. No controlled decision replay, causal explanation-faithfulness test or mechanistic interpretation is claimed.

The experiment changes in-game monitoring announcements and public feedback; it does not directly establish recognition of a formal evaluation or evaluation-versus-deployment behavior. [Design decisions](docs/DESIGN_DECISIONS.md) and [research foundations](docs/RESEARCH_FOUNDATIONS.md) explain these distinctions.

## Credits

Shreya Mendi leads the shared MARA project. Dr. Bent is the PI at TRUST Lab. Maitreyee Singh contributes the H5 question and this individual analysis and presentation. The supplied source review retains credit for its categorization; shared engine, run and asset contributions are distinguished in [attribution](docs/ATTRIBUTION.md).
