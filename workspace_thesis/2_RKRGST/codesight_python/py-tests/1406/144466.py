while 1>0:
    n=int(input())
    s=0
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    g=(sum(a)+sum(b))/len(a)
    for i in range(len(a)):
        d=a[i]+b[i]
        if d<g:
            s=s+1
    print(s)