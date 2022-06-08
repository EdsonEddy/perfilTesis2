from math import *
while True:
    n=int(input())
    r=0
    for i in range(1,n+1,1):
        r=r+log10(i)
    x=int(r+1)
    print(x)
