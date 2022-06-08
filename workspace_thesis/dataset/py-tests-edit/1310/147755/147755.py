def burbuja(n,v):
    for i in range(n):
        for j in range(n-1):
            if v[j]<v[j+1]:
                aux=v[j]
                v[j]=v[j+1]
                v[j+1]=aux
    return

while True:
    n=int(input())
    m=list(map(int,input().split()))
    l=list(map(int,input().split()))
    burbuja(n,l)
    j=sum(m)
    c=0
    i=0
    while j>0:
        j=j-l[i]
        c=c+1
        i=i+1
    print(c)