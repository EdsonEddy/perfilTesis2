from sys import stdin
def invierte(n):
    m=0
    while n>0:
        d=n%10
        m=m*10+d
        n=n//10
    return m

for a in stdin:
    a=int(a)
    c=0
    x=0
    while c<a:
        n=int(input())
        r=invierte(n)
        if(r==n):
            x=x+1
        c=c+1
    print(x)