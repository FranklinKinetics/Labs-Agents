import sys, json, numpy as np, shapely, pandas as pd, datetime as dt, s2lib, chip, rasterio
from PIL import Image, ImageDraw
from pyproj import Transformer
rail = shapely.from_wkb(pd.read_pickle("rail_sk.pkl").geometry.values)
sites = json.loads(sys.argv[1]); HALF = 1500; ims = []
for name, (lat, lon) in sites.items():
    for d, sid, p, cc in chip.clear_scenes(lat, lon, dt.date(2025, 8, 1), dt.date(2025, 9, 30), 5):
        with rasterio.open(f"{s2lib.B}/{p}TCI.tif") as ds:
            tr = Transformer.from_crs(4326, ds.crs, always_xy=True); x0, y0 = tr.transform(lon, lat); rr, cc0 = ds.index(x0, y0); h = HALF // 10
            a = ds.read(window=rasterio.windows.Window(cc0 - h, rr - h, 2 * h, 2 * h))
        if (a == 0).all(0).mean() > 0.01: continue
        im = Image.fromarray(np.moveaxis(a, 0, 2)).resize((600, 600), Image.LANCZOS); dr = ImageDraw.Draw(im); k = 600 / (2 * HALF)
        box = shapely.box(lon - .03, lat - .02, lon + .03, lat + .02)
        for g in rail:
            if g.intersects(box):
                xs, ys = tr.transform(*np.array(g.coords).T); dr.line([((x - x0) * k + 300, -(y - y0) * k + 300) for x, y in zip(xs, ys)], fill=(255, 60, 60), width=1)
        dr.ellipse((290, 290, 310, 310), outline=(255, 255, 0), width=2); dr.rectangle((0, 0, 600, 18), fill=(0, 0, 0)); dr.text((4, 3), f"{name} {d} (3 km across)", fill=(255, 255, 0))
        ims.append(im); break
S = Image.new("RGB", (600 * len(ims), 600))
for i, im in enumerate(ims): S.paste(im, (600 * i, 0))
S.save(sys.argv[2])
