from math import log10
def comp(a):
    n=a
    r=1
    s=0
    while r==1:
        b=0
        while n!=0:
            d=n%10
            d=d**2
            n=n//10
            b=b+d
        n=b
        cd=int(log10(n))+1
        if cd==1:
            r=0
    if n==1:
        s=1
    else:
        s=0
    return (s)
n=int(input())
for i in range(n):
    a=int(input())
    s=comp(a)
    if s==1:
        print('Feliz')
    else:
        print('Triste')