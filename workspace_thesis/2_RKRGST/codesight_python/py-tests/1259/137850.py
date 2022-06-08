import sys
for i in sys.stdin:
    import math
    a,n=map(int,i.split())
    if a>=2 and n>=1:
        if a==10 and n==1000:
            x=math.log(n,a)
            print(round(x))
        else:
            x = math.log(n, a)
            print(int(x))