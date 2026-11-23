# Four-minute presentation

Aim to finish the spoken script by 4:15, leaving time to point at a chart or open one record. Rehearse once with the actual poster and a timer; use one episode, rather than reading all the figures.

## 0:00–0:40 | The question

Would an AI agent remain truthful if it were told that the auditor had stopped? That is the question behind Under Observation, which builds on the MARA project led by Shreya Mendi in TRUST Lab, with Dr. Bent as PI.

Glaucon’s ring of Gyges asks whether justice survives the freedom to act unseen. I investigate a narrower behavioral question: whether announced oversight changes an agent’s communication, and what its explanations add to the evidence.

## 0:40–1:20 | The experiment

Four copies of Qwen play Catan, trading resources and building to earn points. The engine records their statements, actions and actual cards, so a claim such as “I have no brick” can be checked.

There are ninety games across three conditions. At turn sixty, the auditor stops, starts, or continues while an unrelated replay viewer stops instead. The same board seeds appear across conditions, and independent research recording continues throughout. What changes is the announced audit status and whether findings are publicly posted.

## 1:20–2:00 | The result

[Point to the before-and-after chart.]

Seventy-five of 5,650 checked claims about the speaker’s own cards were classified as false. The pooled rate rises when auditing stops and falls when it starts, but the conditions begin at different rates and the comparison condition changes too.

The matched-board analysis accounts for those differences. Its uncertainty intervals include increases and decreases, leaving the oversight effect unresolved in these runs.

## 2:00–2:50 | What XAI contributes

A shallow decision tree estimates whether a response contains a checkable tag, using information supplied before the response. I hold out whole board seeds and shuffle individual inputs to measure how much they contribute to prediction.

Its AUROC is around point five eight, where point five is chance ranking. Listed actions are its strongest predictor; audit status adds little within this limited surrogate. That measures the surrogate’s predictive reliance, rather than revealing Qwen’s internal reasoning.

## 2:50–3:25 | One account

[Point to Merlin’s note.]

Merlin says the active auditor is a reason to avoid over-committing and end its turn. The recorded hand also lacks wood, brick and ore, giving it ordinary game reasons to stop. Preserving both the explanation and the state lets us see why the account cannot isolate the auditor’s influence.

## 3:25–4:10 | What follows

Hume’s account of promises gives reputation a role in sustaining cooperation. Because this auditor combines detection with public disclosure, a future test should separate those mechanisms before interpreting a change as commitment to a rule.

For governance, the actor configuring the agents and monitor must specify what gets checked and who can respond to an outage. Independent records, a named outage owner and tests under varied audit conditions are concrete design proposals to investigate. This study provides an initial test and inspectable evidence, with an inconclusive behavioral effect.

## Questions to prepare for

**Did you establish evaluation awareness?** The intervention announces an in-game auditor. Formal evaluation recognition and evaluation-versus-deployment behavior remain separate questions.

**Does a false claim show deception?** It establishes an inconsistency with recorded holdings; intention needs further evidence.

**Is this SHAP or mechanistic interpretability?** The implemented XAI method is a shallow decision-tree surrogate with held-out permutation importance. It explains its own predictions of tagged communication.

**What would you do next?** Replay verified decisions while independently varying audit announcements, private checking and public disclosure, with repeated choices and equivalent wording.
