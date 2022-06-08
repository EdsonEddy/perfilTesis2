n=int(input())
l=list(map(int,input().split()))
v=[]
y=[]
s=0
for i in l:
    if i not in v:
        v.append(i)
        y.append(l.count(i))
g=y.index(max(y))
for i in range(len(y)):
    if i!=g:
        s=s+y[i]
print(s)
