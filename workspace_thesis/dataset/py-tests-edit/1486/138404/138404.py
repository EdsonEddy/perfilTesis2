import math
sw=0
s=2
a=-1
b=1
f=a+b
a=b
b=f
n=int(input())
for i in range(n):
    if(i%2==0):
        f=a+b
        print(f)
        a=b
        b=f
    else:
        print(s)
        s=s+2
