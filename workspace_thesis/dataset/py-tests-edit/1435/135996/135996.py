import math
n,k=map(int,input().split())
cd=int(math.log10(n))
y=cd+1
for i in range(1,k+1,+1):
        d=n//(10**cd)
        n=n%(10**cd)
        cd=cd-1
print(y,d)
