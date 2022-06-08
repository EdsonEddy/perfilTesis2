casos=int(input())
while casos>0:
    rangoA,rangoB=map(int,input().split())
    lista=[1]*rangoB
    sumando=0
    for i in range(rangoA-1):
        for j in range(i,rangoB):
            sumando=sumando+lista[j]
        rangoB=rangoB+1
        lista.append(sumando)
        sumando=0
    print(lista[rangoA])