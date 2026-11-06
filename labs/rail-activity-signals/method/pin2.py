import pandas as pd, numpy as np, shapely, re
from shapely.strtree import STRtree
from pyproj import Transformer
tr = Transformer.from_crs(4326, 3347, always_xy=True); inv = Transformer.from_crs(3347, 4326, always_xy=True)
P = lambda g: shapely.transform(g, lambda c: np.c_[tr.transform(c[:,0], c[:,1])])
rail = [P(g) for g in shapely.from_wkb(pd.read_pickle("rail_sk.pkl").geometry.values)]; rt = STRtree(rail)
inf = pd.read_pickle("base_infrastructure_sk.pkl"); inf = inf[inf["class"].isin(["silo", "storage_tank"])]
bl = pd.read_pickle("bld_sk.pkl"); bl = bl[bl["class"].isin(["silo", "storage_tank"])]
G = [P(g) for g in shapely.from_wkb(np.r_[inf.geometry.values, bl.geometry.values])]
pts = pd.DataFrame({"x": [g.centroid.x for g in G], "y": [g.centroid.y for g in G], "a": [max(g.area, 30.0) for g in G]})
pts["rail_m"] = [rt.geometries[rt.nearest(shapely.Point(x, y))].distance(shapely.Point(x, y)) for x, y in zip(pts.x, pts.y)]
pts = pts[pts.rail_m < 200].reset_index(drop=True)
# clusters: greedy by 200 m
lab = -np.ones(len(pts), int); k = 0
for i in np.argsort(-pts.a.values):
    if lab[i] >= 0: continue
    m = (np.hypot(pts.x - pts.x[i], pts.y - pts.y[i]) < 200) & (lab < 0); lab[m] = k; k += 1
pts["c"] = lab
C = pts.groupby("c").agg(x=("x", "mean"), y=("y", "mean"), area=("a", "sum"), n=("a", "size")).reset_index()
C = C[(C.area >= 1500) | (C.n >= 6)]
print("bin clusters next to rail:", len(C))
o = pd.read_csv("cgc_sask_located.csv")
big = o[(o.type == "Pri") & (o.capacity_t >= 25000) & (o.railway != "NOT")].copy()
out = []
for st, g in big.groupby("station"):
    r0 = g.iloc[0]
    if pd.isna(r0.lat): 
        for r in g.itertuples(): out.append(dict(station=st, licensee=r.licensee, railway=r.railway, capacity_t=r.capacity_t, lat=None, lon=None, pinned="station not found in map"))
        continue
    # use town centre, not brand place, as search centre
    sx, sy = tr.transform(r0.lon, r0.lat)
    cand = C.assign(d=np.hypot(C.x - sx, C.y - sy)); cand = cand[cand.d < 8000].sort_values("area", ascending=False).head(len(g))
    for j, r in enumerate(g.sort_values("capacity_t", ascending=False).itertuples()):
        if j < len(cand):
            c = cand.iloc[j]; lon, lat = inv.transform(c.x, c.y)
            out.append(dict(station=st, licensee=r.licensee, railway=r.railway, capacity_t=r.capacity_t, lat=round(lat, 5), lon=round(lon, 5), pinned=f"bin cluster {c.area:.0f} m2, {c.n} bins, {c.d/1000:.1f} km from town"))
        else:
            out.append(dict(station=st, licensee=r.licensee, railway=r.railway, capacity_t=r.capacity_t, lat=None, lon=None, pinned="no bin cluster found"))
R = pd.DataFrame(out); R.to_csv("big_elevators_pinned.csv", index=False)
print(len(R), "pinned:", R.lat.notna().sum())
print(R[R.station.isin(["PASQUA", "CLAVET", "MELVILLE", "KINDERSLEY", "WADENA", "COLONSAY", "MOOSE JAW"])].to_string())
