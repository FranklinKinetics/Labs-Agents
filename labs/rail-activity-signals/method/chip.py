import sys, json, urllib.request, datetime as dt, numpy as np, s2lib
from PIL import Image
def clear_scenes(lat, lon, start, end, maxcc=10):
    t = s2lib.tile_of(lat, lon); out = []
    for d, sid, p in s2lib.scenes(t, start, end):
        j = json.load(urllib.request.urlopen(f"{s2lib.B}/{p}{sid}.json", timeout=60))
        cc = j["properties"].get("eo:cloud_cover", 100)
        if cc <= maxcc: out.append((d, sid, p, cc))
    return out
if __name__ == "__main__":
    name, lat, lon, half = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4])
    for d, sid, p, cc in clear_scenes(lat, lon, dt.date(2025,8,1), dt.date(2025,9,15), 5):
        a = s2lib.window(p, "TCI", lat, lon, half)
        if a is None or (a == 0).all(axis=0).mean() > 0.01: continue
        im = Image.fromarray(np.moveaxis(a, 0, 2)).resize((900, 900), Image.NEAREST)
        im.save(f"chip_{name}.png"); print(name, d, sid, cc); break
