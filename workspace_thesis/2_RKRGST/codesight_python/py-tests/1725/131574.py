while 1>0:
    p,t=map(int,input().split())
    c=0
    c2 = 0
    if p==t:
        c=c+1
        print(c)
    else:
        s=0
        while s!=t:
                s=s+((2**c2)*p)
                c2=c2+1
                c=c+1
        print(c)