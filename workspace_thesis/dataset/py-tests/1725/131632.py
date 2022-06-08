while(1>0):    
    a,b=map(int,input().split())
    y=0
    for c in range (0,9999999999999):
        d=a*2**c
        y=y+d
        if(y==b):
            print(c+1)
            break