import numpy as np
import matplotlib.pyplot as plt
x = np.arange(10, 100)
plt.plot(x, np.exp((x) * np.sin(x)), 'ro')
plt.yscale('log')
plt.xlabel('x')
plt.ylabel('y = ln(exp(x * sin(x))')
plt.show()