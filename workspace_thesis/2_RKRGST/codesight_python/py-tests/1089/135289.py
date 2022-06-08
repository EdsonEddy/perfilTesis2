import math
n=int(input())
x=int(math.log(n,10))+1
if x%2==0:
    print("*")
else:    
    y=(x//2)+1
    print(y)
