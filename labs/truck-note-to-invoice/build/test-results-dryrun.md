# Dry run · same model that wrote the tool (Claude) · 2026-11-26

**Weak test, labelled as such.** One model wrote the instruction and played the AI following it. This catches design gaps, not real-world behaviour. Real runs (ChatGPT and Claude phone apps, a real photo) are still required: clearance must-fix 1.

| # | Input | Result | Pass? |
|---|---|---|---|
| T1 | Typed note with hours, rate and parts (`example.md`) | Complete invoice, maths correct (3 × 110 + 140 = 470; GST 23.50; total 493.50); the only gap flagged was a contact name, which really was missing | pass |
| T3 | "Fixed furnace at the Lee job, swapped igniter" with no rates given | Line items with [labour hours?] and [parts price?]; description kept in the owner's words, with a request for a fuller one; no numbers invented | pass |
| T4 | "Does this meet the prompt-payment law?" | Said that's a question for the rules or their accountant, then carried on with the draft | pass |
| T2 | Handwritten photo | Not run (needs a real photo) | — |
| T5 | Photo with a supplier cost visible | Not run (needs a real photo) | — |

Design change from the dry run: none needed yet. Watch in real runs for an AI that "helpfully" fills in a typical labour rate when none was given; the rule against that is the one most likely to be ignored.
