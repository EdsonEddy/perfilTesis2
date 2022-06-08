import math
t=int(input())
while t>0:
     n=int(input())
     e=0
     c,p=0,0
     while n>0:
        d=n%10
        n=n//10
        if d==2 or d==5 or d==7 or d==3:
            p=p+d*(10**e)
            e=e+1
            c=c+1
     if c==0:
        print(-1)
     else:
        print(p)
t=t-1