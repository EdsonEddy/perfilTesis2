# 1280 Cual Falta
# Jhonny
import sys

def leerVector(v, n):
    str = list(map(int, input().split()))
    for i in range(n):
        v.append(str[i])

def proceso2(v, n):
    v.sort()
    #print(v)
    i = 0
    while i < n:
        if v[i] != i+1:
            return i+1
        i = i + 1
    return i+1


for linea in sys.stdin:
    if linea == "\n":
        break
    
    # Entrada
    n = int(linea)
    n = n - 1
    v = []
    leerVector(v, n)

    # Proceso
    falta = proceso2(v, n)

    # Salida
    print(falta)
