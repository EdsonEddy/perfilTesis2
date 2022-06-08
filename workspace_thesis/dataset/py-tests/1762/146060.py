while 1>0:

    n=int(input())
    l=list(map(int,input().split()))
    s=[0]*len(l)
    l=sorted(l)
    g=0
    d=0
    h=0
    for i in l:
        if i not in s:
            s[g]=i
            g=g+1
            d=d+h//2
            h=1

        else:
            h=h+1

    rt=0
    for i in s:
        df=0
        for j in l:
            if j==i:
                df=df+1
        rt=rt+df//2
    print(rt)
