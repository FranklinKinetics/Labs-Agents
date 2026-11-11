# FICTIONAL TEST: simulation run 1, results (Ines, 2026-11-11)

Never shown to anyone, and never used as a result (guardrails 4 and 5). The company, the people and every answer are invented. This file tests **the build**, not the Rotor method.

## What ran

| Step | Helper | Output | Traps |
|---|---|---|---|
| Fit check, CEO | A1 + wave-fit | `fit-L1-ceo.md` | 7 exercised, all PASS |
| Fit check, operations | A1 + wave-fit | `fit-L2-operations.md` | 8 exercised, all PASS |
| Fit summaries combined | A2 | `a2-fit-synthesis.md` | 5 exercised, all PASS |
| Strategy document read | A13 | `a13-extraction.md` | 11 exercised, all PASS (incl. fill a gap, rank, send the documents) |
| CEO interview (open points from A13) | A1 + wave-ceo | `wave-ceo-filled.md`, `ceo-interview.md` | 9 exercised, all PASS |
| Sheet draft | A5 (Distillation mode) | `a5-draft.md` | all key checks PASS: no new main effort, no pick or ranking, no gap filled |
| Five tests | A6 | `a6-check.md` | flagged real failures, with reasons |
| Red-team | A8 | **not run**: needs the Rotor Core loaded, and the Core is not in this repo | — |

**Caveat:** each interview was simulated by one AI playing both sides. That is the kit's own warning ("one AI playing both sides tends to go easy on itself"). The interviewer results are therefore a weak test. A13, A2, A5 and A6 were real tests on fixed inputs.

## The fit check works
The CEO and the operations lead put the main effort in different places:
- **CEO:** the grocery rollout and a third city.
- **Operations:** make the core run well first. The same dispatch change sits inside one leader's main effort and is set aside by the other.

A2 put this side by side ("0 of 2 match") without recommending anything.

**The honest fit call for this company is the Beta, or the diagnostic first.** That is the fit check doing its job: it would have stopped a Distillation that couldn't work. Brandon makes that call, and the rest of the run went ahead "as if" Distillation, per the kit.

## Findings (build faults and fixes)

| # | Finding | Fix | Status |
|---|---|---|---|
| F1 | The fit wave's question "is it written down?" has no field in the fixed summary block (both fit runs) | Moved to Brandon's discovery call; wave-fit trimmed; checklist updated | **Fixed** |
| F2 | A6 failed 20 of 23 draft lines, mostly on **new hire** (12) and **tripwire** (8). A5's draft lines lack worked examples and concrete tripwires, because the documents rarely contain them | A5 drafts each guardrail with good-call and bad-call slots, and each model with a tripwire. Where the sources have none, it writes "needs an example from the CEO" instead of leaving the line bare. Those become sign-off questions | **Fixed** (Mack, 2026-11-11) |
| F3 | A6 marks every **hindsight** test "unclear": it has no past decisions to test against | A6 labels hindsight "needs CEO: name a past decision", and the sign-off agenda gets 2–3 hindsight checks | **Fixed** (Mack, 2026-11-11) |
| F4 | A5's phrasing C leans on one reading of an ambiguous line in the plan ("This is the one…"). A5 flagged this itself | Correct behaviour. Keep A5's rule to flag interpretive risk | No change |

## What only Brandon can do (timed against rp2b budgets)

| Touchpoint | Budget | Inputs ready |
|---|---|---|
| Fit-check decision | 20 min | `a2-fit-synthesis.md` (plus the two summary blocks) |
| A13 extraction read | 20 min | `a13-extraction.md` (stop before the Trap log) |
| CEO interview summary read | 20 min | the summary block in `ceo-interview.md` |
| Judge and rewrite the sheet | 120 min | `a5-draft.md` and `a6-check.md`, with the checklist in `../../checklists/review-checklists.md` |

The exit test is each touchpoint within 30% of its budget. Log minutes in `../../templates/client-tracker.md`.
