import math
n=int(input())
a=int((math.log(n,10)))+1
if a%2!=0:
    if a==1:
        b=1
    elif a==3:
        b=2
    elif a==5:
        b=3
    for i in range(b):
        d=n%10
        n=int(n/10)
    print(d)
else:
    print("*")