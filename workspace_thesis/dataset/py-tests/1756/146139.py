def volverUno(c):
    while len(str(c)) != 1:
        k = 0
        for i in str(c):
            k += int(i)
        c = k#sum(str(c))
    return c

casos = int(input())
for i in range(casos):
    n = int(input()) % 6
    print(volverUno(2**(n+1)))