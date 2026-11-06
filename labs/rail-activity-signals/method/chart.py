import csv, datetime as dt, collections, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, matplotlib.dates as md
rows = list(csv.DictReader(open("../data/g3-pasqua_observations.csv")))
for r in rows: r["d"] = dt.date.fromisoformat(r["date"])
TXT, MUTED, GRID, SURF = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
cats = [("no train seen", "#2a78d6", "o", 1.0), ("train likely", "#eb6834", "D", 1.0), ("train possible", "#eb6834", "D", 0.0),
        ("unreadable (snow)", "#a3a29c", "s", 1.0), ("unusable", "#d6d5d0", "|", 1.0)]
fig, (a1, a2) = plt.subplots(2, 1, figsize=(11, 5.6), sharex=True, gridspec_kw={"height_ratios": [1.1, 1]}, facecolor=SURF)
y = {c[0]: i for i, c in enumerate(cats[::-1])}
for name, col, mk, fill in cats:
    pts = [r["d"] for r in rows if (r["manual_read"].startswith("unusable") if name == "unusable" else r["manual_read"] == name)]
    a1.scatter(pts, [y[name]] * len(pts), marker=mk, s=60 if mk != "|" else 120, facecolors=col if fill else SURF, edgecolors=col, linewidths=2, label=f"{name} ({len(pts)})", zorder=3)
a1.set_yticks(list(y.values())); a1.set_yticklabels(list(y.keys()), color=TXT, fontsize=9)
a1.set_title("G3 Pasqua loop track: what each Sentinel-2 pass showed (Jun 2025 – Jun 2026)", loc="left", color=TXT, fontsize=12)
m = collections.Counter((r["d"].year, r["d"].month) for r in rows if r["manual_read"] in ("no train seen", "train likely", "train possible"))
t = collections.Counter((r["d"].year, r["d"].month) for r in rows if "train" in r["manual_read"] and "no " not in r["manual_read"])
ks = sorted(set((r["d"].year, r["d"].month) for r in rows))
xs = [dt.date(k[0], k[1], 15) for k in ks]
a2.bar(xs, [m[k] for k in ks], width=22, color="#2a78d6", label="readable passes (no snow, no cloud)", zorder=3)
a2.bar(xs, [t[k] for k in ks], width=22, color="#eb6834", label="of which: train likely/possible", zorder=4)
for x, k in zip(xs, ks): a2.text(x, m[k] + 0.2, str(m[k]), ha="center", fontsize=8, color=MUTED)
a2.set_ylabel("passes per month", color=MUTED); a2.set_title("Readable passes per month", loc="left", color=TXT, fontsize=11)
a2.xaxis.set_major_formatter(md.DateFormatter("%b\n%Y"))
for a in (a1, a2):
    a.set_facecolor(SURF); a.grid(axis="x" if a is a1 else "y", color=GRID, zorder=0)
    for s in a.spines.values(): s.set_visible(False)
    a.tick_params(colors=MUTED)
a1.legend(loc="upper center", bbox_to_anchor=(0.5, -0.02), ncol=5, frameon=False, fontsize=8)
a2.legend(loc="upper center", bbox_to_anchor=(0.55, 1.0), frameon=False, fontsize=8)
fig.text(0.01, 0.005, "Source: contains modified Copernicus Sentinel-2 data 2025–2026 (L2A, AWS open data). Reads by eye from 10 m imagery; not verified against shipment records.", fontsize=7, color=MUTED)
plt.tight_layout(rect=(0, 0.02, 1, 1)); plt.savefig("pasqua_timeline.png", dpi=150, facecolor=SURF)
