while True:
    tu,i,m,c=0,0,1,0
    k,t = map(int,input().split())
    while(tu!=t):
        if i == 0:
            tu=tu+k
            c=c+1
            if tu==t:
                break
        i=i+1
        m=k*(2**i)
        tu=tu+m
        c=c+1
    print(c)