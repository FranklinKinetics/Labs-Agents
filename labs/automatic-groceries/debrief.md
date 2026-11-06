# Debrief · Automatic Groceries · DRAFT

**Status:** draft, waiting at G8 for Brandon's answers (2026-11-06)
**Run by:** Ines
**Why this Lab first:** it's already live, so a Debrief can't break anything. It's also the first G8 we've run, so it tests the Debrief itself.

---

## 1. What we know (from the repo)
| Item | What the canon says | Source |
|---|---|---|
| Status | Released, live in the Labs store | `logs/decisions.md`, 2026-11-06 |
| Gates G1–G7 | Grandfathered (built before the crew existed) | `lab.yaml` |
| Buyer | Household | `lab.yaml` |
| Story speaks to | SME owner | `lab.yaml` |
| Craft proof | "Works with Claude" | `lab.yaml` |
| Everything else | TBD: release date, store URL, price, format, free/paid layers, hours, job-to-be-done, Rotor Lesson | `lab.yaml` |
| Signals | None recorded | `lab.yaml` |

## 2. What we couldn't check
- **The live store page.** This cloud session can't reach franklinkinetics.com (blocked by the session's network settings), so the crew couldn't fill the TBD fields from the page itself.
- **Timing.** G8 is meant to run about 2 weeks after Release. Release date is unknown, so we can't confirm we're at the right point.

## 3. Signals
None on record. We will not estimate or fill these in. Brandon's answers go here.

| Signal | Value | Source |
|---|---|---|
| Release date | _Brandon_ | |
| Store visits since Release | _Brandon_ | checkout/analytics |
| Sales | _Brandon_ | checkout |
| Refunds | _Brandon_ | checkout |
| Replies / messages about it | _Brandon_ | |
| Conversations where an SME owner mentioned it | _Brandon_ | (tests LM1) |
| Anyone react to the build hours? | _Brandon_ | (tests LM3) |

## 4. Living Models: what this Debrief can say
| # | Belief | Evidence from this Lab | Proposed change |
|---|---|---|---|
| LM1 | Household products make SME owners think "imagine this in my company" | none yet | none until Signals are in |
| LM2 | Charging builds more credibility than giving away | none yet | none until Signals are in |
| LM3 | Showing build hours is persuasive | none: build hours were never logged for this Lab | none; note that this Lab **can't** test LM3 |
| PM1 | Free layer + paid layer earns goodwill without giving away value | none yet; free/paid layers not on the card | none until Signals are in |
| PM2 | Prices that read cheap anchor FK as cheap | none yet; price not on the card | none until Signals are in |

## 5. Friction review
`logs/friction-log.md` was empty before this Debrief. Two items added today (see the log): the lab card was never filled from the store page, and the store isn't reachable from cloud sessions.

## 6. What we learned about Debriefs
- A Debrief needs Signals, and nothing collects Signals yet. Next Labs should name, at G5, **where** the visit and sales numbers will come from (Sol's checkout recommendation), so G8 is a lookup, not an archaeology dig.
- Grandfathered Labs carry no hours, so they can't add to the Speed proof or LM3.
