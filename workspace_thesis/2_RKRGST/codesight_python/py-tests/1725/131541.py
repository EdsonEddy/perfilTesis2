while True:
    a,b=map(int,input().split())
    c=1
    d=a
    x=2
    if a!=b:
        while a!=b:
            a=a+x*d
            c=c+1
            x=x*2
        print(c)
    else:
        print(c)
