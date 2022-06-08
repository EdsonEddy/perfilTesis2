n=int(input())
for i in range(1,n+1,1):
    a=int(input())
    b=list(map(int,input().split()))
    b.sort()
    print(*b)