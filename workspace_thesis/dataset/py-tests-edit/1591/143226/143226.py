def esPrimo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


x = int(input())
for i in range(x):
    n = int(input())
    s = ''
    while n > 0:
        dig = n % 10
        if esPrimo(dig) and dig != 1 and dig != 0:
            s = str(dig) + s
        n = n // 10
    if s == '':
        print(-1)
    else:
        print(s)