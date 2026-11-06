import os, pyarrow.dataset as ds, pyarrow.compute as pc, pyarrow.fs as pfs
fs = pfs.S3FileSystem(anonymous=True, region="us-west-2", proxy_options=os.environ["HTTPS_PROXY"])
d = ds.dataset("overturemaps-us-west-2/release/2026-10-21.0/theme=transportation/type=segment", filesystem=fs, format="parquet")
print(d.schema.names)
f = (pc.field("subtype") == "rail") & (pc.field("bbox","xmin") > -110.1) & (pc.field("bbox","xmax") < -101.3) & (pc.field("bbox","ymin") > 48.9) & (pc.field("bbox","ymax") < 54.6)
t = d.to_table(filter=f, columns=["id","class","subclass","names","geometry","subclass_rules","sources"])
t.to_pandas().to_pickle("rail_sk.pkl"); print(t.num_rows)
