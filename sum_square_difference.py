import numpy as np

def sum_square_difference(n):
    l1 = np.abs(sum([x ** 2 for x in range(n)]) - (sum([y for y in range(n)])**2))
    return l1

sum_square_difference(101)
