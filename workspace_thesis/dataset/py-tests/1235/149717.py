n=int(input())
v= list(map(int, input().split()))
for i in range(len(v)-1):
    for j in range(i,-1,-1):
        if v[j+1]<v[j]:
            aux=v[j+1]
            v[j+1]=v[j]
            v[j]=aux
s,r=0,0
for i in range(len(v)):
    if i< (len(v)//2)+1:
        s=s+v[i]
    else:
        r=r+v[i]
p=abs(r-s)
print(p)