def sumar_digitos(x):
    suma = 0
    while x > 0:
        d = x % 10
        x = x // 10
        suma += d
    return suma


while True:
    n, a, b = map(int,input().split())
    v = [0] * n
    c = 0
    suma = 0
    for i in range(1,n+1):
        if i > 9:
            foo = sumar_digitos(i)
            v[c] = foo
            if a <= v[c] <= b:
                suma += i
        else:
            v[c] = i
            if a <= v[c] <= b:
                suma += i
        c += 1
    print(suma)