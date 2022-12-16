import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.size'] = 16 # Управление стилем, в данном случаем - размером шрифта
 # Создаем фигуру
plt.figure(figsize=(7,7))

# Подписываем оси и график
plt.title(r"Это название  графика  $y = x^3$ - да, можно использовать LaTeX:")
plt.ylabel("Это ось Y")
plt.xlabel(r"Это ось X, $F(x) = \int f(x) dx + C$")



# Добавляем данные
x = np.linspace(-1,1,100)
y = x**3
plt.plot(x,y, label="Синия линия")

# Еще данные
x2 = x[::10]
y2 = np.sin(x2)
plt.plot(x2,y2, 'r^', label='Красные треугольники')
# 'r^' - задает стиль линии - красные (red) треугольники (^), подробнее в документации

# Данные с ошибками
mu = np.sin(x2)
sigma = np.abs(mu)**0.5
y2 = np.random.normal(mu, sigma)
# Можно рисовать ошибки
plt.errorbar(x2,y2, yerr=sigma, xerr=0.1, fmt='.', label='Кресты')

# Активируем сетку
plt.grid(b=True, which='major', axis='both', alpha=1)
plt.grid(b=True, which='minor', axis='both', alpha=0.5)

# Активируем легенду графика
plt.legend()
# Внимание, запускаете вашу программу как сценарий, то что бы показать график
# Используйте эту команду
# plt.show()
# Сохраняем изображение в текущую директорию
plt.savefig('example.png')
