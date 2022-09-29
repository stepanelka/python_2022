import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(10, 100)
plt.plot(x, np.exp((-x) * np.sin(x)))
plt.show()