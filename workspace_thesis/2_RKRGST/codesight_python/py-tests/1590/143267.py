import sys
def sumadig(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n = n // 10
    return suma
for x in sys.stdin:
    try:
        n, a, b = map(int, x.split())
        sc = 0
        for i in range(1, n + 1):
            suma = sumadig(i)
            if b >= suma >= a:
                sc += i
        print(sc)
    except:
        break