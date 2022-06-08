while True:
    a,b=map(int,input().split())
    e=0
    i=0
    f=0
    c=0
    while True:
        f=2**i*a
        g=a+f
        e=e+g-a
        i=i+1
        c=c+1
        if e==b:
            break
    print(c)