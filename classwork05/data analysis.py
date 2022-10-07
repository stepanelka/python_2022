import numpy as np
import matplotlib
from matplotlib import pyplot as plt

matplotlib.rcParams.update(matplotlib.rcParamsDefault)


def get_numbers(student):
    return student, (student + 4) % 5 + 3, student % 2 * 10 + 12, (student % 5 * 3 + 7) * 3


def fake_data_generator(seed, vmin=0, vmax=10, size=100):
    import numpy as np
    np.random.seed(seed)
    data = np.random.randint(vmin, vmax, size=20)
    mean = data.mean()
    std = data.std()
    noise = np.random.normal(loc=mean, scale=std ** .5, size=size)
    fake_x = np.array([-5 + i * 20 / size for i in range(size)])

    linear = lambda x, k=(.5 - np.random.rand()) * 15, b=np.random.rand() * 10: k * x + b
    linear_data = linear(fake_x)
    fake_y = linear_data + noise
    return fake_x, fake_y




student = 14
x, y = fake_data_generator(*get_numbers(student))
plt.plot(x, y, 'ro')
x2 = x ** 2
proizved = x * y
k = proizved.mean() / x2.mean()
b = y.mean() - k * x.mean()
print(np.polyfit(x, y, 1))
print("МНК: наклон и смещение = ", x.mean(), y.mean(), x2.mean(), proizved.mean(), k, b)
plt.plot(x, k * x + b)
plt.show()