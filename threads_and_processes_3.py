'''3. Use Pool.apply() to get the row wise common items in list_a and list_b.
list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]'''
from multiprocessing import Pool

list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]


def common_items(list_1, list_2):
    return list(set(list_1).intersection(set(list_2)))


with Pool() as p:
    for i in range(4):
        print(p.apply(common_items, [list_a[i], list_b[i]]))
