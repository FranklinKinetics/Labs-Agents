import pandas as pd, numpy as np, shapely, datetime as dt, s2lib, chip, rasterio, json
from rasterio.features import rasterize
from scipy import ndimage
from pyproj import Transformer
from concurrent.futures import ThreadPoolExecutor
R = pd.read_csv("big_elevators_pinned.csv"); loc = pd.read_csv("cgc_sask_located.csv")
rail = shapely.from_wkb(pd.read_pickle("rail_sk.pkl").geometry.values)
todo = R[R.lat.isna()].station.unique()
town = loc.groupby("station").agg(lat=("lat", "first"), lon=("lon", "first"))
HALF = 6000
def one(st):
    if st not in town.index or pd.isna(town.lat[st]): return st, []
    lat, lon = town.lat[st], town.lon[st]
    try:
        for d, sid, p, cc in chip.clear_scenes(lat, lon, dt.date(2025, 7, 1), dt.date(2025, 9, 30), 10):
            bands = []
            for b in ["B02", "B03", "B04"]:
                with rasterio.open(f"{s2lib.B}/{p}{b}.tif") as ds:
                    tr = Transformer.from_crs(4326, ds.crs, always_xy=True); x0, y0 = tr.transform(lon, lat)
                    w = rasterio.windows.from_bounds(x0 - HALF, y0 - HALF, x0 + HALF, y0 + HALF, ds.transform).round_offsets().round_lengths()
                    bands.append(ds.read(1, window=w, boundless=True, fill_value=0).astype(float)); T = ds.window_transform(w); crs = ds.crs
            a = np.stack(bands)
            if (a[0] == 0).mean() > 0.01: continue
            tr2 = Transformer.from_crs(4326, crs, always_xy=True)
            box = shapely.box(*Transformer.from_crs(crs, 4326, always_xy=True).transform_bounds(x0 - HALF, y0 - HALF, x0 + HALF, y0 + HALF))
            geoms = [shapely.transform(g, lambda c: np.c_[tr2.transform(c[:, 0], c[:, 1])]).buffer(120) for g in rail if g.intersects(box)]
            if not geoms: return st, []
            near = rasterize(geoms, out_shape=a.shape[1:], transform=T).astype(bool)
            bright = (a.min(0) > 1300) & (a.max(0) - a.min(0) < 700)   # bright and grey/white (steel, concrete)
            lab, n = ndimage.label(bright & near)
            out = []
            for i, sl in enumerate(ndimage.find_objects(lab), 1):
                px = (lab[sl] == i).sum()
                if px < 10: continue
                rr, cc_ = np.argwhere(lab == i).mean(0); x, y = T * (cc_ + 0.5, rr + 0.5)
                lo, la = Transformer.from_crs(crs, 4326, always_xy=True).transform(x, y)
                out.append(dict(lat=round(la, 5), lon=round(lo, 5), bright_m2=int(px * 100), km=round(np.hypot(x - x0, y - y0) / 1000, 1), scene=sid))
            return st, sorted(out, key=lambda o: -o["bright_m2"])[:4]
    except Exception as e: print(st, e)
    return st, []
with ThreadPoolExecutor(8) as ex: res = dict(ex.map(one, todo))
json.dump(res, open("brightpin.json", "w"), indent=0, default=str)
for st, v in res.items(): print(st, [(o["bright_m2"], o["km"]) for o in v])
