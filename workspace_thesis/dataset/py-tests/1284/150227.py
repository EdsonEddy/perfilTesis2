while True:
    a, b = map(int, input().split())
    a = bin(a)
    a = a.lstrip("0b")
    b = bin(b)
    b = b.lstrip("0b")

    x = list(a)
    y = list(b)

    m = len(x)
    mezcla = ''
    for z in range(m):
        mezcla = mezcla + x[z] + y[z]
    print(mezcla)




