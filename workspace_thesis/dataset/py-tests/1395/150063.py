from sys import stdin
import math
for n in stdin:
    n=int(n)
    t=(math.log10(2*math.pi*n)/2+n*(math.log10(n/math.e)))+1
    t=int(t)
    print(t)