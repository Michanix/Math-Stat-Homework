import matplotlib.pyplot as plt
from statistics import mode, median
from math import sqrt


arr = [200, 271, 295, 225, 268, 245, 275, 248, 250, 270,
       310, 315, 345, 350, 270, 270, 295, 360, 300, 285, 
       270, 260, 210, 274, 300, 275, 300, 260, 260, 260, 
       298, 281, 284, 291, 280, 235, 289, 240, 280, 230, 
       300, 290, 289, 292, 360, 300, 365, 290, 330, 290,
       327, 295, 250, 337, 249, 350, 271, 298, 300, 345,
       232, 235, 248, 273, 237, 256, 255, 238, 220, 220, 
       300, 275, 315, 300, 300, 261, 265, 262, 273, 355, 
       325, 335, 320, 300, 310, 310, 300, 330, 268, 300, 
       280, 340, 280, 260, 320, 345, 350, 279, 258, 260]

def calc_variance(arr, avg):
    return sum([(i - avg)**2 for i in arr]) / (len(arr) - 1)

def main(arr):
    arr = sorted(arr)
    N = len(arr)
    # среднее
    avg = sum(arr) / len(arr)
    # минимум
    minimum = min(arr)
    # максимум
    maximum = max(arr)
    # выборочную дисперсию
    D = calc_variance(arr, avg)
    # стандартное отклонение
    std = sqrt(D)
    # моду
    mod = mode(arr)
    # медиану 
    med = median(arr)
    # ассиметрия
    A = (sum([(i - avg)**3 for i in arr]) / N) / std**3
    # эксцесс
    E = (sum([(i - avg)**4 for i in arr]) / N) / std**4 - 3
    return (avg,minimum,maximum,D,std,mod,med,A,E)

def display_results(*args):
    print('''
    Среднее: {0}\n
    Минимум: {1}\n
    Максимум: {2}\n
    Выборочная дисперсия: {3}\n
    Стандартное отклонение: {4}\n 
    Мода: {5}\n 
    Медиана: {6}\n
    Ассиметрия: {7:.2f}\n 
    Эксцесс: {8:.2f}\n
    Kритические значения для показателей А и Е: {9:.2f}, {10:.2f}\n
    Интервальный вариационный ряд: {11}'''.format(*args))

def filter_data(data, list_of_intervals, k):
    values = [[] for i in range(k)]
    for i in range(len(data)):
        for j in range(len(list_of_intervals)):
            if list_of_intervals[j][0] <= data[i] <= list_of_intervals[j][1]:
                values[j].append(data[i])
    return values

def build_interval_row(arr, low_bound, width):
    arr = sorted(arr)
    # создаем интервалы с нижней границой и шириной
    # в виде списка из тюплей (нижняя, верхняя)
    intervals = [(i, i+width) for i in range(low_bound, arr[-1]+width, width)[:-1]]
    k = len(intervals)
    # вызываем функию filter_data() которой передаём массив,
    # вычисленный на прошлой строке интервалы
    # и количество интервалов k
    filtered_values = filter_data(arr, intervals, k)
    # подсчитываем количество значений в каждом интервале
    filtered_values_count = [len(i) for i in filtered_values]
    # составляем интервальный вариационный ряд,
    # который представлен ввиде dictionary
    table = dict(zip(intervals, filtered_values_count))
    return table

def calc_pustqlnikov(arr):
    N = len(arr)
    # Е.И. Пустыльник
    Akr = 3 * sqrt((6*(N - 1)/((N+1) * (N+3))))
    Ekr = 5 * sqrt((24 * N * (N-2)*(N-3)) / ((N+1)**2 * (N+3) * (N+5)))
    return Akr, Ekr

def t_test(arr):
    x1 = arr[:len(arr)//2]
    x2 = arr[len(arr)//2:]
    x1_avg = sum(x1) / len(x1)
    x2_avg = sum(x2) / len(x2)
    s1 = calc_variance(x1, x1_avg)
    s2 = calc_variance(x2, x2_avg)

    t = (x1_avg - x2_avg) / sqrt(s1/len(x1) + s2/len(x2))
    return t

def z_test(arr):
    d = calc_variance(arr)
    # standard error
    se = d / sqrt(len(arr))
    

def empr_f(arr):
    s = 0
    f = []
    for i in arr:
        x = s / sum(arr)
        s += i
        f.append(round(x, 2))
    return f

# main() return tuple
# so we can unpack the values of tuple accordingly
avg, minimum, maximum, D, std, mod, med, A, E = main(arr)
Akr, Ekr = calc_pustqlnikov(arr)
# интервальный вариационный ряд
intervals_row = build_interval_row(arr, 200, 30)

# ввывод результатов
display_results(avg, minimum, maximum, D, std, mod, med, A, E, Akr, Ekr, intervals_row)
print("T-критерий: {:.2f}".format(t_test(arr)))
# графики
fig, ax = plt.subplots()
ax.hist(arr, range=(minimum, maximum))
plt.show()