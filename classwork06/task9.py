n = f.shape[0]
k1 = f[f["International plan"] == 'Yes'].shape[0]

k2 = f[f["Voice mail plan"] == 'Yes'].shape[0]
print(k1/n, k2/n)