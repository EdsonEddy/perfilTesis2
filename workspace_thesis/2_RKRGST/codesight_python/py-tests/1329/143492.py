n,a,b=map(int,input().split())#
l=input()
v=list(map(int,l.split()))#
#print(v)
v1=v[0:a]
v2=v[a:b+1]
v3=v[b+1:]
v2.sort()
v=v1+v2+v3
#print(v)
for i in range(len(v)):
    print(v[i], end="")
    if(i+1!=len(v)):
        print(end=" ")