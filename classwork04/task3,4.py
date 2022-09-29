import numpy as np

array = np.arange(1, 100)

matrix = array[::3].reshape(11, 3)
print(matrix)

print(np.sum(matrix, axis=1))