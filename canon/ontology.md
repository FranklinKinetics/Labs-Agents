# Ontology

The shared vocabulary of Franklin Kinetics Labs. Every persona uses these words with exactly these meanings. If a new concept keeps coming up, propose it to Brandon at a gate; don't coin terms silently.

## The core chain
```
Spark ──► Lab ──► Offer ──► Release ──► Signal ──► Debrief ──► Living Models
                 (Free layer + Paid layer)                          │
   ▲                                                                │
   └──────────── new Sparks, revised Price Model ◄──────────────────┘
```

## Nouns

| Term | Meaning | Owner | Lives in |
|---|---|---|---|
| **Schwerpunkt** | The single point of main effort for all Labs. One sentence, in `CLAUDE.md`. | Brandon | `CLAUDE.md` |
| **Spark** | A raw idea. Anyone can add one. Not yet approved for work. | Ines (queue) | `labs/sparks.md` |
| **Brief** | Juno's feasibility write-up for a Spark, with Sol's first price read. | Juno + Sol | `labs/<slug>/brief.md` |
| **Lab** | A Spark Brandon approved at G2. Has a lab card. | Ines | `labs/<slug>/` |
| **Lab card** | The structured record of a Lab: status, proofs, hours, price, signals. | Ines | `labs/<slug>/lab.yaml` |
| **Four Proofs** | Speed, Abundance, Craft, Goodwill. Every Lab must score on all four. | Ines | lab card |
| **Rotor Lesson** | The one management idea this Lab demonstrates, in one sentence. No Lesson, no Lab. | Fenn | lab card |
| **Build** | The working product, starting ugly. | Mack | `labs/<slug>/build/` |
| **Look** | The visual direction and the one memorable image. | Iris | `labs/<slug>/look/` |
| **Offer** | What a customer can get: a **Free layer** (goodwill) and a **Paid layer** (value capture). | Sol | lab card |
| **Package** | The final Offer: format, what's included, price, checkout, refund terms. | Sol | `labs/<slug>/package.md` |
| **Story** | The Lab page copy and Substack note that bridge the Offer to the Rotor Lesson. | Fenn | `labs/<slug>/story.md` |
| **Clearance** | Vera's written check against the guardrails. Required before Release. | Vera | `labs/<slug>/clearance.md` |
| **Release** | The Lab goes live in the Labs store. Brandon presses the button. | Brandon | lab card |
| **Signal** | What happened after Release: sales, conversion, replies, conversations, uses. | Ines | lab card |
| **Debrief** | Review at ~2 weeks after Release. What worked, what didn't, what we now believe. | Ines | `labs/<slug>/debrief.md` |
| **Living Model** | A belief we hold until evidence replaces it (Rotor's word for "assumption"). | Ines | `models/living-models.md` |
| **Price Model** | The Living Models specific to pricing and packaging. | Sol | `models/price-model.md` |
| **Friction** | Anything that slowed a build. Logged so the next Lab goes faster. | Everyone | `logs/friction-log.md` |
| **Gate** | A checkpoint where the crew stops for Brandon's decision. | Ines | `canon/gates.md` |
| **Gate packet** | The short summary Brandon decides on at a gate. | Ines | posted in session, logged |
| **Guardrail** | A hard limit. Vera enforces; only Brandon can change one. | Vera | `canon/guardrails.md` |
| **Decision** | Anything Brandon decides, with date and source. The record of truth. | Ines | `logs/decisions.md` |

## Lab statuses
`spark` → `briefed` → `approved` → `building` → `dressed` → `packaged` → `storied` → `cleared` → `released` → `debriefed`
Side states: `held` (paused at a gate), `killed` (with a one-line reason; kept for the record).

## Audiences
- **Household**: buys the product to use at home (e.g. Automatic Groceries).
- **SME owner**: the real target. Owner- or founder-led firm, 20–200 people. Sees a household product and thinks "imagine this in my company."
- **Civic**: Regina residents and businesses who benefit from public data made legible.

A Lab can sell to one audience while its Story speaks to another. That bridge is Fenn's job.

## Words we avoid
- "Pilot" for a client engagement (confusing given Brandon's flying career). Use **Rotor Beta**.
- "Assumption." Use **Living Model**.
- "Drag." Use **Friction**.
- "One-page strategy." Rotor **distills** strategy.
