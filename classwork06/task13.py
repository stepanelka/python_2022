f.groupby(["State"]).agg({"Total intl minutes": "mean"}).mean()[0]