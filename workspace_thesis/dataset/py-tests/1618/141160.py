t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    if 6<=n and m<=10000:
        n=n//3
        m=m//3
        s=n*m
        print(s)
