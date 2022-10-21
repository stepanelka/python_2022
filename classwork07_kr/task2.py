a = input()
n = 0
 for i in range(0, len(a)):
        if a[i] == chr(33, 47) or a[i] == chr(58, 64) or a[i] == chr(91, 96) or a[i] == chr(123, 127):
    n += 1
print(n)