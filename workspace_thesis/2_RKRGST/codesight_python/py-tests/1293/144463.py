x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    s=0
    for j in range(a,b+1):
        s=s+l[j]
    print(s)