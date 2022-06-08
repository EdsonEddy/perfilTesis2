import math
import sys
 
for i in sys.stdin:
    i = int(i)
    for j in range(i):
        n=int(input())
    #    cd=int(math.log(n,10))
        y=n
        s=0
        while n>0:
            d=n%10
            n=n//10
            f=1
            for j in range(1,d+1,1):
                f=f*j
            s=s+f
        if y==s:
            print("Y")
        else:
            print("N")