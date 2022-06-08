def sumar_digitos(x):
    si = 0
    while x > 0:
        d = x % 10
        x = x // 10
        si += d
    return si

v = [0] * 10010
while True:
    n, a, b = map(int, input().split())
    # v = [0] * n
    c = 0
    suma = 0
    for i in range(1, n+1):
        if i > 9:
            v[c] = sumar_digitos(i)
        else:
            v[c] = i
        if a <= v[c] <= b:
            suma += i
        c += 1
    print(suma)