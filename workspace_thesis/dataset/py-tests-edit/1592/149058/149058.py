def llenar(x):
    v=[]
    c=0
    for i in x:
        v.insert(c,int(i))
    v.sort()
    return v

n=int(input())
x=input().split()
v=llenar(x)
c=0
m=0
while c<n:
    e = v[c]
    con=v.count(e)
    c = (c + con)
    if con>m:
        m=con
print(n-m)