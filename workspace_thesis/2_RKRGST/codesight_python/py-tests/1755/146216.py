n=int(input())
while n>0:
    a,b=map(int,input().split())
    l=[1]*b
    suma=0
    for i in range(a-1):
        for j in range(i,b):
            suma=suma+l[j]
        b=b+1
        l.append(suma)
        suma=0
    print(l[a])
    n-=1