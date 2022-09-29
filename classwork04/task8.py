import numpy as np
a=np.array([x for x in range (1, 100)], float)
x=a[::3].reshape(11, 3)
matr = x[1:8:3].reshape(3, 3)
print(np.linalg.det(matr))