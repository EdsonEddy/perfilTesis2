while 1>0:
    e=int(input())
    a=input().split()
    b=input().split()
    c=0
    for d in a:
        d=int(d)
        c=c+d
    for d in b:
        d=int(d)
        c=c+d
    c=c/e
    f=-1
    g=0
    for d in b:
        d=int(d)
        f=f+1
        if d+int(a[f])<c:
            g=g+1
    print(g)