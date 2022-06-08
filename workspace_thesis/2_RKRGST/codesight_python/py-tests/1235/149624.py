def todo (n,v):
    aux=[]
    aux2=[]
    dif=[]
    s,s2=0,0
    for i in range (1,n):
        for j in range (i):
            s= s+v[j]
        aux.append(s)
        s=0
    for i in range (n-1):
        for j in range (i+1,n):
            s= s+v[j]
        aux2.append(s)
        s=0
    for k in range (len (aux)-1):
        r=aux2[k]-aux[k]
        dif.append(r)
    return(min(dif))
while True:
    n=int(input())
    v=list(map(int,input().split()))
    print(todo(n,v))