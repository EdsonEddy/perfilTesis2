from math import *
T=int(input())
a=0
while T>0:
    x,n=map(int,input().split())
    e=int(log10(x))+1
    e=e-1
    while n>0:
        d=x//(10**e)
        b=x- d*(10**e)
        x=b*10+d
        n=n-1
    print(x)
    T=T-1
