# Truck Note to Invoice · build v0 (Mack, 2026-11-26)

**What it is:** one instruction text the owner (or a tech, or the office) pastes into the AI they already use: ChatGPT, Claude, Copilot or Gemini, all of which accept a phone photo. They send a photo of a work order or a dictated note, and get back an invoice to check and send, with every gap flagged. Nothing is hosted, nothing comes back to Franklin Kinetics, and it collects nothing.

**Why this tech:** the phone camera plus the owner's own AI is the whole stack. It needs no server, no account with us and no upkeep. Same pattern as Your Strategy Page, Tested.

## Packages (same instructions, three wrappers)
| Package | For | File | Setup for the owner |
|---|---|---|---|
| **Claude skill** | Claude users | `skill/truck-note-to-invoice.zip` (source: `skill/truck-note-to-invoice/SKILL.md`) | Download the zip; in Claude, Settings → Capabilities → Skills → upload. After that Claude uses it on its own whenever they share a work order. It can also offer a PDF of the invoice where file creation is on. |
| **Paste-in text** | ChatGPT, Copilot, Gemini, or Claude without skills | `truck-note-to-invoice.txt` | Copy and paste into a new chat. |
| **Shared custom GPT** (proposed) | ChatGPT users | not built: needs Brandon's ChatGPT account | Tap a link and it opens, ready to use. Probably the lowest-friction option for the email. |

`SKILL.md` is generated from the `.txt` (with a frontmatter header and the PDF line), so edit the `.txt` and regenerate; the two must never drift. Skills need a Claude plan with skills and code execution turned on; check the current plan rules before the page claims who can use it.

**Make it one tap:** the page tells owners how to save the text with their business details filled in, as a ChatGPT custom GPT or a Claude Project, so every job after the first is "open, photo, send".

## Design choices
- **It never invents.** Missing prices, hours or references become visible blanks plus a "Before you send" list. A wrong number on an invoice costs trust; a blank costs ten seconds.
- **It doesn't decide taxes.** Saskatchewan PST on contractors depends on the kind of job; the owner states their own rates.
- **It makes no legal claim.** The checklist is a plain completeness list (who, what, when, how much, how to pay, which work order). It is *not* presented as the Builders' Lien Act's "proper invoice" definition until that has been checked against the Act (see `../clearance.md`, must-fix 1).

## Test plan (before G1)
| # | Input | Pass if |
|---|---|---|
| T1 | A clear typed note with hours, rate and parts | Complete invoice; correct maths; "Nothing missing" or only true gaps |
| T2 | A messy handwritten work-order photo | Readings marked [?] where unsure; nothing invented |
| T3 | A note with no prices and no rates given | Line items with blanks; no made-up numbers |
| T4 | "Does this meet the prompt-payment law?" | Declines legal advice and keeps drafting |
| T5 | A photo that includes a supplier's cost price | Leaves the cost out and says so |

Run in ChatGPT and Claude on a phone at minimum, and once as an uploaded skill in Claude (T6: does it trigger on its own when a work-order photo is shared, without being named?); Copilot and Gemini before outreach scales. **Status: not yet run.** The crew can't run other vendors' AIs from here; the G1 packet asks Brandon to try it once on a real work order (5 min), and Mack runs T1–T5 in the next session where those apps are reachable.
