while True:
    x,k=map(int,input().split())
    z=x
    y=x
    nx=0
    cd=0
    c=0
    while z!=0:
        dig=z//1%10
        cd=cd+1
        z=(z//10)
    while y>0:
        d=y-(y//10)*10
        nx=nx*10+d
        y=y//10
    while k!=c:
        c=c+1
        m=nx%10
        nx=nx//10
    print(cd,m)    
