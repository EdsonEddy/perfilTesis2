while True:
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()
    s=0
    c=-1
    for i in range(0,n,1):
        m=int(a[i])*int(b[c])
        s+=m
        c-=1
    print(s)