while True:
    pri=[2, 3, 5, 7, 11]
    primos=iter(pri)
    f=[1, 1, 2, 3, 5]
    fb=iter(f)
    r=[1,3,6,10,19]
    t=iter(r)
    n,x=map(int,input().split())
    if(1<=n and n<=5):
        g,s=0,1
        for i in range(1,n+1,1):
           h=x**next(primos)
           b=next(t)*h
           c=(b/next(fb))*s
           g=g+c
           s=s*(-1)
        print('{:.2f}'.format(g))
        g=int(0)