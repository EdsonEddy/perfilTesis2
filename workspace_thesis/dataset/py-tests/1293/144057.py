n=int(input())
for n in range(n):
    a,b=map(int,input().split())
    k=input().split()
    x=k[a:b+1]
    s=0
    for g in x:
        s=s+int(g)
    print(s)