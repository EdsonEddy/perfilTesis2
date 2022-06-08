while 1>0:
    p,t=map(int,input().split())
    a=0
    a2=0
    if p==t:
        a=a+1
        print(a)
    else:
        b=0
        while b!=t:
                b=b+((2**a2)*p)
                a2=a2+1
                a=a+1
        print(a)