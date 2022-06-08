while True:
    a,b=map(int,input().split())
    d=len(str(a))
    r=d-1
    x=str(a)
    z=str(b)
    c=0
    for i in range (0,d,1):
        x1=x[i]
        z1=z[i]
        if x1==z1:
            c=c+1
    if c==r or c==d:
        print("feliz")
    else:
        print("lentes")
