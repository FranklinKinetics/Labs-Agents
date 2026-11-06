# Method: how to rerun the proof of concept

All data is free and needs no login. Needs Python with `rasterio pyproj mgrs numpy pillow pandas pyarrow shapely matplotlib`.

| Step | Script | What it does |
|---|---|---|
| 1 | `ov.py`, `ovrail.py` | Pull Saskatchewan places and rail segments from Overture Maps (S3, anonymous) |
| 2 | `loops.py` | Turn the rail network into closed rings; keep loop-sized ones → `loops_candidates.csv` |
| 3 | `sheet.py` | Contact sheets of each candidate from one clear Sentinel-2 scene, to sort by eye |
| 4 | `loopgeom.py` + `sites_in.json` | Save the ring geometry for the chosen sites |
| 5 | `unwrap.py <site> <from> <to>` | For every Sentinel-2 pass, sample a ribbon ±60 m across the loop ("straightened loop") |
| 6 | `ribbon.py`, `ribbon_sel.py` | Stack straightened strips by date for reading by eye |
| 7 | `dark.py`, `dataset.py` | Automatic scores + eye labels → observations CSV |
| 8 | `chart.py` | Timeline chart |

`s2lib.py` lists Sentinel-2 L2A scenes by MGRS tile from the `sentinel-cogs` bucket and reads small windows over HTTPS, so no full scenes are downloaded. Two sites × 13 months took about two minutes.

Known gaps: some known terminals (Viterra Kindersley, Cargill Clavet, G3 Melville, Cargill Davidson) don't appear as closed loops in the open map and need drawing by hand. The ring for a balloon loop can include a piece of the lead track.
