from sys import stdin
def descomposicion(n):
    y=0
    while n>0:
        d=n%10
        n=n//10
        y=y*10+d
    return(y)

for n1 in stdin:
    n1=int(n1)
    c=0
    for i in range (1,n1+1):
        m=int(input())
        x=m
        r=descomposicion(m)
        if (x==r):
            c=c+1
    print(c)


