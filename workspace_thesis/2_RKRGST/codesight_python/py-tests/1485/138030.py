import math
def p1(n):
    nu=0
    while n>0:
        dig=n-(n//10)*10
        n=n//10
        nu=dig+nu*10
    return(nu)
x=int(input())
while x!=0:
    c=0
    for i in range(x):
        n=int(input())
        aux=n
        z=p1(n)
        if z==aux:
            c=c+1
    print(c)
    x=int(input())
