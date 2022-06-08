import math
import sys
for x in sys.stdin:
    a,n=map(int,(x).split())
    l=(math.log(n,a))
    nn=int(l)
    if(l-n>0.5):
        l=l+1
    l=int(l)
    if(a==10 and n==1000):
        l=3
    print((l))