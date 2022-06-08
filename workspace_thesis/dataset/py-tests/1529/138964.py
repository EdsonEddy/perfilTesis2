import math
T=int(input())
for i in range(T):
    x,n=map(int,input().split())
    y=0
    j=1
    cd=int(math.log10(x))+1
    while j <= n:
        d=int(x/10**(cd-1))
        x=x%(10**(cd-1))
        y=x*10+d
        x=y
        j=j+1
    print(x)