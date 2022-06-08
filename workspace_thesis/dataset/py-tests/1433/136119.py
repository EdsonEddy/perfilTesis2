import math
x,z=map(int,input().split())
u=0
if(x==1):
    x=x*2
for n in range(x,z+1):
    i=2
    Sw=True
    while (i*i<=n):
        if n%i==0:
            Sw=False
            break
        i=i+1
    if Sw:
        u=u+1
print(u)
        