import math
m=int(input())
for i in range(1,m+1,+1):
    n=int(input())
    cd=int(math.log10(n))
    y=0
    sw=False
    while n>0:
        d=n//(10**cd)
        n=n%(10**cd)
        cd=cd-1
        if(d==2 or d==3 or d==5 or d==7):
            y=y*10+d
            sw=True
    if (sw==True):
        print(y)
    else:
        print(-1)