import math
n=int(input())
a=int(math.log(n,10))+1
if a%2==0:
    print("*")
else: 
    b=(a//2)+1
    print(b)
