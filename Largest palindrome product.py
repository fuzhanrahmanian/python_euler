import numpy as np


def lagest_palindrome():
    palindrome = []
    for i in np.arange(100, 1000, 1):
        for j in np.arange(100, 1000, 1):
            n = i * j
            if len(str(n)) == 5 and int(str(n)[0]) == int(str(n)[-1]) and int(str(n)[1]) == int(str(n)[-2]):
                palindrome.append(n)
            elif int(str(n)[0]) == int(str(n)[-1]) and int(str(n)[1]) == int(str(n)[-2]) and int(str(n)[2]) == int(
                    str(n)[-3]):
                palindrome.append(n)
    return np.max(palindrome)


if __name__ == '__main__':
    print(lagest_palindrome())
