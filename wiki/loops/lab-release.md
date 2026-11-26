# Loop: Lab release

Replaces the old lifecycle with gates G1–G8 (retired 2026-11-26).

- **Trigger:** a Lab build is ready, or a live Lab page needs to change (including the retrofit of shipped Labs).
- **Owner:** Fenn writes, Vera clears, Ines packets. **Models:** Fenn on Opus, Vera on Sonnet, Ines on Sonnet.
- **Brandon's minutes:** one G1 packet (about 10 minutes), then he publishes on Squarespace.

## Flow
```
Spark ─► Build (Mack) ─► Page (Fenn) ─► Clearance (Vera) ─► G1 Release (Brandon) ─► Signals ─► Debrief at 4 weeks (Ines)
```

## The page checklist (Vera checks all eight)
1. **The job in the owner's words** (headline).
2. **The price**, or "Free".
3. **What it does in one to five minutes**, and what you need to hand. Phone-first.
4. **Speed**: honest build hours, from the lab card.
5. **The Rotor Lesson**, one sentence, plain words.
6. **The business-owner path**: a short paragraph headed *"If you run a firm of 20–200 people"*, saying what this would look like as a weekly routine in their firm. It describes what it does, never what it earns.
7. **One call to action**: "Book a 20-minute call", linked to the booking page with `?ref=<slug>`, and "or just reply with a question" beside it. Nothing else competes (no newsletter pitch, no second offer). The buy or download button is the product, not a CTA.
8. **None of these:** a consulting or automation price, "$1,000/month", an ROI promise, Brandon's military role or flying.

## Steps
1. Mack marks the lab card `status: building` → done, with hours and sources.
2. Fenn writes `labs/<slug>/page.md` to the checklist and sets `status: paged`.
3. Vera writes `labs/<slug>/clearance.md`, fixes what she can, sends the rest back, and sets `status: cleared`.
4. Ines posts a G1 packet in `QUEUE.md`.
5. On a pass, Brandon publishes; Ines records the URL, the date and `status: released`.
6. At 4 weeks Ines writes `debrief.md`: did the Lab produce contacts and calls? Living Models are updated, and the result goes in the weekly review. No gate.
