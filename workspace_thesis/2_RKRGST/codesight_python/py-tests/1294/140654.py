def suma (v,a,b):
    res=0
    for i in range(a,b+1):
        res+=int(v[i])
    return res
t=int(input())
for i in range(t):
    n,a,b=map(int,input().split())
    v=input().split()
    print(suma(v,a,b))