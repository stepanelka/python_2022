a = input().split()
n = int(input())
b = []
for i in range(len(a) - n):
    for k in range(n):
        sr = a[i] * a[i + k] # ?? произведение от iтого элемента до i+1
        b.append(sr)
else
    b.append(a[i])