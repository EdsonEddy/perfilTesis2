while True:
    from math import *
    n=int(input())
    for i in range(n):
        a=input().split()
        A=a[0]
        B=a[1]
        if len(a)==3:
            C=a[2]
        if A=='rectangle':
            area=(float(B)*float(C))
            print("{:.2f}".format(area))
            A,B,C=0,0,0
        else:
            if A=='circle':
                circulo=(float(pi)*float(B)**2)
                print("{:.2f}".format(circulo))
                A,B,C=0,0,0