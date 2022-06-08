p=int(input())
for i in range (0,p,1):
    n,k=map(int,input().split())
    print(k*(n*(n+1)//2))
