a = input().split()
b = input().split()
c = input().split()
d = input().split()
itog = []
for k in (a + b):
    for p in (c + d):
        if p == k:
            itog.append(p)
print(itog)