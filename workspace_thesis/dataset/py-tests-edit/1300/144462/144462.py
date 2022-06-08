while 1>0:
    
    n=int(input())
    s=0
    a=list(map(int,input().split()))
    for i in a:
        if i==a[len(a)-1]:
            s=s+1
    print(s)