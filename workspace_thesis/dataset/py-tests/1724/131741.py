while(1>0):
    a,b=map(int,input().split())
    y=0
    z="posible"
    for c in range(1,b+1):
        y=y+c
        if(y>a):
            z="imposible"
            break
    print(z)