import matplotlib.pyplot as plt
import numpy as np

# source:
# http://mathprofi.ru/metod_naimenshih_kvadratov.html

# вариант 1
# y = ax + bx^2

xi = [1, 2, 3, 4, 5, 6, 7]
yi = [7, 3, 4, 8, 10, 15, 25]

# Система уравнений
# a * sum(x^2) + b * sum(x^3) = sum(x*y)
# a * sum(x^3) + b * sum(x^4) = sum(x^2*y)
# сумма всех x
x1 = sum(xi)
# сумма всех у 
y1 = sum(yi)
# сумма х^2 
x2 = sum([i**2 for i in xi])
# сумма х^3
x3 = sum([i**3 for i in xi])
# сумма х^4
x4 = sum([i**4 for i in xi])

# x * y
xy = sum([i*j for i,j in zip(xi, yi)])
# x^2 * y
x2_y = sum([i**2 * j for i,j in zip(xi, yi)])

# формулы Крамера
# http://mathprofi.ru/pravilo_kramera_matrichnyi_metod.html
# e = sum(x^2)*sum(x^4) - sum(x^3) * sum(x^3)
e = x2 * x4 - x3 * x3
# delta a = sum(x^4)* sum(x*y) - sum(x^3)*sum(x^2*y)
delta_a = x4 * xy - x3 * x2_y
# delta b = sum(x^2*y) * sum(x^2) - sum(x*y) * sum(x^3)
delta_b = x2_y * x2 - xy * x3

a = delta_a / e
b = delta_b / e

def f(a, b, x):
    return a * x + b * x**2

# теоритический у
y = [f(a, b, i) for i in xi]

print('a = {} b = {}'.format(a, b))
print('x^2 = {} x^3 = {} x^4 = {} xy = {} x^2*y = {}'.format(x2, x3, x4, xy, x2_y))

#d = np.polyfit(xi ,yi, 30)
#p = np.poly1d(d)

plt.grid(True)
plt.scatter(xi, yi)
plt.plot(xi, y, 'orange')
plt.legend(['Эксперемент','Теория'])
plt.show()