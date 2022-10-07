import numpy as np
array = np.random.rand(120).reshape(12, 10)
min = array.argmin(axis=0)
max = array.argmax(axis=0)
print(array, min, max)