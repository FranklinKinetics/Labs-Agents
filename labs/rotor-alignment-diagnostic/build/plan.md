# Build plan · Rotor Alignment Diagnostic

**2026-11-10 · Mack (Builder), written in-session by Ines following `crew/mack.md`**
Nothing has been built, bought or signed up for. This plan ends with a spending decision for Brandon.

---

## Decision needed

```
BUILD PLAN · Rotor Alignment Diagnostic · 2026-11-10
Decision needed: approve the build, and the accounts and spending caps
  it needs.
Recommendation: one small app on Google Cloud in Montréal, written in
  Python, using the Claude API for the report. Bench-built first with no
  accounts and no spend; accounts only when the code is ready to run.
Expected cost: hosting likely $0/month (inside Google's free tiers);
  about US$0.50 per report in AI; about US$5-10 of AI testing before G3.
Caps proposed: Google Cloud budget alert CAD $10/month; Anthropic
  spending limit US$25/month.
Brandon's time: about 1.5h to create three accounts (in the G2 estimate).
Reply: approve · approve with changes · hold
```

---

## 1. What we're building, in one picture

```
 CEO buys in the Labs store (Squarespace)
        │
        │  every 10 min the app asks Squarespace: any new diagnostic orders?
        ▼
 ┌────────────────────── the app (Google Cloud, Montréal) ──────────────────────┐
 │                                                                               │
 │  New order ──► make the company's private link ──► email the setup kit        │
 │                                                                               │
 │  Drop-box page ◄── leaders paste their summary                                │
 │     • checks the format  • strips name and role  • counts  • stores           │
 │                                                                               │
 │  Status page ──► "4 of 6 received" (nothing else)                             │
 │                                                                               │
 │  Window closes (3+ in) ──► Claude writes the report ──► automatic checks      │
 │                                 │                         │ pass     │ fail   │
 │                                 │                         ▼          ▼        │
 │                                 │                  email PDF    hold + alert  │
 │                                 │                  to CEO       Brandon       │
 │                                 │                         │                   │
 │                                 └────────► delete summaries; log date + count │
 │                                                                               │
 │  14 days later ──► one check-in email                                         │
 └───────────────────────────────────────────────────────────────────────────────┘
```

Think of it as a locked mailroom that only opens on a schedule. Squarespace is the front counter. The app is the back room. Claude is the clerk who writes the letter. Nobody walks in and reads the mail.

## 2. The parts, and why each one

| Part | Choice | Why |
|---|---|---|
| Where it runs | **Google Cloud Run, Montréal** (`northamerica-northeast1`) | Runs only when someone uses it. No server to look after. Keeps stored data in Canada. |
| Where it stores things | **Firestore, Montréal** | Simple storage, one free database per project. Holds orders, stripped summaries (until delivery) and kept reports. |
| Scheduled jobs | **Cloud Scheduler** | Checks for new orders, closes windows, sends check-in emails. Three jobs are free. |
| Keys and passwords | **Secret Manager** | Never in the repo (Mack refuses to hardcode secrets). Six are free. |
| Writing the report | **Claude API, model Claude Opus 5.5** | The synthesis agent from deliverable 4, plus a second call for the name check. Refusal fallback switched on so a declined request retries on another model. |
| Knowing someone bought | **Squarespace Orders API**, checked every 10 minutes | Works with a plain API key on Core and higher plans. No webhook or Zapier needed. |
| Email | **Your Google Workspace mailbox, or a sending service** | Question 2 below. |
| The report PDF | Made by the app itself | No extra service. Iris styles it at G4. |
| The code | Python, in `labs/rotor-alignment-diagnostic/build/` | Plain and well supported. A `build/README.md` explains how to run it. |
| Web address | The app's default Google address for the prototype | A `diagnostic.franklinkinetics.com` address is decided before Release, not now. Ugly first. |

## 3. Costs

All prices checked 2026-11-10 from the providers' own pages. Google prices are in US dollars.

**Fixed, per month**

| Item | Free allowance | What we'll use | Expected cost |
|---|---|---|---|
| Cloud Run | 2 million requests, 180,000 vCPU-seconds, 360,000 GiB-seconds a month | Hundreds of requests | $0 |
| Firestore | 1 GiB stored; 50,000 reads, 20,000 writes, 20,000 deletes a day | Tiny | $0 |
| Cloud Scheduler | 3 jobs per billing account | 3 jobs | $0 |
| Secret Manager | 6 active secrets | 4 or 5 | $0 |

The free tiers cover this volume with a lot of room. A budget alert at **CAD $10/month** tells you if that ever stops being true.

**Per report**

| Item | Basis | Cost |
|---|---|---|
| Claude Opus 5.5 | $4 per million tokens in, $20 per million out (Anthropic's published rates). About 8,000 tokens in and 15,000 out for the report, plus a small check call | **about US$0.50** |
| Squarespace card fee | 2.9% + $0.30 on Core (verified 2026-11-10) | about $23 per $790 sale |

**One-time testing before G3:** about **US$5–10** of Claude calls, to run the Larchmere and trap blocks many times.

Sources: https://cloud.google.com/run/pricing · https://cloud.google.com/firestore/pricing · https://cloud.google.com/scheduler/pricing · https://cloud.google.com/secret-manager/pricing · https://www.squarespace.com/pricing · Squarespace API availability by plan: https://support.squarespace.com/hc/en-us/articles/236297987-Squarespace-API-keys

## 4. Order of work

| Step | What happens | Accounts or spend? | Brandon |
|---|---|---|---|
| **1. Bench build** | All the code, with the AI replaced by a stand-in. Tests for the format check, name stripping, counting, the 3-leader rule, deletion and the trap blocks (test plan Stage 1). | **None** | — |
| **2. Accounts** | You create a Google Cloud project with billing and the $10 alert, an Anthropic API account with the $25 cap, and a read-only Squarespace Orders API key. The crew gives click-by-click steps. Keys go straight into Secret Manager. | Accounts, caps set | ~1.5h |
| **3. Real AI on the bench** | The synthesis agent runs on Larchmere and the trap blocks. Every report is checked against the test plan. | ~US$5–10 | — |
| **4. Deploy** | The app goes up in Montréal. The diagnostic is added to the Labs store as a hidden product, so it can be tested without being on sale. | ~$0 | ~15 min |
| **5. G3 prototype** | Your solo run (test plan Stage 2): set up the interviewer, take it as 3–5 invented leaders, read the report. | ~US$1 | ~2.5h |

Steps 1 and 3 are logged in the friction log as they go. Nothing goes on sale until G7.

## 5. What could go wrong, and the plan for it

| Risk | Plan |
|---|---|
| Your Squarespace plan is below Core, so there's no Orders API | Fallback: the setup kit email from Squarespace includes a "start your diagnostic" link, and the CEO enters their order number. Still zero Brandon time. |
| Claude occasionally declines a request | Refusal fallback retries on another model automatically. If it still fails, the report is held and you're alerted. |
| Google's free tier changes | The CAD $10 alert catches it. |
| A bug leaks a name | The second AI check and the plain word search both run before any email goes out. Trap block T1 tests it. |

## 6. Questions for Brandon

1. **Squarespace plan:** which plan is the site on? The Orders API needs Core or higher.
2. **Email:** is contact@franklinkinetics.com a Google Workspace mailbox? If yes, the app sends from it at no extra cost. If not, Mack prices a sending service.
3. **Approve:** the build, the three accounts, and the caps (Google CAD $10/month alert, Anthropic US$25/month limit)?

## 7. Approved · 2026-11-10

Squarespace plan: Core (Orders API available). Email: contact@franklinkinetics.com is Google Workspace. Build, accounts and caps approved.
