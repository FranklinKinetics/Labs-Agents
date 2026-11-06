import os, pyarrow.dataset as ds, pyarrow.compute as pc, pyarrow.fs as pfs
fs = pfs.S3FileSystem(anonymous=True, region="us-west-2", proxy_options=os.environ["HTTPS_PROXY"])
d = ds.dataset("overturemaps-us-west-2/release/2026-10-21.0/theme=divisions/type=division", filesystem=fs, format="parquet")
f = (pc.field("country") == "CA") & (pc.field("region") == "CA-SK")
t = d.to_table(filter=f, columns=["id", "names", "subtype", "class", "geometry"])
t.to_pandas().to_pickle("div_sk.pkl"); print(t.num_rows, t.to_pandas().subtype.value_counts().to_dict())
