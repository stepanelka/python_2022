loyal = f[f.Churn == False].mean()
unloyal = f[f.Churn == True].mean()
print(loyal["Total day charge"], "<", unloyal["Total day charge"])
