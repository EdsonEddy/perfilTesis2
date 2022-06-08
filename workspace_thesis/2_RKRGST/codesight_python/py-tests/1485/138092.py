from sys import stdin
import math
cd=0

def espalindromo(n):
    a=int((math.log10(n))+1)
    k=n
    c=0
    for i in range(1,a+1):
        b=n%10
        n=n//10
        c=c*10+b
    if c==k:
        return(True)
    else:
        return(False)

for h in stdin:
    h=int(h)
    for j in range(h):
        n=int(input())
        if espalindromo(n)==True:
            cd=cd+1
    print (cd)
    cd=0