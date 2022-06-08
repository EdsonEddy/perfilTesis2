x=int(input())
for i in range(x):
    m,a,b=map(int,input().split())
    l=[int(x) for x in input().split()]
    if a < m and b < m and len(l)==m:
        y=l[a:b+1]
        print(sum(y))

