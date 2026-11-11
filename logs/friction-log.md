# Friction log

Anything that slowed a build. Logged so the next Lab goes faster. Ines reviews it at each Debrief.

| Date | Lab | Who | Friction | Fix or idea |
|---|---|---|---|---|
| 2026-11-10 | rotor-alignment-diagnostic | Sol, Ines | Price comparables and Squarespace fees blocked by the environment's network policy; Sol could cite search summaries only. Brandon approved five hosts, but the session's safety checks then blocked both re-check routes. | Verify comparables before the page goes live; consider adding common research hosts to the environment up front for pricing work. |
| 2026-11-10 | rotor-alignment-diagnostic | Mack | The approved check sheet has the line "Any result, savings or ROI claim", so a plain search for the banned word ROI over the whole agent output would hold every report. | Search the report only, not the check sheet (done in `checks.py`). Worth a one-line note in 04-synthesis-agent.md. |
| 2026-11-10 | rotor-alignment-diagnostic | Mack | Test plan T2 says the drop-box "flags" a colleague named in a block. The drop-box only knows the submitter's own name, so it can't. | Left to the interviewer, the agent and the second check; test plan wording to be corrected. |
| 2026-11-10 | rotor-alignment-diagnostic | Mack | Canon lacks the real Start a conversation URL, the sender mailing address the check-in email needs, and how Squarespace delivers checkout answers in an order. | Config placeholders with a `problems()` list; Squarespace mapping to be confirmed against a test order in Step 2. |
| 2026-11-10 | rotor-alignment-diagnostic | Mack | The sample report carries a "Fictional sample" label and a `[link]` placeholder, so it can't be used as a fixture as it stands. | Fixture builder in `tests/conftest.py` edits those two things from the sample file, so the fixture tracks the source. |
