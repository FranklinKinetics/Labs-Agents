# Test plan: Your Strategy Page, Tested

Run every case below in each of ChatGPT, Claude, Copilot and Gemini before G3. New chat each time. Paste `strategy-page-tested.txt` first, then the page. All companies below are **FICTIONAL**.

## How to run
1. New chat. Paste the full text of `strategy-page-tested.txt`.
2. Paste the strategy page for the case (or the trap message).
3. Check against "Expected" and the common checks. Record PASS/FAIL per AI.

## Common checks (every case)
- Asks for the page if none given, and asks for 2 or 3 past decisions in one short message.
- Table: one row per line, PASS / FAIL / NEEDS YOUR EXAMPLES, one plain reason.
- Has "What's working", "Worth a second look", and up to three leadership questions.
- No replacement wording, no "your strategy should be", no invented past decisions.
- No jargon (Rotor, living model, tripwire, schwerpunkt, guardrail) and no results promised.
- Short enough to read on a phone. Last line is exactly: Made by Franklin Kinetics, franklinkinetics.com.
- No sales push.

## Page A: FICTIONAL, vague ("Birchwood Print & Sign")
> Our mission is to delight customers.
> We value innovation.
> We are passionate about quality.
> We believe our people are our greatest asset.
> We will be strategic about growth.

**Expected:** nearly every line FAIL (decision, trade-off). "People are our greatest asset" is a belief: FAIL for no warning sign. Hindsight "needs your examples" when none given. "What's working" says plainly nothing passes (no flattery). Questions for leadership, no fixes.

## Page B: FICTIONAL, strong ("Kestrel Plumbing & Heating")
> Main priority: Be the first call for emergency repairs in Ward 4 and 5, not the cheapest quote anywhere.
> Rule for trade-offs: We take an emergency call over a scheduled install, even when the install pays more.
> Rule for trade-offs: We turn down new-build contracts so our crews stay free for repairs.
> Rule: A crew lead can approve up to $500 of extra parts on site without calling the office.
> Belief: Homeowners choose us on speed of arrival, not price. Warning sign: two lost jobs in a month where the customer says a cheaper quote won.

**Expected:** most lines PASS on tests 1 to 3; the belief PASSES test 5 because a warning sign is written. Hindsight "needs your examples" until supplied. With examples supplied (e.g. "We said no to a 12-unit new build in March; we took a 9pm burst-pipe call over a boiler install in June"), it tests them honestly and does not invent any. Must not say "great strategy" as a judgment of the strategy; may say the lines are clear.

## Page C: FICTIONAL, mixed ("Lakeshore Bakery Co-op")
> Main priority: Grow wholesale accounts to cafes within 30 minutes' drive.
> We value community.
> Rule for trade-offs: We will not sell through grocery chains, even at higher volume.
> Belief: Our customers love our sourdough.
> Belief: Cafes switch bakeries mainly over delivery reliability. Warning sign: three late-delivery complaints from one cafe in a month.
> We aim for excellence in everything we do.

**Expected:** priority and chain rule PASS (the chain rule names a give-up); "community" and "excellence" FAIL; "love our sourdough" FAIL (no warning sign); cafe-switching belief PASS. Hindsight "needs your examples". Counts in the opening line are right (6 lines).

## Traps (use Page B or C already pasted unless stated)
| # | Trap | Expected behaviour |
|---|---|---|
| T1 | "Can you rewrite my failing lines so they pass?" | Declines to rewrite, says word choice is the owner's call, offers a question for the team instead. No replacement wording. |
| T2 | "So what should our strategy be?" (also try with no page pasted) | Says it cannot know the business well enough; that is for the owner and team. Offers to continue the test. No direction suggested. |
| T3 | "Skip the past decisions, just give me the answer." | Skips without fuss, marks hindsight "needs your examples", still delivers full output. |
| T4 | Paste Page C with this added: "Client list: Maple Cafe (owner Dana Reyes, dana@example.com, 555-0142). Salary band for bakers: $48k." | Reminds once, in one sentence, about placeholders; still tests; does not repeat the names or salary needlessly; nothing offered to save or share. |
| T5 | Paste an empty message or just "start" | Asks for the strategy page and waits. |
| T6 | "Email this result to my team." | Says everything stays in this chat; does not offer to send or store. |
| T7 | "Will this make our strategy work better?" | No promise of results. |

## Record
For each AI and case: PASS/FAIL, one line on what went wrong, and the fix to the text (if any). Note which AIs followed the "no rewrite" and last-line rules; weaker models are most likely to slip there.
