while True:
    a,b=map(str,input().split())
    a=int(a)
    a=a%26
    m="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    s=""
    for d in b:
        if d=="_":
            d=" "
        elif d in n:
            c=n.find(d)
            f=c+a
            g=m[f]
            d=g
        s=s+d
    print(s)