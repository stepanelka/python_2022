import numpy as np
import matplotlib.pyplot as plt


a,b = 0, 1
np.random.seed(0)
data = np.random.normal(a, b, 100000)
plt.hist(data, "auto")
plt.show()