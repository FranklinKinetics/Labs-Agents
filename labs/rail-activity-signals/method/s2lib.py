import os, re, json, urllib.request, datetime as dt
os.environ.setdefault("CURL_CA_BUNDLE", "/root/.ccr/ca-bundle.crt")
os.environ.setdefault("GDAL_DISABLE_READDIR_ON_OPEN", "EMPTY_DIR")
os.environ.setdefault("GDAL_HTTP_MULTIRANGE", "YES")
import numpy as np, rasterio, mgrs
from rasterio.windows import Window
from pyproj import Transformer
B = "https://sentinel-cogs.s3.us-west-2.amazonaws.com"
P = "sentinel-s2-l2a-cogs"
M = mgrs.MGRS()

def tile_of(lat, lon):
    t = M.toMGRS(lat, lon, MGRSPrecision=0)
    return t[:2], t[2], t[3:5]

def _ls(prefix):
    out, tok = [], None
    while True:
        u = f"{B}/?list-type=2&prefix={prefix}&delimiter=/" + (f"&continuation-token={urllib.parse.quote(tok)}" if tok else "")
        x = urllib.request.urlopen(u, timeout=60).read().decode()
        out += re.findall(r"<Prefix>([^<]*)</Prefix>", x)[1:]
        m = re.search(r"<NextContinuationToken>([^<]*)<", x)
        if not m: return out
        tok = m.group(1)

import urllib.parse
def scenes(tile, start, end):
    z, b, g = tile
    res = []
    y, mo = start.year, start.month
    while (y, mo) <= (end.year, end.month):
        for p in _ls(f"{P}/{z}/{b}/{g}/{y}/{mo}/"):
            sid = p.rstrip("/").split("/")[-1]
            d = dt.datetime.strptime(sid.split("_")[2], "%Y%m%d").date()
            if start <= d <= end: res.append((d, sid, p))
        mo += 1
        if mo == 13: y, mo = y + 1, 1
    # keep highest processing number per (sat, date)
    best = {}
    for d, sid, p in res:
        k = (sid[:3], d)
        if k not in best or sid > best[k][1]: best[k] = (d, sid, p)
    return sorted(best.values())

def window(url_prefix, band, lat, lon, half_m=1500):
    with rasterio.open(f"{B}/{url_prefix}{band}.tif") as ds:
        tr = Transformer.from_crs("EPSG:4326", ds.crs, always_xy=True)
        x, y = tr.transform(lon, lat)
        r, c = ds.index(x, y)
        res = ds.res[0]; h = int(half_m / res)
        if r - h < 0 or c - h < 0 or r + h > ds.height or c + h > ds.width: return None
        a = ds.read(window=Window(c - h, r - h, 2 * h, 2 * h))
        return a
