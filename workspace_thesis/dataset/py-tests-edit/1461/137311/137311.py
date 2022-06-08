from math import log10
def comp(x):
    n=x
    r=1
    sw=0
    while r==1:
        s=0
        while n!=0:
            d=n%10
            d=d**2
            n=n//10
            s=s+d
        n=s
        cd=int(log10(n))+1
        if cd==1:
            r=0
    if n==1:
        sw=1
    else:
        sw=0
    return (sw)
n=int(input())
for i in range(n):
    x=int(input())
    sw=comp(x)
    if sw==1:
        print('Feliz')
    else:
        print('Triste')