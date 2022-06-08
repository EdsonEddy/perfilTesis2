n=int(input())
for i in range(1,n+1):
    x=int(input())
    if(x==0):
        print(1)
    elif(x==1):
        print(0)
    else:
        d=x//2
        e=x%2
        r=""
        if(e==1):
            g=str(4)
            r=r+g
        for y in range (1,d+1):
            h=str(8)
            r=r+h
        print(r)