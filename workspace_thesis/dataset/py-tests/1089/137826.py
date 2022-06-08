import math
n=int(input())
m=n
if 1<=n<=99999:
    b=int(math.log10(n))
    bb=int(b/2)
    if b%2==0:
        for k in range(bb+1):
            c=pow(10,b)
            d=int(m/c)
            m=m%c
            b=b-1
        print(d)
    else:
        print("*")