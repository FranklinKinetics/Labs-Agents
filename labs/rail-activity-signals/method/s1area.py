"""Radar test for spur/ladder sites: all mapped track within R m of the elevator pin, buffered B m."""
import sys, json, os, urllib.request, numpy as np, shapely, pandas as pd, rasterio, pickle, collections, csv, datetime as dt
from rasterio.features import rasterize
from pyproj import Transformer
from concurrent.futures import ThreadPoolExecutor
os.environ.setdefault("CURL_CA_BUNDLE", "/root/.ccr/ca-bundle.crt")
name, lat, lon, R, B = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
q = {"collections": ["sentinel-1-rtc"], "intersects": {"type": "Point", "coordinates": [lon, lat]}, "datetime": "2025-06-01/2026-06-30", "limit": 250}
items = json.load(urllib.request.urlopen(urllib.request.Request("https://planetarycomputer.microsoft.com/api/stac/v1/search", data=json.dumps(q).encode(), headers={"Content-Type": "application/json"}), timeout=60))["features"]
tok = json.load(urllib.request.urlopen("https://planetarycomputer.microsoft.com/api/sas/v1/token/sentinel-1-rtc", timeout=60))["token"]
rail = shapely.from_wkb(pd.read_pickle("rail_sk.pkl").geometry.values)
def one(it):
    try:
        with rasterio.open(it["assets"]["vv"]["href"] + "?" + tok) as ds:
            tr = Transformer.from_crs(4326, ds.crs, always_xy=True); x0, y0 = tr.transform(lon, lat)
            w = rasterio.windows.from_bounds(x0 - R - 100, y0 - R - 100, x0 + R + 100, y0 + R + 100, ds.transform).round_offsets().round_lengths()
            a = ds.read(1, window=w, boundless=True, fill_value=np.nan).astype(float); T = ds.window_transform(w)
            circ = shapely.Point(x0, y0).buffer(R)
            geoms = [shapely.transform(g, lambda c: np.c_[tr.transform(c[:, 0], c[:, 1])]) for g in rail]
            geoms = [g.intersection(circ).buffer(B) for g in geoms if g.intersects(circ)]
            m = rasterize(geoms, out_shape=a.shape, transform=T).astype(bool)
        return dict(date=it["properties"]["datetime"][:16], rel=it["properties"].get("sat:relative_orbit"), px=10 * np.log10(np.clip(a[m], 1e-4, None)))
    except Exception as e: print("err", e); return None
with ThreadPoolExecutor(8) as ex: res = [r for r in ex.map(one, items) if r is not None]
by = collections.defaultdict(list)
for r in res: by[r["rel"]].append(r)
out = []
for rel, rs in by.items():
    n = min(len(r["px"]) for r in rs); P = np.array([r["px"][:n] for r in rs]); base = np.nanmedian(P, 0)
    for r, p in zip(rs, P):
        out.append(dict(utc=r["date"], local=(dt.datetime.fromisoformat(r["date"]) - dt.timedelta(hours=6)).strftime("%Y-%m-%d %H:%M"), orbit=rel, bright_frac=round(float(np.nanmean(p - base > 3)), 3), fill_db=round(float(np.nanmean(np.sort(p)[-n//3:]) - np.nanmean(np.sort(base)[-n//3:])), 2), track_px=n))
out.sort(key=lambda o: o["utc"])
with open(f"s1area_{name}.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
v = np.array([o["bright_frac"] for o in out])
print(name, "passes", len(v), "track pixels", out[0]["track_px"]); print(" histogram", np.histogram(v, bins=[0, .05, .1, .15, .2, .3, .4, .6, 1])[0])
