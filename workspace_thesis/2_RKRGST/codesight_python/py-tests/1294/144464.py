x=int(input())
for i in range(x):
    a,b,c=map(int,input().split())
    l=list(map(int,input().split()))
    s=0
    for j in range(b,c+1):
        s=s+l[j]
    print(s)