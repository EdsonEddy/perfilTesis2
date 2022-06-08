# 1300: Igual al Ultimo
# Jhonny
import sys

def leerVector(v, n):
    str = list(map(int, input().split()))
    for i in range(n):
        v.append(str[i])

def proceso(v, n):
    y = v[n-1]
    c = 0
    for x in v:
        if x == y:
            c = c + 1
    return c


for linea in sys.stdin:
    if linea == "\n":
        break
    
    # Entrada
    n = int(linea)
    v = []
    leerVector(v, n)

    # Proceso
    c = proceso(v, n)

    # Salida
    print(c)