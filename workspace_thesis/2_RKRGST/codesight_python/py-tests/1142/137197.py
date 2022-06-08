import math
a,b,n=map(int,input().split())
for i in range(2,n):
    f=pow(b,2)+a
    a=b
    b=f
print (f)