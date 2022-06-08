q=int(input())
n=list(map(int,input().split()))
sumlist=0
suma=0
for q in n:
    sumlist=sumlist+q
minimo=sumlist
for w in n[:-1]:
    suma=suma+w
    a=sumlist-suma
    b=a-suma
    if b<minimo and b>=0:
        minimo=b
print(minimo)