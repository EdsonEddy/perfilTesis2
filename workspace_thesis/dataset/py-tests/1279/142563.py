while 1>0:
    a="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b,d=map(str,input().split())
    d=d.upper()
    b=int(b)
    b=b%26
    r=""
    for c in d:
        if (c=="_"):
            c=" "
        if c in a:
            y=a.find(c)
            c=a[y+b]
        r=r+c
    print(r)