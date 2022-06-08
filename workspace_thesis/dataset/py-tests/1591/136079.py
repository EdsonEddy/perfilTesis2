n =int(input())
for i in range (n):
    x=int(input())
    y=x
    p=1
    nn=0
    while (y>0):
        dig=y%10
        y=y//10
        if (dig==2 or dig==3 or dig==5 or dig==7 ):
            nn=dig*p+nn
            p=p*10
    if(nn>0):
        print(nn)
    else:
        
        print(-1)