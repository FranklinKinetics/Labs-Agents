import pandas as pd, numpy as np, shapely, re
from pyproj import Transformer
tr = Transformer.from_crs(4326, 3347, always_xy=True)
cg = pd.read_csv("../cgc/cgc_sask_2026.csv")
dv = pd.read_pickle("div_sk.pkl"); dv = dv[dv.subtype == "locality"].copy()
g = shapely.from_wkb(dv.geometry.values); dv["lat"] = shapely.get_y(g); dv["lon"] = shapely.get_x(g)
dv["key"] = dv.names.map(lambda n: re.sub(r"[^A-Z]", "", n["primary"].upper()) if n else "")
pl = pd.read_pickle("places_flat.pkl"); pl["n"] = pl.name.fillna("").str.lower()
bx, by = tr.transform(pl.lon.values, pl.lat.values); pl["x"], pl["y"] = bx, by
BR = {"Bunge": "bunge|viterra", "Richardson": "richardson pioneer|richardson international|^richardson$", "Cargill": "cargill", "G3": r"^g3", "Parrish": "parrish|heimbecker|p&h",
      "PATERSON": "paterson", "Louis Dreyfus": "dreyfus|ldc", "South West Terminal": "south west terminal", "North West Terminal": "north west terminal", "Prairie West": "prairie west terminal",
      "Scoular": "scoular", "Weyburn Inland": "weyburn inland", "Great Sandhills": "great sandhills", "AGT": "agt|alliance", "Providence": "providence"}
out = []
for r in cg.itertuples():
    k = re.sub(r"[^A-Z]", "", str(r.station).upper())
    m = dv[dv.key == k]
    if m.empty: m = dv[dv.key.str.startswith(k[:6])] if len(k) >= 6 else m
    lat = lon = None; how = "station not found"
    if not m.empty:
        lat, lon = float(m.lat.iloc[0]), float(m.lon.iloc[0]); how = "town centre"
        sx, sy = tr.transform(lon, lat)
        pat = next((v for kk, v in BR.items() if kk.lower() in r.licensee.lower()), None)
        if pat:
            c = pl[pl.n.str.contains(pat) & (np.hypot(pl.x - sx, pl.y - sy) < 8000)]
            if not c.empty:
                i = np.hypot(c.x - sx, c.y - sy).idxmin(); lat, lon = float(c.lat[i]), float(c.lon[i]); how = f"open-map place '{c.name[i]}' {np.hypot(c.x[i]-sx, c.y[i]-sy)/1000:.1f} km from town"
    out.append(dict(r._asdict(), lat=lat, lon=lon, located_by=how))
o = pd.DataFrame(out).drop(columns=["Index"]); o.to_csv("cgc_sask_located.csv", index=False)
print(o.located_by.str.split(" ").str[0].value_counts())
big = o[(o.type == "Pri") & (o.capacity_t >= 25000) & ~o.railway.isin(["NOT"])]
print(len(big), big.located_by.str.startswith("open-map").sum(), big.located_by.str.startswith("town").sum(), big.lat.isna().sum())
print(big[big.lat.isna()][["station", "licensee"]].to_string())
