# Rotor agent packs, A1 to A13

Plain-text instruction packs in the style of the Interviewer Pack: platform-neutral, one fixed output format each, and no agent decides. Each one drafts for Brandon.

**Two programs, one set of packs.** The **Rotor Distillation** (the AI side, `../../rp2b-spec.md`, section 4) uses nine of them. The **Rotor Beta** (alignment, people and AI, `../../rp2-spec.md`, section 5) uses the original set. A5 and A12 each have a Distillation mode and a clearly separated Beta mode.

**Where they run:** A2, A3, A4, A5, A6, A7, A9, A12 run in Brandon's own AI account, one private project per company, named by company code, with training switched off in its settings. A1, A8, A10, A11 (part 1) and **A13** run in the client's own AI. The Rotor Core is loaded separately and is not part of any pack. Brandon receives only the summary blocks and the A13 extraction block, by email, never the documents or full transcripts (Distillation).

**Override log:** every change Brandon makes to a draft gets one line under the step code below (`../templates/override-log.md`). S5 is logged for learning only and is never handed to AI.

## All agents

| Agent | What it does | File | Runs in | Step | Distillation | Beta |
|---|---|---|---|---|---|---|
| A1 Interviewer | Interviews; wave files: fit, CEO (Distillation), waves 1 to 3 (Beta) | `rotor/interviewer-pack.md` (core instructions) | Client's AI | S1 | **Used** (fit, CEO and wave 3 reaction files) | Used |
| A2 Synthesizer | Themes, agreements, differences, unattributed quotes, language harvest, contested items | `a2-synthesizer.md` | Brandon's account | S2 | **Used**, on fewer blocks | Used |
| A3 Wave drafter | Wave 2 follow-ups per leader; the wave 3 file | `a3-wave-drafter.md` | Brandon's account | S3 | Not used (Beta-style rounds) | Used |
| A4 Divergence drafter | Two-page divergence summary and language harvest | `a4-divergence-drafter.md` | Brandon's account | S4 | Not used | Used |
| A5 Candidate drafter | **Distillation mode:** 2 to 3 sharper phrasings of the main effort the company already chose, plus guardrails, living models with tripwires and a language map; gaps flagged, never filled. **Beta mode:** 3 to 5 candidates as options | `a5-candidate-drafter.md` | Brandon's account | S5 | **Used (changed)** | Used |
| A6 Five-tests checker | Marks every sheet line against the five tests | `a6-five-tests-checker.md` | Brandon's account | S6 | **Used** | Used |
| A7 Script drafter | CEO video script and guardrail clips | `a7-script-drafter.md` | Brandon's account | S7 | Not used (no CEO video) | Used |
| A8 Red-team runner | Puts the lead's dilemmas to the loaded AI, records the level, drafts annotations | `a8-red-team.md` | Client's AI | S8 | **Used** | Used |
| A9 Update drafter | Under 300 words: heard, taking shape, next, one question | `a9-flight-log.md` | Brandon's account | S9 | **Used**, every two weeks | Used |
| A10 Noise audit | Same five decision cases to beta and comparison teams | `rotor/interviewer-pack.md` (noise audit variant) | Client's AI | none | Not used (needs a comparison team and a quarter) | Used |
| A11 Pulse | Three questions to the beta team; synthesis by team only | `a11-pulse.md` | Part 1 client's AI; Part 2 Brandon's account | S10 | **Used**, once | Used, monthly |
| A12 Results compiler | **Distillation mode:** before/after within the beta team. **Beta mode:** beta vs comparison team | `a12-results-compiler.md` | Brandon's account | S11 | **Used (changed)** | Used |
| **A13 Document distiller** | Reads the CEO's strategy material and extracts stated priorities, trade-offs, beliefs, measures and language, quoted; flags gaps and contradictions; fills nothing | `a13-document-distiller.md` | **Client's AI** | **S12** | **New** | Not used |

## Order in the Distillation journey

Weeks are one company's (rp2b-spec, section 2). Starts are rolling, with at most two companies in weeks 1 to 4 at once.

| When | Agent | What happens |
|---|---|---|
| Weeks -2 to 0 | A1, A2 | **Fit check** (unless the company has a diagnostic report): CEO and 1 to 2 leaders each do one 20-minute interview on the fit wave file; A2 combines the blocks; Brandon decides Distillation or Beta |
| Week 0 | **A13** | The CEO pastes the strategy material into A13 in their own AI and emails Brandon the extraction block (never the documents) |
| Week 1 | none | CEO kickoff call |
| Weeks 1 to 2 | A1, A2 | CEO interview (CEO wave file); 1 to 2 more leaders optional; A2 synthesis |
| Weeks 2 to 3 | A5, then A6 | A5 drafts the Rotor Sheet from the extraction and summaries; Brandon judges and rewrites (S5); A6 runs the five tests |
| Week 3 | A1, A2 | Leaders react in writing through the wave 3 file; A2 synthesis |
| Week 4 | none | CEO sign-off session |
| Weeks 4 to 5 | none | IT loads the Sheet and the Core using `../client-pack/loading-guide.md`; employee note and behaviour summary published |
| Week 5 | A8 | Team lead's dilemmas run as the red-team |
| Weeks 5 to 11 | A9, A11 | Live use, six weeks: an update every two weeks (A9); one pulse (A11) |
| Week 12 | A12 | Results pack (Distillation mode) for the CEO review |

## Notes

- The Interviewer Pack stays unchanged; these packs sit beside it so the interviewer never sees synthesis instructions.
- Rules that apply to every pack: never invent a quote, fact or number; mark gaps as gaps; never attribute a quote to a named leader in anything meant for the client; say "beta team" (and, in the Beta only, "comparison team").
- The Distillation never uses "intake", "Mirror day" or "waiting room" (retired 2026-11-11).
