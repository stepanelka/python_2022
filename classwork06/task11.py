n = f['Customer service calls'].unique()
a = []
b = []
f1 = pd.DataFrame({"calls": [], "number": []})
for x in n:
    b.append(x)
    a.append(f[f["Customer service calls"] == x].count()[0])

f1 = pd.DataFrame({"calls": a, "number": b})
f1