while 1>0:
    k=list(map(int,input().split()))
    b=k[len(k)-1]
    s=0
    if b==0:
        for t in k:
            s=s+t
        print(s)