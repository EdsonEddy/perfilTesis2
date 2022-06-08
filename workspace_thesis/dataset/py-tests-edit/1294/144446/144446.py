def llenar(n):
    lista=[]
    c=0
    for i in n:
            lista.insert(c, i)
            c = c + 1
    return lista
n=int(input())
for i in range (n):
    a,b,c=map(int,input().split())
    x=input().split()
    lista=[]
    lista=llenar(x)
    s=0
    while b<=c:
        d=int(lista[b])
        s=s+d
        b=b+1
    print(s)