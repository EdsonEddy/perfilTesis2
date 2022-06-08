n,k=map(int,input().split())
if 0<=n<=1*(10**18):
    c=0
    x=0
    while n > 0:
        y=n % 10
        n=n // 10
        x=x * 10+y
        c=c+1
    z=0
    while x > 0:
        y= x % 10
        x= x // 10
        z= z + 1
        if z == k:
            print(str(c)+" "+str(y))
else:
    print("reset")