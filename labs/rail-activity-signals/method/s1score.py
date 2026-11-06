import sys, pickle, numpy as np, collections, csv, datetime as dt
res = sorted(pickle.load(open(sys.argv[1], "rb")), key=lambda r: r["date"])
offs = res[0]["offs"]; core = np.abs(offs) <= 10
def prof(r):
    db = 10 * np.log10(np.clip(r["vv"], 1e-4, None)); return np.nanmax(db[core], 0)   # brightest return across the track
by = collections.defaultdict(list)
for r in res: by[r["rel"]].append(r)
out = []
for rel, rs in by.items():
    P = np.array([prof(r) for r in rs]); base = np.nanmedian(P, 0)
    for r, p in zip(rs, P):
        a = p - base
        out.append(dict(utc=r["date"], local=(dt.datetime.fromisoformat(r["date"]) - dt.timedelta(hours=6)).strftime("%Y-%m-%d %H:%M"),
                        orbit=rel, bright_frac=float(np.nanmean(a > 3)), med_anom_db=float(np.nanmedian(a))))
out.sort(key=lambda o: o["utc"])
with open(sys.argv[2], "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
v = np.array([o["bright_frac"] for o in out])
print("passes", len(v)); print("histogram of bright fraction:", np.histogram(v, bins=[0, .05, .1, .15, .2, .25, .3, .4, .5, .7, 1])[0])
for o in out:
    if o["bright_frac"] >= 0.2: print(o["local"], "orbit", o["orbit"], f"bright {o['bright_frac']:.2f} med {o['med_anom_db']:+.1f} dB")
