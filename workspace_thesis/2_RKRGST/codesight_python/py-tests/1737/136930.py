import math
import sys
for x in sys.stdin:
    n=int(x)
    f=1
    if n!=0:
        for i in range(n):
            print(f,end="")
            f=f*10+1
            if i<n-1:
                print(end=" ")
            else:
                print()
    else:
        print("error")
