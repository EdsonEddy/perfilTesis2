import sys
import math
def esPalindromo(n):
    c=0
    f=n
    nn=0
    while n>0:
        d=n%10
        n=n//10
        nn=nn*(10)
        nn=nn+d
    return nn

for m in sys.stdin:
    c=0
    m=int(m)
    for i in range (m):
        x=int(input())
        if (x==esPalindromo(x)):
            c=c+1
    print (c)
            
    
