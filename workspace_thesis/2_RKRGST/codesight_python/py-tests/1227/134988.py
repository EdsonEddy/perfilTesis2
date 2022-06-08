import math
a,b=map(int,input().split())
r=0
while(a>=b):
    a=a-b
    r=r+1
print(r,a)    