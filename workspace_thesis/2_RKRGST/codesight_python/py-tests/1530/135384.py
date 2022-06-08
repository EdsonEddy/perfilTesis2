import math
n=int(input())
i=1
y=1
p=1
r=0
s=0
l=0
while i<=n:
    i=i+1
    x=int(input())
    d=int(math.log(x,10)+1)
    while y<=d:
        t=x%(10)
        x=int(x/(10))
        y=y+1
        while p<10:
            u=t%p
            p=p+1
            if u==0:
                s=s+1
        if s==2:
            q=t*(10**l)
            r=r+q
            l=l+1
        s=0
        p=1
    y=1
    l=0
    print(r)
    r=0