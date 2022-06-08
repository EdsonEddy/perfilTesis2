n=int(input())
for i in range(0,n,1):
    a,b=map(int,input().split())
    r=0
    while(b>0):
        r=b
        b=a%b
        a=r
    print(a)
