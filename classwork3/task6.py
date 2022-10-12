a = input()
a = set(a)
print(a)
d = {i - 96 : chr(i) for i in range(97, 123)}
print(d)
d_new = {y: x for x, y in d.items()}
print(d_new)
for i in range(len(a)):
  value = d_new(a[i])
print(d_new.key('a'))