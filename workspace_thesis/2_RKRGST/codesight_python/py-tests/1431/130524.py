n,m,a,b=map(int,input().split())
s=0
if n==1:
    print(a)
else:
    if(n==2):
        print(b)
    else:
        n=n-2
        for i in range(n):
            s=a+b
            a,b=b,s
        b=b%m
        print(b)

