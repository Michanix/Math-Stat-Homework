from math import sqrt
from random import randrange

arr1 = [i for i in range(1, 11)]
arr2 = [i for i in range(1, 11)]

arr3 = [randrange(i) for i in range(1, 11)]
arr4 = [randrange(i) for i in range(1, 11)]

def avg(data):
    return sum(data) / len(data)

def std(data):
    mu = avg(data)
    std = (sum([(i - mu)**2 for i in data]) / len(data))**0.5
    return std

def koef_pirsona(x, y):
    # x,y - list of values
    avg_x = avg(x)
    avg_y = avg(y)
    std_x = std(x)
    std_y = std(y)
    avg_xy = avg([i*j for i,j in zip(x,y)])
    result = (avg_xy - avg_x * avg_y) / (std_x * std_y)
    return result

print(koef_pirsona(arr3, arr4))
