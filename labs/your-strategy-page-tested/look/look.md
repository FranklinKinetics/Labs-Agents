# The Look: Your Strategy Page, Tested
*Would it change a decision?*

Iris, 2026-11-21. Draft for G4. Not yet reviewed by Vera. No Rotor Lesson here (Fenn is drafting it).

## 1. The one visual metaphor

What will they see in their head tomorrow? A page, with a few lines lit.

| Option | Picture | Verdict |
|---|---|---|
| A. **Lit lines** | A strategy page where three lines glow and the rest fade to a dotted grey. | **Pick.** Says the whole product in one glance: most of the words aren't steering anything. |
| B. Highlighter and ghosts | A page with highlighter strokes on some lines and the rest struck through. | No. "Struck through" reads as judgment, and the Lab never rewrites or deletes. |
| C. Top on the page | A spinning top balanced on a sheet; lines that lean toward its axis stay lit. | Too clever. Needs explaining. Forced. |

**Chosen: A, with the brand top as a small signature, not the subject.** The tiny top rests at the bottom edge of the sheet, like a maker's mark. It ties to the brand without pretending the Lab is about the top. If it ever feels crowded, drop it; the metaphor stands alone.

Lit lines carry a tick as well as colour, so the meaning does not depend on colour alone. Sketch: `look/hero-sketch.svg`.

## 2. Store thumbnail

- **Image:** the lit-lines page, cropped tight, three lit lines clear, five faded. Small top mark in the bottom corner. No people. No photos.
- **Text on it:** title only, "Your Strategy Page, Tested", large. The subtitle "Would it change a decision?" beneath, if it stays legible at thumbnail size; otherwise drop it from the image (it is on the page anyway). Nothing else: no "FREE" burst, no badges.
- **Colours:** match the site (Brandon to supply the exact values from franklinkinetics.com; I have not seen them). Warm off-white ground, one accent for the lit lines, dark ink for the title.
- **Alt text:** "A page of text with three lines lit up and the rest faded, a small spinning top at its foot. Title: Your Strategy Page, Tested."

## 3. Store/product page, phone, top to bottom

1. **Headline:** Your Strategy Page, Tested
2. **Subtitle:** Would it change a decision?
3. **One-line promise:** Paste your strategy page into the AI you already use, and see which lines would guide a decision and which wouldn't.
4. **Image:** the lit-lines page, full width, with alt text (section 2).
5. **How it works, three steps:**
   1. Copy the instruction text and paste it into a new chat in ChatGPT, Claude, Copilot or Gemini.
   2. Paste your strategy page when it asks. A one-pager, a values list, or slides copied as text all work.
   3. Read the short table it gives back. Optionally name two or three real past decisions so it can test those lines too.
6. **Sample result.** Label above it, visible text: **Example — not a real company.**

   | Line (shortened) | Verdict | Why |
   |---|---|---|
   | "We value excellence" | FAIL | Wouldn't change any choice; nobody could act differently because of it. |
   | "Keep existing clients over chasing new ones" | PASS | Names a real trade-off: it gives up new work to protect current clients. |
   | "Customers love our service" | FAIL | A belief with no warning sign written down to show it's breaking. |

   Caption: "Illustrative only. Your result will quote your own lines."
   Layout note: three narrow columns, short cells, no horizontal scroll (see section 5).
7. **What it doesn't do:** It doesn't rewrite your strategy or suggest wording. It doesn't tell you what your strategy should be. It doesn't judge whether the strategy is right, only whether the lines are clear enough to use. AIs make mistakes, so treat the verdicts as questions to think about.
8. **Privacy line:** It runs in your own AI, under your own account's terms. Franklin Kinetics never sees what you paste. If your page has client names or private details, swap in placeholders first.
9. **Button:** **Get it** (free). Checkout collects your email so we can send the file. Below the button, an unticked box: "Send me occasional notes from Franklin Kinetics (optional)." Not pre-ticked; the file arrives either way.
10. **Small line:** Made by Franklin Kinetics.

No price shown beyond "Free" on the button. No sales push, no countdowns, no "limited". No testimonials or usage numbers.

Note for Ines: the brief (section 6) recommended no sign-up wall; the lab card says email at checkout (Brandon 2026-11-12). I followed the card. The page should say plainly that the email is for delivery only (guardrail 11).

## 4. Usability

- **Obvious first step:** the first thing the owner needs is the text copied. The delivered page or file should open with one big **Copy the instructions** button, then "Now open a new chat and paste." A plain .txt file with no button forces select-all on a phone, which is the single likeliest place to trip.
- Deliver as a **page** (or Squarespace download page) with the button, and keep the .txt as a backup.
- Say which AI to use: "Whichever one you already have an account for." Don't ask them to choose.
- Tell them "new chat" in step 1; stale chats confuse the format.
- A blunt FAIL on their own page can sting. The how-to's "questions to think about, not rulings" line should sit near the sample, not buried.
- The AI asks for past decisions mid-way. Pre-warn in step 3 that it will, and that skipping is fine.
- Say upfront which AIs are tested. Lab card: only Claude tested; ChatGPT, Copilot, Gemini must be run before G7. Don't claim all four on the page until then.
- Phone: long paste into the AI app works but is clumsy; the button matters most there.

## 5. Accessibility checklist (guardrail 14)

- [ ] Text contrast at least 4.5:1 (body), 3:1 for large text and for the lit-line accent against the paper, in light and dark. Check the final site colours; sketch values are placeholders.
- [ ] Lit versus faded is never colour alone: weight, dash pattern and a tick mark also differ.
- [ ] Alt text on the hero and thumbnail (above). The SVG has title and desc.
- [ ] No text baked into images unless the same words are in the alt text or on the page. The thumbnail title is repeated in alt text.
- [ ] Sample table is real HTML table with header row, three narrow columns, wraps on a 320px screen, no sideways scroll. If the store can't do it, use three short stacked entries instead.
- [ ] "Example — not a real company" is real text, not part of an image.
- [ ] Copy button is a real button, at least 44px tall, with a visible focus state, and announces "Copied" in text.
- [ ] Verdicts use words (PASS/FAIL), not just red/green.
- [ ] Text sized to be readable without zoom on a phone; checkbox label is clickable and clearly worded.
- [ ] Respects dark mode where the platform allows it.

## 6. Image production note

- Simplest route: Brandon (or a tool) draws it from `hero-sketch.svg`: a sheet, eight lines, three lit with ticks, five faded and dotted, a tiny top at the foot. Open it in any vector tool (e.g. Canva, Figma, Inkscape) and recolour to the site palette.
- Export two sizes: a wide hero (about 1600x900) and a square or 4:3 crop for the store thumbnail. Export PNG (or keep the SVG if the store accepts it).
- Rules: no stock photos, no people, nothing copying another brand's look or artwork. Draw the spinning top fresh; don't reuse any clip-art top.
- If using an image generator: prompt for flat abstract shapes only ("a blank sheet with eight lines, three glowing, five faded, no readable words"), then check it contains no accidental gibberish text or logos before use.
- Brandon time: about 15 minutes at G4 to review. It should not need more (guardrail 8).
