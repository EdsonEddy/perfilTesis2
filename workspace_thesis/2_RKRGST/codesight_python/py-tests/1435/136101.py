import math
n,k=map(int,input().split())
b=cd=int(math.log10(n))+1
cdig=0
while n >0:
    d=n//(10**(cd-1))
    cdig+=1
    n=n%(10**(cd-1))
    cd=cd-1
    if cdig == k:
        a=d
        break
print(b,a)