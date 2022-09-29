import numpy as np

array = np.arange(1, 100)
matrix = array[::3].reshape(11, 3)
x = np.arange(-9, 2)
print(matrix.T @ x)