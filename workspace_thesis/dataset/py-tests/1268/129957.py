c,d=map(int,input().split())
while c!=0 and d!=0:
    h=(c*2)-d
    h1=h/-2
    g=d-(4*c)
    g1=g/-2
    if h1<0 or g1<0 or h%-2!=0 or g%-2!=0:
        print("-1")
    else:
        print(int(g1),int(h1))
    c,d=map(int,input().split())