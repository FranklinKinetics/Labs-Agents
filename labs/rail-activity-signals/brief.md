# Brief: Saskatchewan Rail Activity Signals

> **Status: killed 2026-11-06.** Reason: no business problem found. See `logs/decisions.md`.

Expands the Spark "Railcar siding tracker" (`labs/sparks.md`). Brandon commissioned a proof of concept on 2026-11-06. Full results: **`findings.md`**.

1. **What it is:** site-level estimates of rail shipment activity at Saskatchewan grain terminals and industrial sidings, from satellite imagery. CN and CPKC publish network totals only.
2. **Who it's for:** outsiders to the grain-rail system (traders and their research providers, lenders, government). Grain companies and railways already know their own numbers. Audience: not an SME-owner product; its Story could speak to SME owners.
3. **Sources:** see the table in `findings.md`. Sentinel-2 is fully open. The OSM-derived rail geometry is ODbL (share-alike). Free high-res (Esri Wayback, Google Earth) forbids commercial derived data.
4. **Feasibility:**
   - *Easy:* finding every loop track in the province, and pulling every free image (169 passes per site per year).
   - *Hard:* seeing the train. At 10 m it's visible by eye on a good day; the automatic score isn't reliable yet; winter is mostly unreadable.
   - *Unknown:* accuracy (no ground truth), train dwell time on the loop, and whether Sentinel-1 radar does better.
5. **Four Proofs, first read:**
   - Speed: strong; one crew session, 0 Brandon hours.
   - Abundance: strong; a free photo of every terminal every 2–3 days plus an open rail map.
   - Craft: strong; loop-finding and "straightened loop" strips.
   - Goodwill: weak so far; a free provincial loop map is the best candidate.
6. **Sol's first price read:** not requested yet. There's no Offer to price until the signal works.
7. **Update (same day):** Sentinel-1 radar works at Pasqua: 111 passes a year, all usable, with clear train spikes that agree with optical on all 7 shared days. Inconclusive at Belle Plaine. Spurs outnumber loops 68 to 24 among 100+ car elevators.
8. **Recommendation:** **reshape.** Radar is the main free signal now. Next: identify every terminal from the Grain Commission list (spurs included), run radar on a sample of spur sites, and get one ground-truth conversation on dwell time and train dates. Then return to G2. As a store product it fails the Schwerpunkt; as a Story it serves it.

## Proposed Living Models (for Brandon to accept at a gate, not yet adopted)
- Radar (Sentinel-1) shows a parked unit train more reliably than 10 m optical imagery, including in winter. (Supported at Pasqua; not yet at Belle Plaine.)
- A loaded unit train sits on a terminal loop roughly 12–24 hours. (A terminal manager can replace this with a real number.)
- Outsiders (traders, analysts, lenders) value site-level rail activity more than insiders do.
