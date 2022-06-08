import math
n,k=map(int,input().split())
c=0
p=int(math.log10(n))
x=p+1
while k>0:
    d=int(n/(math.pow(10,p)))
    n=n%(math.pow(10,p))
    p=p-1
    k=k-1
print(x,d)
    