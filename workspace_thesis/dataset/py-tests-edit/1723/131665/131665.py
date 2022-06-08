while True:
    n,m=map(int,input().split())
    c=0
    h=0
    while n>0 and m>0:
        c=n%10
        d=m%10
        n=n//10
        m=m//10
        if c!= d:
            h=h+1
    if h>1:
        print("lentes")
    else:
        print("feliz")