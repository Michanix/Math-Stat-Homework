import matplotlib.pyplot as plt
import numpy as np
from statistics import stdev, mean
from math import sqrt

expected = [3.4, 3.1, 3.0, 2.8, 3.7,
            3.5, 2.9, 3.7, 3.5, 3.2,
            3.0, 3.5, 3.3, 3.1, 3.3,
            3.9, 2.9, 3.2, 3.4, 3.4]

real = [4.1, 3.4, 3.3, 3.0, 4.7,
        4.6, 3.0, 4.6, 4.6, 3.6,
        3.5, 4.0, 3.6, 3.1, 3.3,
        4.5, 2.8, 3.7, 3.8, 3.9]


# 1) построить диаграмму рассеяния
# (x – ожидаемая, y – полученная оценка),
#  добавить линию тренда (использовать линейную функцию)
def build_diagram(x, y):
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.scatter(x, y)
    plt.plot(x, p(x), color='orange')
    plt.grid(True)
    plt.title('диаграммa рассеяния')
    plt.show()

# 2) рассчитайте линейный коэффициент корреляции Пирсона,
#  оцените его значимость при α=0,05;


def koef_pirsona(x, y):
    # x,y - list of values
    avg_x = mean(x)
    avg_y = mean(y)
    std_x = stdev(x)
    std_y = stdev(y)
    avg_xy = mean([i*j for i, j in zip(x, y)])
    result = (avg_xy - avg_x * avg_y) / (std_x * std_y)
    return result

# 3) проверить гипотезу о равенстве средних значений этих
#  двух наборов данных (ожидаемая и получаемая оценки)
# с помощью t-критерия Стьюдента для связных выборок


def t_test(x, y):
    # средняя разность значений
    avg_d = mean(x) - mean(y)
    # cтандартное отклонение разностей
    std_d = stdev(x) - stdev(y)
    # количество наблюдений
    n = 20
    t = avg_d / (std_d / sqrt(n))
    return t


k_pirsona = koef_pirsona(expected, real)
t_test = t_test(expected, real)
print('коэффициент корреляции Пирсона: {}\nt-критерия Стьюдента: {}'.format(k_pirsona, t_test))
build_diagram(expected, real)

