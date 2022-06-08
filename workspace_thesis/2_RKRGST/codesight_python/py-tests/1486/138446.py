import sys
def serieFibonacci(n):
    a=0
    b=1
    c=1
    for i in range (n-1):
        c=a+b
        a=b
        b=c
    return (c)        

for m in sys.stdin:
    c=1
    m=int(m)
    for i in range (1,m+1):
        if i%2 == 0:
            print (i)
        else:
            print (serieFibonacci(c))
            c=c+1
