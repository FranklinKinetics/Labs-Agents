# Friction log

Anything that slowed a build. Logged so the next Lab goes faster. Ines reviews it at each Debrief.

| Date | Lab | Who | Friction | Fix or idea |
|---|---|---|---|---|
| 2026-11-06 | rail-activity-signals | Ines | Cloud session blocks CGC, CN, CPKC, STAC catalogues, Overpass and Esri tiles; only AWS S3 open data was reachable | Use S3 open data (Sentinel COGs, Overture); ask Brandon to allow Copernicus/Planetary Computer hosts for the radar test |
| 2026-11-06 | rail-activity-signals | Ines | Sentinel-2 true-colour (TCI) saturates on snow, so winter scenes look blank | Read the raw bands (B04/B03/B02) with a wider stretch |
| 2026-11-06 | rail-activity-signals | Ines | Several known terminals aren't closed loops in OpenStreetMap | Draw them by hand from imagery; that also avoids ODbL share-alike |
| 2026-11-06 | rail-activity-signals | Ines | Scene cloud % flags snow as cloud; real cloud on a 3 km site differs from tile-wide cloud | Judge cloud on the loop itself with the SCL layer |
