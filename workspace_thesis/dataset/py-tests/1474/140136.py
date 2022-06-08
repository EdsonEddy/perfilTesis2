# 1474 - Nuevo vector
# Jhonny
def leerVector(v, n):
    str = list(map(int, input().split()))
    for i in range(n):
        v.append(str[i])

def imprimeVector(v, n):
    for x in v:
        print(x)

def proceso(v1, v2, v3, n):
    for i in range(n):
        o = input()
        if o == "+":
            v3.append(v1[i] + v2[i])
        elif o == "*":
            v3.append(v1[i] * v2[i])
        elif o == ">":
            v3.append(max(v1[i], v2[i]))
        elif o == "<":
            v3.append(min(v1[i], v2[i]))
     
# Entrada
n = int(input())
v1 = []
leerVector(v1, n)
v2 = []
leerVector(v2, n)

# Proceso
v3 = []
proceso(v1, v2, v3, n)

# Salida
imprimeVector(v3,n)