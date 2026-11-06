import pandas as pd, shapely, numpy as np, json
from shapely.ops import polygonize, unary_union
from pyproj import Transformer
df = pd.read_pickle("rail_sk.pkl")
print(df["class"].value_counts().to_dict())
g = shapely.from_wkb(df.geometry.values)
tr = Transformer.from_crs(4326, 3347, always_xy=True)  # StatCan Lambert, metres
gm = [shapely.ops.transform(tr.transform, x) for x in g]
net = unary_union(gm)
polys = list(polygonize(net))
pl = pd.read_pickle("places_flat.pkl")
pl = pl[pl.name.fillna("").str.lower().str.contains("viterra|richardson|cargill|g3|parrish|heimbecker|paterson|dreyfus|bunge|ilta|grain|terminal|elevator|crush|aggregat|gravel")]
px, py = tr.transform(pl.lon.values, pl.lat.values)
inv = Transformer.from_crs(3347, 4326, always_xy=True)
out = []
for p in polys:
    per = p.exterior.length
    if 1500 < per < 7000 and p.area > 20000:
        c = p.centroid; lon, lat = inv.transform(c.x, c.y)
        dd = np.hypot(px - c.x, py - c.y); i = dd.argmin()
        out.append(dict(lat=round(lat,5), lon=round(lon,5), perim_m=int(per), area_ha=round(p.area/1e4,1),
                        compact=round(4*np.pi*p.area/per**2,2), near=pl.name.iloc[i], near_town=pl.town.iloc[i], near_km=round(dd[i]/1000,1)))
o = pd.DataFrame(out).sort_values("lat")
o.to_csv("loops_candidates.csv", index=False)
pd.set_option("display.width", 250); print(len(o)); print(o.to_string())
