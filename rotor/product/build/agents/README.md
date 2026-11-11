# Rotor agent packs, A1 to A12

Plain-text instruction packs in the style of the Interviewer Pack: platform-neutral, one fixed output format each, and no agent decides. Each one drafts for Brandon (spec section 5 in `../../rp2-spec.md`).

**Where they run:** A2 to A7, A9 and A12 run in Brandon's own AI account, one private project per company, named by company code (decided at RP2, spec section 8). A1, A8, A10 and A11 run in the client's own AI. The Rotor Core is loaded separately and is not part of any pack.

**Override log:** every change Brandon makes to a draft gets one line under the step code below (spec section 6). S5 is logged for learning only and is never handed to AI.

## All agents

| Agent | What it does | File | Runs in | Step | Status |
|---|---|---|---|---|---|
| A1 Interviewer | Leader interviews, waves 1 to 3 | `rotor/interviewer-pack.md` (core instructions) | Client's AI | S1 | Existing |
| A2 Synthesizer | Themes, agreements, differences, unattributed quotes, language harvest, contested items | `a2-synthesizer.md` | Brandon's account, company project | S2 | Written |
| A3 Wave drafter | Wave 2 follow-ups per leader; the wave 3 file | `a3-wave-drafter.md` | Brandon's account, company project | S3 | Written |
| A4 Divergence drafter | Two-page divergence summary and language harvest, nobody quoted by name | `a4-divergence-drafter.md` | Brandon's account, company project | S4 | Written |
| A5 Candidate drafter | 3 to 5 schwerpunkt candidates as options, with what each gives up; never ranks or recommends | `a5-candidate-drafter.md` | Brandon's account, company project | S5 | Written |
| A6 Five-tests checker | Marks every sheet line against the five tests | `a6-five-tests-checker.md` | Brandon's account, company project | S6 | Written |
| A7 Script drafter | CEO video script and guardrail clips, in the language map | `a7-script-drafter.md` | Brandon's account, company project | S7 | Written |
| A8 Red-team runner | Puts the lead's dilemmas to the loaded AI, records the level, drafts annotations | `a8-red-team.md` | Client's AI | S8 | Written |
| A9 Flight log drafter | Under 300 words: heard, taking shape, next, one question | `a9-flight-log.md` | Brandon's account, company project | S9 | Written |
| A10 Noise audit | Same five decision cases to beta and comparison teams | `rotor/interviewer-pack.md` (noise audit variant) | Client's AI | none | Existing |
| A11 Pulse | Three questions monthly to the beta team; synthesis by team only | `a11-pulse.md` | Part 1 in the client's AI (team-facing); Part 2 (synthesis) in Brandon's account, company project | S10 | Written |
| A12 Results compiler | Beta vs comparison team, null results honestly, no financial claims | `a12-results-compiler.md` | Brandon's account, company project | S11 | Written |

## Order in the client journey

Weeks are the first company's (spec section 3). The three companies in an intake start a week apart.

| When | Agent | What happens |
|---|---|---|
| Week 0 | A1 | Install check: a test session confirms the summary block comes out right |
| Weeks 1 to 3 | A1, A10, A2 | Wave 1 interviews; noise audit baseline; A2 synthesis after each block |
| Week 3 | A3 | Wave 2 follow-up file per leader; Brandon approves |
| Weeks 3 to 5 | A1, A2, A4 | Wave 2 interviews and synthesis; A4 drafts the divergence summary and language harvest |
| Week 5 | A5, then A6 | A5 drafts options (Brandon writes his own view first); Brandon chooses and rewrites (T6); A6 checks the lines; A3 drafts the wave 3 file |
| Weeks 5 to 6 | A1, A2 | Wave 3 reactions; synthesis |
| Week 7 | A2 | Contested-items list for the Mirror pre-read |
| Week 8 | none | The Mirror (Brandon, live) |
| Weeks 8 to 9 | A6, A7, A8 | A6 checks the final sheet; A7 drafts the script; sheet and Core loaded into the team's AI; A8 runs the red-team dilemmas |
| Weeks 1 to 20 | A9 | Flight log: weekly in weeks 1–9, every two weeks in weeks 9–20; drafted by AI, approved by Brandon |
| Weeks 9 to 20 | A9, A11, A10 | Live run: flight logs; monthly pulse (A11); end-of-quarter noise audit (A10) |
| Week 21 | A12 | Results pack for the results video and the CEO review |

## Notes

- The Interviewer Pack stays unchanged; these packs sit beside it so the interviewer never sees synthesis instructions (spec section 7).
- Rules that apply to every pack: never invent a quote, fact or number; mark gaps as gaps; never attribute a quote to a named leader in anything meant for the client; say "beta team" and "comparison team".
