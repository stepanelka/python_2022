import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(min_x, max_x, N)
y = f(x)
plt.plot(x, y, 'g-.')
plt.xlim(min_x, max_x)
plt.ylim(min_y, max_y)
plt.yscale('log')
plt.grid('True')
plt.show()
plt.savefig("function.png")