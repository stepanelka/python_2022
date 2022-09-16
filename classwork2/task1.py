raw = input()
a = []
for k in raw.split():
  a.append(k)
a = [[i for i in range(len(a))], [a[i]]]
for x in a:
  print(*x)