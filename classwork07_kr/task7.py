import numpy as np
from numpy import linalg as la
matrix = np.random.randint(0, 36, (6, 6))
matrix1 = np.delete(matrix, 4, axis = 0)
matrix1 = np.delete(matrix1, 4, axis = 1)
print(matrix1, la.det(matrix1))
