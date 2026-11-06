import sys, pickle, numpy as np
def dark(path):
    P = pickle.load(open(path, "rb")); offs = P["offs"]; out = []; seen = set()
    for r in sorted(P["res"], key=lambda r: (r["date"], r["sid"])):
        if r["date"] in seen: continue
        cloud = np.isin(r["SCL"], [0, 3, 8, 9, 10]).mean(); snow = (r["SCL"] == 11).mean()
        if (r["B04"] == 0).mean() > 0.01: continue
        seen.add(r["date"])
        vis = (r["B04"] + r["B03"] + r["B02"]) / 3
        near = np.abs(offs) <= 20; far = np.abs(offs) >= 45
        fld = np.median(vis[far], 0); mn = vis[near].min(0)
        ratio = mn / np.maximum(fld, 1)
        d = ratio < 0.72
        # longest run
        best = run = 0
        for x in d: run = run + 1 if x else 0; best = max(best, run)
        spk = np.abs(r["B04"] - r["B02"])[near].max(0) / np.maximum(vis[near].max(0), 1)
        out.append(dict(date=r["date"], sid=r["sid"], cloud=cloud, snow=snow, darkfrac=d.mean(), run_m=best * 5, speck=np.mean(spk > 0.6)))
    return out
if __name__ == "__main__":
    for o in dark(sys.argv[1]):
        if o["cloud"] < .05: print(f"{o['date']} snow {o['snow']:.2f} dark {o['darkfrac']:.2f} run {o['run_m']:5d} speck {o['speck']:.2f}")
