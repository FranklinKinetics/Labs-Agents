# Loop: discovery outreach (and the active test)

- **Trigger:** an active discovery test. One test at a time.
- **Owners:** Ines (list, sheet, tally; Sonnet), Fenn (template and replies; Opus for the template, Haiku for filling), Vera (CASL and clearance on every batch; Sonnet).
- **Brandon's minutes:** about 110 a week while sending (glance at and send 20 drafts, approve replies, take calls); about 30 a week in follow-up-only weeks.

## Test 1 · Trades owners × the Invoice Clock
| | |
|---|---|
| **Status** | **Running: crew phase.** Ines qualifies prospects now; the send clock starts on Brandon's G1 pass (`QUEUE.md` item 1). |
| **Segment** | Owners or GMs of trades and construction firms with 20–200 people, Regina first, then Saskatchewan |
| **Hook** | The Invoice Clock (`labs/invoice-clock/`) and the 28-day prompt-payment clock |
| **Ask** | "Reply with one number: how many days from job done to invoice sent." Then the booking link. |
| **Volume** | 40 qualified firms. All first notes sent in days 1–14 (20 a week). One follow-up at day 7. No third note. |
| **Early read · day 21** | ≥ 3 replies (any reply that isn't STOP) |
| **PASS · day 45** | **≥ 1 call booked from the 40** |
| **FAIL · day 45** | **0 calls.** Action: change the hook (not the channel), rerun once with 40 new firms, then judge the channel. |
| **Day-60 bar (whole plan)** | 1 scoped engagement conversation (a State Map Diagnostic or an automation scope agreed in principle), from any source |

Tally (counts only; Ines updates weekly):
| Qualified | Sent | Follow-ups | Replies | STOP | Calls | Scoped |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Steps
1. **Qualify** (Ines, Sonnet). Sources: the firm's own website, Construction Saskatchewan and Saskatchewan Chamber directories, the firm's public job postings. 20–200 people, with the evidence noted. Owner or GM named publicly. Not Procore or paid lead lists (their terms).
2. **Log** each firm in the **private prospect sheet** (a Google Sheet in Brandon's Drive, never this repo): firm, size evidence, contact, **consent source URL and date**, ref code (`ic-01`…`ic-40`), sent, follow-up, reply, call, outcome.
3. **Draft** (Haiku fills Fenn's G1-approved template). Each note gets one line of real personalisation from the firm's own site.
4. **Clear** (Vera): CASL checks per address, guardrails, and no claims beyond the template.
5. **Stage** 20 drafts in Brandon's Gmail drafts folder (or, until the Gmail connector is set up for this, a copy-ready file in the private Drive folder). Brandon glances at each and presses send. **That is the G1 release for the batch.**
6. **Follow up** once at day 7 with the approved two-line note.
7. **Replies.** Haiku drafts from Fenn's canned set (a number came back · "not interested" · "who are you?" · "send me more" · STOP). Brandon approves from his phone. STOP goes on the suppression list the same day.
8. **Travel-week rule.** If Brandon marks a flying stretch in `QUEUE.md`, no sends that week; an away reply points to the booking page.
9. **Tally** every Sunday into the table above and the weekly review.

## CASL rules (Vera)
- Only addresses the business itself published, with no "no solicitation" notice, and a message relevant to the recipient's business role (implied consent).
- Every message: Brandon's name, Franklin Kinetics Consulting Corp., a mailing address, and "Reply STOP and I won't write again."
- The suppression list sits in the private sheet. Honour it the same day (the law allows 10 business days).
- Keep the consent source and date for every address for as long as we keep the address.

## Channels queued behind this test
2. Bookkeepers serving trades firms, as referral partners (start in month 2).
3. Trade-association education on the 28-day clock (pitch in month 2 if test 1 passes).
Evidence and reasoning: `plan/labs-to-calls.md`, section 2.
