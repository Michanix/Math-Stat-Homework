from random import randrange
from math import sqrt
# source: http://mathprofi.ru/asimmetriya_i_excess.html
# source: http://mathprofi.ru/moda_mediana_generalnaya_i_vyborochnaya_srednyaya.html#ismome
data = [randrange(1, 10) for i in range(100)]

# функция для распределения данных по интервалам
def filter_data(data, list_of_intervals, k):
    values = [[] for i in range(k)]
    for i in range(len(data)):
        for j in range(len(list_of_intervals)):
            if list_of_intervals[j][0] <= data[i] <= list_of_intervals[j][1]:
                values[j].append(data[i])
    return values

# find minimum and value in array
# return tuple(min, max)
def find_min_max(arr):
    mn = arr[0]
    mx = arr[0]
    for i in arr:
        if i < mn:
            mn = i
    for j in arr:
        if i > mx:
            mx = i
    return mn, mx


def main(data):
    if len(data) < 5:
        print('Слишком мало данных. Должно быть больше 5 чисел.')
        return None
    data = sorted(data)
    minimum = find_min_max(data)[0]
    maximum = find_min_max(data)[1]
    # количество интервалов
    k = 9
    # размах
    R = maximum - minimum
    # шаг
    h = R // k
    # дискретный ряд
    disc_row = {i: data.count(i) for i in data}
    # интервалы
    intervals = [(i, i+h) for i in range(minimum, maximum)]
    # середины интервалов
    intervals_mid = [(i[0]+i[1])/2 for i in intervals]
    # распрелить данные по интервалам
    data_into_intervals = filter_data(data, intervals, k)
    # определить количество значений в каждом интервале
    count_val_in_intervals = [len(i) for i in data_into_intervals]
    # интервальный ряд
    # Example: (a, b): c, где с количество значений в попавшее в данный интервал
    intervals_row = dict(zip(intervals, count_val_in_intervals))
    list_of_keys = sorted(list(intervals_row.keys()))
    list_of_values = sorted(list(intervals_row.values()))
    # среднее ариф.
    mu = sum([i*j for i, j in zip(intervals_mid, count_val_in_intervals)]
             ) / sum(count_val_in_intervals)
    # модальный интервал
    low_mod = list(intervals_row.keys())[len(intervals_row.keys())//2]
    n = [(list_of_keys[i-1], list_of_keys[i+1], v)
         for i, v in enumerate(list_of_keys) if v == low_mod]
    # нижняя граница модального интервала
    x0 = low_mod[0]
    # частота модального интервала;
    n_mod = intervals_row[low_mod]
    # частота предыдущего интервала
    n_mod_prev = intervals_row[n[0][0]]
    # частота следующего интервала
    n_mod_next = intervals_row[n[0][1]]
    # накопленная частота предыдущего интервала
    sum_of_prev_mods = sum(
        list_of_values[:list(intervals_row.values()).index(n_mod)])
    # модa
    mode = x0 + ((n_mod - n_mod_prev) /
                 ((n_mod-n_mod_prev) + (n_mod-n_mod_next))) * h
    # медианa
    mediana = x0 + ((0.5 * sum(list_of_values) - sum_of_prev_mods) / n_mod) * h
    # дисперсия
    D = sum([(i - mu)**2 * j for i, j in zip(intervals_mid,
                                             count_val_in_intervals)]) / sum(count_val_in_intervals)
    # центральные моменты порядка 1, 2, 3, 4
    # 3
    m3 = sum([(i - mu)**3 * j for i, j in zip(intervals_mid,
                                              count_val_in_intervals)]) / sum(count_val_in_intervals) 
    m4 = sum([(i - mu)**4 * j for i, j in zip(intervals_mid,
                                              count_val_in_intervals)]) / sum(count_val_in_intervals)
    # std
    standard_div = sqrt(D)
    A = m3 / standard_div**3
    # эксцесс
    E = m4 / standard_div**4 - 3
 
    answers = {
        'disc_row': disc_row,
        'intervals_row': intervals_row,
        'mu': mu,
        'D': D,
        'mediana': mediana,
        'mode': mode,
        'standard_div': standard_div,
        'A': A,
        'E': E,
        'm3': m3,
        'm4': m4
    }

    print('''
    Дискретный ряд:{disc_row}\n
    Интервальный ряд:{intervals_row}\n
    Среднее значение:{mu:.2f}\n
    Дисперсия:{D:.2f}\n
    Медиана:{mediana:.2f}\n
    Мода:{mode:.2f}\n
    Стандартное отклонение:{standard_div:.2f}\n
    Ассиметрия:{A:.2f}\n
    Эксцисс:{E:.2f}\n
    Центральные моменты порядка 3: {m3:.2f}\n
    Центральные моменты порядка 4: {m4:.2f}
    '''.format(**answers))


main(data)