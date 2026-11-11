# Override log (template)

*Updated 2026-11-11 for the Rotor Distillation: step S12 (A13, the document distiller) added. Companies now start on a rolling basis, so "intake" no longer applies; the tally runs across all companies. S1 to S12 apply to the Distillation (not every step is used there: S3, S4, S7 and the noise audit are Beta-only).*

**This is a blank template.** Copy it to your private library before the first company. The filled-in log never goes in this repo, never in anything a client sees, and never into a client's workspace.

The override log applies Rotor's own rule to Brandon: repeated overrides are information, not noise.

## What gets logged

Every time you change an AI draft, one line:

```
date | company code (e.g. CO-1) | step (S1–S12) | change: none · cut · added · reworded · reordered · replaced
     | why: wrong · weak · tone · missing context · judgment call | minutes spent | method note (optional, about the agent's instructions, never about the client)
```

## Steps

| Step | Agent | What it drafts |
|---|---|---|
| S1 | A1 | Interviewer summary blocks |
| S2 | A2 | Wave syntheses |
| S3 | A3 | Wave 2 follow-ups and wave 3 file |
| S4 | A4 | Divergence summary and language harvest |
| S5 | A5 | Distillation: Rotor Sheet drafts (phrasings, guardrails, models). Beta: schwerpunkt candidates, guardrails, living models, tripwires |
| S6 | A6 | Five-tests mark-up |
| S7 | A7 | CEO video script and guardrail clips |
| S8 | A8 | Red-team annotations |
| S9 | A9 | Flight logs |
| S10 | A11 | Pulse syntheses |
| S11 | A12 | Results pack (Distillation mode: before/after within the beta team; Beta mode: against a comparison team) |
| S12 | A13 | Document extraction (made in the client's own AI, emailed to Brandon). Log what Brandon changes, discards or has to ask the CEO about when he works from it |

## Rules

- **Private.** It lives in Brandon's private library, never in anything a client sees, and never in this repo.
- **No client content.** Step labels and categories only. No paraphrase of a draft, no company names, no quotes. It holds no client strategy data, so it stays within the hosting rule. If you need the actual draft to remember a lesson, it stays in the client's Rotor workspace.
- **No-change steps count too.** Keep a tally per step ("S9: approved unchanged ×4"), so you get the override rate and not only the overrides.
- **A step becomes a candidate to hand further to AI** when it has 15 or more observations across 3 or more companies, an override rate under 15%, and no "wrong" in its last 10.
- **Handing a step over is decided at a track gate**, never silently.
- **S5 (schwerpunkt candidates) is never handed over**, whatever the numbers say. The Mirror and the CEO review are not logged steps; they stay Brandon's.
- **S5 is logged for learning only.** For the first two companies, write your own one-line view before opening A5's draft; keep that note in the client's workspace. The log records only whether your view matched A5's options: yes · partly · no.
- **Reviewed periodically** (after every four companies, or at a track gate). Ines produces the override-rate table below, and Brandon decides. The same review compares actual minutes against the spec's budgets.

## The log (blank)

| Date | Code | Step | Change | Why | Min | Method note |
|---|---|---|---|---|---|---|
| [YYYY-MM-DD] | [CO-1] | [S1–S12] | [none / cut / added / reworded / reordered / replaced] | [wrong / weak / tone / missing context / judgment call] | [ ] | [optional] |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

## Tally (running, per step)

| Step | Approved unchanged | Changed | Total | Companies seen | "Wrong" in last 10 |
|---|---|---|---|---|---|
| S1 | [ ] | [ ] | [ ] | [ ] | [ ] |
| S2 | | | | | |
| S3 | | | | | |
| S4 | | | | | |
| S5 (match: yes / partly / no) | | | | | |
| S6 | | | | | |
| S7 | | | | | |
| S8 | | | | | |
| S9 | | | | | |
| S10 | | | | | |
| S11 | | | | | |
| S12 | | | | | |

## Override-rate review (periodic)

Override rate = changed ÷ total. Candidate = 15+ observations, 3+ companies, rate under 15%, no "wrong" in last 10. S5 is never a candidate.

| Step | Observations | Companies | Override rate | Last-10 "wrong"? | Avg minutes | Budget minutes (spec section 4) | Candidate to hand to AI? | Decision (Brandon) |
|---|---|---|---|---|---|---|---|---|
| S1 | [ ] | [ ] | [ ]% | [yes / no] | [ ] | [ ] | [yes / no] | [ ] |
| S2 | | | | | | | | |
| S3 | | | | | | | | |
| S4 | | | | | | | | |
| S5 | | | | | | | never | [ ] |
| S6 | | | | | | | | |
| S7 | | | | | | | | |
| S8 | | | | | | | | |
| S9 | | | | | | | | |
| S10 | | | | | | | | |
| S11 | | | | | | | | |
| S12 | | | | | | | | |
