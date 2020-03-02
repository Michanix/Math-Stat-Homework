import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import numpy as np
from math import *


def empr_f(arr):
    s = 0
    f = []
    for i in arr:
        x = s / sum(arr)
        s += i
        f.append(x)
    return f


def find_median(arr):
    data = sorted(arr)
    n = len(arr)
    if n % 2 == 1:
        return data[n//2]
    i = n//2
    return (data[i - 1] + data[i])/2


# data
x = [10.6, 15.6, 20.6, 25.6, 30.6, 35.6, 40.6]
m = [8, 10, 60, 12, 5, 3, 2]
# эмпирическую функия
f = empr_f(m)
# относительные частоты
wi = [i/sum(m) for i in m]

# 3) определить эмпирически
# математическое ожидание (выборочное среднее)
avg = sum([i*j for i, j in zip(x, m)]) / sum(m)
# дисперсия
D = sum([(i - avg)**2 * j for i, j in zip(x, m)]) / sum(m)
# стандартное (среднееквадратичное) отклонение
standard_div = sqrt(D)
#standard_div = sqrt(dis)
# медиану;
med = find_median(m)
# %
k_var = standard_div / avg * 100
print('''Mатематическое ожидание (выборочное среднее): {}\n
Дисперсия: {}\n
Медиана: {}\n
Cтандартное (среднееквадратичное) отклонение: {}\n
Коэффициент вариации: {}
        '''
      .format(avg, D, med, standard_div, k_var))

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharex='row', figsize=(20, 30))
fig.subplots_adjust(hspace=0.5)
# кумулятивная кривая
ax1.plot(x, f, 'o-')
ax1.grid(True)
ax1.set(title='кумулятивная кривая',
        xlabel='x',
        ylabel='f')
# полигон
ax2.plot(x, m, 'o-')
ax2.grid(True)
ax2.set(title='полигон', xlabel='x',
        ylabel='m')
# histogramm
ax3.bar(x, m, width=2.0)
ax3.grid(True)
ax3.set(title='гистограммa', xlabel='x',
        ylabel='m')

plt.show()