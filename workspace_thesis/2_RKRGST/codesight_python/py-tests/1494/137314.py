def primo(p):
    k=2
    sw=0
    while sw==0:
        while p % k != 0 and k <= p // 2:
            k = k + 1
        if k > p // 2:
            sw=1
        else:
            p = p + 1
            k = 2
    return p

while 1>0:
    n,x=map(int,input().split())
    s=0
    a=1
    b=0
    f=a+b
    p=2
    for i in range(n):
        den=primo(p)
        p=den
        s=s+(f/(den*x))
        a=b
        b=f
        f=a+b
        p=p+1
    print("{0:.2f}".format(s))