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
const svgimg = (f) => 'data:image/svg+xml;base64,' + fs.readFileSync(path.join(dir, '../../../brand', f)).toString('base64');
const img = (f) => 'data:image/webp;base64,' + fs.readFileSync(path.join(dir, '../../../brand', f)).toString('base64');
// Labs design system: Klay Design brand guide (Rotor-Wiki raw/brand) + Lab 01/02 product art (see brand/README.md at the repo root)
const C = { teal: '#2B424A', deep: '#1F333A', slate: '#55676D', line: '#455A61', paper: '#EDE8E0', orange: '#ED6B2E', peach: '#F0895A', mist: '#85959A', white: '#FFFFFF' };
const spark = (sz, col) => `<svg width="${sz}" height="${sz}" viewBox="0 0 20 20"><path d="M10 0 C10.6 6.2 13.8 8.6 20 9.2 C13.8 9.8 10.9 12.6 10 20 C9.1 12.6 6.2 9.8 0 9.2 C6.2 8.6 9.4 6.2 10 0Z" fill="${col}"/></svg>`;
const ring = 'SNAP THE WORK ORDER · GET THE INVOICE · SET UP FOR YOUR FIRM · ';
const html = `<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Prompt:wght@600;700&family=Space+Mono:wght@400;700&family=Arimo:wght@400;600;700&display=swap" rel="stylesheet">
<style>
 @page { size: Letter; margin: 0; }
 * { box-sizing: border-box; }
 html, body { margin:0; }
 .page { width:8.5in; height:11in; background:${C.teal}; color:${C.paper}; position:relative; overflow:hidden; font-family:Arimo, Arial, sans-serif; }
 .vl { position:absolute; top:0; bottom:0; width:1px; background:${C.line}; } .vl.l { left:0.42in; } .vl.r { right:0.42in; }
 .row { position:relative; padding:0 0.72in; border-bottom:1px solid ${C.line}; }
 .mono { font-family:'Space Mono', monospace; text-transform:uppercase; letter-spacing:.2em; }
 .top { height:0.95in; display:flex; justify-content:space-between; align-items:center; }
 .top img { height:12pt; } .top .mono { font-size:10pt; color:${C.mist}; letter-spacing:.24em; }
 .hero { padding-top:0.32in; padding-bottom:0.26in; }
 h1 { font-family:Prompt, sans-serif; font-weight:700; color:${C.orange}; font-size:64pt; line-height:.9; letter-spacing:-0.015em; margin:0 0 .22in; }
 .tag { font-size:10.5pt; color:${C.paper}; }
 .badge { position:absolute; right:0.66in; top:0.3in; width:1.45in; height:1.45in; }
 .card { margin:.22in 0.72in; background:${C.paper}; color:${C.teal}; padding:.2in .26in .14in; }
 .card h2 { font-family:Prompt, sans-serif; font-weight:700; font-size:19pt; margin:0; }
 .cardhead { display:flex; justify-content:space-between; align-items:baseline; border-bottom:1.5px dashed ${C.mist}; padding-bottom:8pt; margin-bottom:2pt; }
 .cardhead .mono { font-size:8.5pt; color:${C.slate}; }
 .item { display:grid; grid-template-columns:14pt 1fr auto; gap:9pt; align-items:start; padding:8pt 0; border-bottom:1px solid #D9D3C8; font-size:10.5pt; line-height:1.38; }
 .item:last-child { border-bottom:0; }
 .sq { width:10pt; height:10pt; background:${C.orange}; margin-top:3pt; }
 .item b { font-weight:600; }
 .pill { font-family:'Space Mono', monospace; font-size:8pt; letter-spacing:.08em; text-transform:uppercase; padding:3pt 6pt; white-space:nowrap; }
 .pill.f { background:${C.orange}; color:${C.white}; } .pill.o { border:1.2px solid ${C.teal}; color:${C.teal}; }
 .label { font-size:9pt; color:${C.mist}; margin:.04in 0 8pt; }
 .tiles { display:grid; grid-template-columns:repeat(5,1fr); gap:6pt; }
 .tile { height:.86in; padding:7pt 8pt; display:flex; flex-direction:column; justify-content:space-between; color:${C.white}; }
 .tile .k { font-family:'Space Mono', monospace; font-weight:500; font-size:10pt; letter-spacing:.06em; }
 .tile .v { font-size:8.6pt; line-height:1.3; }
 .t1 { background:${C.deep}; border:1px solid ${C.line}; } .t2 { background:${C.orange}; } .t3 { background:${C.peach}; } .t4 { background:${C.slate}; } .t5 { background:${C.orange}; }
 .sect { padding-top:.16in; padding-bottom:.16in; }
 .try { display:flex; align-items:center; gap:10pt; flex-wrap:wrap; }
 .btn { display:inline-flex; align-items:center; gap:7pt; background:${C.orange}; color:${C.white}; text-decoration:none; font-family:'Space Mono', monospace; font-size:9.5pt; letter-spacing:.12em; text-transform:uppercase; padding:8pt 13pt; }
 .note { font-size:9pt; color:${C.mist}; line-height:1.45; margin:8pt 0 0; }
 .note a { color:${C.peach}; }
 .foot { position:absolute; left:0; right:0; bottom:0; height:.85in; border-top:1px solid ${C.line}; border-bottom:0; display:flex; justify-content:space-between; align-items:center; font-size:9.5pt; }
 .foot .l { color:${C.mist}; } .foot .r { color:${C.orange}; }
</style></head><body><div class="page">
<div class="vl l"></div><div class="vl r"></div>
<div class="row top"><img src="${img('logo-secondary-white.webp')}" alt="Franklin Kinetics"><span class="mono">Lab / 03</span></div>
<div class="row hero">
 <h1>Truck Note<br>to Invoice</h1>
 <div class="mono tag">Set up for your firm · Start here</div>
 <img class="badge" src="${svgimg('badge-on-steel.svg')}" alt="">
</div>
<div class="card">
 <div class="cardhead"><h2>Your setup</h2><span class="mono">3 steps · about 30 min of yours</span></div>
 <div class="item"><div class="sq"></div><div><b>Send us your details.</b> Reply to your order email, or write to ${mail}, with the five things below.</div><span class="pill f">10 min</span></div>
 <div class="item"><div class="sq"></div><div><b>We build your kit:</b> your own ChatGPT and Claude links with your rates and prices built in, truck cards with your QR code, invoice and reminder wording with your logo, and a two-minute office routine.</div><span class="pill o">3 working days</span></div>
 <div class="item"><div class="sq"></div><div><b>Handover call with Brandon</b>, in the evening. Bring a real work order and we'll run it through together.${pending ? ' The booking link comes with your kit.' : ` <a href="${booking}" style="color:${C.orange}">Book it here.</a>`}</div><span class="pill f">20 min</span></div>
</div>
<div class="row sect" style="border-top:1px solid ${C.line}">
 <div class="mono label">What to send us</div>
 <div class="tiles">
  <div class="tile t1"><span class="k">YOU</span><span class="v">Name, address, phone, email, GST no.</span></div>
  <div class="tile t2"><span class="k">RATES</span><span class="v">Labour rates; how you bill parts</span></div>
  <div class="tile t3"><span class="k">TAXES</span><span class="v">What you charge, at what rates</span></div>
  <div class="tile t4"><span class="k">TERMS</span><span class="v">Due when; how customers pay. Your logo.</span></div>
  <div class="tile t5"><span class="k">PRICES</span><span class="v">Your price list, or your top 20 items. A photo is fine.</span></div>
 </div>
</div>
<div class="row sect" style="border-bottom:0">
 <div class="mono label">Start today, free</div>
 <div class="try">
  <a class="btn" href="${gpt}">${spark(10, C.white)} Open in ChatGPT</a>
  <a class="btn" href="${claude}">${spark(10, C.white)} Open in Claude</a>
 </div>
 <p class="note">Tap one, then send a photo of a work order. It never makes up a price or an hour. Your details are used only to build your kit and are deleted 30 days after delivery. Not useful? <a href="mailto:${mail}">Email us</a> within 30 days for a full refund.</p>
</div>
<div class="row foot"><span class="mono l">franklinkinetics.com</span><span class="mono r">Set up for your firm · CAD $79</span></div>
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
