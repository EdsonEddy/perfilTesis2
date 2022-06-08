n=int(input())
s=list(map(int,input().split()))
s.sort()
d=[]
can=[]
c=0
suma=1
for i in range(0,n-1,1):
    x=s[i]
    y=s[i+1]
    if x not in d:
        d.append(x)
    if x==y:
        suma+=1
    else:
        can.append(suma)
        suma=1
can.append(suma)
res=max(can)
r=0
for j in can:
    if j!=res:
        r+=j
print(r)
