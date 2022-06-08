from math import *
def f(n,c):
    while c>0:
        n//=10
        c=c-1
    return n%10

n,k=map(int,input().split())
tam=int(log10(n))+1
c=tam-k
print(tam,f(n,c))
