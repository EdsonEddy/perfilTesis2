z=int(input())
for u in range(z):
    n=int(input())
    y=2
    p=0
    o=0
    cont=2
    n=n%6
    for i in range(n+1):
        g=(y**i)*2
        g=str(g)
    for j in g:
        p=p+int(j)
    p=str(p)
    for q in p:
        o = o + int(q)
    print(o)




