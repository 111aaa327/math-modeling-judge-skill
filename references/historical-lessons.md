# Lessons distilled from prior materials

Use this only after the first-pass blind score is frozen. It is a benchmark checklist, not an answer key.

## Source boundary

The CUMCM collection in CNKI研学 was inspected on 2026-09-10. Its `参赛指导` index contained seven secondary sources, including 李顺勇等《如何在全国大学生数学建模中胜出》、韩中庚《数学建模竞赛论文的写作方法》、赵弘和钱佩玲《论数学建模中的合作学习》以及张不已《2016年全国大学生数学建模竞赛B题解题分析与总结》. The collection is useful for locating teaching literature, but neither the collection nor an article title is treated as a current official rule. Lessons below are retained only when they agree with the problem statement, verified rules, and inspected submission evidence.

Collection entry: `https://x.cnki.net/web/psmc/#/MyStudy/395c3e13-5fb9-4a5b-81bb-f6b50ccc2fb2` (login may be required).

## Evidence hierarchy

1. Current official rules and the exact problem statement.
2. Frozen paper, data, code, result files, and successful reproduction evidence.
3. Verified primary literature and official datasets.
4. Relevant prior excellent papers, inspected critically.
5. Lectures, prompt packs, speed courses, and unofficial checklists.

## Repeated strengths in credible submissions

- Every question maps to a visible model, result, and interpretation.
- The paper reads as one decision chain: later questions reuse earlier variables, estimates, or constraints instead of restarting with unrelated notation and methods.
- Central quantities are defined before optimization; aggregation semantics such as sum, union, intersection, minimum, or weighted score are unambiguous.
- Advanced methods improve a stated metric or capability over a simple baseline.
- Constraints and units are checked numerically, not merely restated.
- Validation targets the actual failure modes of the model: convergence, leakage, feasibility, uncertainty, stability, or limiting cases.
- Abstract, body, tables, figures, attachments, and code agree on the headline numbers.
- Figures answer a question and preserve the underlying values.
- Headings describe the actual analytical task; they do not advertise generic steps such as “data processing” or repeat a catalog of algorithm names.
- Each decisive table or figure is cited in the text and followed by an interpretation tied to the question.
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
- Matching a method to a prompt keyword without checking its assumptions, baseline, identifiability, or failure modes.

## 2025 A simulation lesson

The earlier internal blind review exposed two structural errors that a writing-focused reviewer could miss: optimizing a representative target point instead of the complete cylinder, and maximizing per-missile total duration when the key operational quantity was the three-missile common interval. The corrective pattern is general:

1. formalize the physical or decision object exactly;
2. make quantifier order explicit for multi-object coverage;
3. define union/intersection/minimum/sum objectives before optimization;
4. re-optimize under the corrected criterion rather than only evaluating the old plan afterward;
5. demonstrate spatial and temporal convergence.
