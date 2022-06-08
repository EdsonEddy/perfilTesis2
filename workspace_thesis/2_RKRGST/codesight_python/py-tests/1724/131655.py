while True:
    a, b = map(int, input().split())
    if b==1:
        print("posible")
    else:
        r=0
        for i in range (1,b,1):
            r=r+i
        res=a-r
        if res>i:
            print("posible")
        else:
            print("imposible")
