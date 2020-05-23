import numpy as np


def prime_factor(x):
    i = 2
    prime_factors = []
    while x > 1:
        if x % i == 0:
            x = int(x/i)
            prime_factors.append(i)
        else:
            i += 1

    return np.max(prime_factors)

prime_factor(600851475143)
