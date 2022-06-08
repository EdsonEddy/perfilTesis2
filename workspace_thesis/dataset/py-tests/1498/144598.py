def entero(x):
    x = int(x)
    c = 0
    foo = 0
    while x > 0:
        d = x % 10
        x = x //10
        foo = foo + (d * (2 ** c))
        c += 1

    return foo

while True:
    x = input()
    r = ''
    while len(x) > 0:
        aux = ''
        for i in range(8):
            aux += x[i]
        aux = entero(aux)
        res = chr(aux)
        r += str(res)
        x = x[8:]
    print(r)