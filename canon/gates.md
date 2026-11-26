# Gates

Two gates, only for things that are hard to undo. Set by Brandon on 2026-11-26; the eight-gate system (old G1–G8) is retired (see "Retired" below).

## The gates

| Gate | Covers | Examples | Packet from |
|---|---|---|---|
| **G1 Release** | Anything public | A Lab page going live or changing, a price, an outreach template, each outreach batch, a public post | Ines, with Vera's clearance attached |
| **G2 Money** | Anything that spends money or commits Brandon to a client | A paid tool or subscription, an ad, a proposal, a client agreement, a promised date or deliverable | Ines |

**Outreach batches:** Brandon pressing send in his own Gmail *is* the G1 release for that batch. The crew never sends on his behalf.

## Everything else
- **Vera clears it.** Brandon sees an item only when Vera flags it: a guardrail call she can't settle, or a "must fix" the crew can't fix.
- **If the crew is unsure whether something needs Brandon, it doesn't.** Do it, and log it in the weekly review.
- Reversible work (builds, drafts, internal docs, logs, loop changes, research) never waits on Brandon.

## Packet format (one phone screen)
```
G<1|2> · <item> · <date>
Verdict: <what the crew recommends, one line>
• <bullet>
• <bullet>
• <bullet>                         (three at most)
Decide: <one question> → pass · pass with changes · hold
```
Packets go in `QUEUE.md`. Full detail (clearance, sources, drafts) sits in the repo, linked by path, never in the packet.

## Rules
- Silence is not a pass. An unanswered item stays in `QUEUE.md`.
- Never pass a gate on Brandon's behalf.
- Vera can stop anything at any time for a guardrail issue.
- Every outcome is logged in `logs/gates-log.md`.
- `QUEUE.md` must clear in under an hour a week. If it won't, Ines cuts or batches before posting.

## Retired (2026-11-26)
Old G1 Spark, G2 Go/No-go, G3 Prototype, G4 Look, G5 Package, G6 Story, G7 Release and G8 Debrief. Their checks now live in Vera's clearance (`crew/vera.md`) and Ines's Debrief. The old "three clean passes" retirement rule and the 2× hours mini Go/No-go are retired with them; hours are still logged on each lab card and reported in the weekly review.
