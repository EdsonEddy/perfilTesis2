from math import pi
cas=int(input())
while cas>0:
    x=input().split()
    if x[0]=="rectangle":
        h=float(x[1])
        b=float(x[2])
        Area=b*h
    else:
        r=float(x[1])
        Area=pi*r**2
    print("{0:.2f}".format(Area))
    cas=cas-1