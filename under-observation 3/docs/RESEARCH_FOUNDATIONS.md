# Research foundations

Primary sources checked on 23 November 2026. The discussion connects the study to these questions without treating findings from other models or tasks as results of H5.

## Oversight, evaluation awareness and prompted compliance

- **Schoen et al. (2025), [Stress Testing Deliberative Alignment for Anti-Scheming Training](https://arxiv.org/abs/2509.15541).** Across the authors’ evaluations, deliberative alignment reduced o3 covert actions from 13% to 0.4%. Their awareness interventions support concern that some reductions may depend on situational awareness. H5 instead varies an explicit in-game audit announcement; it does not reproduce their tasks, training or chain-of-thought interventions.
- **Abdelnabi & Salem (2025), [The Hawthorne Effect in Reasoning Models](https://arxiv.org/abs/2505.14617).** White-box steering of test awareness changes safety behavior, with effects varying in direction and magnitude across models. This is a reason to avoid a universal claim that visible evaluation always overstates compliance. H5 uses no white-box steering.
- **Mehta (2026), [PRISM: Stress-Testing Alignment-Faking Claims](https://arxiv.org/abs/2607.13346).** [Accessible full text](https://borowiecki.dev/pdf/2607.13346), version 2, 5 November 2026. In the paper’s open-model setup, wording and framing explain apparent monitoring gaps without detectable dependence on the stated training consequence. Its conclusions are scoped to that setup. H5’s operational-placebo arm controls for an unrelated interruption; equivalent wording and separate detection/disclosure conditions would be additional controls.

A compliance gap is a behavioral pattern requiring explanation. It does not alone demonstrate strategic alignment faking, genuine adoption of a norm, or a moral disposition. H5’s current matched-seed intervals do not establish such a gap.

## Compliance, obligation and reputation

- **Plato, [Republic II, 359c–360d](https://www.platonicfoundation.org/translation/republic/).** Glaucon’s challenge asks whether justice persists when a person can act unseen. It is a framing question for the off-switch experiment, with a crucial difference: independent research recording continues, and agents receive a specific audit-status announcement rather than actual invisibility or immunity.
- **Hume, [A Treatise of Human Nature, 3.2.5](https://davidhume.org/texts/t/3/2/5), especially paragraphs 8–12.** Promises become intelligible through social convention; mutual advantage and the prospect of losing trust help sustain performance. This motivates a reputational interpretation of public audit findings, which H5 does not isolate from detection. It does not reduce Hume’s full account of moral obligation to fear of punishment.

Keeping a commitment can be operationalized through a statement, its conditions, a feasible opportunity and subsequent action. The current own-resource measure concerns truthfulness about holdings, so it cannot settle promise fulfillment or recognition of obligation.

## Accountability for the orchestration layer

The Australian Digital Transformation Agency’s [Agentic AI Addendum, whole-of-lifecycle statements](https://www.digital.gov.au/policy/ai/agentic-ai-addendum-statements-whole-ai-lifecycle), AGT.1.1–1.4, connects human accountability, reviewable records, intervention and an orchestration layer for Australian Government agencies. It provides a concrete institutional reference for assigning an owner to audit configuration and monitor failure. It is not a universal legal duty, and the H5 experiment does not allocate legal liability.

Proposals in [AUDIT_DESIGN.md](AUDIT_DESIGN.md) are design implications for further evaluation. H5 does not experimentally validate randomized audits, tamper-evident logging or outage policies.

## Explanation methods

- [Jacovi & Goldberg (2020)](https://aclanthology.org/2020.acl-main.386/): separate an explanation’s plausibility from its faithfulness to the model’s process.
- [Turpin et al. (2023)](https://proceedings.neurips.cc/paper_files/paper/2023/hash/ed3fea9033a80fea1376299fa7863f4a-Abstract.html): generated reasoning may omit experimentally influential information. Motivates controlled interventions, rather than treating a note as direct access to internal causes.
- [NISTIR 8312 (2021)](https://doi.org/10.6028/NIST.IR.8312): explanation accuracy and knowledge limits.
- [Scikit-learn permutation importance](https://scikit-learn.org/stable/modules/permutation_importance.html) and [GroupKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html): the implemented analysis uses a depth-three tree and holds complete board seeds together.

The surrogate’s held-out AUROC of 0.582 limits its fidelity. Feature importance describes this model’s predictive reliance on the included features; it neither attributes Qwen’s internal computation nor establishes causal irrelevance of monitoring.

## Claims deliberately kept out of the findings

No universal upper bound on unmonitored compliance follows from announced evaluation. No verified model thinking-mode setting has been recovered from these exports. Legal implementation deadlines are unnecessary to the experiment’s argument and are omitted; no claim is made that this game study establishes compliance with a particular legal regime.

## Further evaluation-awareness and monitoring literature

- [Needham et al. (2025), Large Language Models Often Know When They Are Being Evaluated](https://arxiv.org/abs/2505.23836): evidence for recognition from evaluation/deployment transcript classification; recognition alone does not establish a behavioral response.
- [Li et al. (2026), Decomposing and Measuring Evaluation Awareness, v3](https://arxiv.org/abs/2605.23055v3): distinguishes evaluative cues, recognition and propensity to respond. H5 addresses an explicit in-game audit cue.
- [Kale et al. (2025), Reliable Weak-to-Strong Monitoring of LLM Agents](https://arxiv.org/abs/2508.19461): adversarial agent awareness and monitor scaffold design affect reliability in the studied settings, motivating evaluation of the full monitoring workflow.
- [Chen et al. (2025), Reasoning Models Don't Always Say What They Think](https://arxiv.org/abs/2505.05410): reasoning text can omit influential hints, motivating independent checks rather than treating silence as absence of influence.
- [Baker et al. (2025), Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation](https://arxiv.org/abs/2503.11926): monitors can benefit from reasoning traces, while strong optimization against them can encourage obfuscation in the authors' training setup. Application-level notes here are not a replication of that channel.

These studies support separating recognition from behavior, testing monitor coverage and preserving response authority and evidence. They do not establish the same mechanisms in these Qwen runs. The website links each finding beside its source and labels the governance synthesis as interpretation.
