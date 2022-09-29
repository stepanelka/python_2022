import numpy as np
import matplotlib.pyplot as plt
x = np.arange(10, 100)
plt.plot(x, np.exp((x) * np.sin(x)), 'ro', label="точки")
plt.yscale('log')
plt.xlabel('это ось x')
plt.ylabel('y = log(exp(x * sin(x))')
plt.title('график')
plt.legend()
plt.show()