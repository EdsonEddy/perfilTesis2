import math
n,k=map(int,input().split())
c,d=0,0
x= int(math.log10(n)+1)
x=x-1
while n>0:
    d=n//(10**x)
    n=n-d*(10**x)
    c=c+1
    x=x-1
    if k==c:
        dig=d
    if n==10:
        c=c+1
print(c,dig)