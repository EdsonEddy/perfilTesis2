while True:
    primos=[2,3,5,7,11]
    fibo=[1,1,2,3,5]
    suma=[1,3,6,10,19]
    a,b=map(int,input().split())
    s=0
    sig=1
    for i in range(a):
        s=s+(sig*((suma[i]*b**primos[i])/fibo[i]))
        sig=sig*-1
    print("{0:.2f}".format(s))