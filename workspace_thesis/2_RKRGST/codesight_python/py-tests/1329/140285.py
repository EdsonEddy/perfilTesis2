# 1329: Ordenando en rango
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

def proceso(v, n):
    rango = v[i:j+1]
    rango.sort()
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