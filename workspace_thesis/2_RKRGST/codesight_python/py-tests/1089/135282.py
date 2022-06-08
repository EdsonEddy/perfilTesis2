import math
n=int(input())
d=int(math.log(n,10))+1
x=d%2
a=0
if x==0:
    print("*")
else:
    d=round(d/2)
    n=n//(10**d)
    n=n%10
    print (n)