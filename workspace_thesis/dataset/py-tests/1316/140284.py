# 1300: Igual al Ultimo
# Jhonny
import sys

def leerVector(v, n):
    str = list(map(int, input().split()))
    for i in range(n):
        v.append(str[i])

def suma(a, b, n):
    s = 0
    for i in range(n):
        s = s + a[i] * b[i]
    return s

for linea in sys.stdin:
    if linea == "\n":
        break
    
    # Entrada
    n = int(linea)
    a = []
    leerVector(a, n)
    b = []
    leerVector(b, n)

    # Proceso
    a.sort()
    b.sort(reverse=True)
    s = suma(a, b, n)

    # Salida
    print(s)