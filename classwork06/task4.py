'для NY'
df = f.groupby(["State"]).agg({"Total day calls": "mean"})
df.loc['NY']