import pandas as pd, numpy as np, shapely
from shapely.strtree import STRtree
from pyproj import Transformer
tr = Transformer.from_crs(4326, 3347, always_xy=True); inv = Transformer.from_crs(3347, 4326, always_xy=True)
P = lambda g: shapely.transform(g, lambda c: np.c_[tr.transform(c[:,0], c[:,1])])
rail = [P(g) for g in shapely.from_wkb(pd.read_pickle("rail_sk.pkl").geometry.values)]
rtree = STRtree(rail)
b = pd.read_pickle("bld_sk.pkl"); bg = [P(g) for g in shapely.from_wkb(b.geometry.values)]
b["area"] = [g.area for g in bg]; b["cx"] = [g.centroid.x for g in bg]; b["cy"] = [g.centroid.y for g in bg]
b["rail_m"] = [rtree.geometries[rtree.nearest(shapely.Point(x, y))].distance(shapely.Point(x, y)) for x, y in zip(b.cx, b.cy)]
print(b.height.describe())
seedb = b[(b.rail_m < 150) & ((b.height.fillna(0) >= 20) | (b.area >= 400)) & b["class"].isin(["silo", "industrial", "storage_tank"])]
pl = pd.read_pickle("places_flat.pkl"); n = pl.name.fillna("").str.lower()
pl = pl[n.str.contains(r"viterra|richardson pioneer|richardson international|cargill|^g3|parrish|heimbecker|p&h|paterson|louis dreyfus|bunge|ilta|grain terminal|inland terminal|terminal ltd|elevator|sunrise grain|lexington|w\.a\. grain|broadgrain|prairie west|north west terminal|south west terminal|weyburn inland|great sandhills|providence grain|ceres|ag growth|agrocorp|richardson|seed hawk") & ~n.str.contains("museum|pool|park|recreation|creek|bakery|library|kone|escalator|bus|restaurant|grainger|bin direct|studio")]
px, py = tr.transform(pl.lon.values, pl.lat.values)
seeds = [(x, y, f"place:{nm}") for x, y, nm in zip(px, py, pl.name)] + [(x, y, f"bldg:{c}:{h}") for x, y, c, h in zip(seedb.cx, seedb.cy, seedb["class"], seedb.height)]
seeds = [s for s in seeds if rtree.geometries[rtree.nearest(shapely.Point(s[0], s[1]))].distance(shapely.Point(s[0], s[1])) < 1500]
# cluster seeds within 1.2 km
cl = []
for x, y, lab in seeds:
    for c in cl:
        if np.hypot(c["x"] - x, c["y"] - y) < 1200: c["labs"].append(lab); c["pts"].append((x, y)); break
    else: cl.append({"x": x, "y": y, "labs": [lab], "pts": [(x, y)]})
out = []
for c in cl:
    xs, ys = zip(*c["pts"]); x, y = np.mean(xs), np.mean(ys)
    near = [rtree.geometries[i] for i in rtree.query(shapely.Point(x, y).buffer(1500))]
    circ = shapely.Point(x, y).buffer(1500)
    tot = sum(g.intersection(circ).length for g in near)
    lon, lat = inv.transform(x, y)
    names = sorted({l.split(":", 1)[1] for l in c["labs"] if l.startswith("place:")})
    nb = sum(l.startswith("bldg") for l in c["labs"])
    out.append(dict(lat=round(lat, 5), lon=round(lon, 5), rail_km_3km_circle=round(tot / 1000, 1), extra_track_km=round(tot / 1000 - 3.0, 1), n_big_bldgs=nb, names="; ".join(names)[:120]))
o = pd.DataFrame(out).sort_values("extra_track_km", ascending=False)
o.to_csv("terminal_candidates.csv", index=False)
print(len(o), (o.extra_track_km >= 2).sum(), (o.extra_track_km >= 4).sum())
pd.set_option("display.width", 250); print(o.head(60).to_string())
