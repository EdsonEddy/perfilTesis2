def esPrimo(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n :
        if n % i == 0:
            return False
        i = i + 1
    return True
c = 0
i = 1
while i >= c:
    n = int(input())
    c = c+1
    if esPrimo(n):
        print("ES PRIMO")
    else:
        print("NO ES PRIMO")
    i = i + 1
    