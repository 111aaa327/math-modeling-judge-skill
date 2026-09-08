# Lessons distilled from prior materials

Use this only after the first-pass blind score is frozen. It is a benchmark checklist, not an answer key.

## Evidence hierarchy

1. Current official rules and the exact problem statement.
2. Frozen paper, data, code, result files, and successful reproduction evidence.
3. Verified primary literature and official datasets.
4. Relevant prior excellent papers, inspected critically.
5. Lectures, prompt packs, speed courses, and unofficial checklists.

## Repeated strengths in credible submissions

- Every question maps to a visible model, result, and interpretation.
- Central quantities are defined before optimization; aggregation semantics such as sum, union, intersection, minimum, or weighted score are unambiguous.
- Advanced methods improve a stated metric or capability over a simple baseline.
- Constraints and units are checked numerically, not merely restated.
- Validation targets the actual failure modes of the model: convergence, leakage, feasibility, uncertainty, stability, or limiting cases.
- Abstract, body, tables, figures, attachments, and code agree on the headline numbers.
- Figures answer a question and preserve the underlying values.
- Limitations distinguish an approximation from a proved condition and a heuristic solution from a global optimum.

## Repeated high-risk patterns

- Replacing the requested target or object with an easier proxy without quantifying the consequence.
- Adding individual durations when the requirement concerns a union or common intersection.
- Treating a solver's best output as a proof of global optimality.
- Using random train/test splits for time-dependent data or otherwise leaking future information.
- Reporting sensitivity or robustness tests unrelated to the central claim.
- Inventing missing data, citations, links, solver metrics, or implementation details.
- Letting elegant formatting hide incomplete derivation, infeasibility, or inconsistent numbers.
- Following unofficial fixed counts for pages, formulas, models, tests, or diagrams.

## 2025 A simulation lesson

The earlier internal blind review exposed two structural errors that a writing-focused reviewer could miss: optimizing a representative target point instead of the complete cylinder, and maximizing per-missile total duration when the key operational quantity was the three-missile common interval. The corrective pattern is general:

1. formalize the physical or decision object exactly;
2. make quantifier order explicit for multi-object coverage;
3. define union/intersection/minimum/sum objectives before optimization;
4. re-optimize under the corrected criterion rather than only evaluating the old plan afterward;
5. demonstrate spatial and temporal convergence.


