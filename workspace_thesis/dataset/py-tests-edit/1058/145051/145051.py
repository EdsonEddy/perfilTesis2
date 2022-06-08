k=int(input())
for i in range(1,k+1):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    print(*l)
