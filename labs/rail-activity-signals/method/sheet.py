import pandas as pd, datetime as dt, numpy as np, s2lib, chip, sys
from PIL import Image, ImageDraw
from concurrent.futures import ThreadPoolExecutor
o = pd.read_csv("loops_candidates.csv")
o = o[(o.compact >= 0.35) & (o.area_ha >= 15) & (o.perim_m.between(2000, 6500))].reset_index(drop=True)
print(len(o))
def one(r):
    try:
        for d, sid, p, cc in chip.clear_scenes(r.lat, r.lon, dt.date(2025,8,1), dt.date(2025,9,30), 3):
            a = s2lib.window(p, "TCI", r.lat, r.lon, 1500)
            if a is None or (a == 0).all(axis=0).mean() > 0.01: continue
            im = Image.fromarray(np.moveaxis(a, 0, 2)).resize((450, 450), Image.LANCZOS)
            ImageDraw.Draw(im).text((5,5), f"#{r.Index} {r.lat:.4f},{r.lon:.4f} {d}", fill=(255,255,0))
            return r.Index, im
    except Exception as e: print(r.Index, e)
    return r.Index, None
with ThreadPoolExecutor(8) as ex: res = list(ex.map(one, o.itertuples()))
o.to_csv("loops_shortlist.csv")
ims = [im for _, im in sorted(res, key=lambda x: x[0]) if im is not None]
for k in range(0, len(ims), 9):
    S = Image.new("RGB", (1350, 1350))
    for j, im in enumerate(ims[k:k+9]): S.paste(im, ((j%3)*450, (j//3)*450))
    S.save(f"sheet_{k//9}.png")
print("done", len(ims))
