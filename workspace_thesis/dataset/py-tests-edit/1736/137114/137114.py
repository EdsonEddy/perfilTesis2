import math
n=int(input())
for i in range(0,n):
    f = pow(2, 2 ** i) + 1
    if(i==n-1):
        print (f)
    else:
        print(f,end=" ")
