# 1286: Pares incremento
# Jhonny

def leerVector2(v):
    str = list(map(int, input().split()))
    i = 0
    while str[i] != 0:
        v.append(str[i])
        i = i + 1
        
def proceso(v, n):
    c = 0
    for i in range(n-1):
        if v[i] < v[i+1]:
            c = c + 1
    return c
    
# Entrada
k = int(input())
for i in range(k):
    v = []
    leerVector2(v)
    n = len(v)
    
    # Proceso
    c = proceso(v, n)

    # Salida
    print(c)