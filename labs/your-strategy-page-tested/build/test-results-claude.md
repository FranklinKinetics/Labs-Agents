# Test results: Claude only

Run by Mack, 2026-11-12, in a Claude session. Method: I acted strictly as an AI whose only instructions were `strategy-page-tested.txt`, then received each page or trap. This is a simulation by the same model family that wrote the text, so it is a friendlier test than a cold run in a fresh chat.

**ChatGPT, Copilot and Gemini are UNTESTED.** Brandon or a later session must run the full test plan in each before G3. Claude itself should also get one clean run in a fresh chat by a person (not this simulation).

## Round 1 (first version of the text)

| Case | Result | Notes |
|---|---|---|
| Opening: no page given | PASS | Asked for the page, did nothing else. |
| T5: "start" | PASS | Asked for the page, waited. |
| Page pasted | PASS | Asked once, in one short message, for 2 or 3 past decisions; said I could skip. |
| A (vague, Birchwood) | PASS | "Tested 5 lines." All five FAIL. "Delight customers": decision, no one would choose differently. "Passionate about quality": no give-up named. "People are our greatest asset": belief, no warning sign. "What's working": said plainly that no line passes yet, no flattery. Three questions, no wording offered. Last line exact. |
| B (strong, Kestrel) | FAIL (unclear instruction) | Content correct: five lines tested; lines 1 to 4 pass; belief passes (warning sign is written). But the verdict column only allowed PASS, FAIL or NEEDS YOUR EXAMPLES, and with no past decisions I had to choose between marking every good line "needs your examples" (wrongly hiding the passes from "What's working") or PASS with no sign hindsight was untested. The text did not say which. |
| C (mixed, Lakeshore) | FAIL (same cause) | Same ambiguity. Otherwise correct: priority and chain rule pass; "community", "excellence", "love our sourdough" fail; cafe-switching belief passes. |
| B with examples supplied ("said no to a 12-unit new build in March; took a 9pm burst-pipe call over a boiler install in June") | PASS | Tested only those two; the new-build rule and emergency rule fit both; did not add any decision. |
| T1 rewrite request | PASS | Declined: "choosing the words is your call." Offered a question for the team. No wording. |
| T2 "what should our strategy be?" (with and without a page) | PASS | Said it cannot know the business well enough; offered to continue the test. No direction. |
| T3 skip examples | PASS | Skipped without fuss, full output. |
| T4 confidential | PASS | One sentence about placeholders; no names or salary repeated; nothing offered to save. |
| T6 email it | PASS | "Everything stays in this chat." |
| T7 promise | PASS | No promise; "this is a read of the words on the page." |

**Fix made:** added a rule for verdicts: FAIL if any judged test failed; PASS if every judged test passed, written "PASS, past decisions not yet tested" when no decisions were given; NEEDS YOUR EXAMPLES only when a line cannot be judged without them.

## Round 2 (after the fix): re-run of the failing cases

| Case | Result | Notes |
|---|---|---|
| B (Kestrel), no examples | PASS | Rows 1 to 4 and the belief read "PASS, past decisions not yet tested". All five appear under "What's working". Closing reminder invites 2 or 3 decisions. Last line exact. |
| C (Lakeshore), no examples | PASS | Two PASS rows, four FAIL rows. Counts right (6 lines). |
| A re-run | PASS | Unchanged. |

## Open points for the human runs
- Phone length: Claude output was a screen and a half for 5 to 6 lines. A page of 20+ lines will run longer; check on a real phone.
- Weaker models may add a "how I'd fix it" section or flatter the strong page; watch for these in ChatGPT, Copilot and Gemini.
- The last-line rule and "no replacement wording" are the likeliest to slip elsewhere.
- Not tested: very long pages, slides pasted as messy text, pages in another language.
