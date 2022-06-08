while(True):
    x=int(input())
    c=0
    v=list(map(int,input().split()))
    for k in range(x):
            if v[k]>=v[0]:
                c=c+1
    m= v[0]*c
    for i in range (1,x):
        c1=0
        for k in range(x):
            if v[k]>=v[i]:
                c1=c1+1
        b=v[i]*c1
        if b>m:
            m=b
    print(m)  