def llenar(n):
    lista=[]
    c=0
    for i in n:
            lista.insert(c, i)
            c = c + 1
    return lista
n=int(input())
for i in range (n):
    a,b=map(int,input().split())
    x=input().split()
    lista=[]
    lista=llenar(x)
    s=0
    while a<=b:
        d=int(lista[a])
        s=s+d
        a=a+1
    print(s)

