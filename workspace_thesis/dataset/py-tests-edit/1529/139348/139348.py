from math import *
r=int(input())
while r>0:
    x,n=map(int,input().split())
    cd=int(log10(x))+1
    while n>0:
        x=x*10+x//(10**(cd-1))
        x=x%(10**cd)
        n=n-1
    print(x)
    r=r-1