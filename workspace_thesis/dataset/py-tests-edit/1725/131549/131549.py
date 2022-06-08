while 2>0:
    a,b=map(int,input().split())
    c=0
    s=0
    for i in range(10000000):
        r=a*2**i
        s=s+r
        c = c + 1
        if s==b:
            print(c)
            break