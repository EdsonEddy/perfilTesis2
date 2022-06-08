w=0
while w==0:
    n1, d1, n2, d2=map(int,input().split())
    if n1==n2==d1==d2==0:
        w=1
    else:
        if n1>=n2:
            n=n1%n2
        else:
            n=n2%n1
        if d1>=d2:
            d=d1%d2
        else:
            d=d2%d1
        if d==n==0:
            print("=")
        else:
            print("!=")