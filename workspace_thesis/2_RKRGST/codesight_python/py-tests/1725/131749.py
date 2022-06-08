while 1>0:
    n,m=map(int,input().split())
    c=0
    c2 = 0
    if n==m:
        c=c+1
        print(c)
    else:
        b=0
        while b!=m:
                b=b+((2**c2)*n)
                c2=c2+1
                c=c+1
        print(c)