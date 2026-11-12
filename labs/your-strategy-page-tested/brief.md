# Brief: Your Strategy Page, Tested
*Would it change a decision?*

Scout: Juno · Date: 2026-11-12 · Status: for G2 (Go/No-go)

## 1. The Spark in one line
A free instruction text an owner copies into their own AI (ChatGPT, Claude, Copilot or Gemini), then pastes their strategy page under it, and gets a line-by-line verdict against five tests, with plain reasons. Built on agent A6 (`rotor/product/build/agents/a6-five-tests-checker.md`).

## 2. Who it's for and the job it does
**Audience:** owner-led SME leaders who already have a strategy page, plan or values list somewhere. Story speaks to the SME owner; buyer type in the lab card: `sme-owner`.

**Job:** "Tell me, honestly, which lines on my strategy page would actually change something someone does, and which are just nice words." It marks up; it does not rewrite and does not say what the strategy should be. That is a feature: the owner stays the author.

**The five tests** (Franklin Kinetics' own material, `rotor/beta-playbook.md`, "The five tests"):
1. Decision: would this line change a choice someone makes?
2. Trade-off: does it name something good we give up?
3. New hire: could someone apply it on day one without asking?
4. Hindsight: would it have pointed the right way on real past decisions?
5. Tripwire: is there a signal that would prove it wrong?

## 3. Sources
| Source | Link | Licence / terms | Freshness | Quality notes |
|---|---|---|---|---|
| The five tests (table and examples) | `rotor/beta-playbook.md`, "The five tests" | Franklin Kinetics' own; Brandon cleared to publish 2026-11-11 (`logs/decisions.md`) | Current | Only the five tests and their pass/fail examples go public. |
| Agent A6 instruction block | `rotor/product/build/agents/a6-five-tests-checker.md` | Franklin Kinetics' own | Current; the simulation tested it | Written for Rotor Sheets (Schwerpunkt, guardrails, living models) and a loaded Rotor Core. The public version must be generalised and must not reference or describe the Core (guardrail 12). |
| Outside data | none | n/a | n/a | No external data is used. |

**Comparables (context for the market scan only; not sources of content). All unverified: I did not open these pages, and current availability and terms were not checked.**
- ZOKRI "Free OKR Coach Kit" (https://zokri.com/ai-okr-coach): per search results, an AI prompt kit with 10 quality checks, an output format and rules; you paste it into an AI tool to review your OKRs. Closest in format to ours. Sign-up terms unknown. Unverified.
- Goals and Progress OKR Builder (https://goalsandprogress.com/okr-builder-alignment-tree/): per search results, a free browser tool that checks Key Results in real time, flags activity-based language, and needs no account. Hosted, narrower (OKRs). Unverified.
- Taskade OKR Generator (https://www.taskade.com/app/okr-generator-b78glkob82afey87): per search results, generates OKRs with a measurability check; free to clone. Account likely needed. Unverified.
- Context only: Rumelt's "kernel" (diagnosis, guiding policy, coherent actions) is used by some as a checklist for strategy (e.g. https://zokri.com/the-kernel). Different test set. Unverified.

Read of the field: the comparables I found check goals (OKRs), not a whole strategy page, and none that I saw tests for trade-off, hindsight or tripwire. Based on a brief search only; not a full scan.

## 4. Feasibility
**Easy**
- The core exists and was simulation-tested (A6). The Lab is packaging, plus a public instruction file and a short "how to use it" page.
- Text file works in any chat AI the owner already pays for; nothing hosted, no accounts, no data held by us (guardrail 11 is met by collecting nothing).
- A fixed output format already exists, so results look the same across runs.

**Hard**
- **Generalising A6.** It is written for a Rotor Sheet with named sections and a loaded Core. The public version has to work on any messy strategy page (a one-pager, a values list, a slide pasted as text) without our Rotor vocabulary leaning on the Core. Needs Fenn and Vera eyes on the wording.
- **Consistency across AIs.** Different models will follow the "never rewrite" and exact-format rules with different discipline. Needs a test run in all four before G3 passes.
- **Hindsight needs the owner to name real past decisions.** A6 already handles it: with none supplied, it marks "NEEDS CEO" rather than inventing. The instruction text must ask for the decisions up front, in one sentence, without making it a chore. Note the playbook table says "five real past decisions"; A6 says "any real past decisions". Needs one consistent public wording.
- **Never rewriting is a product choice.** Owners will ask "how do I fix it?" The text should hold the line without lecturing (guardrail 13) and without pointing to consulting (guardrail 7).
- **Phone use.** Pasting a long instruction and a page on a phone works but is clumsy; the instruction text should be short enough to copy in one go and the page must have a copy button and readable contrast (guardrail 14).

**Unknown**
- Whether very long strategy pages exceed what free-tier AI plans accept; we should state a rough size guide only after testing.
- Whether the Labs store requires any email or account to get a free item (Sol and Mack to check the platform).
- How owners react to a blunt FAIL on their own page. Tone needs testing on real pages (Brandon's own first).
- Hosted custom GPT / Claude project alternative: would be smoother for the user but means an account on one vendor, something hosted and maintained, and it fits one AI only. Ines recommends the text file. I agree: it matches "nothing hosted", works in all four AIs, and is the smallest thing that proves the point.

## 5. Four Proofs: first read
- **Speed:** A6 is built, so the work is generalising, packaging and testing in four AIs. Estimate about 1 to 2 hours of Brandon, at gates only. Ines owns the number at G2.
- **Abundance:** every company already has a strategy page, and most already pay for an AI tool. Nothing new to buy or host.
- **Craft:** one paste, any AI, fixed output format, honest FAIL/PASS/UNCLEAR with the deciding words quoted, and "never invent a past decision." The craft is in what it refuses to do.
- **Goodwill:** free, useful on its own, no sign-up wall, no data collected, no rewriting pushed on the owner.

**Vera flags to carry:** guardrail 12 (no Rotor Core contents; use the five tests only); 3 (describe what it does, no ROI); 7 and 8 (nothing implying a consulting price; the free tool must not push toward consulting); 11 (collect nothing); 14 (works on a phone).

## 6. Sol's first price read
*(Sol, 2026-11-12)*

**Number:** free (CAD 0). Packaging: a copy-paste instruction text plus a one-page how-to. No paid layer proposed.

**Why free:** the Lab's job is the five-minute feel and the favour owed. The tool delivers its value in one use, on the owner's own page, in their own AI. A price would turn it from a favour into a transaction and would sit awkwardly beside the Rotor Distillation and Beta, which stay unpriced (guardrail 7). It also leans on Franklin Kinetics' own tests, which we are already publishing.

**Sign-up wall:** recommend none. The text is on the page to copy. Nothing hosted means no form is needed to deliver it. If Brandon wants a newsletter list, the existing decision (2026-11-10: opt-in tick box on site forms, not pre-ticked) allows it as a separate, unticked option on the Lab page. It must never gate the text. I recommend we skip it for this Lab unless Brandon asks; a free layer with no ask is the stronger goodwill message.

**Comparables (all unverified, see section 3):** ZOKRI Free OKR Coach Kit (free AI prompt kit), Goals and Progress OKR Builder (free, no account), Taskade OKR Generator (free to clone). Market read: free is the norm in this space for checkers like this. Pricing anything above free here would read against the field. I did not find paid comparables doing line-by-line strategy testing; that is thin evidence, not proof there are none.

**Who it's for and the job:** the owner who wants to know whether their strategy page would change a decision.

**The Signal that free is wrong** (to watch after Release; numbers to be set at G5, none assumed here):
- Owners repeatedly ask for a hosted or saved version and say they would pay for it.
- Owners run it and then ask us to fix the page for them. That is a sign the free layer shows the problem but leaves a gap worth packaging (still must not become consulting, guardrail 8).
- It is copied in volume but nobody replies or comes back, so the favour is not landing and the Goodwill proof is not showing up in any signal.
Any of these, logged as a signal on the lab card, is a reason to revisit at G8.

**Storefront note:** free means no revenue and no GST/HST flag for this Lab.

## 7. Recommendation: BUILD

Reasons: it serves the Schwerpunkt directly (an owner feels their own strategy tested in five minutes), hits all four proofs credibly, rests on material already cleared to publish, and is the lightest Lab we could ship. Condition: the public instruction must be reworded without Rotor-Sheet or Core language (Vera to clear), and tested in all four AIs before G3.

**Proposed hours estimate for Brandon: about 2 hours. Ines to confirm at G2.**
- G2 read and decision, about 15 minutes.
- G3: run it on his own strategy page in at least two AIs and judge the tone, about 45 minutes.
- G4, G5, G6 and G7 quick passes (look, free packaging, voice and lesson, release), about 60 minutes in total.
Twice-estimate trigger (4 hours) would call a mini Go/No-go.

**Rotor Lesson:** TBD (Fenn).

## Open questions for Brandon
1. Does the Labs store need an email or account for a free download? (Sol and Mack to check.)
2. Hindsight wording: "five real past decisions" (playbook) or "any real past decisions" (A6)?
3. Newsletter tick box on the Lab page, or none for this Lab?
4. Which public words are fine to keep from A6 (e.g. "living model", "Schwerpunkt")? Vera to rule against guardrail 12.
