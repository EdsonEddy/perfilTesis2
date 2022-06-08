import math
n,k=map(int,(input().split()))
c=0
z=int(math.log10(n)+1)
if(k<=z):
    y=n
    dig=1
    u=z
    while (y>0):
        u=u-1
        dig=y//(10**(u))
        y=y%(10**(u))     
        c=c+1
        if(c==k):
            print(z,dig)
            break
        