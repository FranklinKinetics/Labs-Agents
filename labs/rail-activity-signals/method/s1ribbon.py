import sys, pickle, numpy as np
from PIL import Image, ImageDraw
res = sorted(pickle.load(open(sys.argv[1], "rb")), key=lambda r: r["date"]); out = sys.argv[2]
orbit = sys.argv[3] if len(sys.argv) > 3 else None
rows = []
for r in res:
    if orbit and orbit != "all" and str(r["rel"]) != orbit: continue
    if len(sys.argv) > 5 and not (sys.argv[4] <= r["date"][:10] <= sys.argv[5]): continue
    vv = r["vv"]
    if np.isnan(vv).mean() > 0.05: continue
    db = 10 * np.log10(np.clip(vv, 1e-4, None))
    a = (np.clip((db + 25) / 25, 0, 1) * 255).astype(np.uint8)   # -25..0 dB
    im = Image.fromarray(a).resize((a.shape[1] * 2, a.shape[0] * 2), Image.NEAREST).convert("RGB")
    rows.append((f"{r['date'][:10]} o{r['rel']}", im))
W = rows[0][1].width + 150; S = Image.new("RGB", (W, sum(i.height + 2 for _, i in rows)), (30, 30, 30)); y = 0; d = ImageDraw.Draw(S)
for lab, im in rows: S.paste(im, (150, y)); d.text((4, y + 18), lab, fill=(255, 255, 0)); y += im.height + 2
S.save(out); print(len(rows))
import collections; print(collections.Counter(str(r["rel"]) for r in res))
