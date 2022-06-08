size,giro=map(int,input().split())
matriz=[]
for i in range(size):
    elemento=list(map(int,input().split()))
    matriz.append(elemento)
if giro==360:
    nro=0
else:
    nro=giro//90
for k in range(nro):
    newmatriz = []
    for i in range(size):
        matrizaux=[]
        for j in range(size-1,-1,-1):
            matrizaux.append(matriz[j][i])
        newmatriz.append(matrizaux)
    matriz=newmatriz
for i in matriz:
    print(*i)