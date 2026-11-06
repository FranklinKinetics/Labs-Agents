import pandas as pd, shapely, json
from shapely.ops import polygonize, unary_union
from pyproj import Transformer
df = pd.read_pickle("rail_sk.pkl")
tr = Transformer.from_crs(4326, 3347, always_xy=True); inv = Transformer.from_crs(3347, 4326, always_xy=True)
net = unary_union([shapely.ops.transform(tr.transform, x) for x in shapely.from_wkb(df.geometry.values)])
polys = list(polygonize(net))
sel = json.load(open("sites_in.json")); out = {}
for k, (lat, lon) in sel.items():
    x, y = tr.transform(lon, lat); pt = shapely.Point(x, y)
    p = min((q for q in polys if 1500 < q.exterior.length < 7000 and q.area > 1e5), key=lambda q: q.centroid.distance(pt))
    out[k] = shapely.ops.transform(inv.transform, p.exterior).wkt
json.dump(out, open("loops_geom.json", "w"))
print({k: len(v) for k, v in out.items()})
