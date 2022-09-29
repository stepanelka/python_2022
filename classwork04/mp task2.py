import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 100, 10)
plt.plot(x, np.sin(x) * (x ** 0.5), 'ro')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y = sin(x) * x ^ 0.5')
plt.show()