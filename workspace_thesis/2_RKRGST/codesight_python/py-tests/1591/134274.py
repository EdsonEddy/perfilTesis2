from math import sqrt
t=int(input())
c=1
while c<=t:
    po=1
    y=0
    c2=0
    n=int(input())
    while n!=0:
        d=n%10
        n=n//10
        if d==2 or d==3 or d==5 or d==7:
            y=d*po+y
            po=po*10
            c2=1
    if c2==0:
        y=-1
    c=c+1
    print (y)
    