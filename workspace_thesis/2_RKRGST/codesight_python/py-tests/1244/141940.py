import math
a=int(input())
for i in range(a):
        a=input().split()
        s=a[0]
        d=float(a[1])
        if(s=="circle"):
            e=float(math.pi*d*d)
            print("{0:.2f}".format(e))
        else:
            f=float(a[2])
            y=d*f
            print("{0:.2f}".format(y))
