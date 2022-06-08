while 1>0:
    n=int(input())
    c=1
    f=0
    a = 1
    b = 0
    while c<=n:
        f=a+b
        a=b
        b=f
        c=c+1
    print(f)