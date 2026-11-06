import sys, datetime as dt, numpy as np, s2lib, json, urllib.request
from PIL import Image, ImageDraw
from concurrent.futures import ThreadPoolExecutor
name, lat, lon, half, d0, d1 = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), sys.argv[5], sys.argv[6]
t = s2lib.tile_of(lat, lon)
sc = s2lib.scenes(t, dt.date.fromisoformat(d0), dt.date.fromisoformat(d1))
def one(x):
    d, sid, p = x
    try:
        a = np.stack([s2lib.window(p, b, lat, lon, half)[0] for b in ["B04", "B03", "B02"]]).astype(float)
        scl = s2lib.window(p, "SCL", lat, lon, half)[0]
    except Exception: return None
    if (a == 0).mean() > 0.01: return None
    cloud = np.isin(scl, [8, 9, 10, 3]).mean()
    if cloud > 0.5: return None
    hi = np.percentile(a, 99.5); lo = np.percentile(a, 1)
    a = np.clip((a - lo) / (hi - lo), 0, 1) ** 0.8 * 255
    im = Image.fromarray(np.moveaxis(a.astype(np.uint8), 0, 2)).resize((400, 400), Image.NEAREST)
    ImageDraw.Draw(im).text((4, 4), f"{d} {sid[:3]} cl{cloud:.0%} snow{(scl==11).mean():.0%}", fill=(255, 0, 255)); return im
with ThreadPoolExecutor(8) as ex: ims = [i for i in ex.map(one, sc) if i]
n = len(ims); S = Image.new("RGB", (2000, 400 * ((n + 4) // 5)))
for j, im in enumerate(ims): S.paste(im, ((j % 5) * 400, (j // 5) * 400))
S.save(f"zoomr_{name}.png"); print(len(sc), n)
