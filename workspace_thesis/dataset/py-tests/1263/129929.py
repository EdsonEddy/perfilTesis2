while True:
    a,b=map(int,input().split())
    x=0
    lim=1
    c=0
    while x!=b:
        c+=1
        x=(lim+a)//2
        if x<b:
            lim=x+1
        else:
            a=x-1
        while x==b:
            print(c)
            break