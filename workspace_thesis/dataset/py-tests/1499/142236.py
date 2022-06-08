x=int(input())
c=1
v=list(map(int,input().split()))
m=v[0]
sw=0
for i in range(1,len(v)):
    c=c+1
    if v[i]>=m:
        m=v[i]
    else:
        u=v[i]
        break   
for k in range(c,len(v)):
    if v[k]<u:
        u=v[k]
    else:
        sw=1
        break
if sw==0:
    print("SI")
else:
    print("NO")
        