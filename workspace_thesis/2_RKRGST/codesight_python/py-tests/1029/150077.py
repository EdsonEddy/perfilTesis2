while 1>0:
    l=list(map(int,input().split()))
    l=sorted(l)
    l=l[::-1]
    s=0
    d=0
    for i in range(len(l)):
        if i%2==0:
            s=s+l[i]
    
        else:
            d=d+l[i]
    print(abs(s-d))