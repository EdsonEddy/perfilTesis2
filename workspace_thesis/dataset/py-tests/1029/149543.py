while 1:
    n=map(int,input().split())
    ln=list(n)
    le=sorted(ln)
    c1=0
    c2=0
    for i in range (len(le)-1,-1,-1):
        if i%2==0:
            c1+=int(le[i])
        else:
            c2+=int(le[i])
    if c2>c1 :
        re=c2-c1
    else:
        re = c1 - c2

    print(re)

