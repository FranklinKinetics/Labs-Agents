# Labs to calls: the plan (v2)

Ines, 2026-11-26. Written from Brandon's brief of the same day (recorded in `logs/decisions.md`). v1 went to one adversarial critic (Sonnet); the critique is in `critique-2026-11-26.md`, and section 6 says what changed. This is the plan the crew now runs.

## The goal
Labs exist to get owner-led firms (20–200 people) to **call Brandon** about paid work: Rotor strategy engagements, or AI automations worth at least $1,000/month per client. Selling Lab products is secondary. A Lab that sells copies but never produces a call has failed.

Brandon's budget: **10 hours a week at most**, one hour a night. He can't run operations.

---

## 1. Audit: the current system against the goal

| Part | Today | Serves "get a call"? | Change |
|---|---|---|---|
| Schwerpunkt | "Feel how fast… leave them owing us a favour." | Half: no ask. | **Rewritten** to end in a call. |
| 7 personas | One per stage, a production line | No. Every handoff is a context load and a wait. | **Cut to 4**: Ines, Mack, Fenn, Vera. |
| 8 gates | ~10 min each, ~80 min per Lab, plus waiting | No. Most are reversible calls. | **Retired. 2 remain: G1 Release, G2 Money.** |
| Four Proofs | Quality bar | None of the four is "leads to a call". | **Kept, plus a fifth line on every card: the call path.** |
| Signals | Free text; no tracking at all | No data on calls. | **Replaced** by a four-rung ladder: visits → contacts → calls → clients. |
| Rotor Alignment Diagnostic | Building; CAD $790; cloud build with spend | Indirect, and costly to finish | **Held** behind the invoicing Lab. Not killed. |
| Your Strategy Page, Tested | G3 passed, Look drafted | Yes, for Rotor calls; nearly done | **Finish** under the new flow, with the page checklist. |
| Automatic Groceries, Regina Data Map | Shipped | Weak: no owner path, no CTA, no tracking | **Retrofit** the pages (checklist below). |
| Discovery | None. Labs are posted and wait. | **The biggest gap.** | **One outreach loop**, one 45-day test. |
| Fenn's "soft CTA, no hard pitch" | Avoids the ask | Works against the goal | **One clear call CTA per page**, still no hard pitch. |

### The crew: 4, down from 7

| Persona | Role | Took over | Model |
|---|---|---|---|
| **Ines** | Steward: queue, weekly review, signals, prospect list, price reads | Sol (pricing), Juno's prospect research | Sonnet; Haiku for chores |
| **Mack** | Builder: data, licences, build, look, usability | Juno (data, licences), Iris (look, usability) | Sonnet |
| **Fenn** | Voice: Lab pages, Rotor Lesson, outreach notes, canned replies | Story, outreach copy | **Opus** for anything public; Haiku fills canned replies |
| **Vera** | Guardian: clearance on everything, CASL, the filter that replaces the gates | Accessibility (from Iris) | Sonnet |

**Two checks on every source:** Mack (or Ines) records the licence; Vera checks it independently at clearance. The person who writes something never clears it.

### Gates: 2
- **G1 Release**: anything public. A Lab page, a price, an outreach template, and **each outreach batch** (Brandon pressing send in Gmail is the release; nothing is sent for him).
- **G2 Money**: anything that spends money or commits Brandon to a client.

Everything else Vera clears, and Brandon sees only what she flags. Brandon's rule stands: *if the crew is unsure whether something needs him, it doesn't; it's logged in the weekly review.* (The critic argued for "unsure → escalate". We didn't adopt it as a blanket rule, because Brandon set the opposite; the risky case it was guarding, irreversible sends, is covered because every send is already a G1 item he releases himself.)

---

## 2. Discovery: top 3 channels

| # | Channel | Brandon h/week | 30-day test | Pass / fail |
|---|---|---|---|---|
| **1 · start** | **Personal email to owners of qualified trades and construction firms**, with a one-minute Invoice Clock and a reply-with-a-number ask | 1.5 | 40 qualified firms, all sent in days 1–14, one follow-up at day 7 | **Pass: ≥1 call booked by day 45.** Early read at day 21: ≥3 replies. **Fail: 0 calls by day 45 → change the hook and rerun once, then judge the channel.** |
| 2 | Bookkeepers and accountants who serve trades firms, as referral partners | 1.0 | 15 Regina bookkeeping firms contacted | Pass: ≥2 agree to show the Invoice Clock to a client. Fail: 0. |
| 3 | Trade-association education: an article or evening session on "the proper invoice and the 28-day clock" | 0.5 now | Pitch 3 associations | Pass: 1 slot booked. Fail: 0. |

**The bar at day 60 for the whole plan: one scoped engagement conversation** (a State Map Diagnostic or an automation scope agreed in principle), from any source. A call alone isn't the finish line.

### Channel 1: personal email to trades owners (start here)
**Evidence**
- **A dated, local pain.** Saskatchewan's prompt-payment rules (in force 1 March 2022, for contracts from that date) give an owner 28 days to pay after receiving a *proper invoice*. The clock starts when a correct invoice arrives, not when the job ends. Sources: [Government of Saskatchewan](https://www.saskatchewan.ca/government/news-and-media/2022/march/01/legislation-to-protect-contractors-takes-effect-today), [Miller Thomson](https://www.millerthomson.com/en/insights/construction-and-infrastructure-law/saskatchewan-prompt-payment-legislation-in-force/), [Osler](https://www.osler.com/en/blogs/construction/march-2022/saskatchewan-leads-western-canada-to-prompt-payment-and-adjudication).
- **A findable audience.** Firms list themselves on association and chamber directories ([constructionsk.ca](https://constructionsk.ca/association/regina/), [Sask Chamber directory](https://business.saskchamber.com/)) and publish contact addresses on their own websites.
- **One real case.** Brandon's first prospect is a ~30-person trades firm with slow invoicing.
- **Unknown:** reply rates for this segment here. Forty sends is a test of the hook, not a verdict on the channel.

**Why first.** It's the only channel the crew can run almost end to end. Ines builds and qualifies the list, Fenn writes each note, Vera clears the batch, drafts land in Brandon's Gmail, and he presses send. Nothing waits on a third party.

**How it runs** (loop: `wiki/loops/discovery-outreach.md`)
1. **Qualify first.** 20–200 people, evidenced by the firm's own site, an association listing or a job posting. Owner or GM named publicly. No `info@` unless it's the only published address, and then the note asks to be passed to the owner.
2. **One private prospect sheet** (Google Sheet in Brandon's Drive, never this repo): firm, size evidence, contact, **consent source URL and date** (CASL proof), ref code, sent, follow-up, reply, call, outcome. The repo holds counts only.
3. **The note** (Fenn, Opus, cleared once at G1 as a template): three short paragraphs. The 28-day clock in one line, the Invoice Clock link (`?ref=<code>`), and the ask: *"Reply with one number, how many days from job done to invoice sent, and I'll tell you where invoices usually wait in a firm your size."* Then the booking link with fixed evening slots, then "Reply STOP and I won't write again."
4. **One follow-up** at day 7, two lines. Never a third.
5. **Replies.** Haiku drafts from Fenn's canned set (a number came back; "not interested"; "who are you"; "send more"; STOP). Brandon approves from his phone. STOP goes on the suppression list the same day.
6. **Travel-week rule.** If Brandon flags a flying stretch in the queue, no sends that week. An away reply points to the booking page.

**CASL rules (Vera checks every batch):** only addresses the business itself published, with no "no solicitation" notice, about something relevant to the recipient's role; consent source logged; sender name, mailing address and a working unsubscribe in every message; suppression list honoured within 10 business days (we do it same day). No scraping against a site's terms; Procore and paid lead lists are out.

### Channel 2: bookkeepers as referral partners
- **Evidence.** Late invoicing lands on the bookkeeper's desk as late receivables, but fixing the workflow isn't their job. US data puts the accountant as owners' most trusted advisor (31%, OnPay 2019, via [CPA Practice Advisor](https://www.cpapracticeadvisor.com/2019/05/24/86-of-smbs-view-accountants-as-trusted-business-advisors/)). **No Canadian figure was found**, so this is a Living Model, not a fact.
- **Hours:** ~1 h/week. **Why second:** higher leverage, but partners refer when a client complains, not on our clock. Start in month 2.

### Channel 3: trade-association education
- **Evidence.** Prompt payment is the associations' own advocacy topic ([constructionsk.ca, June 2026](https://constructionsk.ca/news-updates/latest-news/2026/06/)). The Saskatoon Construction Association reports 575+ members ([source](https://sites.google.com/view/stoon-construction-assoc/about-us)); a Regina count wasn't found.
- **Hours:** low to pitch; a talk is usually in the daytime, and lead times run months. **Why third:** credibility, not speed.

### Channel 0: the firm Brandon already knows
It isn't a channel, so it isn't ranked, but it's the first conversation. After its State Map Diagnostic, Brandon asks for **one introduction** to another owner. Fenn drafts the line.

---

## 3. Conversion path: Lab → call

```
Outreach note ──┐
Lab page ───────┼─► Invoice Clock (1 min, phone, no AI) ─► Reply with a number
Referral / intro┘          │ optional                          or book a call
                           ▼                                         │
              Where Invoices Wait (AI check,                         │
              for the office manager, 10 min) ───────────────────────┤
                                                                     ▼
                                            Call (20 min, fixed evening slots)
                                                                     │
                                                                     ▼
                                     State Map Diagnostic (consulting, unpriced)
                                  steps where invoices and jobs wait with no owner
                                                                     │
                                            ┌────────────────────────┴───────┐
                                            ▼                                ▼
                         Automation (unattended,                   Rotor engagement
                         unpriced in public)                       (Distillation / Beta)
```
This chain is also written into `canon/ontology.md` as **the Call Path**.

### Every Lab page must have (Vera checks all eight)
1. **The job in the owner's words** (headline).
2. **The price**, or "Free".
3. **What it does in one to five minutes**, and what you need to hand. Phone-first.
4. **Speed**: honest build hours.
5. **The Rotor Lesson**, one sentence, plain words.
6. **The business-owner path**: one short paragraph headed *"If you run a firm of 20–200 people"*, saying what this would look like as a weekly routine in their firm. It describes what it does, never what it earns (guardrail 3).
7. **One call to action**: "Book a 20-minute call", linked `?ref=<slug>`, with "or just reply with a question" beside it. No second ask competes with it. (The buy or download button is the product, not a CTA.)
8. **None of these:** a consulting price, "$1,000/month", an ROI promise, Brandon's military role.

### The next Lab: the Invoice Clock (+ Where Invoices Wait)
Two layers, built in that order:
- **Invoice Clock** (free, the hook): five yes/no questions on one phone screen, no AI and no data. Each "no" marks a step where invoices wait. It ends with the reply-with-a-number ask and the CTA.
- **Where Invoices Wait** (free, the optional second step): a paste-in AI check for whoever holds the dates (usually the office manager). It maps the steps from job done to paid, the days waiting at each, and which step has no one responsible. A self-serve mini State Map.

**Why invoicing beats the alternatives.** It leads straight to a recurring automation (job closed → invoice drafted with the paperwork → office approves in one tap → sent → reminders → a weekly owner digest), which is monthly value that fits a ≥ $1k/month offer and runs without Brandon. The firm already has the data, it matches the live prospect, and the 28-day rule gives it a date. Quote follow-up came second: strong, but no legal clock and no live prospect. After-hours lead response is harder to run unattended.

---

## 4. Measurement

### Per Lab: the Signal ladder (on every lab card)
`visits → contacts → calls → clients`, monthly.
| Rung | Counted from | Who |
|---|---|---|
| Visits | Squarespace page views for the Lab page | Brandon reads one number (1 min) until analytics is connected |
| Contacts | Replies and forms carrying a `ref`, a "Which Lab or email brought you here?" answer, or a reply to an outreach note | Ines (Gmail search) |
| Calls | Bookings on the booking page with `ref`, plus calls booked by reply | Ines (Calendar) |
| Clients | Signed paid work, credited to the **first touch** (a Lab slug or an outreach ref code) | Ines, confirmed by Brandon |

Phone and email replies lose the `ref`, so Ines matches them by firm against the private prospect sheet.

### Weekly review
`logs/weekly/YYYY-Www.md`, compiled by Ines on Haiku every Sunday. One phone screen: a verdict, three bullets at most, one decision. Detail sits below a line Brandon never has to scroll past. Loop: `wiki/loops/weekly-review.md`.

---

## 5. Brandon's week (cap 10 h)

| Item | Time |
|---|---|
| Weekly review | 10 min |
| Queue: G1 / G2 packets | ≤ 45 min |
| Glance at each outreach draft and press send (20/week in weeks 1–2, then follow-ups) | 1.5 h |
| Approve canned replies from the phone | 20 min |
| Calls (≈2) including 10 min prep each | 1.5 h |
| State Map Diagnostic for the trades prospect, **capped at 90 min** of Brandon | 1.5 h |
| **Planned** | **≈ 5.75 h**, leaving 4 h for surprises and the first proposal |

One-off setup, already in the queue: a booking page with fixed evening slots (Google Calendar appointment schedule, included in Workspace), and one form field on Start a conversation. About 25 minutes in total, once.

---

## 6. What changed after the critique

| Critic's point | Change |
|---|---|
| The hook is homework | **Invoice Clock first**: one minute, no AI, no data, plus a reply-with-a-number ask. The AI check becomes the optional second layer, aimed at the office manager. |
| The numbers are noise; 30 vs 60 days | All 40 sent in days 1–14, a follow-up at day 7, an early read at day 21, **judged at day 45 (≥1 call)**, and a **day-60 bar of one scoped engagement conversation**. Fail means changing the hook once before judging the channel. |
| A junk denominator | Qualify 20–200 headcount with evidence before a firm enters the sheet. |
| Hidden hours | Fixed evening booking slots, Haiku-drafted canned replies, a travel-week rule, the diagnostic capped at 90 min, and a recounted budget (5.75 h). |
| CASL gaps | Consent source and date logged per address, a suppression list, "reply STOP", no Procore or lead lists, and the sheet kept private (out of the repo). |
| The cuts remove safety nets | Each batch is a G1 item; the writer never clears; licences get two checks. "Unsure → escalate" was declined because Brandon set the opposite (see section 1). |
| No CRM, weak attribution | Private prospect sheet, per-recipient ref codes, and first-touch credit matched by firm. |
| The known prospect is a footnote | It's Channel 0: the first conversation, ending in one introduction. |
| Not adopted | Charging for the State Map Diagnostic: that's a Money decision for Brandon, raised in the weekly review once the first one is done, not now. |
