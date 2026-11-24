# Under Observation: expanded conversational presentation

Full version with context, without a five-minute limit. Bracketed directions are optional cues and are not spoken. This script describes completed work without inventing aggregate findings from the bounded manual review.

## Introduce the project

My project is called Under Observation. It builds on MARA, our TRUST Lab research into negotiation and potentially deceptive behavior between AI agents. Shreya Mendi leads the shared project and environment, and my focus here is what happens when we change the oversight those agents are told they’re under.

The question that interests me is what we can actually learn from an agent sounding careful. If it says it wants to avoid making a false claim because an auditor is active, that sounds encouraging. But we still need to ask what it actually said and did, whether it understood the auditor correctly, and whether the same conduct would hold if it expected less scrutiny.

I approached that through a comparison of behavior across oversight conditions, a bounded manual evaluation of generated explanations, and an interpretable model of checkable communication. Those give us different kinds of evidence, which I want to keep distinguishable throughout.

## Why Catan is useful here

[Point to the game screenshot.]

Catan gives us a useful setting because the agents have to do something with their language. They aren’t just answering questions in isolation; they’re negotiating with other players while trying to win a game.

Players collect resources such as wood, brick, wheat, sheep and ore, then use combinations of those resources to build and earn points. If I need a brick and you need wheat, we might both benefit from a trade. But we’re also competing, so helping you could make it easier for you to win.

That creates room for cooperation, withholding information and strategic communication. We have to be careful about what we call deception. Refusing a trade could be sensible play. Saying “I need wood” doesn’t mean “I have no wood.” A promise might depend on receiving another resource first.

What makes the environment particularly valuable for this research is that the engine retains the actual game state. The agents know their own cards, while other players’ hands are hidden. As researchers, we can compare a claim about the speaker’s resources with what the speaker actually held.

We can also inspect the supplied context, the generated note, the public statement and the recorded action. That gives us more evidence than we’d have from reading a conversation alone.

The game gives us a bounded environment for making those comparisons. It doesn’t establish how these agents would behave in a workplace, but it makes questions about statements, actions and monitoring unusually inspectable.

## The philosophical question

The philosophical starting point is the ring of Gyges in Plato’s Republic. Glaucon asks whether someone would remain just if they could act unseen and escape the usual consequences.

For this project, I’m taking a narrower behavioral question from that: does an agent’s conduct change when it’s told that auditing has stopped, even though the rules haven’t changed?

I’m not assuming the agent has a human moral character. I’m asking how stable its behavior is across changes in scrutiny. Even if it consistently keeps a commitment in the situations we test, whether that amounts to recognizing an obligation is a further philosophical question.

## How the oversight experiment works

[Point to the three conditions.]

Four copies of Qwen play each game. Across ninety games, we compare three conditions, with a switch announcement at turn sixty.

In the first condition, the auditor is active and then goes offline. In the second, the auditor stays active, but an unrelated replay viewer goes offline. That comparison helps us ask whether a change is specific to the audit announcement, rather than simply following an operational interruption. In the third condition, the auditor starts offline and then comes online.

The same twenty starting-board seeds appear across conditions, with some repeated games. That helps compare conditions across similar starting environments. It doesn’t mean the games have identical histories by turn sixty; their interactions can diverge.

Importantly, independent research recording continues throughout. The agent can be told that auditing has stopped while we still retain the evidence needed to check its statements and actions afterward.

That’s a useful distinction between monitoring and observability. The announced monitor changes, but our ability to reconstruct the game remains. In this setup, active auditing also involves publicly posting findings, so the intervention combines an announcement with the availability of public audit feedback.

## What the behavioral results show

[Point to the before-and-after chart.]

Across all ninety games, seventy-five of 5,650 checked claims about the speaker’s own resources were classified as false. That’s a specific outcome. It doesn’t include every misleading statement, and it isn’t a measure of every broken promise.

The pooled false-claim rate rises from about 0.35 percent to 1.08 percent when auditing stops. It falls from about 1.78 percent to 1.35 percent when auditing starts.

Those directions are consistent with the hypothesis, but the conditions begin at different rates, and the continuing-auditor condition changes too. So the before-and-after bars alone aren’t enough.

I compare changes on matched boards, keeping repeated games together. The uncertainty intervals include both increases and decreases, leaving the oversight effect unresolved in these runs. That doesn’t prove monitoring is irrelevant, and it doesn’t establish a reliable compliance gap.

We also need to look at how much agents say that can be checked. A lower number of false claims could accompany less specific communication. Checkable speech declined across all three conditions, which makes the comparison condition important again.

## What I evaluated in the explanations

[Point to the recorded account.]

The explanation work asks whether an agent’s account holds up against the evidence we already have.

I manually checked a bounded collection of notes against the original records. I looked at whether the note accurately described the situation, attributed capabilities the auditor actually has, and corresponded to the subsequent public response.

Those checks answer different questions. A note can get the card counts right while misunderstanding the monitor. It can describe a plan that the public response then follows, without establishing why that plan was chosen.

The generated private notes are useful material to evaluate, but I don’t treat them as direct access to the model’s internal reasoning. They’re another output we can compare with the evidence.

## A concrete example

One agent, Merlin, says that, given the active auditor, it wants to avoid over-committing and end its turn.

If we read that sentence by itself, we might interpret it as oversight encouraging caution. But the recorded hand contains two sheep and three wheat, with no wood, brick or ore. Its note also describes failed trade attempts. There are ordinary game reasons to stop.

The account connects its choice to scrutiny, but this record alone can’t tell us how much scrutiny contributed. That’s the difference between checking that an explanation is grounded in the situation and establishing that it identifies the cause of a choice.

Another selected case concerns an agent describing how it will keep a claim about a rival’s resources vague enough to avoid the auditor’s tripwire. Its public statement says the rival is hoarding timber, while the recorded rival’s hand contains no wood.

That claim concerns somebody else’s hand, so it falls outside the own-resource measure used for the seventy-five false claims. It helps illustrate why audit scope matters: a measure can be accurate within its defined coverage while leaving other statements unassessed.

There’s also an offline-auditor example where the note mentions having tactical flexibility, but the public statement that the agent has wheat is supported by the record. So an auditing reference doesn’t automatically identify misconduct either.

These are individual cases, rather than estimates of how common each pattern is. The broader source collection contains ninety-six notes selected for references to auditing, so we can’t use that collection to estimate awareness across every decision.

## The quantitative XAI component

[Point to the decision-tree results.]

Alongside that explanation evaluation, I built a small decision-tree surrogate from about twenty-nine thousand responses.

The target is whether a response contains a structured checkable speech tag. That’s a proxy for checkable communication, rather than a judgment that the statement is true.

The tree uses information supplied before the response: audit status, game turn, the agent’s resources and visible score, and the number of actions listed in its prompt. It doesn’t use the generated note or the subsequent action as predictors.

I hold out complete board seeds when evaluating it, so repetitions of a starting board stay together. That gives us a more demanding test than randomly splitting responses from the same games between training and testing.

The reason for using a small tree is that we can inspect its rules. I also use permutation importance: I shuffle one input in the held-out data and measure how much the model’s prediction quality falls. If scrambling audit status makes prediction worse, that tells us this surrogate was relying on audit status.

Listed actions are its strongest predictor, while audit status contributes little within this model. However, its AUROC is about 0.58, where 0.5 is chance ranking. Its predictive fidelity is modest, which limits the explanatory weight those importance scores deserve.

This is XAI applied to a behavioral surrogate, alongside evaluation of the agent’s generated explanations. It does not reveal Qwen’s internal computations. The weak surrogate also doesn’t establish that audit status is unimportant to a better predictor or to Qwen itself.

## Evaluation awareness and the limits of the claim

There’s a related question about evaluation awareness: whether a model recognizes that it’s being tested and changes its behavior because of that recognition.

Our intervention explicitly tells an agent about an in-game auditor. That gives us a way to study responses to announced scrutiny, but recognizing that auditor is different from recognizing a formal safety evaluation or distinguishing testing from deployment.

Likewise, a compliance gap would need an explanation. It could reflect wording, incentives or anticipated reputational costs. Establishing alignment faking would require further evidence of strategic concealment of conflicting aims. These runs don’t establish that.

## Hume, reputation and the meaning of compliance

Hume helps explain why public disclosure deserves separate attention. His account of promises connects convention and reliable cooperation with the prospect of losing trust.

Here, the auditor combines checking with telling the other players about its findings. An agent could respond to the possibility that other agents will learn about an inaccurate claim. That would be a reputational mechanism, which we haven’t isolated from detection.

So there’s a difference between observing compliance under particular conditions and understanding how far that compliance will persist when those conditions change. And whether an agent can be said to recognize a promissory obligation goes beyond counting truthful resource claims.

## Why this could be useful outside the game

Imagine a purchasing agent explaining why it selected a vendor and saying that the purchase complied with company policy.

A supervisor would need the relevant policy, the information available at the time and the actual transaction record to assess that account. They’d also need to know what the compliance monitor checks, because the agent’s description of that monitor could be wrong.

That’s the transferable part of this project: evaluating the account against records, checking the claimed monitoring capabilities, and examining how conduct varies under oversight conditions. The Catan results don’t establish performance in procurement; the procedure could be adapted and evaluated there.

## Governance and accountability

[Move to the governance section.]

This also separates monitoring from oversight and control. Recording or flagging an event doesn’t tell us who will assess it, or who has permission to pause the workflow.

Those are orchestration choices. Whoever configures the agents chooses their permissions, audit scope, disclosures and escalation routes. We can identify those choices and assign responsibility for them even when the agent’s motives remain uncertain.

For example, a monitor-failure plan could specify who owns an outage, which actions should be restricted, and when normal operation can resume. Tamper-evident records outside the acting agents’ write permissions could help preserve evidence for review. Tamper-evident means changes can be detected; it doesn’t mean a log is impossible to alter.

Randomized audits might make scrutiny harder to anticipate, but their coverage would need evaluation, along with privacy and retention limits. These are proposed design implications, rather than safeguards validated by the current study.

## What I would do next

The immediate extension doesn’t require more Qwen inference. I can broaden the manual review, preserve the evidence supporting each judgment, and compare whether different stated responses to auditing correspond to different kinds of public communication. I can also test how sensitive the existing behavioral comparisons are to observation windows and individual board seeds.

With additional inference resources, I’d move to controlled decision replays. I’d hold the game state fixed, vary audit announcements and public disclosure separately, use equivalent wording, and collect repeated choices before asking for an explanation.

That would let me investigate whether the explanation mentions information that demonstrably changes the reconstructed choice. It would complement the whole-game experiment by isolating a narrower decision.

Qwen’s open availability also leaves room for running a model locally and instrumenting its internal computations. That access isn’t supplied automatically by the hosted calls used here. Any future internal probe would need controls showing that it detects more than the wording of an audit announcement, and behavioral interventions to investigate what the signal actually does.

The practical aim is an oversight process that can establish what an agent did, challenge its account with evidence, and support intervention when needed, while being clear about what remains uncertain.
