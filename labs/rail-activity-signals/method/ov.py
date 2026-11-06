import os, sys, re, pyarrow.dataset as ds, pyarrow.compute as pc, pyarrow.fs as pfs
px = os.environ["HTTPS_PROXY"]
fs = pfs.S3FileSystem(anonymous=True, region="us-west-2", proxy_options=px)
theme = sys.argv[1]
d = ds.dataset(f"overturemaps-us-west-2/release/2026-10-21.0/{theme}", filesystem=fs, format="parquet")
bx = pc.field("bbox")
f = (pc.field("bbox","xmin") > -110.1) & (pc.field("bbox","xmax") < -101.3) & (pc.field("bbox","ymin") > 48.9) & (pc.field("bbox","ymax") < 54.6)
cols = sys.argv[2].split(",")
t = d.to_table(filter=f, columns=cols + ["bbox"])
t.to_pandas().to_pickle(sys.argv[3]); print(t.num_rows)
