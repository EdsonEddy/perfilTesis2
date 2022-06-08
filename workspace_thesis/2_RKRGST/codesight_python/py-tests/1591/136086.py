import math
g= int(input())
for i in range(1,g+1):
    z=int(input())
    x=z
    cd=int(math.log10(z))
    y=0
    while (z>0):
        d=z//(10**cd)
        z=z%(10**cd)
        cd=cd-1
        if (d==2 or d==3 or d==5 or d==7):
            y=y*10+d
    if(y==0):
        print("-1")
    else:
        print(y)