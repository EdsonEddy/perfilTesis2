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
    suma = 0
    for i in range(1,n+1):
        if i > 9:
            foo = sumar_digitos(i)
            v[i-1] = foo
        else:
            v[i-1] = i
    for k in range(len(v)):
        if a <= v[k] <= b:
            suma += k+1
    print(suma)