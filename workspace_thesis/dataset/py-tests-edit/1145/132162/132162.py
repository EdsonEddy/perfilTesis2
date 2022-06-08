m=int(input())
for i in range(1,m+1,1):
    n=int(input())
    a=0
    b=1
    if(1<=n and n<=200):
        if(n==1):
            print(1)
        else:
            for i in range(2,n+1,1):
                c=a+b
                a=b
                b=c
            print(c)