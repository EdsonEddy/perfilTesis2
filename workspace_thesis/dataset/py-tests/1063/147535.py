def modulo(n,m):
    d=n%m
    return d
f=int(input())
for i in range(f):
    n,m=map(int,input().split())
    s=modulo(n,m)
    print(s)