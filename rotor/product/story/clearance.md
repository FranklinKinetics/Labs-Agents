CLEARANCE · Rotor Distillation, RP5 Story (redo) · 2026-11-11

Reviewed: every new text line in `story/website-changes.md` (H1–H9, HW1–HW14, F1–F6, S1–S4, SEO1–SEO3, O1), `story/playbook-changes.md` (P1–P14, private), and `package/offer.md` (sections 1–5). Decisions in force to 2026-11-11 applied: existing military references stay, the playbook's Beta range is private, no Beta count in client copy, no Distillation/Beta contrast on how much of Brandon.

## Guardrails 1–14
1. No DND/CAF endorsement or connection: pass. No new military reference (the playbook's existing "DND specifics" line in P14 stays by decision).
2. Military aviation course: pass (not mentioned).
3. No ROI: pass. "What it doesn't promise" says plainly that six weeks can't show up on the books.
4. No client results: pass. H8 placeholder and founding wording require separate written permission.
5. No invented testimonials, customers, quotes or numbers: pass. No clients or results are claimed.
6. Traceable data claims: pass. Figures (12 weeks, 3 calls, 45/60/60 min, 20-min interview, 10 dilemmas, 6 weeks live, team of at least 5, 3 working days) match `rp2b-spec.md` and `offer.md`.
7. Pricing: pass. Neither Distillation nor Beta carries a price, range, discount or credit in client copy. The $790 appears only in a rule line (website-changes line 13), not in copy. The playbook's CAD range is private and marked internal-only (P6).
8a. No Brandon time for Labs: pass. The diagnostic is described as needing none of his time (private playbook). The consulting offers are consulting.
8b. No dark patterns: pass with one note (S3 below). The "places are limited" scarcity line is removed in H3, H9, S1 and SEO3. The playbook's founding discount and "time-limited line" are removed (P6).
9. Public or licensed data: n.a. (no new data sources).
10. No profiling of individuals: pass. Results are by team only, the beta team has at least five people, and quotes are unattributed.
11. Customer data minimal: pass. See data check below.
12. Rotor Core contents: pass. Named only (HW10, offer §3), never described.
13. Reader knows more than the AI: pass.
14. Accessible: pass (text and tables; no new images).

## Specific checks
- "Pilot": none in client copy. It appears once in `offer.md` line 23 (see Nice to fix).
- Betas a year: not in the website or offer copy. It appears only in the private playbook (P1, P14), labelled internal.
- Fake scarcity: none. "You'd be among the first" is a true statement, with no countdown or limit.
- Offers compared on price: none, except the S3 problem below.
- Offers compared on how much of Brandon: none in client copy. The ladder (H7, offer §2) sorts by "do your leaders already agree". HW12 is borderline (see Nice to fix).
- Data wording, in HW11, F3, F5, offer §3 and P5, P8: pass.
  - Interviews and document reading run in the client's own AI.
  - Brandon receives short summaries and a structured digest by email, never documents or full conversations.
  - Drafting is in his own account with training "switched off in settings", and never "excluded by contract".
  - Deleted at close-out with written confirmation.
  - Vendor retention is bracketed as [X days] (tracked in O1).
  - Beta line ("full transcripts read only by you", "never hosts your strategy data") and diagnostic line (drop-box, names removed, deleted once the report is delivered) are accurate to their own decisions.
- Reply standards: Beta two working days (HW4, P11), Distillation three, urgent flags first (HW7, offer §3, P1, P11). Pass.
- F3 diagnostic sentence ("The alignment diagnostic briefly holds each leader's summary, with names removed, and deletes it once your report is delivered.") is word for word the approved text. The Beta sentence is also intact (split by the inserted Distillation sentence). Brandon is flagged in the Why line that an approved answer was edited. Pass.

Claims checked: 22 of 22 have sources (the spec, offer §3, governance one-pager, decisions log, and the existing site copy for "Works with ChatGPT, Claude or Microsoft Copilot").

## Must fix before release
1. **S3 (website-changes.md, "Start a conversation" step 3).** "fixed fee" sits only beside the Beta, so the sentence contrasts the two offers on price and hints at a fee structure. Replace with: "**We begin.** The Rotor Distillation takes about 12 weeks, with three calls with your CEO, and starts when you're ready. The Rotor Beta takes about four and a half months: a build, one live quarter, and a review where you decide whether to scale. Three meetings; the rest runs on your schedule." (Fenn's own note offers this fallback.)

## Nice to fix
1. **HW12 ("What it doesn't include").** It lists what the Distillation leaves out (the leadership working session, video, interview rounds) and ends "it's the Rotor Beta". Read cold, that is "less of Brandon in the room". Suggested: "The Distillation starts from a strategy your leaders already share, so it doesn't include the work of getting them there. If that work is what you need, it's the Rotor Beta."
2. **`offer.md` line 23.** The naming record lists "pilot", "flight", "mission", "squadron", "wing". It's internal, but the repo grep for "pilot" will hit it. Suggested: delete the line, or reduce it to "Avoided on purpose: anything that sounds like a trial run, or a group that meets."
3. **F4 versus HW8/HW9.** F4 says "the other leaders send a short written reaction", while HW8 and HW9 say one or two more leaders may also do an interview. Suggested: "...and the other leaders send a short written reaction to the draft (one or two may also do a short interview)."
4. **HW13 note.** "you keep the Rotor Sheet" against "the Rotor Sheet and the Rotor Core go into your AI tools under licence" (offer §3, spec). The open [NOTE] already flags it. Resolve before publishing.
5. **P12.** "your own account's company project" is ambiguous. Suggested: "the private project for that company in your own account".

Verdict: NOT CLEARED until the S3 fix is applied. With that single change, CLEARED. The nice-to-fix items do not block release.
