from math import *
c=int(input())
for i in range (c):
    a=input().split()
    l=[]
    for j in a:
        l.append(j)
    if l[0]=="circle":
        b=pi*float(l[1])**2
    else:
        b=float(l[1])*float(l[2])
    print("{0:.2f}".format(b))
