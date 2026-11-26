# Ontology

The shared vocabulary of Franklin Kinetics Labs. Every persona uses these words with exactly these meanings. If a new concept keeps coming up, add it here and log it in the weekly review; don't coin terms silently.

## The core chain
```
Spark ──► Lab ──► Page ──► Release ──► Signals ──► Debrief ──► Living Models
                                          │                          │
                                          ▼                          │
                                  the Call Path (below)               │
   ▲                                                                  │
   └──────────── new Sparks, revised Price Model ◄────────────────────┘
```

## The Call Path
Approved by Brandon, 2026-11-26. **Why Labs exist: every Lab leads to a call.**
```
Outreach note / Lab page / referral
        │
        ▼
Hook: the Lab, used in 1–5 minutes on a phone
        │
        ▼
Contact: a reply (often "reply with one number") or a form, carrying a ref
        │
        ▼
Call: 20 minutes, booked into Brandon's fixed evening slots
        │
        ▼
State Map Diagnostic (consulting, unpriced)
        │
        ├──► Automation (≥ $1k/month, runs unattended, never priced in public)
        └──► Rotor engagement (Distillation or Beta, unpriced)
```

| Term | Meaning | Lives in |
|---|---|---|
| **Call Path** | The route above, from a Lab to paid work. Every lab card names its Call Path: which paid work it leads to, and how. | lab card `call_path` |
| **Hook** | The first thing an owner uses: one minute, a phone, no setup. A Lab may have a deeper second layer behind it. | the Lab |
| **Business-owner path** | The paragraph on every Lab page headed "If you run a firm of 20–200 people": what this looks like as a weekly routine in their firm. Describes, never promises a result. | Lab page |
| **CTA** | The one call to action on a Lab page: "Book a 20-minute call", linked with `?ref=<slug>`. Exactly one per page. | Lab page |
| **ref** | A short code on every link (`?ref=<lab-slug>` or a per-prospect code) so a contact or call can be credited to its first touch. | links; private prospect sheet |
| **Signal ladder** | Four counts per Lab: **visits → contacts → calls → clients**. Replaces the old free-text Signal. | lab card `signals` |
| **Contact** | A reply, form or message that names a Lab or carries a ref. | Signal ladder |
| **Call** | A booked conversation with Brandon. | Signal ladder |
| **Client** | Signed paid work, credited to its first touch. | Signal ladder |
| **State Map Diagnostic** | Consulting deliverable: find the steps where invoices and jobs wait with no one responsible. Unpriced. Brandon's time is capped per diagnostic. | consulting files (private) |
| **Automation offer** | Paid AI automation, at least $1,000/month per client, that runs without daily babysitting (guardrail 16). Never priced in public. | consulting |

## Nouns

| Term | Meaning | Owner | Lives in |
|---|---|---|---|
| **Schwerpunkt** | The single point of main effort for all Labs. One sentence, in `CLAUDE.md`. | Brandon | `CLAUDE.md` |
| **Spark** | A raw idea. Anyone can add one. Not yet approved for work. | Ines (queue) | `labs/sparks.md` |
| **Brief** | Mack's short feasibility note for a Spark: sources, licences, Call Path, Ines's price read. Optional for small Labs. | Mack + Ines | `labs/<slug>/brief.md` |
| **Lab** | A Spark Ines has started, with a lab card and a Call Path. (Brandon's approval comes at G1 Release, not before the build.) | Ines | `labs/<slug>/` |
| **Lab card** | The structured record of a Lab: status, proofs, hours, price, signals. | Ines | `labs/<slug>/lab.yaml` |
| **Four Proofs** | Speed, Abundance, Craft, Goodwill. Every Lab must score on all four, plus a Call Path. | Ines | lab card |
| **Rotor Lesson** | The one management idea this Lab demonstrates, in one sentence, on the Lab page. No Lesson, no Lab. | Fenn | lab card |
| **Build** | The working product, starting ugly. | Mack | `labs/<slug>/build/` |
| **Look** | The visual direction and the one memorable image. | Mack | `labs/<slug>/look/` |
| **Offer** | What a customer can get: a **Paid layer** and, where it genuinely helps, a **Free layer**. The free layer is optional. | Ines | lab card |
| **Package** | The final Offer: format, what's included, price, checkout, refund terms. | Ines | lab card |
| **Page** | The Lab's store page, built to the eight-point page checklist (`wiki/loops/lab-release.md`). Replaces "Story". | Fenn | `labs/<slug>/page.md` |
| **Clearance** | Vera's written check against the guardrails and the page checklist. Required before anything reaches G1. Replaces the retired gates. | Vera | `labs/<slug>/clearance.md` |
| **Release** | Something goes public: a Lab page, a price, an outreach batch. Brandon passes G1 and presses the button. | Brandon | lab card |
| **Signal** | What happened after Release, counted on the Signal ladder (visits → contacts → calls → clients), plus sales. | Ines | lab card |
| **Debrief** | Ines's review about 4 weeks after Release: did it produce contacts and calls? Reported in the weekly review; no gate. | Ines | `labs/<slug>/debrief.md` |
| **Living Model** | A belief we hold until evidence replaces it (Rotor's word for "assumption"). | Ines | `models/living-models.md` |
| **Price Model** | The Living Models specific to pricing and packaging. | Ines | `models/price-model.md` |
| **Friction** | Anything that slowed a build. Logged so the next Lab goes faster. | Everyone | `logs/friction-log.md` |
| **Gate** | One of two checkpoints where the crew stops for Brandon: **G1 Release** (public) and **G2 Money** (spend or client commitment). | Ines | `canon/gates.md` |
| **Gate packet** | One phone screen: a verdict, three bullets at most, one decision. | Ines | `QUEUE.md`, then `logs/gates-log.md` |
| **Queue** | Everything waiting on Brandon, clearable in under an hour a week. | Ines | `QUEUE.md` |
| **Weekly review** | Ines's Sunday one-screen report: verdict, three bullets, one decision; detail below. | Ines | `logs/weekly/` |
| **Loop** | A recurring workflow, written down with its owner, model, trigger and Brandon's minutes. | Ines | `wiki/loops/` |
| **Discovery test** | A time-boxed test of one channel, with a pass/fail number set in advance. | Ines | `wiki/loops/discovery-outreach.md` |
| **Guardrail** | A hard limit. Vera enforces; only Brandon can change one. | Vera | `canon/guardrails.md` |
| **Decision** | Anything Brandon decides, with date and source. The record of truth. | Ines | `logs/decisions.md` |

## Rotor Product terms
Approved by Brandon at RP2, 2026-11-10. These are consulting terms, not Lab terms. *Intake*, *Mirror day* and *waiting room* were retired on 2026-11-11, when the Distillation was reshaped.

| Term | Meaning | Lives in |
|---|---|---|
| **Wave 0** | A company's alignment diagnostic results, used with its consent as the program's starting point. | `rotor/product/` |
| **Override log** | Brandon's private record of each change he makes to an AI draft, by step and reason only, with no client content. | Brandon's private library |

## Lab statuses
`spark` → `building` → `paged` → `cleared` → `released` → `debriefed`
Side states: `held` (paused, with a reason), `killed` (with a one-line reason; kept for the record).
Retired 2026-11-26 with the old gates: `briefed`, `approved`, `dressed`, `packaged`, `storied`.

## What belongs in Labs
Labs is the Franklin Kinetics storefront: products people take off the shelf and use without any of Brandon's time. Anything that needs Brandon's consulting time is consulting, not a Lab.

## Audiences
- **Household**: buys the product to use at home (e.g. Automatic Groceries).
- **Business**: buys a self-serve product to use in their company (e.g. the alignment diagnostic).
- **SME owner**: the real target. Owner- or founder-led firm, 20–200 people, in Regina and Saskatchewan first. Sees a Lab, for home or for work, thinks "imagine this in my company", and calls.
- **Trades owner**: the first SME segment (from 2026-11-26): trades and construction firms, 20–200 people, where invoices wait.
- **Civic**: Regina residents and businesses who benefit from public data made legible.

A Lab can sell to one audience while its Story speaks to another. That bridge is Fenn's job.

## Words we avoid
- "Pilot" for a client engagement (confusing given Brandon's flying career). Use **Rotor Beta**.
- "Assumption." Use **Living Model**.
- "Drag." Use **Friction**.
- "One-page strategy." Rotor **distills** strategy.
