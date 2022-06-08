while 1>0:
    a,b,c=map(int,input().split())
    g=0
    for d in range(1,a+1):
        d=str(d)
        h=int(d)
        f=0
        for e in d:
            e=int(e)
            f=f+e
        if f in range (b,c+1):
            g=g+h
    print(g)