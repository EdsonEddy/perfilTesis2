import math
n=int(input())
for i in range(0,n,1):
    f=int(math.pow(2,math.pow(2,i)))+1
    if i==n-1:
         print(f)
    else:
         print(f,end=" ")


