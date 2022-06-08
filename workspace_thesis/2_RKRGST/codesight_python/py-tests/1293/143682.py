x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    l=[int(x) for x in input().split()]
    if a < len(l) and b < len(l):
        y=l[a:b+1]
        print(sum(y))