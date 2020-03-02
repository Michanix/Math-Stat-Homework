# источник http://qxov.narod.ru/spirmen.html
from random import randrange


test1 = [randrange(100) for i in range(1,21)]
test2 = [randrange(100) for i in range(1,21)]

test3 = [i for i in range(1,11)]
test4 = [i for i in range(1,11)]

def get_ranks(arr):
    ranks = []
    arr.sort()
    for i in arr:
        c1 = 0
        c2 = 0
        for j in arr:
            if j < i:
                c1 += 1
            elif i == j:
                c2 += 1
        ranks.append((c1+(c2-1)/2 + 1))
    return ranks

def f_helper(x):
    return (x**3 - x) / 12

# При наличии одинаковых рангов расчитать поправки
def calculate_errors(arr):
    t = []
    for i in arr:
        for j in arr:
            if i == j:
                t.append(f_helper(j))
    if t != []:
        return sum(t)
    return 0

def main(arr_A, arr_B):
    # N - количество испытуемых участвовавших в ранжировании
    N = len(arr_A + arr_B)
    # вычисляем ранги для ряда А и Б
    ranks_A = get_ranks(arr_A)
    ranks_B = get_ranks(arr_B)
    # проверяем присутсвуют ли одинаковые ранги
    # если да, то расчитываем поправки, 
    # если нет, то возвращяем 0
    Ta = calculate_errors(ranks_A)
    Tb = calculate_errors(ranks_B)
    # sum(d**2) - сумма квадратов разностей между рангами
    d = sum([(i-j)**2 for i,j in zip(ranks_A, ranks_B)])
    # коэффициент ранговой корреляции
    Rs = 1 - 6 * ((d + Ta + Tb) / (N**3 - N))
    return Rs
result = main(test4, test3)
print('Kоэффициент ранговой корреляции: {}'.format(result))