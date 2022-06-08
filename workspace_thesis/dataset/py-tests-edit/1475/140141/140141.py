# 1475 Invertir un rango
# Jhonny

def leerVector(v, n):
    str = list(map(int, input().split()))
    for i in range(n):
        v.append(str[i])
        
def imprimeVector(v, n):
    for x in v:
        print(x)

def proceso(v, n):
    rango = v[i:j+1]
    rango.reverse()
    v1 = v[:i] + rango + v[j+1:]
    return v1
    
# Entrada
n, i, j = map(int, input().split())
v = []
leerVector(v, n)

# Proceso
v = proceso(v, n)

# Salida
imprimeVector(v, n)
