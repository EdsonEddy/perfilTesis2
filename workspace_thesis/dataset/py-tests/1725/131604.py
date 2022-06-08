k,t=map(int,input().split())
while k>0 and t>0:
    m=1
    c=0
    a=0
    r=0
    while a==0:
        p=k*m
        r=p+r
        m=m*2
        c=c+1
        if r==t:
            a=1
    print(c)
    k, t = map(int, input().split())