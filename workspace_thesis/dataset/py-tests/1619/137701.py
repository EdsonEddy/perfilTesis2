while True:    
    a,b=map(int,input().split())
    x,y,z=a+b,a-b,a*b
    r=max(x,y,z)
    print(r)