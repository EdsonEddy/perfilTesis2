while True:
    k, t = map(int, input().split())
    a = 0
    e=1
    w = 0
    c=0
    while a==0:
        p=k*e
        w=p+w
        e=e*2
        c=c+1
        if w==t:
            a=1
    print(c)