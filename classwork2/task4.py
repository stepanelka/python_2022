a = input()
n = 1
for x in a.split():
    if len(x) > n:
        n = len(x)
m = n
for x in a.split():
    if len(x) < m:
        m = len(x)
print(m,n)
