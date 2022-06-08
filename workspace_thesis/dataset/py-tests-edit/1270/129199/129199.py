n=int(input())
for i in range (1,n+1):
    a=int(input())
    if(a==0):
        print(1)
    elif(a==1):
        print(0)
    else:
        b=a//2
        r=""
        e=a%2
        if(e==1):
            g=str(4)
            r=r+g
        for j in range(1,b+1):
            h=str(8)
            r=r+h
        print(r)