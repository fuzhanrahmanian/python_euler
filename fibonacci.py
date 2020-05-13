def fibonacci(x, y, n):
    even_num = list()
    while n < 4000000:
        if n % 2 == 0:
            even_num.append(n)
        y = x
        x = n
        n = x + y

    return sum(even_num)



fibonacci(1, 0, 1)

