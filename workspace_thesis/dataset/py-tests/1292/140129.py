# 1292: Lectura4
# Jhonny
def leerVector(v, n):
    str = list(map(int, input().split()))
    for i in range(n):
        v.append(str[i])

def suma(v, n):
    s = 0
    for i in range(n):
        s = s + v[i]
    return s

while True:

    # Entrada
    n = int(input())
    if n == 0:
        break
    
    v = []
    leerVector(v, n)
     
    # Proceso
    s = suma(v,n)
    
    # Salida
    print(s)
