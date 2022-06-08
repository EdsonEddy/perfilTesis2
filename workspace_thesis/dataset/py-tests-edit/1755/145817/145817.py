cas=int(input())
while cas>0:
    x,n=map(int,input().split())
    l=[1]*n
    s=0
    for i in range(x-1):
        for j in range(i,n):
            s=s+l[j]
        n=n+1
        l.append(s)
        s=0
    print(l[x])
    cas-=1