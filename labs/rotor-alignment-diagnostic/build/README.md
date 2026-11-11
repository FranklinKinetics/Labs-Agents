# Rotor Alignment Diagnostic: the app (bench build)

**Status:** Step 1 of the build plan, the "bench build". All the logic is written and tested. Nothing is connected to the outside world: no Google Cloud, no Squarespace, no email, no Claude. No accounts exist and nothing has been spent.

Think of it as a mailroom built and tested on a workbench. The walls, locks and sorting rules are done. The real mail slot (Squarespace), the real clerk (Claude) and the real post office (email) are plastic stand-ins until Step 2 and Step 3.

## Run the tests

```
cd labs/rotor-alignment-diagnostic/build
pip install -r requirements.txt
python3 -m pytest
```

No internet is needed for the tests, and none of them can spend money. Expect `168 passed`.

## What each part does

| File | What it does, in plain words |
|---|---|
| `diagnostic/blocks.py` | Checks a pasted summary has the exact 17-line shape (leaders may edit what they wrote, not the labels). Rejects bad pastes with a plain message and stores nothing. Removes the leader's name and role from the whole text, blanks the "Leave out" field, and makes a one-way code (HMAC-SHA256 with a per-company secret salt) so the same person can't submit twice. The name itself is never kept. |
| `diagnostic/service.py` | The rules: making a company from an order, the 21-day window, closing early, the one 14-day extension, the one restart, the "fewer than 3" outcome, running the report, holding a bad report, delivery, deletion, and the 14-day check-in. |
| `diagnostic/synthesis.py` | Builds the request to the AI: the approved instructions (section 3 of `04-synthesis-agent.md`, with the section 7 changes) with the report template dropped in, and the blocks as the user message. Also holds the bench stand-ins (a fake AI that returns a canned report, a fake that says `INSUFFICIENT`, a fake name checker). |
| `diagnostic/checks.py` | The automatic checks on what the AI returns: headings present and in order, section 9 word for word (the Beta paragraph, then the Rotor Distillation sentence, then one link; a report missing the Distillation sentence is held), the check sheet present with every answer right, a plain word search for banned words, no leftover `[removed]`. Any failure holds the report. |
| `diagnostic/emails.py` | The email texts (setup kit, report, not enough leaders, held-report alert to Brandon, 14-day check-in) and the mail interface. Emails can only be built for the CEO or Brandon. There is no way to address a leader. |
| `diagnostic/orders.py` | The interface for "any new diagnostic orders?" plus a fake. |
| `diagnostic/pdf.py` | A plain PDF of the report. Iris styles it at G4. |
| `diagnostic/store.py` | Where things are kept. Bench version is in memory. |
| `diagnostic/prompts/` | Word-for-word copies of the approved instructions, report template, interviewer instructions and leader note. A test fails if they drift from the files in the lab folder. |
| `diagnostic/adapters/` | The real connections (Claude, Squarespace, email). Written, never run, never called by a test. They read secrets from environment variables only. |
| `tests/` | 168 tests: Stage 1 of `08-test-plan.md` (see below). `tests/aligned.py` is the invented, broadly aligned bench company (Tamarack Supply, marked FICTIONAL). `tests/test_reconciliation_changes.py` covers the 2026-11-11 changes. |

## Two links, not one

Each company gets two private links. The **drop-box link** goes to leaders. The **status link** is the CEO's alone: it shows "2 of 5 received" (or "6 received (5 planned)" when more leaders take part than planned) and is the only place to close early, extend or restart. Keeping them apart means a leader can't close the window.

## Which Stage 1 tests run on the bench

| Plan item | Covered by |
|---|---|
| Check A: 0, 1, 2 blocks give no report; the agent never runs; email with restart option; blocks deleted | `test_app.py` |
| Check A: forced agent run on 2 blocks handled as `INSUFFICIENT`; 3 valid plus 1 malformed runs on 3; restart once only, refused after 12 months; status shows count only | `test_app.py` |
| Check B: stored text has no name, role or leave-out content; fingerprints only | `test_app.py`, `test_blocks.py` |
| Check C: labels and order checked by script against `rotor/interviewer-pack.md` (and `03-interviewer.md`); edited content accepted, edited labels rejected; headings; check sheet; banned words | `test_blocks.py`, `test_synthesis_checks.py` |
| Check D: setup kit and check-in go to the CEO only; no leader email; check-in exactly once; section 9 wording exact | `test_delivery_emails.py`, `test_synthesis_checks.py`, `test_reconciliation_changes.py` |
| Check B2 (new): an aligned team. Five invented blocks; the canned aligned report passes every check and is delivered, not held | `test_reconciliation_changes.py` |
| Extra leaders: status wording, up to 8 accepted, the ninth refused | `test_reconciliation_changes.py` |
| Held reports: summaries wait with no time limit until Brandon acts | `test_reconciliation_changes.py` |
| Deletion; report kept only with consent; held report alerts Brandon and sends nothing | `test_delivery_emails.py` |
| Trap blocks T1, T3, T7, T8 | fully tested (`tests/traps.py`) |
| Trap blocks T2, T4, T5, T6 | built as fixtures; the bench proves the plumbing (they reach the agent as leader content, never as instructions; a leaked name holds the report). Whether the real AI handles them well is a Step 3 test. |
| Quebec head office rejected | `test_app.py`, `test_orders_adapters.py` |

## What is faked on the bench

- **The AI report.** A canned Larchmere report (and a canned report for the aligned company, Tamarack Supply) stands in for Claude. Nothing here shows the real agent writes a good report.
- **The second name check.** The fake only flags names the test plants. The real one is a separate AI call.
- **Squarespace orders.** A list of invented orders.
- **Email.** A list that records what would have been sent.
- **Storage.** Memory. Everything disappears when the tests finish.
- **Time.** A clock the tests move forward, so 21 days takes no time.

## Known limits (said plainly)

- **A colleague's name inside a block can't be found at the drop-box.** The drop-box only knows the submitter's own name. The defences are the interviewer ("a colleague"), the agent's rules, and the second check. The test plan says the drop-box "flags" T2; it can't, so I haven't pretended it does.
- **Names that are also ordinary words** (Mark, Will, Grant) are removed everywhere, as specified, so the text can read oddly. Safe, if a little clumsy.
- **Only the exact role phrase is removed**, not each word of it ("Engineering Lead" goes; "engineering" alone stays).
- **A held report is kept in the app** and its blocks stay until delivery (the privacy notice says "until the report is delivered"). There is no time limit: they wait until Brandon acts (decision 2026-11-11; a test covers it). The alert email gives reasons only, not the report. Brandon reads a held report on a private page that only his Google account can open (decision 2026-11-11). It is built when the app goes online, in Step 2, and nothing exists for it yet.
- **Banned-word search covers the report, not the check sheet.** The agent's own check line reads "Any result, savings or ROI claim", so searching the sheet would hold every report.
- **A report containing `[removed]`** (a stripped name inside a quote) is held. That rule is mine, not in the plan.
- **Word count** (1,200 to 2,000) is a warning, not a hold, because the plan doesn't list it as a hold reason. A report for a team that mostly agrees may be shorter. (Amended 2026-11-11 after the reconciliation with Rotor Product.)

## What Step 2 (accounts) needs

1. **Google Cloud project** with billing and the CAD $10/month alert. Montréal region. Cloud Run, Firestore, Cloud Scheduler (three jobs: poll orders every 10 min, process due windows and emails, and one spare), Secret Manager.
2. **A Firestore store** with the same methods as `store.py`. Not written yet.
3. **A thin web layer** (drop-box page, status page, the three URLs `/drop/<token>`, `/status/<token>` and the scheduler hooks) calling `App`. Not written yet; the logic it calls is done and tested.
   **Deploy step, held reports:** also build the private page where Brandon reads a held report. Only his Google account can open it (decision 2026-11-11). No code exists for it yet. It needs no time limit logic: summaries wait until he acts.
4. **Squarespace read-only Orders API key.** Then check `adapters/squarespace.py` against one real test order: how the checkout questions appear is my best guess and unverified.
5. **Email route.** `adapters/smtp_mailer.py` is a placeholder shape. Brandon's Google Workspace mailbox is the plan; the route (SMTP app password, or the Gmail API) is decided here.
6. **Secrets in Secret Manager:** `ANTHROPIC_API_KEY`, `SQUARESPACE_API_KEY`, the mail credentials. Never in the repo. A test scans this folder for key patterns.
7. **Settings to fill** (`config.py` lists them; `Config().problems()` reports what is still a placeholder): the app's web address. The mailing address (Franklin Kinetics Consulting Corporation, 1400-2500 Victoria Ave, Regina SK S4P 3X2) and the Start a conversation link (`https://www.franklinkinetics.com/contact`) are set as of 2026-11-11.

## What Step 3 (real AI) needs

1. Anthropic API account with the US$25/month cap.
2. Run `adapters/anthropic_adapters.py` on the five Larchmere blocks and the trap blocks (T1 to T8). Request settings follow the plan: model `claude-opus-5-5`, streaming, `max_tokens` 64000, `output_config={"effort": "high"}`, default thinking, and the server-side refusal fallback. `stop_reason` is checked before any content is read, and a refusal holds the report.
3. Check every report against the test plan: Check B's second-check test (plant a name, catch it 10 times out of 10), the "all" claims, the guess test with Vera.
4. The second name check is a real adapter too (`AnthropicIdentifierCheck`). Its prompt is mine and untested against the real model.

## Brandon decides

All four earlier questions are answered (2026-11-11). (Amended 2026-11-11 after the reconciliation with Rotor Product.)

1. **Held reports:** Brandon reads one on a private page only his Google account can open. Built when the app goes online (Step 2).
2. **How long may a held report's blocks wait?** No limit. They wait until Brandon acts.
3. **More leaders than planned:** the drop-box takes up to 8 whatever was planned. The status reads "4 of 6 received" while received is at or under planned, and "6 received (5 planned)" when over.
4. **Mailing address and link:** Franklin Kinetics Consulting Corporation, 1400-2500 Victoria Ave, Regina SK S4P 3X2; Start a conversation is `https://www.franklinkinetics.com/contact`.

## What changed on 2026-11-11 (reconciliation with Rotor Product)

- **Report section 9** keeps the approved Beta paragraph and adds one sentence: "If there's little to settle, the Rotor Distillation takes your strategy into your AI tools." One link, no verdict. `checks.py` holds any report whose section 9 differs or lacks that sentence.
- **The report may show an aligned team.** Minimum counts in the template and instructions are now "up to" the old maximum. "Your views don't split here" is allowed where there is nothing. Every section is still filled.
- The prompt copies in `diagnostic/prompts/` were regenerated from `04-synthesis-agent.md`; the drift test passes.
