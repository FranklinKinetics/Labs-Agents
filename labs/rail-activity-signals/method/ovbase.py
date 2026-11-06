import os, sys, pyarrow.dataset as ds, pyarrow.compute as pc, pyarrow.fs as pfs
fs = pfs.S3FileSystem(anonymous=True, region="us-west-2", proxy_options=os.environ["HTTPS_PROXY"])
typ = sys.argv[1]
d = ds.dataset(f"overturemaps-us-west-2/release/2026-10-21.0/theme=base/type={typ}", filesystem=fs, format="parquet")
print(d.schema.names)
f = (pc.field("bbox","xmin") > -110.0) & (pc.field("bbox","xmax") < -101.4) & (pc.field("bbox","ymin") > 49.0) & (pc.field("bbox","ymax") < 54.5)
cols = [c for c in ["id","subtype","class","names","geometry","source_tags","sources"] if c in d.schema.names]
t = d.to_table(filter=f, columns=cols).to_pandas(); t.to_pickle(f"base_{typ}_sk.pkl")
print(len(t)); print(t["class"].value_counts().head(60).to_dict())
