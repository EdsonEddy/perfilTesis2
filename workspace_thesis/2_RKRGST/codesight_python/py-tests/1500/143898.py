g=int(input())
v,d=[],[]
if g!=0:
    m=list(map(int,input().split()))
    for i in range(g):
        v.append(m[i])
    for j in reversed(v):
        d.append(j)
    if v==d:
        print("SI")
    else:
        print("NO")