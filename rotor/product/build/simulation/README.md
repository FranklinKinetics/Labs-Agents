# FICTIONAL TEST COMPANY

**Never shown to anyone. Never used as a result, case study or example (guardrails 4 and 5).**
Everything in this folder is invented: the company, the people, the answers. Do not quote it, cite it or describe it to a client, a prospect or on the website.

---

# Stage 1 simulation kit: how to run it

**Purpose:** with no friendly company available, test the whole build (A1 to A7, and A8 on a few dilemmas) and time Brandon's real work, using Tamarack Ridge Mechanical Services (fictional) and four AI-played leaders. See `../checklists/dry-run-plan.md`, stage 1.

**What you need:** an AI account for the interviewer, one more chat (or a second account) for the leader, and a private test project in your own account for A2 to A7. Name the test project `TEST-TRMS`, so it can never be mistaken for a client.

**What this cannot test:** whether leaders feel heard, real politics, the Mirror, the 4 pm calls. There is no Mirror: you write the draft sheet yourself.

## Files

| File | Use |
|---|---|
| `company-brief.md` | Facts every persona shares. Paste it into every leader chat. |
| `leader-1-ceo.md` to `leader-4-finance-admin.md` | One persona each. |
| `test-traps.md` | The traps planted, and the agent rule each tests. Tick it as you go. |

## Step 1: Set up the interviewer (A1)

1. Create a Claude Project called `TEST-TRMS interviewer` (any platform works; see the table in `rotor/interviewer-pack.md`).
2. Paste the core instructions from `rotor/interviewer-pack.md`. Replace `[COMPANY]` with `Tamarack Ridge Mechanical Services (TEST, fictional)`.
3. Put the Wave 1 file in the project knowledge.
4. Run the "Before you hand it over" checklist from the interviewer pack once, as your install check (this is T2's install check; time it).

## Step 2: Run each leader's wave 1 session

Do one leader at a time. Start a fresh chat per leader, per wave. Pick **one** way:

### Option A (recommended): single role-play chat
The simplest. One chat plays both sides.
1. Open a new chat **inside the interviewer project**.
2. Send this first, then the leader file's full text and `company-brief.md`:
   > "For this test only: I will paste a leader persona. You will play the interviewer exactly as your project instructions say. I will type the questions you ask to the persona and bring back its answers." 
   
   Caution: one AI playing both sides tends to go easy on itself. If it starts answering for the leader, stop and use Option B.
3. If your platform lets the project's AI role-play the leader too, paste: "Now also answer as the leader below, in the next message. Do not write the interviewer's lines." Prefer Option B whenever you can.

### Option B: two chats, copy between them
Truer to a real session, more copying.
1. **Chat 1** (the interviewer project): start the session. The interviewer asks for name and role.
2. **Chat 2** (plain chat, no project): paste `company-brief.md`, then one leader file. Add: "Answer as this person. Wait for my first message."
3. Copy each interviewer question into Chat 2; copy the persona's answer back into Chat 1. Do not edit either side, except to type the persona's pre-planned requests (below) if it forgets.
4. Repeat until the interviewer produces the summary block.

> Recommendation: use **Option B for leaders 1 and 3** (the two with the hardest traps), **Option A** for the others. Note which you used in the log.

## Step 3: Collect summary blocks

Save each `=== ROTOR INTERVIEW SUMMARY ===` block as a text file (`TRMS-L1-w1.txt` and so on), and the whole transcript beside it. Fix any format fault once (log it as a fault in `test-traps.md`). Check the "Leave out" field against each persona's leave-out item.

## Step 4: Run A2 to A7 as for a real company

In the `TEST-TRMS` project, in this order, as in the agents README: A2 (after each block), A3 (wave 2 files), run waves 2 and 3 the same way as wave 1 using the persona's "wave 2 / wave 3" notes, A4, then A5, then A6, then A7. Run A8 on two or three dilemmas. Do your **real** review checklists in `../checklists/review-checklists.md`: **T4, T5, T6 and T9**. For T6, write your own view first, then read A5. No Mirror: write the draft sheet yourself, in your own words.

## Step 5: Time yourself

Start a timer at the start of each touchpoint; stop for breaks. Fill the log the same day.

| Touchpoint | Budget (min) | Actual (min) | Over / under | Notes |
|---|---|---|---|---|
| T2 Install check (the simulation's share) | 25 | | | |
| T4 Transcript reading (all waves, four leaders) | 140 | | | |
| T5 Synthesis, wave 2 file, divergence summary edits | 95 | | | |
| T6 Choosing the candidates | 105 | | | |
| T9 Sheet, script, red-team | 120 | | | |
| **Total for these** | **485** | | | |

**Exit test (dry-run plan):** each of T4 to T6 and T9 within 30% of budget, or re-estimate before RP4 pricing work. Note that four leaders is fewer than the real company's size, so scale T4 by the number of transcripts read, and say so in the notes. A transcript here is a simulated person: your reading may be faster or slower than real. Treat that as a known bias.

## Step 6: Close out

- Tick `test-traps.md`. Every trap must be handled correctly after **at most one fix**. A5 must never rank.
- Log every faulty agent response as a Friction entry in `logs/friction-log.md` (Ines does this).
- When done, delete the `TEST-TRMS` project and the chats. Keep only your minutes and the fault list. Delete the summary blocks, syntheses and sheet, or file them in a folder marked FICTIONAL. Never reuse them.
