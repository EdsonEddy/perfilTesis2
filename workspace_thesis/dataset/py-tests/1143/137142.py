import math
t=int(input())
for pe in range(t):
    n=int(input())
    a=-1
    b=1
    c=0
    s=0
    if n!=0:
        for i in range(n):
            f=a+b+c
            s=s+f
            a=b
            b=c
            c=f
        print(s)
    else:
        print("error")