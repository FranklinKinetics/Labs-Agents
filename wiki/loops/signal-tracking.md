# Loop: signal tracking

- **Trigger:** every Sunday, before the weekly review.
- **Owner:** Ines. **Model:** Haiku.
- **Brandon's minutes:** 1. He sends one number (Lab page views) until analytics is connected.

## The Signal ladder, per Lab
`visits → contacts → calls → clients`

| Rung | Source | How Ines counts it |
|---|---|---|
| Visits | Squarespace Analytics, page views per Lab page | Brandon pastes the numbers into the queue reply (1 min). Replace with a direct feed when one is connected. |
| Contacts | Replies and forms that name a Lab or carry a `ref`; replies to outreach notes | Gmail search on `ref=` and on the "Which Lab or email brought you here?" field; prospect-sheet replies |
| Calls | Bookings on the call booking page (`ref` in the booking answers), plus calls booked by reply | Google Calendar, bookings titled "FK call" |
| Clients | Signed paid work | Brandon confirms; credited to the first touch |

## Steps
1. Count each rung for every live Lab and for the active discovery test, for the week and month to date.
2. Update `signals` on each lab card (`labs/<slug>/lab.yaml`).
3. **First-touch credit.** A contact or call is credited to the first `ref` that reached that firm. Phone or plain-email replies carry no ref, so Ines matches them by firm against the private prospect sheet.
4. Hand the totals to the weekly review.

## Rules
- Counts only in the repo. No names, emails or firm names.
- Unknown is written as "unknown", never guessed.
