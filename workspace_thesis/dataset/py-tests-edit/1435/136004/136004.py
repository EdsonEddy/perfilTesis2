import math
a,k=map(int,input().split())
c=int(math.log10(a)+1)
aux=c
d=0
ck=0
while ck<k:
    c=c-1
    d=int(a/pow(10,c))
    ck=ck+1
    a=a%pow(10,c)
print(aux,d)
