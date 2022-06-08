casos=int(input())
for i in range(casos):
    a,b=map(int,input().split())
    li=list(map(int,input().split()))
    suma=0
    for j in range(a,b+1):
        suma=suma+li[j]
    print(suma)