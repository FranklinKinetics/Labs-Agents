# Loop: weekly review

- **Trigger:** every Sunday (or the first crew session after it).
- **Owner:** Ines. **Model:** Haiku compiles; Ines (Sonnet) writes the verdict line only if the week had a real decision.
- **Brandon's minutes:** under 10.

## Steps
1. Run the [signal tracking](signal-tracking.md) loop first.
2. Copy `logs/weekly/_template.md` to `logs/weekly/YYYY-Www.md` (ISO week).
3. Fill the **top screen** (everything above the line): one verdict, at most three bullets, one decision.
4. Fill everything below the line: the Signal ladder table, the discovery test's tally, hours, things the crew did without asking ("unsure → did it"), Vera's clearances, friction, and loop changes.
5. If the decision is a G1/G2 item, it also goes in `QUEUE.md`. Otherwise it's a plain question with a default ("If no answer, we'll …").
6. Commit: `weekly: YYYY-Www`.

## Rules
- Nothing above the line that Brandon doesn't need. If there's no decision, write "Decide: nothing this week."
- Numbers come from the Signal ladder or the prospect sheet's counts, never estimates.
- Name no prospect; use counts and ref codes.
