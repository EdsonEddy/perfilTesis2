t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    if (n+1)//2<k:
        print(2*(k-(n+1)//2))
    else:
        print(2*k-1)