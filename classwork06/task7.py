df = f.groupby(["State"]).agg({"Total eve calls": "mean",'Total day calls': 'mean'})
df