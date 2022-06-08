while True:   
    h1,m1,h2,m2=map(int,input().split())
    nm=m2-m1
    a=nm/60
    nm=nm%60
    nh=h2-h1
    nh=nh+a
    nh=int(nh%24)
    print(nh,nm)