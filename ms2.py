import matplotlib.pyplot as plt
from math import *
from statistics import median, mode

# source: http://mathprofi.ru/formula_dispersii_standartnoe_otklonenie_koefficient_variacii.html#fd

data = [530, 570, 660, 701, 700, 670, 825, 780, 700, 600, 665, 785, 840,
        805, 820, 818, 900, 860, 830, 840, 797, 785, 550, 900, 760, 660,
        650, 910, 905, 640, 760, 810, 850, 820, 885, 850, 873, 773, 870,
        880, 775, 950, 970, 860, 1000, 682, 1000, 574, 1050, 980, 760, 930,
        955, 960, 740, 1000, 608, 1220, 708, 1190, 580, 695, 530, 600, 881,
        1190, 821, 699, 1200, 600, 828, 817, 800, 819, 943, 883, 595, 890,
        880, 885, 1180, 840, 1230, 1200, 700, 953, 1100, 788, 900, 860, 800,
        1040, 1000, 767, 969, 1160, 700, 1210, 997, 900]

# interval
x = 100
# amount of intervals
k = 7
# sorting and removing duplicates
data = sorted(data)

# my functions
def filter_data(data, list_of_intervals, k):
    values = [[] for i in range(k)]
    for i in range(len(data)):
        for j in range(len(list_of_intervals)):
            if list_of_intervals[j][0] <= data[i] <= list_of_intervals[j][1]:
                values[j].append(data[i])
    return values


def empr_f(arr):
    s = 0
    f = []
    for i in arr:
        x = s / sum(arr)
        s += i
        f.append(round(x, 2))
    return f


# action
# разбиваем на интервалы и группируем в список списков
# работает только с отсортированными даннами по возрастанию
# convert to tuples so later use as keys in dict
intervals = [(i, i+x) for i in range(data[0], data[-1]+x, 100)[:-1]]
# середины интервалов
intervals_mid = [(i[0]+i[1])/2 for i in intervals]
# values that fits into ranges
filtered_values = filter_data(data, intervals, k)
# count how many values we have for each interval
filtered_values_count = [len(i) for i in filtered_values]
# относительные частоты
wi = [i/sum(filtered_values_count) for i in filtered_values_count]
# таблица интервалов
table = dict(zip(intervals, filtered_values_count))
# эмпирическая функция
f = empr_f(table.values())

# список значений из таблицы в отсортированном виде
x = sorted(list(table.values()))

# список интервалов
x_intervals = list(table.keys())
right_intervals_list = [i[1] for i in x_intervals]
# математическое ожидание (выборочное среднее)
Xe = sum([i*j for i, j in zip(intervals_mid, filtered_values_count)]
         ) / sum(filtered_values_count)
# дисперсия
D = sum([(i - Xe)**2 * j for i, j in zip(intervals_mid,
                                         filtered_values_count)]) / sum(filtered_values_count)
# стандартное (среднееквадратичное) отклонение
standard_div = sqrt(D)
#  моду и медиану;
med = median(filtered_values_count)
mod = mode(filtered_values_count)
# Коэффициент вариации
k_var = standard_div / Xe * 100
# ассиметрия
A = (sum([(i - Xe)**3 * j for i, j in zip(intervals_mid,
                                          filtered_values_count)]) / sum(filtered_values_count)) / standard_div**3
# эксцесс
E = (sum([(i - Xe)**4 * j for i, j in zip(intervals_mid,
                                          filtered_values_count)]) / sum(filtered_values_count)) / standard_div**4 - 3 

# словарь вычислений
calculation = {
    'table': table,
    'Xe': Xe,
    'D': D,
    'med': med,
    'mod': mod,
    'standard_div': standard_div,
    'k_var': k_var,
    'A': A,
    'E': E
}
print('''
интервальный вариационный ряд: {table}\n
Mатематическое ожидание (выборочное среднее): {Xe:.2f}\n
Дисперсия: {D:.2f}\n
Медиана: {med}\n
Мода: {mod}\n
Cтандартное (среднееквадратичное) отклонение: {standard_div:.2f}\n
Коэффициент вариации: {k_var:.2f}%\n
Ассиметрия:{A:.2f}\n 
Эксцесс:{E:.2f}
        '''.format(**calculation))


# plots
fig, ax = plt.subplots(1, 3, figsize=(20, 20))
# кумулятивная кривая
ax[0].plot([0]+right_intervals_list, [0]+f, 'o-')
ax[0].set(title="кумулятивная кривая")
#ax[0].set_xticks(x)
#  полигон
ax[1].plot(intervals_mid, wi, 'o-')
ax[1].set(title="полигон")
# Гистограмма
ax[2].hist(data,range=(530, 1130))
ax[2].set(title='Гистограмма')
# show plots
plt.show()