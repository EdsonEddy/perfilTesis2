# 1315 Anti-Acumulada
# Jhonny
import sys

def leerVector(v, n):
    str = list(map(int, input().split()))
    for i in range(n):
        v.append(str[i])

def proceso(v, n):
    x = 0
    for i in range(n):
        if i > 0:
            print(end=" ")
        print(v[i]-x, end = "")
        x = v[i]
            
# Entrada
n = int(input())
v = []
leerVector(v, n)
 
# Proceso y Salida
proceso(v,n)    