import numpy as np


def smallest_multiple(x):
    divi_list = []
    for i in np.arange(1, 21, 1):
        if x % i == 0:
            divi_list.append(True)
        else:
            divi_list.append(False)
    return divi_list

x = 1
while all(smallest_multiple(x)) != True:
    x += 1
print(x)


