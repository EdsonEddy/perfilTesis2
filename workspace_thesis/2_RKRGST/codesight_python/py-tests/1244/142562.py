import math
b=int(input())
for c in range(1,b+1):
    a=input().split()
    a=list(a)
    if a[0]=="rectangle":
        d=float(a[1])*float(a[2])
        print("{0:.2f}".format(d))
    else:
        d=math.pi*float(a[1])**2
        print("{0:.2f}".format(d))