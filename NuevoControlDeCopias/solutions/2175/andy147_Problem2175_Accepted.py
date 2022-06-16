nroCasos = int(input())
for k in range(0, nroCasos, 1):
    nf = int(input())
    a = -1
    b = 1
    c = 0
    i = -1
    d = 0
    while nf != d:
        c = a + b
        d = c
        a = b
        b = c
        i = i +1
    if nf == 0:
        print(0)
    else:
        print(i)
