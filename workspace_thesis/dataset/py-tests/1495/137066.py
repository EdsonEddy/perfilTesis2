while 1>0:
    a,b=map(int,input().split())
    def f(x):
        b=1
        c=0
        z=[]
        for d in range(1,x+1):
            y=b+c
            b=c
            c=y
            z.append(y)
        return z
    def g(x):
        b=1
        c=1
        e=1
        z=[1]
        for d in range(1,x):
            if d==2:
                y=b+c+e+1
            else:
                y = b + c + e
            b=c
            c=e
            e=y
            z.append(y)
        return z
    def p(x):
        a=0
        b=0
        c=[]
        while 1>0:
            a=a+1
            if a==2 or a==3 or a==5 or a==7 or a==11 or a==13 or a==17 or a==19 or (a%2!=0 and a%3!=0 and a%5!=0 and a%7!=0 and a%11!=0 and a%13!=0 and a%17!=0 and a%19!=0) and a!=1:
                b=b+1
                c.append(a)
            if b==x:
                break
        return c
    c=f(a)
    d=p(a)
    j=g(a)
    f=0
    i=0
    for e in range (0,a):
        i=i+1
        if i%2==0:
            f=f-(((j[e])*(b**d[e]))/c[e])
        else:
            f = f + (((j[e]) * (b ** d[e])) / c[e])
    print("{0:.2f}".format(f))