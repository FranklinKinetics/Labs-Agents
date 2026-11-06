"""Straighten a loop in Sentinel-1 RTC radar (Planetary Computer): VV and VH on a ribbon ±60 m."""
import sys, json, numpy as np, shapely, rasterio, pickle, os
from shapely import wkt
from pyproj import Transformer
from rasterio.windows import from_bounds
from concurrent.futures import ThreadPoolExecutor
os.environ.setdefault("CURL_CA_BUNDLE", "/root/.ccr/ca-bundle.crt")
name, items_path = sys.argv[1], sys.argv[2]
tok = open("s1_token.txt").read().strip()
ring = wkt.loads(json.load(open("loops_geom.json"))[name])
items = json.load(open(items_path))
def one(it):
    out = {"date": it["properties"]["datetime"][:16], "id": it["id"], "orbit": it["properties"].get("sat:orbit_state"),
           "rel": it["properties"].get("sat:relative_orbit")}
    try:
        for b in ["vv", "vh"]:
            with rasterio.open(it["assets"][b]["href"] + "?" + tok) as ds:
                tr = Transformer.from_crs(4326, ds.crs, always_xy=True)
                r = shapely.transform(ring, lambda c: np.c_[tr.transform(c[:,0], c[:,1])])
                s = np.arange(0, r.length, 5.0); pts = np.array([r.interpolate(v).coords[0] for v in s])
                nx = np.gradient(pts[:,1]); ny = -np.gradient(pts[:,0]); nn = np.hypot(nx, ny); nx /= nn; ny /= nn
                offs = np.arange(-60, 61, 5.0)
                X = pts[:,0][None,:] + offs[:,None]*nx[None,:]; Y = pts[:,1][None,:] + offs[:,None]*ny[None,:]
                w = from_bounds(X.min()-50, Y.min()-50, X.max()+50, Y.max()+50, ds.transform).round_offsets().round_lengths()
                a = ds.read(1, window=w, boundless=True, fill_value=np.nan).astype(float)
                rr, cc = rasterio.transform.rowcol(ds.window_transform(w), X.ravel(), Y.ravel())
                out[b] = a[np.clip(rr, 0, a.shape[0]-1), np.clip(cc, 0, a.shape[1]-1)].reshape(X.shape)
        out["offs"] = offs; return out
    except Exception as e: print("err", it["id"], e); return None
with ThreadPoolExecutor(8) as ex: res = [o for o in ex.map(one, items) if o]
pickle.dump(res, open(f"s1unw_{name}.pkl", "wb")); print(name, len(items), len(res))
