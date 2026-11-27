// Builds start-here.pdf (the file Squarespace delivers on purchase).
// Run from the repo root: node labs/truck-note-to-invoice/squarespace/make-pdf.js
// Re-run whenever config.json or the one-tap prompt changes.
const fs = require('fs'), path = require('path');
const { chromium } = require('playwright');
const dir = __dirname;
const cfg = JSON.parse(fs.readFileSync(path.join(dir, 'config.json'), 'utf8'));
const prompt = fs.readFileSync(path.join(dir, '../build/one-tap-prompt.txt'), 'utf8').trim();
const q = encodeURIComponent(prompt);
const gpt = 'https://chatgpt.com/?q=' + q, claude = 'https://claude.ai/new?q=' + q;
const booking = cfg.booking_link, mail = cfg.contact_email;
const pending = booking.startsWith('[');
const html = `<!doctype html><html><head><meta charset="utf-8"><style>
 @page { size: Letter; margin: 0.7in; }
 body { font-family: Georgia, 'Times New Roman', serif; color:#1d1d1b; font-size: 11.5pt; line-height: 1.45; }
 h1 { font-size: 24pt; margin: 0 0 2pt; } .sub { color:#555; margin:0 0 18pt; font-style: italic; }
 h2 { font-size: 13.5pt; margin: 18pt 0 6pt; border-bottom: 1px solid #ccc; padding-bottom: 3pt; }
 ol li, ul li { margin-bottom: 5pt; } .step { font-weight: bold; }
 a.btn { display:inline-block; background:#1d1d1b; color:#fff; text-decoration:none; padding:7pt 14pt; border-radius:4pt; margin:4pt 8pt 4pt 0; font-family: Helvetica, Arial, sans-serif; font-size:10.5pt; }
 .box { background:#f4f1ea; padding:10pt 14pt; border-radius:4pt; } .small { font-size: 9.5pt; color:#555; }
 .foot { margin-top: 24pt; font-size: 9.5pt; color:#555; border-top:1px solid #ccc; padding-top:6pt; }
</style></head><body>
<h1>Truck Note to Invoice</h1>
<p class="sub">Set up for your firm. Start here.</p>
<p>Thank you. Over the next few days we set up your own invoice assistant: your rates and your price book built in, ready for every tech and the office. Here's what happens next.</p>
<h2>Three steps</h2>
<ol>
<li><span class="step">Send us your details (10 minutes).</span> Reply to your order email, or write to <a href="mailto:${mail}?subject=Truck%20Note%20setup">${mail}</a>, with:
 <ul>
 <li>business name, mailing address, phone, email, and GST number if you have one</li>
 <li>labour rate(s), and how you bill parts (at cost, or your markup)</li>
 <li>the taxes you charge and at what rates</li>
 <li>payment terms, and how customers pay you</li>
 <li>your logo, if you have one</li>
 <li>your price list: a photo, a spreadsheet, or your 20 most common parts and services</li>
 <li>how many trucks, and which AI your crew uses (ChatGPT, Claude, or not sure)</li>
 </ul></li>
<li><span class="step">We build your kit</span> within three working days of getting your details: your own ChatGPT and Claude links, truck cards with your QR code, invoice and reminder wording with your logo, and a two-minute office routine.</li>
<li><span class="step">A 20-minute handover call with Brandon</span>, in the evening. Bring a real work order, and we'll run it through on the call.<br>
${pending ? '<span class="small">The booking link comes with your kit.</span>' : `<a class="btn" href="${booking}">Book your handover call</a>`}</li>
</ol>
<h2>Start today, while you wait</h2>
<div class="box">
<p>The quick version is free and works now. Tap one, then send a photo of a work order:</p>
<a class="btn" href="${gpt}">Open in ChatGPT</a><a class="btn" href="${claude}">Open in Claude</a>
<p class="small">Your own version, coming in your kit, already knows your rates and prices, so nobody types them in.</p>
</div>
<h2>Good to know</h2>
<ul>
<li><b>Your data.</b> We use your details and price list only to build your kit, and delete them 30 days after we deliver it. Once it's set up, it runs on your own phones and AI accounts; nothing comes back to us.</li>
<li><b>It drafts; you decide.</b> It never makes up a price or an hour. Anything missing shows as a blank to fill in.</li>
<li><b>Not useful?</b> Email us within 30 days for a full refund.</li>
</ul>
<div class="foot">Franklin Kinetics Consulting Corp. · franklinkinetics.com · ${mail}</div>
</body></html>`;
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.setContent(html, { waitUntil: 'load' });
  await p.pdf({ path: path.join(dir, 'start-here.pdf'), format: 'Letter', printBackground: true });
  await p.screenshot({ path: path.join(dir, 'start-here-preview.png'), fullPage: true });
  await b.close(); console.log('ok', pending ? '(booking link pending)' : '');
})();
