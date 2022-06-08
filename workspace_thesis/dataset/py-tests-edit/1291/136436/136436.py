while 1>0:
    l=list(map(int,input().split()))
    b=l[len(l)-1]
    s=0
    if b==0:
        for i in l:
            s=s+i
        print(s)