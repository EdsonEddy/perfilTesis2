pokemon=1
while(pokemon==1):
    a,b=map(int,input().split())
    if(a==0 and b==0):
        break
    else:
        if((b%2!=0) or (a*4<b) or (a>b)):
            print(-1)
        else:
            y=(b-2*a)//2
            x=(4*a-b)//2
            if(x<0 or y<0):
                print(-1)
            else:
                print(x,y)