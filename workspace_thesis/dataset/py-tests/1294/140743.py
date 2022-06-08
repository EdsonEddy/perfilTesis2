# 1294: Suma en rango
# Jhonny

def leerVector(v, n):
    str = list(map(int, input().split()))
    for i in range(n):
        v.append(str[i])
        
def imprimeVector(v, n):
    i = 0
    for x in v:
        if i > 0:
            print(end=" ")
        print(x, end="")
        i = i + 1

def sumaRango(v, n, i, j):
    rango = v[i:j+1]
    s = sum(rango)
    return s

n = int(input())
for t in range(n):
    
    # Entrada
    m, i, j = map(int, input().split())
    v = []
    leerVector(v, m)
    
    # Proceso
    s = sumaRango(v, n, i, j)

    # Salida
    print(s)
