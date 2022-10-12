import matplotlib.pyplot as plt
f1 = f.groupby(["Customer service calls"]).agg({"Churn": "mean"})
a = f1["Churn"]
c = []
b = f["Customer service calls"].unique()
for x in b:
    c.append(x)
c = sorted(c)
f1
f.groupby("Customer service calls").agg({"Churn": "mean"})

plt.plot(c, a)
plt.show()