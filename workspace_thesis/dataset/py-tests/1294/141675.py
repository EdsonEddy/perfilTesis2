import sys

def s(x,y):
    #global v
    suma=0
    for k in range(x,y+1):
        suma=suma+v[k]
    return suma

v=[]
for n in sys.stdin:#hasta n casos de prueba
    n=int (n)
    for i in range(n):
        m,a,b=map(int,input().split())
        v=list(map(int,input().split()))
        print(s(a,b))