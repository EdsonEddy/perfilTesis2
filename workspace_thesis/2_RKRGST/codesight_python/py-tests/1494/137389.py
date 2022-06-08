def primo(pr):
    k=2
    sw=0
    while sw==0:
        while pr % k != 0 and k <= pr // 2:
            k = k + 1
        if k > pr // 2:
            sw=1
        else:
            pr = pr + 1
            k = 2
    return pr

while 1>0:
    n,x=map(int,input().split())
    s=0
    a=1
    b=0
    f=a+b
    pr=2
    for i in range(n):
        den=primo(pr)
        pr=den
        s=s+(f/(den*x))
        a=b
        b=f
        f=a+b
        pr=pr+1
    print("{0:.2f}".format(s))