import sys, pickle, numpy as np
from PIL import Image, ImageDraw
P = pickle.load(open(sys.argv[1], "rb")); out = sys.argv[2]; m0, m1 = (sys.argv[3], sys.argv[4]) if len(sys.argv) > 4 else ("0000", "9999")
res = sorted([r for r in P["res"] if m0 <= str(r["date"]) <= m1], key=lambda r: (r["date"], r["sid"]))
seen = set(); rows = []
for r in res:
    if r["date"] in seen: continue
    scl = r["SCL"]; bad = np.isin(scl, [0, 3, 8, 9, 10]).mean()
    if bad > 0.05 or (r["B04"] == 0).mean() > 0.01: continue
    seen.add(r["date"])
    a = np.stack([r["B04"], r["B03"], r["B02"]], -1)
    lo, hi = np.percentile(a, 1), np.percentile(a, 99.5)
    a = (np.clip((a - lo) / (hi - lo + 1), 0, 1) * 255).astype(np.uint8)
    im = Image.fromarray(a).resize((a.shape[1] * 2, a.shape[0] * 2), Image.NEAREST)
    rows.append((r["date"], im, (scl == 11).mean()))
W = rows[0][1].width + 130; H = sum(i.height + 2 for _, i, _ in rows)
S = Image.new("RGB", (W, H), (30, 30, 30)); y = 0; dr = ImageDraw.Draw(S)
for d, im, sn in rows:
    S.paste(im, (130, y)); dr.text((4, y + 18), f"{d}{' snow' if sn > .5 else ''}", fill=(255, 255, 255)); y += im.height + 2
S.save(out); print(len(rows))
