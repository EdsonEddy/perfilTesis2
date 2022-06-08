import math
l,r,k=map(int,input().split(" "))
c=0
if(l>r):
    aux=l
    l=r
for i in range(l,r+1,1):
    if(i%k==0):
        c=c+1
print(c)
