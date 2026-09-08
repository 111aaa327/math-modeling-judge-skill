# Review report schema

Use only sections relevant to the chosen review mode. Keep evidence close to each finding.

## Header

- Competition, year, problem, review mode, review date
- Frozen packet path and manifest hash/path
- Independence status: `fresh-context blind`, `partially isolated`, or `same-context`
- Inputs reviewed and material inputs missing

## 1. Verdict

- One-sentence decision
- Score range, central estimate, confidence
- Submission state: `not ready`, `conditionally ready`, or `ready for final compliance pass`
- Three most consequential reasons

## 2. Hard gate

Table: `ID | requirement or claim | evidence | result | consequence`.

Cover every requested question, required output, main constraint, and current official submission rule.

## 3. Scorecard

Table: `dimension | weight | score | evidence | uncertainty`.

Explain deductions. Do not infer an official award level from the numeric score; if an award-readiness band is requested, label it an internal estimate and provide assumptions.

## 4. Claim–evidence matrix

Sample the decisive claims from the abstract, results, and conclusion. Table: `claim | source location | supporting artifact | independently checked? | verdict`.

## 5. Mathematical and numerical findings

For each finding: severity (`P0/P1/P2`), exact location, expected behavior, observed evidence, impact, and smallest credible repair.

## 6. Reproducibility

Record commands or checks run, regenerated artifacts, environment limitations, failures, and remaining unverifiable claims. Distinguish `not reproduced` from `incorrect`.

## 7. Paper, visuals, and compliance

Report page-level layout issues, notation/unit inconsistencies, citation problems, anonymity, AI declaration, appendix/archive gaps, and file constraints.

## 8. Historical benchmark addendum

Only after the blind score is frozen. Compare with relevant prior papers on problem interpretation, evidence, validation, and communication. State any weaknesses found in the benchmark papers themselves.

## 9. Revision queue

- P0: must fix before submission
- P1: high-value credibility/competitiveness improvements
- P2: clarity and polish

End with a short re-review checklist whose items can be marked pass/fail against a new frozen version.


