while True:
    n = int(input())
    lib = n // 240
    res = n % 240
    che = res // 12
    pen = res % 12
    tup = (lib, che, pen)
    print(tup)