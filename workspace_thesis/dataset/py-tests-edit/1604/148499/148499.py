while 1>0:
    a,b=map(int,input().split())
    s=0
    a=str(a)
    a=a[::-1]
    for i in range(len(a)):
        s=s+int(a[i])*b**i
    print(s)
