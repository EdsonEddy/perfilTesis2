import math
a=int(input())
b=int(input())
r=1
for i in range (1, a+1):
    if(i==a):print(r)
    else: print(r,end=' ')
    r=r*10+1
if b==0:
    print ("error")
