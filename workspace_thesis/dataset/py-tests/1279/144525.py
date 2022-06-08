while True:
    a,b=map(str,input().split())
    r=str.upper(b)
    l="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    g=len(l)
    n=len(b)
    s=""
    d="_"
    for i in range(0,n,1):
        t=l.find(r[i])
        c=t+int(a)
        if c>=g:
            c=c%g
        if t==-1:
            if r[i]==d:
                s=s+" "
            else:
                s=s+r[i]
        else:
            s=s+l[c]
    print(s)

