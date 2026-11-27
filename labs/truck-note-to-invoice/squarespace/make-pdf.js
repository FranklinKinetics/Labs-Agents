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
const img = (f) => 'data:image/webp;base64,' + fs.readFileSync(path.join(dir, '../../../brand', f)).toString('base64');
// Franklin Kinetics brand, read from franklinkinetics.com on 2026-11-27 (see brand/README.md at the repo root)
const C = { ink: '#2B424A', paper: '#ECE7DF', black: '#000000', orange: '#ED6B2E', white: '#FFFFFF' };
const html = `<!doctype html><html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Titillium+Web:wght@400;600;700&display=swap" rel="stylesheet">
<style>
 @page { size: Letter; margin: 0; }
 * { box-sizing: border-box; }
 body { margin:0; background:${C.paper}; color:${C.ink}; font-family:'Titillium Web', Arial, sans-serif; font-size:11pt; line-height:1.45; }
 .hero { background:${C.black}; color:${C.white}; padding:30pt 48pt 40pt; position:relative; }
 .hero .logo { height:11pt; display:block; margin-bottom:22pt; }
 .eyebrow { color:${C.orange}; font-weight:600; font-size:12pt; margin:0 0 6pt; }
 h1 { font-family:'Syne', sans-serif; font-weight:800; text-transform:uppercase; letter-spacing:-0.03em; font-size:32pt; line-height:1.0; margin:0 0 9pt; }
 .hero p { font-size:12pt; max-width:430pt; margin:0; color:#E8E8E8; }
 .curve { position:absolute; left:0; right:0; bottom:-1px; height:22pt; width:100%; display:block; }
 main { padding:10pt 48pt 0; }
 h2 { font-family:'Syne', sans-serif; font-weight:800; text-transform:uppercase; letter-spacing:-0.02em; font-size:14pt; margin:13pt 0 7pt; }
 .steps { display:grid; gap:7pt; }
 .step { display:grid; grid-template-columns:30pt 1fr; gap:10pt; align-items:start; }
 .num { font-family:'Syne', sans-serif; font-weight:800; font-size:24pt; line-height:1; color:${C.orange}; }
 .step b { font-weight:700; }
 .step ul { margin:3pt 0 0; padding-left:14pt; columns:2; column-gap:18pt; font-size:9.5pt; line-height:1.35; }
 .step li { margin-bottom:1pt; break-inside:avoid; }
 .try { background:${C.black}; color:${C.white}; padding:12pt 18pt; }
 .try h2 { color:${C.white}; margin-top:0; }
 .btn { display:inline-block; background:${C.orange}; color:${C.white}; text-decoration:none; font-weight:600; font-size:11.5pt; padding:7pt 16pt; margin:2pt 8pt 6pt 0; }
 .muted { font-size:9.5pt; opacity:.8; margin:4pt 0 0; }
 .facts { display:grid; grid-template-columns:repeat(3,1fr); gap:12pt; font-size:10pt; }
 .facts b { display:block; font-family:'Syne', sans-serif; text-transform:uppercase; font-size:9.5pt; letter-spacing:.02em; color:${C.orange}; margin-bottom:2pt; }
 a { color:${C.orange}; }
 footer { position:absolute; bottom:0; left:0; right:0; background:${C.black}; color:#BDBDBD; padding:12pt 48pt; display:flex; justify-content:space-between; align-items:center; font-size:9pt; }
 footer img { height:8pt; }
 .page { position:relative; height:11in; overflow:hidden; }
</style></head><body><div class="page">
<section class="hero">
 <img class="logo" src="${img('logo-secondary-white.webp')}" alt="Franklin Kinetics">
 <p class="eyebrow">Set up for your firm · Start here</p>
 <h1>Truck Note<br>to Invoice</h1>
 <p>Thank you. Over the next few days we set up your own invoice assistant: your rates and your price book built in, ready for every tech and the office.</p>
 <svg class="curve" viewBox="0 0 100 10" preserveAspectRatio="none"><path d="M0,0 Q50,20 100,0 L100,10 L0,10 Z" fill="${C.paper}"/></svg>
</section>
<main>
 <h2>Three steps</h2>
 <div class="steps">
  <div class="step"><div class="num">1</div><div><b>Send us your details (10 minutes).</b> Reply to your order email, or write to <a href="mailto:${mail}?subject=Truck%20Note%20setup">${mail}</a>, with:
   <ul><li>business name, address, phone, email, GST number</li><li>labour rate(s), and how you bill parts</li><li>the taxes you charge, and their rates</li><li>payment terms, and how customers pay</li><li>your logo, if you have one</li><li>your price list: a photo, a spreadsheet, or your top 20 items</li><li>how many trucks, and which AI your crew uses</li></ul></div></div>
  <div class="step"><div class="num">2</div><div><b>We build your kit</b> within three working days: your own ChatGPT and Claude links, truck cards with your QR code, invoice and reminder wording with your logo, and a two-minute office routine.</div></div>
  <div class="step"><div class="num">3</div><div><b>A 20-minute handover call with Brandon</b>, in the evening. Bring a real work order, and we'll run it through together.
   ${pending ? '<p class="muted" style="opacity:.7">The booking link comes with your kit.</p>' : `<br><a class="btn" href="${booking}">Book your handover call</a>`}</div></div>
 </div>
 <h2>Start today</h2>
 <div class="try">
  <p style="margin:0 0 8pt">The quick version is free and works now. Tap one, then send a photo of a work order.</p>
  <a class="btn" href="${gpt}">Open in ChatGPT</a><a class="btn" href="${claude}">Open in Claude</a>
  <p class="muted">Your own version, coming in your kit, already knows your rates and prices.</p>
 </div>
 <h2>Good to know</h2>
 <div class="facts">
  <div><b>Your data</b>Used only to build your kit, and deleted 30 days after we deliver it. Once set up, it runs on your own phones and AI accounts.</div>
  <div><b>It drafts, you decide</b>It never makes up a price or an hour. Anything missing shows as a blank to fill in.</div>
  <div><b>Not useful?</b>Email us within 30 days for a full refund.</div>
 </div>
</main>
<footer><img src="${img('logo-secondary-white.webp')}" alt="Franklin Kinetics"><span>Franklin Kinetics Consulting Corp. · franklinkinetics.com · ${mail}</span></footer>
</div></body></html>`;
(async () => {
  const proxy = process.env.HTTPS_PROXY || process.env.https_proxy;
  const b = await chromium.launch(proxy ? { proxy: { server: proxy } } : {}); const p = await b.newPage();
  await p.setContent(html, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: path.join(dir, 'start-here.pdf'), format: 'Letter', printBackground: true });
  await p.screenshot({ path: path.join(dir, 'start-here-preview.png'), fullPage: true });
  await b.close(); console.log('ok', pending ? '(booking link pending)' : '');
})();
