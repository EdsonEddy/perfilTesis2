from math import *
n,k=map(int,input().split())
x=n
if (1<=n<10**18 and k<=n):
    cd=int(log(n,10))+1
    p=int(log(n,10))-k+1
    for i in range(p+1):
        d=x%10
        x=x//10
    print(cd,d)