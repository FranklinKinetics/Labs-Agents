import csv, datetime as dt, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, matplotlib.dates as md
s1 = list(csv.DictReader(open("../data/g3-pasqua_radar.csv"))); s2 = list(csv.DictReader(open("../data/g3-pasqua_observations.csv")))
TXT, MUTED, GRID, SURF, BLUE, ORANGE, GREY = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb", "#2a78d6", "#eb6834", "#a3a29c"
fig, (a1, a2) = plt.subplots(2, 1, figsize=(11, 5.4), sharex=True, gridspec_kw={"height_ratios": [3, 1]}, facecolor=SURF)
x = [dt.datetime.fromisoformat(r["local"]) for r in s1]; y = [float(r["bright_frac"]) for r in s1]
col = [ORANGE if v >= 0.2 else BLUE for v in y]
a1.vlines(x, 0, y, color=col, lw=2, zorder=2); a1.scatter(x, y, c=col, s=36, zorder=3, edgecolors=SURF, linewidths=1.5)
a1.axhline(0.2, color=MUTED, lw=1, ls="--", zorder=1); a1.text(x[0], 0.215, "train threshold (20% of loop brighter than usual)", fontsize=8, color=MUTED)
a1.set_ylim(0, 0.75); a1.set_ylabel("share of loop brighter than usual", color=MUTED)
a1.set_title(f"G3 Pasqua in free radar (Sentinel-1): {len(s1)} passes, cloud and snow don't matter", loc="left", color=TXT, fontsize=12)
n = sum(v >= 0.2 for v in y); a1.text(0.99, 0.95, f"{n} of {len(s1)} passes show a likely train", transform=a1.transAxes, ha="right", va="top", fontsize=9, color=TXT)
for lab, c, mk, f in [("no train seen", BLUE, "o", True), ("train likely", ORANGE, "D", True), ("train possible", ORANGE, "D", False)]:
    pts = [dt.datetime.fromisoformat(r["date"]) + dt.timedelta(hours=11, minutes=40) for r in s2 if r["manual_read"] == lab]
    a2.scatter(pts, [0] * len(pts), marker=mk, s=40, facecolors=c if f else SURF, edgecolors=c, linewidths=1.8, label=f"optical: {lab}", zorder=3)
a2.set_yticks([]); a2.set_title("Optical (Sentinel-2) reads by eye, for comparison", loc="left", color=TXT, fontsize=10)
a2.legend(loc="lower center", bbox_to_anchor=(0.5, -1.25), ncol=3, frameon=False, fontsize=8)
a2.xaxis.set_major_formatter(md.DateFormatter("%b\n%Y"))
for a in (a1, a2):
    a.set_facecolor(SURF); a.grid(axis="y" if a is a1 else "x", color=GRID, zorder=0); a.tick_params(colors=MUTED)
    for s in a.spines.values(): s.set_visible(False)
fig.text(0.01, 0.005, "Source: contains modified Copernicus Sentinel-1 and Sentinel-2 data 2025–2026 (Sentinel-1 RTC via Microsoft Planetary Computer). Not yet checked against shipment records.", fontsize=7, color=MUTED)
plt.tight_layout(rect=(0, 0.03, 1, 1)); plt.savefig("pasqua_radar.png", dpi=150, facecolor=SURF)
