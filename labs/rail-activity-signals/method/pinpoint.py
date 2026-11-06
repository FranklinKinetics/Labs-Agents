import pandas as pd, numpy as np, shapely
from shapely.strtree import STRtree
from pyproj import Transformer
tr = Transformer.from_crs(4326, 3347, always_xy=True); inv = Transformer.from_crs(3347, 4326, always_xy=True)
P = lambda g: shapely.transform(g, lambda c: np.c_[tr.transform(c[:,0], c[:,1])])
rail = [P(g) for g in shapely.from_wkb(pd.read_pickle("rail_sk.pkl").geometry.values)]; rt = STRtree(rail)
b = pd.read_pickle("bld_sk.pkl"); bg = [P(g) for g in shapely.from_wkb(b.geometry.values)]
b["area"] = [g.area for g in bg]; b["x"] = [g.centroid.x for g in bg]; b["y"] = [g.centroid.y for g in bg]
b["rail_m"] = [rt.geometries[rt.nearest(shapely.Point(x, y))].distance(shapely.Point(x, y)) for x, y in zip(b.x, b.y)]
b = b[(b.rail_m < 250) & b["class"].isin(["silo", "industrial", "storage_tank", "warehouse"])]
o = pd.read_csv("cgc_sask_located.csv")
res = []
for r in o.itertuples():
    row = r._asdict(); row.pop("Index")
    if pd.isna(r.lat): res.append(row); continue
    sx, sy = tr.transform(r.lon, r.lat); rad = 2500 if r.located_by.startswith("open-map") else 6000
    c = b[np.hypot(b.x - sx, b.y - sy) < rad]
    best = None
    for x, y in zip(c.x, c.y):
        s = c[np.hypot(c.x - x, c.y - y) < 250].area.sum()
        if best is None or s > best[0]: best = (s, x, y)
    if best and best[0] > 1500:
        nb = c[np.hypot(c.x - best[1], c.y - best[2]) < 250]
        lon, lat = inv.transform(nb.x.mean(), nb.y.mean())
        row.update(lat=round(lat, 5), lon=round(lon, 5), located_by=row["located_by"] + f" -> bin cluster {best[0]:.0f} m2", bin_area_m2=int(best[0]))
    res.append(row)
R = pd.DataFrame(res); R.to_csv("cgc_sask_pinpointed.csv", index=False)
big = R[(R.type == "Pri") & (R.capacity_t >= 25000) & (R.railway != "NOT")]
print(big.located_by.str.contains("bin cluster").sum(), "of", len(big), "big elevators pinned to a bin cluster")
# multiple licensees pinned to the same cluster?
d = big.dropna(subset=["lat"]).groupby(["lat", "lon"]).size(); print("shared pins:", (d > 1).sum())
