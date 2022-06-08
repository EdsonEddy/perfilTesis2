import math
n,k=map(int,input().split())
e=0
d=0
if n>=1 and n<=1*10**18:
    e=math.log10(n)
    e=int(e+1)
    k=e-k
    for i in range(1,k+2):
        d=n%10
        nn=n//10
        n=nn
        i+=1
print(e,d)
