c,p=map(int,input().split())
while c!=0 and p != 0:
    h=(c*2)-(p*1)
    h1=h/-2
    g=(1*p)-(4*c)
    g1=g/-2
    if h1 <0 or g1 < 0 or h%-2!=0 or g%-2!=0:
        print(-1)
    else:
        print(int(g1),int(h1))
    c,p=map(int,input().split())