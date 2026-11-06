import re, csv, pdfplumber
p = pdfplumber.open("ge.pdf"); rows = []; station = None
R = r"(CN2|CP2|OTH2|NOT2|CN|CP|OTH|NOT|BCR)"
pat = re.compile(rf"^(?:(?P<st>[A-Z0-9][A-Z0-9 .'\-()/&]*?)\s+)?{R}\s*(?P<lic>.+?)\s+(?:(?P<fn>[A-Z0-9])\s+)?(?P<typ>Pri\.|Proc\.|Term\.)\s+(?P<cap>[\d,]+)$")
for i in range(40, 49):
    for line in (p.pages[i].extract_text() or "").split("\n"):
        line = line.strip()
        m = pat.match(line)
        if m:
            rly = re.search(R, line[len(m.group("st") or ""):]).group(1)
            if m.group("st"): station = m.group("st").strip()
            rows.append(dict(station=station, railway=rly, licensee=m.group("lic").strip(), type=m.group("typ").rstrip("."), capacity_t=int(m.group("cap").replace(",", "")), page=i + 1))
        elif rows and line and not line.startswith(("Table", "Au 1", "STATION", "GARE", "©", "Tableau")) and not re.search(r"\d,\d{3}$", line):
            rows[-1]["licensee"] += " " + line
        elif line and re.search(r"\d,\d{3}$|\s0$", line) and not line.startswith("©"):
            print("UNPARSED", i + 1, line)
w = csv.DictWriter(open("cgc_sask_2026.csv", "w", newline=""), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
import collections
print(len(rows), collections.Counter(r["type"] for r in rows), collections.Counter(r["railway"] for r in rows))
print("primary >= 25,000 t:", sum(r["type"] == "Pri" and r["capacity_t"] >= 25000 for r in rows))
