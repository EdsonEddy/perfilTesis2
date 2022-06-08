while True:
    a,b,c,d=map(int,input().split())
    if a==0 and b==0 and c==0 and d==0:
        break
    else:
        r=a/b
        x=c/d
        if x==r:
            print("=")
        else:
            print("!=")