# Squarespace build sheet · Truck Note to Invoice (Mack, 2026-11-27)

Squarespace's API can't create digital products, attach files or edit pages ([products overview](https://developers.squarespace.com/commerce-apis/products-overview), [create product](https://developers.squarespace.com/commerce-apis/create-product), [websites API](https://developers.squarespace.com/commerce-apis/websites)), so this is a click-by-click sheet. **About 20 minutes, on a computer.** Menu names may differ slightly from these.

**Build everything hidden. Nothing goes public until you pass G1 (`QUEUE.md` item 1).**

## A · Short links, so the buttons stay tidy (3 min)
Settings → Developer Tools → URL Mappings. Add these lines, pasting the long links from `../build/one-tap-links.md`:
```
/truck-note/chatgpt -> <the ChatGPT link> 302
/truck-note/claude -> <the Claude link> 302
```
Now any button can point to `franklinkinetics.com/truck-note/chatgpt`, and you can change the long link in one place later. *If Squarespace refuses a link that long, skip this step and paste the long links straight into the buttons in C.*

## B · The product (7 min)
Commerce → Products → **+** → **Digital product**.
| Field | Enter |
|---|---|
| Name | Truck Note to Invoice: set up for your firm |
| Price | 79.00 (CAD) |
| File | upload `start-here.pdf` (this folder) |
| Description | We set up your own invoice assistant for the whole crew: your rates and price book built in, truck cards with your QR code, invoice and reminder wording with your logo, a two-minute office routine, and a 20-minute evening handover call with Brandon. Your details are used only to build your kit and deleted 30 days after delivery. Not useful? Full refund within 30 days. |
| Visibility | **Hidden** until G1 |
| Taxes | as for your other Labs (PST/GST: check with your accountant, as decided on 2026-11-10) |

## C · The Lab page (8 min)
Pages → your Labs section → **+** → blank page, titled "Truck Note to Invoice", slug `truck-note`. **Leave it disabled or hidden** until G1. Add these blocks top to bottom, with the text from `../page.md`:
1. **Text block:** headline "Snap the work order. Get the invoice." and its sub-line.
2. **Text block:** "Try it free in ChatGPT or Claude. Or have it set up for your firm: CAD $79, once."
3. **Text block:** "How it works", steps 1–3.
4. **Two button blocks:** "Open in ChatGPT" → `/truck-note/chatgpt?ref=truck-note`; "Open in Claude" → `/truck-note/claude?ref=truck-note`. *(If step A was skipped, use the long links.)*
5. **Text block:** the example (`../build/example.md`), with the label "Example: invented business, customer and job" visible.
6. **Text block:** "Set up for your firm · CAD $79, once" and its bullets.
7. **Product block:** the product from B (Add to cart).
8. **Text block:** "Built with AI in about [N] hours…" (Ines fills the hours at release) and the lesson line.
9. **Text block:** "If you run a firm of 20–200 people" paragraph.
10. **Button block:** "Book a 20-minute call" → your booking link + `?ref=truck-note`. Under it, a text line: "or reply with a question; I read every one" (linked to Start a conversation, `?ref=truck-note`).

## D · Order email (2 min)
Settings → Notifications (customer emails) → **Order confirmed** (digital). Add one line:
> Your Start Here guide is in the download link below. To begin, reply to this email with your setup details; the guide lists what to send.

## E · Tell Ines (1 min)
Reply "built" in `QUEUE.md`. Ines checks the page on a phone from the outside once you pass G1 and it's visible.

## When something changes
- The booking link exists → put it in `config.json` and re-run `node labs/truck-note-to-invoice/squarespace/make-pdf.js` from the repo root. Re-upload the PDF to the product.
- The one-tap prompt changes → re-run the same script; update the URL mappings.
