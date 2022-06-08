def primo(p):
    k=2
    sw=0
    while sw==0:
        while p % k != 0 and k <= p // 2:
            k = k + 1
        if k > p // 2:
            sw=1
        else:
            p = p + 1
            k = 2
    return p

while 1>0:
    n,x=map(int,input().split())
    s=0
    a=1
    b=0
    f=a+b
    p=2
    a3=-1
    b3=0
    c3=2
    f3=a3+b3+c3
    s1=1
    s2=0
    sf=s1+s2
    c=1
    for i in range(n):
        prim=primo(p)
        p=prim
        numerador=f3*(x**p)
        denominador=f
        a=b
        b=f
        f=a+b
        a3=b3
        b3=c3
        c3=f3
        f3=a3+b3+c3
        p=p+1
        if c<=sf:
            s=s+(numerador/denominador)
            c=c+1
        else:
            s=s-(numerador/denominador)
            s1 = s2
            s2 = sf
            sf = s1 + s2
            c=1
    print("{0:.2f}".format(s))