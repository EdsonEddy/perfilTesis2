import math
n,k=map(int,input().split())
cd=int(math.log(n,10)+1)
cd1=cd
for i in range(1,k+1):
    d=n//(10**(cd1-1))
    n=n%(10**(cd1-1))
    cd1=cd1-1
print(cd,d)