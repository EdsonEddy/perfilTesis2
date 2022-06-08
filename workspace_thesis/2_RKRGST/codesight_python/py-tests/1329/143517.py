n,a,b=map (int,input().split())
l= input()
v=list(map(int,l.split()))
v1=v[:a]
v2=v[a:b+1]
v3=v[b+1:]
v2.sort()
v=v1+v2+v3
for i in range(len(v)):
    print(v[i],end="")
    if i+1!=len(v):
        print(end=" ")
