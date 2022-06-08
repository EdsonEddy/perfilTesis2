import math
n=int(input())
for i in range (n):
    a,b=map(int,input().split())
    if 2<=a<=10**5 and 2<=b<=10**5:
        x=max(a, b)
        y=min(a, b)
        while y:
            mcd=y
            y=x%y
            x=mcd
        print(x)