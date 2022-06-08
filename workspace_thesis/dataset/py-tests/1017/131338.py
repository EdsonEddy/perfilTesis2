N = int(input())
for casos in range(N):
    n, a = map(int, input().split())
    cad = str(a)
    dMa = 2
    for i in range(len(cad)):
        if int(cad[i]) + 1 > dMa:
            dMa = int(cad[i]) + 1
    for j in range(dMa, 10):
        nuevoN = ''
        cN = n
        while cN > 0:
            d = cN % j
            cN //= j
            nuevoN = str(d) + nuevoN
        if nuevoN == cad:
            break
    print(j)