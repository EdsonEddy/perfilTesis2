import math
h=int(input())
for i in range(h):
    x,n=map(int,input().split())
    m=int(math.log10(x))
    cont=1
    while cont<=n:
        nu=x//10**m
        x=x-(10**m*nu)
        x=x*10+nu
        cont=cont+1
    print(x)
