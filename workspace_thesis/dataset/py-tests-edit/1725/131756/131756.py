while 1>0:
    n,m=map(int,input().split())
    a=0
    a2 = 0
    if n==m:
        a=a+1
        print(a)
    else:
        b=0
        while b!=m:
                b=b+((2**a2)*n)
                a2=a2+1
                a=a+1
        print(a)