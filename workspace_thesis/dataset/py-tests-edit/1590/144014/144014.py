while True:
    a,b,c=map(int,input().split())
    s=0
    for d in range(1,a+1):
        d=str(d)
        h=int(d)
        s2=0
        for i in d:
            i=int(i)
            s2=s2+i
        if s2 in range(b,c+1):
            s=s+h
    print(s)
