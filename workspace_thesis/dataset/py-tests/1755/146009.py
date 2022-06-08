k=int(input())
for k in range(k):
    a,b=map(int,input().split())
    z=[1]*b
    g=0
    for i in range(a):
        c=0
        for u in range(b):
            c=c+z[u+g]
        g=g+1
        z.append(c)
    print(z[a])