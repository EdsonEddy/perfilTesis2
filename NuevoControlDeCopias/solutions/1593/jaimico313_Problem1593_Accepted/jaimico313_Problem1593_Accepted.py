import sys
def descomposicion(valor):
    sumatoria=0
    while valor>=5:
        sumatoria+=valor//5
        valor=valor//5
    return sumatoria
numero=500001
suma=0
for i in sys.stdin:
    casos=int(i)
    auxiliar=[]
    for l in range(4,numero):
        if descomposicion(l)>casos:
            break
        elif descomposicion(l) == casos:
            auxiliar.append(l)
    if len(auxiliar) == suma:
        print(suma)
    else:
        print(*auxiliar)
