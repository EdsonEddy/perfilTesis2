import math
c=0
d=0
x=1
while(True):
    n=float(input())
    if(n==0):
        break
    elif(n>0):
        c=c+1
        if(n>=x):
            x=n
    else:
        c=c+1
        d=d+1
y=(d*100)/c
print(int(y))
print(int(x))