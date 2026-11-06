import pandas as pd, numpy as np, shapely, datetime as dt, s2lib, chip, rasterio
from PIL import Image, ImageDraw
from pyproj import Transformer
from concurrent.futures import ThreadPoolExecutor
R = pd.read_csv("cgc_sask_pinpointed.csv")
big = R[(R.type == "Pri") & (R.capacity_t >= 25000) & (R.railway != "NOT")].copy()
st = big.groupby("station").agg(lat=("lat", "first"), lon=("lon", "first"), lic=("licensee", lambda s: "; ".join(x.split(",")[0].replace(" Limited", "").replace(" Canada Inc.", "").replace(" Ltd.", "")[:18] for x in s)),
                                cap=("capacity_t", lambda s: "/".join(f"{v//1000}k" for v in s)), rly=("railway", lambda s: "/".join(s))).reset_index()
st = st.dropna(subset=["lat"]).reset_index(drop=True); st.to_csv("station_sheet_index.csv")
rail = shapely.from_wkb(pd.read_pickle("rail_sk.pkl").geometry.values)
HALF = 2500
def one(i):
    r = st.iloc[i]
    try:
        for d, sid, p, cc in chip.clear_scenes(r.lat, r.lon, dt.date(2025, 8, 15), dt.date(2025, 10, 15), 5):
            with rasterio.open(f"{s2lib.B}/{p}TCI.tif") as ds:
                tr = Transformer.from_crs(4326, ds.crs, always_xy=True); x0, y0 = tr.transform(r.lon, r.lat)
                rr, cc0 = ds.index(x0, y0); h = HALF // 10
                if rr - h < 0 or cc0 - h < 0 or rr + h > ds.height or cc0 + h > ds.width: continue
                a = ds.read(window=rasterio.windows.Window(cc0 - h, rr - h, 2 * h, 2 * h))
                if (a == 0).all(0).mean() > 0.01: continue
            im = Image.fromarray(np.moveaxis(a, 0, 2)).resize((450, 450), Image.LANCZOS); dr = ImageDraw.Draw(im); k = 450 / (2 * HALF)
            box = shapely.box(*Transformer.from_crs(ds.crs, 4326, always_xy=True).transform_bounds(x0 - HALF, y0 - HALF, x0 + HALF, y0 + HALF))
            for g in rail:
                if not g.intersects(box): continue
                xs, ys = tr.transform(*np.array(g.coords).T)
                dr.line([((x - x0) * k + 225, -(y - y0) * k + 225) for x, y in zip(xs, ys)], fill=(255, 60, 60), width=1)
            for j in range(1, 5):
                dr.line((j * 90, 0, j * 90, 450), fill=(255, 255, 255, 80)); dr.line((0, j * 90, 450, j * 90), fill=(255, 255, 255, 80))
            for cx in range(5):
                for cy in range(5): dr.text((cx * 90 + 3, cy * 90 + 3), "ABCDE"[cx] + str(cy + 1), fill=(255, 255, 255))
            dr.rectangle((0, 432, 450, 450), fill=(0, 0, 0)); dr.text((3, 435), f"#{i} {r.station} {r.rly} {r.cap}", fill=(255, 255, 0))
            return i, im
    except Exception as e: print(i, e)
    return i, None
with ThreadPoolExecutor(8) as ex: res = dict(ex.map(one, range(len(st))))
ims = [(i, res[i]) for i in range(len(st)) if res[i] is not None]
for k in range(0, len(ims), 12):
    S = Image.new("RGB", (1800, 1350))
    for j, (i, im) in enumerate(ims[k:k + 12]): S.paste(im, ((j % 4) * 450, (j // 4) * 450))
    S.save(f"st_sheet_{k // 12}.png")
print(len(st), "stations;", len(ims), "chips;", [i for i in range(len(st)) if res[i] is None])
print(st[["station", "lic", "cap", "rly"]].to_string())
