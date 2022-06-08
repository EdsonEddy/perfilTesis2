# 1291: Lectura3
# Jhonny
import sys
def leerVector1(v, linea):
    str = list(map(int, linea.split()))
    i = 0
    while str[i] != 0:
        v.append(str[i])
        i = i + 1

for linea in sys.stdin:
    
    # Entrada
    v = []
    leerVector1(v, linea)
    
    # Proceso
    s = sum(v)

    # Salida
    print(s)