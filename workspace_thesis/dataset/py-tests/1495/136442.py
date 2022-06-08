while True:
    PRIMOS=[2, 3, 5, 7, 11]
    primos=iter(PRIMOS)
    fib=[1, 1, 2, 3, 5]
    fibo=iter(fib)
    tri=[1,3,6,10,19]
    trif=iter(tri)
    n,x=map(int,input().split())
    if(1<=n and n<=5):
        g=0
        sig=1
        for i in range(1,n+1,1):
           h=x**next(primos)
           b=next(trif)*h
           c=(b/next(fibo))*sig
           g=g+c
           sig=sig*(-1)
        print('{:.2f}'.format(g))
        g=int(0)
    