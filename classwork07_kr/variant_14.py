def task1():
    a, b = map(int, input().split())
    c = a ** 2 - b ** 2
    print(c)

def task2():
    a = input()
    n = 0
    for i in range(0, len(a)):
        if a[i] == chr(33, 47) or a[i] == chr(58, 64) or a[i] == chr(91, 96) or a[i] == chr(123, 127):
    n += 1
print(n)

def task3():
    a = input()  # здесь что-то сломалось :с
    n = 0
    for i in range(1, len(a) - 3):
        if a[i] == 'A' and a[i + 1] == 'b' and a[i + 2] == 'o' and a[i - 1] == ' ':
            n = n + 1  # для всех кроме первого
        if a[0] == 'A' and a[1] == 'b' and a[2] == 'o':
            n = n + 1  # для первого слова
    print(n)

def task4(generator):
    def foo(a):
        if a % 2 == 0:
            return False
        if a % 2 != 0:
            return True

    itog = filter(foo, generator)
    print(itog)

def task5(list_of_smth):
    a = input().split()
    b = a[::2]
    itog = b[::-1]
    print(itog)


def task6(list1, list2, list3, list4):
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

def task7():
    import numpy as np
    from numpy import linalg as la
    matrix = np.random.randint(0, 36, (6, 6))
    matrix1 = np.delete(matrix, 4, axis=0)
    matrix1 = np.delete(matrix1, 4, axis=1)
    print(matrix1, la.det(matrix1))


def task8(f, min_x, max_x, N, min_y, max_y):
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.linspace(min_x, max_x, N)
    y = f(x)
    plt.plot(x, y, 'g-.')
    plt.xlim(min_x, max_x)
    plt.ylim(min_y, max_y)
    plt.yscale('log')
    plt.grid('True')
    plt.show()
    plt.savefig("function.png")

def task9(data, x_array, y_array):
    # TODO: ...

def task10(list_of_smth):
    # TODO: ...

def task11(filename="infile.csv"):
    # TODO: ...

def task12(filename="video-games.csv"):
    # TODO: ...
