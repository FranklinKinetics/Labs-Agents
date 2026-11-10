# Brief · Rotor Alignment Diagnostic

**2026-11-10 · For G1/G2**
Compiled by Ines in Juno's Brief format, from the design work already done (files 01–09). Sol's first price read is the $790 Brandon approved on 2026-11-10. Fenn's Rotor Lesson is proposed below.
Nothing has been built, published, sent or bought.

---

## G1/G2 gate packet

```
GATE G1/G2 · Rotor Alignment Diagnostic · 2026-11-10
Decision needed: does this Lab get built?
Recommendation: build. The design is done and approved piece by piece;
  the Lab lifecycle now adds what it was missing: a free layer, a
  Rotor Lesson, a Look (G4) and a Story with a Substack note (G6).
Four Proofs check: Speed: hours logged from here · Abundance: leaders'
  own knowledge + AI the company already has · Craft: one interviewer,
  four platforms, sealed synthesis · Goodwill: OPEN, needs a free layer
Risks / Vera flags: first Lab that holds personal information (briefly);
  first Lab whose buyer is an SME owner, not a household
Hours: Brandon estimate 8h to Release · crew sessions 11
Reply: pass · pass with changes · hold
```

**Brandon also decides at this gate:** the free layer (question 2) and the Rotor Lesson (question 3).

---

## 1. What it is

A self-serve diagnostic. Each of 3–8 leaders takes one ~20-minute AI interview in their company's own AI platform. An agent combines their summaries into a report on where the leadership team agrees, where it differs, and what it must settle. The report ends with one offer: the Rotor Beta.

## 2. Who it's for, and the job

**Buyer:** the CEO of an owner-led company, 20–200 people, outside Quebec. The first Lab sold straight to the SME owner rather than to a household.
**Job:** "Show me where my leadership team agrees, where it differs, and what we still have to settle, without a consultant in the room and without my leaders feeling watched."
**Where it sits:** in the Labs store, and linked from How It Works ("Not ready for the Beta? Start here") and from Start a conversation (decision 2026-11-10).

## 3. Sources

There is no outside dataset. The "data" is what the leaders say, and they own it.

| Source | Terms | Notes |
|---|---|---|
| Rotor Interviewer Pack, wave 1 questions 1–9 | Franklin Kinetics' own material | Reused word for word for comparison with Beta data. No Rotor Core content. |
| Anthropic Claude API | Commercial terms | Writes the report. Juno confirms retention and no-training terms before build. |
| Google Cloud, Montréal | Commercial terms | Proposed home for the drop-box (crew recommendation, 2026-11-10). Mack confirms. |
| Squarespace Commerce | Already in use | Labs store checkout. |

## 4. Feasibility

**Easy:** the interviewer (written and tested against the Pack), the report template, the sample, the price, the copy, the privacy notice and terms. All approved.
**Hard:** the drop-box. It must strip names before storing anything, count submissions, close windows, call the agent, run checks and delete on delivery. A small app, not a no-code chain.
**Unknown:**
- Whether Squarespace can tell the app about a purchase automatically. If not, the CEO enters their order number on a start page.
- Real setup time on each platform (the solo run measures it).
- Whether real leaders are candid, and whether a CEO can guess who said what (the first paid sales test it, each report read by the crew before it goes out).

## 5. Four Proofs (first read)

| Proof | Read |
|---|---|
| **Speed** | Built by one person with an AI crew. Hours logged from G2. Most of the design is already done. |
| **Abundance** | What every leader already knows but never says out loud in a meeting, plus the AI tools the company already pays for. Nothing new to buy or install. |
| **Craft** | One plain-text interviewer that runs the same on four AI platforms; a sealed drop-box; an AI-written report with automatic anonymity checks. |
| **Goodwill** | **Open.** Fair flat price, a free restart, and a report that's useful without the Beta. But every Lab needs a free layer, and this one has none yet (question 2). |

## 6. Sol's first price read

**$790 CAD flat**, approved 2026-11-10 against verified comparables (`06-package-price.md`). Sol re-confirms it at G5 alongside the free layer. Guardrail 7 holds: the Lab shows its price, and the Beta stays unpriced.

## 7. Hours estimate (Ines)

Brandon's hands-on hours from G2 to Release, estimated:

| Step | Hours |
|---|---|
| Gate reviews (G3–G7) | 2 |
| Accounts: Google Cloud, Anthropic API, Squarespace product | 1.5 |
| Solo run on two platforms | 2.5 |
| Reading the first one or two real reports before they go out | 1 |
| Buffer | 1 |
| **Total** | **8** |

If actual hours pass 16, Ines calls a mini Go/No-go.

## 8. Recommendation

**Build**, with a free layer added before G5.

## 9. Questions for Brandon

1. **Gate pass.** Build it?
2. **Free layer.** Every Lab needs one. Options, with the crew's pick first:
   - **A. "Try the interview yourself" (recommended).** A free download: the interviewer for one person. The CEO takes it alone and sees their own summary, the same way their leaders will. It costs nothing to run, shows the craft, and leads to "now ask your team." It gives away nothing secret: the interviewer ships to every buyer anyway and holds no Rotor Core.
   - **B. The fictional sample report.** Larchmere, labelled fictional. Shows what you get.
   - **C. Both.**
3. **Rotor Lesson.** Fenn proposes: *"You don't know your leadership team agrees until you ask each leader alone."* Approve, change, or ask for alternatives.
4. **Your hours so far.** Roughly how much time have you spent on the gate reviews to date? It goes on the card as Brandon's hours.

## 10. Things this reclassification changes

- **Store page, not a standalone page.** The diagnostic's page becomes its Labs store product page. The copy in `07-website-copy.md` is reworked into a store page at G6, with a Substack note. The links from How It Works and Start a conversation stay.
- **Gates now count.** G1–G8 outcomes for this Lab count toward gate-retirement streaks. The earlier per-deliverable gates do not.
- **Beta Playbook says otherwise.** `rotor/beta-playbook.md` says the diagnostic is "not in the Labs store, whose buyers are households." That line is now out of date. Brandon may want to update the master doc.
- **Audience.** The ontology describes Lab buyers mainly as households. This Lab sells straight to the SME owner, which the lab card allows (`buyer: sme-owner`).
