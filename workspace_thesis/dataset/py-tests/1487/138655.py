def esPrimo(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n :
        if n % i == 0:
            return False
        i = i + 1
    return True

for i in range(10000):
    n = int(input())
    if esPrimo(n):
        print("ES PRIMO")
    else:
        print("NO ES PRIMO")
    