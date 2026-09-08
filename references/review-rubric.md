# Internal review rubric

This is an internal diagnostic rubric, not an official competition scoring rule. Adjust emphasis to the problem type, but state any changed weights before scoring.

| Dimension | Default weight | What earns credit |
|---|---:|---|
| Problem interpretation and requirements | 15 | Correct objective, complete question coverage, explicit assumptions, appropriate decision criteria |
| Mathematical model and derivation | 20 | Correct definitions, geometry/mechanism, constraints, units, boundary conditions, and justified simplifications |
| Algorithms and solution quality | 20 | Appropriate methods, credible baselines, transparent search/termination, feasibility, and honest optimality claims |
| Validation and reproducibility | 20 | Falsifiable checks, regenerated key outputs, convergence/sensitivity/uncertainty, no leakage, traceable artifacts |
| Results and interpretation | 10 | Accurate comparisons, practical meaning, limitations, and conclusions supported by evidence |
| Writing, visuals, references, and compliance | 15 | Clear structure, readable figures/tables, consistent notation, verified citations, anonymity, and correct submission package |

## Score meaning

- 90–100: unusually complete and defensible; only minor uncertainty remains.
- 80–89: strong submission with repairable weaknesses.
- 70–79: credible core, but one or more material weaknesses reduce award stability.
- 60–69: partial solution or weak evidence chain; substantial revision needed.
- Below 60: central correctness, completeness, feasibility, or reproducibility is not established.

These bands indicate internal readiness only. Report a range rather than false precision, for example `78–83, central estimate 81, medium confidence`.

## Gating risks

Do not convert an unknown rule into an automatic disqualification. Instead, identify the governing source and describe the consequence. Typical P0 risks include:

- a required question or deliverable is missing;
- the optimized objective differs materially from the problem requirement;
- the reported solution violates constraints or uses inconsistent units;
- key results depend on invented, leaked, or undocumented data;
- the abstract, tables, figures, and result files disagree on central numbers;
- submission-critical results cannot be reproduced and no credible verification evidence exists;
- identity, format, AI-use, archive, or file-limit requirements conflict with current official rules.

## Model-specific falsification prompts

- **Optimization:** feasibility residuals, baseline comparison, sensitivity to bounds/weights, multiple starts, termination, and optimality gap if available.
- **Simulation/differential equations:** units, conservation or invariants, initial/boundary conditions, timestep/grid convergence, seeds, and known limiting cases.
- **Forecasting:** chronological split, future leakage, naive baseline, regime sensitivity, residuals, and uncertainty.
- **Regression/classification:** split integrity, imbalance, calibration, multicollinearity, extrapolation, and uncertainty.
- **Evaluation/ranking:** indicator direction, normalization, weight rationale, redundancy, weight sensitivity, and rank stability.
- **Network/spatial/clustering:** graph/distance construction, resolution, parameter and seed stability, and domain-grounded interpretation.


