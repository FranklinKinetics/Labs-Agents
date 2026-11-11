# Reconciliation · Rotor Alignment Diagnostic × Rotor Product

**2026-11-11 · Draft for Brandon · written for Ines (Steward), with Vera's guardrail lens applied**
This memo changes nothing. No other file was edited. Nothing was built, committed, published or sent.

**What was read:** every file in `labs/rotor-alignment-diagnostic/` (lab card, brief, files 01–09, the build plan, README, prompts and code), every file in `rotor/product/`, the three Rotor docs in `rotor/`, the canon, and `logs/decisions.md` from top to bottom. Later decisions were followed over earlier ones.

---

## 1. Packet

```
RECONCILIATION · Rotor Alignment Diagnostic × Rotor Product · 2026-11-11
Decision needed: agree how the diagnostic hands buyers to the Rotor
  Distillation or the Rotor Beta, so both efforts say the same thing
  before any more building.
Recommendation: keep the diagnostic as built. Make five small fixes
  first. The report names both ways forward and gives no verdict. The
  CEO's own copy of the report is the fit check. Brandon makes the call.
Conflicts found: 5 must-resolve before build · 7 to fix at a later Lab
  gate · 9 wording only
Risks / Vera flags: (1) leaders were told the report is for their CEO;
  Brandon may read it only when the CEO sends it. (2) The site privacy
  policy says Labs send nothing back; this Lab does.
Reply: agree · agree with changes · hold
```

**The short story.** The two efforts mostly agree. The diagnostic was designed when the Beta was the only next step. On 2026-11-11 you decided "The diagnostic sorts buyers between them." Nothing in the diagnostic was changed to match. Rotor Product knew that and left the diagnostic's approved copy alone on purpose (`rotor/product/story/website-changes.md`, D4 and the last section). The gaps below are what was left for this gate.

---

## 2. The picture

```
                "Do your leaders already agree on where the company is going?"
                                        │
              not sure                  │  think so, or clearly not
                 ▼                      │
   ┌───────────────────────────┐        │
   │ ALIGNMENT DIAGNOSTIC      │        │
   │ Lab · CAD $790            │        │
   │ none of Brandon's time    │        │
   │ report: each leader's     │        │
   │ main effort, side by side │        │
   │ no names · no verdict     │        │
   └─────────────┬─────────────┘        │
                 │ the CEO starts a     │ no report? the CEO and 1–2 leaders
                 │ conversation and     │ each do one short AI interview
                 │ sends the report     │
                 ▼                      ▼
        ┌─────────────────────────────────────────┐
        │ FIT CHECK · Brandon reads and decides   │
        │ never automated                         │
        └───────────┬─────────────────┬───────────┘
          broadly agree            clearly differ
                    ▼                 ▼
        ┌──────────────────┐  ┌──────────────────────────┐
        │ ROTOR            │  │ ROTOR BETA               │
        │ DISTILLATION     │  │ alignment, people and AI │
        │ the AI side      │  │ unpriced · unchanged     │
        │ unpriced         │  │                          │
        └──────────────────┘  └──────────────────────────┘
```

Think of the diagnostic as the scale at a weigh station. It shows the weight. It does not tell the driver which road to take. The driver and Brandon read the number together.

**What the report already gives the fit check.** The fit check needs one thing from the diagnostic: the leaders' main efforts side by side (`rotor/product/build/checklists/review-checklists.md`, lines 7–13). The report already has that in section 2, plus the line that counts different answers ("Five leaders gave four different answers", allowed by decision 2026-11-10). Rotor Product asks for no score, no threshold and no label. I searched for one and found none. The other two fit questions (is there a written strategy; would it pass the five tests) come from Brandon's discovery call, not from the diagnostic.

---

## 3. Conflict table

File references are `file:line`. "RP" means the Rotor Product track. Diagnostic paths are inside `labs/rotor-alignment-diagnostic/`. Rotor Product paths are inside `rotor/product/` unless they start with `rotor/`.

### 3a. Must resolve before build (5)

These touch code, prompts, the report, the data flow or an interviewer file.

| # | The diagnostic says | Rotor Product says | Decision that governs | Recommended resolution |
|---|---|---|---|---|
| **M1** | The report ends with one offer, the Beta. Fixed text in section 9 (`04-synthesis-agent.md:198`, `build/diagnostic/prompts/report_template.md:47–52`). The app holds any report whose section 9 differs (`build/diagnostic/checks.py`, "section 9"). | The diagnostic sorts buyers both ways. Fenn already drafted the extra line for "the diagnostic's own gate" (`rotor/product/story/website-changes.md:345`). The playbook list says the same (`playbook-changes.md:133`). | 2026-11-11: "The diagnostic sorts buyers between them." This is later than 2026-11-09 "the entry step before the Rotor Beta" and 2026-11-10 "Beta description … is accurate". The Beta sentence stays accurate, so it is kept word for word. | Section 9 names both ways and keeps one link. The report still gives no verdict. The reader sorts themselves; Brandon confirms at the fit check. |
| **M2** | The report template asks for a minimum number of splits: "2–5 splits", "2–5 trade-offs", "2–4 effects", "3–7 questions" (`04-synthesis-agent.md:167, 170, 175, 193`; rule at `:103`). Another line says an empty section gets one sentence (`:125`). The two pull against each other. The only test company, Larchmere, is badly split. | For a team that broadly agrees, "its report is the check" (`package/offer.md:66`; `rp2b-spec.md:45`). So the report must be able to show agreement honestly. | 2026-11-11 "sorts buyers between them", and 2026-11-09 "never invent" (guardrail 5: no invented quotes or results). | Remove the minimums. Let the agent say "your views don't split here" in one sentence. Add an invented, broadly aligned test company to the bench. |
| **M3** | Summaries arrive, names are stripped, and they are deleted on delivery. The report never says who said what (`02-product-spec.md:72`; `04-synthesis-agent.md:94–100`). | The short wave 1 file says "Wave 0 is the leader's diagnostic result" and tells Brandon to "read each leader's wave 0 answers" (`build/interviews/wave-1-short.md:7, 11`). Those per-leader answers do not exist. The RP2 spec already corrected this (`rp2-spec.md:237`); the wave file was "kept as it was". | 2026-11-09: "Summary blocks are always deleted" and "all quotes unattributed". The ontology: wave 0 is used "with its consent". | Wave 0 is the report, at team level. A leader gets the short file only if they choose to forward their own saved summary. No change to the diagnostic. |
| **M4** | The report goes to the CEO. Franklin Kinetics keeps a copy only if the CEO ticks a box, "for Franklin Kinetics' research" (`02-product-spec.md:64`), used "only to improve our own work and to compare patterns across companies" (`09-privacy-and-terms.md:76`). A person at Franklin Kinetics sees a report only if a check holds it or the CEO agreed to keep it (`09:71`). | The report is the fit check and wave 0. One line says the kept copy "becomes wave 0 if the company goes on" (`playbook-changes.md:137`; also `rp2-spec.md:237`). But the Distillation's data lists say Brandon receives "two things by email" (`package/offer.md:96`; `website-changes.md:205`; `client-pack/governance-one-pager.md:21`). The report is a third thing. | 2026-11-09: keep the report "with the client's consent" for comparison. 2026-11-10: "No hosting of client strategy data unless Brandon approves it at a gate." 2026-11-11: summary block only, plus the A13 digest. | The fit check and wave 0 always use the copy **the CEO sends**. Brandon never pulls the kept research copy. Add the report to the Distillation's data lists. No change to checkout or code. |
| **M5** | The link printed in every report defaults to `…/start-a-conversation`, marked "confirm real URL" (`build/diagnostic/config.py:14`). | The site map says Start a conversation is `/contact` (`rotor/website-copy.md:19`). The offer sheet links to `https://franklinkinetics.com/contact` (`package/offer.md:107`). | None found. This is a fact only Brandon can confirm. | Use the site's `/contact` address once Brandon confirms it. |

### 3b. Fix at a later Lab gate (7)

Nothing here blocks the build. Each is parked at the gate where it belongs.

| # | Gate | The diagnostic says | Rotor Product says | Decision that governs | Recommended resolution |
|---|---|---|---|---|---|
| **L1** | G6 Story | How It Works block: "Not ready for the Beta? Start here." and "the first step" (`07-website-copy.md:152–154`). | Suggested: "Not sure which one fits? Start here." (`website-changes.md:342–343`). The ladder says "Not sure? The alignment diagnostic finds out." (`package/offer.md:35`). | The old headline is quoted inside your decisions of 2026-11-09 and 2026-11-10. The 2026-11-11 sorting decision is later. | Take Fenn's wording at G6. It needs your word because the old headline is in the decisions log. |
| **L2** | G6 Story | Diagnostic page FAQ "What comes after?" and the "handoff to the Beta" table name only the Beta (`07:130–131, 172–179`). | Suggested two-way answer (`website-changes.md:344`). | 2026-11-11 "sorts buyers between them". | Rewrite at G6 to match the report's new section 9 (M1). |
| **L3** | G6 Story | The How It Works block, the Start a conversation link and the form option "I've done the alignment diagnostic" are approved (`07:150–168`) but are **not** in `rotor/website-copy.md`. | The RP5 list assumes they are already there: "The diagnostic's approved block still follows it" (`website-changes.md:120`) and "stays under it, unchanged" (`:297`). | 2026-11-11: "Brandon pastes them into the Claude Doc masters". | Paste the RP5 list first, then the diagnostic's block and link at G6, with L1's wording. Unclear whether the master doc already has them; the repo copy does not. |
| **L4** | G6, checked at G7 | The page is `/alignment-diagnostic`, "not in the main navigation" (`07:34`). The brief says it becomes a Labs store product page (`brief.md`, section 10). The app's privacy and terms links assume `/alignment-diagnostic/…` (`config.py:15–16`). | The ladder and How It Works link to `/alignment-diagnostic` (`website-changes.md:85, 107`). | 2026-11-10: "sold in the Labs store, and also linked from How It Works … and from Start a conversation". | Pick one address at G6. If the store page gets a different address, redirect `/alignment-diagnostic` to it. |
| **L5** | G5 Package | "The report's last section already carries the only offer" (`06-package-price.md:50`). The price Signal counts buyers who "ask for the Beta" (`06:128`). The block calls the diagnostic "the first step" (`07:154`). | Sol's wording table warns against "first step" and "entry" phrasing on a Lab page, because it hints at a priced path (`package/price-read.md:54–59`). | Guardrail 7. 2026-11-11: price confirmed, CAD $790. | At G5, Sol re-reads the package against that table and counts conversations for either offer. Price unchanged. |
| **L6** | G7 Clearance | The diagnostic is a Lab and briefly holds summaries. | Not an RP file, but found on the way: the site privacy policy says "Labs run on your own device or accounts. They don't send information back to us." (`site/privacy-policy.md:66`). | 2026-11-10 "Labs … send no data back" came before 2026-11-10 "The Rotor Alignment Diagnostic is a Lab". | At G7, add "except the Rotor Alignment Diagnostic; see its own notice". Vera checks. |
| **L7** | G6 Story | Works on Claude, ChatGPT, Copilot and Gemini. Not offered to Quebec companies or leaders (`07:104`; decision 2026-11-09). | The Distillation's table lists three tools, without Gemini (`website-changes.md:156`), though its loading guide covers Gemini. The ladder offers the diagnostic to every "not sure" buyer, with no Quebec note. | 2026-11-09: four platforms; Quebec excluded "for now". | At G6, make the tool lists match, and have Brandon send Quebec companies to the fit check instead. |

**G4 Look:** no conflict found. Rotor Product has no visual rules that touch the report PDF.

### 3c. Wording only (9)

| # | Where | What disagrees | Decision that governs | Recommended resolution |
|---|---|---|---|---|
| **W1** | `brief.md:33`, `02-product-spec.md:46, 72`, `04:19`, `08-test-plan.md:19, 98`, `lab.yaml:19`, `labs/sparks.md` | They describe the report as ending in "one offer: the Beta", or "useful without the Beta". | 2026-11-11 "sorts buyers between them". | After M1, add a dated note to each. Do not rewrite gate-passed files. |
| **W2** | `canon/ontology.md:46` | Wave 0 is defined as the diagnostic's "results". It should say "report". Also, "Rotor Distillation", "Rotor Sheet" and "fit check" are used everywhere but are not in the ontology. | 2026-11-11: "Wave 0" stays. The ontology says not to coin terms silently. | Ines proposes the three terms and the one-word fix at the next gate. |
| **W3** | `rotor/product/package/price-read.md:5, 34, 44, 64`; `labs/sparks.md` (five-tests row); `build/agents/a6-five-tests-checker.md:13` | Stale notes: "he recalls 699", "CAD 199", "waiting room", "the diagnostic's own free layer", and "Brandon to confirm the five tests". | 2026-11-11: price confirmed CAD $790; five tests may be published; "waiting room" retired. 2026-11-10: no free layer. | Mark each as superseded. A chore, not a decision. |
| **W4** | `playbook-changes.md:182` | "follow up on every report, and use it to sort them". Brandon never sees a report unless the CEO sends it. The only follow-up is the one automatic check-in email. | 2026-11-09: "no person reads the blocks"; one check-in email at 14 days. | Reword: "sort them when a CEO brings the report to a conversation". |
| **W5** | `build/interviews/wave-ceo.md:30, 33`; `wave-fit.md:19, 23` | The CEO file's "question 9" is a different question from wave 1's question 9. The fit file adds a sentence to question 3 and writes "fit check" in the Wave field, which the format calls a number. | 2026-11-09 "reuse wave 1 questions unchanged" applies to the diagnostic only. No decision covers these files. | Rename the CEO file's last question so "question 9" always means one thing. Leave the rest. See the comparability table below. |
| **W6** | `logs/decisions.md` | The no-hosting rule (2026-11-10) and the drop-box (2026-11-09) sit apart. The playbook list already calls the drop-box an approved exception (`playbook-changes.md:116`). | 2026-11-09 Option C, then 2026-11-10 "unless Brandon approves it at a gate", then the build plan approved 2026-11-10. | One confirming line in the decisions log. |
| **W7** | `brief.md:47`, `03-interviewer.md:43`, `beta-playbook.md:566` | Kept reports are "for comparison with Beta data". RP now says "program data" (`playbook-changes.md:135`). | 2026-11-09 (kept for comparison). | Use "Beta and Distillation data". |
| **W8** | `canon/guardrails.md`, guardrail 1 | Guardrail 1 reads as absolute. Your later decision keeps existing references on the site and in the playbook. | 2026-11-11: existing references stay; new material adds none. | No change to the diagnostic: it has none and adds none. Vera notes at G7 that the Lab's own page stays clean. |
| **W9** | `lab.yaml:40–42` | The card lists two links to the diagnostic. RP5 added more ways in: the Home ladder, the How It Works intro and a new FAQ answer (`website-changes.md:77, 107, 272`). | 2026-11-11: RP5 change lists approved. | Update the card at G6. |

### Interview questions: how comparable is the data?

| File | Used in | Questions 1–2 | Question 3 | Questions 4–8 | Question 9 | Question 10 |
|---|---|---|---|---|---|---|
| Diagnostic interviewer | Diagnostic | word for word | word for word | word for word | word for word | dropped (decision 2026-11-10) |
| `wave-1-short.md` | Beta, after a diagnostic | word for word | word for word | word for word | word for word | asked, plus one new check question first |
| `wave-ceo.md` | Distillation | word for word | word for word | word for word | **a different question** | not asked |
| `wave-fit.md` | Distillation fit check | word for word | **one sentence added** | not asked | not asked | not asked |

So the main effort and the trade-offs compare cleanly across all four. That is the part the sorting needs. The summary block is the same 15 fields everywhere, and the diagnostic's tests fail if the Interviewer Pack's block ever changes (`build/tests/test_blocks.py:28`).

---

## 4. Exact changes for the must-resolve items

Proposed only. None has been made.

### M1 · The report's closing offer

**New section 9.** Paragraphs one and two are today's approved text, unchanged. Paragraph three is Fenn's sentence, word for word, from `website-changes.md:345`.

```
## 9. Next step
These are your team's questions to settle. Many teams do that on their own, and this report is yours to use however you like.

If you'd like help, settling these questions is what the Rotor Beta does. Over one quarter, we work with your leadership team to agree the main effort, the trade-offs and the warning signs, in your own words, and put them where your people make decisions.

If there's little to settle, the Rotor Distillation takes your strategy into your AI tools.

Start a conversation: {start_conversation_link}
```

Why this sorts without advising: the text is fixed and the same for every company. The agent writes none of it and never says which case a team is in. It names no price and does not compare the two on how much of Brandon each includes (decision 2026-11-11).

**Files, diagnostic side:**
- `04-synthesis-agent.md`, section 4 template: add the one sentence. Add a dated note under section 7.
- `05-sample-report.md`, section 3, "9. Next step": add the same sentence. The bench tests build their sample from this file.
- `build/diagnostic/prompts/report_template.md`: same sentence. A test fails until it matches file 04.
- `build/tests/test_synthesis_checks.py`: add one test that the Distillation sentence is present. The existing section 9 test still works, because the Beta sentence is unchanged.
- `08-test-plan.md`, Check D: rename "The Beta handoff" to "The handoff".
- No change to `checks.py`. It compares against the template.

**Files, Rotor Product side:** none. `playbook-changes.md:133` says the diagnostic "still names only the Beta"; that line becomes out of date once this is done.

### M2 · Let the report show agreement

**Files, diagnostic side:**
- `04-synthesis-agent.md`, section 4 template: change "2–5 splits" to "Up to 5 splits", "2–5 trade-offs" to "Up to 5 trade-offs", "2–4 effects" to "Up to 4 effects", "3–7 questions" to "Up to 7 questions". Add to each: "If there are none, say so in one sentence."
- `04-synthesis-agent.md`, section 3, under "What these differences may lead to": change "Write 2 to 4 effects" to "Write up to 4 effects". Add one rule under "How to find agreement and difference": "Never stretch a small difference to fill a section."
- `build/diagnostic/prompts/report_template.md` and `synthesis_instructions.md`: the same edits, so the copies match.
- `08-test-plan.md`, Stage 1: add an invented, broadly aligned company as a new trap set. Pass if the report shows the shared main effort, invents no split, and still fills every heading.
- `08-test-plan.md`, Stage 1: add one reading test. Run Brandon's fit-check list (`rotor/product/build/checklists/review-checklists.md:7–13`) on the Larchmere report and on the aligned one. Expect "Beta" for Larchmere and "Distillation is possible" for the aligned one. Nobody has yet tried a report as a fit check: simulation run 1 tested the short fit interview only (`build/simulation/run-1/results.md`).

An aligned report may run under 1,200 words. The app treats length as a warning, not a hold, so nothing else changes.

**Files, Rotor Product side:** none.

### M3 · Wave 0 is the report, not each leader's answers

**Files, Rotor Product side:**
- `build/interviews/wave-1-short.md:7`: change to "Wave 0 is the company's diagnostic report. It is about the team. It cannot tell you what one leader said."
- `build/interviews/wave-1-short.md:11–15`: fill "Already answered" for a leader only when that leader has chosen to forward their own saved diagnostic summary. Everyone else gets the standard wave 1 file. (Line 15 already allows this.)
- `rp2-spec.md:229`: the "before" baseline is the report's count of different main efforts, not a per-leader score.
- `canon/ontology.md:46`: "results" becomes "report" (see W2).

**Files, diagnostic side:** none. The drop-box keeps deleting. Each leader's summary already stays in their own company AI chat, so there is nothing to build.

### M4 · Which copy of the report, and under what rules

**Files, Rotor Product side:**
- `story/playbook-changes.md:137`: replace "With the client's consent the report is kept, and becomes wave 0 if the company goes on." with "With the client's consent the report is kept for research. If the company goes on, the CEO sends you their own copy; that copy is the fit check and wave 0."
- `rp2-spec.md:237`: "(already kept with consent)" becomes "(sent by the CEO)".
- `package/offer.md:96`, `story/website-changes.md:205` and `build/client-pack/governance-one-pager.md:21`: after the two things Brandon receives, add "and your alignment diagnostic report, if you choose to send it". The close-out lines already say "every copy I hold".

**Files, diagnostic side:**
- `09-privacy-and-terms.md:71` (at G7): the Franklin Kinetics cell gains "or the CEO chooses to send it to us".
- No change to checkout, the consent box, the leader note or the app. The app gets no way for Brandon to look up a kept report. That keeps the Lab at zero Brandon time (guardrail on Brandon's time).

Brandon reads the report himself. It does not go through the A2 helper, which accepts summary blocks only (`build/agents/a2-synthesizer.md`).

### M5 · The Start a conversation address

**Files, diagnostic side:**
- `build/diagnostic/config.py:14`: set the default to the site's `/contact` address, once Brandon confirms it. Unclear from the repo whether the live site uses `www`.
- `build/README.md`, "Brandon decides", item 4: tick it off.

---

## 5. Decisions for Brandon

Recommended answer first.

1. **Does the report name both ways forward?** **Yes.** Keep the Beta paragraph, add Fenn's one Distillation sentence, keep one link (M1). "One offer" becomes "one next step: a conversation". Fallback if you'd rather name neither: Sol's neutral line, "help settling what the report shows" (`price-read.md:54`).
2. **May the report show a team that agrees, with few or no splits?** **Yes.** Drop the minimum counts and add an aligned test company (M2). This edits prompt text you passed on 2026-11-10.
3. **Is wave 0 the team's report only, with a leader's own summary used only if that leader forwards it?** **Yes** (M3). The drop-box keeps deleting everything.
4. **Is the fit check always the copy the CEO sends you, never the kept research copy?** **Yes** (M4). It adds the report to the Distillation's data list as a third thing you receive.
5. **Is Start a conversation at `franklinkinetics.com/contact`?** **Yes, if the site map is right** (M5). Only you can confirm.
6. **At G6, does "Not ready for the Beta? Start here." become "Not sure which one fits? Start here."?** **Yes, at G6** (L1). It can wait. It is here because the old headline is written into two of your decisions.
7. **One line for the record: is the drop-box the approved exception to the no-hosting rule?** **Yes** (W6). It passed its own gate on 2026-11-09 and the build plan passed on 2026-11-10.

Not asked, because you already decided: the price (CAD $790, 2026-11-11), the sealed drop-box, question 10 dropped, no verdict from AI, the Beta unchanged, and existing military references staying.

---

## 6. Already in agreement

- **Price.** CAD $790 flat, no credit toward consulting, no launch price. Both efforts. Sol's CAD 199 read is withdrawn.
- **No price near consulting.** The $790 sits only on the diagnostic's own page. The ladder and the How It Works block show no price. Both offers stay unpriced.
- **The Labs line.** The diagnostic needs none of Brandon's time. When he reads a report as a fit check, that time belongs to the conversation, not the Lab.
- **No verdict.** The diagnostic never recommends a main effort and has no score. The fit call is Brandon's and "is never automated" (`rp2b-spec.md:35`).
- **Questions.** Wave 1 questions 1–9 word for word. Question 10 is dropped in the diagnostic and asked again in the Beta's short wave.
- **Summary block.** One format everywhere. The Interviewer Pack stays unchanged, and a diagnostic test guards it.
- **The drop-box.** Rotor Product's playbook list describes it correctly and names it as an approved exception.
- **The site FAQ.** The diagnostic's approved sentence is kept word for word in the RP5 change (`website-changes.md:254`).
- **Quotes.** Never attributed in the diagnostic. Unattributed "unless that leader agrees" in the Distillation and the Beta. Different on purpose. A diagnostic report's quotes stay unattributed for good, since the names are gone.
- **Five-tests checker.** A separate free Lab that runs in the buyer's own AI. It tests one strategy page; the diagnostic compares leaders. No overlap found.
- **Words.** "Beta" throughout. "Main effort" in everything a client reads. No military reference in any diagnostic file or new Rotor Product copy. No Rotor Core content in either.
- **Who it's for.** Owner-led companies of 20 to 200 people, in both.
- **The check-in email.** It offers a conversation and names neither offer (`build/diagnostic/emails.py`, check-in text). It already fits.

---

## 7. Small open points (not conflicts)

- **How old may a report be and still count as the fit check?** No file says. The Distillation's CEO interview asks the main-effort question again, which covers drift. Left to Brandon's judgment.
- **Held reports.** The build README asks how long a held report's summaries may wait (`build/README.md`, "Brandon decides", item 2). The no-hosting rule makes a limit more worth having. Still Brandon's call at G3.
- **GST/HST.** Still open from 2026-11-10. Check with the accountant before the page goes live.
- **Guardrail numbering.** `canon/guardrails.md` has two rules numbered 8 (already in the friction log). This memo names them in words to avoid confusion.

---

## Outcome · 2026-11-11

**Agreed.** Brandon accepted every recommended answer. The five must-resolve fixes are applied before building resumes.
