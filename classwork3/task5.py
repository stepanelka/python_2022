d = {i - 96 : chr(i) for i in range(97, 123)}
print(d)
d_new = {y: x for x, y in d.items()}
print(d_new)