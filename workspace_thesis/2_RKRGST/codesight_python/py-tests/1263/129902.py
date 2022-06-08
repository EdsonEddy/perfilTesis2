while True:
    a,b=map(int,input().split())
    c=0
    x=0
    li=1
    while x!=b:
        c=c+1
        x=(li+a)//2
        if x<b:
            li=x+1
        else:
            a=x-1
        while x==b:
            print(c)
            break