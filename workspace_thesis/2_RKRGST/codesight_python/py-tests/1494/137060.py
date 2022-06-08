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
    f=0
    for e in range (0,a):
        f=f+(c[e]/(d[e]*b))
    print("{0:.2f}".format(f))