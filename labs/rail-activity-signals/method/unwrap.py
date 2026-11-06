"""Straighten the loop: for each date, sample RGB on a ribbon -60..+60 m across the track, stack dates."""
import sys, json, datetime as dt, numpy as np, shapely, s2lib, rasterio, pickle
from shapely import wkt
from pyproj import Transformer
from rasterio.windows import from_bounds
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageDraw
name, d0, d1 = sys.argv[1], sys.argv[2], sys.argv[3]
ring = wkt.loads(json.load(open("loops_geom.json"))[name])
lon0, lat0 = ring.centroid.x, ring.centroid.y
tile = s2lib.tile_of(lat0, lon0); crs = f"EPSG:{32600+int(tile[0])}"
tr = Transformer.from_crs(4326, crs, always_xy=True)
r = shapely.transform(ring, lambda c: np.c_[tr.transform(c[:,0], c[:,1])])
s = np.arange(0, r.length, 5.0); pts = np.array([r.interpolate(v).coords[0] for v in s])
nx = np.gradient(pts[:,1]); ny = -np.gradient(pts[:,0]); nn = np.hypot(nx, ny); nx /= nn; ny /= nn
offs = np.arange(-60, 61, 5.0)
X = pts[:,0][None,:] + offs[:,None]*nx[None,:]; Y = pts[:,1][None,:] + offs[:,None]*ny[None,:]
minx, miny = X.min()-50, Y.min()-50; maxx, maxy = X.max()+50, Y.max()+50
def one(x):
    d, sid, p = x; out = {"date": d, "sid": sid}
    try:
        for b in ["B04", "B03", "B02", "B08", "SCL"]:
            with rasterio.open(f"{s2lib.B}/{p}{b}.tif") as ds:
                w = from_bounds(minx, miny, maxx, maxy, ds.transform).round_offsets().round_lengths()
                a = ds.read(1, window=w, boundless=True, fill_value=0).astype(float)
                rr, cc = rasterio.transform.rowcol(ds.window_transform(w), X.ravel(), Y.ravel())
                out[b] = a[np.clip(rr, 0, a.shape[0]-1), np.clip(cc, 0, a.shape[1]-1)].reshape(X.shape)
        return out
    except Exception as e: print("err", sid, e); return None
sc = s2lib.scenes(tile, dt.date.fromisoformat(d0), dt.date.fromisoformat(d1))
with ThreadPoolExecutor(8) as ex: res = [o for o in ex.map(one, sc) if o]
pickle.dump({"s": s, "offs": offs, "res": res}, open(f"unw_{name}_{d0}_{d1}.pkl", "wb"))
print(name, len(sc), len(res), int(r.length))
