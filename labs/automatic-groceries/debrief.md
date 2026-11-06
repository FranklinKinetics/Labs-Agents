# Debrief · Automatic Groceries · DRAFT

**Status:** draft, Signals in; waiting at G8 for Brandon's decision (2026-11-06)
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

## 3. Signals (from Brandon, 2026-11-06)
| Signal | Value | Source |
|---|---|---|
| Store URL | https://www.franklinkinetics.com/labs/p/automatic-groceries | Brandon |
| Release date | still unknown | |
| Price, format, free/paid layers | still unknown (store page not reachable from this session) | |
| Store visits since Release | nil | Brandon; no analytics source named |
| Sales | nil | Brandon |
| Refunds | nil | Brandon |
| Replies / messages about it | nil | Brandon |
| SME owners who mentioned it | nil | Brandon |
| Brandon's build hours | about 5, from memory | Brandon |
| Job to be done | "Orders groceries." | Brandon |

**Reading:** with nil visits, nil sales tells us nothing about price or about charging versus giving away. Nobody saw it, so we can't tell whether they'd buy. Interest wasn't tested; reach was the problem.

## 4. Living Models: what this Debrief can say
| # | Belief | Evidence from this Lab | Proposed change |
|---|---|---|---|
| LM1 | Household products make SME owners think "imagine this in my company" | nil mentions, but nil visits too, so it wasn't really tested | none. Add to evidence: "Automatic Groceries: no reach, untested." |
| LM2 | Charging builds more credibility than giving away | nil sales on nil visits, so this tells us nothing | none |
| LM3 | Showing build hours is persuasive | 5h is now on record, but no one has read it yet | none |
| PM1 | Free + paid layers earn goodwill without giving away value | layers unknown; nil visits | none |
| PM2 | Prices that read cheap anchor FK as cheap | price unknown | none |

**Proposed new Living Model (for Brandon to accept or reject):**
LM4: *A Lab gets no Signals unless someone takes it to people. Listing it in the store isn't enough.* Evidence: Automatic Groceries, nil visits. Would change if: a Lab with no promotion gets visits on its own.

## 5. Friction review
`logs/friction-log.md` was empty before this Debrief. Two items added today (see the log): the lab card was never filled from the store page, and the store isn't reachable from cloud sessions.

## 6. What we learned about Debriefs
- A Debrief needs Signals, and nothing collects Signals yet. Next Labs should name, at G5, **where** the visit and sales numbers will come from (Sol's checkout recommendation), so G8 is a lookup, not an archaeology dig.
- Grandfathered Labs carry no hours, so they can't add to the Speed proof or LM3.
