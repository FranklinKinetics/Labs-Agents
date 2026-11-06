import sys, csv, pickle, numpy as np, dark
site, path, outcsv = sys.argv[1], sys.argv[2], sys.argv[3]
lab = dict(x.split(":") for x in sys.argv[4].split(",")) if len(sys.argv) > 4 and sys.argv[4] else {}
rows = []
for o in dark.dark(path):
    d = str(o["date"])
    if o["cloud"] >= 0.05: state = "unusable (cloud/shadow)"
    elif o["snow"] > 0.5: state = "unreadable (snow)"
    else: state = lab.get(d, "no train seen")
    rows.append(dict(site=site, date=d, scene=o["sid"], cloud_on_loop=round(o["cloud"], 2), snow_on_loop=round(o["snow"], 2),
                     auto_dark_fraction=round(o["darkfrac"], 2), auto_colour_speckle=round(o["speck"], 2), manual_read=state))
with open(outcsv, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
from collections import Counter; print(Counter(r["manual_read"] for r in rows), len(rows))
