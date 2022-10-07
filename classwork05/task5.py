import numpy as np
array = np.random.rand(120).reshape(12, 10)
print(array, "\n")
print("столбец: среднее, среднеквадратичное, сумма = ", array.mean(axis=1), array.std(axis=1), array.sum(axis=1), "\n" )
print("строка: среднее, среднеквадратичное, сумма = ", array.mean(axis=0), array.std(axis=0), array.sum(axis=0), "\n" )