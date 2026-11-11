# Rotor Product · RP5 Story · Beta Playbook change list

Fenn, 2026-11-11. For Brandon at Rotor Product Gate 5. The master is the Claude Doc "Rotor Beta Playbook"; this is a **paste list**. Section names follow `rotor/beta-playbook.md`.

**What this does:** adds the product ladder and the Rotor Distillation, brings the override log, data rule, calendar and AI helpers in line with the approved spec, and lists every military reference for your decision.
**What it doesn't do:** change how the Rotor Beta is delivered. Whether the Beta uses the new AI helpers is your call (spec §9; see P9). The Beta keeps its name, terms and form.
**The playbook is private.** Internal rules (such as the Beta cap) can appear here; they never go into client-facing copy.

---

## Decide first

| # | Decision | Recommendation |
|---|---|---|
| D1 | Does the Beta switch to the AI helpers (A2–A12)? | Not yet. Keep the Beta as is until the first intake's override log shows which helpers hold up. Decide at RP6. |
| D2 | "Pricing and the offer" offers founding betas "at a reduced fixed fee, in exchange for a testimonial", with "a separate, time-limited line". | Flag only, not rewritten. It conflicts with the founding-intake wording you approved (no discount; testimonials only later, by separate permission; "saying no changes nothing"), and "time-limited" is the kind of urgency Vera checks for (guardrail 8). Worth aligning before any Beta proposal goes out. |
| D3 | Military references: 13 places in the playbook (list at the end). | Your call, item by item. Conflict-of-interest steps stay as private to-dos. |

---

## P1 · New section: "The product ladder and the Rotor Distillation"

- **Location:** new section between **Overview** and **Selling the beta**.
- **Current text:** none.
- **New text:**

> ## The product ladder and the Rotor Distillation
>
> Rotor now comes in three rungs. One test sorts them: **does it need my time?** No means a Lab (self-serve, priced, in the Labs store). Yes means consulting (unpriced, sold through Start a conversation).
>
> | Rung | What it is | My time | Price |
> |---|---|---|---|
> | **Rotor Alignment Diagnostic** | Self-serve AI interview for each leader; a report on where they agree and differ. A Lab. Also the **waiting room** for the next start date, and **wave 0** for clients who go on. | None | Priced on its own page, in the Labs store |
> | **The Rotor Distillation** | The full build on set start dates. Each leader interviewed by AI, the hard calls settled at the Mirror, one beta team for a quarter, measured against a comparison team. About 21 weeks. | ~21.5 h per company (estimate), mostly evenings; the Mirror on a planned day off | Unpriced |
> | **The Rotor Beta** | This playbook, unchanged: the same journey with me in every session, on a timetable built around the client. | As this playbook | Unpriced |
>
> Also on the ladder: the **five-tests checker**, a free goodwill tool, going through the Lab lifecycle.
>
> **How the Distillation differs from the Beta**
> - **Intakes.** Up to three companies start within the same three weeks, one week apart, and share one **Mirror day**. They never meet and never learn each other's names. To a client it is simply "the next start date". No direct competitors in the same intake.
> - **Three live moments:** a 45-minute kickoff (4 pm, CEO), the 2-hour Mirror (remote by default), a 60-minute review (4 pm, CEO).
> - **Reply standard:** three working days, urgent flags first (the Beta's is two).
> - **Drafting by AI helpers A2–A12** in my own AI account (P8, P9). Choosing the schwerpunkt candidates is never automated; I choose, the leadership team signs off.
> - **Beta team of at least five people,** set at kickoff.
>
> **Internal rule, never said to a client:** at most one Beta client a year. Client copy never states how many.
>
> **How to describe the rungs to a client:** use "Which one is for me?" (`rotor/product/package/offer.md` §2). For the first two companies, use the founding-intake wording (§4): "You'd be on the first run." No discount, no "founding rate".
>
> **Where the detail lives** (`rotor/product/` in the Labs-Agents repo):
> - `rp2-spec.md`: client journey week by week, your minutes per step, calendar rules, risks.
> - `package/offer.md`: name, ladder, offer sheet, founding wording.
> - `build/agents/`: the A2–A12 helper packs. `build/client-pack/`: welcome email, IT checklist, governance one-pager, kickoff agenda. `build/voice/`: video scripts, update style, reply guide. `build/templates/`: override log, intake calendar. `build/checklists/`: review checklists, dry-run plan.

- **Why:** the playbook still describes one offer. This gives the whole ladder on one screen and points to the canon instead of copying it.

---

## Selling

### P2 · Selling the beta › Pitch A › last sentence
- **Current:** "The founding beta is a short build followed by a full quarter with one team, at a fixed fee."
- **New:** "The Rotor Distillation is a short build followed by a full quarter with one team, starting on set dates. If you want me in the room for every session, that's the Rotor Beta."
- **Why:** leads with the main offer; no fee language said aloud before a proposal. (The Bungay sentence in the same pitch is in the military list, X2.)

### P3 · Selling the beta › after the pitch comparison table
- **Current:** "Either way, the offer is the same beta: a short build, then a full quarter."
- **New:** "Either way, the journey is the same: a short build, then a full quarter. Close on the rung that fits: the diagnostic if they want to look first, the Rotor Distillation by default, the Rotor Beta only if they need you in every session or can't work to a set date."
- **Why:** the Distillation is now the default close; the Beta is the high-access rung.

### P4 · Objections and answers › "Is our strategy safe in an AI tool?"
- **Current:** "It stays in tools your company already approved, under your control. Nothing confidential goes in, and we agree what that means up front."
- **New:** "Interviews stay in tools your company already approved, under your control. Nothing confidential goes in, and we agree what that means up front. In the Distillation, leaders email me their interview summaries, and I draft in my own AI account, one private project per company, training switched off in its settings, deleted from my side at the end with written confirmation; the vendor may retain it for [X days]."
- **Why:** the old answer is only true for the Beta.

---

## Data

### P5 · Organizational AI integration › Three levels › after the table
- **Current:** "Do not host client strategy data yourself. If a client wants level 2 or 3 and has no IT team, bring in a developer partner under a separate agreement."
- **New:** "Do not host client strategy data yourself, with one approved exception: the Rotor Distillation's drafting (see Governance). If a client wants level 2 or 3 and has no IT team, bring in a developer partner under a separate agreement."
- **Why:** approved at RP2 (2026-11-10) and amended at RP3 (2026-11-11).

### P6 · Organizational AI integration › Governance › "Interview data" bullet
- **Current:** "Interview data: full interview transcripts are read only by you, stored in the client's own AI platform, and deleted from your notes at the end of the engagement. What goes into the divergence summary is quoted without names unless the leader agrees."
- **New:**
  > - **Interview data (Beta):** full interview transcripts are read only by you, stored in the client's own AI platform, and deleted from your notes at the end of the engagement. What goes into the divergence summary is quoted without names unless the leader agrees.
  > - **Interview data (Distillation):** interviews run in the client's own AI. Each leader emails you their summary block only; full transcripts stay in the client's AI and you don't read them (unlike the Beta). Your drafting runs in your own AI account (a one-person plan), one private project per company, named by code, with training **switched off in settings**; confirm that in writing before the first interview. At close-out, delete the project, the summary emails and every copy, and send written confirmation. Tell the client the vendor's retention period for deleted content: [X days, confirmed before kickoff]. Say "switched off", never "excluded by contract". Quotes are never attributed unless the leader agrees; no AI helper may attribute one. Full wording: `build/client-pack/governance-one-pager.md`.
- **Why:** decisions of 2026-11-10 and 2026-11-11.

### P7 · Learning loop › The alignment diagnostic › three bullets now out of date
- **Current (data rule):** "**Data rule:** interviews run in the client's own AI. Decide before building how summaries are combined: by the client in their own AI (no hosting, but the CEO sees individual answers) or sent to you for the agent to combine and delete (more candour, but you hold data briefly). Either way, no report for fewer than three leaders, and quotes are unattributed."
- **New:** "**Data rule (decided):** interviews run in the client's own AI. Each leader's summary goes to a sealed drop-box; names and roles are removed on arrival, an agent writes the report, no person reads the summaries, and they are deleted once the report is delivered. No report for fewer than three leaders; quotes are never attributed. With the client's consent, the report is kept; for Distillation clients it becomes wave 0."
- **Current (what it collects):** "**What it collects:** the same wave 1 questions as the Interviewer Pack, so diagnostic data and beta data can be compared."
- **New:** "**What it collects:** wave 1 questions 1–9, word for word, so diagnostic data and program data can be compared. Question 10 is dropped, so the short wave 1 for diagnostic graduates asks it."
- **Current (first bullet's offer line, in the section intro):** "It ends with one offer: help settling them, which is the Beta."
- **New:** "It ends with one offer: help settling them. The diagnostic's approved copy names the Rotor Beta; whether it should also name the Rotor Distillation is for the diagnostic's own gate."
- **Why:** the diagnostic is built and gated; the playbook still describes it as undecided. Its approved copy isn't changed here.

---

## Calendar and delivery

### P8 · Beta structure › Rules for the async core › three bullets
- **Current:** "**Sell responsiveness, not availability.** Promise a reply standard, such as every memo answered within two working days, instead of open meeting access."
- **New:** "**Sell responsiveness, not availability.** Promise a reply standard instead of open meeting access: two working days in the Beta, three in the Distillation (urgent flags first)."
- **Current:** "**Book all three live sessions at kickoff,** inside windows you set. Never let two clients' Mirrors land in the same week."
- **New:** "**Book all three live sessions at kickoff,** inside windows you set (in the Distillation, the Mirror date is fixed at signing). **Never two Mirror days within three weeks of each other,** the Beta's Mirror included."
- **Current:** "**Scale in waves.** Start two or three clients together so prompt packs, review batches and the weekly rhythm are shared. Set the number per wave from your tracked hours, and protect synthesis time first."
- **New:** "**Scale in intakes.** In the Distillation, up to three companies start one week apart and share one Mirror day. Each intake's build overlaps no other build; the Beta starts after an intake's Mirror day, during its light live run. An intake runs with two companies, never with one. If any evening-and-weekend week passes 6 h, the next intake drops to two. Use `build/templates/intake-calendar.md`."
- **Why:** the five calendar rules in RP2 §2, tightened from "the same week".

### P9 · Beta structure › after "Rules for the async core"
- **Current:** "The rotor-async-beta skill runs each step: engagement plan, prompt packs, interviewer brief, synthesis, flight logs, session prep and live-run pulses."
- **New:** "**In the Beta,** the rotor-async-beta skill runs each step: engagement plan, prompt packs, interviewer brief, synthesis, flight logs, session prep and live-run pulses. Whether the Beta moves to the AI helpers below is your decision (RP6).
**In the Distillation,** AI helpers draft and you decide. A1 interviewer and A10 noise audit run in the client's AI (existing). A2 synthesizer, A3 wave drafter, A4 divergence drafter, A5 candidate drafter (options only, never a recommendation), A6 five-tests checker, A7 script drafter, A9 update drafter and A12 results compiler run in your own account's company project. A8 red-team and A11 pulse run in the client's AI. Packs: `rotor/product/build/agents/`. Not automated, by design: choosing the schwerpunkt candidates, the Mirror, the CEO review, and your replies (AI may draft; you send in your own words)."
- **Why:** RP2 §5. The Beta's delivery is unchanged unless you decide otherwise.

### P10 · Learning loop › The override log › first paragraph
- **Current:** "Keep it from the first beta. Every time you change something the AI drafted, log one line: what the AI said, what you changed, why, and which step it was (interview follow-up, synthesis theme, divergence summary, schwerpunkt candidate, guardrail wording, flight log, pulse question)."
- **New:** "Keep it from the first intake or Beta. Every time you change something the AI drafted, log one line, **step code and categories only, never client content:** date · company code (e.g. 27A-2) · step S1–S11 · change (none, cut, added, reworded, reordered, replaced) · why (wrong, weak, tone, missing context, judgment call) · minutes · optional method note about the helper's instructions, never about the client. Steps: S1 interviewer summaries, S2 syntheses, S3 wave files, S4 divergence summary, S5 schwerpunkt candidates, S6 five-tests mark-up, S7 video script, S8 red-team, S9 updates, S10 pulse syntheses, S11 results pack. Count unchanged approvals too, so you get a rate. Template: `build/templates/override-log.md`."
- **Add after the existing bullets:** "- A step becomes a candidate to hand further to AI at 15+ observations across 3+ companies, an override rate under 15%, and no "wrong" in its last 10. Handing over is decided at a track gate, never silently. **S5 is never handed over.**"
- **Why:** the old line ("what the AI said, what you changed") would put client content in your library. The ontology now defines the log as step and reason only.

### P11 · Next steps › three to-dos now out of date
- **Current:** "Decide your capacity rule: start clients in waves, never two Mirrors in the same week, a written reply standard, and a named backup facilitator for live sessions. Set the clients per wave from hours tracked on the first beta."
- **New:** "Capacity rule (decided): intakes of up to three, Mirror days at least three weeks apart, reply standards of two (Beta) and three (Distillation) working days, at most one Beta a year. Still open: a named backup facilitator for live sessions."
- **Current:** "Run the AI interviews and five tests on a friend's business as a dry run, and time your own review and synthesis hours. Keep all DND specifics out of anything you show clients."
- **New:** "Dry run in two stages (decided 2026-11-11): a simulated company with four AI-played leaders, then a founding intake of at most two real companies, told they're the first run. Time your own minutes on every step. The simulation is fictional and is never shown or used as a result." *(The DND sentence is in the military list, X11.)*
- **Current:** "Set up the override log template before the first beta starts."
- **New:** "Copy `build/templates/override-log.md` into your private library before the first intake or Beta."
- **Also:** "Write a one-page offer sheet and the employee transparency note." → tick the offer sheet (done, `package/offer.md` §3); the transparency note stays open. "Offer one or two founding betas." → "Offer the founding intake (at most two companies), using the founding wording. Offer the Beta only where a client needs you in every session." "Build the alignment diagnostic with the Labs agent crew, starting with the data-flow decision." → tick (built; in its Lab gates).
- **Why:** these are decided or done.

---

## For Brandon's decision: military references in the playbook

**Your track rule:** nothing new mentions your military service. The playbook is private, so these are lower risk than the website, but lines in it get said aloud to clients (pitches, "Why you", objections). Each has a civilian alternative. **The conflict-of-interest steps (X10–X13) are private compliance to-dos, not marketing: keep them, and check their status.**

| # | Location | Current (exact) | Civilian alternative | Note |
|---|---|---|---|---|
| X1 | Selling › Why you › quote | "I'm a military flight instructor with an MBA. My job is teaching people to hold a complex situation in their heads and make good decisions under pressure. I also train fellow pilots in human performance, using mishap case studies to sharpen how they make sense of situations. Rotor brings that to business strategy, for your people and the AI tools they now work with." | "I help leadership teams turn a written strategy into the calls their people make every day. I have an MBA. I built Rotor because I kept seeing strategy that was thorough and well argued, and almost none of it reached the moment of decision." | Said aloud to every prospect. The "fellow pilots… mishap case studies" sentence also falls under **guardrail 2**. |
| X2 | Selling › Why you › note | "Use the human performance line only after completing the December course. Keep all examples to general experience; no unit specifics." | Delete if X1 is accepted; otherwise keep. | Guardrail 2. |
| X3 | Selling › Pitch A | "The method builds on Porter, Rumelt and Bungay's work on mission command in business." | Keep (a citation), or "…builds on Porter, Rumelt and Bungay's work on turning strategy into action." | Low risk. |
| X4 | Objections › "You're a pilot, not a strategy consultant." | Answer: "Military aviation runs on commander's intent, briefing and debriefing, and crew resource management, which business has borrowed for decades. I bring that discipline plus an MBA." | Replace the row: **"You're not a big-firm strategy consultant."** → "No, and that's the point. You work with me directly, no associates and no hand-offs. The method builds on well-tested work on strategy and decision-making, and you'll see it on your own leaders' answers within weeks." | If no one knows your background, they won't raise it. Also the only "pilot" in the playbook. |
| X5 | How the AI behaves › after the bullets | "This mirrors graded assertiveness in aviation crew resource management (often taught as PACE: probe, alert, challenge, emergency). The Rotor AI behaves like a well-briefed first officer, not a compliance officer." | "This mirrors graded assertiveness as high-stakes teams such as hospital wards teach it (often as PACE: probe, alert, challenge, emergency). The Rotor AI behaves like a well-briefed colleague, not a compliance officer." | Matches the website change M14. |
| X6 | One model, many bridges › first paragraph | "…the way the laws of flight describe how an aircraft works. … A flight instructor teaching a loop, low-level navigation or radio calls keeps the physics constant, but reaches for analogies the student already understands: a sport they played, an instrument, cooking." | "…the way the laws of physics describe how a bridge stands. … A good coach teaching a new play keeps the play constant, but reaches for analogies the player already understands: a sport they played, an instrument, cooking." | Internal, but it's where your instructing voice leaks into client prep. |
| X7 | "Flight log" (Beta structure intro; table; Deliverables; "Between sessions: flight logs and pulses"; "Weekly flight log"; override log step list) | "weekly flight log" | Internal name can stay; client-facing it's already "update" (`build/voice/flight-log-style.md`). If you want it gone: "weekly update". | Aviation, not military. Listed so it's a choice, not an accident. |
| X8 | Optional module: the strategy debrief | "A sensemaking workshop built on how aviation and safety fields study failure." Cases: Mann Gulch, Tenerife, Air France 447. Last line: "Nothing from DND investigations or course materials." | Hold the module until you decide (guardrail 2). If kept: "…built on how safety-critical fields study failure", lead with Mann Gulch and the corporate cases, and keep the "public cases only" rule without naming DND. | Closest thing to the mishap case-study facilitation in **guardrail 2**. |
| X9 | Next steps › Days 31 to 60 › dry run | "Keep all DND specifics out of anything you show clients." | Keep as a private rule (it's now part of P11's replaced bullet; move it to its own line if you keep it). | Internal safeguard. |
| X10 | Next steps › intro | "Clear the conflict-of-interest disclosure first, build the demo second, and approach your first client within 90 days." | **Keep.** Private. | **Flag:** is the disclosure filed? |
| X11 | Next steps › First 30 days | "Submit a conflict-of-interest disclosure for outside work through your chain of command, under the DND/CAF conflict-of-interest rules (DAOD 5012-0). Include workshop facilitation and the strategy debrief module. Confirm what you may and may not do while serving." | **Keep.** Consider adding: "Include the Rotor Distillation, the Labs store sales, and the planned days off for Mirror days." | **Flag:** the disclosure predates the Distillation and the Labs store; you may want it to cover them. Your call; I can't judge the rules. |
| X12 | Next steps › Days 31 to 60 › December course | "During the December human performance course, keep private notes on facilitation techniques, in your own words, and ask which general human-factors models you're free to apply outside the CAF." | **Keep.** Private. | Guardrail 2 until you confirm completion. |
| X13 | Next steps › Days 31 to 60 › white paper | "…update white paper v1.1 with the ideas developed since (guardrails, living models and tripwires, margin, the human context window, graded assertiveness)…" | Keep; when the white paper is rewritten, use the civilian framing in X5 and website M15. | Indirect: the white paper is where "first officer" would resurface. |

**Count: 13 places in the playbook** (X1–X13). Four are private conflict-of-interest or course to-dos to keep (X9–X12).
