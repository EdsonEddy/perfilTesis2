m,n=map(int,input().split())
l=list(map(int,input().split()))
v=[0]*m
for i in range(len(l)):
    v[l[i]]=1
if v[n]==1:
    print("SI")
else:
    print("NO")