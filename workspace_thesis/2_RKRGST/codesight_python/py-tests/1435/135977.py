import math
c=0

n,k=map(int,input().split())
b=int(math.log10(n))
for i in range(b+1):
    m=n//10**b
    c=c+1
    if c==k:
        a=m
    n=int(n%10**b)
    b=b-1
print(c,a)
