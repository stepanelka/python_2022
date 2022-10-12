df = f.groupby(["State"]).agg({"Total eve calls": "mean",'Total day calls': 'mean'})
df['X'] = df['Total day calls'] > df['Total eve calls']
df