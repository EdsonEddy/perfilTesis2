n,m = map(int,input().split())
l = list(tuple(map(int,input().split())))
lis=[]
x=None
l.sort()
for i in range(m):
    lis.append(l.count(i))
for j in range(m):
    if lis[j]<2:
        x=True
    else:
        x=False
        break
if x!=False:
    print("SI")
else:
    print("NO")