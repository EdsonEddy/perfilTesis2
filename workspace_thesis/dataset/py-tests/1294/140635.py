from sys import*

def suma(v,a,b):
    res=0
    for i in range (a,b+1):
        res+=int(v[i])
    return(res)


n=int(input())#para casos de prueba establecido
for i in range(n):
    n,a,b=map(int, input().split())
    v=input().split()#ya estoy haciendo una lista
    #print(v)
    print(suma(v,a,b))
    