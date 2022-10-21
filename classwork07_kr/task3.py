a = input() #здесь что-то сломалось :с
n = 0
for i in range (1, len(a) - 3):
    if a[i] == 'A' and a[i + 1] == 'b' and a[i + 2] == 'o' and a[i - 1] == ' ':
        n = n + 1 #для всех кроме первого
    if a[0] == 'A' and a[1] == 'b' and a[2] == 'o':
        n = n + 1 #для первого слова
print(n)