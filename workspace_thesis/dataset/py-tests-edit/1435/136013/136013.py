import math
a,b,=map(int,input().split())
cd=int(math.log10(a))
x=cd+1
for i in range (1,b+1,1):
    d=a//(10**cd)
    a=a%(10**cd)
    cd=cd-1
print(x, d)
