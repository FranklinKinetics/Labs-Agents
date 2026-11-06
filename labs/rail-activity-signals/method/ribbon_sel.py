import sys, pickle, numpy as np
from PIL import Image, ImageDraw
P = pickle.load(open(sys.argv[1], "rb")); out = sys.argv[2]; sel = sys.argv[3].split(","); offs = P["offs"]
keep = np.abs(offs) <= 30
rows = []
for want in sel:
    d, lab = want.split(":")
    r = [x for x in P["res"] if str(x["date"]) == d and np.isin(x["SCL"], [0,3,8,9,10]).mean() < .05][0]
    a = np.stack([r["B04"], r["B03"], r["B02"]], -1)[keep]
    lo, hi = np.percentile(a, 1), np.percentile(a, 99.5)
    a = (np.clip((a - lo) / (hi - lo + 1), 0, 1) * 255).astype(np.uint8)
    rows.append((d, lab, Image.fromarray(a).resize((a.shape[1] * 2, a.shape[0] * 6), Image.NEAREST)))
W = rows[0][2].width + 190; S = Image.new("RGB", (W, sum(i.height + 4 for *_, i in rows)), (25, 25, 25)); y = 0; dr = ImageDraw.Draw(S)
for d, lab, im in rows:
    S.paste(im, (190, y)); dr.text((6, y + 25), d, fill=(255, 255, 255)); dr.text((6, y + 45), lab, fill=(255, 220, 0)); y += im.height + 4
S.save(out)
