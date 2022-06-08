a=int(input())
for b in range(1,a+1):
    c=int(input())
    if(c==0):
        print(1)
    elif(c==1):
        print(0)
    else:
        d=c//2
        e=c%2
        r=""
        if(e==1):
            g=str(4)
            r=r+g
        for f in range(1,d+1):
            h=str(8)
            r=r+h
        print(r)
