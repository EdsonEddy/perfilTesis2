n=int(input())
c=0
for i in range(1,n+1,1):
    r,p=map(int,input().split())
    while(r>=3 and p>=2):
        r=r-3
        p=p-2
        c=c+1
    d=r+p
    print(c,d)
    c=0