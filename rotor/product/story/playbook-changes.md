# Rotor Product · RP5 Story · Beta Playbook change list

> **2026-11-11, Brandon:** existing military references stay as they are. Nothing below touches them, and no new text adds any.

Fenn, 2026-11-11. **Redone for the reshaped Rotor Distillation** (the AI side), replacing the list written for the old intake design. For Brandon at Rotor Product Gate 5. This is a **paste list**. Section names follow `rotor/beta-playbook.md`.

**What this does:** adds a short section on the ladder and the Distillation that points to `rotor/product/` instead of copying it; removes the founding-Beta discount (decided 2026-11-11); brings the data rule, the diagnostic, the override log and the to-dos in line with decisions.
**What it doesn't do:** change how the Rotor Beta is delivered. Its name, terms, form and two-working-day reply standard stay. Whether the Beta uses the AI helpers is still your call at RP6.
**The playbook is private.** Internal rules (the Beta cap, Brandon's hours) can appear here. Lines marked *(said aloud)* get spoken to clients, so they follow the client-copy rules: no comparison of the two offers on price or on how much of Brandon, no count of Betas, no scarcity.

---

## Decide first

| # | Decision | Recommendation |
|---|---|---|
| D1 | Does the Beta switch to the AI helpers (A2–A12)? | Not yet. Keep the Beta as is until the override log shows which helpers hold up across the first Distillations. Decide at RP6. |
| D2 | The starting range in "Pricing and the offer" (CAD $6,000 to $10,000) is untested, and was set as a *founding* price "rising to full price once you have two case studies". | P6 removes the founding-discount wording, as decided. The range itself is internal and Beta pricing is yours, so it stays, with "founding" and "rising to full price" taken out. Say if you'd rather the range go too. It never reaches client copy either way. |

---

## P1 · New section: "The ladder and the Rotor Distillation"

- **Location:** new section between **Overview** and **Selling the beta**.
- **Current text:** none.
- **New text:**

> ## The ladder and the Rotor Distillation
>
> Rotor now comes in rungs, sorted by one question the client can answer: **do the leaders already agree on where the company is going?**
>
> | Rung | What it is | Sold as |
> |---|---|---|
> | **Rotor Alignment Diagnostic** | Self-serve AI interview for each leader, and a report on where they agree and differ. Needs none of my time. | A Lab, priced on its own page in the Labs store |
> | **Five-tests checker** | Free goodwill tool, going through the Lab lifecycle | A Lab, free |
> | **The Rotor Distillation** | The AI side. Starts from a strategy the leaders already agree on, distills it into a Rotor Sheet, loads it into one team's AI tools, tests it, and runs six weeks of live use. About 12 weeks. | Consulting, unpriced |
> | **The Rotor Beta** | This playbook, unchanged: alignment, people and AI, for leadership teams that don't yet agree. | Consulting, unpriced |
>
> **How buyers are sorted.** Aligned → the Distillation. Split → the Beta. Not sure → the diagnostic first. A company that hasn't taken the diagnostic does a **fit check** before signing: the CEO and one or two leaders each do one 20-minute AI interview, and you read the summaries. If their main efforts clearly differ, recommend the Beta or the diagnostic. That call is yours and is never automated.
>
> **How the Distillation runs, in one breath.** Rolling starts, no shared days. The CEO runs the strategy documents through the document distiller (A13) in the company's own AI and emails you the digest. Three calls, all with the CEO, at 4 pm or in the evening: kickoff (45 min), sign-off (60 min), review (60 min). You judge and rewrite the Rotor Sheet; you never choose the main effort, only sharpen the one they chose, and the CEO signs it off. Leaders react in writing. IT loads the sheet; the team lead writes ten dilemmas for the red-team; six weeks live with an update every two weeks and one pulse. **Reply standard: three working days, urgent flags first** (the Beta's stays two).
>
> **What it leaves out, on purpose:** leader-by-leader interview rounds, the Mirror, the one-page visual and CEO video, the comparison team and the noise audit. Those are the Beta's.
>
> **Data.** Interviews and the reading of strategy documents run in the client's own AI. You receive only the short summary blocks and the structured digest, by email, never the documents or full conversations. Drafting runs in your own AI account, one private project per company, training switched off in settings. Delete it all at close-out and send written confirmation; tell the client the vendor's retention period, [X days].
>
> **Internal planning rules (never said to a client):**
> - About 12 h of your time per Distillation, 0 days off (estimates; the first clients replace them).
> - At most two companies in weeks 1–4 at the same time. Offer evenings before 4 pm.
> - Up to two Rotor Beta clients a year. Client copy never states a number.
>
> **How to describe it to a client** *(said aloud)*: use "Which one is for me?" (`package/offer.md` §2). Sort by whether the leaders agree, never by price or by how much of you they get. For the first companies, use the founding wording (§4): "You'd be among the first." No discount, no "founding rate".
>
> **Where the detail lives** (`rotor/product/` in the Labs-Agents repo):
> - `rp2b-spec.md`: the Distillation week by week, your minutes per step, your year, risks.
> - `package/offer.md`: the ladder, the offer sheet, the founding wording.
> - `build/agents/README.md`: which AI helpers (A1–A13) the Distillation and the Beta use, and where each runs.
> - `build/client-pack/`: welcome email, kickoff and sign-off agendas, governance one-pager, disclosure note, IT checklist, loading guide.
> - `build/interviews/`: the fit, CEO and short wave files. `build/voice/`: update style, reply guide, scripts.
> - `build/templates/`: override log, client tracker. `build/checklists/`: review checklists, dry-run plan.

- **Why:** the playbook still describes one offer. This puts the whole ladder on one screen and points to the canon rather than copying it.

---

## Overview

### P2 · Overview › first paragraph › last sentence
- **Current:** "It is sold through Franklin Kinetics as a fixed-fee founding beta."
- **New:** "It is sold through Franklin Kinetics at a fixed fee. For leadership teams that already agree, the Rotor Distillation is the other way in (see The ladder and the Rotor Distillation)."
- **Why:** "founding beta" carried the discount that P6 removes. The Beta keeps its fixed fee.

---

## Selling

### P3 · Selling the beta › Pitch A › last sentence *(said aloud)*
- **Current:** "The founding beta is a short build followed by a full quarter with one team, at a fixed fee."
- **New:** "If your leaders already agree on the strategy, the Rotor Distillation puts it into your AI tools and tests it with one team. If they don't, the Rotor Beta settles the hard calls first: a short build, then a full quarter with one team."
- **Why:** Pitch A ("your AI knows nothing about your strategy") is the Distillation's problem. No fee words said aloud next to an offer whose fee isn't on the table yet.

### P4 · Selling the beta › after the pitch comparison table *(said aloud)*
- **Current:** "Either way, the offer is the same beta: a short build, then a full quarter."
- **New:** "Either way, close on the rung that fits, sorted by one question: do the leaders already agree? Yes: the Rotor Distillation, after a fit check. Clearly not: the Rotor Beta. Not sure: the alignment diagnostic first. Never sort by price or by how much of you they get. Discovery question 1 is the sorting question; listen hard to the answer."
- **Why:** the reshape's whole logic in one paragraph.

### P5 · Selling the beta › Objections and answers *(said aloud)*
Five rows change; the rest stay.

| They say | Current answer | New answer |
|---|---|---|
| "We already have a strategy." | "Good, the beta starts from it. The question is whether it reaches daily decisions. The leader interviews will show you." | "Good. If your leaders stand behind it, the Rotor Distillation starts from it and puts it into your AI tools. If you're not sure they do, the leader interviews in the Beta, or the diagnostic, will show you." |
| "Is our strategy safe in an AI tool?" | "It stays in tools your company already approved, under your control. Nothing confidential goes in, and we agree what that means up front." | "In the Beta, it stays in tools your company already approved, under your control. In the Distillation, interviews and the reading of your documents stay in your own AI; I receive only short summaries and a structured digest by email, never your documents or the full conversations. I draft in my own AI account with training switched off, and delete it all at the end with written confirmation; the vendor may keep deleted content for [X days]. Either way, nothing confidential goes in, and we agree what that means up front." |
| "Can't we do this ourselves?" | "You could. Most teams find the hard part is the honest convergence between leaders, which is easier with an outsider in the room." | "You could. Where leaders don't yet agree, the hard part is the honest convergence between them, which is easier with an outsider in the room. Where they do agree, the hard part is turning the plan into something an AI can apply, and testing it before people rely on it." |
| "We don't have time for another round of meetings." | "Good, because there are three. Leaders do their interviews when it suits them, by voice or text, and the CEO gets a short weekly update instead of a status meeting." | "Good, because there are three. In the Beta, leaders do their interviews when it suits them and the CEO gets a short weekly update. In the Distillation, all three calls are with the CEO, and the other leaders send a short written reaction." |
| "An AI is interviewing our executives?" | "…I read every transcript and make every call…" | "…I make every call. In the Beta I read every transcript; in the Distillation the conversation stays in your AI and I read only its summary…" (rest unchanged) |

- **Why:** each old answer was true only of the Beta. Data wording matches the offer sheet ("switched off", never "excluded by contract").

### P6 · Selling the beta › Pricing and the offer *(decided 2026-11-11: remove the founding-Beta discount)*
- **Current (opening line):** "Offer the first two or three betas as **founding betas** at a reduced fixed fee, in exchange for a testimonial and permission to write up the results anonymously."
- **New:** "The Beta is priced at a fixed fee, set in the proposal. There is no founding discount and no fee traded for a testimonial. For the first clients, ask for honest feedback instead; any testimonial or write-up comes later, only with separate written permission, and saying no changes nothing (the same terms as the Distillation's founding wording, `package/offer.md` §4)."
- **Current (second bullet):** "Show the full price on the proposal, with the founding discount as a separate, time-limited line. This keeps clients from anchoring on the discounted number."
- **New:** delete the bullet.
- **Current (fourth bullet):** "A suggested starting point to test against your local market: CAD $6,000 to $10,000 for a founding beta covering the build and the live quarter (or price the build alone and treat the live quarter as the first retainer quarter), rising to full price once you have two case studies. This range is untested; validate it in your first five conversations."
- **New:** "A suggested starting point to test against your local market: CAD $6,000 to $10,000 for a beta covering the build and the live quarter (or price the build alone and treat the live quarter as the first retainer quarter). This range is untested; validate it in your first five conversations. Internal only: never on the website, in a Lab, or said before a proposal." *(see D2)*
- **Add (new last bullet):** "The Rotor Distillation is also unpriced in every client-facing place. Its fee is set in the written proposal, after the fit check."
- **Why:** a reduced fee is an implied price and a discount; "time-limited" is urgency (guardrail 8). Brandon decided to remove it.

---

## Data

### P7 · Organizational AI integration › Three levels › after the table
- **Current:** "Do not host client strategy data yourself. If a client wants level 2 or 3 and has no IT team, bring in a developer partner under a separate agreement."
- **New:** "Do not host client strategy data yourself, with two approved exceptions: the Rotor Distillation's summary blocks, document digest and drafting project (see Governance), and the alignment diagnostic's sealed drop-box, which briefly holds summaries with names removed. If a client wants level 2 or 3 and has no IT team, bring in a developer partner under a separate agreement."
- **Why:** decisions of 2026-11-10 and 2026-11-11.

### P8 · Organizational AI integration › Governance › "Interview data" bullet
- **Current:** "Interview data: full interview transcripts are read only by you, stored in the client's own AI platform, and deleted from your notes at the end of the engagement. What goes into the divergence summary is quoted without names unless the leader agrees."
- **New:**
  > - **Interview data (Beta):** full interview transcripts are read only by you, stored in the client's own AI platform, and deleted from your notes at the end of the engagement. What goes into the divergence summary is quoted without names unless the leader agrees.
  > - **Interview and document data (Distillation):** interviews and the reading of strategy documents (A13) run in the client's own AI. You receive by email only each summary block and the A13 digest; never the documents, never a full transcript. Drafting runs in your own AI account (a one-person plan), one private project per company, named by code, training **switched off in settings**; confirm the setting in writing before the first block arrives. At close-out, delete the project, the block emails, the digest and every copy, and send written confirmation. Tell the client the vendor's retention for deleted content: [X days, confirmed before kickoff]. Say "switched off", never "excluded by contract". Quotes are never attributed unless the leader agrees; no AI helper may attribute one. Full wording: `build/client-pack/governance-one-pager.md`.
- **Why:** the Beta's line stays as it is; the Distillation gets its own.

### P9 · Beta structure › Rules for the async core › "Disclose before the first interview"
- **Current:** "**Disclose before the first interview.** Tell leaders what is attributed and what is anonymized, that only you read full transcripts, and which vendor's AI holds them."
- **New:** "**Disclose before the first interview.** Tell leaders what is attributed and what is anonymized, who reads what (in the Beta, only you read full transcripts; in the Distillation, you receive only the summary), and which vendor's AI holds them. The Distillation has its own disclosure note (`build/client-pack/disclosure-note.md`)."
- **Why:** decision 2026-11-11: the Distillation gets its own disclosure note.

### P10 · Learning loop › The alignment diagnostic
- **Current (section intro, last sentence):** "It ends with one offer: help settling them, which is the Beta."
- **New:** "It now sorts buyers: where the leaders broadly agree, the next step is the Rotor Distillation, and the report serves as its fit check; where they're split, the Rotor Beta. The diagnostic's approved copy still names only the Beta; changing that goes through the diagnostic's own gate."
- **Current (what it collects):** "**What it collects:** the same wave 1 questions as the Interviewer Pack, so diagnostic data and beta data can be compared."
- **New:** "**What it collects:** wave 1 questions 1–9, word for word, so diagnostic data and program data can be compared."
- **Current (data rule):** "**Data rule:** interviews run in the client's own AI. Decide before building how summaries are combined: by the client in their own AI (no hosting, but the CEO sees individual answers) or sent to you for the agent to combine and delete (more candour, but you hold data briefly). Either way, no report for fewer than three leaders, and quotes are unattributed."
- **New:** "**Data rule (decided):** interviews run in the client's own AI. Each leader's summary goes to a sealed drop-box; names and roles are removed on arrival, an agent writes the report, no person reads the summaries, and they are deleted once the report is delivered. No report for fewer than three leaders; quotes are never attributed. With the client's consent the report is kept for research. If the company goes on, the CEO sends you their own copy; that copy is the fit check and wave 0." *(Amended 2026-11-11 after the reconciliation with the diagnostic.)*
- **Current (what it must not do, last sentence):** "It shows the gaps; the Beta closes them."
- **New:** "It shows the gaps. Where there are real gaps, the Beta closes them; where there are few, the Distillation carries the strategy into the AI."
- **Why:** the diagnostic is built and gated, and now sorts buyers both ways.

---

## Calendar and delivery

### P11 · Beta structure › Rules for the async core › two bullets
- **Current:** "**Sell responsiveness, not availability.** Promise a reply standard, such as every memo answered within two working days, instead of open meeting access."
- **New:** "**Sell responsiveness, not availability.** Promise a reply standard instead of open meeting access: two working days in the Beta, three in the Distillation (urgent flags first)."
- **Current:** "**Scale in waves.** Start two or three clients together so prompt packs, review batches and the weekly rhythm are shared. Set the number per wave from your tracked hours, and protect synthesis time first."
- **New:** "**Rolling starts, capped.** Distillations start when the client is ready, with no shared days. At most two companies in weeks 1–4 at the same time, because the sheet work in weeks 2–3 is the peak. Offer evenings for CEO calls before 4 pm. Keep the Beta's own rule: never two Mirrors in the same week."
- **Why:** rp2b-spec §2 and §7. Waves and intakes are retired.

### P12 · Beta structure › after "Rules for the async core"
- **Current:** "The rotor-async-beta skill runs each step: engagement plan, prompt packs, interviewer brief, synthesis, flight logs, session prep and live-run pulses."
- **New:** "**In the Beta,** the rotor-async-beta skill runs each step: engagement plan, prompt packs, interviewer brief, synthesis, flight logs, session prep and live-run pulses. Whether the Beta moves to the AI helpers is your decision (RP6).
**In the Distillation,** AI helpers draft and you decide: A1, A2, A5, A6, A8, A9, A11, A12 and A13. A13 (document distiller), A1, A8 and the pulse questions run in the client's AI; the rest run in your own account's company project. Not automated, by design: the fit-check decision, your judgment on the Rotor Sheet, the three CEO calls, and your replies (AI may draft; you send in your own words). Which helper does what: `rotor/product/build/agents/README.md`."
- **Why:** rp2b-spec §4. The Beta's delivery is unchanged unless you decide otherwise.

### P13 · Learning loop › The override log › first paragraph and bullets
- **Current:** "Keep it from the first beta. Every time you change something the AI drafted, log one line: what the AI said, what you changed, why, and which step it was (interview follow-up, synthesis theme, divergence summary, schwerpunkt candidate, guardrail wording, flight log, pulse question)."
- **New:** "Keep it from the first Distillation or Beta. Every time you change something the AI drafted, log one line, **step code and categories only, never client content** (no paraphrase of a draft, no company names, no quotes): date · company code (e.g. CO-1) · step S1–S12 · change (none, cut, added, reworded, reordered, replaced) · why (wrong, weak, tone, missing context, judgment call) · minutes · optional method note about the helper's instructions, never about the client.
Steps: S1 interviewer summary blocks (A1) · S2 syntheses (A2) · S3 wave files (A3) · S4 divergence summary and language harvest (A4) · S5 Rotor Sheet drafts in the Distillation, schwerpunkt candidates in the Beta (A5) · S6 five-tests mark-up (A6) · S7 video script (A7) · S8 red-team annotations (A8) · S9 updates (A9) · S10 pulse syntheses (A11) · S11 results pack (A12) · S12 document extraction (A13). S3, S4 and S7 are Beta-only. Count unchanged approvals too, so you get a rate. Template: `rotor/product/build/templates/override-log.md`."
- **Add after the existing bullets:**
  - "A step becomes a candidate to hand further to AI at 15+ observations across 3+ companies, an override rate under 15%, and no "wrong" in its last 10. Handing over is decided at a track gate, never silently."
  - "**S5 is never handed over**, whatever the numbers say. It is logged for learning only."
- **Why:** the old line ("what the AI said, what you changed") would put client content in your library. The ontology defines the log as step and reason only; S12 covers the new document distiller.

### P14 · Next steps › to-dos now decided or done
- **Current:** "Decide your capacity rule: start clients in waves, never two Mirrors in the same week, a written reply standard, and a named backup facilitator for live sessions. Set the clients per wave from hours tracked on the first beta."
- **New:** "Capacity rule (decided): Distillations on rolling starts, at most two in weeks 1–4 at once; Beta Mirrors never in the same week; reply standards of two (Beta) and three (Distillation) working days; up to two Betas a year (internal only). Still open: a named backup facilitator for live sessions."
- **Current:** "Run the AI interviews and five tests on a friend's business as a dry run, and time your own review and synthesis hours. Keep all DND specifics out of anything you show clients."
- **New:** "Dry run in two stages (decided 2026-11-11): a simulated company with four AI-played leaders, then the first one or two real companies, told they're the first. Time your own minutes on every step. The simulation is fictional and is never shown or used as a result. Keep all DND specifics out of anything you show clients."
- **Current:** "Write a one-page offer sheet and the employee transparency note."
- **New:** "- [x] Offer sheet (`rotor/product/package/offer.md` §3). - [ ] Employee transparency note."
- **Current:** "Set up the override log template before the first beta starts."
- **New:** "Copy `rotor/product/build/templates/override-log.md` into your private library before the first Distillation or Beta."
- **Current:** "Build the alignment diagnostic with the Labs agent crew, starting with the data-flow decision."
- **New:** tick it: "- [x] Alignment diagnostic built with the Labs crew; in its Lab gates."
- **Current:** "Offer one or two founding betas."
- **New:** "Offer the Rotor Distillation where the leaders agree (fit check first), and the Rotor Beta where they're split. For the first companies, use the founding wording, with no discount."
- **Current:** "Offer the diagnostic to warm contacts who aren't ready for a beta; follow up on every report."
- **New:** "Offer the diagnostic to warm contacts who aren't sure whether their leaders agree; follow up on every report, and use it to sort them."
- **Why:** these are decided or done. The DND sentence in the dry-run line is an existing reference and stays.
