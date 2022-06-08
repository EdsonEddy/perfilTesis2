def tribo(i):
    a,b,c,d=-1,0,2,0
    for j in range(i):
        d=a+b+c
        a,b,c=b,c,d
    return(d)
def fibo(i):
    a,b,c=1,0,0
    for j in range(i):
        c=a+b
        a,b=b,c
    return(c)
def primo(i):
    p, c, k = 2, 1, 2
    while c <= i:
        if p % k != 0 and k <= p // 2:
            k = k + 1
        else:
            if k > (p // 2):
                # print(p)
                c = c + 1
            p = p + 1
            k = 2
    return(p - 1)
import sys
for l in sys.stdin:
    n,x=map(int,l.split())
    d=float(0)
    s=float(0)
    sig=1
    for i in range(1,n+1):
        f,t,p=fibo(i),tribo(i),primo(i)
        d=sig*((t*(x**p))/f)
        s=s+d
        sig=sig*-1

    print("{0:.2f}".format(s))