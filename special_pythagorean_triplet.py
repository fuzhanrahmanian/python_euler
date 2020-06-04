import numpy as np

def pythagorean_triplet():
    for a in range(1, 1001):
        for b in range(a+1, 1001):
            c = np.sqrt(a**2 + b ** 2)
            if a + b + c == 1000.0:
                x = a * b * c
                break
    return x

print(pythagorean_triplet())