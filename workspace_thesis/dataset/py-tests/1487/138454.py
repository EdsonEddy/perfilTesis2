import sys
import math
def esPrimo(n):
    if n==1:
        c=1
    else:    
        l=int (math.sqrt(n))
        c=0
        for i in range (2,l+1,1):
            if n%i==0:
                c=c+1
    return c

for m in sys.stdin:
    m=int(m)
    c=esPrimo(m)
    if c>0:
        print ("NO ES PRIMO")
    else:
        print ("ES PRIMO")    