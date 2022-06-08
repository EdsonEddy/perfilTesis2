
def llenar(n):
    lista=[]
    c=0
    for i in n:
            lista.insert(c, i)
            c = c + 1
    return lista
while 1>0:
    x=int(input())
    n=input().split()
    lista=[]
    lista=llenar(n)
    c=0
    for i in n:
        if i==lista[x-1]:
            c=c+1
    print(c)
