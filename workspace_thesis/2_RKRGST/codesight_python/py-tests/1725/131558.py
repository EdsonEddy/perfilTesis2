while True:
    k,t=map(int,input().split())
    c=0
    s=0
    for i in range (10000000):
        r=k*2**i
        s=s+r
        c=c+1
        if s==t:
            print(c)
            break
