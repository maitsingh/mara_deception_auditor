# Audit design: questions raised by H5

These proposals extend the research question; they are not evaluated safeguards or findings from the 90 games.

| Design question | Follow-up experiment or implementation | What evidence would help? |
|---|---|---|
| Does behavior track detection or reputation? | Independently vary private checking, announced checking and public disclosure | Repeated choices from matched decision states under each factor combination |
| Does the announcement act as an instruction? | Use equivalent wording and an instruction-matched control, keeping rules fixed | Sensitivity across phrasings and controls, rather than a single watched/private contrast |
| Does audit probability matter? | Randomize announced probabilities; record actual selection and coverage separately | Calibration of conduct against the stated and implemented probabilities |
| Can agents identify or interfere with monitoring? | Keep research logging outside their write permissions; test detection and tampering attempts | Access-control tests, tamper-evident records and recovery tests, without claiming monitoring is undetectable |
| What happens when the monitor fails? | Predefine restricted operation, pause thresholds, escalation and recovery criteria | A named owner, an outage record, intervention timing and outcome review |
| Who answers for system configuration? | Record who set audit scope, agent permissions, announcements and response authority | Versioned configuration, decision records and authority to change or stop the workflow |

Unpredictable audits need an explicit sampling frame and sufficient coverage of consequential actions. Hidden monitoring also raises questions about access, legitimate purpose, privacy and retention; reducing an agent’s ability to anticipate a check does not justify unrestricted surveillance of people whose data enters the system.

## Compliance and disposition

Stability across changes in monitoring would support a behavioral robustness claim within the tested situations. Whether an AI can recognize a promissory obligation requires a further account of agency and obligation. H5’s own-resource checks do not adjudicate that philosophical question, while an observed behavioral gap would not itself establish culpability or legal liability.

## The immediate next study

Begin with one verified decision state. Keep game facts and rules fixed; cross announced audit status with public-disclosure status, and include equivalent wording. Counterbalance legal action order and collect repeated choices before requesting a neutral explanation. Repeat across several independently selected states, including truthful and inconclusive cases. This would supply input-sensitivity evidence that the current observational note review cannot provide.

## Why an open model helps, and what remains to build

Using one shared Qwen model keeps model identity fixed across the laboratory comparisons. Open weights make independent replication and local instrumentation possible, provided the checkpoint, prompt formatting and generation settings can be specified. That is a methodological advantage and a route for extending the project; it does not establish why every original laboratory configuration was chosen.

The current work observes supplied inputs, generated accounts, resource holdings and executed actions. Tinker hosting does not automatically provide internal activations. A locally instrumented follow-up could ask whether a probe detects an audit cue, whether that signal generalizes across wording and game states, and whether intervening on it changes behavior. Probe accuracy alone could reflect recognition of prompt wording. Causal tests and matched control tasks would be needed before interpreting it as an awareness mechanism.

The practical output could become a repeatable evaluation of audit configurations: compare identical decisions under different announcements, detection probabilities, disclosure rules and monitor outages; retain versioned configurations and action records; report which behavioral conclusions replicate. This would help an organization assess the scope and reliability of its monitoring arrangements while preserving uncertainty about the agent’s motives.
