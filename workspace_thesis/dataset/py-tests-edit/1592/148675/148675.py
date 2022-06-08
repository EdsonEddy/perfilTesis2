n=int(input())
x=list(map(int,input().split()))
may=0
for i in range(n):
    y=x.count(x[i])
    if(y>may):
        may=y
print(n-may)