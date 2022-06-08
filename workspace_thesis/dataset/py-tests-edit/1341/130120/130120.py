while True:
    try:
        n = int(input())
        a = 0
        b = 1
        fib = 0
        while n > 0:
            n = n - 1
            fib = a + b
            b = a
            a = fib
        print(fib)
    except ValueError:
        break