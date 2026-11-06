import os, pyarrow.dataset as ds, pyarrow.compute as pc, pyarrow.fs as pfs
fs = pfs.S3FileSystem(anonymous=True, region="us-west-2", proxy_options=os.environ["HTTPS_PROXY"])
d = ds.dataset("overturemaps-us-west-2/release/2026-10-21.0/theme=buildings/type=building", filesystem=fs, format="parquet")
f = (pc.field("bbox","xmin") > -110.0) & (pc.field("bbox","xmax") < -101.4) & (pc.field("bbox","ymin") > 49.0) & (pc.field("bbox","ymax") < 54.5) & pc.field("class").isin(["silo","grain_silo","storage_tank","industrial","warehouse","agricultural"])
t = d.to_table(filter=f, columns=["id","class","subtype","names","height","geometry"])
t.to_pandas().to_pickle("bld_sk.pkl"); print(t.num_rows); print(t.to_pandas()["class"].value_counts())
