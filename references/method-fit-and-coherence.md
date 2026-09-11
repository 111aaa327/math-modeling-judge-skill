# Method fit and solution coherence

Use this reference before awarding credit for an advanced method. A familiar model name is not evidence that it fits the question.

## Operational-semantics audit

For each requested output, record:

| Item | Required statement |
|---|---|
| Object | The physical, statistical, geometric, or decision object being modeled |
| Quantifiers | `for all`, `exists`, `at least`, `simultaneously`, worst case, expectation, or probability level |
| Grain | Time interval, spatial region, population unit, aggregation level, and sampling frequency |
| Operator | Sum, union, intersection, minimum, maximum, average, weighted score, or other aggregation |
| Output | Exact number, interval, classification, schedule, policy, proof, or file required |

If two plausible interpretations lead to materially different answers, score the ambiguity as a substantive modeling risk until the paper justifies one with problem text, domain evidence, or a comparison calculation.

## Subproblem dependency graph

Write one node per subproblem and an arrow for every result that should feed a later stage. Audit:

- whether the promised upstream variable or result is actually consumed;
- whether symbols, units, and data versions remain consistent across the edge;
- whether later constraints relax or add resources and therefore should change the answer;
- whether an implausible zero marginal effect signals a semantic or implementation error.

Disconnected subproblems are not automatically wrong, but the paper must explain why independence is valid.

## Method-fit certificate

For each substantial method, require concise answers to:

1. Which decision, estimate, or claim does it produce?
2. Which assumptions and data conditions make it applicable?
3. What is the simplest credible baseline?
4. Which failure mode is most dangerous for this problem?
5. Which validation directly tests that failure mode?
6. What measurable value does the method add over the baseline?

Deduct for a method catalog when multiple named methods share no dependency chain, baseline, validation, or decision role.

## Assumption-to-result trace

For every consequential assumption, record the affected equations, code/configuration, outputs, and sensitivity evidence. If the paper calls an assumption “reasonable” without showing its effect on the answer, treat the corresponding conclusion as conditionally supported.

## Result interpretation test

For every headline result, the paper should answer: what changed, relative to what, by how much, under which uncertainty, why it matters, and what action or conclusion follows. A solver printout or a table without this bridge earns computation credit but limited modeling or communication credit.
