import numpy as np
import matplotlib.pyplot as plt


np.random.seed(0)
data = np.random.random(270000).reshape(300, 300, 3)

fig, img = plt.subplots()
img.imshow(data)
plt.show()